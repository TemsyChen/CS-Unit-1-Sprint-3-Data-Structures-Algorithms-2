'''
What are the two primary categories for tree traversals?
1. Depth-First
2. Breadth-First

Select the three different types of depth-first traversals.
Inorder, Preorder, Postorder

Select the correct ordering of steps for an inorder depth-first traversal.
1. Go to the left subtree
2. Visit node
3. Go to the right subtree

Select the correct ordering of steps for a preorder depth-first traversal.
1. Visit node
2. Go to the left subtree
3. Go to the right subtree

Select the correct ordering of steps for a postorder depth-first traversal.
1. Go to the left subtree
2. Go to the right subtree
3. Visit node

What data structure would you use in order 
to write an iterative depth-first traversal method?
Stack
'''

'''
You are given a binary tree. Write a function that 
returns the binary tree's node values using an in-order traversal.

Understand:
Input: [2,None,3,4]

   2
    \
     3
    /
   4
Output: [2,4,3]
'''
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeInOrderTraversal(root):
    result = []
    helper(root, result)
    return result
    
def helper(root, res):
    if root is None:
        return
    helper(root.left, res)
    res.append(root.value)
    helper(root.right, res)

'''
Author's Solution
''''
def helper(root, res):
    if root is not None:
        if root.left is not None:
            helper(root.left, res)
        res.append(root.value)
        if root.right is not None:
            helper(root.right, res)
            
def binaryTreeInOrderTraversal(root):
    res = []
    helper(root, res)
    return res

'''
Note: Try to solve this task without using recursion, 
since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node 
values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at 
height 1 (i.e. the root children), ordered from the leftmost 
to the rightmost one;
The elements after that should be the values of the nodes at 
height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
traverseTree(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    if t is None:
        return []
        
    result = []
    queue = []
    queue.append(t)
    
    while len(queue) != 0:
        node = queue.pop(0)
        result.append(node.value)
        
        if node.left is not None:
            queue.append(node.left)
            
        if node.right is not None:
            queue.append(node.right)
    
    return result

'''
Given a binary tree of integers, return all the paths from 
the tree's root to its leaves as an array of strings. 
The strings should have the following format:
"root->node1->node2->...->noden", representing the path 
from root to noden, where root is the value stored in the 
root and node1,node2,...,noden are the values stored in the 
1st, 2nd,..., and nth nodes in the path respectively 
(noden representing the leaf).

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 10,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": -3,
        "left": null,
        "right": null
    }
}
the output should be
treePaths(t) = ["5->2->10", "5->2->4", "5->-3"].

The given tree looks like this:

    5
   / \
  2  -3
 / \
10  4
'''

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def treePaths(t):
    if t is None:
        return []
    result = []
    helper(t, result, [])
    return result

def isleaf(t):
    return t.left is None and t.right is None

def helper(t, result, path):
    if t is None:
        return
        
    path.append(f'{t.value}')
    if isleaf(t):
        result.append("->".join(path))
    helper(t.left, result, path)
    helper(t.right, result, path)
    
    path.pop()