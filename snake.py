# -*- coding: utf-8 -*-
# Snake game made by Raouf Tamssaout

from __future__ import unicode_literals
import pygame as pg
import random, time


class Snake():
	def __init__(self):
		self.position = [100,50]
		self.body = [[100,50],[90,50],[80,50]]
		self.direction = "RIGHT"
		self.changeDirectionTo = self.direction

	def changeDirTo(self,dir):
		if dir == "RIGHT" and not dir == "LEFT":
			self.direction = "RIGHT"
		if dir == "LEFT" and not dir == "RIGHT":
			self.direction = "LEFT"
		if dir == "UP" and not dir == "DOWN":
			self.direction = "UP"
		if dir == "DOWN" and not dir == "UP":
			self.direction = "DOWN"

	def move(self,foodpos):
		if self.direction == "RIGHT":
			self.position[0] += 10
		if self.direction == "LEFT":
			self.position[0] -= 10
		if self.direction == "UP":
			self.position[1] -= 10
		if self.direction == "DOWN":
			self.position[1] += 10

		self.body.insert(0,list(self.position))
		if self.position == foodpos:
			return 1
		else :
			self.body.pop()
			return 0


	def checkCollision(self):
		if self.position[0] > 790 or self.position[0] < 0 :
			return 1
		elif self.position[1] > 490 or self.position[1]<0:
			return 1
		for bodypart in self.body[1:]:
			if self.position == bodypart :
				return 1
		return 0

	def getHeadPos(self):
		return self.position

	def getBody(self):
		return self.body


class Foodgenerator():
	def __init__(self):
		self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
		self.isFoodOnScreen = True

	def generateFood(self):
		if self.isFoodOnScreen == False:
			self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
			self.isFoodOnScreen = True
		return self.position

	def setFoodOnScreen(self,b):
		self.isFoodOnScreen = b



width = 800
height = 500


Display = pg.display.set_mode((width,height))
fps = pg.time.Clock()
score=0

snake = Snake()
foodgenerator = Foodgenerator()

def gameOver():
	pg.quit()


while True:
	pg.display.set_caption("Game over | Score: " + str(score))
	for event in pg.event.get():
		if event.type == pg.quit:
			gameOver()
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT and snake.direction != "LEFT":
				snake.changeDirTo('RIGHT')
			if event.key == pg.K_LEFT and snake.direction != "RIGHT":
				snake.changeDirTo('LEFT')
			if event.key == pg.K_UP and snake.direction != "DOWN":
				snake.changeDirTo('UP')
			if event.key == pg.K_DOWN and snake.direction != "UP":
				snake.changeDirTo('DOWN')
	foodPos = foodgenerator.generateFood()
	if snake.move(foodPos)==1:
		score += 1
		foodgenerator.setFoodOnScreen(False)


	Display.fill(pg.Color(0,0,0))

	for pos in snake.getBody():
		pg.draw.rect(Display,pg.Color(225,225,225),pg.Rect(pos[0],pos[1],10,10))

	pg.draw.rect(Display,pg.Color(225,0,0),pg.Rect(foodPos[0],foodPos[1],10,10))

	if snake.checkCollision()==1:
		gameOver()

	pg.display.flip()
	fps.tick(30)
