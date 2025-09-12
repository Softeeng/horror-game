from ursina import *

# Ground entity
ground = Entity(model='plane', scale=(20,1,20), color=color.blue, position=(0,-1,0), collider='box')

# Rooms module
def room_1():
    walls = [
    Entity(model='cube', scale=(1,4,40), color=color.gray, position=(-10,0,0), collider = 'box'),
    Entity(model='cube', scale=(1,4,40), color=color.gray, position=(10,0,0), collider = 'box'),
    Entity(model='cube', scale=(40,4,1), color=color.gray, position=(0,0,-10), collider = 'box'),
    Entity(model='cube', scale=(40,4,1), color=color.gray, position=(0,0,10), collider = 'box')
    ]
    return walls