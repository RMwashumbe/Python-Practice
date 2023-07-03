# create a function that gives you an average of a list
# data = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
def calculate_average(numbers):
    total = sum(numbers)
    count=len(numbers)
    average = total / count
    return average

mydata = [2, 4, 6, 8, 10, 12, 14, 16, 18, 100]
result = calculate_average(mydata)
print(result)
