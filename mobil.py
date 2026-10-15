import os
import time
import random
import shutil

# warna
RED = "\033[91m"
BLUE = "\033[94m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# mobil
car1 = [
",/``````````'.______",
"|  SYR      |   [] |",
"| _         |    _ |>",
"'-(O)----------(O)-'"
]

car2 = [
"/~~~~~~~~~\______",
"|  MBG   ||  ##\\_",
"| _           _ |*|",
"'-(o)```````(o)```'"
]

# terminal
try:
    width = shutil.get_terminal_size().columns
except:
    width = 80

center = width // 2
start_pos = width // 3
finish_x = center + 10

# =====================
# GARIS PUTUS
# =====================
road_offset = 0

def get_dash(i):
    if (i + road_offset) % 6 < 3:
        return "-"
    return " "

# =====================
# DRAW
# =====================
def draw_line(car_line, pos, color):
    pos = int(pos)
    line = ""

    for i in range(width):
        if i >= pos and i < pos + len(car_line):
            line += color + car_line[i - pos] + RESET
        elif i == 2 or i == width - 3:
            line += "|"
        elif i == center:
            line += WHITE + get_dash(i) + RESET
        else:
            line += " "
    print(line)

def draw_finish_line(car_line, pos, color):
    pos = int(pos)
    line = ""

    for i in range(width):
        if i >= pos and i < pos + len(car_line):
            line += color + car_line[i - pos] + RESET
        elif i == finish_x:
            line += GREEN + "#" + RESET
        elif i == 2 or i == width - 3:
            line += "|"
        elif i == center:
            line += WHITE + get_dash(i) + RESET
        else:
            line += " "
    print(line)

def draw_scene(title, pos1, pos2):
    clear()
    print("\n" + YELLOW + title.center(width) + RESET + "\n")

    for i in range(len(car1)):
        draw_line(car1[i], pos1, RED)

    print("\n")

    for i in range(len(car2)):
        draw_line(car2[i], pos2, BLUE)

# =====================
# COUNTDOWN
# =====================
for t in ["3", "2", "1"]:
    draw_scene(t, start_pos, start_pos)
    time.sleep(1)

draw_scene("GO!!!", start_pos, start_pos)
time.sleep(1)

# =====================
# BALAPAN RANDOM
# =====================
pos1 = start_pos
pos2 = start_pos

speed1 = 0
speed2 = 0

max_pos = finish_x - len(car1[0]) - 2

for step in range(180):
    clear()

    road_offset += 1

    # akselerasi random
    speed1 += random.uniform(0.01, 0.05)
    speed2 += random.uniform(0.01, 0.05)

    # efek salip
    if pos1 < pos2:
        speed1 += random.uniform(0.02, 0.05)
    else:
        speed2 += random.uniform(0.02, 0.05)

    # drama
    if random.random() < 0.05:
        speed1 *= 0.7
    if random.random() < 0.05:
        speed2 *= 0.7

    speed1 = min(speed1, 0.8)
    speed2 = min(speed2, 0.8)

    # GERAK TANPA DIKUNCI SAMA
    pos1 += speed1
    pos2 += speed2

    # stop setelah finish (tapi tetap beda posisi)
    if pos1 > max_pos:
        pos1 = max_pos + random.uniform(0, 2)

    if pos2 > max_pos:
        pos2 = max_pos + random.uniform(0, 2)

    # gesekan
    speed1 *= 0.9
    speed2 *= 0.9

    print(YELLOW + "RACE...\n" + RESET)

    for i in range(len(car1)):
        draw_line(car1[i], pos1, RED)

    print("\n")

    for i in range(len(car2)):
        draw_line(car2[i], pos2, BLUE)

    time.sleep(0.06)

# =====================
# ANTI SERI (FIX TERAKHIR)
# =====================
if abs(pos1 - pos2) < 0.5:
    if random.random() < 0.5:
        pos1 += 0.5
    else:
        pos2 += 0.5

# =====================
# FINISH
# =====================
clear()

print("\n" + " " * (finish_x - 3) + GREEN + "FINISH" + RESET + "\n")

for i in range(len(car1)):
    draw_finish_line(car1[i], pos1, RED)

print("\n")

for i in range(len(car2)):
    draw_finish_line(car2[i], pos2, BLUE)

# hasil
if pos1 > pos2:
    print(RED + "\n🏆 SAYUR BALAP MENANG!" + RESET)
else:
    print(BLUE + "\n🏆 MBG MENANG!" + RESET)