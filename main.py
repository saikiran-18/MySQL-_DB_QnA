import streamlit as st
from langchain_helper import get_db_chain

st.set_page_config(page_title="Atlas T-Shirts Q&A", page_icon="👕")
st.title("Atlas T-Shirts: Database Q&A 👕 (MySQL + Llama3)")
st.caption("Ask questions about the t-shirt database and get answers directly from the MySQL database using Llama3 model.")

question = st.text_input("Enter your question:")

if question:
    chain = get_db_chain()
    result = chain.run(question)

    st.subheader("Answer")

    # If the result is a list of tuples, format it nicely
    if isinstance(result, list):
        try:
            formatted = ", ".join(f"{cat}: {qty}" for cat, qty in result)
            st.write(f"Total quantity sold by category: {formatted}")
        except:
            st.write(result)
    else:
        st.write(result)

















