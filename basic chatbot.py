# Internship Task - Rule Based Chatbot

print("=" * 45)
print("        🤖 Welcome to SmartBot!")
print("=" * 45)
print("You can ask me simple questions.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey", "hii"]:
        print("Bot: Hello! 👋 Nice to meet you.")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! 😊 Thanks for asking.")

    # Bot name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I'm SmartBot, a basic Python rule-based chatbot.")

    # What can you do
    elif "what can you do" in user_input:
        print("Bot: I can answer simple questions and have a basic conversation.")

    # Programming
    elif "python" in user_input:
        print("Bot: Python is a popular and beginner-friendly programming language.")

    # Internship
    elif "internship" in user_input:
        print("Bot: Internships help students gain practical experience and skills.")

    # Study
    elif "study" in user_input:
        print("Bot: Regular practice and consistency can improve your learning.")

    # Time
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: The current time is", current_time)

    # Thanks
    elif "thank" in user_input:
        print("Bot: You're welcome! 😊")

    # Help
    elif user_input == "help":
        print("\nBot: You can try questions like:")
        print("- Hello")
        print("- How are you?")
        print("- What is your name?")
        print("- Who are you?")
        print("- What can you do?")
        print("- Tell me about Python")
        print("- Tell me about internship")
        print("- What should I do to study?")
        print("- What is the time?")
        print("- Thank you")
        print("- Bye")

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! 👋 Have a great day!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that question yet.")
        print("Bot: Type 'help' to see what I can answer.")

print("\nThank you for using SmartBot!")
