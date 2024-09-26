import pandas as pd 
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="resource/project_portfolio_data.csv") -> None:
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection("portfolio")

    def load_portfolio(self):
            if self.collection.count() == 0:
                print("Collection is empty. Adding data...")
                for _, row in self.data.iterrows():
                    self.collection.add(documents=row["Tech Stack"],
                                metadatas={"links":row["Project Links"]},
                                ids=[str(uuid.uuid4())])
                print(f"Added {len(self.data)} items to the collection.")
            else:
                print(f"Collection already contains {self.collection.count()} items.")
    
    def query_links(self,skills):
        return self.collection.query(query_texts=skills,n_results=2).get('metadatas',[])