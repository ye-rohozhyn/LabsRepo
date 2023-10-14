import re


def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            first_sentence = re.split(r'[.!?]', text)[0].strip()
            print("Перше речення:")
            print(first_sentence)
            return first_sentence
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None


if __name__ == '__main__':
    file_path = 'text_file.txt'
    read_first_sentence(file_path)
