# Question 1: OSKI STOLE YOUR POWER
def computePower(x,y):
    result = 1
    if y < 0:
        x = 1/x
        y = -y
    while y > 0:
        if y % 2 == 1:
            result *=x
        x *= x
        y //= 2
    return result
x = 2
y = 3
print(computePower(x,y))


# Question 2: WHAT SHOULD I WEAR?
def temperatureRange(readings):
    return(min(readings), max(readings))
readings = [15,14,17,20,23,28,20]
print(temperatureRange(readings))


# Question 3: CHECK IF ITS THE WEEKEND
def isWeekend(day):
    # Check if the day represents a weekend (6 = Saturday, 7 = Sunday)
    if day in [6, 7]:
        return True
    else:
        return False
day = 6
print(isWeekend(day))


# Question 4: FUEL EFFICIENCY CALCULATOR
def fuel_efficiency(distance, fuel):
    return round(distance/fuel, 2)
distance = 70
fuel = 21.5
print(fuel_efficiency(distance, fuel))


# Question 5: SECRET CODE
def decodeNumbers(n):
    last_digit = n % 10
    remaining_number = n // 10
    multiplier = 1
    while remaining_number >= multiplier:
        multiplier *=10
    result = last_digit * multiplier + remaining_number
    return result
n = 12345
print(decodeNumbers(n))


# Question 6: MIN & MAX BUT WITH LOOPS
# 6.1 FOR LOOPS
def find_min_with_for_loop(nums):
    current_num = nums[0]
    for num in nums:
        if num < current_num:
            current_num = num
    return current_num

def find_max_with_for_loops(nums):
    current_num = nums[0]
    # Iterate through the list
    for num in nums:
        # Update the maximum if a larger value is found
        if num > current_num:
            current_num = num
    return current_num
nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  
print(find_max_with_for_loops(nums)) 


# 6.2 WHILE LOOPS
def find_min_with_while_loop(nums):
    current_num = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] < current_num:
            current_num = nums[index]
        index += 1
    return current_num

def find_max_with_while_loops(nums):
    current_num = nums[0]
    index = 1
    while index < len(nums):
        if nums[index] > current_num:
            current_num = nums[index]
        index += 1
    return current_num
nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  
print(find_max_with_for_loops(nums)) 


# Question 7: COUNTING VOWELS
def vowel_and_consonant_count(text):
    vowels = set("aeiouAEIOU") 
    num_vowels = 0
    num_consonants = 0
    for char in text:
        if char.isalpha():  
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return (num_vowels, num_consonants)
text = "UC Berkeley, founded in 1868!"
print(vowel_and_consonant_count(text)) 


# Question 8: CALCULATE DIGITAL ROOT
def digital_root(num):
    sum_of_digits = 0
    while num > 0:
        sum_of_digits += num % 10  
        num //= 10  
    return sum_of_digits
num = 2468
result = digital_root(num)
print(result)
