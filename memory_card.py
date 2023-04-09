from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle
class Question():
    def __init__(self, question, right_answer, wrong_1, wrong_2, wrong_3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list = []
question_list.append(Question('Когда распался СССР', '1991', '1992', '1990', '1999'))
question_list.append(Question('Кем работает отец Вовочки', 'программистом чего-то', 'пионистом в борделе', 'военным', 'полицейским'))
question_list.append(Question('Что сделал дед Вовочки, когда получил пенсию', 'пропил её', 'купил обувь', 'купил продукты', 'отдал внукам'))
shuffle(question_list)
app = QApplication([])
widget = QWidget()
widget.setWindowTitle('Memory card')
text = QLabel('Какой национальности не существует?')
btn1 = QPushButton('Ответить')
rgb = QGroupBox('Варианты ответов')
btn2 = QRadioButton('Энцы')
btn3 = QRadioButton('Смурфы')
btn4 = QRadioButton('Чулымы')
btn5 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)
RadioGroup.addButton(btn5)
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line_main = QVBoxLayout()
line2.addWidget(btn2)
line2.addWidget(btn3)
line3.addWidget(btn4)
line3.addWidget(btn5)
line1.addLayout(line2)
line1.addLayout(line3)
AnswerGroup = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_current = QLabel('Правильный отает')
Ans_line = QVBoxLayout()
Ans_line.addWidget(lb_result)
Ans_line.addWidget(lb_current)
AnswerGroup.setLayout(Ans_line)
AnswerGroup.hide()
line_main.addWidget(text)
line_main.addWidget(rgb)
line_main.addWidget(AnswerGroup)
line_main.addWidget(btn1)
rgb.setLayout(line1)
widget.setLayout(line_main)
def show_result():
    rgb.hide()
    AnswerGroup.show()
    btn1.setText('Следующий вопрос')
def show_question():
    AnswerGroup.hide()
    RadioGroup.setExclusive(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    btn5.setChecked(False)
    RadioGroup.setExclusive(True)
    rgb.show()
    btn1.setText('Ответить')
def start():
    if btn1.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answers = [btn2, btn3, btn4, btn5]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    text.setText(q.question)
    lb_current.setText(q.right_answer)
    show_question()
def next_question():
    widget.num_of_question += 1
    if widget.num_of_question == len(question_list):
        widget.num_of_question = 0
    q = question_list[widget.num_of_question]
    ask(q)
def check_answer():
    if answers[0].isChecked() == True:
        lb_result.setText('Правильно!')
    else:
        lb_result.setText('Неверно!')
    show_result()
widget.num_of_question = -1
next_question()
btn1.clicked.connect(start)
widget.show()
app.exec()