import time
from dataclasses import dataclass
from random import choice, shuffle


@dataclass(slots=True)
class Question:
    question: str
    answers: list[str]
    correct_answers: str

def random_question(questions: list[Question]) -> int:
    question:Question = choice(questions)
    print(f'{question.question}')

    shuffle(question.answers)

    for answer in question.answers:
        print('-',answer)

    user_input=input('\n Your answeer >>').lower().strip()

    if user_input==question.correct_answers:
        print('Correct!')
        question.remove(question)
        return 1
    else:
        print(f'Wrong, the ans was!{question.correct_answers.capitalize()}\n')
        questions.remove(question)
        return 0

def run_quiz(questions: list[Question]):
    total_score=0
    while questions:
        score=random_question(questions=questions)
        total_score+=score
        time.sleep(2)
    else:
        print('Final score:',total_score)

def get_questions()->list[Question]:
    return[
        Question(question='How are you?',
                 answers=['Good','Bad','Ok','Potato'],
                 correct_answers='Good'),
        Question(question='What is your name?',
                 answers=['Mario','Luigi','Peach'],
                 correct_answers='Mario'),
        Question(question='What time is it?',
                 answers=['11','10','12'],
                 correct_answers='10'),
        Question(question='What is 1 + 1',
                 answers=['1','2','3'],
                 correct_answers='2')

]
def main():
    questions=get_questions()
    run_quiz(questions=questions)
if __name__ == '__main__':
    main()

