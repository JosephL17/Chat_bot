from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# app = Flask(__name__)
# CORS(app)  # Allow CORS for all origins

# template = """
# Answer the question below.

# here is the conversation history: {context}

# Question: {question}

# Answer:
# """

# model = OllamaLLM(model='llama3')
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

# def get_chatbot_response(message):
#     return f"Echo: {message}"

# @app.route('/http://127.0.0.1:5000', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data.get('message')
#     response = get_chatbot_response(user_message)
#     return jsonify({'response': response})

# def handle_conversation():
#     context = ''
#     print('welcome to the AI ChatBot, Type "exit" to quite.')
#     while True:
#         user_input = input('you: ')
#         if user_input.lower() == 'exit':
#             break

#         result = chain.invoke({'context': context, 'question': user_input})
#         print('Bot: ', result)
#         context += f"]nUser: {user_input}\nAi: {result}"

# if __name__ == '__main__':
#     handle_conversation()

app = Flask(__name__)
CORS(app)  # Allow CORS for all origins

# Define the template for the chatbot conversation
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model and chain
model = OllamaLLM(model='llama3')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    context = data.get('context', '')

    # Generate the response from the chatbot
    result = chain.invoke({'context': context, 'question': user_message})

    # Debugging information
    print("Type of result:", type(result))
    print("Result:", result)

    # Ensure result is a dictionary and access text
    if isinstance(result, dict):
        response_text = result.get('text', '')
    else:
        response_text = result  

    # Update the context
    updated_context = f"{context}\nUser: {user_message}\nAI: {response_text}"

    return jsonify({'response': response_text, 'context': updated_context})

if __name__ == '__main__':
    app.run(debug=True)