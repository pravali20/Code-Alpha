import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define the conversation patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you!", "I'm fine, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "Alright, good to know!",]
    ],
    [
        r"quit",
        ["Bye, take care!", "It was nice talking to you. See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you rephrase that?",]
    ],
]

# Reflections for pronouns and verbs
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Function to start the chatbot
def chatbot():
    print("Hi, I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main entry point
if __name__ == "__main__":
    chatbot()
