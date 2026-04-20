from openai import OpenAI

client = OpenAI()

prompts = [
    "List 3 benefits of regular exercise.",
    "Explain the benefits of exercise to someone who hates working out in a friendly tone."
]

for prompt in prompts:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("\nPROMPT:", prompt)
    print("RESPONSE:", response.output_text)