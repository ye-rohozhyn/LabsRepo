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


def process_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    words.sort()

    ukrainian_words = [word for word in words if re.search(r'[а-яїєґіь]+', word)]
    english_words = [word for word in words if re.search(r'[a-z]+', word)]

    if ukrainian_words:
        print("\nУкраїнські слова:")
        print(", ".join(ukrainian_words))
    if english_words:
        print("\nАнглійські слова:")
        print(", ".join(english_words))

    word_count = len(words)
    print("\nЗагальна кількість слів:", word_count)


if __name__ == '__main__':
    file_path = 'text_file.txt'
    first_sentence = read_first_sentence(file_path)
    if first_sentence is not None:
        process_text(first_sentence)
