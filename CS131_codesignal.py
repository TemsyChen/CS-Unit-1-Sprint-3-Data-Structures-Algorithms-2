'''
What are the strengths of a Linked List as a data structure?
1. Fast operations at both ends (head and tail)
2. They can grow and shrink to accomodate the data
'''

'''
What is the primary weakness of a Linked List data structure?
1. Costly search operations
'''

'''
Note: Your solution should have O(n) time complexity, 
where n is the number of elements in l, since this is 
what you will be asked to accomplish in an interview.

You have a singly linked list l, which is sorted in 
strictly increasing order, and an integer value. 
Add value to the list l, preserving its original sorting.

Note: in examples below and tests preview linked lists 
are presented as arrays just for simplicity of visualization: 
in real data you will be given a head node l of the linked list
'''

'''
Understand:
l = [1, 3, 4, 6], value = 5 --> [1, 3, 4, 5, 6]
l = [1, 3, 4, 6], value = 10 --> [1, 3, 4, 6, 10]
l = [1, 3, 4, 6], value = 0 --> [0, 1, 3, 4, 6]

Plan: Make if statements for 4 possible situations:
1 - the linked list is empty
2 - the value belongs at the head of the list
3 - the value belongs at the middle of the list
4 - the value belongs at the tail of the list
Note: the code to insert linked lists is
-find where the value should operate, if value >< current.next.value
-point the new node to the next node "new_node.next = current.next"
-point the current node to the new node "current.next = next_node"

Runtime: O(n) to iterate through the elements of l
Space: O(1) inserting just one more element
'''


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
    
def insertValueIntoSortedLinkedList(l, value):
    new_node = ListNode(value)
    current = l
    
    #insert if the linked list is empty        
    if l is None:
        l = new_node
        return l
    
    #insert if the value belongs at the head
    if value < l.value: #if value is lower than the head value
        new_node.next = l #point the new node to the head
        return new_node
    
    #insert if the value belongs at the middle
    while current.next: #while you are before the end of the list
        if value < current.next.value: #if the value is less than the next node
            new_node.next = current.next #point the new node at the next node
            current.next = new_node #put the next node after the current node
            return l
        current = current.next #move the current node over one to iterate
        
    #insert if the value belongs at the tail
    last = l
    while (last.next): #while there is a next node
        last = last.next #this ends with the pointer at the end of the list
    last.next = new_node #inserts the value after the last node
    return l
    
'''
Author's solution
'''
ListNode<Integer> insertValueIntoSortedLinkedList(ListNode<Integer> l, int value) {
  if (l == null) {
    return new ListNode<>(value);
  }
  if (value < l.value) {
    ListNode<Integer> result = new ListNode<>(value);
    result.next = l;
    return result;
  }
  ListNode<Integer> head = l;
  while (l != null) {
    if (l.value < value && (l.next == null || l.next.value > value)) {
      ListNode<Integer> next = new ListNode<>(value);
      next.next = l.next;
      l.next = next;
      break;
    }
    l = l.next;
  }
  return head;
}

'''
Note: Your solution should have O(l1.length + l2.length) 
time complexity, since this is what you will be asked to 
accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, 
your task is to merge them. In other words, return a singly 
linked list, also sorted in non-decreasing order, that contains 
the elements from both original lists.
'''

'''
Understand:
l1 = [1, 2, 3], l2 = [4, 5, 6] --> [1, 2, 3, 4, 5, 6]
l1 = [1, 1, 2, 4], l2 = [0, 3, 5] --> [0, 1, 1, 2, 3, 4, 5]

Plan:
Create a new list that will merge the two input lists.
Create pointers for the two input lists and the new list.
Make if statements for the following situations:
1 - if l1 is empty
2 - if l2 is empty
3 - looking at each pointer and seeing which value is lower,
inserting that value into the newList.
(do this once to start the newList)
3a - make current point at the newList value
4 - look at each pointer for the lower value,
fill the newList with each value from both lists.
5 - if one pointer runs out, fill it with the rest of the 
other pointer.

Runtime: O(n), to iterate through both lists

Space: O(n), the length of the newList
'''


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    newList = None
    node1 = l1 #pointer for l1
    node2 = l2
    current = None
    
    if not node1: #executes if node1 is any kind of zero or empty container
        return node2
        
    if not node2:
        return node1
    
    if node1.value < node2.value: #this begins the newList
        newList = ListNode(node1.value) #creates a node with the l1 value
        node1 = node1.next
    else:
        newList = ListNode(node2.value)
        node2 = node2.next
        
    current = newList #creates a pointer on newList
            
    while node1 and node2: #while the two node pointers exist
        if node1.value < node2.value:
            current.next = ListNode(node1.value)
            node1 = node1.next #move the l1 pointer over one
        else:
            current.next = ListNode(node2.value)
            node2 = node2.next
        current = current.next #move the newList pointer over one
    
    if node1: #if there is one pointer left
        current.next = node1 #make the next node what the l1 pointer node is
    elif node2:
        current.next = node2
        
    return newList
    
'''
Author's Solution
'''
ListNode<Integer> mergeTwoLinkedLists(ListNode<Integer> l1, ListNode<Integer> l2) {
  if (l1 == null) {
    return l2;
  }
  if (l2 == null) {
    return l1;
  }
  ListNode<Integer> result = null;
  ListNode<Integer> prev = null;
  ListNode<Integer> head = null;
  while (l1 != null && l2 != null) {
    if (l1.value.compareTo(l2.value) <= 0) {
      result = new ListNode<>(l1.value);
      l1 = l1.next;
    } else {
      result = new ListNode<>(l2.value);
      l2 = l2.next;
    }
    if (prev != null) {
      prev.next = result;
    } else {
      head = result;
    }
    prev = result;
  }
  while (l1 != null) {
    result = new ListNode<>(l1.value);
    l1 = l1.next;
    prev.next = result;
    prev = result;
  }
  while (l2 != null) {
    result = new ListNode<>(l2.value);
    l2 = l2.next;
    prev.next = result;
    prev = result;
  }
  return head;
}
