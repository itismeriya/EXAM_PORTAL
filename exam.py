import json
from utils import load_data, save_data

class Exam:
    def __init__(self):
        self.exams_file = 'data/exams.json'
        self.exams = load_data(self.exams_file)

    def create_exam(self):
        title = input("Enter exam title: ")
        num_questions = int(input("Enter number of questions: "))
        questions = []

        for _ in range(num_questions):
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            questions.append({'question': question, 'answer': answer})

        self.exams[title] = questions
        save_data(self.exams_file, self.exams)
        print("Exam created successfully.")

    def take_exam(self):
        title = input("Enter exam title: ")

        if title not in self.exams:
            print("Exam not found.")
            return

        score = 0
        for q in self.exams[title]:
            print(f"Question: {q['question']}")
            answer = input("Enter your answer: ")
            if answer == q['answer']:
                score += 1

        print(f"Your score: {score}/{len(self.exams[title])}")
