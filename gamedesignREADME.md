# coinslide
Jack Van Meter
Cs 120
Game design
4-5-2024


Theme for the game:
 Late night with David letterman. 

Catch or avoid:
Dave will be catching the half dollars as they fall from the curtain of the Ed Sullivan theater. 

Sprites: 
 Dave.png is the name of the sprite that we will use. 
 Coin is the second sprite and is represented by a half dollar coin. 
Label Sprites:
  Self.directions, which is is text that serves s a welcome screen
  Self.btnPlay, which is the play button. plays the game in the loop
  Self.btnQuit, which is the quit button which exits the game via keepgoing = false
  Self.btnlblScore, which shows the previous games high score
  Self.LblScore, which has acts as a running score count while game play is underway
  Self.LblTime, Is a count down clock that is displayed. 
  

Diagram:
Elements on the screen are the Dave sprite,coins, and the varius lables. The background image is also part of the scene. The first scene displays a menue. On the menue are the choices play and quit. As well as the directions how to play the game. If the user chooses play the game will initiate. If quit is choosen the game closes out. Quiting the game can be done by clicking quit or the red x. When playing a countdown timer appears displaying 10 seconds. You are to collect as many coins in 10 seconds as the lable will keep track of your progress. The coins are set to a random speed between 3 and 8 pulse a random position. So 10 appear at the top of the screen and fall down at different locations and speeds. Dave moves on an x plane in the scene. He is able to glide and uses wrap to the other side when exits the screen. When the Dave sprite collides with the half dollars a for loop is exited and the half dollar is reset to the top of the screen. In addition to this a sound effect takes place that is called from our GE. After the 10 seonds also the menue apears again showing your score and again displayig your options to play or quit. The GE is titled simpleGE and is imported over. 

Player sprite:
It is always here and is immediately initialized. It starts at position 320,400 and then is free to move left or right by the arrow keys on that x plain. The speed of Dave is set at 5 pixels. 

Target sprite:
The Coin Sprite initializes at the top of the screen. There are 10 coins that fall at random points and at random speeds as well. When the coin sprite makes contact with the Dave sprite the reset function is executed which sends it back to the top. In addition the sound effect titled random.wav is sounded as well. 

Lable Sprites:
The lable sprites initiate when run is selected. So they are there from the begining. 


self.directions is initiated off the bat and prints text to show the user how to play the game. they are centered at 320,200 and have a size of 500,250.

self.btnPlay is the play button for the game. It is centered at 100,400 and is only run if the button is clicked. If clicked play game is initiated and the game stays in the while loop

self.btnQuit is the quit button or exit for the game. When pressed keep going is set to false and the game is exited. It is centered at 540,400.

Self.btnlblScore is the lable that displays your score from the last game. At the end of the game it is displayed in the center of the screen (320,400) as well as the play and quit buttons.

self.LlbScore is the running total during the game. It is initiated when play is selected and tracks the dave sprite as it collects coins. this lable is centered at 100,30

self.LblTime is the running countdown clock. The clock starts at 10 seconds and at the end the game quits. Only 2 decimal places are shown from the imported timer from simpleGE. The clock is centered at 500,30







![image](https://github.com/JackVM2001/coinslide/assets/156926086/a08431aa-eca2-4740-910d-9e856f1877c0)
