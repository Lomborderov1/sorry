from random import randint
from flask import Flask
from app4 import get_question_after

def index():
    max_quiz = 3
    session['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return '<a href="/test">Тест</a>'

def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return 