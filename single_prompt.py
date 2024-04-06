import boto3
import json
import streamlit as st

bedrock = boto3.client(service_name='bedrock-runtime')
modelId = 'anthropic.claude-v2:1'
accept = 'application/json'
contentType = 'application/json'

prompt = st.text_input("Enter your prompt")

if prompt:

    body = json.dumps({
        "prompt": "\n\nHuman:\n\n" + prompt + "\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })

    response = bedrock.invoke_model(
        body=body, modelId=modelId, accept=accept, contentType=contentType)

    response_body = json.loads(response.get('body').read())
    # text
    # print(response_body.get('completion'))

    st.write(response_body.get('completion'))
