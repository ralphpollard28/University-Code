"""
This file contains the code for the Week 3 lab exercises,
focusing on for loops, while loops, and GitHub integration.
"""

# Example of a for loop that prints numbers from 1 to 10
for i in range(10):
    print(f"This is iteration number {i + 1}")  

# Example of a for loop that prints even numbers from 2 to 20
for i in range(2, 21, 2):
    print(f"Even number: {i}")


costs = [15.00, 12.50, 3.75, 40.25, 6.99]
total_cost = 0
for cost in costs:
    total_cost += cost
print(f"Total cost of items: ${total_cost:.2f}")




