from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")
my_key_google = os.getenv("google_apikey")
my_key_cohere = os.getenv("cohere_apikey")

llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")
llm_openai = ChatOpenAI(api_key=my_key_openai, model="gpt-4-0125-preview")
embeddings = OpenAIEmbeddings(api_key=my_key_openai)
cohere_client = cohere.Client(api_key=my_key_cohere)


def generate_multi_query(original_prompt):

    multiquery_prompt = f"""Sen bir yapay zeka asistanısın.

    Bir vektör veri tabanından, kullanıcı sorusuna en fazla benzerlik gösteren dokümanların getirilmesi için, sana verilen kullanıcı girdisinin 3 farklı versiyonunu yazmakla görevlisin.

    Bunu yaparken amacın ise vektörleri karşılaştırırken kullanılan mesafe ölçümlerinin bazı sınırlılıklarını aşmak için, verilen soruyla ilgili birden çok bakış açısı geliştirerek kullanıcıya yardımcı olmak.

    Bu yazacağın alternatif soruları ayrı ayrı satırlarda olacak şekilde yaz.
    Alternatif soruları yazarken bunların 1, 2, 3 gibi numaralandırmalar koyma.

    Kullanıcı girdisi şöyle: {original_prompt}"""

    generated_queries = llm_openai.invoke(input=multiquery_prompt)

    temp_list = generated_queries.content.strip().split("\n")

    query_list = [original_prompt]
    query_list.extend(temp_list)

    return query_list


def get_relevant_documents(target_url, prompt):

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

    vectorstore = FAISS.from_documents(custom_documents, embeddings)
    retriever = vectorstore.as_retriever()

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


def rag_with_url(target_url, prompt):

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

    vectorstore = FAISS.from_documents(custom_documents, embeddings)
    retriever = vectorstore.as_retriever()

    relevant_documents = retriever.get_relevant_documents(prompt)

    context_data = ""

    for document in relevant_documents:
        context_data = context_data + " " + document.page_content

    final_prompt = f"""Şöyle bir sorum var: {prompt}
    Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data} .
    Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
    """

    AI_Response = llm_gemini.invoke(input=final_prompt)

    return AI_Response.content, relevant_documents



def get_unique_documents(retrieved_documents):

    unique_docs = {}

    for doc in retrieved_documents:
        doc_id = doc.metadata['doc_id']

        if doc_id not in unique_docs:
            unique_docs[doc_id] = doc

    return list(unique_docs.values())

def get_reranked_documents(documents, query, document_count=4):

    document_contents = []

    for doc in documents:
        document_contents.append(doc.page_content)

    reranked_documents = cohere_client.rerank(
        model="rerank-multilingual-v2.0",
        query=query, 
        documents=document_contents, 
        top_n=document_count
    )

    reranked_documents_list = []

    # for reranked_doc in reranked_documents:
    #     reranked_documents_list.append(reranked_doc.document['text'])
    
    for reranked_doc in reranked_documents:
        reranked_documents_list.append(documents[reranked_doc.index])

    
    return reranked_documents_list




