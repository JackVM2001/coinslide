#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:41:51 2024

@author: carlgroundstine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Mar 29 09:06:03 2024

@author: carlgroundstine
"""

import pygame, simpleGE, random

class Coin(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("halfdollar.png") 
        self.setSize(25,25)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0,self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
            
            
        

class Dave(simpleGE.Sprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("david-removebg-preview.png")
        self.setSize(50,50)
        self.position = (320,400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -=self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x +=self.moveSpeed
            
class LblScore(simpleGE.Label):
     def __init__(self):
         super().__init__()
         self.text = "Score: 0"
         self.center = (100,30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500,30)
        
        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("backgroundimage.png")
        self.sndCoin = simpleGE.Sound("random.wav")
        self.numCoins = 10
        
        self.score = 0
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.LblTime =LblTime()
        self.LblScore = LblScore()
        
        self.dave = Dave(self)
        #self.coin = Coin(self)
        self.coins =[]
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        self.sprites = [self.dave,
                        self.coins,
                        self.LblScore,
                        self.LblTime]
        
    
    
    def process(self):
        for coin in self.coins:
            if coin.collidesWith(self.dave):
                coin.reset()
                self.sndCoin.play()
                self.score += 1
                self.LblScore.text = f"Score:{self.score}"
                
        self.LblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print (f"Score: {self.score}")
            self.stop()
                
class Instructions(simpleGE.Scene):
    def __init__(self,prevScore):
         super().__init__()
         
         self.prevScore = prevScore
         
         
         self.setImage("backgroundimage.png")
         self.responce = "Quit"
         #self.prevScore = 0
         
         
         
         self.directions = simpleGE.MultiLabel()
         self.directions.textLines = [
         "You are the head of David Letterman",
         "To move use the arrow keys",
         "Colect a lot of coins",
         "You only have 10 seconds",
         "",
         "Good luck soldier"]
         
         self.directions.center = (320,200)
         self.directions.size = (500,250)
         
         self.btnPlay = simpleGE.Button()
         self.btnPlay.text = "Play"
         self.btnPlay.center = (100,400)
         
         self.btnQuit = simpleGE.Button()
         self.btnQuit.text = "Quit"
         self.btnQuit.center = (540,400)
         
         self.lblScore = simpleGE.Label()
         self.lblScore.text = "Last Attempt: 0"
         self.lblScore.center = (320, 400)
         
         
         
         self.sprites = [self.directions,
                         self.btnPlay,
                         self.btnQuit,
                         self.lblScore]
     
        
    #def setPrevScore(self, prevScore):
        #self.prevScore = prevScore
         self.lblScore.text = f"Last Try: {self.prevScore}"
        
    def process(self):
        if self.btnPlay.clicked:
            self.responce = "Play"
            self.stop()
            
        if self.btnQuit.clicked:
            self.responce = "Quit"
            self.stop()
            
            
   
        
         
         
       
        
def main():
    
    keepGoing = True
    lastScore = 0
    while keepGoing: 
        #lastScore = 0
        instructions = Instructions(lastScore)
        #instructions.setPrevScore(lastScore)
        instructions.start()
        
        if instructions.responce == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else: 
            keepGoing = False
        
            
            
        
    
if __name__== "__main__":
    main()
     
    
    