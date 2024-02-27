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
    columns = ["Number", "Priority", "Description", "Testing type", "Steps", "Expected results"]
    prompt = f"You are a QA Engineer. Write a list of test cases based on requirements {reqs}, but not limited to them. Outcome should be ready for instant converting to the csv file with ; as a separator. Don't add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, don't add extra blank lines. DO NOT add testing type in the Description column. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered. Test cases numeration should be like 1, 2, 3 etc"

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
