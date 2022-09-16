import unittest
from unittest.mock import patch
from io import StringIO

from main import get_choices, check_win


class TestRockPaperScissors(unittest.TestCase):
    def setUp(self):
        self.stdout_patcher = patch("sys.stdout", new_callable=StringIO)
        self.mock_stdout = self.stdout_patcher.start()

    @patch("main.input", return_value="spam")
    def test_get_choices_does_not_accept_invalid_input(self, mock_input):
        self.assertRaises(ValueError, get_choices)

    @patch("main.input", return_value="rock")
    @patch("main.random.choice", return_value="paper")
    def test_get_choices_returns_a_hash(self, mock_random_choice, mock_input):
        expected_get_choices_return_value = {
            "player": "rock",
            "computer": "paper",
        }
        self.assertEqual(get_choices(), expected_get_choices_return_value)

    @patch("main.input", return_value="rock")
    @patch("main.random.choice", return_value="rock")
    def test_check_win_returns_tie_for_same_human_and_computer_choice(
        self, mock_random_choice, mock_input
    ):
        choices = get_choices()
        expected_output = """You chose rock Computer chose rock
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]), "It's a tie"
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="rock")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_rock_and_computer_picks_scissors(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "scissors"
        choices = get_choices()
        expected_output = """You chose rock Computer chose scissors
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Rock smashes scissors! You win!",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="rock")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_rock_and_computer_picks_paper(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "paper"
        choices = get_choices()
        expected_output = """You chose rock Computer chose paper
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Paper covers Rock! You lose.",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="paper")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_paper_and_computer_picks_rock(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "rock"
        choices = get_choices()
        expected_output = """You chose paper Computer chose rock
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Paper covers Rock! You win!",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="paper")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_paper_and_computer_picks_scissors(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "scissors"
        choices = get_choices()
        expected_output = """You chose paper Computer chose scissors
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Scissors cuts paper! You lose.",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="scissors")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_scissors_and_computer_picks_paper(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "paper"
        choices = get_choices()
        expected_output = """You chose scissors Computer chose paper
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Scissors cuts paper! You win!",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    @patch("main.input", return_value="scissors")
    @patch("main.random.choice")
    def test_check_win_returns_correct_results_when_human_picks_scissors_and_computer_picks_rock(
        self, mock_random_choice, mock_input
    ):
        mock_random_choice.return_value = "rock"
        choices = get_choices()
        expected_output = """You chose scissors Computer chose rock
"""
        self.assertEqual(
            check_win(choices["player"], choices["computer"]),
            "Rock smashes scissors! You lose.",
        )
        self.assertMultiLineEqual(self.mock_stdout.getvalue(), expected_output)

    def tearDown(self):
        self.stdout_patcher.stop()
