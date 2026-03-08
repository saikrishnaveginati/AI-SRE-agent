import boto3

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "cohere.command-r-v1:0"


def ask_bedrock(prompt):

    response = bedrock.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        inferenceConfig={
            "maxTokens": 200,
            "temperature": 0.3
        }
    )

    return response["output"]["message"]["content"][0]["text"]