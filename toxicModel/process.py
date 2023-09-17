import re
import contractions

class Text:

    def remove_numbers_and_non_english(self, text):

        text = re.sub(r'\d+', '', text)

        # Remove non-English characters (assuming English alphabet)
        text = re.sub(r'[^a-zA-Z\s]', '', text)

        return text

    def expand_contractions(self, text):
        expanded_text = contractions.fix(text)

        return expanded_text

    def remove_extraSpace(self, text):
        text = re.sub(' +', ' ', text)
        # Remove trailing and leading whitespaces in string
        text = text.strip()
        return text

    def remove_newline(self, text):
        text = text.replace("\n", " ")
        return text

    @staticmethod
    def preprocess(text):
        instance = Text()
        text = instance.remove_newline(text)
        text = instance.expand_contractions(text)
        text = instance.remove_numbers_and_non_english(text)
        text = instance.remove_extraSpace(text)
        return text