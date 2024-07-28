from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#llama3 template that run in the terminal
# template = """
# Answer the question below.

# here is the conversation history: {context}

# Question: {question}

# Answer:
# """

# model = OllamaLLM(model='llama3')
# prompt = ChatPromptTemplate.from_template(template)
# chain = prompt | model

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

# result = model.invoke(input='hello world')
# print(result)