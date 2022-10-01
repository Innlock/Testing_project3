import random
import sys
import time

import pytest
from unittest.mock import call, Mock

commands = ["help", "start", "quit", "A", "B", "C", "D", "50/50", "call", "points"]
answers = {"A": "1", "B": "2", "C": "3", "D": "4"}


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


def check_answer(player_a, right_a):
    return player_a == right_a


def command(points):
    answer = input("Введите команду: ")
    if answer not in commands:
        print("Команда не найдена. Введите help для просмотра команд.")
        answ = command(points)
    else:
        answer = commands.index(answer)

    if answer == 0:
        print_commands()
        answ = command(points)
    if answer == 1:
        points = 0
        play_game(points)
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
        answ = command(points)
    if answer == 9:
        print(f"Ваши очки: {points}")
        answ = command(points)
    return answ


def play_round(num, point, questions_file, points):
    print(f"Раунд {num}. Каждый вопрос {point} баллов.\n")
    questions = get_questions(questions_file)
    for i in range(3):
        question = questions.pop(random.randrange(len(questions)))
        print_question(question)
        answer = command(points)
        if not answer:
            print_half_question(question)
            answer = command(points)
        if answers[answer] == question[5]:
            points += point
            print("Верно.\n")
        else:
            print("Неверно.\n")
    return points


def play_final_round(points):
    print("Финальный вопрос 1 000 000 баллов:")
    questions = get_questions("questions4.txt")
    question = random.choice(questions)
    print_question(question)
    answer = command(points)
    if check_answer(answers[answer], question[5]):
        points += 1000000
        print("Верно!\n")
    else:
        print("Неверно.\n")
    return points


@pytest.mark.parametrize('inp', [True, False])
def test_mocking_play_final_round(monkeypatch, inp):
    my_mock1 = Mock(return_value=[['Что во время игры принимает волейболист?',
                                   'подачу', 'роды', '100 грамм', 'снотворное', '1']])
    my_mock2 = Mock()
    my_mock3 = Mock(return_value="A")
    my_mock4 = Mock(return_value=inp)
    monkeypatch.setattr('main.get_questions', my_mock1)
    monkeypatch.setattr('main.print_question', my_mock2)
    monkeypatch.setattr('main.command', my_mock3)
    monkeypatch.setattr('main.check_answer', my_mock4)

    points = play_final_round(0)
    my_mock1.assert_has_calls([call("questions4.txt")])
    my_mock2.assert_called()
    my_mock3.assert_called()
    my_mock4.assert_called()
    if inp:
        assert points == 1000000
    else:
        assert points == 0


def play_game(points):
    points = play_round(1, 100, "questions1.txt", points)
    points = play_round(2, 5000, "questions2.txt", points)
    points = play_round(3, 10000, "questions3.txt", points)
    if points < 300:
        print("Сожалеем, но вы не дошли до финала.")
    else:
        points = play_final_round(points)
        print(f"Ваш выигрыш: {points} рублей\nСпасибо за игру!")
    sys.exit()


@pytest.mark.parametrize('inp', [500, 1])
def test_mocking_play_game(monkeypatch, inp):
    my_mock1 = Mock(return_value=inp)
    my_mock2 = Mock()
    my_mock3 = Mock()
    monkeypatch.setattr('main.play_round', my_mock1)
    monkeypatch.setattr('main.play_final_round', my_mock2)
    monkeypatch.setattr('main.sys.exit', my_mock3)
    play_game(0)
    my_mock1.assert_has_calls([call(1, 100, "questions1.txt", 0),
                               call(2, 5000, "questions2.txt", inp),
                               call(3, 10000, "questions3.txt", inp)])
    if inp == 500:
        my_mock2.assert_has_calls([call(inp)])
    else:
        my_mock2.assert_not_called()
    my_mock3.assert_called_once()


if __name__ == "__main__":
    print('Игра «Как стать миллионером»')
    print_commands()
    print("Введите start, чтобы начать игру")
    command(0)
