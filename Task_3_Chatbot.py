import nltk
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')



# Download tokenizer (runs once)
nltk.download('punkt')

# Chatbot knowledge
responses = {
    "hi": "Hello! How can I help you?",
    "hello": "Hi there!",
    "how are you": "I am fine. What about you?",
    "what is your name": "I am an AI chatbot.",
    "what is nlp": "NLP means Natural Language Processing.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day."
}

def get_response(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for question in responses:
        question_tokens = word_tokenize(question)

        if all(word in tokens for word in question_tokens):
            return responses[question]

    return "Sorry, I did not understand that."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break

    response = get_response(user_input)
    print("Chatbot:", response)
