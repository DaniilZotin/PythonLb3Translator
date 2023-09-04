from langdetect import detect_langs


def LangDetect(text):
    """
    Find out language and probability

    :param text: the text you want to detect language
    """
    try:
        language_probabilities = detect_langs(text)
        if language_probabilities:
            most_probable_language = language_probabilities[0]
            return most_probable_language.lang, most_probable_language.prob
        else:
            return "Language not detected"
    except:
        return "Unable to detect language"

#Second function
print("---------------------------------------------")
print("LangDetect - result")
txt = "Hello, how are you?"
detected_language, probability = LangDetect(txt)
print(f"Detected language: {detected_language} Probability: {probability}")
print("---------------------------------------------")