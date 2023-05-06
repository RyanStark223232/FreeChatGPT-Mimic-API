from flask import Flask, request
from ChatGPT_Mimic_API import ChatGPT_Mimic_API

gpt = ChatGPT_Mimic_API()
gpt.go_to()

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    prompt = request.args.get('prompt')
    print(f"*** Received Prompt: {prompt}")
    gpt.enter_text(prompt)
    gpt.click_send()
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