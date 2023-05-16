from flask import Flask, request
from ChatGPT_Mimic_API import ChatGPT_Mimic_API

with open("id_pass.txt", "r") as fp:
    splited = fp.read().split("\n")
    username, password = splited[0], splited[1]
gpt = ChatGPT_Mimic_API(username, password)
gpt.login()

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    prompt = request.args.get('prompt')
    print(f"*** Received Prompt: {prompt}")
    gpt.fill_textarea(prompt, "textarea[placeholder='Send a message.']")
    gpt.click_button("button[class*='bottom']")
    print("*** Waiting for Generation")
    gpt.wait_for_generate()
    response = gpt.get_response()
    print(f"*** Response: {response}")
    return {"response": response}
    
@app.route('/new_chat', methods=['GET'])
def new_chat():
    if gpt.new_chat():
        return {"status": "Created New Chat"}

if __name__ == '__main__':
    app.run()