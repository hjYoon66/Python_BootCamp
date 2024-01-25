from art import logo, vs
import random 
from game_data import data

# Generate a random account from the game data.
def random_account():
    return random.choice(data)

# Format account data into printable format.
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


# Ask user for a guess.

# Check if user is correct.

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

def game():
    print(logo)
    score = 0
    a_account = random_account()
    b_account = random_account()
    game_should_continue = True

    while game_should_continue:
        a_account = b_account
        b_account = random_account()
        
        while a_account == b_account:
            b_account = random_account()

        print(f"Compare A : {format_data(a_account)}")
        print(vs)
        print(f"Compare B : {format_data(b_account)}")



        user_guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]
        is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score +=1
            print(f"You're right! Current score : {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score : {score}")

game()
