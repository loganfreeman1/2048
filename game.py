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

	def takeAction(self, letter):
		if letter == 'w':
			for i in range(0,4):
				column = []
				for l in self.board:
					column.append(l[i]) #Now the column == a 'row', with index 0 corresponding to row zero
				print('Column: ' + str(column))
				idx = 0 #Start from the top of the column, since we are going up
				shift = 0
				n=0
				for j in range(0,4): #Don't need to check top index
					n=j
					if column[j]==0:
						shift+=1
						continue
					if shift>0:
						column[j-shift]=column[j]
						n=j-shift
						column[j]=0
						shift=0

					if n-1>-1 and column[n-1]==column[n]: #Up-shifted to touching now
						shift+=1
						column[n-1]*=2
						column[n]=0
						n-=1
				for k in range(4):
					self.board[k][i]=column[k]
		elif letter == 's':
			pass
		elif letter == 'a':
			pass
		elif letter == 'd':
			pass

	def getAction(self):
		return input('w, a, s, or d to slide tiles around: ')

	def checkAction(self, letter):
		if letter == 'w':
			#Iterate through every tile, if it can move to the tile above then return the
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
