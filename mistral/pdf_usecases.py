import os
import fitz

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    doc = fitz.open('..\\resources\\usecases.pdf')
    usecases = ""
    for page in doc: 
        text = page.get_text() 
        usecases += text
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-medium"  # the best one.

    client = MistralClient(api_key=api_key)
    testing_types = ["functional", "usability", "compatibility", "negative"]
    columns = ["Title", "Automation Type", "Estimate", "Preconditions", "Priority", "Steps(Step)", "Steps(Expected Results)", "Type"]
    prompt = f"You are a QA Engineer. Write a list of test cases based on requirements {usecases}. Outcome should be ready for instant converting to the csv file with ; as a separator. Do not add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, do not add extra blank lines. DO NOT add testing type values to the test cases descriptions. The output should be compatible with Testrail. Estimate should be measured in seconds, for example 30s, but it can be more or less. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered."

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]# remove " symbols
    with open("results\\test_cases_use_cases.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
