from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = my_key_google = os.getenv("google_apikey")

embeddings = OpenAIEmbeddings(api_key=my_key_openai)
llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")
llm_openai = ChatOpenAI(api_key=my_key_openai, model="gpt-4-0125-preview")

def load_and_split_documents(target_url):

    loader = WebBaseLoader(target_url)

    raw_documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    splitted_documents = text_splitter.split_documents(raw_documents)

    custom_documents = []

    for i, raw_doc in enumerate(splitted_documents):

        new_doc = Document(
            page_content=raw_doc.page_content,
            metadata = {
                "source": raw_doc.metadata["source"],
                "title" : raw_doc.metadata["title"],
                "description" : raw_doc.metadata["description"],
                "language" : raw_doc.metadata["language"],
                "doc_id" : i
            }
        )

        custom_documents.append(new_doc)

    return custom_documents


def get_relevant_documents(prompt, documents):

    vectorstore = Chroma.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever(search_type="mmr")

    relevant_documents = retriever.get_relevant_documents(prompt)

    return relevant_documents


def run_rag(relevant_documents, prompt):

    context_data = ""

    for document in relevant_documents:
        context_data = context_data + " " + document.page_content

    final_prompt = f"""Şöyle bir sorum var: {prompt}
    Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data} .
    Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
    """

    AI_Response = llm_gemini.invoke(input=final_prompt)

    return AI_Response.content



def generate_hypothetical_document(prompt):

    HyDE_Prompt = f"""Kullanıcının sorusunu cevaplamak için kısa bir paragraf yaz.
    Kullanıcı Sorusu: {prompt}
    """

    hypothetical_answer = llm_gemini.invoke(input=HyDE_Prompt)

    return hypothetical_answer.content