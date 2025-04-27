import streamlit as st
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
def load_env():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    return api_key

# Read text from a file
def txt_string(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

# Split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

# Create a vector store using GoogleEmbeddings
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Get the conversational chain
def get_conversational_chain():
    prompt_template = """
    You are a chatbot of a girls hostel.
    Answer to the question which is from text.
    Be polite.
    If there is something which is not from pdf just say I can't answer this You can contact  and give contact details.
    In case there is some weird thing which is not related to hostel only say I can't answer this
    Context:\n{context}\n
    Question:\n{question}\n
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Handle user input and respond
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )
    
    output_text = response["output_text"]
    
    if "I can't answer this question" in output_text:
        with open("unsatisfied.txt", "a", encoding="utf-8") as file:
            file.write(f"Unanswered Question: {user_question}\n\n")
        
    return output_text

# Initial setup
def initialize_chatbot():
    load_env()
    raw_text = txt_string("data/hostel_info.txt")
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)

# STREAMLIT UI
st.set_page_config(page_title="Vijay Laxmi Villa Girl's Hostel ChatBot", layout="centered")
st.title("🏠 Vijay Laxmi Villa Girl's Hostel Hostel ChatBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_question = st.text_input("Ask something about the hostel")

if st.button("Ask") and user_question:
    answer = user_input(user_question)
    st.session_state.chat_history.append(("You", user_question))
    st.session_state.chat_history.append(("Bot", answer))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")

