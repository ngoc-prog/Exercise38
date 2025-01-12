import random

#1: Initialize a list with 10 random elements (values from -100 to 100)
lst = [random.randint(-100, 100) for _ in range(10)]
print("Initial list:", lst)

#2: Add elements to the list
element_to_add = int(input("Enter an element to add to the list: "))
lst.append(element_to_add)
print("List after adding an element:", lst)

#3: Enter k, check how many times k appears in the list
k = int(input("Enter a value to count its occurrences in the list: "))
count_k = lst.count(k)
print(f"The value {k} appears {count_k} times in the list.")

#4: Calculate the sum of the perfect numbers in the list
def is_perfect(n):
    if n < 1:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

perfect_numbers = [num for num in lst if is_perfect(num)]
sum_perfect_numbers = sum(perfect_numbers)
print("Perfect numbers in the list:", perfect_numbers)
print("Sum of perfect numbers:", sum_perfect_numbers)

#5: Sort the list (ascending and descending)
lst.sort()  # Ascending order
print("List sorted in ascending order:", lst)
lst.sort(reverse=True)  # Descending order
print("List sorted in descending order:", lst)

#6: Delete elements from the list
#Delete a specific element
element_to_delete = int(input("Enter an element to delete from the list: "))
if element_to_delete in lst:
    lst.remove(element_to_delete)
    print(f"List after removing {element_to_delete}:", lst)
else:
    print(f"{element_to_delete} not found in the list.")

#Delete negative numbers
lst = [x for x in lst if x >= 0]
print("List after deleting negative numbers:", lst)

#Delete the entire list
lst.clear()
print("List after clearing:", lst)
