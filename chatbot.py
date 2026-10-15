print(" Chatbot: Hello! I am RuleBot.")
print(" Chatbot: You can ask me questions.")
print(" Chatbot: Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! Nice to meet you.")
    # About chatbot
    elif "tell me about yourself" in user_input or "about yourself" in user_input:
        print("Bot: I am a simple rule-based chatbot created using Python.")
        print("Bot: I answer questions using predefined rules and responses.")

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: My name is Avesh Assistant.")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I am doing great! Thank you for asking.")

    # What can you do
    elif "what can you do" in user_input:
        print("Bot: I can answer simple questions using predefined rules.")
        print("Bot: I can also have a basic conversation with you.")

    # Who created you
    elif "who created you" in user_input or "who made you" in user_input:
        print("Bot: I was created as a Python rule-based chatbot project.")

    # Programming language
    elif "which language" in user_input or "programming language" in user_input:
        print("Bot: I am created using Python programming language.")
    # AI
    elif "are you ai" in user_input or "are you artificial intelligence" in user_input:
        print("Bot: I am a basic rule-based chatbot, not a machine learning AI.")

    # Purpose
    elif "what is your purpose" in user_input or "your purpose" in user_input:
        print("Bot: My purpose is to demonstrate how rule-based chatbots work.")

    # Help
    elif "help" in user_input:
        print("Bot: Sure! You can ask me about my name, purpose, creator, or capabilities.")

    # Favorite
    elif "favorite color" in user_input:
        print("Bot: My favorite color is blue!")

    # Age
    elif "how old are you" in user_input or "your age" in user_input:
        print("Bot: I don't have a real age because I am a computer program.")

    # Location
    elif "where are you" in user_input or "where do you live" in user_input:
        print("Bot: I live inside this Python program!")

    # Study
    elif "what are you studying" in user_input:
        print("Bot: I am studying patterns in your questions using predefined rules.")

    # Python
    elif "what is python" in user_input:
        print("Bot: Python is a popular programming language used for AI, ML, web development, and automation.")

    # Chatbot
    elif "what is chatbot" in user_input:
        print("Bot: A chatbot is a computer program that communicates with users through text or voice.")

    # Rule based
    elif "what is rule based" in user_input:
        print("Bot: A rule-based chatbot uses predefined rules such as if-else conditions to respond to users.")

    # NLP
    elif "what is nlp" in user_input:
        print("Bot: NLP stands for Natural Language Processing. It helps computers understand human language.")

    # Thanks
    elif "thank you" in user_input or "thanks" in user_input:
        print("Bot: You're welcome!")

    # Good morning
    elif "good morning" in user_input:
        print("Bot: Good morning! Have a great day.")

    # Good night
    elif "good night" in user_input:
        print("Bot: Good night! Sleep well.")

    # Goodbye
    elif "bye" in user_input or "goodbye" in user_input:
        print("Bot: Goodbye! It was nice talking to you.")
        break
    # Unknown question
    else:
        print("Bot: Sorry, I don't understand that question.")
        print("Bot: Please try asking another question.")