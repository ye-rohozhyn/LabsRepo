from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException


def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translation = GoogleTranslator(source=src, target=dest).translate(text)
        return translation
    except LanguageNotSupportedException as e:
        return str(e)
    except Exception as e:
        return f"Помилка: {e}"


def LangDetect(text: str, set: str = "all"):
    try:
        detected_language = GoogleTranslator(source='auto', target='en').detect(text)
        return detected_language
    except LanguageNotSupportedException as e:
        return str(e)
    except Exception as e:
        return f"Помилка: {e}"


def CodeLang(lang: str) -> str:
    try:
        translator = GoogleTranslator(source='auto', target='en')
        supported_languages = translator.get_supported_languages(as_dict=True)
        lang = lang.lower()
        if lang in supported_languages:
            return supported_languages[lang]
        else:
            return "Мову не знайдено"
    except Exception as e:
        return f"Помилка: {e}"


def LanguageList(out: str, text: str = None):
    try:
        translator = GoogleTranslator(source='auto', target='en')
        supported_languages = translator.get_supported_languages(as_dict=True)
        table = "Мова\t\tКод"

        if text:
            table += "\t\tПереклад тексту"

        if out == "screen":
            print(table)
        elif out == "file":
            with open('translation.txt', 'w', encoding='utf-8') as file:
                file.write(table + '\n')
        else:
            return "Невідомий параметр 'out'. Використовуйте 'screen' або 'file'."

        for lang, code in supported_languages.items():
            if text:
                try:
                    translation = GoogleTranslator(source='en', target=code).translate(text)
                    table_row = f"{lang}\t\t{code}\t\t{translation}"
                except LanguageNotSupportedException:
                    table_row = f"{lang}\t\t{code}\t\tМова не підтримується"
            else:
                table_row = f"{lang}\t\t{code}"

            if out == "screen":
                print(table_row)
            elif out == "file":
                with open('translation.txt', 'a', encoding='utf-8') as file:
                    file.write(table_row + '\n')

        return 'Ok'
    except Exception as e:
        return f"Помилка: {e}"
