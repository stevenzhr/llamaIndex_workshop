# LlamaIndex Workshop Guide
This workshop session focuses on building a document and code query system using LlamaIndex. The sample data contains a fabricated product description called "Chronoscape" along with some of its code. 

Our first step is to connect to the model using LlamaIndex and ask the model about this product. Ideally, the model should have no prior knowledge of this product. 

After that, we'll use LlamaIndex to create a Document Indexing process, allowing us to store the product description in a vector database and retrieve relevant information based on future queries. 

Finally, we'll explore the CodeSplitter feature in LlamaIndex, which can be used to analyze code.


## Setup Instructions
0. Create a python virtual environment
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

### Ultra task (Optional): 
Integrate Task 0 and Task 1 so that when you ask the model about "Chronoscape," it will reply with the content from the made-up document. 

## Debug
If you encounter the following error at task2:
```
Could not get parser for language python. Check https://github.com/grantjenks/py-tree-sitter-languages#license for a list of valid languages.
Traceback (most recent call last):
  File "D:\temp\llamaIndex_workshop\task2.py", line 9, in <module>
    splitter = CodeSplitter(
  File "D:\temp\llamaIndex_workshop\venv\lib\site-packages\llama_index\core\node_parser\text\code.py", line 77, in __init__
    parser = tree_sitter_languages.get_parser(language)
  File "tree_sitter_languages\\core.pyx", line 19, in tree_sitter_languages.core.get_parser
  File "tree_sitter_languages\\core.pyx", line 14, in tree_sitter_languages.core.get_language
TypeError: __init__() takes exactly 1 argument (2 given)
```
Try to run `pip install -U "tree-sitter<0.22.0"`. 

## Referenece link

[LlamaIndex python starter code](https://docs.cloud.llamaindex.ai/llamaparse/getting_started/python)

[LlamaIndex - OpenRouter](https://docs.llamaindex.ai/en/stable/examples/llm/openrouter/)

[LlamaIndex - Embeddings](https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings/)

[LlamaIndex - Querying](https://docs.llamaindex.ai/en/stable/understanding/querying/querying/)

[LlamaIndex - VectorStoreIndex](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/#using-vectorstoreindex)

[LlamaIndex - Node Parser Modules](https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/)