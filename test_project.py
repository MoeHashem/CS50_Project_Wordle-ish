from project import check_word, colored_word, get_valid_input, check_real_word, check_length



def test_check_word():
        # Test correct position
        wordle = "hello"
        assert check_word("hello", wordle) == ["G", "G", "G", "G", "G"]

        # Test incorrect position
        wordle = "world"
        assert check_word("dlwor", wordle) == ["Y", "Y", "Y", "Y", "Y"]
        assert check_word("wordl", wordle) == ["G", "G", "G", "Y", "Y"]

        # Test non-matching word
        wordle = "world"
        assert check_word("spain", wordle) == ["N", "N", "N", "N", "N"]

        # Test repeated letters with one in green
        wordle = "world"
        assert check_word("herro", wordle) == ["N", "N", "G", "N", "Y"]

        # Test repeated letters with both in yellow
        wordle = "world"
        assert check_word("label", wordle) == ["Y", "N", "N", "N", "N"]

        # Test repeated letters in input word but not in wordle
        wordle = "apple"
        assert check_word("banan", wordle) == ["N", "Y", "N", "N", "N"]

        # Test input word with letters not in wordle
        wordle = "apple"
        assert check_word("choir", wordle) == ["N", "N", "N", "N", "N"]



from colorama import Fore, Style

def test_colored_word():
        # Test all correct letters
        results = ["G", "G", "G", "G", "G"]
        word = "hello"
        assert len(word) == 5
        assert colored_word(results, word) == [Fore.GREEN + 'h', Fore.GREEN + 'e', Fore.GREEN + 'l', Fore.GREEN + 'l', Fore.GREEN + 'o']

        # Test all incorrect letters
        results = ["N", "N", "N", "N", "N"]
        word = "hello"
        assert len(word) == 5
        assert colored_word(results, word) == ['h', 'e', 'l', 'l', 'o']

        # Test some correct and some incorrect letters
        results = ["G", "Y", "N", "Y", "G"]
        word = "hello"
        assert len(word) == 5
        assert colored_word(results, word) == [Fore.GREEN + 'h', Fore.YELLOW + 'e', 'l', Fore.YELLOW + 'l', Fore.GREEN + 'o']


def test_check_real_word():

        final_word_list = ["A", "B", "C"]
        #checks valid word
        assert check_real_word("A", final_word_list) == True
        #checks invalid word
        assert check_real_word("D", final_word_list) == False

def test_check_length():

        length = 5
        #checks valid word
        assert check_length("ABCDE", length) == True
        #checks invalid word
        assert check_real_word("D") == False