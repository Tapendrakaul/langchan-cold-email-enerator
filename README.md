
# Cold Email Generator on Behalf of Business Development Executive (BDE) using Langchain

## Project Overview

This project is an AI-powered agent built using the Langchain framework to scrape job posts from websites using their URLs. Users can input a job post URL through a front-end interface built with Streamlit, and the backend processes the request to scrape the job post data. The data is stored in JSON format, and the agent further processes it using prompt engineering to generate a cold email response. Additionally, the system leverages a VectorDB to store custom data and link relevant profiles or portfolios to job posts.

### Key Features:
- Scrapes job post data from URLs
- Stores Jb Post data in JSON format
- Uses prompt engineering to generate cold emails on behalf of a Business Development Executive (BDE)
- Integrates VectorDB to link custom data (profiles, portfolios) to job posts
- Built with Langchain framework, vector database (chromadb), and Streamlit

---

## Installation and Setup

### Prerequisites

Before setting up the project, ensure you have the following installed:
- **Python 3.10+**
- **pip** (Python package installer)
- **Git** (optional, for version control)

### Step-by-Step Instructions

1. **Clone the repository**
   Open a terminal and run the following command to clone the project repository:
   ```bash
   git clone https://github.com/Tapendrakaul/langchan-cold-email-enerator.git
   ```
   Replace `your-username` and `your-repo-name` with the actual GitHub details of the project.

2. **Navigate to the project directory**
   ```bash
   cd langchan-cold-email-enerator
   ```

3. **Set up a virtual environment** (optional but recommended)
   Create a virtual environment to avoid conflicts with other Python projects on your machine:
   ```bash
   python3.11 -m venv env
   ```
   Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scriptsctivate
     ```
   - On Mac/Linux:
     ```bash
     source env/bin/activate
     ```
     
4. **Install the project dependencies**
   Run the following command to install all required libraries:
   ```bash
   pip install -r requirements.txt
   ```
   
5. **Run the Streamlit front-end**
   In a new terminal (with the virtual environment still activated), start the Streamlit application:
   ```bash
   streamlit run main.py
   ```

6. **Using the Project**
   - Open the URL provided by Streamlit (typically `http://localhost:8501`) in your browser.
   - Input a job post URL and submit.
   - The backend will process the job post, store the data in JSON format, and return an AI-generated cold email response on behalf of your organization.