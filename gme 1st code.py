import random
# Global Variables
lives = 3
score = 0
distance = 5

# Welcome Function
def welcome():
    print("=" * 40)
    print("      🤖 ROBO FOOTBALL 🤖")
    print("=" * 40)
    print("Goal: Score 3 goals!")
    print("You have 3 lives.")
    print("Reach the goal and shoot.")
    print()

# Show
def show_status():
    print("\n----------------------------")
    print("Lives :", lives)
    print("Score :", score)
    print("Distance from Goal :", distance)
    print("----------------------------")

# Move Forward
def move_forward():
    global distance, lives

    print("\nRobot moves forward...")

    chance = random.randint(1, 100)

    if chance <= 70:
        distance -= 1
        print("✅ Success! You moved closer to the goal.")
    else:
        lives -= 1
        print("❌ Defender blocked you!")
        print("You lost 1 life.")

# Pass Ball
def pass_ball():
    global lives

    print("\nPassing the ball...")

    chance = random.randint(1, 100)

    if chance <= 80:
        print("✅ Perfect Pass!")
    else:
        lives -= 1
        print("❌ Bad Pass!")
        print("Opponent stole the ball.")
        print("You lost 1 life.")

# Dribble
def dribble():
    global lives

    print("\nTrying to dribble...")

    chance = random.randint(1, 100)

    if chance <= 60:
        print("✅ Nice Dribble!")
    else:
        lives -= 1
        print("❌ Defender took the ball.")
        print("You lost 1 life.")

# Shoot
def shoot():
    global score, distance

    if distance > 0:
        print("\n⚠ You are too far from the goal!")
        return

    print("\nShooting...")

    chance = random.randint(1, 100)

    if chance <= 70:
        score += 1
        distance = 5
        print("🥳 GOOOOAAALLL!!")
    else:
        distance = 5
        print("🥅 Goalkeeper saved the shot!")

# Win Check
def check_win():
    if score == 3:
        print("\n🏆 Congratulations!")
        print("You won the Robo Football Game!")
        return True
    return False

# Game Over Check
def game_over():
    if lives == 0:
        print("\n💀 GAME OVER")
        return True
    return False

# Main Game
def play_game():
    welcome()

    while True:

        show_status()

        print("\nChoose an action")
        print("1. Move Forward")
        print("2. Pass")
        print("3. Dribble")
        print("4. Shoot")

        choice = input("Enter your choice: ")

        if choice == "1":
            move_forward()

        elif choice == "2":
            pass_ball()

        elif choice == "3":
            dribble()

        elif choice == "4":
            shoot()

        else:
            print("Invalid Choice!")

        if check_win():
            break

        if game_over():
            break

play_game()