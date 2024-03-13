import os
import prompts
import anthropic


def main():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    #prompt = f"{prompts.sut}. {prompts.prompt_sample}"
    prompt = f"You are a part of the team who is going to try different available modern AI models to come up with an AI-based solution for the finnish MTV Katsomo company. The solution is intended to automate the daily routine of QA engineers. It should generate test cases based on the software description, design drafts, use cases and other documents. Your purpose right now is to write an introduction for the document with the description of this task, this product and all the comparison, selection and scripts development process. The instruction should fit one A4 page in Word."

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    cases = message.content[0].text
    print(cases)

    with open("results\\desc.txt", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
