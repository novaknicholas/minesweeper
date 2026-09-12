import random
import sys
import time, os
win = False
position = 0
grid =[]
blank = []
def play_game():
    global win, position, grid, blank, width, height
    win = False
    position = 0
    grid =[]
    blank = []
    print("Welcome to Minesweeper! Would you like a basic introduction? (y/n)")
    choice = input("> ").lower().strip()
    if choice in ["yes", "y"]:
        print("Minesweeper is a game of logic\n")
        print("The grid contains hidden mines, indicated by (💣 )")
        print("Each number shows how many mines are touching it (in 8 directions)\n")
        print("You can FLAG (🚩 ) a tile if you think it contains a mine by typing (f)")
        print("Or, you can reveal a tile by typing (r)")
        print("Be careful though! Revealing a mine means you lose!")
        print("Your goal is to flag all mines (note: tiles marked with flags that are NOT mines will prevent you from winning)\n")
        print("""
    - Commands:
        r = reveal the current tile
        f = flag the current tiler
        w / a / s / d = move up / left / down / right
    Reveal carefully... if you hit a mine, you lose!
    Good luck, and watch your step.
    """)
    while True:
        try:
            width = int(input("Select the desired width of your map: ").strip())
            if 1<= width < 60:
                break
            print("Please enter a positive integer less than 60 for performance reasons.")
        except ValueError:
            print("Please enter a whole number as an integer.")
    while True:
        try:
            height = int(input("Select the desired height of your map: ").strip())
            if 1<= height < 60:
                break
            print("Please enter a positive integer less than 60 for performance reasons.")
        except ValueError:
            print("Please enter a whole number as an integer")
    
    
    print("You selected a "+ str(width) + " by "+ str(height) + " map. ")
    # Create mines randomly, function unncessary
    for i in range(width * height):
        if random.randint(1,10) == 1:
            grid.append("*")
        else: 
            grid.append(0)
    while True:
        grid = []
        for i in range(width*height):
            if random.randint(1,10) == 1:
                grid.append("*")
            else:
                grid.append(0)
        create()
        if grid [0] == 0:
            break
    create_blank()
    
    create_blank()
    while not win:
        blank[0] = grid[0]  # reset initial reveal
        show_grid()
        position_find()
    reply = input("Want to play again? yes (y) or no (n): ").lower().strip()
    if reply in ["y", "yes"]:
        return True  # signal to replay?
    else:
        return False  # signal to quit
def create():
    global width
    global height
    total = len(grid)

    for i in range(total):
        if grid[i] == "*":
            if i % width != 0 and grid[i - 1] != "*":
                grid[i - 1] += 1
            if i % width != (width - 1) and grid[i + 1] != "*":
                grid[i + 1] += 1
            if i - width >= 0 and grid[i - width] != "*":
                grid[i - width] += 1
            if i + width < total and grid[i + width] != "*":   
                grid[i + width] += 1
            if i - (width + 1) >= 0 and i % width != 0 and grid[i - (width + 1)] != "*":
                grid[i - (width + 1)] += 1
            if i - (width - 1) >= 0 and i % width != (width - 1) and grid[i - (width - 1)] != "*":
                grid[i - (width - 1)] += 1
            if i + (width - 1) < total and i % width != 0 and grid[i + (width - 1)] != "*":  
                grid[i + (width - 1)] += 1
            if i + (width + 1) < total and i % width != (width - 1) and grid[i + (width + 1)] != "*":  
                grid[i + (width + 1)] += 1
def create_blank():
    for i in range(len(grid)):
        blank.append("#")

def position_find():
    global win
    global position  # needed to be specified as a global variable
    move = (str(input("Check tile (r) or flag (f)? Or (w),(a),(s),(d) to keep moving: "))).strip().lower()
    if move == "r":
        if grid[position] == "*":
            print("You hit a mine!")
            win = True
            boom_animation(grid, width, height, position)
            return
        elif grid[position] == 0:
            reveal_zero(position)
        blank[position] = grid[position]
        
    elif move == "f":
        if blank[position] == "🚩":
            blank[position] = "#"
        blank[position] = "🚩"
        
    elif move == "w":
        if position -width >=0:
            position = position -width
    elif move == "a":
        if position -1 >= 0:
            position = position -1
    elif move == "s":
        if position + width < len(grid):
            position = position + width
    elif move == "d":
        if position + 1 < len(grid):
            position = position + 1

    check_win()
