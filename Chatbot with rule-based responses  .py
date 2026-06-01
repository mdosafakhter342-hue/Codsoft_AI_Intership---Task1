def chatbot():
    print("🤖 Rule-Based Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you?")

        elif "how are you" in user:
            print("Bot: I'm fine, thank you!")

        elif "your name" in user:
            print("Bot: I am a Rule-Based Chatbot.")

        elif "help" in user:
            print("Bot: I can answer simple questions like greetings, name, and time.")

        elif "time" in user:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: Current time is {current_time}")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()