commands = ["help", "start", "quit", "A", "B", "C", "D", "50/50", "call", "points"]
answers = {"A": "1", "B": "2", "C": "3", "D": "4"}


def get_questions(file_name):
    pass


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