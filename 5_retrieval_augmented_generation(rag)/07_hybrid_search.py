import streamlit as st
import hybridhelper

st.set_page_config(layout="wide")
st.title("Advanced RAG: Hybrid Search | Hibrit Arama")
st.divider()

col_left, col_input, col_right = st.columns(3)

with col_left:
    st.empty()

with col_input:
    target_url = st.text_input(label="Hedef Web Adresini Giriniz", value="https://cbarkinozer.medium.com/reg%C3%BCle-edilmemi%C5%9F-yapay-zeka-teknolojileri-kullanman%C4%B1n-tehlikeleri-nelerdir-fa465da15491")
    original_prompt = st.text_input(label="Sorunuzu Giriniz:", value="Yapay zekayla ilgili muhtemel sorunları çözmek için yapılabilecek aksiyonlar nelerdir?")
    weight_options = ["%90 Karakter Bazlı", "%75 Karakter Bazlı", "%50 - %50", "%75 Semantik Bazlı", "%90 Semantik Bazlı"]
    retriever_weight = st.select_slider(label="Arama Yöntemlerinini Ağırlıklarını Belirleyin:", options=weight_options, value="%50 - %50")
    submit_btn = st.button(label="Gönder")
    st.divider()

with col_right:
    st.empty()

col_keyword, col_hybrid, col_semantic = st.columns(3)

with col_keyword:
    st.subheader("Karakter Bazlı Arama | BM25")
    st.divider()

with col_hybrid:
    st.subheader("Hibrit Arama")
    st.divider()

with col_semantic:
    st.subheader("Semantik Arama")
    st.divider()


if submit_btn:

    initial_documents = hybridhelper.load_and_split_documents(target_url=target_url)

    bm25_documents, bm25retriever = hybridhelper.get_relevant_documents_with_bm25(documents=initial_documents, query=original_prompt)

    faiss_documents, faissretriever = hybridhelper.get_relevant_documents_with_FAISS(documents=initial_documents, query=original_prompt)


    weight1 = 0.5
    if retriever_weight == "%90 Karakter Bazlı":
        weight1 = 0.9
    elif retriever_weight == "%75 Karakter Bazlı":
        weight1 = 0.75
    elif retriever_weight == "%50 - %50 Dengeli":
        weight1 = 0.5
    elif retriever_weight == "%75 Semantik Bazlı":
        weight1 = 0.25
    elif retriever_weight == "%90 Semantik Bazlı":
        weight1 = 0.1


    hybrid_search_documents = hybridhelper.get_relevant_documents_for_hybrid_search(
                                                        query=original_prompt, 
                                                        retriever1=bm25retriever, 
                                                        retriever2=faissretriever,
                                                        weight1=weight1,
                                                        weight2=1-weight1
                                                        )
    
    for keyword_doc in bm25_documents:
        col_keyword.warning(f"ID: {keyword_doc.metadata['doc_id']} || {keyword_doc.page_content}")
    
    for faiss_doc in faiss_documents:
        col_semantic.info(f"ID: {faiss_doc.metadata['doc_id']} || {faiss_doc.page_content}")

    for hybrid_doc in hybrid_search_documents:
        col_hybrid.success(f"ID: {hybrid_doc.metadata['doc_id']} || {hybrid_doc.page_content}")