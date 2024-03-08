import os
import prompts

import anthropic


def main():
    # model = "mistral-medium"  # the best one.
    # client = MistralClient(api_key=api_key)
    # 

    # chat_response = client.chat(
        # model=model,
        # messages=[ChatMessage(role="user", content=prompt)],
    # )
    # cases = chat_response.choices[0].message.content
    # if cases[0] == '"':
        # cases = cases[1:-1]# remove " symbols

    # with open("results\\test_cases_prompt.csv", "w") as file:
        # file.write("sep=;\n")  # User-friendly Excel
        # file.write(cases)

    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    prompt = f"{prompts.sut}. {prompts.prompt_sample}"
    
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
        #    {"role": "user", "content": prompt}
            {"role": "user", "content": 'Hi!'}
        ]
    )
    print(message.content[0].text)

if __name__ == "__main__":
    main()
