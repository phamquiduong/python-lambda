from fastapi import FastAPI


def handler(event, context):
    app = FastAPI()
    # Your Lambda function logic goes here
    message = "Hello, world!"
    return {
        'statusCode': 200,
        'body': message
    }
