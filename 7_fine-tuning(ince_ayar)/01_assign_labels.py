import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

my_key_google = os.getenv("google_apikey")

llm_gemini = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=my_key_google)

system_prompt = """Sen bir Türk edebiyatı uzmanısın. Türk şiir literatürünü çok iyi biliyorsun.
Özellikle de Orhan Veli şiirlerini çok iyi biliyorsun.
Sana verilen Orhan Veli şiirlerinde ele alınan konuyu, temayı, duyguyu, şiirdeki başlıca motifleri tespit edebiliyorsun.
Yanıtını verirken bu tespit ettiğin konu, tema, duygu veya motifleri aralarında birer virgül olacak şekilde yazıyorsun.
Yanıtında sadece bunları yazıyorsun. Başka hiçbir açıklama ya da ek bilgi vermiyorsun.
"""

prompt = "Orhan Veli'nin aşağıdaki şiirinde ele alınan konu, tema, duygu veya motifleri yaz."

source_file_path = "./data/siir.xlsx"
target_file_path = source_file_path

st.set_page_config(page_title="Şiir Etiketleme Uygulaması")
st.title("Şiir Etiketleme Uygulaması")
st.divider()

start_row = st.number_input("Başlangıç Satırı", min_value=1, value=1)
end_row = st.number_input("Bitiş Satırı", min_value=1, value=10)
submit_btn = st.button(label='Etiketle')

if submit_btn:

    df = pd.read_excel(source_file_path, engine="openpyxl")

    progress_bar = st.progress(0)
    total_rows = end_row - start_row + 1

    for index, row in df.iloc[start_row-1:end_row].iterrows():

        try:
            siir = row['siir']

            full_prompt = f"{system_prompt} {prompt} {siir}"

            AI_response = llm_gemini.invoke(input=full_prompt)
            
            df.at[index, 'response'] = AI_response.content

        except Exception as e:
            st.error(f"Şu satırı işlerken hata oluştu: {index + 1}: {e}. Sonraki satıra geçiliyor...")
            continue
        
        progress_percentage = (index + 1 - (start_row-1)) / total_rows
        progress_bar.progress(progress_percentage)
    
    df.to_excel(target_file_path, index=False, engine="openpyxl")
    
    progress_bar.empty()
    
    st.success("Etiketleme İşlemi Tamamlandı")

st.dataframe(pd.read_excel(target_file_path, engine="openpyxl"))
