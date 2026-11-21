# Simple Bank Chatbot — Python Rule-Based Project

> A beginner-friendly command-line banking chatbot built with Python during a one-week AI/ML Bootcamp at NGCC Software Technologies, Hyderabad.

## 1. Project Background

After completing my Intermediate studies, I appeared for the **TG EAPCET examination** and later attended a **1-week AI/ML Bootcamp conducted by NGCC Software Technologies, Hyderabad**.

During the bootcamp, I was introduced to concepts related to **Artificial Intelligence, Machine Learning, Python, and chatbot development**. As a practical application of what I was learning, I built this **Simple Bank Chatbot using Python during the bootcamp**.

This is a **rule-based chatbot**: it checks the user's input against predefined phrases and displays the corresponding response. It is an early learning project, not a machine-learning model or a real banking service.

## 2. Features

- Greeting responses for `hello` and `hi`
- Bank account opening information
- Balance-checking guidance
- Personal loan interest-rate information (predefined sample response)
- Loan application guidance
- Cheque book request information
- Branch timing information
- A `bye` response
- An `exit` command to end the conversation
- Interactive command-line conversation

## 3. Technology and Python Concepts

- **Python 3**
- **Visual Studio Code**
- Python dictionary (predefined question-and-answer mapping)
- Functions
- `while` loop
- User input and output
- Conditional logic
- String handling with `.lower()`
- Dictionary lookup with `.get()`

No external Python libraries are required.

## 4. How It Works

The chatbot follows a simple input-to-response flow:

```text
User enters a message
        |
        v
Convert input to lowercase
        |
        v
Check the predefined response dictionary
        |
        +---- Match found ----> Display the matching response
        |
        +---- No match -------> Display the fallback message
        |
        v
Continue until the user enters "exit"
```

The responses are stored in a Python dictionary. The program reads each message, converts it to lowercase, and uses the input as a key. If the key exists, the matching response is displayed. Otherwise, a default message is shown.

Example of the response mapping:

```python
responses = {
    "hello": "Hello! How can I help you today?",
    "check balance": "You can check your balance via net banking or by visiting an ATM."
}
```

## 5. Project Structure

```text
Simple-Bank-Chatbot/
├── my_chatbot.py
└── README.md
```

## 6. How to Run

### Step 1 — Install Python 3

Check that Python is installed:

```bash
python --version
```

### Step 2 — Clone the repository

```bash
git clone https://github.com/hasnain1522/Simple-Bank-Chatbot.git
```

### Step 3 — Open the project folder

Open the cloned folder in Visual Studio Code or a terminal.

### Step 4 — Run the chatbot

```bash
python my_chatbot.py
```

Enter one of the supported phrases to receive a response. Type `exit` to end the chat.

## 7. Example Conversation

```text
🧾 Welcome to Python Bank Chatbot!
By Mohammed Hasnain
Type 'exit' anytime to leave the chat.

👤 You: hello
🤖 Bot: Hello! How can I help you today?

👤 You: check balance
🤖 Bot: You can check your balance via net banking or by visiting an ATM.

👤 You: exit
🤖 Bot: Thank you for chatting with us. Goodbye!
```

## 8. Learning Outcomes

Building this project during the bootcamp gave me practical experience with:

- Taking input from a user and displaying output
- Organising predefined data using dictionaries
- Writing and calling a Python function
- Repeating a conversation using a `while` loop
- Applying conditions and handling an exit command
- Converting text to lowercase for consistent matching
- Providing a fallback response when an input is not recognised
- Understanding a basic rule-based chatbot conversation flow

The project helped me practise a foundational programming pattern:

**Input → Logic → Response**

## 9. Scope and Limitations

- The chatbot only recognises predefined phrases; it does not understand unrestricted natural language.
- It does not use machine learning, a trained AI model, or an LLM.
- It does not connect to a real bank, customer account, or financial database.
- It cannot perform real balance checks, transactions, loan applications, or cheque-book requests.
- Banking details, including the sample interest-rate response, are predefined illustrative text and are not live banking information.

## 10. Bootcamp Acknowledgement

Special thanks to **NGCC Software Technologies, Hyderabad**, for organising the AI/ML Bootcamp and providing the opportunity to learn and practise introductory AI/ML concepts.

I would also like to thank **Syed Imran Sir** for teaching and guiding me during the bootcamp.

- Mentor: [Syed Imran Ahmed](https://www.linkedin.com/in/syed-imran-ahmed-b38b2a21b/)

## 11. Author

**Mohammed Hasnain**  
CSE AI/ML Student

---

*An early Python project built during my AI/ML learning journey.*
