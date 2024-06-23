def chatbot():
    from langchain_pinecone import PineconeVectorStore
    from langchain.prompts import PromptTemplate
    from src.prompt import prompt_template
    from langchain.chains import RetrievalQA
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_groq import ChatGroq
    import os
    from dotenv import load_dotenv

    load_dotenv()

    index_name = "medical-chatbot"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain_type_kwargs={"prompt": PROMPT}

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    model = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY)

    qa = RetrievalQA.from_chain_type(  
        llm=model,  
        chain_type="stuff",  
        retriever=vectorstore.as_retriever(search_kwargs={'k': 7}),
        return_source_documents=True, 
        chain_type_kwargs=chain_type_kwargs 
    )  
    return qa
