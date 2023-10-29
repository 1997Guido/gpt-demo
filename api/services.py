import openai
import json
import os
openai.api_key = os.getenv('GPT_KEY')


def get_query_response(query_category, user_query):
    # Preparing the system message with database explanation
    system_message = {
        "role": "system",
        "content": f"You are a database assistant you can only answer in SQL without any additional text. U will be asked for info and need to write SQL based on the following explanation of the tables: {query_category.database_explanation.description}"
    }

    # Preparing the user message with the user query
    user_message = {
        "role": "user",
        "content": user_query
    }

    # Sending the request to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message]
    )

    # Extracting the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']

    return assistant_reply
