# Імпорт потрібних класів із бібліотеки PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint  # для перемішування варіантів відповідей


class Question():

    def __init__(self, ques, right_answer, wrong1, wrong2, wrong3):
        self.ques = ques
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []

questions_list.append( Question("Скільки буде 2+2?", "4", "2", "1", "22") )
questions_list.append( Question("Який колір сонця?", "жовтий", "синій", "черовний", "чорний") )
questions_list.append( Question("Грут?", "Я є Грут", "Я не Грут", "Хто Грут?", "Він Грут?") )

questions_list.append( Question("?", "Я", "Я", "Хто?", "Він?") )



# === СТВОРЕННЯ ГОЛОВНОГО ВІКНА ===
app = QApplication([])   # обов’язково створюється першим
window = QWidget()       # головне вікно
window.resize(800, 500)  # задаємо розмір
window.setWindowTitle("Memory card")  # назва вікна




# === СТВОРЕННЯ ОСНОВНИХ ВІДЖЕТІВ ===
question = QLabel("переклади англійською")  # напис із питанням
btn_ok = QPushButton("Answer")               # кнопка для відповіді / переходу




# === ГРУПА З ВАРІАНТАМИ ВІДПОВІДЕЙ ===
RadioGroupBox = QGroupBox("Варіанти відповідей")  # рамка для варіантів


# Створюємо радіокнопки (можна вибрати тільки одну)
rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")


# Об’єднуємо всі кнопки в одну групу, щоб не можна було вибрати кілька одразу
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


# === Створюємо лейаут (розташування) для варіантів ===
ans_h_layout = QHBoxLayout()  # головний горизонтальний ряд
ans_v1_layout = QVBoxLayout() # перша колонка
ans_v2_layout = QVBoxLayout() # друга колонка


# додаємо кнопки у дві колонки
ans_v1_layout.addWidget(rbtn1)
ans_v1_layout.addWidget(rbtn2)
ans_v2_layout.addWidget(rbtn3)
ans_v2_layout.addWidget(rbtn4)


# об’єднуємо дві колонки в один ряд
ans_h_layout.addLayout(ans_v1_layout)
ans_h_layout.addLayout(ans_v2_layout)


# встановлюємо лейаут у групу
RadioGroupBox.setLayout(ans_h_layout)




# === ГРУПА З РЕЗУЛЬТАТОМ ВІДПОВІДІ ===
AnsGroupBox = QGroupBox("Результат тесту")


lb_Result = QLabel("Відповідь вірна?")         # текст про правильність
lb_Correct = QLabel("відповідь буде тут!")     # правильна відповідь


layout_res = QVBoxLayout()  # вертикальне розміщення для блоку результату
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)




# === ОСНОВНА СХЕМА РОЗМІЩЕННЯ ===
v_line = QVBoxLayout()  # головне вертикальне розташування


h1_line = QHBoxLayout()  # рядок для питання
h2_line = QHBoxLayout()  # рядок для варіантів / результатів
h3_line = QHBoxLayout()  # рядок для кнопки


# 1. Питання по центру
h1_line.addWidget(question, alignment=Qt.AlignCenter)


# 2. Групи з варіантами та результатом поруч
h2_line.addWidget(RadioGroupBox)
h2_line.addWidget(AnsGroupBox)


# 3. Кнопка по центру з відступами
h3_line.addStretch(1)
h3_line.addWidget(btn_ok, stretch=2)
h3_line.addStretch(1)


# 4. Об’єднуємо всі рядки у вертикальну структуру
v_line.addLayout(h1_line, stretch=2)
v_line.addLayout(h2_line, stretch=8)
v_line.addStretch(1)
v_line.addLayout(h3_line, stretch=1)
v_line.addStretch(1)


# Спочатку ховаємо групу з результатом (показується пізніше)
AnsGroupBox.hide()




# === ФУНКЦІЇ ДЛЯ ЗМІНИ СТАНІВ ===


# показати результат (при натисканні кнопки)
def show_result():
    RadioGroupBox.hide()             # сховати варіанти
    AnsGroupBox.show()               # показати результат
    btn_ok.setText("Наступне запитання")  # змінити текст кнопки




# показати запитання (перед новим питанням)
def show_question():
    AnsGroupBox.hide()               # сховати результат
    RadioGroupBox.show()             # показати варіанти
    btn_ok.setText("Answer")         # повернути напис кнопки


    # Зняти вибір з усіх кнопок
    RadioGroup.setExclusive(False)   # тимчасово дозволяємо змінювати стан
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)    # повертаємо звичайний режим




# список усіх кнопок для зручності
answers = [rbtn1, rbtn2, rbtn3, rbtn4]




# --- ФУНКЦІЯ ДЛЯ ПЕРЕВІРКИ І ВИВОДУ ЗАПИТАННЯ ---
def ask( q : Question ):
    """Встановлює нове запитання та перемішує варіанти"""
    shuffle(answers)  # перемішуємо варіанти місцями


    # встановлюємо текст для кожної кнопки
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)


    # виводимо запитання та правильну відповідь
    question.setText(q.ques)
    lb_Correct.setText(q.right_answer)


    # показуємо блок із питанням
    show_question()




# --- ФУНКЦІЯ ДЛЯ ВІДОБРАЖЕННЯ РЕЗУЛЬТАТУ ---
def show_correct(res):
    """Показує результат (правильно / неправильно)"""
    lb_Result.setText(res)
    show_result()




# --- ФУНКЦІЯ ПЕРЕВІРКИ ВИБОРУ КОРИСТУВАЧА ---
def check_answer():
    """Перевіряє, яку відповідь обрано"""
    if answers[0].isChecked():  # перша кнопка — правильна (після shuffle)
        show_correct("Correct!")      # якщо правильна
        window.score += 1

        print("Statictics \n Total question", window.total, "\n Right answer", window.score)
        print("Raiting", window.score / window.total * 100, "%")

    else:
        # якщо вибрана будь-яка інша
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("INCORRECT!!")

            print("Raiting", window.score / window.total * 100, "%")



def next_question():
    window.total += 1
    print("Statictics \n Total question", window.total, "\n Right answer", window.score)

    cur_question = randint(0, len(questions_list) - 1 )

    q = questions_list[cur_question]

    ask(q)



def click_OK():

    if btn_ok.text() == "Answer":
        check_answer()
    else:
        next_question()


# --- ПОДІЯ: при натисканні кнопки ---
btn_ok.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()

# Встановлюємо головний лейаут у вікно
window.setLayout(v_line)


# Показуємо вікно
window.show()


# Запускаємо програму (основний цикл)
app.exec()









