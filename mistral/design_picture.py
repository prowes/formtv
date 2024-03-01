from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

import os
import cloudmersive_ocr_api_client


def main():
    pic = ""
    mistral_api_key = os.environ["MISTRAL_API_KEY"]
    cloudmersive_api_key = os.environ["CLOUDMERSIVE_API_KEY"]
    #model = "mistral-small"
    #model = "mistral-tiny"
    model = "mistral-medium"  # the best one.

    configuration = cloudmersive_ocr_api_client.Configuration()
    configuration.api_key['Apikey'] = cloudmersive_api_key
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    image_file = 'design.png' 
    api_response = api_instance.image_ocr_post(image_file)
    texts_from_pics = (api_response._text_result)  # get texts from the image

    client = MistralClient(api_key=mistral_api_key)
    testing_types = ["functional", "usability", "compatibility", "negative"]
    columns = ["Title", "Automation Type", "Estimate", "Preconditions", "Priority", "Steps(Step)", "Steps(Expected Results)", "Type"]
    prompt = f"You are a QA Engineer. Write a list of test cases. UI contains elements with the following signs: {texts_from_pics}. Outcome should be ready for instant converting to the csv file with ; as a separator. Do not add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, do not add extra blank lines. DO NOT add testing type values to the test cases descriptions. The output should be compatible with Testrail. Estimate should be measured in seconds, for example 30s, but it can be more or less. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered."

    chat_response = client.chat(
       model=model,
       messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    print(cases)
    if cases[0] == '"':
        cases = cases[1:-1]  # remove " symbols
    with open("test_cases_med.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
