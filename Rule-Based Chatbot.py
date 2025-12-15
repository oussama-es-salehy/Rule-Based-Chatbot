import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

# Step 1: Define intents and keywords
intents = {
    "greeting": ["hello", "hi", "hey"],
    "opening_hours": ["open", "opening", "hours", "time"],
    "pricing": ["price", "cost", "how", "much"],
}

# Step 2: Define responses
responses = {
    "greeting": "Hello! How can I help you today?",
    "opening_hours": "We are open from 9 AM to 6 PM, Monday to Friday.",
    "pricing": "Our pricing starts at $10 per month.",
    "default": "Sorry, I didn't understand that. Can you please rephrase?"
}

# Step 3: Chatbot function
def rule_based_chatbot(user_input):
    tokens = word_tokenize(user_input.lower())

    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in tokens:
                return responses[intent]

    return responses["default"]

# Step 4: Run chatbot (terminal interaction)
if __name__ == "__main__":
    print("Rule-Based Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = rule_based_chatbot(user_input)
        print("Bot:", response)
