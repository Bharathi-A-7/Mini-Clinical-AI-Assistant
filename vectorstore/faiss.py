import os
import json
import numpy as np
import faiss
from typing import List, Tuple, Union
from utilities.functions import load_json_docs, json_to_text
from sentence_transformers import SentenceTransformer


class FaissVectorStore:
    """
    A class to represent FAISS Vector Store
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initializes the class attributes.

        Args:
            model_name (str): Name of the sentence transformer model to use for embeddings.
        """
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = []
        self.embeddings = None


    def _generate_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Generates vector embeddings for a list of text inputs.

        Args:
            texts (List[str]): List of text documents.

        Returns:
            np.ndarray: Numpy array of embeddings.
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings

    def build_index(self, docs: List = None, folder_path: str = None):
        """
        Builds the FAISS index using provided documents or documents loaded from a folder.

        Args:
            docs (List) : List of documents, either plain text or JSON dicts.
            folder_path (str): Path to folder containing JSON files.

        """
        docs = load_json_docs(folder_path)

        self.documents = docs
        texts = [json_to_text(doc) for doc in docs]
        self.embeddings = self._generate_embeddings(texts)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(self.embeddings)

    def search(self, query: str, top_k: int = 5):
        """
        Performs a similarity search against the FAISS index for a given query.

        Args:
            query (str): The text query to search.
            top_k (int): Number of top results to return.

        Returns:
            List: List of (document, similarity score) tuples.
        """
        query_vec = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_vec, top_k)
        results = [(self.documents[i], float(D[0][rank])) for rank, i in enumerate(I[0])]
        return results
