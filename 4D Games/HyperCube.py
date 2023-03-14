
from ursina import *
from random import randint
import time

app = Ursina()
camera.position = (5,0,-30)

c=0
opt_texture = [
    'sky_default',
    'circle_outlined',
    'brick',
    'grass',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
    'radial_gradient',
    'reflection_map_3',
    'shore',
    'sky_sunset',
    'ursina_logo',
    'ursina_wink_0000',
    'ursina_wink_0001',
    'vertical_gradient',
    'white_cube',
]

def input(key):
    global c

    if key == 'c':
        red = randint(0,255)
        green = randint(0,255)
        blue = randint(0,255)
        cube.color = color.rgb(red, green, blue)

    if key == 'space':
        c+=1


def update():
    global speed, deatils, cube, c
    cube.texture = opt_texture[c%len(opt_texture)]

    deatils.text = f'''
>>> Details ...
-----------------------------
Unix Time = {int(time.time())}
Texture = {str(cube.texture).split('.')[0]}
Speed = {speed}

Coordinate X = {cube.x}
Coordinate Y = {cube.y}
Coordinate Z = {cube.z}
Coordinate W = {cube.scale}

Rotation   X = {cube.rotation_x}
Rotation   Y = {cube.rotation_y}
Rotation   Z = {cube.rotation_z}
'''

    if held_keys['o']:
        cube.scale += (.1,.1,.1)
    if held_keys['p']:
        cube.scale -= (.1,.1,.1)

    if held_keys['e']:
        speed += 5.0
    if held_keys['q']:
        speed -= 5.0

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

    if held_keys['j']:
        cube.rotation_x -= time.dt*speed
    if held_keys['u']:
        cube.rotation_y -= time.dt*speed
    if held_keys['m']:
        cube.rotation_z -= time.dt*speed

    if held_keys['l']:
        cube.rotation_x += time.dt*speed
    if held_keys['i']:
        cube.rotation_y += time.dt*speed
    if held_keys['k']:
        cube.rotation_z += time.dt*speed

speed=100.0
cube = Entity(model='cube',
              color=color.violet,
              texture='sky_sunset',
              scale=4,
              )

instructions = '''
>>> Instructions ...
--------------------------
Camera Angle is at `Z` = -30
Hold  `O` to Increase scale (4D)
Hold  `P` to Decrease scale (4D)

Hold  `L` to Rotate in X axis
Hold  `I` to Rotate in Y axis
Hold  `K` to Rotate in Z axis

Hold  `J` to Anit-Rotate in X axis
Hold  `U` to Anit-Rotate in Y axis
Hold  `M` to Anit-Rotate in Z axis

Hold  `W` to move Up
Hold  `S` to move Down
Hold  `A` to move Left
Hold  `D` to move Right

Hold  `R` to move Ahead
Hold  `F` to move Back
Press `C` to change Color
Press `Space` to change Texture

Hold  `E` to change Spin Speed Clockwise
Hold  `Q` to change Spin Speed Anti-Clockwise
'''

Text(
instructions, 
scale=.8,
origin=(-.5, .4),
font='VeraMono.ttf', 
color=color.blue,
) 

deatils = Text(origin=(-.6, -.7),
                font='VeraMono.ttf', 
                color=color.red,
                ) 

Sky()
window.fullscreen = 1
app.run()