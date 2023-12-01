file_path = '1/input-day1-2.txt'
with open(file_path, 'r') as file:
    input_strings = [line.strip() for line in file.readlines()]

list_ = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','1', '2', '3', '4', '5', '6','7','8','9']
res = 0
extracted_words = []

for x in input_strings: 
  for i in range(len(x)):
    for j in range(i+1, len(x)+1):
        substring = x[i:j]
        if substring in list_:
            extracted_words.append(substring)            
  firstDigit = list_.index(extracted_words[0])+1 if not extracted_words[0].isdigit() else extracted_words[0]
  lastDigit = list_.index(extracted_words[-1])+1 if not extracted_words[-1].isdigit() else extracted_words[-1]
  res += (int(str(firstDigit) + str(lastDigit)))
  extracted_words = []
print(res)