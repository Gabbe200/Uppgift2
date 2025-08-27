from collections import Counter
import os

os.system('cls')

most_common_numbers = Counter([1, 5, 6, 5, 3, 1, 2, 5]).most_common(2)
print(most_common_numbers)
# -> [(5, 3), (1, 2)]

print("mest vanlig", most_common[0])
