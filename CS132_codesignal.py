'''
If a queue only allows operations at the ends (front and back), 
what other data structure would work perfectly to use to build the queue?
A: Linked List
Stacks are useful for it's fast operations, 
which are push, pop, peek. They all take constant O(1) runtime.

They are Last-in First-Out, so elements are added to the top 
(or the right) of the collection using push, and the most recent 
elements are removed first using pop.
'''

'''
Implement a queue using two stacks.

You are given an array of requests, where requests[i] can be 
"push <x>" or "pop". Return an array composed of the results 
of each "pop" operation that is performed.

Example

For requests = ["push 1", "push 2", "pop", "push 3", "pop"], 
the output should be
queueOnStacks(requests) = [1, 2].

After the first request, the queue is {1}; after the second it 
is {1, 2}. Then we do the third request, "pop", and add the first 
element of the queue 1 to the answer array. The queue becomes {2}. 
After the fourth request, the queue is {2, 3}. Then we perform "pop" 
again and add 2 to the answer array, and the queue becomes {3}.
'''
'''
Runtime: O(n)
Space: O(n)
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)
        return left

    def remove():
        while not left.isEmpty():
            right.push(left.pop())
        result = right.pop()
        while not right.isEmpty():
            left.push(right.pop())
        return result
        
    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans

'''
Given a string sequence consisting of the characters '(', ')', '[', ']', '{', and '}'. Your task is to determine whether or not the sequence is a valid bracket sequence.

The Valid bracket sequence is defined in the following way:

An empty bracket sequence is a valid bracket sequence.
If S is a valid bracket sequence then (S), [S] and {S} are also valid.
If A and B are valid bracket sequences then AB is also valid.
For sequence = "()", the output should be validBracketSequence(sequence) = true;
For sequence = "()[]{}", the output should be validBracketSequence(sequence) = true;
For sequence = "(]", the output should be validBracketSequence(sequence) = false;
For sequence = "([)]", the output should be validBracketSequence(sequence) = false;
For sequence = "{[]}", the output should be validBracketSequence(sequence) = true.
'''
'''
Runtime: O(n)
Space: O(n)
'''

def validBracketSequence(sequence):
    result = []
    
    openSymbol = '([{'
    
    for char in sequence:
        if char in openSymbol:
            result.append(char)
        elif char == ")":
            if len(result) > 0 and result[-1] == "(":
                result.pop()
            else:
                result.append(char)
        elif char == "]":
            if len(result) > 0 and result[-1] == "[":
                result.pop()
            else:
                result.append(char)
        elif char == "}":
            if len(result) > 0 and result[-1] == "{":
                result.pop()
            else:
                result.append(char)
        else:
            return False
    
    return result == []        

