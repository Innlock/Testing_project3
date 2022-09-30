import random

commands = ["help", "start", "quit", "A", "B", "C", "D", "50/50", "call", "points"]
answers = {"A": "1", "B": "2", "C": "3", "D": "4"}
points = 0


def get_questions(file_name):
    with open(file_name, encoding='utf-8', mode='r') as f:
        text = f.read()
        text = text.split('\n')
        questions = []
        for x in range(0, len(text), 6):
            questions.append(text[x:x + 6])
        return questions


def test_get_questions():
    right_questions = [['Откуда обычно достает подарки Дед Мороз?', 'из шкатулки', 'из мешка', 'из-за пазухи',
                        'из интернет-магазина', '2'],
                       ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1'],
                       ['Как же, согласно поговорке, там, где нас нет?', 'Тепло', 'Сытно', 'Хорошо', 'Весело', '3']]
    questions = get_questions("questions_test.txt")
    assert questions is not None
    if questions:
        for q in questions:
            assert q in right_questions
            questions.pop()


def print_question(question):
    q = f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}"
    print(q)
    return q


def test_print_question():
    question = ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1']
    q = print_question(question)
    right_q = f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}"
    assert q == right_q


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


def test_print_half_question():
    question = ['Что во время игры принимает волейболист?', 'подачу', 'роды', '100 грамм', 'снотворное', '1']
    q = print_half_question(question)
    right_q1 = f"{question[0]}\nA. {question[1]}\nB. {question[2]}"
    right_q2 = f"{question[0]}\nA. {question[1]}\nC. {question[3]}"
    right_q3 = f"{question[0]}\nA. {question[1]}\nD. {question[4]}"
    assert q == right_q1 or q == right_q2 or q == right_q3


def command():
    pass


def play_round(num, point, questions_file):
    global points
    str = f"Раунд {num}. Каждый вопрос {point} баллов.\n"
    print(str)
    answ = []
    questions = get_questions(questions_file)
    for i in range(2):  # 2 для теста, вообще в раундк по 3 вопроса
        question = questions.pop(random.randrange(len(questions)))
        print_question(question)
        # answer = command()
        # if not answer:
        #     print_half_question(question)
        #     answer = command()
        # if answers[answer] == question[5]:
        #     points += point
        #     print("Верно.\n")
        # else:
        #     print("Неверно.\n")
        str.join(print_question(question))
        answ.append(question[5])
    return str, answ


def test_play_round():
    str, answ = play_round(1, 100, "questions_test.txt")
    print (str, answ)
    questions = get_questions("questions_test.txt")
    right_round1 = f"Раунд 1. Каждый вопрос 100 баллов.\n"
    for question in questions:
        right_round1.join(f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}")
    questions.reverse()
    right_round2 = f"Раунд 1. Каждый вопрос 100 баллов.\n"
    for question in questions:
        right_round2.join(f"{question[0]}\nA. {question[1]}\nB. {question[2]}\nC. {question[3]}\nD. {question[4]}")
    assert (str == right_round1 and answ == ["1", "3"]) or (str == right_round2 and answ == ["3", "1"])
