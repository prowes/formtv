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
    columns = ["number", "short description", "priority", "steps", "expected results"]
    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=f"Write a list of test cases for the {sut} with {sut_elements}. Please without greetings etc, just the test cases list. The outcome should be in a .csv file format, so it could be Excel-friendly. Columns: {columns}. One step is one action.")],
    )
    cases = chat_response.choices[0].message.content
    print(cases)
    with open("test_cases_3.csv", "w") as file:
        file.write("sep=\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
