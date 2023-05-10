
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
t = time.time()
window.fullscreen = True

player = FirstPersonController(collider='box')
player.gravity = 10e-2

player.x = 1
player.y = 3
player.z = 3

ball = Entity(
    scale=.5,
    collider='box',
    model='sphere',
    color=color.red,
    position=(5,2,110),
    texture='reflection_map_3',
)

box_1 = Entity( 
    model='cube',
    scale=(2,4,2),
    collider='box',
    color=color.white,
    position=(8,2,110), 
    texture='static/wall.png',
)

box_2 = duplicate(box_1, x=-8)
cont = True
dx=.1

mario  = Audio('static/super-mario-bros.mp3',  loop = True,  autoplay = True)
fall   = Audio('static/Super Mario Death.mp3', loop = False, autoplay = False)
winner = Audio('static/Super Mario Won.mp3',   loop = True,  autoplay = False)

class Voxel(Button):
    def __init__(
        self, position=(0,0,0),
        color=color.white,
        texture='static/wall.png'
        ):
        
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color,
            highlight_color=color,
            )

for y in range(3,-1,-1):
    for z in range(y, 100, 12):
        for x in range(3):
            Voxel(position=(x,y,z))

for y in range(4):
    for z in range(y+110, 216, 13):
        Voxel(position=(1,y,z))

def update():
    global deatils, player, won, cont, dx
    tc = time.time()

    if (player.z < 212 and player.y < -2) or (tc - t > 100) or (str(player.intersects().entity) == 'entity'):
        won.text = 'You Lost'
        won.color = color.red

        mario.pause()
        if cont:
            cont = False
            fall.play()
        
    if player.z > 212 and player.y > -1:
        won.text = 'You Won'

        mario.pause()
        if cont:
            cont = False
            winner.play()
        
    deatils.text = f'''
    Score = {int(player.z)}
    Time left = {int(100 - (tc - t))} sec.
    '''

    ball.x += dx # to move ball side-wise
    # ball.z = box_1.z = box_2.z = int(player.z) # to move ball forward

    ball.rotation_x += time.dt*100
    ball.rotation_y += time.dt*100
    ball.rotation_z += time.dt*100

    if ball.intersects().hit:
        dx =- dx # bounce back

def input(key):
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

deatils = Text(
    origin=(.1, -4),
	font='VeraMono.ttf', 
	color=color.white,
	) 

won = Text(
    origin=(0,-4),
	color=color.green,
	) 

skybox_image = load_texture("static/space.png")
sky = Sky(texture=skybox_image)
# Sky()
app.run()
