import os
import fitz


def main():
    doc = fitz.open('usecases.pdf')
    usecases = ""
    for page in doc: 
        text = page.get_text() 
        usecases += text

    client = MistralClient(api_key=api_key)
    testing_types = ["functional", "usability", "compatibility", "negative"]
    columns = ["Number", "Priority", "Description", "Testing type", "Steps", "Expected results"]
    prompt = f"You are a QA Engineer. Write a list of test cases based on requirements {usecases}. Outcome should be ready for instant converting to the csv file with ; as a separator. Don't add any other text. Use different testing types, such as, but not limited to, {testing_types}. Use columns {columns}. One line is one test case, don't add extra blank lines. DO NOT add testing type in the Description column. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered. Test cases numeration should be like 1, 2, 3 etc"

if __name__ == "__main__":
    main()
