#!/usr/bin/python3
"""determine if all the boxes can be opened"""


def canUnlockAll(boxes):
    """
    Return: True or False
    """
    n = len(boxes)
    if n == 0:
        return True
    
    unlocked = {0}
    stack = [0]
    
    while stack:
        curr_box = stack.pop()
        for key in boxes[curr_box]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n
