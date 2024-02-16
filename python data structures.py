#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])   # Output: 1

# Modifying elements
my_list[0] = 10
print(my_list)      # Output: [10, 2, 3, 4, 5]

# Adding elements
my_list.append(6)
print(my_list)      # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(3)
print(my_list)      # Output: [10, 2, 4, 5, 6]


# In[11]:


# Creating a tuple
my_tuple = (20, 19, 18, 17, 16)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Immutable (cannot modify elements)

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5


# In[3]:


# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)      # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)      # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)   # Output: {1, 2, 3, 4, 5}


# In[4]:


# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Accessing elements
print(my_dict['a'])     # Output: 1

# Modifying elements
my_dict['a'] = 10
print(my_dict)          # Output: {'a': 10, 'b': 2, 'c': 3}

# Adding elements
my_dict['d'] = 4
print(my_dict)          # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Removing elements
del my_dict['b']
print(my_dict)          # Output: {'a': 10, 'c': 3, 'd': 4}


# In[10]:


# Creating an array using a Python list
my_array = [3, 6, 1, 20, 31]

# Accessing elements
print(my_array[0])   # Output: 1

# Modifying elements
my_array[0] = 10
print(my_array)      # Output: [10, 2, 3, 4, 5]


# In[9]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

# Example usage:
stack = Stack()
stack.push(2)
stack.push(4)
stack.push(6)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3


# In[8]:


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

# Example usage:
binary_tree = BinaryTree(1)
binary_tree.root.left = Node(2)
binary_tree.root.right = Node(3)


# In[12]:


def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage:
string = "A man, a plan, a canal: Panama"
print(is_palindrome(string))  # Output: True


# In[13]:


def is_anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    # Check if the sorted characters of both strings are equal
    return sorted(s1) == sorted(s2)

# Example usage:
string1 = "listen"
string2 = "silent"
print(is_anagram(string1, string2))  # Output: True


# In[14]:


# Sorting an array
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_array = sorted(my_array)
print("Sorted Array:", sorted_array)

# Reversing an array
reversed_array = my_array[::-1]
print("Reversed Array:", reversed_array)


# In[15]:


# Sorting a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()
print("Sorted List:", my_list)

# Reversing a list
my_list.reverse()
print("Reversed List:", my_list)


# In[16]:


# Sorting a stack (using a list as a stack)
my_stack = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_stack = sorted(my_stack)
print("Sorted Stack:", sorted_stack)

# Reversing a stack (using a list as a stack)
reversed_stack = my_stack[::-1]
print("Reversed Stack:", reversed_stack)


# In[17]:


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def reverse_inorder_traversal(root):
    if root:
        reverse_inorder_traversal(root.right)
        print(root.value, end=" ")
        reverse_inorder_traversal(root.left)

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Original Tree (In-order Traversal):")
reverse_inorder_traversal(root)  # Output: 5 2 4 1 3


# In[ ]:




