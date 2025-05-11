print("Do you want to play the quiz? ")

playing = input("Yes or No? ").lower()
if playing != "yes":
    quit()

print("Okay! Let's Play :)")

score = 0

answer = input("What does the CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the VRAM stand for? ").lower()
if answer == "virtual random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the OS stand for? ").lower()
if answer == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the HDD stand for? ").lower()
if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the USB stand for? ").lower()
if answer == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer = input("What does the DNS stand for? ").lower()
if answer == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

print("You got " + str(score) + " questions correct!")
