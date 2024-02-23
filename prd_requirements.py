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
    columns = ["number", "short description", "priority", "testing type", "steps", "expected results"]
    prompt = f"Write a list of test cases based on requirements {reqs}, but not limited to them. Outcome should be ready for instant convertation to the csv file with ; as a separator. Don't add any other text. Use different testing types, for example {testing_types}. Use columns {columns}. One line is one test case, don't add extra blank lines."

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content[1:-1]  # remove " symbols
    print(cases)
    with open("test_cases_reqs.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
