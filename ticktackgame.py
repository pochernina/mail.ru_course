'''
task 1 in backend mail.ru
'''
import numpy as np

class TicTacGame:
	'''
	the game of tic-tac-toe 5 by 5
	wins the one who first placed 4 crosses or noughts next to each other
	'''
	def __init__(self):
		self.board = np.reshape(np.arange(1, 26).astype('str'), (5, 5))
		self.count = 0
		self.name1 = ''
		self.name2 = ''
		self.player = ''

	def show_board(self):
		'''
		prints board
		'''
		dashes = '—' * (5 * 3 + 6)
		print(dashes)
		for i in range(5):
			print('|', end="")
			for j in range(5):
				if self.board[i][j] == 'X':
					print(f'\033[1m\033[32m {self.board[i][j]}', end='')
					print(f'\033[0m {"|"}', end='')
				elif self.board[i][j] == 'O':
					print(f'\033[1m\033[34m {self.board[i][j]}', end='')
					print(f'\033[0m {"|"}', end='')
				else:
					print(self.board[i][j].center(3) + '|', end="")
			print()
			print(dashes)

	def next_move(self):
		'''
		replaces the field cell
		'''
		valid = False
		self.player = self.name1 if self.player == self.name2 else self.name2
		print('Твой ход, ' + self.player)
		while not valid:
			player_answer = input('Введите число от 1 до 25: ')
			try:
				player_answer = validate_answer(player_answer)
			except ValueError:
				print('Некорректный ввод.')
				continue
			i = (player_answer - 1) // 5
			j = (player_answer - 1) % 5
			try:
				assert self.board[i][j] == str(player_answer)
			except AssertionError:
				print('Ячейка уже занята!')
				continue
			if self.player == self.name1:
				self.board[i][j] = 'X'
			else:
				self.board[i][j] = 'O'
			valid = True
			self.count += 1

	def check_winner(self):
		'''
		checks if someone has won
		'''
		no_winner = True
		for i in range(5):
			if (self.board[i][0] == self.board[i][1] == self.board[i][2] == self.board[i][3] or
			self.board[i][1] == self.board[i][2] == self.board[i][3] == self.board[i][4] or
			self.board[0][i] == self.board[1][i] == self.board[2][i] == self.board[3][i] or
			self.board[1][i] == self.board[2][i] == self.board[3][i] == self.board[4][i]):
				no_winner = False
		all_coords = (((0,0), (1,1), (2,2), (3,3)), ((1,1), (2,2), (3,3), (4,4)),
		((1,0), (2,1), (3,2), (4,3)), ((0,1), (1,2), (2,3), (3,4)),
		((0,4), (1,3), (2,2), (3,1)), ((1,3), (2,2), (3,1), (4,0)),
		((1,4), (2,3), (3,2), (4,1)), ((0,3), (1,2), (2,1), (3,0)))
		for coords in all_coords:
			if (self.board[coords[0][0]][coords[0][1]] == self.board[coords[1][0]][coords[1][1]] ==
			self.board[coords[2][0]][coords[2][1]] == self.board[coords[3][0]][coords[3][1]]):
				no_winner = False
		if not no_winner:
			self.show_board()
			print(self.player + ' выиграл(а)!')
			return True
		return False

	def valid_name(self, number):
		'''
		checks if name is valid
		number - number of player
		'''
		name_not_valid = True
		while name_not_valid:
			try:
				name = input('Имя игрока ' + number + ': ')
				if validate_name(name):
					if int(number) == 1:
						self.name1 = name
					else:
						self.name2 = name
					name_not_valid = False
			except ValueError:
				print('Некорректное имя.')
				continue

	def start_game(self):
		'''
		the algorithm of the game
		'''
		self.valid_name('1')
		self.valid_name('2')
		self.player = self.name2

		while (not self.check_winner() and self.count != 25):
			self.show_board()
			self.next_move()
		if self.count == 25:
			self.show_board()
			print('Ничья!')

def validate_name(name):
	'''
	checks that the name contains only letters
	'''
	if name.isalpha():
		return True
	raise ValueError

def validate_answer(answer):
	'''
	checks that answer is correct
	'''
	answer = int(answer)
	if (answer < 1 or answer > 25):
		raise ValueError
	return answer

if __name__ == '__main__':
	game = TicTacGame()
	game.start_game()
