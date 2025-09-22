from ursina import *

# Ground entity
ground = Entity(model='plane', scale=(20,1,20), color=color.blue, position=(0,-1,0), collider='box')

# Helper function to create walls with doorways
def make_wall_with_door(position, axis='z', length=20, height=4, door_size=(4,3), wall_color=color.gray):
    ''' Creates a wall with a doorway opening in the center
    axis ='z' for north/south walls, 'x' for east/west walls'''
    entities = []
    door_w, door_h = door_size

    if axis == 'z': # north/south
        # Left/right parts of the wall
        entities.append(Entity(model='cube', scale=(length/2 - door_w/2, height, 1), position=(position[0] - (length/4 + door_w/4),
                                                                                               position[1] + height/2, position[2]), color=wall_color, collider='box'))
        entities.append(Entity(model='cube', scale=(length/2 - door_w/2, height, 1),position=(position[0], position[1] + height/2,
                                                                                              position[2]), color=wall_color, collider='box'))
        # Top part of the wall
        entities.append(Entity(model='cube', scale=(door_w, height - door_h, 1), position=(position[0], position[1] + height - (height - door_h)/2,
                                                                                           position[2]), color=wall_color, collider='box'))
    elif axis == 'x': # east/west
        # Front/back parts of the wall
        entities.append(Entity(model='cube', scale=(1, height, length/2 - door_w/2), position=(position[0], position[1] + height/2,
                                                                                               position[2] - (length/4 + door_w/4)), color=wall_color, collider='box'))
        entities.append(Entity(model='cube', scale=(1, height, length/2 - door_w/2), position=(position[0], position[1] + height/2,
                                                                                               position[2] + (length/4 + door_w/4)), color=wall_color, collider='box'))
        # Top part of the wall
        entities.append(Entity(model='cube', scale=(1, height - door_h, door_w), position=(position[0], position[1] + height - (height - door_h)/2,
                                                                                           position[2]), color=wall_color, collider='box'))
        return entities
# Rooms module
def make_room(size=(20,4,20), position=(0,0,0), wall_color=color.gray, floor_color=color.blue, doorways=None, add_ceiling=True):
    """ This creates a simple room with no doorways. The doorways = list of directions where doorways should be placed
      (i.e north,south,east,west). add_ceiling = True/False to add/remove ceiling."""
    
    if doorways is None:
        doorways = []

    x, y, z = position
    w, h, d = size
    parts = []

    # Create walls, floor, and ceiling

    # North wall
    if "north" in doorways:
        parts += make_wall_with_door(x, y, z - d/2, axis='z', length=w, height=h, wall_color=wall_color)
    else:
        parts.append(Entity(model='cube', scale=(w,h,1), position=(x, y, z - d/2), color=wall_color, collider='box'))

    # South wall
    if "south" in doorways:
        parts += make_wall_with_door(x, y, z + d/2, axis='z', length=w, height=h, wall_color=wall_color)
    else:
        parts.append(Entity(model='cube', scale=(w,h,1), position=(x, y + h/2, z +d/2), color=wall_color, collider='box'))

    # East wall
    if "east" in doorways:
        parts += make_wall_with_door((x + w/2, y, z), axis='x', length=d, height=h, wall_color=wall_color)
    else:
        parts.append(Entity(model='cube', scale=(1,h,d), position=(x + w/2, y + h/2, z), color=wall_color, collider='box'))
    
    # West wall
    if "west" in doorways:
        parts += make_wall_with_door((x - w/2, y, z), axis='x', length=d, height=h, wall_color=wall_color)
    else:
        parts.append(Entity(model='cube', scale=(1,h,d), position=(x - w/2, y + h/2, z), color=wall_color, collider='box'))
    
    # Floor
    parts.append(Entity(model='cube', scale=(w,1,d), position=(x, y - 0.5, z), color=floor_color, collider='box'))

    # Add ceiling
    if add_ceiling:
        parts.append(Entity(model='cube', scale=(w,1,d), position=(x, y + h + 0.5, z), color=color.rgb(50,50,50), collider='box'))
    
    return parts

    # Individual rooms
def room_1():
    return make_room(position=(0,0,0), size=(20,4,20), wall_color=color.azure, doorways=["east"], add_ceiling=True)
def room_2():
    return make_room(position=(20,0,0), size=(20,4,20), wall_color=color.orange, doorways=["west"], add_ceiling=True)

# Load rooms function
def load_rooms():
    rooms = []
    rooms += room_1()
    rooms += room_2()
    return rooms