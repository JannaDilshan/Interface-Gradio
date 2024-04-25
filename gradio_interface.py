import requests
import gradio as gr

def query_chatbot(message):
    
    rasa_endpoint = "http://localhost:5005/webhooks/"
  
    payload = {
        "sender": "user",
        "message": message
    }
    # Send a POST request to the Rasa chatbot endpoint
    response = requests.post(rasa_endpoint, json=payload)
    # Parse the response and extract the chatbot's message
    chatbot_response = response.json()[0]['text'] if response.status_code == 200 else "Failed to connect to chatbot"
    return chatbot_response

iface = gr.Interface(fn=query_chatbot, inputs="text", outputs="text", title="Rasa Chatbot")
iface.launch()
