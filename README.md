# 64 Crazyhouse Deep Learning
A deep learning Crazyhouse chess program that uses a Monte Carlo Tree Search (MCTS) based evaluation system and reinforcement to enhance its play style. Created as an individual project by a high school student.

Information on the inner workings and the code breakdown can be found on the blog post [here](https://ftlearning.wordpress.com/2018/08/13/64-a-crazyhouse-learning-project/). 

Side Note: Parts of the code are yet to be optimized since project is still in progress.


## What is this?

This is a framework of a neural network-based Crazyhouse Chess Engine inspired by the procedures specified by Google DeepMind and their multiple papers on AlphaGo and AlpahZero. This project was initiated in June 15, 2018, following the successful framework of a self-learning Tic Tac Toe engine that managed to solve the game in an hour. You may find the repository for that [here](https://github.com/FTdiscovery/GOMCTS); however, that project has yet to be annotated for the general public to use. 

Currently, this repository is designed for three processes: supervised learning (training a network model based on PGN master games), reinforcement learning (having the best network play itself to generate training games, from which this data can be used to train better networks), as well as self-learning (start with a randomly initialized or even a pre-trained Pytorch model if desired, from which training games and new networks will be created for however long the user desires.)

As of now, due to the lack of computational resources readily available for me, the focus is on creating a trained model based on top available games. From this documentation, I will explain the whole process of training a model and sending it back for further testing. 

Your name will be added on the list of contributors once you have uploaded a relevant file. :)

## Requirements

It will be necessary to download the following packages:

python-chess <br>
scipy <br>
numpy (if that's somehow not on your computer) <br>
torch (pytorch) <br>
torchvision <br>
pathlib <br>

As this program was written, tested, and edited on the PyCharm CE IDE, I also recommend that users also download the interpreter and run the code on it. However, I acknowledge that it is possible to run any of the attached files through terminal/other IDEs, provided that all the necessary libraries are downloaded. Python 3 (3.6) is strongly recommended.


Once these are all running on your computer, then you will be able to continue to the next step!

## How do I run the program?

Start off by downloading the repository through terminal...

    git clone https://github.com/FTdiscovery/64CrazyhouseDeepLearning.git
    
... or by downloading the ZIP file on the top right hand corner.

## How does this program work?

You can learn more about the training checkpoints, parameters, and others on the [wiki](https://github.com/FTdiscovery/64CrazyhouseDeepLearning/wiki)!

## Future Goals

I plan on writing the engine for UCI Compatibility. The current barebones are written on UCICommunication.py, and will be worked upon once the policy and value networks are trained.

## Additional Code Information

### Input Representation
The input for the neural network is a basic (raw) representation of the board. It is an array of 960 values (15 planes of 8×8 boards), which determines the player turn, position of each piece type, captive pieces held by a player, and whether the piece is a promotion. The last part is relevant since promoted pieces can only be placed down as pawns after being captured.

### Output Representation
The output for the neural network is a 1D representation of multiple move planes (8×8 boards). Here they are as followed:

The first five planes represent the possible squares in which a given piece should be placed (pawn, knight, bishop, rook, queen).

The next plane represents the piece that should be picked up from the board.

The next 56 planes represent the possible queen moves. There are 8 planes for each direction (N, NE, E, SE, S, SW, W, NW), and 7 planes for how far a piece can move (1-7). This is used to map all moves made by a pawn, bishop, rook, queen, and king.

The next 8 planes represent the possible knight moves (2F1L, 2F1R, 1F2L, 1F2R, 1B2L, 1B2R, 2B1L, 2B1R). This is used to map moves made by a knight.

Last, we have 3 planes of 8×1 boards, which determine the column in which a pawn is being underpromoted. Each plane denotes a different promotion (rook, bishop, knight).

In total, the action is represented by an array of (5+1+56+8) x (8×8) + 3×8 = 4504 values.

## Sample Games


### Self Play Games


GAME 1: 1. e4 e6 2. d4 d5 3. e5 Ne7 4. Nf3 Nf5 5. Bd3 Nc6 6. O-O Be7 7. c3 O-O 8. Bf4 f6 9. Nbd2 fxe5 10. dxe5 P@e4 11. P@d6 exf3 12. Nxf3 Bxd6 13. exd6 P@e4 14. Bxe4 dxe4 15. P@g5 exf3 16. gxf3 N@h4 17. B@h3 N@e2+ 18. Kh1 B@g2+ 19. Bxg2 Nxg2 20. Kxg2 Nh4+ 21. Kh1 B@g2# 0-1


GAME 2: 1. e4 Nc6 2. Nc3 Nf6 3. Nf3 d5 4. exd5 Nxd5 5. Bc4 e6 6. O-O Nb6 7. Bb5 Bd7 8. Re1 Be7 9. d4 O-O 10. P@h6 gxh6 11. Bxh6 P@e4 12. P@g7 exf3 13. Qxf3 P@g4 14. Qxg4 N@f5 15. gxf8=Q# 1-0


GAME 3: 1. e4 Nc6 2. Nc3 Nf6 3. Nf3 d5 4. exd5 Nxd5 5. d4 e6 6. Bb5 Bb4 7. Bd2 Bxc3 8. bxc3 N@e4 9. @b2 Nxd2 10. Qxd2 B@h5 11. O-O-O O-O 12. Kb1 @g4 13. Ng5 Bg6 14. Nxf7 Rxf7 15. Bxc6 bxc6 16. N@h6+ gxh6 17. Qxh6 Rf6 18. N@e7+ Kh8 19. B@g7# 1-0

### Wins against Humans

GAME 4: 1. e4 Nf6 2. e5 d5 3. d4 Ne4 4. f3 Bf5 5. fxe4 dxe4 6. Bc4 e6 7. Nc3 Qh4+ { White resigns. } 0-1

GAME 5: 1. e4 e5 2. Nf3 Nc6 3. Bc4 d6 4. Nc3 Be7 5. d4 exd4 6. Nxd4 Nxd4 7. Qxd4 P@h3 8. Bxf7+ Kxf7 9. Qd5+ B@e6 10. Qh5+ g6 11. Qf3+ Nf6 12. N@g5+ Kg7 13. P@h6+ Kxh6 14. Nxe6+ g5 15. Bxg5+ Kg6 16. Qf5+ Kf7 17. Nxd8+ Bxd8 18. B@d5+ P@e6 19. Bxe6+ Bxe6 20. Qxe6+ Kxe6 21. P@f5+ Kf7 22. P@e6+ { Black resigns. } 1-0



## Contributors

Below is a list of contributors to the project:
