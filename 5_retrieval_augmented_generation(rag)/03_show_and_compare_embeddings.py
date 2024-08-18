from openai import OpenAI
import cohere
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_cohere = os.getenv("cohere_apikey")
my_key_hf = os.getenv("huggingface_access_token")

OpenAI_client = OpenAI(api_key=my_key_openai)
Cohere_client = cohere.Client(api_key=my_key_cohere)

sample_text ="Mevsimler neden oluşur? Dünya kendi etrafında döndüğü için mi?"

def get_openai_embeddings(text):
    response = OpenAI_client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    embeddings = response.data[0].embedding
    return embeddings

def get_cohere_embeddings(text):

    response=Cohere_client.embed(
        texts=[text], 
        input_type="classification", 
        model="embed-multilingual-v3.0"
    )
    return response.embeddings[0]

def get_hf_embeddings(text):

    model_id = "sentence-transformers/all-MiniLM-L6-v2"

    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {my_key_hf}"}

    response = requests.post(api_url, headers=headers, json={"inputs": text, "options":{"wait_for_model":True}})
    return response.json()

st.set_page_config("Embedding Modelleri Karşılaştırması", layout="wide")
st.title("Farklı Embedding Modelleriyle Vektörizasyon")
st.divider()

col_input, col_openai, col_cohere, col_hf = st.columns([2,1,1,1])

with col_input:
    text_input = st.text_area(label="Metin Girdisi", value=sample_text)
    submit_btn = st.button(label="Gönder")

    if submit_btn:

        with col_openai:
            st.header("OpenAI")
            openai_embeddings = get_openai_embeddings(text=sample_text)
            st.success(f"Vektördeki Boyut Sayısı: {len(openai_embeddings)}")
            for i, embedding in enumerate(openai_embeddings):
                col_openai.code(f"{i+1}: {embedding}")
        
        with col_cohere:
            st.header("Cohere")
            cohere_embeddings = get_cohere_embeddings(text=sample_text)
            st.info(f"Vektördeki Boyut Sayısı: {len(cohere_embeddings)}")
            for i, embedding in enumerate(cohere_embeddings):
                col_cohere.code(f"{i+1}: {embedding}")
        
        with col_hf:
            st.header("Hugging Face")
            hf_embeddings = get_hf_embeddings(text=sample_text)
            st.warning(f"Vektördeki Boyut Sayısı: {len(hf_embeddings)}")
            for i, embedding in enumerate(hf_embeddings):
                col_hf.code(f"{i+1}: {embedding}")