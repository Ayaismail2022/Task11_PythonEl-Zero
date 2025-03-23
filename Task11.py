"""
Task 11
"""
#Task 1
my_nums = [15, 81, 5, 17, 20, 21, 13]

filtered_nums = [num for num in my_nums if num % 5 == 0]

sorted_nums = sorted(filtered_nums, reverse=True)
index = 1
for num in sorted_nums:
    print(f"{index} => {num}")
    index += 1

print("All Numbers Printed")

print("-" * 20)

#Task 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in numbers:
    if num == 6 or num == 8 or num == 12:
        continue
    if num < 10:
        print(str(num).zfill(2))
    else:
        print(num)
    
print("All Numbers Printed")

print("-" * 20)

#Task 3
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total_points = 0

for subject, rank in my_ranks.items():
    if rank == 'A':
        points = 100
    elif rank == 'B':
        points = 80
    elif rank == 'C':
        points = 40
    
    print(f"{subject} => {points} Points")
    total_points += points

print(f"Total Points is {total_points}")
    
    