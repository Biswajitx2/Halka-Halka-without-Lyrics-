import sys
import time
import os

PINK, BLUE, CYAN = "\033[95m", "\033[94m", "\033[96m"
GREEN, YELLOW, RESET = "\033[92m", "\033[93m", "\033[0m"

lyrics = [
    f"{PINK}💗 kisi ne naa kiya he jaisaa ishq tera meraa...{RESET}",
    f"{BLUE}💫 me daudta aata hoon koi naam le jo tera...{RESET}",
    f"{CYAN}✨kisi ne na kiya hai ishq tera mera...{RESET}",
    f"{GREEN}😋 mera ghamon ki raat ka tu ujla savera...{RESET}",
    f"{YELLOW}💖 rhneee doo na nasheee me...{RESET}",
    f"{PINK}(⁠＾⁠3⁠＾⁠♪{RESET}",
]
delays = [0.2, 0.2, 0.2, 0.2, 1.5, 4.2]

os.system("cls" if os.name == "nt" else "clear")

print("=" * 60)
print(" HALKA HALKA SONG LYRICS ".center(60))
print("=" * 60)


def type_line(line):
    for char in line:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()


for i in range(len(lyrics)):
    type_line(lyrics[i])
    time.sleep(delays[i])