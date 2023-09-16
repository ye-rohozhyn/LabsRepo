import json
from Translators.googleTransModule import *


def read_config(config_file):
    try:
        with open(config_file, "r", encoding="utf-8") as file:
            config_data = json.load(file)
        return config_data
    except Exception as e:
        print(f"Помилка при зчитуванні конфігураційного файлу: {e}")
        return None


def process_text(config):
    try:
        source_file = config["source_file"]
        target_language = config["target_language"]
        output_type = config["output_type"]
        max_characters = config["max_characters"]
        max_words = config["max_words"]
        max_sentences = config["max_sentences"]

        with open(source_file, "r", encoding="utf-8") as file:
            text = file.read()

        original_text_length = len(text)
        words = text.split()
        sentences = text.split(".")

        if original_text_length > max_characters:
            text = text[:max_characters]

        if len(words) > max_words:
            words = words[:max_words]
            text = ' '.join(words)

        if len(sentences) > max_sentences:
            sentences = sentences[:max_sentences]
            text = '. '.join(sentences)

        print("Переклад тексту: " + text + "\nМова тексу:", LangDetect(text, "lang"))

        translated_text = TransLate(text, "auto", target_language)

        if output_type == "screen":
            print("Перекладений текст: " + translated_text)
        elif output_type == "file":
            output_file = source_file.replace(".txt", f"_{target_language}.txt")
            with open(output_file, "w", encoding="utf-8") as file:
                file.write(translated_text)
            print(f"Результат збережено у файлі: {output_file}")
        else:
            print("Недійсний тип виведення у конфігураційному файлі.")

    except Exception as e:
        print(f"Помилка: {e}")


config = read_config("config.json")

if config:
    process_text(config)
