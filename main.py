from mistralai import Mistral
from dotenv import load_dotenv
load_dotenv()
import os

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
MODEL="mistral-large-latest"

# MistralAI Question and Answer Code

client = Mistral(api_key=MISTRAL_API_KEY)
response = client.chat.complete(
    model=MODEL,
    messages=[
        {   
            "role": "user", 
            "content": "What is the capital of Germany?"
        },
    ]
)       
# print(response.choices[0].message.content)

# Now Converting the above code into a chatbot.

client = Mistral(api_key=MISTRAL_API_KEY)

def chat_loop():
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        
        input_message = [
            {
                "role": "user",
                "content": user_input
            }
        ]
        
        response = client.chat.complete(
            model=MODEL,
            messages=input_message
        )
        
        print(f"Bot: {response.choices[0].message.content}")

# if __name__ == "__main__":
#     print("Welcome to the Mistral chatbot! Type 'exit' or 'quit' to end the chat.")
#     chat_loop()

# # Adding the ability to get conversation history to the Chatbot (the old way before the new API)

client = Mistral(api_key=MISTRAL_API_KEY)

def chat_loop():

    history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        
        history.append(
            {
                "role": "user",
                "content": user_input
            }
        )    

        response = client.chat.complete(
            model=MODEL,
            messages=history
        )
        
        history.append(
            {
                "role": "assistant",
                "content": response.choices[0].message.content
            }
        )

        print("Bot: ",response.choices[0].message.content)

if __name__ == "__main__":
    print("Welcome to the Mistral chatbot with conversation history capability! Type 'exit' or 'quit' to end the chat.")
    chat_loop()

