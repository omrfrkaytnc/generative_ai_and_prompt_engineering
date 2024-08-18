import chromadb

client = chromadb.HttpClient()

collection_status = False

current_collections = client.list_collections()

for collection in current_collections:
    if collection.name == "new_collection":
        collection_status = True
        break
        
if collection_status:
    my_collection = client.get_collection("new_collection")
else:
    my_collection = client.create_collection("new_collection")

    my_collection.add(
        documents=[
            "labirentte peynir arayan hayvanlara yardım ettik", 
            "deneklerin hepsi aynı peyniri tercih etti", 
            "deneyde kullanılan sıçanlar aynı türden",
            "araştırmada on laboratuvar hayvanı kullanıldı",
            "Zahmetli hesaplamalar sayesinde roketlerin yörünge hızı hesaplanıyor"
            ],
            
        metadatas=[
            {"source": "notion"}, 
            {"source": "google-docs"},
            {"source": "txt file"},
            {"source": "txt file"},
            {"source": "txt file"}
            ],
        ids=[
            "doc1", 
            "doc2", 
            "doc3",
            "doc4",
            "doc5"
            ], # must be unique for each doc 
    )

results = my_collection.query(
    query_texts=["deney faresi kullanıldı"],
    n_results=5,
)

retrieved_docs = results['documents'][0]
retrieved_distances = results['distances'][0]

for i, doc in enumerate(retrieved_docs):
    print(f"{doc}: {retrieved_distances[i]}")













#Before running this file, first run the "chroma run" command from another terminal. Once server is up you can use this
# python can also run in-memory with no server running: chromadb.PersistentClient()

# import chromadb
# client = chromadb.HttpClient()
# collection = client.create_collection("thenewest_collection")

# # Add docs to the collection. Can also update and delete. Row-based API coming soon!
# collection.add(
#     documents=["You are not alone", "This is document2", "Seasons happen for some reason"], # we embed for you, or bring your own
#     metadatas=[{"source": "notion"}, {"source": "google-docs"}, {"source":"txt file"}], # filter on arbitrary metadata!
#     ids=["doc1", "doc2", "doc3"], # must be unique for each doc 
# )

# results = collection.query(
#     query_texts=["Earth has seasons due to certain factors"],
#     n_results=1,
#     # where={"metadata_field": "is_equal_to_this"}, # optional filter
#     # where_document={"$contains":"search_string"}  # optional filter
# )

# print(results)
# print("*"*100)
# print(f"Distances: {results['distances']}")