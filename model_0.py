import random

N_OF_ROUNDS = 20
N_OF_AGENTS = 5
PROB_BEST = 0.8

BANDIT1 = {"mu": float(0), "sigma": float(2)}
BANDIT2 = {"mu": float(2), "sigma": float(10)}

def play(n_of_rounds=N_OF_ROUNDS, p=PROB_BEST):
    rounds = 0
    draws = {"bandit_1": [], "bandit_2": []}
    
    def bandit_draw(bandit):
        return random.normalvariate(bandit["mu"], bandit["sigma"])
    
    while rounds < n_of_rounds:
        if draws["bandit_1"] and draws["bandit_2"]:
            mean_bandit1 = sum(draws["bandit_1"]) / len(draws["bandit_1"])
            mean_bandit2 = sum(draws["bandit_2"]) / len(draws["bandit_2"])
            if random.random() < p:
                fav_bandit = BANDIT1 if mean_bandit1 > mean_bandit2 else BANDIT2
            else:
                fav_bandit = random.choice([BANDIT1, BANDIT2])
        else:
            fav_bandit = random.choice([BANDIT1, BANDIT2])
        
        if fav_bandit == BANDIT1:
            bandit_key = "bandit_1"
        else:
            bandit_key = "bandit_2"
        
        draws[bandit_key].append(bandit_draw(fav_bandit))
        rounds += 1

    return draws

def generate_turtles(n_of_agents=N_OF_AGENTS):
    turtles = []
    for _ in range(n_of_agents):
        turtles.append(play())
    return turtles

def print_turtles(turtles):
    for i, turtle in enumerate(turtles):
        print(f"TURTLE {i+1}:")
        for bandit in turtle:
            draws = ", ".join(f"{round(draw, 2)}" for draw in turtle[bandit])
            print(f"  {bandit}: {draws}")
        print()

turtles = generate_turtles()
print_turtles(turtles)
