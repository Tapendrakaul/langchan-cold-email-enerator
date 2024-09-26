from langchain_groq import ChatGroq
import os
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException



load_dotenv()

class Chain:
    def __init__(self) -> None:
        self.llm =  ChatGroq(
        model="llama-3.1-70b-versatile",
        temperature=0,
        groq_api_key=os.environ["GROQ_CLOUD_API"]
    )
        
    def extractor_job(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scrapped text is from the career's page of a website.
                your job is to extract the job postings and return them in JSON format container.
                following keys: `role`,`experience`,`skills` and `description`.
                only return the valid JSON.
                ### VALID JSON (NO PREAMBLE)
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data':cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big, unable to parse jobs.")
         
        return res if isinstance(res,list) else [res]
    
    def write_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
                ### JOB DESCRIPTION
                {job_description}

                ### INSTRUCTION
                you are Tapendra Kaul, a business development executive at Futurely. Futurely is an AI & Consulting company dedicated to facilitating and seamless integration of business process
                through automated tools.
                over our experience , we have empowered numerous enterprices with tailored solutions, fostering scalability,
                process optimization, cost reduction and heightened overall efficency.
                your job is to write a cold email to the client regarding the job mentioned above describing the capabilities  and expertise  in fulfiling their needs .
                Also add the most relevent ones from the following links to showcase Futurely's portfolio: {link_list}
                Remember you are Tapendra Kaul, BDE at Futurely.
                Do not provide a preamble.
                ### EMAIL (NO PREAMBLE):
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content


                    
