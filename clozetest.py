from grammar_test import test1, test3, game

import random

if __name__ == "__main__":
    m = random.choice([test1, test3, game])
    m.madlib()
