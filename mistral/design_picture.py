from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

import os
import prompts
import cloudmersive_ocr_api_client


def main():
    pic = ""
    mistral_api_key = os.environ["MISTRAL_API_KEY"]
    cloudmersive_api_key = os.environ["CLOUDMERSIVE_API_KEY"]
    model = "mistral-medium" # the best one.

    configuration = cloudmersive_ocr_api_client.Configuration()
    configuration.api_key['Apikey'] = cloudmersive_api_key
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    image_file = '..\\resources\\design.png'
    api_response = api_instance.image_ocr_post(image_file)
    texts_from_pics = (api_response._text_result)  # get texts from the image

    client = MistralClient(api_key=mistral_api_key)
    prompt = f"UI elements, links and forms: {texts_from_pics}. {prompts.prompt_sample}."

    chat_response = client.chat(
       model=model,
       messages=[ChatMessage(role="user", content=prompt)],
    )
    cases = chat_response.choices[0].message.content
    if cases[0] == '"':
        cases = cases[1:-1]  # remove " symbols
    with open("results\\test_cases_pic.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
