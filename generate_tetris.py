import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import random

# Configuration
WIDTH, HEIGHT = 10, 20  # Grid size
BLOCK_SIZE = 20  # Size of each block in pixels
FRAME_COUNT = 50  # Number of frames
GIF_FILE = "tetris_graph.gif"

# Colors for blocks
COLORS = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF2"]

def create_frame(grid):
    """Creates an image frame from the current grid."""
    img = Image.new("RGB", (WIDTH * BLOCK_SIZE, HEIGHT * BLOCK_SIZE), "white")
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x]:
                draw.rectangle(
                    [x * BLOCK_SIZE, y * BLOCK_SIZE,
                     (x + 1) * BLOCK_SIZE - 1, (y + 1) * BLOCK_SIZE - 1],
                    fill=grid[y][x]
                )
    return img

def generate_tetris_animation():
    """Generates a Tetris-style animation."""
    frames = []
    grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for frame in range(FRAME_COUNT):
        # Add a new random block
        x = random.randint(0, WIDTH - 1)
        color = random.choice(COLORS)
        for y in range(HEIGHT - 1, -1, -1):
            if grid[y][x] is None:
                grid[y][x] = color
                break

        # Generate the frame
        frames.append(create_frame(grid))

    # Save as GIF
    frames[0].save(
        GIF_FILE,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )

if __name__ == "__main__":
    generate_tetris_animation()
