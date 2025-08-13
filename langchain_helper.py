import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

def get_db_chain():
    # Connect to SQLite DB
    db = SQLDatabase.from_uri(
    "mysql+pymysql://root:1971@localhost/atliq_tshirts"
)

    
    # Initialize Groq LLaMA 3 model
    llm = ChatGroq(
        model="llama3-70b-8192",
        temperature=0.1,
        groq_api_key=os.environ["GROQ_API_KEY"]
    )

    # Directly return SQL execution results
    chain = SQLDatabaseChain.from_llm(
        llm,
        db,
        verbose=True,
        top_k=5,
        return_direct=True  # ✅ Only returns DB result
    )

    return chain


