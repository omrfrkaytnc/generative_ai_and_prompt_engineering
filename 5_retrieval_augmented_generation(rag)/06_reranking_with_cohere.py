import streamlit as st
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
my_key_cohere = os.getenv("cohere_apikey")

cohere_client = cohere.Client(api_key=my_key_cohere)

query = "Türkiye'nin başkenti neresidir?"

documents = [
   "Ankara, Türkiye'nin başlıca turistik lokasyonlarından biridir ve her yıl beş milyondan fazla turist ev sahipliği yapar.",
   "Genç adam Başkent Üniversitesi'nde bilgisayar mühendisliği bölümüne yerleştiği için son derece heyecanlıydı.",
   "Orta kuşak ikliminin özelliklerini gösteren Türkiye, dünya üzerinde dört mevsimi birden yaşayan şanslı coğrafyalardan biridir.",
   "Türkiye'nin başkenti Ankara'dır",
   "Yahya Kemal bir şiirinde Ankara'nın en çok İstanbul'a dönüş yolunu sevdim diyordu ama o sıralar eski bir başkent olarak bugünkü kaotik metropol havasından uzaktı.",
   "Cumhuriyetin ilanı ile birlikte yaşanan önemli değişikliklerden biri de başkentin yer değiştirerek Ankara'ya taşınmış olmasıydı.",
   "Başkentin neresi olması gerektiğiyle ilgili tartışmalar sürerken, güvenli ve merkezi bir lokasyon aranıyordu tıpkı Ankara gibi.",
   "Elektromanyetizmayla ilgili çalışmalarıyla ünlenen Maxwell, Einstein gibi pek çok bilim adamına da ilham olmuştu.",
   "Ankara'nın başlıca ilçeleri Çankaya, Yenimahalle ve Keçiören'dir diyebiliriz.",
   "Kentleşme, ülkemizde geç başlamış ve sancıları halen devam etmekte olan bir sosyolojik süreçtir.",
   "Başkent Ankara'da yılın ilk kar yağışının keyfini yine çocuklar çıkardı.",
   "Türkiye Cumhuriyeti devletinin resmi başkenti olan Ankara şehri İç Anadolu bölgesinde yer alır."
   ]


st.set_page_config(layout="wide")
st.title("Advanced RAG: Reranking | Yeniden Sıralama")
st.divider()

col_left, col_input, col_right = st.columns([1,8,1])

with col_left:
    st.empty()
   
with col_input:
    submit_btn = st.button(label="Yeniden Sırala",use_container_width=True)

with col_right:
    st.empty()


col_original, col_dummy, col_reranked = st.columns([9,1,9])

with col_original:
    st.subheader("Orijinal Sırayla Dokümanlar")
    for doc in documents:
        st.info(doc)

with col_dummy:
    st.empty()


with col_reranked:
    st.subheader("Yeniden Sıralanmış Dokümanlar")


if submit_btn:
    
   results = cohere_client.rerank(query=query, documents=documents, top_n=12, model="rerank-multilingual-v2.0")

   for result in results:
      col_reranked.success(f"{result.document['text']}   ||   {result.relevance_score} || #Sıra {result.index+1}")