# CodeAlpha Task 4 - Basic Chatbot
# Student Name: Are karthik
# Student ID: CA/DF1/175540

def main():
    print("CodeAlpha Chatbot - Task 4")
    print("Student: Are karthik")
    print("Type 'bye' to exit")
    print("------------------------------")

    while True:
        user = input("You: ").lower().strip()

        if user == "hello" or user == "hi" or user == "hey":
            print("Bot: Hi! How can I help you?")
        
        elif user == "how are you":
            print("Bot: I am fine, thank you")
            
        elif user == "bye":
            print("Bot: Goodbye! Have a great day")
            break
            
        else:
            print("Bot: I don't understand. Try: hello, how are you, bye")

if __name__ == "__main__":
    main()