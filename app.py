import streamlit as st
# from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

def txt_string(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks=text_splitter.split_text(text);
    return chunks;

def get_vector_store(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=FAISS.from_texts(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template="""
    Answer the question only from pdf if answer is not related with pdf just say "I can't answer this question"
    Context:\n {context}?\n
    Question: \n{question}\n

    """
    model=ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",temperature=0.3)
    prompt=PromptTemplate(template=prompt_template,input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain




def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )

    st.write("Reply:", response["output_text"])
    
    feedback = st.radio("Are you satisfied with this answer?", ("Yes", "No"), key=user_question)

    if feedback :
        if feedback=="No":
            with open("unsatisfied.txt", "a", encoding="utf-8") as f:
                f.write(f"Question: {user_question}\n")
                f.write(f"Answer: {response['output_text']}\n")
                f.write("-" * 60 + "\n")
        st.warning("We've saved your feedback. Thank you!")

    return response['output_text']





def load_env():
    load_dotenv();
    api_kk=os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_kk)

def main():
    load_env()
    st.title('Welcome to hostel')
    raw_text = txt_string("data/hostel_info.txt")
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)
    user_question = st.text_input("Ask question related to Green Valley Boys' Hostel")

    if user_question:
        output=user_input(user_question)
        if output=="I can't answer this question.":
            with open("unanswered.txt", "a", encoding="utf-8") as f:
                f.write(user_question)
           
        st.warning("We've saved your feedback. Thank you!")

    

if __name__=="__main__":
    main()