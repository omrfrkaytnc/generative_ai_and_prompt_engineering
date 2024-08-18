from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
embeddings = OpenAIEmbeddings(api_key=my_key_openai)

documents=[
            "labirentte peynir arayan hayvanlara yardım ettik", 
            "deneklerin hepsi aynı peyniri tercih etti", 
            "deneyde kullanılan sıçanlar aynı türden",
            "araştırmada on laboratuvar hayvanı kullanıldı",
            "Zahmetli hesaplamalar sayesinde roketlerin yörünge hızı hesaplanıyor"
            ]

query = "deney faresi kullanıldı"

vectorstore = Chroma.from_texts(documents, embeddings)

#Method1 - directly from the vectorstore
relevant_documents_vs = vectorstore.max_marginal_relevance_search(query)

#Method2 - using a retriever
retriever = vectorstore.as_retriever(search_type="mmr") 
relevant_documents_rt = retriever.get_relevant_documents(query)


print("Doğrudan MMR ile Elde Edilen Dokümanlar:")
print("*"*100)
for doc in relevant_documents_vs:
    print(doc.page_content)
print("-"*90)
print("Retriever Üzerinden Elde Edilen Dokümanlar:")
print("*"*100)
for doc in relevant_documents_rt:
    print(doc.page_content)


