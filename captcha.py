import random

while True:
    code = random.randint(100000, 999999)
    print(f"Your code:", code, "Input it!")
    try:
        input_code = int(input("Input code:"))
    except ValueError:
        print("Incorrect value! Try again!")
    if code == input_code:
        print("Captcha is completed! Thanks!")
        break
    else:
        print("Captcha is not completed! Try again!")
