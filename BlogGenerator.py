from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
st.set_page_config(page_title="Generate_Blogs",
                   layout="centered",
                   initial_sidebar_state="collapsed")
st.header("Generate Blogs")
input_text=st.text_input("Enter the Blog Topic")
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input("No. of words")
with col2:
    blog_style=st.selectbox("writing the blog for ",("Researchers","Data Scientist","Common people"),index=0)
def generateblog(input_text,no_words,blog_style):
    llm=ChatOpenAI()
    prompt=PromptTemplate(template="write the blog for {blog_style} job profile for a topic {input_text} within {no_words} words",
                          input_variables=["blog_style","input_text","no_words"])
    formatted_prompt = prompt.format(
        input_text=input_text,
        no_words=no_words,
        blog_style=blog_style
    )
    response=llm.invoke(formatted_prompt)

    print(response)
    return response.content

submit=st.button("Generate")
if submit:
    st.write(generateblog(input_text,no_words,blog_style))
