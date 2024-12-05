import os
import sys
import yaml

def get_student_name():
    student_folders = [name for name in os.listdir() if os.path.isdir(name) and not name.startswith('.')]
    if len(student_folders) != 1:
        print("Ошибка: Должна быть только одна папка с именем студента.")
        sys.exit(1)
    return student_folders[0]

def load_correct_answers():
    with open('correct_answers.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def verify_submission(student_name, submitted_word, correct_answers):
    correct_word = correct_answers.get(student_name)
    if not correct_word:
        print(f"Ошибка: Не найден правильный ответ для студента {student_name}.")
        sys.exit(1)
    if submitted_word.strip().lower() == correct_word.lower():
        print(f"Успех: Отправленное слово для {student_name} верно.")
        sys.exit(0)
    else:
        print(f"Неудача: Отправленное слово '{submitted_word}' неверно.")
        sys.exit(1)

def main():
    student_name = get_student_name()
    submission_file = os.path.join(student_name, 'answer.txt')

    if not os.path.exists(submission_file):
        print(f"Ошибка: Файл с ответом {submission_file} не найден.")
        sys.exit(1)

    with open(submission_file, 'r', encoding='utf-8') as f:
        submitted_word = f.read()

    correct_answers = load_correct_answers()
    verify_submission(student_name, submitted_word, correct_answers)

if __name__ == '__main__':
    main()
