from googletrans import Translator, LANGUAGES


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translation = Translator().translate(text, src=scr, dest=dest)
        return translation.text
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str = "all"):
    try:
        translator = Translator()
        detected_language = translator.detect(text)
        return detected_language.lang
    except Exception as e:
        return str(e)


def CodeLang(lang: str) -> str:
    try:
        for code, name in LANGUAGES.items():
            if name.lower() == lang.lower():
                return code
        return "Language not found"
    except Exception as e:
        return str(e)


def LanguageList(out: str, text: str = None):
    try:
        translator = Translator()
        supported_languages = LANGUAGES
        table = "Код\t\tМова"

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
                translation = translator.translate(text, src='en', dest=code)
                table_row = f"{lang}\t\t{code}\t\t{translation.text}"
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
