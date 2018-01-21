import  pyglet
import random

window = pyglet.window.Window(width=800, height=600, caption="Kill the dragon game")
dragon = pyglet.image.load("dragon.png")

dragon_x1 = random.randint(0, window.width-dragon.width)
dragon_y1 = random.randint(0, window.width-dragon.width)

dragon.anchor_x = dragon.width/2
dragon.anchor_y = dragon.height/2

dragon_x = 100
dragon_y = 100

@window.event
def on_mouse_press(x, y, button, modifier):
    
    mouse_x_in_image_area = x>=(dragon_x - dragon.width/2) and x <= (dragon_x + dragon.width/2)
    mouse_y_in_image_area = y>=(dragon_y - dragon.height/2) and y <= (dragon_y + dragon.height/2)

    if button ==  pyglet.window.mouse.LEFT and mouse_x_in_image_area and mouse_y_in_image_area :
        print "dragon mar gya"
    else:
        print "dragon jeet gya"   

@window.event
def on_draw():
   
    dragon.blit(dragon_x, dragon_y)

pyglet.app.run()




