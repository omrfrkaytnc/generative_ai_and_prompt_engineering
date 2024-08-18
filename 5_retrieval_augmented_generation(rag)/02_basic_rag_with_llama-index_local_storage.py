from llama_index import VectorStoreIndex
from llama_index import SimpleDirectoryReader
from llama_index import StorageContext
from llama_index import load_index_from_storage
from llama_index.response.pprint_utils import pprint_response

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("openai_apikey")

PERSIST_DIR = "./storage"

if not os.path.exists(PERSIST_DIR):

    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)

    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:

    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)


query_engine = index.as_query_engine()
response = query_engine.query("Yapay Zekanın kullanım alanları nelerdir?")

pprint_response(response,show_source=True)