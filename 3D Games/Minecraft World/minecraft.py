
import json, time, sys
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


try:
	data = sys.argv[1]
except:
	data = 'home'

try:
	sky = sys.argv[2]
except:
	sky = 'night'


path = f"worlds/{data}.json"
with open(path) as f:
   obj = json.load(f)

app = Ursina()
len_pos = len(obj['position'])
t = time.time()

sky_texture   = load_texture(f'assets/{sky}.png')
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
arm_texture   = load_texture('assets/arm_texture.png')

punch_sound   = Audio('assets/punch_sound', loop = False, autoplay = False)
block_pick = 1


window.fps_counter.enabled = False
window.exit_button.visible = False
window.fullscreen = True


def update():
	global block_pick, deatils

	if player.y < -5:
		player.y = 75 # jump off the boundry 

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if held_keys['1']: block_pick = 1
	if held_keys['2']: block_pick = 2
	if held_keys['3']: block_pick = 3
	if held_keys['4']: block_pick = 4

	deatils.text = f'''
		Time Spent = {int(time.time() - t)} sec.
		Coordinate X = {player.x}
		Coordinate Y = {player.y}
		Coordinate Z = {player.z}
	'''

class Voxel(Button):
	def __init__(self, position = (0,0,0), texture = grass_texture):
		super().__init__(
			parent = scene,
			position = position,
			model = 'assets/block',
			origin_y = 0.5,
			texture = texture,
			color = color.color(0,0,random.uniform(0.9,1)),
			scale = 0.5)


	def input(self, key):
		if self.hovered:
			save_new = self.position + mouse.normal

			if block_pick == 1: 
				texture = grass_texture
			if block_pick == 2: 
				texture = stone_texture
			if block_pick == 3: 
				texture = brick_texture
			if block_pick == 4: 
				texture = dirt_texture
			
			if key == 'left mouse down':
				punch_sound.play()
				box = {str(texture) : list(save_new)}
				# print('------Appended-------', box)
				
				voxel = Voxel(position = save_new, texture = texture)
				obj["position"].append(box)

			if key == 'right mouse down':
				punch_sound.play()
				box = {str(self.texture) : list(self.position)}
				# print('------Removed-------', box)

				obj["position"].remove(box)
				destroy(self)

			with open(path,"w+") as of:
				json.dump(obj, of)


class Sky(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'sphere',
			texture = sky_texture,
			scale = 150,
			double_sided = True)


class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'assets/arm',
			texture = arm_texture,
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.4,-0.6))

	def active(self):
		self.position = Vec2(0.3,-0.5)

	def passive(self):
		self.position = Vec2(0.4,-0.6)


for i in obj['position']:
	texture = load_texture(f'assets/{list(i.keys())[0]}')
	save_new = Vec3(tuple(list(i.values())[0]))
	voxel = Voxel(position = save_new, texture = texture)


if len_pos == 0:
	for z in range(20):
		for x in range(20):
			box = {str(grass_texture) : list((x,0,z))}
			obj["position"].append(box)
			voxel = Voxel(position = (x,0,z))
else:
	print('------->', len_pos)


deatils = Text(origin=(-.7, -1.5),
	font='VeraMono.ttf', 
	color=color.black,
	) 

player = FirstPersonController()
sky = Sky()
hand = Hand()
app.run()
