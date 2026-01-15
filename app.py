import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from rag.retriever import get_relevant_docs

load_dotenv()

st.set_page_config(page_title="HiDevs AI Clone", page_icon="🤖")
st.title("🤖 Build Your Own AI Clone - HiDevs")

query = st.text_input("Ask me anything about HiDevs:")

if query:
    docs = get_relevant_docs(query)
    context = "\n".join([d.page_content for d in docs])

    template = """
    You are a helpful AI assistant.
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {question}
    """

    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    response = llm.invoke(
        prompt.format(context=context, question=query)
    )

    st.subheader("Answer:")
    st.write(response.content)
