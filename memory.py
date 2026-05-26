chat_history=[]

def set_memory(role, message):
    chat_history.append(f"{role}:{message}")

def get_memory():
    return "\n".join(chat_history)