from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings

load_dotenv()

# # Load the dataset
# reader = SimpleDirectoryReader() #TODO: fill in the path to the directory containing the documents
# documents = #TODO: load the documents from the reader

# # Create a vector store index using VectorStoreIndex
# # ref for embedding model: https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/
# index = #TODO: create a VectorStoreIndex object with the documents

# # Create query engine
# query_engine = #TODO: create a query engine object with the index

query = "What is Chronoscape?"
# # Print the response
# response = #TODO: query the query engine with the query
# print(response)

# ref for querying process: https://docs.llamaindex.ai/en/stable/understanding/querying/querying/
# We could also print the raw results by using the following code:
# TODO: try to uncomment the following code and run it
# raw_results = index.as_query_engine(response_mode="accumulate").query(query)
# print(raw_results)