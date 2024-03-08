import os
import prompts
import cloudmersive_ocr_api_client


def main():
    pic = ""
    cloudmersive_api_key = "161c6cfc-bd4d-474f-a2fe-518e99a36041"
    configuration = cloudmersive_ocr_api_client.Configuration()
    configuration.api_key['Apikey'] = cloudmersive_api_key
    api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
    image_file = '..//resources//design.png'
    api_response = api_instance.image_ocr_post(image_file)
    texts_from_pics = (api_response._text_result.replace('\n', ' '))  # get texts from the image

    #print(texts_from_pics.replace('\n', ' '))

    prompt = f"UI elements, links and forms: {texts_from_pics}. {prompts.prompt_sample}."
    print(prompt)
    os.system(f'ollama run codellama:7b-instruct {prompt} > results/test_cases_pic.csv')

if __name__ == "__main__":
    main()
