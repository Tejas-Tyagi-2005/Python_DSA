# ============================================================
# PROBLEM 20 — PRODUCT POSITIVE NUMBERS
# ============================================================
# Task:
# Find the product of all positive numbers in an array.
#
# Example:
# arr = [-2, 5, 2, -3, 4]
#
# Answer:
# 40
#
# Function:
# def positive_product(arr):
#     ...


def pos(arr):


    product = 1 

    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] * product

    return product 
        

