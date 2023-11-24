import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
os.environ['OPENAI_API_KEY'] = "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"

def generate_question(text_input, difficulty, creativity):
    llm = OpenAI(temperature=creativity)

    prompt_template_name = PromptTemplate(input_variables =['difficulty','text','creativity'],template = "Generate 5 most {difficulty} question related to: '{text}' with a touch of creativity: {creativity}")
	
    chain =LLMChain(llm=llm, prompt=prompt_template_name)

    content = chain.run({"difficulty": difficulty,"text":text_input,"creativity":creativity})
	
    return content

# Streamlit app
st.title("Question Generator App")

# User input
text_input = st.text_input("Enter the text:")

# Difficulty and creativity sliders
difficulty_options = ['Easy', 'Medium', 'Hard']
difficulty = st.selectbox("Select difficulty level:", difficulty_options)
creativity = 1

# Generate question button
if st.button("Generate Question"):
    if text_input:
        generated_question = generate_question(text_input, difficulty, creativity)
        st.success(f"Generated Question:\n {generated_question}")
    else:
        st.warning("Please enter some text before generating a question.")
