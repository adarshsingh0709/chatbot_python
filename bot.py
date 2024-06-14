import datetime
import requests

class ChatBot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a bot, but I'm doing fine! How about you?",
            "what's your name": "I'm a chatbot created to assist you. You can call me ChatBot!",
            "what can you do": "I can chat with you and answer basic questions. Try asking me something!",
            "how old are you": "I'm timeless, existing beyond the constraints of age.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "thank you": "You're welcome! I'm here to help.",
            "bye": "Goodbye! Have a great day!",
            "what's the time": self.get_time,
            "give me a quote": self.get_quote,
            "default": "I'm sorry, I don't understand that. Can you rephrase?"
        }

    def get_response(self, user_input):
        response = self.responses.get(user_input.lower(), self.responses["default"])
        if callable(response):
            return response()
        return response

    def get_time(self):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    def get_quote(self):
        try:
            response = requests.get("https://api.quotable.io/random")
            if response.status_code == 200:
                quote_data = response.json()
                return f"Here's a quote for you: \"{quote_data['content']}\" - {quote_data['author']}"
            else:
                return "Sorry, I couldn't fetch a quote at the moment."
        except Exception as e:
            return f"An error occurred while fetching the quote: {e}"

    def chat(self):
        print("ChatBot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("ChatBot: " + self.responses["bye"])
                break
            response = self.get_response(user_input)
            print("ChatBot: " + response)

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat()
