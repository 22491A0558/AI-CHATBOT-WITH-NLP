"""
NLP Processor module for text processing using basic Python string operations
"""

import string
from utils import print_colored

class NLPProcessor:
    def __init__(self):
        """Initialize the NLP processor"""
        # Common English stop words
        self.stop_words = {
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
            "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
            'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's",
            'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
            'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do',
            'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because',
            'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
            'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below',
            'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
            'further', 'then', 'once'
        }
        print_colored("NLP Processor initialized!", "green")

    def process_text(self, text):
        """
        Process the input text using basic text processing techniques

        Args:
            text (str): Input text to process

        Returns:
            dict: Processed text information
        """
        try:
            # Clean the text
            cleaned_text = self._clean_text(text)

            # Tokenize into words
            tokens = self._tokenize(cleaned_text)

            # Split into sentences (basic implementation)
            sentences = self._split_sentences(text)

            # Remove stop words
            filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]

            return {
                'original_text': text,
                'cleaned_text': cleaned_text,
                'tokens': tokens,
                'sentences': sentences,
                'filtered_tokens': filtered_tokens,
                'pos_tags': [],  # Placeholder for compatibility
                'ner_tags': []   # Placeholder for compatibility
            }
        except Exception as e:
            print_colored(f"Error processing text: {str(e)}", "red")
            raise

    def _clean_text(self, text):
        """Clean the input text by removing extra whitespace and normalizing"""
        try:
            # Remove punctuation except periods for sentence splitting
            text = ''.join([char if char in '.!?' else ' ' if char in string.punctuation else char for char in text])

            # Convert to lowercase and strip whitespace
            text = text.lower().strip()

            # Normalize whitespace
            text = ' '.join(text.split())

            return text
        except Exception as e:
            print_colored(f"Error cleaning text: {str(e)}", "red")
            raise

    def _tokenize(self, text):
        """Split text into words"""
        return [word.strip() for word in text.split() if word.strip()]

    def _split_sentences(self, text):
        """Split text into sentences using basic punctuation rules"""
        # Split on period, exclamation mark, or question mark followed by space and uppercase letter
        sentences = []
        current = ""

        for char in text:
            current += char
            if char in '.!?' and len(current.strip()) > 0:
                sentences.append(current.strip())
                current = ""

        if current.strip():
            sentences.append(current.strip())

        return sentences