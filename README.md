# AutoGen_testing.v.01

First, run the LLM servers needed.
Im using FastChat
link - https://github.com/lm-sys/FastChat
or
pip install fastchat

________________________________________
Step 1: Start the Controller
Run the FastChat controller module:

python -m fastchat.serve.controller

________________________________________
Step 2: Choose the Model
Choose the specific language model you want to use. For example, to use the vicuna-7b-v1.5-16k model:

I use choose
python -m fastchat.serve.model_worker --model-path lmsys/vicuna-7b-v1.5-16k

________________________________________
Step 3: Handle API Requests
Start the FastChat API server to handle requests:

python -m fastchat.serve.openai_api_server --host localhost --port 8000

________________________________________

Running AutoGen Script
With FastChat running in the background, you can now run your AutoGen script to interact with the language model.


Run Script.

EG only.




__________________________


I started using LM Studio
its so simple
link - https://lmstudio.ai/
download the software
download the Model you want.
There you go done, you can start chatting to AI
there is a option to use the software as an api too..
