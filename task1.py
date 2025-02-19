from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings

load_dotenv()

# Load the dataset
reader = SimpleDirectoryReader(input_dir='./sample_data')
documents = reader.load_data()

# Create a vector store index
# ref for embedding model: https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/
index = VectorStoreIndex.from_documents(documents)

# Query the index
query_engine = index.as_query_engine()

query = "What is Chronoscape?"

# ref for querying process: https://docs.llamaindex.ai/en/stable/understanding/querying/querying/
# Print the raw results
# raw_results = index.as_query_engine(response_mode="accumulate").query(query)
# print(raw_results)

# Print the response
response = query_engine.query(query)
print(response)

