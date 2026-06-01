# 🤖 Rule-Based Chatbot

A simple Rule-Based Chatbot built using Python. The chatbot responds to predefined user inputs such as greetings, name queries, help requests, and current time.

## Features

- Responds to greetings (Hi, Hello, Hey)
- Answers "How are you?"
- Tells its name
- Provides help information
- Shows current system time
- Exits when the user types `bye`

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Save the code in a file named `chatbot.py`.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the following command:

```bash
python chatbot.py
```

## Example Usage

```text
🤖 Rule-Based Chatbot
Type 'bye' to exit.

You: hello
Bot: Hello! How can I help you?

You: how are you
Bot: I'm fine, thank you!

You: time
Bot: Current time is 14:35:20

You: bye
Bot: Goodbye! Have a nice day.
```

## Project Structure

```text
├── chatbot.py
└── README.md
```

## Working

The chatbot continuously takes user input using a `while` loop and checks the input against predefined rules using `if-elif-else` statements. Based on the matched condition, it returns the appropriate response.

## Future Improvements

- Add more conversation rules
- Integrate Natural Language Processing (NLP)
- Create a graphical user interface (GUI)
- Store chat history
- Add voice interaction

## Author

Developed using Python as a beginner-friendly chatbot project.
