from googletrans import Translator, LANGUAGES
import pandas as pd
from tabulate import tabulate

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


def LanguageList(out="screen", text=None):
    try:
        languages = list(LANGUAGES.values())
        codes = list(LANGUAGES.keys())

        data = {"Language": languages, "ISO-639 code": codes}

        if text:
            translator = Translator()
            translations = [translator.translate(text, dest=lang).text for lang in codes]
            data["Text"] = translations

        df = pd.DataFrame(data)

        if out == "screen":
            print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
            return "Ok"
        elif out == "file":
            filename = "language_list_gtrans.txt"
            df.to_csv(filename, index=False, sep='\t', encoding='utf-8')
            return f"Table saved to file: {filename} \n Ok"
        else:
            return "Invalid 'out' parameter"
    except Exception as e:
        return f"Error: {e}"
