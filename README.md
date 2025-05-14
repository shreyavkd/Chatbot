# Finance Chatbot

### Overview
A simple question-answering system (chatbot) that allows a user to ask questions about finance-related topics and get an answer. Uses gpt-4o-mini via OpenAI client.

---

### Prerequisites
- Python 3.7 or higher
- OpenAI API key

---

### Running
1. Clone repository:
Use the following command to clone the repository.

```bash
git clone https://github.com/shreyavkd/Chatbot.git
cd Chatbot
```

2. Set up a virtual environment:
Use the following commands to set up a virtual Python environment and install dependencies safely.

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
Run the following command to install the required python packages.

```
pip install openai python-dotenv
```

4. Providing API key:
Create a .env file in the root directory with the following line:

```
OPENAI_API_KEY={your_api_key}
```

Replace {your_api_key} with the respective gpt-4o-mini key, ensuring no whitespaces.

5. Run:
Run the chatbot with the following command. For examples of queries, please refer to the section below. To exit, type 'q' as your query.

```
python main.py
```

---

### Example Questions:
- How can I find out my credit score?
- How do interest rates affect my savings and investments?
- Why is gold considered a safe investment?
- What is the difference between debt and equity financing?

---

#### Thank you!