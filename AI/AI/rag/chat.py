from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_key=os.getenv("GOOGLE_API_KEY")

client = OpenAI(
    api_key=API_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Vector embeddings
embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding=embedding_model
)

# Take user input
user_query = input("Ask something: ")

# Relevant chucks from the vector db
search_results = vector_db.similarity_search(query=user_query)

context="\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
You are helpful AI assistant who answers user query based on the available context retrieved from the PDF file along with page_contents
and page_number.

You should only ans the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context}

"""

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")