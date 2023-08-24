import unittest
import app as hangman

class HangmanTestCase(unittest.TestCase):

    # checkCorrectAnswer(“사용자가입력한글자들", “맞춰야할 단어”)
    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

if __name__ == "__main__":
    unittest.main()

