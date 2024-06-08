from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create an OpenAI client using API key and optionally, the base URL
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Priming GPT
system_prompt = """
You are a chatbot that is exceptional at playing the twenty questions game.
"""

# The first instruction that we give GPT
prompt = """
You are a chatbot that is exceptional at playing the twenty questions game, and guessing the name of the celebrity within twenty questions.

I have thought of a celebrity and your task is to guess who the celebrity is. You may do so by asking twenty or fewer questions. 
If you get it right, you stand a chance to win a thousand dollars.

Here are a few rules
- The celebrity I'm thinking of can be a Hollywood movie star or a singer
- You can only ask me yes or no questions. Alternatively, you can ask me a multiple choice question where I choose an option.
- Assume I'm always telling the truth.
- Assume if you get the answer right, I will tell you so. 
- At no point of time am I allowed to change my celebrity midway.
- When asking a question, also let yourself and me know what question number it is. In other words, keep track of the number of questions you're asking.

Me: I have thought of a celebrity. Ask me a question!

You:
"""

# Run a loop where GPT asks questions and we answer
messageHistory = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt},
]

while True:

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messageHistory,
        temperature=0.7,
    )

    messageHistory.append(response.choices[0].message)

    print(f"{response.choices[0].message.content}")
    answer = input("Your Response: ")

    messageHistory.append({
        "role": "user",
        "content": answer
    })
