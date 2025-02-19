# LlamaIndex Workshop Guide
This workshop session focuses on building a document and code query system using LlamaIndex. The sample data contains a fabricated product description called "Chronoscape" along with some of its code. 

Our first step is to connect to the model using LlamaIndex and ask the model about this product. Ideally, the model should have no prior knowledge of this product. 

After that, we'll use LlamaIndex to create a Document Indexing process, allowing us to store the product description in a vector database and retrieve relevant information based on future queries. 

Finally, we'll explore the CodeSplitter feature in LlamaIndex, which can be used to analyze code.


## Setup Instructions
1. Install requirements:
```bash
pip install -r requirements.txt
```
2. Refer `.env_sample` to create `.env` file with your API keys

## Exercises
The exercises are divided into 3 tasks:
### Task 0: Chat with LLM

- Configure the OpenRouter LLM connection
- Call LLM through ChatCompletion
- Call LLM with ChatMessage List

### Task 1: Document Indexing

- Implement document loading from directory
- Create vector store index
- Configure query engine
- Execute sample query

### Task 2: Advanced Query Handling

- Configure text splitting parameters
- Create index with custom code context
- Execute sample query

