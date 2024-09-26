from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from portfolio import Portfolio
from chain import Chain



load_dotenv()

def create_streamlit_app(chain,portfolio,clean_text):
    st.title(" 📩 Cold Mail Genrator")
    url_input = st.text_input("Enter a URL:",value="https://jobs.nike.com/job/R-37070?from=job%20search%20funnel")
    submit_button = st.button("Submit")
    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = chain.extractor_job(data)
            for job in jobs:
                skills = job.get('skills',[])
                links = portfolio.query_links(skills)
                email = chain.write_email(jobs,links)
                st.code(email, language='markdown')

        except Exception as e:
            st.error(f"An Error  occurred: {e} ")
        
if __name__=="__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Genrator", page_icon="📩")
    create_streamlit_app(chain,portfolio,clean_text)
