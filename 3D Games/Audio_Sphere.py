
from ursina import *
from random import randint
import time
import librosa
import os

filename = 'input/Dior.mp3'
# https://youtu.be/S0nOYs0PRak

y, sr = librosa.load(filename)
t1 = int(time.time())
i=0

app = Ursina()
camera.position = (5,0,-30)
# os.startfile(filename)

c=0
opt_texture = [
    'sky_default',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
]

def update():
    global speed, deatils, cube, c, i
    t2 = int(time.time())
    cube.texture = opt_texture[t2%len(opt_texture)]
    # cube.texture = opt_texture[5]

    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    cube.color = color.rgb(red, green, blue)
    
    deatils.text = f'''
>>> Details ...
-----------------------------

Time = {(t2-t1)//60} min {(t2-t1)%60} sec
Texture = {str(cube.texture).split('.')[0]}
Speed = {speed}

Coordinate W = {cube.scale}
Radius     R = {sqrt((cube.scale.x)**2 + (cube.scale.y)**2 + (cube.scale.z)**2)}

Rotation   X = {cube.rotation_x}
Rotation   Y = {cube.rotation_y}
Rotation   Z = {cube.rotation_z}






>>> Instruction ...
----------------------------

Press and Hold `W` or `S` key ...
    ... to adjust Sphere size.

Press and Hold `A` or `D` key ...
    ... to adjust Sphere speed.
'''

    try:
        print(i, sr, y[i], t2-t1)
        cube.scale += (y[i],y[i],y[i])
        i+=int(sr/45)
    except:
        pass

    if cube.scale.x > 10:
        cube.scale = (5,5,5)

    if held_keys['w']:
        cube.scale += (1,1,1)
    if held_keys['s']:
        cube.scale -= (1,1,1)

    if held_keys['d']:
        speed += 5.0
    if held_keys['a']:
        speed -= 5.0

    cube.rotation_x -= time.dt*speed
    cube.rotation_y -= time.dt*speed
    cube.rotation_z -= time.dt*speed

speed=220.0
cube = Entity(model='sphere',
              color=color.red,
              texture='sky_sunset',
              origin=(.1,.2,.1),
              scale=6,
              )

deatils = Text(origin=(-.6, -.07),
                font='VeraMono.ttf', 
                color=color.red,
                ) 

Sky()
window.fullscreen = 1
app.run()