'''
How can you compute the total number of nodes in a 
"perfect" binary tree if you know the height?
2^h - 1 where h is the height of the binary tree.

What is one of the primary weaknesses of the binary 
search tree as a data structure?
The performance degrades if it becomes unbalanced.

What does the phrase "in-order successor" mean 
when we are talking about a node in a binary search tree?
The node that has the next highest value.
'''

'''
You are given a binary tree and you need to write a 
function that can determine if it is height-balanced.

A height-balanced tree can be defined as a binary tree 
in which the left and right subtrees of every node differ 
in height by a maximum of 1.
'''
def maxDepth(root):
    if root is None:
        return 0
        
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1
        
def minDepth(root):
    if root is None:
        return 0
        
    else:
        return min(minDepth(root.left), minDepth(root.right)) + 1
        
        
def balancedBinaryTree(root):
    return (maxDepth(root) - minDepth(root)) <= 1
        
def balancedBinaryTree1(root):
    
    if root is None:
        return True
    
    else:
        left_h = maxDepth(root.left)
        right_h = maxDepth(root.right)

        if (abs(left_h - right_h) <= 1):
            return True
            
        else:
            return False

        # if left_h > (right_h + 1) or left_h < (right_h - 1):
        #     return False
        
        # else:
        #     return True
        
        #get min and max of each subtree and compare if it's more than one

'''
Author's solution
'''
def balancedBinaryTree(root):
    # Compute the tree's height via recursion
    def height(root):
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(height(root.left), height(root.right))
    
    # An empty tree satisfies the definition of a balanced tree
    if not root:
        return True

    # Check if subtrees have height within 1. If they do, check if the
    # subtrees are balanced
    return abs(height(root.left) - height(root.right)) < 2 \
        and balancedBinaryTree(root.left) \
        and balancedBinaryTree(root.right)

'''
You are given a binary tree and you are asked to 
write a function that finds its minimum depth. 
The minimum depth can be defined as the number of 
nodes along the shortest path from the root down to 
the nearest leaf node. As a reminder, a leaf node is 
a node with no children.
'''
#my approach, didn't pass one test
def minimumDepthBinaryTree1(root):
    height = None
    
    if root is None:
        return 0
        
    else:
        left_h = minimumDepthBinaryTree(root.left)
        right_h = minimumDepthBinaryTree(root.right)
        
        min_height = min(left_h, right_h) + 1
        
        return min_height
        
        
#iterative approach
def minimumDepthBinaryTree2(root): 
    if root is None:
        return 0
    
    q = []
    
    # Enqueue root and initialize depth as 1
    q.append({'node': root , 'depth' : 1})
 
    # Do level order traversal
    while(len(q)>0):
        # Remove the front queue item
        queueItem = q.pop(0)
     
        # Get details of the removed item
        node = queueItem['node']
        depth = queueItem['depth']
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:   
            return depth
         
        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({'node' : node.left , 'depth' : depth+1})
 
        # if right subtree is not None, add it to queue
        if node.right is not None: 
            q.append({'node': node.right , 'depth' : depth+1})

#recursive approach
def minimumDepthBinaryTree(root):
    if not root.left and not root.right:
        return 1

    if not root.left:
        return minimumDepthBinaryTree(root.right) + 1

    if not root.right:
        return minimumDepthBinaryTree(root.left) + 1
        
    if root.left and root.right:
        return(min(
            minimumDepthBinaryTree(root.left),
            minimumDepthBinaryTree(root.right)
        )) + 1

'''
Author's Solution
'''
def minimumDepthBinaryTree(root):
    if root is None: 
        return 0 
    
    children = [root.left, root.right]
    # if we're at leaf node
    if not any(children):
        return 1
    
    min_depth = float('inf')
    for c in children:
        if c:
            min_depth = min(minimumDepthBinaryTree(c), min_depth)
    return min_depth + 1 
