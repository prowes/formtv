import os
import fitz


def main():
    doc = fitz.open("..\\resources\\usecases.pdf")
    usecases = ""
    for page in doc:
        text = page.get_text()
        text = ' '.join(text.split())
        usecases += text

    testing_types = "functional, usability, compatibility, negative"
    columns = "Number, Priority, Description, Testing type, Steps, Expected results"
    prompt = f"You are a QA Engineer. Write a list of test cases based on use cases {usecases}. Outcome should be ready for instant converting to the csv file with semicolon as a separator. Do not add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, do not add extra blank lines. DO NOT add testing type in the Description column. In Steps, each step is one numbered action like 1, 2, etc, separate every step with a comma ONLY, do not add semicolon sign there. In Expected results column, text for each case should be splitted and not numbered. Test cases numeration should be like 1, 2, 3 etc"
    #print(prompt)
    os.system(f'ollama run codellama:7b-instruct {prompt} > test_use_cases.csv')
    #os.system(f'"{prompt}" > test_use_cases.csv')

if __name__ == "__main__":
    main()
