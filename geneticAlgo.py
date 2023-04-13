import random

class offcialActivity:
    def __init__(self, activityName, room, time, facilitator, fitness):
        self.activityName = activityName
        self.room = room
        self.time = time
        self.facilitator = facilitator
        self.fitness = fitness

# Selection
# Several selection Methods
# Roulette Wheel Selection: In this method, each individual is assigned a probability of selection based on their fitness value. The individuals with higher fitness values have a higher probability of being selected.
# Tournament Selection: In this method, a random subset of individuals is selected from the population, and the fittest individual from that subset is selected for mating.
# Rank Selection: In this method, the individuals are ranked based on their fitness values, and the probability of selection is proportional to their rank.
# Elitism Selection: In this method, the best individuals from the population are selected to be parents in the next generation, ensuring that their favorable traits are passed on to future generations.

def selection(list, num_parents):
    # Sort the list by fitness
    list.sort(key=lambda x: x.fitness, reverse=True)
    return list[:num_parents]

# Crossover
def crossover(list, activityList, roomList, timeList, Facilitators):
    childList = []
    while len(list) > 0:
        random_mutation = random.randint(0, 100)
        random_number1 = random.randint(0, 1)
        random_number2 = 1 if random_number1 == 0 else 0
        if random_mutation == 1:
            childList.append(mutation(activityList, roomList, timeList, Facilitators))
        else:
            childList.append(offcialActivity(
                list[random_number1].activityName, list[random_number1].room, list[random_number2].time, list[random_number2].facilitator, 0))
        list.pop(0)
        list.pop(0)
    return childList

# Mutation
def mutation(activityList, roomList, timeList, Facilitators):
    random_actvitiy = random.choice(activityList)
    random_room = random.choice(roomList)
    random_time = random.choice(timeList)
    random_facilitator = random.choice(Facilitators)
    return offcialActivity(
        random_actvitiy, random_room, random_time, random_facilitator, 0)
