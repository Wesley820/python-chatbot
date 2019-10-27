import src.chatbot as chatbot

def requestLine (string):
    response = chatbot.chat(string)
    print(response)

while (True):
    question = input('Você: ')
    requestLine(question)