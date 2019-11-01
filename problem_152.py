""" You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly."""
from random import random

def generate_number(numbers: list, probabilities: list):
    randnum = random()
    temp = 0

    for i, prob in enumerate(probabilities):
        if temp<= randnum < temp+prob:
            return numbers[i]
        temp+= prob


if __name__ == '__main__':
    numbers = [1,2,3,4]
    probs = [0.1, 0.5, 0.2, 0.2]
    print(generate_number(numbers, probs))