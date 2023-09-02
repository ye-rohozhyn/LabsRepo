from langdetect import detect
from translate import Translator


def LangDetect(txt):
    lang = detect(txt)
    confidence = 1
    return f"Detected(lang={lang}, confidence={confidence})"


def TransLate(txt, lang):
    from_lang = detect(txt)
    translator = Translator(from_lang=from_lang, to_lang=lang)
    translated_text = translator.translate(txt)
    return translated_text


def CodeLang(lang):
    language_names = {"en": "English", "uk": "Ukrainian"}
    return language_names.get(lang, "Unknown")


if __name__ == '__main__':
    txt = "Доброго дня. Як справи?"
    lang = "en"
    print(txt)
    print(LangDetect(txt))
    print(TransLate(txt, lang))
    print(CodeLang(lang))
