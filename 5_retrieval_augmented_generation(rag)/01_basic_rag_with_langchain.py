from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import CohereEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

my_key_google = os.getenv("google_apikey")
my_key_cohere = os.getenv("cohere_apikey")

llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")
embeddings = CohereEmbeddings(cohere_api_key=my_key_cohere, model="embed-multilingual-v3.0")

def ask_gemini(prompt):

    AI_Response = llm_gemini.invoke(prompt)

    return AI_Response.content


def rag_with_url(target_url, prompt):

    loader = WebBaseLoader(target_url)

    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )


    splitted_documents = text_splitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(splitted_documents, embeddings)
    retriever = vectorstore.as_retriever()

    relevant_documents = retriever.get_relevant_documents(prompt)

    context_data = ""

    for document in relevant_documents:
        context_data = context_data + " " + document.page_content

    final_prompt = f"""Şöyle bir sorum var: {prompt}
    Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data} .
    Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
    """

    AI_Response = ask_gemini(prompt=final_prompt)

    return AI_Response, relevant_documents


test_url = "https://kpmg.com/tr/tr/home/gorusler/2023/12/uretken-yapay-zeka-uygulamalarinin-kurumsallasma-yaklasimi.html"

test_question = "Üretken yapay zeka uygulamalarının hayata geçirirken yaşanan temel sorunlar neler?"

AI_Response, relevant_documents = rag_with_url(target_url=test_url, prompt=test_question)

print(f"SORU: {test_question}")
print("-"*100)
print(f"YZ YANITI: {AI_Response}")
print("-"*100)
for doc in relevant_documents:
    print(doc.page_content)
    print("*"*100)