import requests
from collections import Counter, defaultdict
import re


class WordFinder:
    def __init__(self, word_list_url=None):
        """
        Initialize the WordFinder with a word list.

        Args:
            word_list_url: URL to download word list from. If None, uses a default.
        """
        self.words = set()
        # self.load_word_list(word_list_url)
        self.load_word_list_from_file('scrabble_dictionary.txt')

    def load_word_list_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            words = [line.strip() for line in file if line.strip()]
        self.words = set(words)

    def load_word_list(self, url=None):
        """Load English words from a URL or use a basic built-in list."""
        if url is None:
            # Default word list URL (common English words)
            url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

        try:
            response = requests.get(url)
            response.raise_for_status()
            # Split by lines and clean up
            words = response.text.strip().split('\n')
            # Filter out very short words and convert to lowercase
            self.words = {word.lower().strip() for word in words if len(word.strip()) >= 2}
            print(f"Loaded {len(self.words)} words from word list.")
        except Exception as e:
            print(f"Error loading word list: {e}")
            # Fallback to a basic word list
            self.words = self._get_basic_word_list()
            print(f"Using basic word list with {len(self.words)} words.")

    def _get_basic_word_list(self):
        """Fallback basic word list if URL fails."""
        return {
            'add', 'aid', 'air', 'art', 'dot', 'duo', 'had', 'hat', 'hit', 'hid', 'hut',
            'oat', 'odd', 'old', 'our', 'out', 'rod', 'rot', 'rut', 'tar', 'too', 'tad',
            'auto', 'dart', 'dirt', 'door', 'hour', 'hurt', 'riot', 'road', 'root',
            'tour', 'trio', 'hard', 'hood', 'hoot', 'dirt', 'radio', 'ratio', 'audio',
            'hoard', 'rotor', 'audit', 'adult', 'chair', 'third', 'truth', 'about',
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'her', 'was',
            'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'may',
            'new', 'now', 'old', 'see', 'two', 'who', 'boy', 'did', 'man', 'run', 'try'
        }

    def can_make_word(self, word, available_letters):
        """
        Check if a word can be made from available letters.

        Args:
            word: The word to check
            available_letters: Counter object with available letters

        Returns:
            bool: True if word can be made, False otherwise
        """
        word_letters = Counter(word.lower())

        # Check if we have enough of each letter
        for letter, count in word_letters.items():
            if available_letters[letter] < count:
                return False
        return True

    def find_words(self, letters):
        """
        Find all possible words from given letters.

        Args:
            letters: List of letters or string of letters

        Returns:
            dict: Dictionary with word length as key and list of words as value
        """
        if isinstance(letters, str):
            letters = list(letters.lower())
        else:
            letters = [letter.lower() for letter in letters]

        # Count available letters
        available_letters = Counter(letters)

        # Find all possible words
        possible_words = []
        for word in self.words:
            if self.can_make_word(word, available_letters):
                possible_words.append(word)

        # Group by length
        words_by_length = defaultdict(list)
        for word in possible_words:
            words_by_length[len(word)].append(word)

        # Sort words within each length group
        for length in words_by_length:
            words_by_length[length].sort()

        return dict(words_by_length)

    def print_results(self, words_by_length):
        """Print the results in a formatted way."""
        if not words_by_length:
            print("No words found!")
            return

        total_words = sum(len(words) for words in words_by_length.values())
        print(f"\nFound {total_words} total words:")
        print("=" * 50)

        for length in sorted(words_by_length.keys()):
            words = words_by_length[length]
            print(f"\n{length}-letter words ({len(words)} found):")
            print("-" * 30)

            # Print words in columns for better readability
            words_per_line = 6
            for i in range(0, len(words), words_per_line):
                line_words = words[i:i + words_per_line]
                print("  ".join(f"{word:<8}" for word in line_words))


def main():
    """Main function to run the word finder."""
    print("Word Finder - Find all English words from given letters")
    print("=" * 55)

    # Initialize the word finder
    finder = WordFinder()

    while True:
        print("\nEnter letters (space-separated or as a string):")
        print("Example: 'a r o o d a o i a d h i u t i' or 'aroodaoiadhiuti'")
        print("Type 'quit' to exit")

        user_input = input("> ").strip()

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        if not user_input:
            continue

        # Parse input - handle both space-separated and string formats
        if ' ' in user_input:
            letters = user_input.split()
        else:
            letters = list(user_input)

        # Remove any non-alphabetic characters
        letters = [letter for letter in letters if letter.isalpha()]

        if not letters:
            print("Please enter valid letters.")
            continue

        print(f"\nSearching for words using letters: {', '.join(letters)}")

        # Find words
        words_by_length = finder.find_words(letters)

        # Print results
        finder.print_results(words_by_length)


if __name__ == "__main__":
    main()