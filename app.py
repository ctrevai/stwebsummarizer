import streamlit as st
import html_loader
import llm_selector


st.title("websummarizer")


url = st.text_input("Enter a url")

note = st.text_input("Enter a note")

#url = 'https://aws.amazon.com/blogs/media/video-summarization-with-aws-artificial-intelligence-ai-and-machine-learning-ml-services/'    

# Core system prompt
if url and note:
    #parse URL
    text = html_loader.html_to_text(url)
    #prepare prompt
    prompt = '''

    Provide the summary of the following text
    which the most relevent to the note

    <note> ''' + note + ''' </note>

    <text> ''' + text + ''' </text> '''

    response_content = llm_selector.llm_selector(prompt)
    st.write(response_content)
