import streamlit as st
import hydehelper

st.set_page_config(layout="wide")
st.title("Advanced RAG: HyDE | Kurgusal Yanıt Üzerinden Bellek Genişletme")
st.divider()

col_input, col_dummy1, col_hyde, col_dummy2, col_normal = st.columns([4,1,8,1,8])

with col_input:
    target_url = st.text_input(label="Hedef Web Adresini Giriniz", value="https://cbarkinozer.medium.com/reg%C3%BCle-edilmemi%C5%9F-yapay-zeka-teknolojileri-kullanman%C4%B1n-tehlikeleri-nelerdir-fa465da15491")
    original_prompt = st.text_input(label="Sorunuzu Giriniz:", value="Yapay zeka kullanımının yol açabileceği olumsuz durumlar nelerdir?")
    submit_btn = st.button(label="Gönder")
    st.divider()

with col_dummy1:
    st.empty()

with col_hyde:
    st.subheader("HyDE")
    st.empty()

with col_dummy2:
    st.empty()

with col_normal:
    st.subheader("Standart RAG")
    st.empty()


if submit_btn:

    splitted_documents = hydehelper.load_and_split_documents(target_url=target_url)

    HyDE_query = hydehelper.generate_hypothetical_document(prompt=original_prompt)

    col_input.subheader("Kurgusal Yanıt:")
    col_input.info(HyDE_query)

    relevant_documents = hydehelper.get_relevant_documents(prompt=HyDE_query, documents=splitted_documents)

    AI_Response = hydehelper.run_rag(relevant_documents=relevant_documents, prompt=original_prompt)
    
    col_hyde.info(AI_Response)
    col_hyde.divider()
    for rel_doc in relevant_documents:
        col_hyde.info(f"{rel_doc.metadata['doc_id']} || {rel_doc.page_content}")
    
    relevant_documents_normal = hydehelper.get_relevant_documents(prompt=original_prompt, documents=splitted_documents)

    AI_Response_normal = hydehelper.run_rag(relevant_documents=relevant_documents_normal, prompt=original_prompt)    

    col_normal.success(AI_Response_normal)
    col_normal.divider()
    for rel_doc_n in relevant_documents_normal:
        col_normal.success(f"{rel_doc_n.metadata['doc_id']} || {rel_doc_n.page_content}")
    



