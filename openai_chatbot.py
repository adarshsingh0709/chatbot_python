import openai

class OpenAIChatBot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",  # You can use "gpt-3.5-turbo" if it's available
            prompt=f"User: {user_input}\nChatBot:",
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    def chat(self):
        print("ChatBot: Hi! I'm your friendly chatbot powered by OpenAI. Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("ChatBot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print("ChatBot: " + response)

if __name__ == "__main__":
    # Replace 'your-api-key' with your actual OpenAI API key
    api_key = "your-api-key"
    chatbot = OpenAIChatBot(api_key)
    chatbot.chat()
