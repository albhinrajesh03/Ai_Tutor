chat_history=[]

def set_memory(role, message):
    text=f"{role}:{message}"
    chat_history.append(text)

    with open("history.txt","a") as file:
        file.write(text + "\n")

def get_memory():

    with open("history.txt","r") as file:
        return file.read()