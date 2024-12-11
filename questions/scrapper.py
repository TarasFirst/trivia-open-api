import requests

from questions.models import Question

url_questions = "https://opentdb.com/api.php?amount=10"


def scrapper() -> list[Question]:
    questions = requests.get(url_questions).json()

    questions_list = []

    for question_dict in questions["results"]:
        questions_list.append(
            Question(
                type=question_dict["type"],
                difficulty=question_dict["difficulty"],
                category=question_dict["category"],
                question=question_dict["question"],
                correct_answer=question_dict["correct_answer"],
                incorrect_answers=question_dict["incorrect_answers"],
            )
        )

    return questions_list


def save_questions(questions_list: list[Question]) -> None:
    for question in questions_list:
        question.save()


def sync_questions_with_db() -> None:
    questions_list = scrapper()
    save_questions(questions_list)
