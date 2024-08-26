  Consider the following n-ary tree:

        1
       /|\
      3 2 4
     / \
    5   6

The postorder traversal for this tree would be [5, 6, 3, 2, 4, 1].
Step-by-Step Execution:

Start with stack = [(1, False)].
Pop (1, False), push (1, True) and push (4, False), (2, False), (3, False) to stack.
Pop (3, False), push (3, True) and push (6, False), (5, False).
Pop (5, False), push (5, True).
Pop (5, True), append 5 to res.
Pop (6, False), push (6, True).
Pop (6, True), append 6 to res.
Pop (3, True), append 3 to res.
Pop (2, False), push (2, True).
Pop (2, True), append 2 to res.
Pop (4, False), push (4, True).
Pop (4, True), append 4 to res.
Pop (1, True), append 1 to res.
Final res = [5, 6, 3, 2, 4, 1], which is the correct postorder traversal.






