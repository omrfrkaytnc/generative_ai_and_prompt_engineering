import streamlit as st
import localhelper

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role": "system", "content":"You are a helpful assistant."})


def generate_response():

    if selected_provider == "LM Studio":

        AI_Response = localhelper.generate_with_lmstudio(chat_history=st.session_state.messages, temperature=0.7)
    
    if selected_provider == "Ollama":

        AI_Response = localhelper.generate_with_ollama(chat_history=st.session_state.messages, temperature=0.7)
    
    return AI_Response



st.header("Sohbet Botu: Yerelde Açık Kaynak Model İşletimi")
st.divider()

st.sidebar.subheader("Yerel İşletim Türü Seçiniz:")
st.sidebar.divider()
selected_provider = st.sidebar.selectbox(label="Yerel İşletim Türü:", options=["LM Studio", "Ollama"])

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Please enter your message"):

    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role":"user", "content": prompt})

    with st.spinner("Yapay Zeka yanıtlıyor..."):
        response = generate_response()
    
    st.chat_message("assistant").markdown(response)

    st.session_state.messages.append({"role":"assistant", "content": response})