def reveal_zero(position):
    time.sleep(.05)
    show_grid()
    total = len(grid)
    #Left
    if position % width != 0 and grid[position - 1] == 0 and blank[position - 1] != 0:
        blank[position - 1] = grid[position - 1]
        blank[position - 1] = 0
        reveal_zero(position-1)

    #Bottom left
    if position + (width - 1) < total and position % width != 0 and grid[position + (width - 1)] == 0 and blank[position + (width - 1)] != 0:
        blank[position + (width - 1)] = grid[position + (width - 1)]
        blank[position + (width - 1)] = 0
        reveal_zero(position + (width - 1))

    #Bottom
    if position + width < total and grid[position + width] == 0 and blank[position + width] != 0:
        blank[position + width] = grid[position + width]
        blank[position + width] = 0
        reveal_zero(position + width)

    #Bottom right
    if position + (width + 1) < total and position % width != (width - 1) and grid[position + (width + 1)] == 0 and blank[position + (width + 1)] != 0:
        blank[position + (width + 1)] = grid[position + (width + 1)]
        blank[position + (width + 1)] = 0
        reveal_zero(position + (width + 1))

    #Right
    if position % width != (width - 1) and grid[position + 1] == 0 and blank[position + 1] != 0:
        blank[position + 1] = grid[position + 1]
        blank[position + 1] = 0
        reveal_zero(position+1)

    #Topright
    if position - (width - 1) >= 0 and position % width != (width - 1) and grid[position - (width - 1)] == 0 and blank[position - (width - 1)] != 0:
        blank[position - (width - 1)] = grid[position - (width - 1)]
        blank[position - (width - 1)] = 0
        reveal_zero(position - (width - 1))

    #Top
    if position - width >= 0 and grid[position - width] == 0 and blank[position - width] != 0:
        blank[position - width] = grid[position - width]
        blank[position - width] = 0
        reveal_zero(position - width)

    #Top left
    if position - (width + 1) >= 0 and position % width != 0 and grid[position - (width + 1)] == 0 and blank[position - (width + 1)] != 0:
        blank[position - (width + 1)] = grid[position - (width + 1)]
        blank[position - (width + 1)] = 0 
        reveal_zero(position - (width + 1))
    # reveal non zeros adjacent to zeros
    if position % width != 0 and grid[position - 1] != "*" and grid[position - 1] != 0 and blank[position - 1] == "#":
        blank[position - 1] = grid[position - 1]
    # Bottom left
    if position + (width - 1) < total and position % width != 0 and grid[position + (width - 1)] != "*" and grid[position + (width - 1)] != 0 and blank[position + (width - 1)] == "#":
        blank[position + (width - 1)] = grid[position + (width - 1)]
    # Bottom
    if position + width < total and grid[position + width] != "*" and grid[position + width] != 0 and blank[position + width] == "#":
        blank[position + width] = grid[position + width]

    # Bottom right
    if position + (width + 1) < total and position % width != (width - 1) and grid[position + (width + 1)] != "*" and grid[position + (width + 1)] != 0 and blank[position + (width + 1)] == "#":
        blank[position + (width + 1)] = grid[position + (width + 1)]
    # Right
    if position % width != (width - 1) and grid[position + 1] != "*" and grid[position + 1] != 0 and blank[position + 1] == "#":
        blank[position + 1] = grid[position + 1]
    # Top right
    if position - (width - 1) >= 0 and position % width != (width - 1) and grid[position - (width - 1)] != "*" and grid[position - (width - 1)] != 0 and blank[position - (width - 1)] == "#":
        blank[position - (width - 1)] = grid[position - (width - 1)]
    # Top
    if position - width >= 0 and grid[position - width] != "*" and grid[position - width] != 0 and blank[position - width] == "#":
        blank[position - width] = grid[position - width]
    # Top left
    if position - (width + 1) >= 0 and position % width != 0 and grid[position - (width + 1)] != "*" and grid[position - (width + 1)] != 0 and blank[position - (width + 1)] == "#":
        blank[position - (width + 1)] = grid[position - (width + 1)]


def check_win():
    global win
    for i in range(len(grid)):
        if grid[i] == "*" and blank[i] != "🚩":
            win = False
            return
        if grid[i] != "*" and blank[i] == "🚩":
            win = False
            return
    win = True
    win_animation(grid, width, height)
    print("Victory! You found all the mines!")

