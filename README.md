# AutoGen_testing.v.01

First run the LLM servers needed.
________________________________________
Step 1 - The Controller

python -m fastchat.serve.controller

________________________________________
Step 2 
choose the model.

I use chosose
python -m fastchat.serve.model_worker --model-path lmsys/vicuna-7b-v1.5-16k

________________________________________
Step 3 - Handel the requeest for api

python -m fastchat.serve.openai_api_server --host localhost --port 8000

________________________________________

