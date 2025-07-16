import yaml
from vectorstore.faiss import FaissVectorStore
from models.data_classes import GPT4oCreds, GenPromptConfig
from models.model_classes import GPT4O
from models.llm_json_generators import GPT4oJSONGenerator
from utilities.functions import *

if __name__ == "__main__":
    store = FaissVectorStore()

    # Load documents from a folder and build the index
    store.build_index(folder_path="extracts_for_db/")

    query = "Treatments for PCOS"
    print("The User query is: ", query)
    results = store.search(query, top_k=3)
    context = " ".join([str(doc) for (doc, score) in results])
    rag_input = f""" 
    Query: {query}
    Context: {context}
    """
    # Read GPT4o model credentials
    credentials = load_yaml_file("models/credentials/gpt4o.yaml")

    # Load GPT4o model and the prompts
    gpt4o = GPT4O(GPT4oCreds(**credentials))
    prompts = load_prompts_from_dir("prompts/")

    rag_system_prompt = GenPromptConfig(**prompts['rag_generation'])
    rag_generation = GPT4oJSONGenerator(gpt4o, rag_system_prompt, rag_input).generate()[1]
    print("The Model response is: ", rag_generation)


    # for i, (doc, score) in enumerate(results):
    #     print(f"Result {i+1} (Score: {score})\n{doc}\n")