import boto3
import json


def llm_selector(prompt):
    accept = 'application/json'
    contentType = 'application/json'

    bedrock = boto3.client(
        service_name="bedrock-runtime",
        region_name="us-east-1",
    )

    # Claude2.1
    # modelId = 'anthropic.claude-v2:1'

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
        "temperature": 0,
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

    response_body = json.loads(response.get('body').read())
    response_content = response_body.get('content')
    return response_content
