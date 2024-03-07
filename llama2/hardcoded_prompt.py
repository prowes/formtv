import os
import prompts


def main():
    prompt = f"{prompts.sut}. {prompts.prompt_sample}"
    os.system(f'ollama run codellama:7b-instruct {prompt} > results/test_reqs.csv')

if __name__ == "__main__":
    main()
