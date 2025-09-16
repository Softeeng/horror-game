from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import H_rooms

app = Ursina()

# Player entity
player = FirstPersonController()

# Load rooms (from H_rooms module)
rooms = H_rooms.load_rooms()

# Quit game function
def input(key):
    if key == 'escape':
        print("Thanks for playing! Goodbye.")
        application.quit()

# Run the game
app.run()