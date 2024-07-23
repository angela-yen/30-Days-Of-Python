empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# join with extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 

# Level 1

# 1. Declare an empty list
list = []

# 2. Declare a list with more than 5 items
list = ["apple", "banana", "orange", "grape", "lemon"]

# 3. Find the length of your list
len(list)

# 4. Get the first item, the middle item and the last item of the list
print(list[0])
print(list[2])
print(list[len(list) - 1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["ange", 28, 174, "not married", "Salisbusry St"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[2])
print(it_companies[len(it_companies) - 1])

print(it_companies[::3])

# 10. Print the list after modifying one of the companies
it_companies[0] = "Canva"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append('GitLab')

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Instagram')

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper()

# 14. Join the it_companies with a string '#;  '
new = it_companies + ['#;  ']
print(new)

# 15. Check if a certain company exists in the it_companies list.
print('Instagram' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)

# 18. Slice out the first 3 companies from the list
del it_companies[0:3]

# 19. Slice out the last 3 companies from the list
del it_companies[-3::]

# 20. Slice out the middle IT company or companies from the list
middle = (len(it_companies) - 1 )/ 2
it_companies.pop(middle)

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22.Remove the middle IT company or companies from the list
it_companies.pop(middle)

# 23. Remove the last IT company from the list
it_companies.pop

# 24. Remove all IT companies from the list
it_companies.clear

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined_list = front_end + back_end

print(joined_list)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

joined_list.insert(5, 'Python')
joined_list.insert(6, 'SQL')

full_stack = joined_list
print(full_stack)

# Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[len(ages) -1]

print(min)
print(max)

# 2. Add the min age and the max age again to the list
ages.append(min)
ages.append(max)

print(ages)

# 3. Find the median age (one middle item or two middle items divided by two)
ages.sort()

median_index = int((len(ages) - 1)/2)
median_age = (ages[median_index] + ages[median_index + 1])/2

print(median_age)

# 4. Find the average age (sum of all items divided by their number )
average_age = sum(ages)/len(ages)

print(average_age)

# 5. Find the range of the ages (max minus min)
min = ages[0]
max = ages[len(ages) - 1]
range = max - min

print(range)

# 6. Compare the value of (min - average) and (max - average), use abs() method
print((min - average_age)%(max - average_age))

# 7. Find the middle country(ies) in the countries list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Check if there is a middle 
print(len(countries)%2)

middle_index = int((len(countries) - 1)/2)

middle_country = countries[middle_index]

print(middle_country)

# 8. Divide the countries list into two equal lists if it is even if not one more country for the first half.
list_1 = countries[0:3]
list_2 = countries[3:len(countries)]

print(list_1)
print(list_2)

# 9. Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic = countries

print(first_country)
print(second_country)
print(third_country)
print(scandic)