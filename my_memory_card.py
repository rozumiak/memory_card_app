

print("Hello world!")




# Імпорт потрібних класів із бібліотеки PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QButtonGroup)

from random import shuffle, randint

class Question():
    
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []

question_list.append(
    Question("2+2?", "4", '421412', '112', "42424")
)
question_list.append(
    Question("Best pokemon?", "Pikachu", 'Bulbasavr', 'Pegeot', "Ghost")
)
question_list.append(
    Question("Best car?", "Toyota", 'BMW', 'Dacia', "Lanos")
)

# Створюємо головний застосунок (обов’язково для PyQt5)
app = QApplication([])


# Створюємо головне вікно програми
window = QWidget()
window.resize(800, 500)  # Розмір вікна
window.setWindowTitle("Memory card")  # Заголовок вікна


# Створюємо основні елементи інтерфейсу
question = QLabel("переклади англійською")  # Текст питання
btn_ok = QPushButton("Answer")  # Кнопка для відповіді


# === ГРУПА З ВАРІАНТАМИ ВІДПОВІДЕЙ ===
RadioGroupBox = QGroupBox("Варіанти відповідей")


# Створюємо радіокнопки (можна обрати лише одну)
rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


# --- Внутрішній макет для кнопок ---
ans_hline = QHBoxLayout()   # Горизонтальне розташування
ans_vline1 = QVBoxLayout()  # Вертикальна колонка 1
ans_vline2 = QVBoxLayout()  # Вертикальна колонка 2


# Додаємо кнопки в колонки
ans_vline1.addWidget(rbtn1)
ans_vline1.addWidget(rbtn2)
ans_vline2.addWidget(rbtn3)
ans_vline2.addWidget(rbtn4)


# Додаємо обидві колонки у горизонтальний ряд
ans_hline.addLayout(ans_vline1)
ans_hline.addLayout(ans_vline2)


# Встановлюємо розмітку для групи з відповідями
RadioGroupBox.setLayout(ans_hline)


# === ГРУПА З РЕЗУЛЬТАТОМ ТЕСТУ ===
AnsGroupBox = QGroupBox("Test result")  # Назва рамки
lb_Result = QLabel('Are you correct or not?')  # Повідомлення про результат
lb_Correct = QLabel('the answer will be here!')  # Правильна відповідь


# Створюємо вертикальну розмітку для результатів
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)


# === ОСНОВНЕ РОЗТАШУВАННЯ ВІКНА ===


v_line = QVBoxLayout()  # Головний вертикальний макет (усе вікно)


# Горизонтальні блоки для окремих частин
h1_line = QHBoxLayout()  # для питання
h2_line = QHBoxLayout()  # для варіантів відповіді та результату
h3_line = QHBoxLayout()  # для кнопки


# --- Заповнюємо блоки ---
h1_line.addWidget(question, alignment=Qt.AlignHCenter)  # Питання по центру
h2_line.addWidget(RadioGroupBox)  # Додаємо блок із варіантами
h2_line.addWidget(AnsGroupBox)    # Додаємо блок із результатом


AnsGroupBox.hide()  # Спочатку ховаємо блок із відповідями (можна потім показати)


# Центруємо кнопку внизу
h3_line.addStretch(1)                 # Відступ зліва
h3_line.addWidget(btn_ok, stretch=2)  # Кнопка
h3_line.addStretch(1)                 # Відступ справа


# --- Збираємо всі частини разом ---
v_line.addLayout(h1_line, stretch=2)  # Питання зверху
v_line.addLayout(h2_line, stretch=8)  # Середня частина
v_line.addStretch(1)                  # Відступ


v_line.addLayout(h3_line, stretch=1)  # Кнопка знизу
v_line.addStretch(1)                  # Нижній відступ


v_line.addSpacing(5)  # Додатковий простір між елементами

########################## FUNCTION #########

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне запитання")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Answer")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn1, rbtn2, rbtn3, rbtn4]


def ask( q : Question ):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    question.setText(q.question)
    lb_Correct.setText(q.right_answer)

    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    
    if answers[0].isChecked():

        show_correct("Correct!")

        window.score += 1

        print('-Total questions: ', window.total, ' -Right answers: ', window.score)
        print('Rating: ', (window.score / window.total * 100), '%')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect!!!!")
            print('Rating: ', (window.score / window.total * 100), '%')
            


def next_question():
    window.total += 1
    print('-Total questions: ', window.total, ' -Right answers: ', window.score)
        

    cur_question = randint(0,  len(question_list) - 1 )

    q = question_list[ cur_question ]
    ask(q)


def click_OK():

    if btn_ok.text() == "Answer":
        check_answer()
    else:
        next_question()


btn_ok.clicked.connect(click_OK)


window.score = 0
window.total = 0

next_question()

# Встановлюємо головний макет для вікна
window.setLayout(v_line)


# Показуємо вікно
window.show()


# Запускаємо програму (головний цикл)
app.exec()
