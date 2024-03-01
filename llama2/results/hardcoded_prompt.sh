SUT="e-mail restore"
SUT_ELEMENTS="email field, send button"
TESTING_TYPES="functional, usability, compatibility, negative, positive"
COLUMNS="Number, Priority, Description, Testing type, Steps, Expected results"
PROMPT="You are a QA Engineer. Write a list of test cases for $SUT with $SUT_ELEMENTS. Outcome should be ready for instant converting to the csv file with ; as a separator. Don't add any other text. Use different testing types, such as, but not limited to, $TESTING_TYPES. Use columns $COLUMNS. One line is one test case, don't add extra blank lines. DO NOT add testing type in the Description column. In Steps, each step is one numbered action (1, 2, etc), separate every step with a comma ONLY, don't add ; sign there. In Expected results column, text for each case should be splitted and not numbered. Test cases numeration should be like 1, 2, 3 etc."

ollama run codellama:7b-instruct $PROMPT > test_cases_prompt.csv