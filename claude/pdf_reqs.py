import os
import prompts
import anthropic
import fitz


def main():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    doc = fitz.open('..\\resources\\requirements.pdf')
    reqs = ""
    for page in doc: 
        text = page.get_text() 
        reqs += text

    prompt = f"Use cases: {reqs}. {prompts.prompt_sample}"

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    cases = message.content[0].text
    print(cases)

    with open("results\\test_cases_reqs.csv", "w") as file:
        file.write("sep=;\n")  # User-friendly Excel
        file.write(cases)

if __name__ == "__main__":
    main()
