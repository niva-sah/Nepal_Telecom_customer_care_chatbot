import os

def load_text():
    data = ""

    data_folder = "chatbot/data"

    for filename in os.listdir(data_folder):
        filepath = os.path.join(data_folder, filename)

        if os.path.isfile(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data += f.read() + "\n"

    return data