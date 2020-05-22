"""Module for testing binary search tree"""

import random
from time import time
from binary_search_tree.linkedbst import LinkedBST


def read_file(path):
    """
    Read file and save it into list
    :param path: str
    :return: list
    """
    with open(path, "r", encoding="utf-8") as file:
        text = []
        line = file.readline()
        while line:
            text.append(line.lower().strip())
            line = file.readline()
        return text


def test_list():
    """
    Tests search tree and returns time
    :return: float
    """
    test_words = random.sample(WORDS, 10000)
    search_words = random.sample(WORDS, 990)
    start = time()
    for word in test_words:
        try:
            search_words.index(word)
        except ValueError:
            pass
    finish = time()
    return finish - start


def test_tree(ordered=True, balanced=False):
    """
    Tests search tree and returns time
    :param ordered: bool
    :param balanced: bool
    :return: float
    """
    test_words = random.sample(WORDS, 10000)
    tree_words = random.sample(WORDS, 990)
    if ordered:
        tree_words = sorted(tree_words)
    empty_tree = LinkedBST()
    for item in tree_words:
        empty_tree.add(item)
    if balanced:
        empty_tree = empty_tree.rebalance()
    start = time()
    for word in test_words:
        empty_tree.find(word)
    finish = time()
    return finish - start


def main():
    """
    Function for running tests and writing results in file
    :return: None
    """
    with open("test_results.txt", "w", encoding="utf-8") as file:
        result = []
        temps = [0 for _ in range(4)]
        for _ in range(10):
            test = [test_list(), test_tree(), test_tree(False, False), test_tree(False, True)]
            for j, _ in enumerate(temps):
                temps[j] += test[j]
            result.append("  ".join(list(map(lambda x: '{:.4f}'.format(x), test))) + "\n")
        temps = list(map(lambda x: '{:.4f}'.format(x / 10), temps))
        result.append("==============================\n")
        result.append("  ".join(temps))
        file.writelines(result)


if __name__ == '__main__':
    WORDS = read_file("words.txt")
    main()
