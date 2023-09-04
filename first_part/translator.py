from googletrans import Translator, LANGUAGES
import pycountry


def TransLate(text: str, src: str, dest: str) -> str:
    """
    The function returns the text translated into the specified language, or an error message

    :param text: string you want to translate
    :param src: ISO-639 code of language you entered
    :param src: ISO-639 code of language you want to get in the result of translation
    """
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=src, dest=dest)
        return translated_text.text
    except Exception as e:
        return str(e)

# First function
print("-------------------------------------")
print("1. TransLate - result")
text_to_translate = "Hello, world!"
src_language = "en"
dest_language = "uk"
translated_text = TransLate(text_to_translate, src_language, dest_language)
print(translated_text)
print("-------------------------------------")


def LangDetect(text: str, set: str = "all") -> str:
    """
    The function determines the language and confidence factor for the given text,
    or returns an error message

    :param text: the text you want to detect language
    :param set: optional parametr:
        'lang' - return only language of the text
        'confidence' - return only confidence of the language
        'all'(default) - return language and confidence
    """
    try:
        translator = Translator()
        detection = translator.detect(text)

        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {detection.confidence}"
    except Exception as e:
        return str(e)

# Second function
print("2. LangDetect - result")
text_to_detect = "Bonjour tout le monde"
result_lang = LangDetect(text_to_detect, set="lang")
result_confidence = LangDetect(text_to_detect, set="confidence")
result_all = LangDetect(text_to_detect)
print("Language:", result_lang)
print("Confidence:", result_confidence)
print("All:", result_all)
print("-------------------------------------")


def CodeLang(lang):
    """
    The function returns the language code (according to the table)

    :param lang: ISO-639 of country u want to get full name
    """
    language = pycountry.languages.get(alpha_2=lang)
    if language:
        return language.name
    else:
        return "Language not found"

# Third function
print("3. CodeLang - result")
print(CodeLang("uk"))
print("-------------------------------------")


def LanguageList(out="screen", text=None) -> str:
    """
    Displays a table of all supported languages and their codes in a file or on the screen,
    as well as the text translated into that language.

    :param out: Output table on the ('screen') or in the ('file')
    :param text: Text you want to translate
    """
    try:
        translator = Translator()

        if out == "file":
            with open("languages_table.txt", "w", encoding="utf-8") as file:
                file.write("Language\t\tISO-639 code\t\t\tText")
                file.write("\n-----------------------------------------------------\n")
                print("Please wait we are making the table in a file ...... ")
                for lang_code, lang_name in LANGUAGES.items():
                    translation = ""
                    if text:
                        translation = translator.translate(text, src='en', dest=lang_code).text
                    lang_name = lang_name.ljust(15)  # Вирівнюємо назву мови
                    lang_code = lang_code.ljust(15)  # Вирівнюємо ISO-639 код
                    file.write(f"{lang_name}\t{lang_code}\t{translation}\n")
                file.write("......................................................")
            return "We have written list of language we can translate into languages_table.txt file"
        elif out == "screen":
            print("Language\t\tISO-639 code\t\t\tText")
            print("---------------------------------------------------------------")
            for lang_code, lang_name in LANGUAGES.items():
                translation = ""
                if text:
                    translation = translator.translate(text, src='en', dest=lang_code).text
                lang_name = lang_name.ljust(15)  # Вирівнюємо назву мови
                lang_code = lang_code.ljust(15)  # Вирівнюємо ISO-639 код
                print(f"{lang_name}\t\t{lang_code}\t\t{translation}")
            print("......................................................")
            return "It is list of languages that googletrans can translate"
        else:
            return "Entered value of 'out' if incorrect. Choose 'screen' or 'file'."

    except Exception as e:
        return str(e)


# Fought function
result = LanguageList(out="screen", text="Hello, world!")
print(result)

result = LanguageList(out="file", text="Hello, world!")
print(result)