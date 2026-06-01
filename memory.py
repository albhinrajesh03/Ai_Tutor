def set_memory(role, message, count):
    text=f"{role}:{message}"

    if count%2==0:
        text=text + "\n---END---\n"

    with open("history.txt","a") as file:
        file.write(text + "\n")



def get_memory(limit=4):

    with open("history.txt","r") as file:
        data=file.read()

        conversation=data.split("---END---")

        return "\n".join(conversation[-limit:])
