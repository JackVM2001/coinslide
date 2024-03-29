# coinslide
Jack Van Meter
Cs 120
Game design
3-29-2024


Theme for the game:
 Late night with David letterman. 

Catch or avoid:
Dave will be catching the half dollars as they fall from the curtain of the Ed Sullivan theater. 

Sprites: 
 Dave.png is the name of the sprite that we will use. Coin is the second sprite and is represented by a half dollar coin. 

Diagram:
Elements on the screen are the Dave sprite, and coins. The background image is also part of the scene. The coins are set to a random speed between 3 and 8 pulse a random position. So 10 appear at the top of the screen and fall down at different locations and speeds. Dave moves on an x plane in the scene. He is able to glide and uses wrap to the other side when exits the screen. When the Dave sprite collides with the half dollars a for loop is exited and the half dollar is reset to the top of the screen. In addition to this a sound effect takes place that is called from our GE. The GE is titled simpleGE and is imported over. 

Player sprite:
It is always here and is immediately initialized. It starts at position 320,400 and then is free to move left or right by the arrow keys on that x plain. The speed of Dave is set at 5 pixels. 

Target sprite:
The Coin Sprite initializes at the top of the screen. There are 10 coins that fall at random points and at random speeds as well. When the coin sprite makes contact with the Dave sprite the reset function is executed which sends it back to the top. In addition the sound effect titled random.wav is sounded as well. 


![image](https://github.com/JackVM2001/coinslide/assets/156926086/a08431aa-eca2-4740-910d-9e856f1877c0)
