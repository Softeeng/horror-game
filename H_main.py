from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import H_rooms

app = Ursina()

# Load rooms (from H_rooms module)
walls = H_rooms.load_rooms()

# Player entity (create after rooms so initial ground-raycast can find floor)
player = FirstPersonController()
player.position = (0,5,0)  # start higher, then snap down
player.collider = 'box'
player.gravity = 1.0

# Helper: validate whether there's a walkable floor below the current player position
def _needs_snap():
    ray = raycast(player.world_position + (0, player.height, 0), player.down, traverse_target=scene, ignore=[player], distance=3, debug=False)
    return not (ray.hit and getattr(ray, 'world_normal', Vec3(0,0,0)).y > 0.6 and ray.world_point.y < player.y)

# Snap to floor if needed
if _needs_snap():
    _start = Vec3(player.x, player.y + player.height + 0.1, player.z)
    _down_ray = raycast(_start, (0,-1,0), traverse_target=scene, ignore=[player], distance=200, debug=False)
    if _down_ray.hit and _down_ray.world_point.y < player.y and getattr(_down_ray, 'world_normal', Vec3(0,0,0)).y > 0.6:
        player.y = _down_ray.world_point.y + 0.05
        player.grounded = True
    else:
        _high_ray = raycast((player.x, player.y + 100, player.z), (0,-1,0), traverse_target=scene, ignore=[player], distance=400, debug=False)
        if _high_ray.hit and _high_ray.world_point.y < player.y and getattr(_high_ray, 'world_normal', Vec3(0,0,0)).y > 0.6:
            player.y = _high_ray.world_point.y + 0.05
            player.grounded = True
# Debugging removed; keep a safety clamp to reset the player if they fall too far
def update():
    if player.y < -50:
        print("[safety] player fell below -50 — resetting position")
        player.position = (0,5,0)
        player.grounded = False

# Quit game function
def input(key):
    if key == 'escape':
        print("Thanks for playing! Goodbye.")
        application.quit()

# Run the game
app.run()