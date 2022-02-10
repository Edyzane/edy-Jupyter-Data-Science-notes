import random



def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
        return heads

def simulate(x):
    trials = []
    for i in range(x):
        trials.append(coin_trial())
    return(sum(trials)/x)

print(simulate(10))
print(simulate(100))
