from openai import OpenAI
import google.generativeai as genai
import base64
import PIL.Image
import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = os.getenv("google_apikey")

client = OpenAI(api_key=my_key_openai)

genai.configure(
    api_key=my_key_google
)


def gpt_vision_with_url(image_url, prompt="Bu resmin içeriğini betimle"):

    AI_Response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {
                            "url": image_url,
                            },
                },
            ],
        }
    ],
    max_tokens=300
    )

    return AI_Response.choices[0].message.content


def encode_image(image_path):

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def gpt_vision_with_local_file(image_path, prompt="Bu resmin içeriğini betimle"):
    
    base64_image = encode_image(image_path)

    gpt_vision_url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_key_openai}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": prompt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
    }

    AI_Response = requests.post(url=gpt_vision_url, headers=headers, json=payload)

    final_response = AI_Response.json()['choices'][0]['message']['content']

    return final_response

def gemini_vision_with_local_file(image_path, prompt="Bu resmin içeriğini betimle"):

    client = genai.GenerativeModel(
        model_name="gemini-pro-vision"
    )

    source_image = PIL.Image.open(image_path)

    AI_Response = client.generate_content(

        [
            prompt,
            source_image
        ]
    )

    AI_Response.resolve()

    return AI_Response.text




st.title("Çoklu Form Etkileşimi")
st.divider()

tab_url, tab_local, tab_gemini = st.tabs(
   [
      "GPT-4 Vision ile URL'den Çalışma", 
      "GPT-4 Vision ile Yerel Dosyadan Çalışma", 
      "Gemini Pro Vision ile Yerel Dosyadan Çalışma"
    ]
)


with tab_url:

    image_url = st.text_input(label="Görselin bulunduğu web adresini giriniz", key="imageurl_url")

    prompt = st.text_input(label="Görsel ilgili ilgili yapmak istediğiniz işlemi tarif ediniz", key="prompt_url")

    submit_btn = st.button(label="Gönder", key="submit_url")

    if submit_btn:
        
        response = gpt_vision_with_url(image_url=image_url, prompt=prompt)

        st.success(response)

        st.image(image=image_url)

with tab_local:

    prompt = st.text_input(label="Görsel ile ilgili yapmak istediğiniz işlemi tarif ediniz", key="prompt_gpt")

    selected_image = st.file_uploader(label="Modele göndermek istediğiniz resmi seçiniz", type=["png"], key="image_gpt")

    if selected_image:

        st.image(image=selected_image.name)

    submit_btn = st.button(label="Gönder", key="submit_gpt")

    if submit_btn:
        
        response = gpt_vision_with_local_file(image_path=selected_image.name, prompt=prompt)

        st.success(response)

with tab_gemini:

    prompt = st.text_input(label="Görsel ile ilgili yapmak istediğiniz işlemi tarif ediniz", key="prompt_gemini")

    selected_image = st.file_uploader(label="Modele göndermek istediğiniz resmi seçiniz", type=["png"], key="image_gemini")

    if selected_image:

        st.image(image=selected_image.name)

    submit_btn = st.button(label="Gönder", key="submit_gemini")

    if submit_btn:
        
        response = gemini_vision_with_local_file(image_path=selected_image.name, prompt=prompt)

        st.success(response)