# this is the "game_test.py" file...

from game import rock_paper_scissors_outcome

def test_of_outcome():
    assert rock_paper_scissors_outcome("rock", "rock") == None # represents a tie
    assert rock_paper_scissors_outcome("rock", "paper") == "paper"
    assert rock_paper_scissors_outcome("rock", "scissors") == "rock"

    assert rock_paper_scissors_outcome("paper", "rock") == "paper"
    assert rock_paper_scissors_outcome("paper", "paper") == None # represents a tie
    assert rock_paper_scissors_outcome("paper", "scissors") == "scissors"

    assert rock_paper_scissors_outcome("scissors", "rock") == "rock"
    assert rock_paper_scissors_outcome("scissors", "paper") == "scissors"
    assert rock_paper_scissors_outcome("scissors", "scissors") == None # represents a tie