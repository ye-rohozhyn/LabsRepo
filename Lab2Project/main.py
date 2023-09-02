from langdetect import detect
from translate import Translator


def LangDetect(txt):
    lang = detect(txt)
    confidence = 1  # In this example, assume language detection is always accurate
    return f"Detected(lang={lang}, confidence={confidence})"


def TransLate(txt, lang):
    translator = Translator(from_lang=lang, to_lang="en")
    translated_text = translator.translate(txt)
    return translated_text


def CodeLang(lang):
    # You can add a dictionary with language code to name mappings here
    # For example, {"en": "English", "uk": "Ukrainian", ...}
    language_names = {"en": "English", "uk": "Ukrainian"}
    return language_names.get(lang, "Unknown")


if __name__ == '__main__':
    txt = "Доброго дня. Як справи?"
    lang = "uk"
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))
