# 🏦 Simple Bank Chatbot — Rule Based

A beginner-friendly **rule-based banking chatbot built using Python**.

This project was created as a practical project after attending a **1-week AI/ML Bootcamp organized by NGCC Software Technologies, Hyderabad**.

## 👨‍💻 About This Project

After completing my Intermediate studies, I appeared for the **TG EAPCET examination** and later attended a **1-week AI/ML Bootcamp conducted by NGCC Software Technologies, Hyderabad**.

During the bootcamp, I was introduced to concepts related to **Artificial Intelligence, Machine Learning, Python, and chatbot development**.

As a practical application of what I learned, I built this simple **Bank Chatbot using Python**.

This project is a **rule-based chatbot**, meaning it matches the user's input with predefined questions and provides the corresponding response.

## 🚀 Features

* 👋 Greeting responses
* 🏦 Bank account opening information
* 💰 Balance-checking information
* 💳 Loan information
* 📝 Loan application guidance
* 📖 Cheque book request information
* 🕘 Branch timing information
* 👋 Exit command
* 💬 Interactive command-line chat

## 🛠️ Technologies Used

* **Python 3**
* **VS Code**
* Python built-in functions and data structures
* Dictionary
* Functions
* While Loop
* User Input
* Conditional Logic

No external Python libraries are required.

## 📂 Project Structure

```text
Simple_Bank_Chatbot/
│
├── bank_chatbot.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone (My Repository URL)
```

### 3. Open the Project

Open the project folder in **VS Code**.

### 4. Run the Chatbot

Open the VS Code terminal and run:

```bash
python bank_chatbot.py
```

## 💬 Example

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

## 🧠 How It Works

The chatbot stores predefined questions and answers inside a Python dictionary:

```python
responses = {
    "hello": "Hello! How can I help you today?",
    "check balance": "You can check your balance via net banking or by visiting an ATM."
}
```

When the user enters a question, the program converts it to lowercase and searches for an exact match in the dictionary.

If a matching question is found, the chatbot displays the corresponding response.

If no match is found, it displays a default message.

## 🎓 Learning Experience

This project represents one of my early practical projects while learning **Python and AI/ML concepts**.

I built it after attending a **1-week AI/ML Bootcamp organized by NGCC Software Technologies, Hyderabad**.

The bootcamp helped me understand the fundamentals and encouraged me to apply what I learned by building a working project.

## 🙏 Acknowledgement

Special thanks to **NGCC Software Technologies, Hyderabad** for organizing the AI/ML Bootcamp and providing an opportunity to learn and practice AI/ML concepts.

I would also like to thank **Syed Imran Sir** for teaching and guiding me during the bootcamp.

>
> `@NGCC-Software-Technologies.
>
> `@https://www.linkedin.com/in/syed-imran-ahmed-b38b2a21b?utm_source=share_via&utm_content=profile&utm_medium=member_android

## 👨‍💻 Author

**Mohammed Hasnain**

Student | Computer Science | AI/ML Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
