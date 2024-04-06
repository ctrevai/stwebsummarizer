import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
import boto3
import json


st.title("websummarizer")


url = st.text_input("Enter a url")

note = st.text_input("Enter a note")

# url = 'https://aws.amazon.com/blogs/media/video-summarization-with-aws-artificial-intelligence-ai-and-machine-learning-ml-services/'

# URL parser
if url:
    loader = WebBaseLoader(url)
    html = loader.load()

    html2text = Html2TextTransformer()
    docs = html2text.transform_documents(html)
    text = docs[0].page_content

# Core system prompt
if url and note:
    prompt = '''

    Provide the summary of the following text
    which the most relevent to the note

    <note> ''' + note + ''' </note>

    <text> ''' + text + ''' </text> '''

    accept = 'application/json'
    contentType = 'application/json'

    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    # Claude2.1
    # modelId = 'anthropic.claude-v2:1'
    # # modelId = 'anthropic.claude-3-sonnet-20240229-v1:0'

    # Claude2.1 payload
    # body = json.dumps({
    #     "prompt": "\n\nHuman:\n\n" + prompt + "\n\nAssistant:",
    #     "max_tokens_to_sample": 10000,
    #     "temperature": 0.1,
    #     "top_p": 0.9,
    # })

    # Claude 3 Sonnet
    # modelId = "anthropic.claude-3-sonnet-20240229-v1:0"
    # Claude 3 Haiku
    modelId = "anthropic.claude-3-haiku-20240307-v1:0"
    # Claude 3 payload
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ]
            }
        ]
    })

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType)

    print(response)

    response_body = json.loads(response.get('body').read())
    response_content = response_body.get('content')

    st.write(response_content)
