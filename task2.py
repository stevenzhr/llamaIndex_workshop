from dotenv import load_dotenv
from llama_index.core.node_parser import CodeSplitter
from llama_index.core import Document, VectorStoreIndex

load_dotenv()

# Create a code splitter
# Ref: https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/
splitter = CodeSplitter(
    language="python",
    chunk_lines=40,  # lines per chunk
    chunk_lines_overlap=15,  # lines overlap between chunks
    max_chars=1500,  # max chars per chunk
)

# Load the code file
with open("sample_data/embeddings.py", "r", encoding="utf-8") as f:
    code_text = f.read()

# Parse the code file
nodes = splitter.get_nodes_from_documents([Document(text=code_text)])
print(f"Parsed {len(nodes)} nodes from the code file.")

# Create a vector store index
index = VectorStoreIndex(nodes=nodes)

# Query the index
query = "Show me the function signature of import_data."
response = index.as_query_engine().query(query)
print(response)