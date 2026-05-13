# Task 1: Simple Rule-Based Chatbot for CODSOFT

print("RuleBot: Hello! I am a chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")
    user = user.lower()  # make it lowercase so Hi = hi
    
    if user == "hi" or user == "hello":
        print("RuleBot: Hi there! How can I help?")
    
    elif user == "how are you":
        print("RuleBot: I'm just code, but I'm doing great!")
    
    elif user == "what is your name":
        print("RuleBot: I'm RuleBot, your CODSOFT chatbot.")
    
    elif user == "what is codsoft":
        print("RuleBot: CODSOFT provides internships in AI and other tech fields!")
    
    elif user == "help":
        print("RuleBot: You can say hi, ask how I am, or say bye.")
    
    elif user == "bye":
        print("RuleBot: Goodbye! Have a nice day.")
        break  # this stops the program
    
    else:
        print("RuleBot: Sorry, I don't understand. Type 'help'.")