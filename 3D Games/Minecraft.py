
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
c=0
opt_texture = [
    'arrow_down',
    'arrow_right',
    'brick',
    'circle',
    'circle_outlined',
    'cobblestone',
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

class Voxel(Button):
    def __init__(self, position=(0,0,0), 
                 texture='grass',
                 default_color=color.green,
                 ):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            highlight_color=color.red,
            color=default_color,
        )

for y in range(0,101,50):
    for z in range(12):
        for x in range(12):
            voxel = Voxel(position=(x,y,z))

def input(key):
    global c
    c+=1

    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=100)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, 
                  texture='brick',
                  default_color=color.orange,
                #   texture=opt_texture[c%len(opt_texture)],
                #   default_color=color.random_color(),
                  )
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)


window.fullscreen = 1
player = FirstPersonController(gravity=.6)

# https://stackoverflow.com/a/75692459/11493297
def update():
    print('Player is at Height = ', player.y)

    if player.y < -10:
        player.y = 110   # No infinite falling.

# player = FirstPersonController(
                    # model='sphere', 
                    # texture='white_cube',
                    # color=color.blue,
                    # origin = (0, -1, -2),
                    # )

# skybox_image = load_texture("sunset.jpg")
# sky = Sky(texture=skybox_image)

Sky()
app.run()
