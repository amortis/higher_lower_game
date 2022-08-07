from random import randint
from data import data
from art import logo, vs

def comparing(follower_count_a,follower_count_b):
    if follower_count_a>follower_count_b:
        return 'A'
    else:
        return 'B'
def game():
    user_score = 0
    gameend = False
    num_a = randint(1,len(data))
    person_a = data[num_a]
    print(logo)
    while not gameend:
        name_a = person_a['name']
        follower_count_a = person_a['follower_count']
        description_a = person_a['description']
        country_a = person_a['country']
        num_b = randint(1, len(data))
        while num_a == num_b:
            num_b = randint(1, len(data)-1)
        else:
            person_b = data[num_b]
            name_b = person_b['name']
            follower_count_b = person_b['follower_count']
            description_b = person_b['description']
            country_b = person_b['country']
        print(f"Your current score: {user_score}")
        print(f"Compare A: {name_a}, {description_a}, from {country_a}")
        print(vs)
        print(f"Against B: {name_b}, {description_b}, from {country_b}")
        user_choise = input("Who has more followers? Type 'A' or 'B': ")
        if user_choise == comparing(follower_count_a, follower_count_b):
            user_score += 1
            person_a = person_b
        else:
            gameend = True
    print()
    print(f"You lost :(. Your final score: {user_score}")

game()