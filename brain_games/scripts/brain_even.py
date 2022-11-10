#!/usr/bin/env python3
import prompt
from random import randrange


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_random_number():
    return randrange(1, 100)


def is_correct_answer(number_for_question):
    if number_for_question % 2 == 0:
        return "yes"
    else:
        return "no"


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_counter = 0
    counter = 0
    while counter <= 2:
        counter += 1
        number_for_question = get_random_number()
        answer = prompt.string(f'Question: {number_for_question} ')
        print(f'Your answer: {answer}')
        correct_answer = is_correct_answer(number_for_question)
        if answer == correct_answer:
            print('Correct!')
            correct_answers_counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    if correct_answers_counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main()__':
    main()
