class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_min(top):
    while top.left is not None:
        top = top.left

    return top


def bst_max(top):
    if top is None:
        raise ValueError("Uwaga - puste drzewo")

    while top.right is not None:
        top = top.right

    return top
