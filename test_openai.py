import sys

print("PYTHON:", sys.executable)


from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Say hello in one sentence."
)

print(response.output_text)