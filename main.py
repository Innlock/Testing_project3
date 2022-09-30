commands = ["help", "start", "quit", "A", "B", "C", "D", "50/50", "call", "points"]
answers = {"A": "1", "B": "2", "C": "3", "D": "4"}


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