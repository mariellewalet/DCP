import random

class Markov:
    def __init__(self, transitions):
        self.transitions = transitions
        self.states = list(set([state for state, _, _ in transitions]))

    def prob(self, state, ran_num):
        temp = 0
        for start, end, prob in self.transitions:
            if start == state:
                if temp<= ran_num < temp+prob:
                    return end
                temp += prob
        return None

    def step(self, state):
        if state not in self.states:
            return None
        random_num = random.random()
        return self.prob(state, random_num)

def run_steps(start, transitions, num_steps ):
    chain = Markov(transitions)
    num_iterations = dict()
    for state in chain.states:
        num_iterations[state] = 0
    for i in range (0, num_steps):
        start = chain.step(start)
        num_iterations[start] += 1
    return num_iterations


if __name__ =='__main__':
    transitions = [
        ('a', 'a', 0.9),
        ('a', 'b', 0.075),
        ('a', 'c', 0.025),
        ('b', 'a', 0.15),
        ('b', 'b', 0.8),
        ('b', 'c', 0.05),
        ('c', 'a', 0.25),
        ('c', 'b', 0.25),
        ('c', 'c', 0.5)
    ]
    print(run_steps('a', transitions, 5000))
