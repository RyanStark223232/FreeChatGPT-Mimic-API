<h1> FreeChatGPT-Mimic-API </h1>

Welcome to this exciting python flask app! With this app, you can easily transform the free ChatGPT trial page into an API that will revolutionize the way you work.

API allows you to seamlessly integrate ChatGPT into any simple script, giving you the power to perform tasks such as writing resumes, classifying local directories, and simple Q&A.
Especially for people living in places where ChatGPT is now accessible and have a hard time paying for the service. 

To ensure that our app is used ethically, we have intentionally omitted the feature of automatic login, preventing individuals from making mass requests. 
Hope you all value the importance of responsible usage and allow everyone to make their life slightly easier with this simple hack.

<h2> Setup </h2>

<ol>
<li>Step 0: Get an OpenAI account.</li>
<li>Step 1: Install the dependcies, preferably in a new virtual environment

</li>

   ```bat
   git clone https://github.com/RyanStark223232/FreeChatGPT-Mimic-API/
   cd FreeChatGPT-Mimic-API
   pip install requirements.txt
   ```
   
<li>Step 2: Setup Selenium Chrome Driver by following https://chromedriver.chromium.org/getting-started, or just ask ChatGPT. 
We all deserve to make our life a bit easier, right?</li>
<li>Step 3: Input your username and password in the id_pass.txt </li>
<li>Step 4: Run the following command. You should see a small chrome window opening and automatically input all the information </li>
   
```bat
python app.py
```
   
Wait until you see the following message pops up and DO NOT close the chrome window

```bat
Running on http://127.0.0.1:5000
```
   
</ol>

And DONE! Your api is now running.

<h2>API</h2>

<h3>API: generate</h3>

* Descritpion: This will basically type into the textarea, press send, and wait till the response is completed. Note that if you don't call new_chat, 
it still keeps all the conversation history <br />
* Endpoint: `http://127.0.0.1:5000/generate` <br />
* Method: `GET` <br />
* URL Example: http://localhost:5000/generate?prompt="What%20was%20the%20name%20of%20the%203rd%20US%20president?"
* Request Body:

```json
{"prompt": "Who is the 3rd president in US?"} 
```

* Response Body:

```json
{"response": "The name of the 3rd President of the United States was Thomas Jefferson. He served as the President from 1801 to 1809, after being elected in the 1800 presidential election. Jefferson was one of the Founding Fathers of the United States, and is known for his role in drafting the Declaration of Independence."}
```

<h3>API: new_chat</h3>

* Endpoint: `http://127.0.0.1:5000/new_chat` <br />
* Method: `GET` <br />
* URL Requset Example: http://localhost:5000/new_chat
* Request Body: N/A <br />
* Response Body:

```json
{"status": "Created New Chat"}
```
