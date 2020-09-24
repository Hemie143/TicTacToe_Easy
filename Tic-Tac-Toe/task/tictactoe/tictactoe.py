
print('Enter cells: ')
grid_input = input()
# print('X O O\n X X O \nO X X')

print('--------')
print(f'| {" ".join(grid_input[:3])  } |')
print(f'| {" ".join(grid_input[3:6])  } |')
print(f'| {" ".join(grid_input[6:])  } |')
print('---------')
