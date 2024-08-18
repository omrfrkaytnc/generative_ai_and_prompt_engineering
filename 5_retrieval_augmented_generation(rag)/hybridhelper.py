from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import WebBaseLoader
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")


embeddings = OpenAIEmbeddings(api_key=my_key_openai)

doc_list = [
    "I like apples",
    "I like oranges",
    "Apples and oranges are fruits",
    "I like computers by Apple",
    "I love fruit juice but particularly apples as apples are the best",
    "Air Cana serves apple juice",
    "Beetlejuice is a terrible movie",
    "That country literally is a banana republic",
    "The iPhone made its manufacturer rich",
    "I dislike apples",
]


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



def get_relevant_documents_with_bm25(documents, query):

    bm25_retriever = BM25Retriever.from_documents(documents=documents)
    bm25_retriever.k = 4

    bm25_relevant_documents = bm25_retriever.get_relevant_documents(query=query)

    return bm25_relevant_documents, bm25_retriever

def get_relevant_documents_with_FAISS(documents, query):

    vectorstore = FAISS.from_documents(documents, embeddings)
    faiss_retriever = vectorstore.as_retriever(search_kwargs = {"k":4})

    FAISS_relevant_documents = faiss_retriever.get_relevant_documents(query)

    return FAISS_relevant_documents, faiss_retriever


def get_relevant_documents_for_hybrid_search(query, retriever1, retriever2, weight1=0.5, weight2=0.5):


    ensemble_retriever = EnsembleRetriever(
                                retrievers=[retriever1, retriever2],
                                weights=[weight1, weight2]
                            )

    hybrid_relevant_documents = ensemble_retriever.get_relevant_documents(query)

    return hybrid_relevant_documents