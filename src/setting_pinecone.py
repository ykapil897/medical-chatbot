from src.helper import load_pdf
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')
extracted_data = load_pdf("medical-chatbot-using-llama2/data/")

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=20)
docs = text_splitter.split_documents(extracted_data)

index_name = "medical-chatbot"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore_from_docs = PineconeVectorStore.from_documents(
    docs,
    index_name=index_name,
    embedding=embeddings
)

