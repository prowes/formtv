import os
import prompts
import anthropic
import cloudmersive_ocr_api_client


def main():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    pic = ""
    cloudmersive_api_key = os.environ["CLOUDMERSIVE_API_KEY"]
    configuration = cloudmersive_ocr_api_client.Configuration()
    configuration.api_key['Apikey'] = cloudmersive_api_key
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    image_file = '..//resources//design.png'
    api_response = api_instance.image_ocr_post(image_file)
    texts_from_pics = (api_response._text_result.replace('\n', ' '))  # get texts from the image

    prompt = f"UI elements, links and forms: {texts_from_pics}. {prompts.small_prompt}."

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    cases = message.content[0].text
    print(cases)

    with open("results\\test_cases_small_prompt.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