def show_grid():
    for row in range(height):
        for col in range(width):
            index = row * width + col
            val = blank[index]

            # Convert all numbers, without changing their true values
            if val == 0:
                val = "0️⃣"
            elif val == 1:
                val = "1️⃣"
            elif val == 2:
                val = "2️⃣"
            elif val == 3:
                val = "3️⃣"
            elif val == 4:
                val = "4️⃣"
            elif val == 5:
                val = "5️⃣"
            elif val == 6:
                val = "6️⃣"
            elif val == 7:
                val = "7️⃣"
            elif val == 8:
                val = "8️⃣"
            elif val == "#":
                val = "⬜"
            elif val == "*":
                val = "💣"
            elif val == "🚩":
                val = "🚩"

            cell = (f"{val}")

            # Highlight the current cursor position — no width shift
            if index == position:
                print(f"▶{cell}", end="")
            else:
                print(f" {cell}", end="")
        print()


# boom_animation() and win_animation() below are purely cosmetic (non-invasive
# to game logic) and were largely AI-generated/adapted.

def boom_animation(grid, width, height, hit_pos):
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def draw_grid(emitter):
        clear()
        for r in range(height):
            row = []
            for c in range(width):
                row.append(emitter(r, c))
            print(" ".join(row))

    def idx(r, c):
        return r * width + c

    # Phase 1: red diagonal sweep
    span = width + height
    for t in range(-span, span + 1):
        def emit(r, c, t=t):
            return "🟥" if (r + c) <= t else "·"
        draw_grid(emit)
        time.sleep(0.03)

    # Phase 2: center ripple from the hit
    hx, hy = (hit_pos % width), (hit_pos // width)
    max_rad = int(max(width, height) * 1.2)

    for rad in range(max_rad):
        def emit(r, c, rad=rad):
            d = abs(c - hx) + abs(r - hy)
            if d == rad:
                return "💥"
            elif d < rad:
                return "🔥"
            else:
                return "🟥"
        draw_grid(emit)
        time.sleep(0.045)

    # Phase 3: ember rain pass
    ember_cols = [random.randint(0, width - 1) for _ in range(max(3, width // 2))]
    frames = height + 8
    for step in range(frames):
        def emit(r, c, step=step):
            base = "🟥"
            for k, col in enumerate(ember_cols):
                rr = (step - k * 2) % (height + 6) - 3
                cc = (col + (step // 3 + k) % 2) % width
                if r == rr and c == cc:
                    return random.choice(["🔥", "🔥", "💥", "💨"])
            return base
        draw_grid(emit)
        time.sleep(0.06)

    # Final: solid red with bombs revealed
    clear()
    for r in range(height):
        row_out = []
        for c in range(width):
            cell = grid[idx(r, c)]
            row_out.append("💣" if cell == "*" else "🟥")
        print(" ".join(row_out))
    print("\n☠️ GAME OVER ☠️")
    time.sleep(1.0)


def win_animation(grid, width, height):
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def draw_grid(emitter):
        clear()
        for r in range(height):
            for c in range(width):
                ch = emitter(r, c)
                print(ch, end=" ")
            print()

    # Phase 1: diagonal sweep fill
    span = width + height
    for t in range(-span, span + 1):
        def emit(r, c, t=t):
            return "🟩" if (r + c) <= t else "·"
        draw_grid(emit)
        time.sleep(0.03)

    # Phase 2: ripple rings from center
    cx, cy = (width - 1) / 2.0, (height - 1) / 2.0
    max_rad = int(max(width, height) * 1.2)
    for rad in range(max_rad):
        def emit(r, c, rad=rad):
            d = abs(r - cy) + abs(c - cx)
            if int(d) == rad:
                return "✅"
            elif d < rad:
                return "🟢"
            else:
                return "🟩"
        draw_grid(emit)
        time.sleep(0.045)

    # Phase 3: confetti rain
    conf_cols = [random.randint(0, width - 1) for _ in range(max(3, width // 2))]
    frames = height + 10
    for step in range(frames):
        def emit(r, c, step=step):
            base = "🟩"
            for k, col in enumerate(conf_cols):
                rr = (step - k * 2) % (height + 6) - 3
                cc = (col + (step // 3 + k) % 2) % width
                if r == rr and c == cc:
                    return random.choice(["✨", "✅", "🎉", "🍀"])
            return base
        draw_grid(emit)
        time.sleep(0.06)

    # Final reveal: full green board with mines shown
    clear()
    for r in range(height):
        row_out = []
        for c in range(width):
            idx = r * width + c
            if grid[idx] == "*":
                row_out.append("💣")
            else:
                row_out.append("🟩")
        print(" ".join(row_out))
    msg = "🏆  YOU WIN!  🏆"
    print("\n" + msg.center(width * 2))
    time.sleep(1.2)


while True:
    again = play_game()
    if not again:
        print("Thanks for playing!")
        break
