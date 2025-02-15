from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from textblob import TextBlob
import random
import sys

class ChatbotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Quirky Chatbot')
        self.setGeometry(300, 100, 600, 700)
        self.initUI()
        self.nickname = ''
        self.conversation_stage = 0
        self.topics = [
            'football',
            'coding',
            'Marvel',
            'DC',
            'Python',
            'Computer Games',
            'pubg',
            'COD'
        ]

    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        self.chat_display = QtWidgets.QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont('Arial', 14))
        self.layout.addWidget(self.chat_display)

        self.user_input = QtWidgets.QLineEdit()
        self.user_input.setPlaceholderText('Type your response...')
        self.user_input.setFont(QFont('Arial', 14))
        self.user_input.returnPressed.connect(self.processInput)
        self.layout.addWidget(self.user_input)

        self.setLayout(self.layout)
        self.startConversation()

    def startConversation(self):
        self.addBotMessage("Hello hooman, what's your name?! 🤔")

    def processInput(self):
        user_text = self.user_input.text().strip()
        self.user_input.clear()

        if user_text.lower() == "exit":
            self.addBotMessage("Goodbye! 👋")
            QtCore.QTimer.singleShot(1000, self.close)  # Closes the app after 1 second
            return

        self.addUserMessage(user_text)

        if self.conversation_stage == 0:  # Name
            self.name = user_text
            self.addBotMessage('Do you have a nickname?! [y/n] 🙃')
            self.conversation_stage += 1

        elif self.conversation_stage == 1:  # Nickname
            if 'y' in user_text.lower():
                self.addBotMessage("What's your nickname?!😍")
                self.conversation_stage += 1
            else:
                name_list = ['killua', 'gon', 'naruto', 'idiot', 'xoxo', 'kimchi', 'fatty-mcFat', 'mother-coconuts', 'phineas',
                               'ferb', 'tennison', 'gwen', 'prarthana', 'meow', 'tuple', 'silly goose', 'babe', 'rose', 'tupperware', 'dude']
                self.nickname = random.choice(name_list)
                self.addBotMessage('I will call you ' + self.nickname + ' 😜')
                self.askHowAreYou()

        elif self.conversation_stage == 2:  # Nickname Input
            self.nickname = user_text
            self.addBotMessage('Good to meet you ' + self.nickname + ' 😁')
            self.askHowAreYou()

        elif self.conversation_stage == 3:  # Greeting
            blob = TextBlob(user_text)
            if blob.polarity > 0:
                self.addBotMessage('Glad you are doing well! 😊')
            else:
                self.addBotMessage('Sorry to hear that! 😔')
            self.askOpinions()

        elif self.conversation_stage == 4:  # Opinions
            blob = TextBlob(user_text)
            if blob.polarity > 0.5:
                self.addBotMessage("OMG, you really love " + self.current_topic)
            elif blob.polarity > 0:
                self.addBotMessage("Well, you clearly like " + self.current_topic)
            elif blob.polarity < -0.5:
                self.addBotMessage("Uff, you totally hate " + self.current_topic)
            elif blob.polarity < -0.1:
                self.addBotMessage("So you don't like " + self.current_topic)
            else:
                self.addBotMessage('That is a very neutral view on ' + self.current_topic)

            if blob.subjectivity > 0.6:
                self.addBotMessage('and you are so biased!')
            elif blob.subjectivity > 0.3:
                self.addBotMessage('and you are a bit biased!')
            else:
                self.addBotMessage('and you are quite objective, huh!')

            if len(self.topics) > 0:
                self.askOpinions()  # Ask next opinion
            else:
                self.sayGoodbye()  # End conversation

    def askHowAreYou(self):
        greetings = [
            'How are you today ' + self.nickname + '?',
            'Howdy ' + self.nickname + " friend, how you feelin' today?",
            "What's up " + self.nickname + '?',
            'Greetings ' + self.nickname + ' are you well?',
            'How are things going ' + self.nickname + '?'
        ]
        self.addBotMessage(random.choice(greetings))
        self.conversation_stage += 1

    def askOpinions(self):
        questions = [
            'What is your take on ',
            'What do u think about ',
            'How do u feel about ',
            'What do u reckon about ',
            'I would like your opinion on '
        ]
        question = random.choice(questions)
        self.current_topic = random.choice(self.topics)
        self.topics.remove(self.current_topic)
        self.addBotMessage(question + self.current_topic + '?')
        self.conversation_stage = 4

    def sayGoodbye(self):
        goodbyes = [
            'It was good talking to u ' + self.nickname + ', I gotta go now!',
            "OK I'm bored, I go watch NetFlix",
            "Bye Bye American Pie, I'm out!",
            "Catch ya later " + self.nickname
        ]
        self.addBotMessage(random.choice(goodbyes))
        QtCore.QTimer.singleShot(2000, self.close)  # Closes the app after 2 seconds

    def addBotMessage(self, message):
        self.chat_display.append(f"<b>Bot:</b> {message}")

    def addUserMessage(self, message):
        self.chat_display.append(f"<b>You:</b> {message}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    chatbot = ChatbotApp()
    chatbot.show()
    sys.exit(app.exec_())
