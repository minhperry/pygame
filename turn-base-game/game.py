from init import player
import random as r
from time import sleep

p = player("Player")
b = player("bot")
print(f"You: {p.health}", "♥" * int(p.health))
print(f"Bot: {b.health}", "♥" * int(b.health))

def main():
    while p.health >= 0 and b.health >= 0:
        pt = True
        ct = False
        while pt == True:
            print(f"It's {p.name}'s turn!")
            ab = int(input("Ability > "))
            if ab == 1:
                d = p.attack(b)
                print(f"You used 'Attack' on bot. It dealt {d} damage.")
            elif ab == 2:
                p.heal()
                print(f"You used 'Heal' on yourself.")
            elif ab == 3:
                d = p.drain(b)
                print(f"You used 'Drain' on bot. It dealt {d} damage.")
            elif ab == 4:
                d = p.critical(b)
                print(
                    f"You used 'Critical' on bot. You lost {d} HP but dealt {2 * d} dammage on the enemy."
                )
            elif ab == 5:
                d = p.kill(b)
                print(f"You used 'Kill' on bot. Both of you lost {d} HP.")
            print(f"You: {p.health}", "♥" * int(p.health))
            print(f"Bot: {b.health}", "♥" * int(b.health))
            print("\n")
            sleep(0.5)
            pt = False
            ct = True

        while ct == True:
            print(f"It's {b.name}'s turn!")
            ab = r.randint(1, 5)
            if ab == 1:
                d = b.attack(p)
                print(f"Bot used 'Attack' on you. It dealt {d} damage.")
            elif ab == 2:
                b.heal()
                print(f"Bot used 'Heal' on themselves.")
            elif ab == 3:
                d = b.drain(p)
                print(f"Bot used 'Drain' on you. It dealt {d} damage.")
            elif ab == 4:
                d = b.critical(p)
                print(
                    f"Bot used 'Critical' on you. Bot lost {d} HP but dealt {2 * d} damage on you."
                )
            elif ab == 5:
                d = b.kill(p)
                print(f"Bot used 'Kill' on you. Both of you lost {d} HP.")
            print(f"You: {p.health}", "♥" * int(p.health))
            print(f"Bot: {b.health}", "♥" * int(b.health))
            print("\n")
            sleep(0.5)
            pt = True
            ct = False
    else:
        print('Game over!')
        if p.health > b.health: print(f'You have defeated the bot!')
        elif p.health < b.health: print(f'You were defeated by the bot :( Good luck next time')

if __name__ == "__main__":
    main()