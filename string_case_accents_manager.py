import unidecode
import re


class CaseAccentHandler:
    def __init__(self, string=""):
        self.__base_str = self.normalize(string)

    @staticmethod
    def normalize(string):
        return re.sub(' +', ' ', re.sub(r"[^a-zA-Z0-9-\-]+", ' ', unidecode.unidecode(string)).lower().strip()).title()

    # Return -1 if no match, 0 if match in order, 2 if match but words mixed
    def compare_in_order(self, string):
        normalize_string = self.normalize(string)
        if normalize_string == self.__base_str:
            return 0
        return self.__compare_any_order(normalize_string)

    def __compare_any_order(self, string):
        array_base = self.__base_str.split(" ")
        array_string = string.split(" ")

        for word in array_string:
            if word not in array_base:
                return -1
        return 2

    def get_result(self):
        return self.__base_str
