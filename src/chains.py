import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

load_dotenv()

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "mistral:7b"),
    base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
)

def get_summarize_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that summarizes text."),
        ("human", "Summarize the following text:\n\n{text}")
    ])
    return prompt | llm | StrOutputParser()

def get_qa_chain():
    loader = TextLoader("data/document.txt")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text:v1.5",
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    )
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)
    retriever = vectorstore.as_retriever()

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)

def get_learn_path_chain():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert career coach. Your task is to generate a structured learning path for a user based on their profile and goals."),
        ("human", "My profile is: {profile}.\nMy goal is: {goal}.\n\nPlease provide a step-by-step learning path.")
    ])
    return prompt | llm | StrOutputParser()

