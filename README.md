# Bank-Transaction-History-Mini-Project
The mini project based on Python Datastructure (Stack) the performing undo and redo operation in this mini project.
Stack Concept Used: LIFO (Last In, First Out)

Undo Stack: Stores recent actions

Redo Stack: Stores undone actions

Efficient Data Handling: Undo/Redo works in O(1) time

Practical Use: Text editors, banking systems, version control, etc.
Concept: Stack

A stack is a Last-In-First-Out (LIFO) data structure.
Think of it like a stack of plates — the last plate you put on is the first one you take off.

Main Operations:

push(item) → Add an item on top of the stack

pop() → Remove the topmost item

Undo and Redo actions are implemented using two stacks:

undo_stack → Stores previous actions (for undo)

redo_stack → Stores undone actions (for redo)
