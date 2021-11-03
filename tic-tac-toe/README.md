# Harvard CS50's Introduction to Artificial Intelligence with Python 2021 course

### Project 0b - Tic Tac Toe
* A simple AI for the famous tic tac toe game
* The `runner.py` file with the graphic environment and the game flow code was given in the distribution code
* The goal was to implement the functions of the `tictactoe.py` file

### Optimizations
* Via the `opt` flag of the `tictactoe.py` file, you can choose which optimization method will be used
* The first method is tha alpha-beta pruning method
* In the second method (chosen by default in line 12), I am using a set and two hashmaps, to 'remember' the explored states and decrease the time complexity by not calculating their values again and again
* The second optimization has a better time complexity, but requires more memory for the explored set and the hashmaps

- - -

* Developer: Giannis Athanasiou
* Github Username: John-Atha
* Email: giannisj3@gmail.com