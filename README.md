# rock-paper-scissors-app

Welcome to my Rock Paper Scissors application, where you can play rock paper scissors against the computer. Before you can play, there are a few setup steps detailed below 

## Setup of Environment

### Clone Repository To Local Desktop

Using the Code ("Green Button") in GitHub Online (above), Open the repository with GitHub Desktop.
*Note, remember the file path of where you are saving the repository, as you will need this in the next step.

### Navigate to your files and create and activate a new project-specific Anaconda virtual environment:

Using your command-line (Terminal on Mac, Git Bash on Windows), navigate to the file path of the repository you recently saved to your local desktop

`cd ~/Desktop/rock-paper-scissors-app` 
(if not saved in the Desktop folder, replace 'Desktop' with the appropriate file path from above)

Now, create and activate a new project-specific Anaconda virtual environment to run the rock paper scissors game:

```sh
conda create -n my-game-env python=3.8 # (first time only)

conda activate my-game-env
```

Within that virtual environment, run our rock-paper-scissors game calling the following script: 

`python game.py`

### Playing the Game

When prompted, please enter your choice of Rock, Paper, or Scissors.

If you spelled one of the above choices correctly, you will be notified of the results of the game (including the computer's pick). If you have spelled your choice incorrectly, please re-run the above code to run our game `python game.py` and retry. 

#### Extra - Running a personal game of rock paper scissors, where you are the player:

If you want to play a more intimate game, where "you" (your name) is Player 1 rather than the standard "Player 1" title, run the following script to launch the game: 

`PLAYER_NAME="Your Name Here" python game.py` (insert your name in the quotations)


