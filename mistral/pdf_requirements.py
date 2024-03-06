import os
import fitz
import prompts

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    doc = fitz.open('..\\resources\\requirements.pdf')
    reqs = ""
    for page in doc: 
        text = page.get_text() 
        reqs += text
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-medium"  # the best one.

    client = MistralClient(api_key=api_key)

    prompt = f"Requirements: {reqs}. {prompts.prompt_sample}"
    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]# remove " symbols
    with open("results\\test_cases_reqs.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
