import arcade # ignore pylint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "My Game"

class MyGame(arcade.Window): # main app class
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) # call parent class and set up window
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        # set up game here - call this function to restart the game
        pass

    def on_draw(self):
        # render the screen
        arcade.start_render()
        # code to draw screen goes here

if __name__ == "__main__":
    window = MyGame() # generate window
    window.setup()
    arcade.run()