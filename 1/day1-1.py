file_path = '1/input-day1-1.txt'
with open(file_path, 'r') as file:
    input_strings = [line.strip() for line in file.readlines()]

res = 0
for x in input_strings:
  digits = [int(i) for i in x if i.isdigit()]
  res += int((str(digits[0]) + str(digits[-1])))
print(res)