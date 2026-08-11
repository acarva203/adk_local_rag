import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.litellm import LiteLLM as LlamaIndexLiteLLM
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm as ADKLiteLlm

# ==========================================
# 1. Setup the Local RAG Engine (LlamaIndex)
# ==========================================
# Configure LlamaIndex to use your Gateway via LiteLLM
Settings.llm = LlamaIndexLiteLLM(
    model="openai/gemini-2.5-pro", # Use your gateway's expected prefix
    api_base=os.environ.get("LITELLM_API_BASE"),
    api_key=os.environ.get("LITELLM_API_KEY")
)

# This model runs entirely on your local machine and uses ~100MB of RAM
print("Loading local HuggingFace embedding model...")
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5" # Excellent, lightweight retrieval model
)

# Load document and build the local in-memory index
print("Indexing document...")
documents = SimpleDirectoryReader(input_files=["./data/grounding_gsearch.md"]).load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine() #llama index functions

# ==========================================
# 2. Define the ADK Tool
# ==========================================
def search_document(query: str) -> str:
    """
    Searches the reference document for information to answer the user's query.
    Always use this tool before answering questions about the document.
    """
    # This executes the local RAG retrieval and generation
    response = query_engine.query(query)
    return str(response)

# ==========================================
# 3. Define the ADK Root Agent
# ==========================================
# Configure the ADK Agent to use your Gateway LLM wrapper
adk_llm = ADKLiteLlm(
    model="openai/gemini-2.5-pro", # Note: ADK LiteLLM often uses openai/ prefix for generic gateways
    api_base=os.environ.get("LITELLM_API_BASE"),
    api_key=os.environ.get("LITELLM_API_KEY")
)

root_agent = Agent(
    name="Document_RAG_Agent",
    model=adk_llm,
    description="An agent that answers questions based strictly on a provided document.",
    instruction=(
        "You are a helpful research assistant. "
        "When a user asks a question, you MUST use the `search_document` tool to find the answer. "
        "Do not answer from your general knowledge."
    ),
    tools=[search_document] # Attach our RAG function as a tool
)
