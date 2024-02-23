#!/usr/bin/env python

import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage


def main():
    api_key = os.environ["MISTRAL_API_KEY"]
    #model = "mistral-small"
    #model = "mistral-tiny"
    model = "mistral-medium"  # the best one.

    client = MistralClient(api_key=api_key)
    sut = "e-mail restore"
    sut_elements = ["email field", "send button"]
    testing_types = ["functional", "usability", "compatibility", "negative", "positive"]
    columns = ["Number", "Priority", "Description", "Testing type", "Steps", "Expected results"]
    prompt = f"Write a list of test cases for {sut} with {sut_elements}. Outcome should be ready for instant convertation to the csv file with ; as a separator. Don't add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, don't add extra blank lines. DO NOT add testing type in the Description column. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered."

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]# remove " symbols

#    print(cases)
    with open("test_cases_prompt.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
