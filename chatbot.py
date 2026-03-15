# Basic Rule-Based Chatbot (Single File)

def chatbot():

    print("🤖 Chatbot Started!")
    print("Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user_input == "who made you":
            print("Bot: I was created using Python.")

        elif user_input == "good morning":
            print("Bot: Good morning!")

        elif user_input == "good evening":
            print("Bot: Good evening!")

        elif user_input == "thanks" or user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")


# Run chatbot
chatbot()
