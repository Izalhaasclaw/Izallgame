import random
angka_rahasia = random.randint(1, 50)
percobaan = int(0)
print("Welcome to Faizal Gambit!".upper())
depo = int(input("Enter the amount for deposit (Minimal 20.000 Maximal 50000): ".upper()))
hadiah = int (random.randint(1000000, 5000000))

if depo >= 20000:  
    max = depo/5000
    bonus = depo*50/100
    hadiah += bonus
    print(f"You have {max} Guessing Chance".upper())
    while True:
        print("Guessing Chance.")
        tebakan = int(input("Enter your guess : "))
        percobaan += 1
        cashback = max - percobaan
        
        if tebakan == angka_rahasia:
            print("="*100)
            print(f"GACOR BANG! You Get Rp.{hadiah:,.2f} in {percobaan} Trial Times".upper)
            print(f"You Get Cashback Rp.{cashback*5000:,.2f}")
            break
        elif percobaan == max:
            print("="*100)
            print(f"The Correct Number Is {angka_rahasia}".upper())
            print(f"Your Chance Is Over, Try Again Next Time!".upper())
            break
        else:
            print("="*100)
            print("You're Out of Luck!")
            print(f"Chance to guess Stay {max - percobaan} Trial Times".upper())
            
else:
    print("="*100)
    print(f"YAHAA POOR DON'T DEPOSIT!")
            