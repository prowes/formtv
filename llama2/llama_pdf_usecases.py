import os
import fitz
import prompts


def main():
    doc = fitz.open('..//resources//usecases.pdf')
    usecases = ""
    for page in doc:
        text = page.get_text()
        text = ' '.join(text.split())
        usecases += text

    prompt = f"Use cases: {usecases}. {prompts.prompt_sample}"
    #print(prompt)
    os.system(f'ollama run codellama:7b-instruct {prompt} > results/test_use_cases.csv')
    #os.system(f'"{prompt}" > test_use_cases.csv')

if __name__ == "__main__":
    main()
