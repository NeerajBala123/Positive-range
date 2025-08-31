list1 = list(map(int, input("Enter numbers : ").split()))
print("Input:", list1)
positive_numbers = [num for num in list1 if num > 0]
print("Output:", positive_numbers)
