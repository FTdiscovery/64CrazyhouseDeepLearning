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

## Creating a Supervised Learning (SL) Based Model

As you may imagine, this step will require a database created from Crazyhouse games. There exists no database or folder for that attached in this repository; luckily, this process can be easily completed by following the steps on the documentation. The <b> CreateDatabase.py </b> file looks through all the PGN files in a folder and generates two numpy files for the neural network to train from. For that reason, it is important to first create two (empty) folders in the 64CrazyhouseDeepLearning repository. One will be named <i>lichessdatabase</i>, while the other will be named <i>Training Data</i>. You may change the names of them, of course - these are just the directories I have specified in the program - but bear in mind that it is necessary to change the code if you desire so.

Once these folders are created, we begin by adding Crazyhouse pgn files into the <i> lichessdatabase </i> folder. As the title suggest, zipped PGN files containing ~130-190,000 games can be downloaded [from the Lichess Database.](https://database.lichess.org/). These are found by clicking on the VARIANTS tab, and then scrolling down to the CRAZYHOUSE section. You may download as many files, or even take your own Crazyhouse PGN files input, and drag them into the <i> lichessdatabase </i> folder. Do note that for pgn files from the above database have to be unzipped.

Once all games are downloaded, simply run <b> CreateDatabase.py</b>. The file will take some time to generate a database. Be careful, however, of how much memory and RAM you have on your computer. A dataset of ~15,000 games creates an input matrix and output matrix with ~830,000 rows, and this requires 38.37 GB of space. 

The second step is to determine the model size 

## What if I have a GPU?

### Required Future Edits

1. GPU Optimization (Urgency: <b>High</b>)
2. Changes to playout mechanism. Right now, all playouts end only after a result (win or draw) is reached. However, in the future, the tree should be able to specify a search depth and use np.amax to determine the win probability in the final searched position (1-np.amax if depth is even). This has not been implemented yet, as all values outputted by the neural network are less than 1e-03 after the first ten moves or so. (Urgency: <b>High</b>)
3. Create a Leela-like online server training system for everyone to work with and to lend their GPUs on. (Urgency: <b>medium</b>)
4. Time Control – If this engine is to compete in competitions, it must be able to determine when it can search further, and whether it has the time to do so.(Urgency: <b>low</b>)
5. Translate into C++? (Urgency: <b>low</b>)

## Contributors

Below is a list of contributors to the project:
