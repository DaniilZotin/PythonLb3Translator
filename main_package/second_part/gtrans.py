from deep_translator import GoogleTranslator



def TransLate(string: str, lang: str)-> str:
    """
    Translate text

    :param string: text you want to translate
    :param lang: ISO-639 code of language you want to get in the result of translation
    """
    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(string)
        return "Result: " + translated
    except Exception as e:
        return str(e)

# First function
print("---------------------------------------------")
print("TransLate - result")
txt = "Hello, how are you?"
print(TransLate(txt, "uk"))
print("---------------------------------------------")