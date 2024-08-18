from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

client = OpenAI(api_key=my_key_openai)

fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:emreyz:orhan-veli-siir:93r1jeZT"

response = client.models.delete(model=fine_tuned_model_name)

print(response)

list = client.models.list()

for model in list.data:

    print(model.id)