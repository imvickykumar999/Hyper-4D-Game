
import sys
from ursina import *
import fetch_commit as fc
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
t = time.time()
c=0

opt_texture = [
    'arrow_down',
    'arrow_right',
    'brick',
    'circle',
    'circle_outlined',
    # 'cobblestone',
    'cursor',
    'file_icon',
    'folder',
    'grass',
    'heightmap_1',
    'horizontal_gradient',
    'noise',
    'radial_gradient',
    'reflection_map_3',
    'shore',
    'sky_default',
    'sky_sunset',
    'ursina_logo',
    'ursina_wink_0000',
    'ursina_wink_0001',
    'vertical_gradient',
    'white_cube',
]

mario  = Audio('static/super-mario-bros.mp3',  loop = True,  autoplay = True)
fall   = Audio('static/Super Mario Death.mp3', loop = False, autoplay = False)
winner = Audio('static/Super Mario Won.mp3',   loop = True,  autoplay = False)
cont = True

class Voxel(Button):
    def __init__(self, position=(0,0,0), 
                 texture=opt_texture[-1],
                 default_color=color.green,
                 ):
        
        super().__init__(
            parent=scene,
            position=position,
            collider='box',
            model='cube',
            origin_y=.5,
            texture=texture,
            highlight_color=color.red,
            color=default_color,
        )

try:
    username = sys.argv[1]
except:
    username = 'imvickykumar999'

plain = fc.commit_history(username)
# print(plain)

for i in plain:
    for y in range(plain[i][0]):
        Voxel(position=(i%7, y, i//7))

def input(key):
    hit_info = raycast(camera.world_position, camera.forward, distance=200)
    global c
    c+=1

    if key == 'left mouse down':
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, 

                # texture=opt_texture[c%len(opt_texture)],
                # default_color=color.random_color(),                  
                  
                  texture='brick',
                  default_color=color.orange,
                )
            
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

    try:
        if key == 'e': # teleporting at center of screen
            player.x = hit_info.entity.position.x
            player.y = hit_info.entity.position.y
            player.z = hit_info.entity.position.z
    except:
        pass

    if key == 'f': # press f for anti-gravity
        player.gravity *= -1

window.fullscreen = 1
player = FirstPersonController(collider='box')

player.gravity = 10e-2
player.x = 1
player.y = 200
player.z = 1

def update():
    global deatils, player, won, cont
    tc = time.time()
    
    if player.y < -10: # respawn
        player.y = 100

    if (player.y < -5) or (tc - t > 100):
        won.text = 'You Lost'
        won.color = color.red

        mario.pause()
        if cont:
            cont = False
            fall.play()
        
    if player.z > 50 and player.y > -1:
        won.text = 'You Won'

        mario.pause()
        if cont:
            cont = False
            winner.play()
        
    deatils.text = f'''
    Coordinates(X,Y,Z) = {(int(player.x), int(player.y +1), int(player.z))}
    Time left = {int(60 - (tc - t))} sec.
    '''

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

# username = sys.argv[1]
# python minecraft.py JeffersonRPM
