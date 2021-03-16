# Game that asks the user for the capital of a randomly chosen state.
# The game must keep asking questions until the user enters the correct answer, or types 'exit'.

import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}



def choose_random_state(dictionary):
    # Todo: Make a copy of the original dictionary because we will be mutating the values throughout the game
    # dict_copy = dictionary.copy()
    randomly_chosen_state = random.choice(list(dictionary))
    randomly_chosen_capital = dictionary[randomly_chosen_state]

    return randomly_chosen_state, randomly_chosen_capital


def hint_reveal(capital):
    return capital[0]



def play_game(num_of_coins, capitals_dict):

    capitals_dict_copy = capitals_dict.copy()

    num_of_chances = num_of_coins

    user_score = 0

    high_score = 0

    num_of_hints_left = 3

    print(f"Welcome to the states capital game! \nYou have {num_of_chances} chances to answer all the questions correctly!\n")
    print(f"If you are stuck, you can use the command 'hint' to reveal the first letter of the correct answer!\n")
    while True:

        if user_score == len(capitals_dict):
            print('Great job, you won! Let\'s play again soon!')
            break

        question_state, question_capital = choose_random_state(capitals_dict_copy)
        user_answer = input(f"What is the state capital of {question_state}?: ")

        if user_answer.lower() == question_capital.lower():
            print("\nThat is the correct answer!\n")
            # Todo: Delete the key, value of correct answers
            del capitals_dict_copy[question_state]
            user_score = user_score + 1
            if high_score < user_score:
                high_score = user_score
            print(f"Your score is {user_score}\n")

        # If the user types any combination of letters resulting in 'exit', exit the game
        elif user_answer.lower() == 'exit':
            print("Are you a quitter? We don't like quitters. Bye Bye!")
            break    

        # If the user types in a wrong answer, decrement num_of_chances by 1 and stop the loop if num_of_chances is equal to 0
        else:
            print("\nThat was a wrong answer.\n")
            print(f"The correct answer is \'{question_capital}\'\n")

            num_of_chances = num_of_chances - 1

            print(f"You have {num_of_chances} chances left.\n")
            print(f"Your current score: {user_score}\n")

            if num_of_chances == 0:
                print("Game Over!\n")
                print(f"Your high score: {high_score}\n")
                play_again = input('Try again? (Y/N): ')
                if play_again.lower() == 'y':
                    # Reset the number of chances and replenish the deleted states back into dict
                    num_of_chances = num_of_coins
                    capitals_dict_copy = capitals_dict.copy()
                    user_score = 0
                    continue
                else:
                    print(f"\nYour highscore this round was {high_score} points! Great job! See you next time!")
                    break


play_game(3, capitals_dict)




# Todo: Make a highscore variable to show the player what the current highscore is
# Todo: When the player triggers gameover, ask the player if they want to continue.
#       If the player types 'Y' for yes, keep the current highscore
# Todo: Make a 'hint' function where user gets 3 hint options when stuck. The hint command reveals the first letter of the answer