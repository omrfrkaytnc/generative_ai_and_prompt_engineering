import streamlit as st
import multiqueryhelper

st.set_page_config(layout="wide")
st.title("Advanced RAG: Multi-Query | Sorgu Çeşitlendirme ile Bellek Genişletme Örneği")
st.divider()

col_input, col_docs, col_uniquedocs, col_rerankeddocs, col_response = st.columns([1,2,2,2,1])

with col_input:
    target_url = st.text_input(label="Hedef Web Adresini Giriniz", value="https://cbarkinozer.medium.com/reg%C3%BCle-edilmemi%C5%9F-yapay-zeka-teknolojileri-kullanman%C4%B1n-tehlikeleri-nelerdir-fa465da15491")
    original_prompt = st.text_input(label="Sorunuzu Giriniz:", value="Yapay zeka kullanımının yol açabileceği olumsuz durumlar nelerdir?")
    submit_btn = st.button(label="Gönder")
    st.divider()

with col_docs:
    st.empty()

with col_uniquedocs:
    st.empty()

with col_rerankeddocs:
    st.empty()

with col_response:
    st.empty()


if submit_btn:

    #Generate alternative queries and show
    with st.spinner("Soru havuzu oluşturuluyor..."):
        query_list = multiqueryhelper.generate_multi_query(original_prompt=original_prompt)

        col_input.markdown("SORU HAVUZU")
        st.divider()
        for query in query_list:
            col_input.markdown(f"**{query}**")
        
    #Get relevant documents for each query and show
    retrieved_documents = []

    for query in query_list:
        relevant_documents = multiqueryhelper.get_relevant_documents(target_url=target_url, prompt=query)

        retrieved_documents.extend(relevant_documents)
    
    col_docs.code(f"Bulunan Doküman Sayısı: {len(retrieved_documents)}")

    for retrieved_doc in retrieved_documents:
        col_docs.error(f"ID: {retrieved_doc.metadata['doc_id']} | {retrieved_doc.page_content}")
    
    #Get unique documents out of all retrieved documents and show
    final_documents = multiqueryhelper.get_unique_documents(retrieved_documents=retrieved_documents)

    col_uniquedocs.code(f"Bulunan Özgün Doküman Sayısı: {len(final_documents)}")

    for final_doc in final_documents:
        col_uniquedocs.warning(f"ID: {final_doc.metadata['doc_id']} | {final_doc.page_content}")
    
    #Get reranked documents and show
    reranked_docs = multiqueryhelper.get_reranked_documents(documents=final_documents, query=original_prompt)

    col_rerankeddocs.code(f"Yeniden Sıralanmış Doküman Sayısı: {len(reranked_docs)}")

    for reranked_doc in reranked_docs:
        col_rerankeddocs.info(f"ID: {reranked_doc.metadata['doc_id']} | {reranked_doc.page_content}")
    
    #Get AI response and show
    AI_Response  = multiqueryhelper.run_rag(relevant_documents=reranked_docs, prompt=original_prompt)
    col_response.code("NİHAİ YANIT")
    col_response.success(AI_Response)
