SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500 

   
def draw_text(screen, text, font, color, x, y):
    """
    Utility function to draw text
    Borrowed from previous tutorial: Pong by Coding with Russ
    """
    img = font.render(text, True, color) #Creates text image
    screen.blit(img, (x, y)) # Draws text image
