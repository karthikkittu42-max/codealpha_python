# CodeAlpha Task 4 - Basic Chatbot
# Student Name: ARE KARTHIK
# Student ID: CA/DF1/175541

def main():
    print("CodeAlpha Chatbot - Task 4")
    print("Student: ARE KARTHIK")
    print("Type 'bye' to exit")
    print("------------------------------")

    while True:
        user = input("You: ")
        user = user.lower()

        if user == "hello":
            print("Bot: Hi")
        
        elif user == "how are you":
            print("Bot: I am fine, thank you")
            
        elif user == "bye":
            print("Bot: Goodbye")
            break
            
        else:
            print("Bot: I don't understand")

if __name__ == "__main__":
    main()
