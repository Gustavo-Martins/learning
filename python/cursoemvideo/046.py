"""Countdown."""
from time import sleep


print("T Minus 20 seconds and counting.")
sleep(10)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("BLASTOFF!")
print("Burn, baby. BURN!")
