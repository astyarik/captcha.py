import random
import time

midt = 5
mint = 3
max = 3
tries = 0

while tries < max:
    start = time.time()

    code = random.randint(100000000, 999999999)
    print(f"Your code:", code, "Input it!")
    
    
    try:
        input_code = int(input("Input code:"))
    except ValueError:
        print("Incorrect value! Try again!")
        tries += 1

    elapsed = round(time.time() - start, 2)

    if code == input_code:
        if elapsed <= mint:
            print("Too fast!", elapsed)
            tries += 1.5
            continue
        if elapsed <= midt:
            print("Please, try again!")
            tries += 0.34
            continue

        print("Captcha is completed! Thanks! Time to this:", elapsed)
        break
    else:
        print("Captcha is not completed! Try again!")
        tries += 1
if tries == max:
    print("Blocked! Too many incorrect attempts.")
