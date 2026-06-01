def set_memory(role, message, count):
    text=f"{role}:{message}"

    if count%2==0:
        text=text + "\n---END---\n"

    with open("history.txt","a") as file:
        file.write(text + "\n")



def get_memory(limit=4):

    with open("history.txt","r") as file:
        data=file.read()

        conversations=data.split("---END---")

        clean_convo=[]

        for c in conversations:
            c.strip()

            if c:
                clean_convo.append(c)

        return "\n".join(clean_convo[-limit:])
