from Translators.googleTransModule import *

def main():
    text_to_translate = "Hello, how are you?"
    translation_result = LanguageList("file", text_to_translate)
    if translation_result == "Ok":
        print("Переклад завершено!")
    else:
        print("Під час виконання перекладу виникла помилка\n" + translation_result)


if __name__ == '__main__':
    main()
