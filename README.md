# Fibonacci Photo v1.1

## **Info**
Fibonacci was an Italian mathematician that lived lived in the 12th century. He is regarded as one of the biggest mathematicians ever because of his work on numbers. One of his most notable works is the so called Fibonacci Sequence. It follows two simple rules:

1. The sequence starts with 0, 1 (or 1, 1)
2. Every next number is the sum of the two previous ones

So the sequence becomes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ...
There's also a geometric interpretation of the Fibonacci sequence. It tells you that you can create a square with side length of a Fibonacci number, put them together in a pattern so that it always forms a rectangle. It looks like this:

![Fibonacci Photo](https://github.com/Cqsi/Fibonacci-Photo/blob/master/test_images/fibonacci_rectangle.png)

Fibonacci Photo will produce this pattern, but instead of colored squares, you can input an image (only square photos for now) and it will output a new image in this pattern where each square is your inputed image. The photo is then rotated 90 degrees. Quite fun huh?

## Installation Guide

Go to a terminal and do these steps.


1. Clone this repository by running `git clone https://github.com/Cqsi/Fibonacci-Photo`

2. Run `cd FibonacciPhoto`

3. Run `pip install -r requirements.txt`

4. Open `defaults.py` in a text editor, and edit the variable in that file to your path of image ( + the limit, but you can just leave it)

5. Run main.py and your photo will be generated in the folder `generated_media`

6. Don't move any folders or code files outside the directories or the program won't work

Have fun!

## Examples

If you run with the default settings in `defaults.py` this photo will be generated in `generated_media`:

![Fibonacci Photo](https://github.com/Cqsi/Fibonacci-Photo/blob/master/test_images/example.png)