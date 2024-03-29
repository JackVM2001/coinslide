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
            



class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("backgroundimage.png")
        self.sndCoin = simpleGE.Sound("random.wav")
        self.numCoins = 10
        self.dave = Dave(self)
        #self.coin = Coin(self)
        self.coins =[]
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
        self.sprites = [self.dave,
                        self.coins]
    
    
    def process(self):
        for coin in self.coins:
            if coin.collidesWith(self.dave):
                coin.reset()
                self.sndCoin.play()
            
        
       
        
def main():
    game = Game()
    game.start()
    
if __name__== "__main__":
    main()
     
    
    
