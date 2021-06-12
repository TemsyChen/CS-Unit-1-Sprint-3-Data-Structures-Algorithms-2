'''
Note: Your solution should have O(l.length) 
time complexity and O(1) space complexity, 
since this is what you will be asked to accomplish in an interview.

Given a singly linked list, reverse and return it.

Example

For l = [1, 2, 3, 4, 5], the output should be
reverseLinkedList(l) = [5, 4, 3, 2, 1].
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    current = l
    prev = None
    next_node = None
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

'''
You are given the root node of a binary search tree (BST).

You need to write a function that returns the sum of 
values of all the nodes with a value between lower and upper (inclusive).

The BST is guaranteed to have unique values.

Example 1:

Input:
root = [10, 5, 15, 3, 7, null, 18]
lower = 7
upper = 15

         10
         / \
        5  15
       / \    \
      3   7    18

Output:
32
'''
'''
Understand:
traverse the tree and store the node.value if it is between the boundaries. Sum up the stored values
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBSTRangeSum(root, lower, upper):
    values = []
    result = []
    helper(root, values)
    for value in values:
        if value <= upper and value >= lower:
            result.append(value)
        else:
            continue
    return sum(result)
    
def helper(root, res):
    if root is None:
        return
    helper(root.left, res)
    res.append(root.value)
    helper(root.right, res)
    
'''
Given a binary tree, write a function that inverts the tree.

Example:

Input:
     6
   /   \
  4     8
 / \   / \
2   5 7   9

Output:
     6
   /   \
  8     4
 / \   / \
9   7 5   2
'''
'''
Understand:
Do an preorder traversal. Swap out the left and right nodes by saving one side to a third temporary variable. Go down the tree recursively, which will repeat the swap of left and right down the subtree. 

Runtime: O(n) to traverse the tree
Space: O(1) saving just one temporary variable.
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def csBinaryTreeInvert(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    csBinaryTreeInvert(root.left)
    csBinaryTreeInvert(root.right)
    return root

