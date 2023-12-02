file_path = '2/input.txt'
with open(file_path, 'r') as file:
    input_strings = [line.strip() for line in file.readlines()]

number_of_games = len(input_strings)

fulfillment_red = 12
fulfillment_blue = 14
fulfillment_green = 13

red = 'red'
blue = 'blue'
green = 'green'

r = [0]
b = [0]
g = [0]

for id, game in enumerate(input_strings):
    reveals = game.split(':')[1].replace(';', ',').split(',')
    for reveal in reveals:
        amount = reveal.split()[0]
        if red in reveal and r[id] < int(amount):
            r[id] = int(amount)

        elif blue in reveal and b[id] < int(amount):
            b[id] = int(amount)

        elif green in reveal and g[id] < int(amount):
            g[id] = int(amount)

    if number_of_games-1 > id:
      r.append(0)
      b.append(0)
      g.append(0)

set_game_id_red = set([index + 1 for index, element in enumerate(r) if element <= fulfillment_red])
set_game_id_blue = set([index + 1 for index, element in enumerate(b) if element <= fulfillment_blue])
set_game_id_green = set([index + 1 for index, element in enumerate(g) if element <= fulfillment_green])

set_all_games = set(range(1, number_of_games + 1))

possible_games = set_game_id_red & set_game_id_blue & set_game_id_green

print(sum(possible_games))

# part 2
power_list = []

for id in range(number_of_games):
    power_list.append(r[id] * g[id] * b[id])

print(sum(power_list))

