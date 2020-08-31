import os
import random

class Game:
	def __init__(self):
		self.board = [x[:] for x in [[0] * 4] * 4]
	def printBoard(self):
		#os.system('clear')
		for row in self.board:
			for col in row:
				print(' ' + str(col) + ' ', end='')
			print('')
	def gameLoop(self):
		while True:
			if self.randomTile() == False:
				break
			self.printBoard()
			while True:
				action = self.getAction()
				check = self.checkAction(action)
				print(check)
				if check != False:
					self.takeAction(action)
					break
	def randomTile(self):
		zeroes=[]
		for r in range(4):
			for c in range(4):
				if self.board[r][c] == 0:
					zeroes.append([r,c])
		if len(zeroes) == 0:
			return False

		selection = random.choice(zeroes)
		self.board[selection[0]][selection[1]] = 2 if random.random()<0.9 else 4
		return True

	def slide(self, l, direction): #direction = True for up or left, false for right or down
		if direction == False:
			l.reverse()
		j=0
		while j<16:
			tookAction = False
			idx=0
			while idx<len(l)-1:
				if(l[idx]==0):
					l[idx]=l[idx+1]
					l[idx+1]=0
				idx+=1
			j+=1
		if direction == False:
			l.reverse()
		return l

	def combine(self, l, combineTowardsStart):
		list = self.slide(l, combineTowardsStart)
		if combineTowardsStart == False: #Up or left, start combining from the 4th index
			list.reverse()

		#Check from the	start of the list, combining and then moving on, and then reverse list again if combineTowardsStart
		for i in range(0,3):
			if list[i] == list[i+1]:
				list[i]*=2
				list[i+1]=0
		if combineTowardsStart == False:
			list.reverse()
		list = self.slide(list, combineTowardsStart)
		return list

	def takeAction(self, letter):
		if letter == 'w' or letter == 's':
			for i in range(0,4):
				column=[]
				for c in range(0,4):
					column.append(self.board[c][i])
				column = self.combine(column, True if letter == 'w' else False)
				for c in range(0,4):
					self.board[c][i]=column[c]
		else:
			for r in range(0,4):
				row = self.board[r]
				row = self.combine(row, True if letter == 'a' else False)
				self.board[r]=row

	def getAction(self):
		return input('w, a, s, or d to slide tiles around: ')

	def checkAction(self, letter):
		if letter == 'w':
			#Iterate through every tile, if it can move to the tile above then return the
			testBoard = self.board
			for i in range(1,4):
				for j in range(0,4):
					#Check first 3 rows
					currentSquare = self.board[i][j]
					aboveSquare = self.board[i-1][j]
					if currentSquare==aboveSquare and currentSquare !=0:
						return True
					if aboveSquare == 0:
						return True
					return False
		elif letter == 'd':
			for i in range(0,3):
				for j in range(0,4):
					#Check last 3 rows
					currentSquare = self.board[i][j]
					belowSquare = self.board[i+1][j]
					if currentSquare==belowSquare and currentSquare != 0:
						return True
					if belowSquare == 0:
						return True
					return False
		elif letter == 'a':
			for i in range(0,4):
				for j in range(1,4):
					#Check columns 2-4
					currentSquare = self.board[i][j]
					leftSquare = self.board[i][j-1]
					if currentSquare==leftSquare and currentSquare != 0:
						return True
					if leftSquare == 0:
						return True
					return False
		elif letter == 's':
			for i in range(0,4):
				for j in range(0,3):
					#Check columns 1-3
					currentSquare = self.board[i][j]
					rightSquare = self.board[i][j-1]
					if currentSquare==rightSquare and currentSquare != 0:
						return True
					if rightSquare == 0:
						return True
					return False
		else:
			return False

def test():
	g = Game()
	g.gameLoop()

if __name__ == '__main__':
	test()
