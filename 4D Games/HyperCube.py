
from ursina import *
from random import randint

app = Ursina()

def input(key):
    if held_keys['z']:
        cube.scale += (.1,.1,.1)
    if held_keys['x']:
        cube.scale -= (.1,.1,.1)

    if key == 'c':
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        cube.color = color.rgb(red, green, blue)

def update():
    global speed

    if held_keys['t']:
        speed += 1
    if held_keys['g']:
        speed -= 1

    if held_keys['d']:
        cube.x += time.dt
    if held_keys['w']:
        cube.y += time.dt
    if held_keys['a']:
        cube.x -= time.dt
    if held_keys['s']:
        cube.y -= time.dt

    if held_keys['r']:
        cube.z += time.dt*20
    if held_keys['f']:
        cube.z -= time.dt*20

    if held_keys['q']:
        cube.rotation_y -= time.dt*speed
    if held_keys['e']:
        cube.rotation_z -= time.dt*speed
    if held_keys['v']:
        cube.rotation_x -= time.dt*speed

    camera.position = (5,0,-30)

cube = Entity(model='cube',
              color=color.orange,
              texture='brick',
              scale=4,
              )

speed=100

instructions = f'''
    Instructions ...
--------------------------

Camera Angle is at Z = -30

Hold x to decrease scale (4D)
Hold z to increase scale (4D)

Hold v to rotate in x axis
Hold q to rotate in y axis
Hold e to rotate in z axis

Hold w to move up
Hold s to move down
Hold a to move left
Hold d to move right

Hold r to move ahead
Hold f to move back

Press c to change color
Hold t to change spin speed clockwise
Hold g to change spin speed anti-clockwise
'''

text = Text(instructions, 
            origin=(-.5, 0),
            font='VeraMono.ttf', 
            color=color.blue,
            resolution=100*Text.size,
            ) 

Sky()
window.fullscreen = 1
app.run()