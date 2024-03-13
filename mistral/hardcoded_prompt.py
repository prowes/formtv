import os
import prompts

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-medium"  # the best one.
    client = MistralClient(api_key=api_key)
    #prompt = f"{prompts.sut}. {prompts.prompt_sample}"
    prompt = "Please give me a test plan for the login screen"

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]# remove " symbols

    print(cases)
    #with open("results\\test_cases_prompt.csv", "w") as file:
    with open("results\\test_plan.txt", "w") as file:
     #   file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
