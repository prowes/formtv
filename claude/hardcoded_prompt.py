import os
import prompts
import anthropic


def main():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = f"{prompts.sut}. {prompts.prompt_sample}"

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=3072,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    cases = message.content[0].text
    print(cases)

    with open("results\\test_cases_prompt.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
