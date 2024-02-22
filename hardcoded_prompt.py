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
    testing_types = ["functional", "usability", "compatibility"]
    columns = ["number", "short description", "priority", "testing type", "steps", "expected results"]
    prompt = f"Write a list of test cases for {sut} with {sut_elements}. Without greetings etc, just the test cases list. Outcome should be in a .csv file format. Columns: {columns}. One step is one action."

    chat_response = client.chat(
        model=model,
        messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    print(cases)
    with open("test_cases_3.csv", "w") as file:
        file.write("sep=\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
