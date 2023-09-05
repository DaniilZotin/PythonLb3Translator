import json
import os
import nltk
from langdetect import detect
from deep_translator import GoogleTranslator
import pycountry



def GetInformationAboutFile():
    """
        We get all information from our file with text
    """
    data = JsonConfigurationOpen()
    file_name = data["name"]
    file_size_bytes = 0; character_count = 0; word_count = 0; sentence_count = 0
    detected_language = "none"
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_path):
        file_size_bytes = os.path.getsize(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            # read file
            file_content = file.read()
        # count  characters in the file
        character_count = len(file_content)
        detected_language = detect(file_content)
        # divide text to words
        words = file_content.split()
        # count words
        word_count = len(words)
        sentences = nltk.sent_tokenize(file_content)
        sentence_count = len(sentences)
    else:
        print("This file does not exist")
    print("Name of the file: ", file_name)
    print(f"Size '{file_name}' in bites: {file_size_bytes} ")
    print("Symbols in the text: ", character_count)
    print("Words: ", word_count)
    print("Count of sentence in the text: ", sentence_count)
    print("Language in the file: ", CodeLang(detected_language))

def CodeLang(lang) -> str:
    """
        Returns full name of language from ISO-639

        :param lang: ISO-639 of country u want to get full name
    """
    language = pycountry.languages.get(alpha_2=lang)
    if language:
        return language.name
    else:
        return "Language not found"

def ReadFile() -> str:
    """
        Read the text until certain rules are followed,
        It returns result of read
    """
    config = JsonConfigurationOpen()

    # Get values from json
    file_name = config["name"]
    max_symbols = config["quantitySymbols"]
    max_words = config["quantityWords"]
    max_sentences = config["quantitySentences"]
    full_content = ""
    # full path to file in the root
    file_path = os.path.join(os.getcwd(), file_name)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            # Read the file by character
            while True:
                char = file.read(1)  # read one character
                if not char:
                    break
                # print(char, end="")
                full_content += char
                words = full_content.split()
                sentences = nltk.sent_tokenize(full_content)

                if(len(full_content) > max_symbols):
                    # print("Break because of symbols")
                    break
                if(len(words) > max_words):
                    # print("Break because of words")
                    break
                if(len(sentences) > max_sentences):
                    # print("Break because of sentences")
                    break
            full_content = full_content[:-1]
            # print(full_content)
            return full_content
    else:
        # print(f"File '{file_name}' does not exist in the root of directory.")
        return f"File '{file_name}' does not exist in the root of directory."


def Translate(text: str) -> str:
    """
        Translate text, get language from json

        :param text: content you want to translate
    """
    config = JsonConfigurationOpen()

    language = config["code"]
    translated = GoogleTranslator(source='auto', target=language).translate(text)
    return translated



def OutputResult(text):
    """
        Output result with two ways which we get from json(screen, file)

        :param text: content you want to output
    """

    config = JsonConfigurationOpen()

    view = config["view"]
    language = config["code"]
    if(view == "screen"):
        print("Language you get in the result: ", language)
        print(text)
        exit()
    if(view == "file"):
        path_to_folder = "C:/Users/Daniil/PycharmProjects/ProjectLb3DifferentTranslators/FilesWithResult/"
        new_file_name = "translation_" + language
        with open(path_to_folder + new_file_name, 'w', encoding='utf-8') as file:
            file.write(text)
        print("Ok")
    else:
        print("Error here")

def JsonConfigurationOpen():
    """
        Function for open json configuration file
    """
    json_file_configuration = "configuration.json"
    if os.path.exists(json_file_configuration):
        with open(json_file_configuration, "r", encoding="utf-8") as config_file:
            return json.load(config_file)
    else:
        print(f"Configuration file '{json_file_configuration}' is not exist.")
        exit()

GetInformationAboutFile()
OutputResult(Translate(ReadFile()))

