# Chatbot Training Data Formatter
# README

## Overview
This Python script is designed to generate an `intents.json` file for training a chatbot. The script reads questions and answers from two separate text files, groups them into intents, and writes the intents to a JSON file. Each intent consists of a list of patterns (questions) and a list of responses (answers). The chatbot can use this file to learn conversation patterns, understand how certain questions might be phrased, and learn possible ways to answer them.

### Chatbot trained with resulting data
https://mediafiles.botpress.cloud/a65bb32e-7d9c-40c0-8615-6fb2aa1b6489/webchat/bot.html - In Progress

Please, be a bit patient with it

## How to Use
1. Prepare two text files: one containing the questions and the other containing the answers. Each question and answer should be on a separate line. The questions and answers should be in the same order in both files.

2. Update the `readFile` function calls in the `main` function with the paths to your question and answer files:

```python
questions = readFile('path_to_your_question_file')
answers = readFile('path_to_your_answer_file')
```

3. Run the script. The script will read the questions and answers, group them into intents, and write the intents to a JSON file named `bom_deus.json`.

## Functions
- `readFile(file)`: Reads a text file and returns a list of lines.
- `create_an_intent(questions, answers, file_delimiter)`: Creates an intent from the given questions and answers. An intent is a dictionary with a 'tag', 'patterns', and 'responses'. The 'patterns' are the questions and the 'responses' are the answers.
- `refine_read_file_data(train_Qs, train_As, file_delimiter)`: Refines the read file data into intents.
- `main()`: The main function that reads the question and answer files, creates the intents, and writes them to a JSON file.

## Output
The output is a JSON file named `bom_deus.json`. This file contains the intents created from the questions and answers. Each intent is a dictionary with a 'tag', 'patterns', and 'responses'. The 'patterns' are the questions and the 'responses' are the answers. This file can be used to train a chatbot to understand and respond to various conversation patterns.

## Note
This script uses the `collections.deque` class for efficient removal of elements from the front of the list (which is used in the `create_an_intent` function). It also uses the `json` module to write the intents to a JSON file. Make sure these modules are available in your Python environment.
