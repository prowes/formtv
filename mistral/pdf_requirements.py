import os
import fitz

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    doc = fitz.open('requirements.pdf')
    reqs = ""
    for page in doc: 
        text = page.get_text() 
        reqs += text
    api_key = os.environ["MISTRAL_API_KEY"]
    #model = "mistral-small"
    #model = "mistral-tiny"
    model = "mistral-medium"  # the best one.

    client = MistralClient(api_key=api_key)
    testing_types = ["functional", "usability", "compatibility", "negative", "positive"]
    columns = ["Title", "Automation Type", "Estimate", "Preconditions", "Priority", "Steps(Step)", "Steps(Expected Results)", "Type"]
    prompt = f"You are a QA Engineer. Write a list of test cases based on requirements {reqs}, but not limited to them. Outcome should be ready for instant converting to the csv file with ; as a separator. Do not add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, do not add extra blank lines. DO NOT add testing type values to the test cases descriptions. The output should be compatible with Testrail. Estimate should be measured in seconds, for example 30s, but it can be more or less. In Steps(Step), give all steps of the case, do not separate them with a semicolon. In Steps(Expected Results), give expected results after each step. Do not separate them with a semicolon."

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]# remove " symbols
    with open("test_cases_reqs.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
