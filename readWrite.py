# Import deque from collections module
from collections import deque
# Import json module
import json

# Read file function
def readFile(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return lines

# Write file function
def create_an_intent(questions, answers, file_delimiter):
    intent = {
      "tag": "question",
      "patterns": [],
      "responses": []
    }

    # i = len(questions)
    # print(i, "questions")
    # while i > 0:
    #     item = questions.popleft()
    #     if(item != file_delimiter):
    #         intent["patterns"].append(item)
    #     else:
    #         i = len(answers)
    #         print(i, "answers")
    #         while i > 0:
    #             item = answers.popleft()
    #             if(item != file_delimiter):
    #                 intent["responses"].append(item)
    #             else:
    #                 i = 0
    # return intent
    
    q = True
    a = True

    while q or a:
        q_item = questions.popleft() if (len(questions) > 0 and q == True) else file_delimiter
        a_item = answers.popleft() if (len(answers) > 0 and a == True) else file_delimiter
        if q_item != file_delimiter:
            intent["patterns"].append(q_item.strip())
        else:
            q = False
        
        if a_item != file_delimiter:
            intent["responses"].append(a_item.strip())
        else:
            a = False
    return intent


# Refine data function
def refine_read_file_data(train_Qs, train_As, file_delimiter):
    questions = deque(train_Qs)
    answers = deque(train_As)
    intents = []
    while len(questions) > 0 and len(answers) > 0:
        intents.append(create_an_intent(questions,answers,file_delimiter))
    return intents
        

# Main function
def main():
    questions = readFile('training_texts/Training text.txt')
    answers = readFile('training_texts/answers_training.txt')

    data = {
        "intents" : refine_read_file_data(questions,answers,'\n')
    }

    # write to json file extracted data
    with open("bom_deus.json", "w") as f:
        json.dump(data, f, indent=4)


#Using the special variable
#__name__

if __name__ == "__main__":
    main()