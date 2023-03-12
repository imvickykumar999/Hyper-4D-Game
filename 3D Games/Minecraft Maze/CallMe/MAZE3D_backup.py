
from ursina.prefabs.first_person_controller import FirstPersonController as FPC
from CallMe import MAZE3D_solver as mzs
from CallMe import MAZE3D_generator as mzg
from ursina import *

app = Ursina()
n=10 # initial maze side
c=0  # texture index

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
            # scale=(.5,.5,.5),
            texture=texture,
            highlight_color=color.yellow,
            color=default_color,
        )

p=-2
for k in [0,-30,-50]:
    n+=5
    p+=1

    us_maze = mzg.returnMaze(n,n)
    # print(us_maze) # UNsolved

    s_maze = mzs.solve_maze(us_maze)
    # print(s_maze) # Solved

    y=k
    for z in range(len(s_maze)):
        for x in range(len(s_maze[z])):
            c+=1

            if us_maze[z][x] == 'p':
                Voxel(position=(x,y,z), 
                            texture=opt_texture[c%len(opt_texture)],
                            # texture='ursina_logo',
                            default_color=color.blue,
                            )
            else:
                voxel = Voxel(position=(x,y,z))
                
    y=k+1                          # for lower wall
    # for y in range(k+1,k+3+p):   # for higher wall
    for z in range(len(us_maze)):
        for x in range(len(us_maze[z])):

            if us_maze[z][x] == 'w':
                voxel = Voxel(position=(x,y,z), 
                            texture='brick',
                            # scale=(.5,.5,.5),
                            default_color=color.orange,
                            )

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=100)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, 
                  texture='brick',
                #   scale=(.5,.5,.5),
                  default_color=color.orange,
                  )
    # # removing wall is not allowed.
    # if key == 'right mouse down' and mouse.hovered_entity: 
    #     destroy(mouse.hovered_entity)


window.fullscreen = True
player = FPC(gravity=.07)

def update():
    # print(player.y)

    if (player.x > n-3 and player.z > n-3) or (player.x < 3 and player.z < 3):
        print_on_screen("Jump Down to switch Levels", position=(-.1,0))     

    if player.y > -2:
        print_on_screen("Level 1", position=(0,.1))
    elif player.y > -32:
        print_on_screen("Level 2", position=(0,.2))
    else:
        print_on_screen("Level 3", position=(0,.3))

    if player.y < -51:
        player.y = 30

Sky()
app.run()
