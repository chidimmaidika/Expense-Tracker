#!/usr/bin/env python
# coding: utf-8

# # Introduction
# The goal of this assignment is to assess my understanding of object-oriented programming (OOP) concepts in Python. I have been tasked with implementing two classes, Expense and ExpenseDatabase, to model and manage financial expenses. 
# 
# The assignment tests my proficiency in defining classes, utilizing class attributes and methods,and handling time-related functionalities.
# 
# # Classes Overview:
# 
# 
# ## Expense Class:
# Represents an individual financial expense.
# 
# 
# ### Attributes:
# id: A unique identifier generated as a UUID string.
# title: A string representing the title of the expense.
# amount: A float representing the amount of the expense.
# created_at: A timestamp indicating when the expense was created (UTC).
# updated_at: A timestamp indicating the last time the expense was updated (UTC).
# 
# 
# ### Methods:
# __init__: Initializes the attributes.
# update: Allows updating the title and/or amount, updating the updated_at timestamp.
# to_dict: Returns a dictionary representation of the expense.
# 
# 
# 
# ## ExpenseDB class
# Manages a collection of Expense objects.
# 
# ### Attributes:
# expenses: A list storing Expense instances.
# 
# 
# ### Methods:
# __init__: Initializes the list.
# add_expense: Adds an expense.
# remove_expense: Removes an expense.
# get_expense_by_id: Retrieves an expense by ID.
# get_expense_by_title: Retrieves expenses by title.
# to_dict: Returns a list of dictionaries representing expenses.

# # Instructions
# ### Expense class
# 1. Implement an __init__ method to initialize the attributes.
# 2. Implement an update method that allows updating the title and/or amount of the expense.    
# The updated_at attribute should be automatically set to the current UTC timestamp whenever an update occurs.
# 3. Implement a to_dict method that returns a dictionary representation of the expense.

# In[2]:


import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at

    def update(self, title=None, amount=None):
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


# ### Expense Database class
# 1. Implement an __init__ method to initialize the expenses list.
# 2. Implement methods to:
#     - Add an expense to the database.
#     - Remove an expense from the database.
#     - Get an expense by ID.
#     - Get expenses by title (returning a list).
# 3. Create a to_dict method that returns a list of dictionaries representing each expense in the database.

# In[3]:


class ExpenseDatabase:
    def __init__(self):
        # Initialize the expenses list
        self.expenses = []

    def add_expense(self, expense):
        # Add an expense to the database
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        # Remove an expense from the database by ID
        self.expenses = [e for e in self.expenses if e.id != expense_id]

    def get_expense_by_id(self, expense_id):
        # Retrieve an expense by ID
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if the expense is not found

    def get_expenses_by_title(self, title):
        # Retrieve expenses by title (returning a list)
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        # Return a list of dictionaries representing each expense in the database
        return [expense.to_dict() for expense in self.expenses]


# In[ ]:




