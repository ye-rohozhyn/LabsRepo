from Translators.googleTransModule import *

def main():
    text_to_translate = "Hello, how are you?"
    target_language = "uk"
    translation_text = TransLate(text_to_translate, scr='auto', dest=target_language)
    print(translation_text)


if __name__ == '__main__':
    main()
