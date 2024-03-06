import os
import fitz
import prompts


def main():
    doc = fitz.open('..//resources//requirements.pdf')
    reqs = ""
    for page in doc:
        text = page.get_text()
        text = ' '.join(text.split())
        reqs += text

    prompt = f"Requirements: {reqs}. {prompts.prompt_sample}"

    os.system(f'ollama run codellama:7b-instruct {prompt} > results/test_reqs.csv')

if __name__ == "__main__":
    main()
