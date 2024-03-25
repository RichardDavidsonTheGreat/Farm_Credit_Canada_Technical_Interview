from operator import countOf
import random
import time

def roll_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        rolls.append(random.randint(1, 6))
    return rolls

def play_game(num_dice):
    total_score = 0
    while num_dice > 0:
        dice = roll_dice(num_dice)
        if 3 in dice:
            total_score += 0
            num_3_rolled = countOf(dice, 3)
            num_dice -= num_3_rolled
        else:
            lowest_die = min(dice)
            total_score += lowest_die
            num_dice -= 1
    return total_score

def simulate_game(num_simulations, num_dice):
    num_possible_scores = num_dice * 6 + 1
    results = [0] * num_possible_scores
    start_time = time.time()
    for _ in range(num_simulations):
        score = play_game(num_dice)
        results[score] += 1
    end_time = time.time()
    total_time = end_time - start_time
    return results, total_time

def main():
    num_dice = int(input("Enter the number of dice: "))
    num_simulations = int(input("Enter the number of simulations: "))

    results, total_time = simulate_game(num_simulations, num_dice)

    print(f"Number of simulations was {num_simulations} using {num_dice} dice.")
    for score in range(len(results)):
        count = results[score]
        print(f"Total {score} occurs {count/num_simulations:.3f} occurred {count} times.")
    print(f"Total simulation took {total_time:.1f} seconds")

if __name__ == "__main__":
    main()