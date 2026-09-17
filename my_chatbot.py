# Simple Bank Chatbot - Rule Based
# NGCC Software Technologies
print("🧾 Welcome to Python Bank Chatbot!")
print("By Mohammed Hasnain")
print("Type 'exit' anytime to leave the chat.\n")

# Pre-defined Q&A
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What banking help do you need?",
    "how to open an account": "You can open an account by visiting the nearest branch with your KYC documents.",
    "check balance": "You can check your balance via net banking or by visiting an ATM.",
    "what is the loan interest rate": "Our personal loan interest rates start from 10.5% per annum.",
    "how to apply for a loan": "You can apply online on our website or visit your nearest branch.",
    "cheque book request": "You can request a cheque book using net banking or by visiting a branch.",
    "branch timings": "Our branches are open from 9:30 AM to 4:00 PM, Monday to Friday.",
    "bye": "Thank you for banking with us. Have a great day!"
}

def chatbot():
    while True:
        user_input = input("👤 You: ").lower()

        if user_input == 'exit':
            print("🤖 Bot: Thank you for chatting with us. Goodbye!")
            break

        response = responses.get(user_input,
                    "I'm sorry, I didn’t understand that. You can ask about account opening, loans, balance, etc.")
        print(f"🤖 Bot: {response}")

chatbot()