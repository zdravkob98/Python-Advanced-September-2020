import config

x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
food_pos = [x, y]
food_img = None

def show():
    fill(0, 255, 0)
    image(food_img, food_pos[0], food_pos[1], config.SCALE, config.SCALE)
    
def reset():
    x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE
    y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE
    food_pos[0] = x
    food_pos[1] = y
