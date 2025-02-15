# Quirky Chatbot

## Description
Quirky Chatbot is a fun and interactive chatbot built using **PyQt5** for the GUI and **TextBlob** for sentiment analysis. The bot engages in casual conversation, assigns a quirky nickname, and discusses different topics while analyzing user sentiment.

## Features
- Interactive GUI built with PyQt5
- Asks for the user's name and assigns a nickname
- Analyzes user sentiment using TextBlob
- Discusses multiple topics with user opinions
- Ends the conversation and closes when the user types **"exit"**

## 🖥️ Technologies Used

- **Python** 
- **Tkinter** - GUI framework
- **Pandas** - Data manipulation and storage
- **Matplotlib** - Data visualization
- **tkcalendar** - Calendar widget for date selection

## Requirements
Ensure you have Python installed and install the required libraries using:

```sh
pip install PyQt5 textblob
```

## How to Run
Run the chatbot using:

```sh
python chatbot.py
```

## Usage
1. The chatbot starts by asking for your name.
2. It assigns or asks for a nickname.
3. It asks how you're feeling and analyzes your response.
4. It discusses topics and evaluates your opinions using sentiment analysis.
5. Type **"exit"** at any point to end the conversation and close the app.

## Exit Conditions
- Typing **"exit"** at any time will close the chatbot.
- The chatbot will automatically close after all topics are discussed.

## 📸 Screenshots

| ChatBot  |----------------|
| ![dashboard](./Screenshot%20(149).png) | 

---
## Example Interaction
```
Bot: Hello hooman, what's your name?! 🤔
You: Alex
Bot: Do you have a nickname?! [y/n] 🙃
You: y
Bot: What's your nickname?!😍
You: Ace
Bot: Good to meet you Ace 😁
Bot: How are you today Ace?
You: I'm feeling great!
Bot: Glad you are doing well! 😊
Bot: What do u think about Marvel?
You: I love Marvel movies!
Bot: OMG, you really love Marvel and you are a bit biased!
...
Bot: It was good talking to u Ace, I gotta go now!
(Closes automatically)
```

