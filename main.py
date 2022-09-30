import random
import sys
import time

commands = ["help", "start", "quit", "A", "B", "C", "D", "50/50", "call", "points"]
answers = {"A": "1", "B": "2", "C": "3", "D": "4"}
points = 0


def print_commands():
    print("""
    Игра Кто хочет стать миллионером? - это конкурс викторина, в котором участники должны правильно ответить на ряд вопросов 
    с несколькими вариантами ответов, чтобы перейти на следующий уровень. 
    Всего 10 вопросов, каждый вопрос стоит определенной суммы денег, участники не имеют никаких временных ограничений для 
    предоставления ответа.
    Вопросы, сгруппированные на одном уровне, будут иметь одинаковую сложность. Например: вопросы 1-3 составляют первый уровень
    и будут содержать самые простые вопросы. Второй уровень (вопросы 4–6) будет несколько сложнее, за ним следует третий уровень
    (вопросы 7–9).

    Команды:
    help - вывести все команды.
    start - начать игру (если игра уже начата, то игра начнется сначала).
    quit - закончить игру.
    A, B, C, D - ответы на вопросы викторины.
    50/50 - исключает два неправильных ответа из множественного выбора.
    call - запускает 30-секундный таймер, вы можете сделаить звонок другу.
    points - вывести заработанную сумму очков.
    """)


def get_questions(file_name):
    with open(file_name, encoding='utf-8', mode='r') as f:
        text = f.read()
        text = text.split('\n')
        questions = []
        for x in range(0, len(text), 6):
            questions.append(text[x:x + 6])
        return questions


# def test_get_questions():
#     right_questions = [['Откуда обычно достает подарки Дед Мороз?', 'из шкатулки', 'из мешка', 'из-за пазухи',
#                         'из интернет-магазина', '2'],
#                        ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1'],
#                        ['Как же, согласно поговорке, там, где нас нет?', 'Тепло', 'Сытно', 'Хорошо', 'Весело', '3']]
#     questions = get_questions("questions_test.txt")
#     assert questions is not None
#     if questions:
#         for q in questions:
#             assert q in right_questions
#             questions.pop()


def print_question(question):
    q = f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}"
    print(q)
    return q


# def test_print_question():
#     question = ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1']
#     q = print_question(question)
#     right_q = f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}"
#     assert q == right_q


def print_half_question(question):
    q = {0: question[0], question[1]: "A", question[2]: "B", question[3]: "C", question[4]: "D"}
    a1 = question[int(question[5])]
    question = question[1:5]
    question.remove(a1)
    a2 = random.choice(question)
    half_question = {q[a1]: a1, q[a2]: a2}
    half_question = sorted(half_question.items())
    q_print = f"{q[0]}\n{half_question[0][0]}. {half_question[0][1]}\n{half_question[1][0]}. {half_question[1][1]}"
    print(q_print)
    return q_print


# def test_print_half_question():
#     question = ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1']
#     q = print_half_question(question)
#     right_q1 = f"{question[0]}\nA. {question[1]}\nB. {question[2]}"
#     right_q2 = f"{question[0]}\nA. {question[1]}\nC. {question[3]}"
#     right_q3 = f"{question[0]}\nA. {question[1]}\nD. {question[4]}"
#     assert q == right_q1 or q == right_q2 or q == right_q3


def command():
    answer = input("Введите команду: ")
    if answer not in commands:
        print("Команда не найдена. Введите help для просмотра команд.")
        answ = command()
    else:
        answer = commands.index(answer)

    if answer == 0:
        print_commands()
        answ = command()
    if answer == 1:
        play_game()
    if answer == 2:
        print("Спасибо за игру.")
        sys.exit()

    if answer == 3:
        return commands[answer]
    if answer == 4:
        return commands[answer]
    if answer == 5:
        return commands[answer]
    if answer == 6:
        return commands[answer]
    if answer == 7:
        return None
    if answer == 8:
        time.sleep(20)
        print("Осталось 10 секунд.")
        time.sleep(10)
        print("Время вышло.")
        answ = command()
    if answer == 9:
        print(f"Ваши очки: {points}")
        answ = command()
    return answ


def play_round(num, point, questions_file):
    global points
    print(f"Раунд {num}. Каждый вопрос {point} баллов.\n")
    questions = get_questions(questions_file)
    for i in range(3):
        question = questions.pop(random.randrange(len(questions)))
        print_question(question)
        answer = command()
        if not answer:
            print_half_question(question)
            answer = command()
        if answers[answer] == question[5]:
            points += point
            print("Верно.\n")
        else:
            print("Неверно.\n")


# def test_play_round():
#     str, answ = play_round(1, 100, "questions_test.txt")
#     print (str, answ)
#     questions = get_questions("questions_test.txt")
#     right_round1 = f"Раунд 1. Каждый вопрос 100 баллов.\n"
#     for question in questions:
#         right_round1.join(f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}")
#     questions.reverse()
#     right_round2 = f"Раунд 1. Каждый вопрос 100 баллов.\n"
#     for question in questions:
#         right_round2.join(f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}")
#     assert (str == right_round1 and answ == ["1", "3"]) or (str == right_round2 and answ == ["3", "1"])


def play_game():
    global points
    points = 0
    play_round(1, 100, "questions1.txt")
    play_round(2, 5000, "questions2.txt")
    play_round(3, 10000, "questions3.txt")
    if points < 300:
        print("Сожалеем, но вы не дошли до финала.")
        sys.exit()
    print("Финальный вопрос 1 000 000 баллов:")
    questions = get_questions("questions4.txt")
    question = random.choice(questions)
    print_question(question)
    answer = command()
    if answers[answer] == question[5]:
        points += 1000000
        print("Верно!\n")
    else:
        print("Неверно.\n")
    print(f"Ваш выигрыш: {points} рублей\nСпасибо за игру!")
    sys.exit()


print('Игра «Как стать миллионером»')
print_commands()
print("Введите start, чтобы начать игру")
command()
