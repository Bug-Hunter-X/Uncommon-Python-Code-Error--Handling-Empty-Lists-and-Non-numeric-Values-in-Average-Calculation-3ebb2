def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0 which is correct

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 3.0 which is correct

my_list = [1,2,3,4,'a']
result = calculate_average(my_list) #This will throw an error