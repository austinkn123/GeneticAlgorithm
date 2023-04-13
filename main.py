import createLists
import firstRandSchedules
import fitness
import geneticAlgo
import random
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Set the seed value
random.seed(1234)

activityList = createLists.return_activityList()
roomList = createLists.return_roomList()
timeList = createLists.return_timeList()
Facilitators = createLists.return_Facilitators()

rand_activity_list = firstRandSchedules.generate(activityList, roomList, timeList, Facilitators)
# Find the fitness of the random list
rand_activity_list = fitness.facilitator_choice_score(
    rand_activity_list, activityList)
rand_activity_list = fitness.room_score(
    rand_activity_list, activityList, roomList)
rand_activity_list = fitness.facilitator_load_score(rand_activity_list)
rand_activity_list = fitness.activity_adjustment(rand_activity_list)



officialActivityList = []

officialGenFitnessTotal = []

officialGenFitnessAvg = []

generationArrays = []

officialActivityList += rand_activity_list
for i in range(100):
    
    # total sum of fitness
    total_fitness_score = fitness.fitness_score_total(officialActivityList)

    # average fitness
    mean_fit = fitness.fitness_score_avg(
        total_fitness_score, officialActivityList)

    print("Fitness average for generation " + str(i + 1) +
          ": " + str(mean_fit) + "\n" + "Fitness total for generation " + str(i + 1) +
          ": " + str(total_fitness_score) + "\n" + "----------------------------------")
    
    officialGenFitnessTotal.append(total_fitness_score)
    officialGenFitnessAvg.append(mean_fit)

    # Select half of the list and crossover
    selectedList = geneticAlgo.selection(rand_activity_list, 250)
    childList = geneticAlgo.crossover(
        selectedList, activityList, roomList, timeList, Facilitators)

    childList = fitness.facilitator_choice_score(childList, activityList)
    childList = fitness.room_score(childList, activityList, roomList)
    childList = fitness.facilitator_load_score(childList)
    childList = fitness.activity_adjustment(childList)
    # print(str(len(childList)) + "\n" + "----------------------------------")

    
    # list_fitness_score = fitness.fitness_score_total(officialActivityList)
    officialActivityList[len(officialActivityList)//4:] = childList
    generationArrays.append(officialActivityList)
    

final_generation = generationArrays[-1]
final_fitness = []

for obj in final_generation:
    final_fitness.append(obj.fitness)

final_fitness_total = fitness.fitness_score_total(final_generation)
final_mean_fit = fitness.fitness_score_avg(
    final_fitness_total, final_fitness)

print("Fitness average for final generation: " + str(final_mean_fit) + "\n" + "Fitness total for final generation: " + str(final_fitness_total))

# find the highest element and its index in the array
highest_element = max(final_fitness)
highest_index = final_fitness.index(highest_element)
print ("Highest element in the array is: ", highest_element)
print ("Index of the highest element in the array is: ", highest_index)

i = 0
with open('output.txt', 'w') as file:
    for obj in final_generation:
        i+=1
        file.write("Activity Number: " + str(i) + "\n")
        file.write("Actvity Name: " + str(obj.activityName) + "\nActivtiy Room: " + str(obj.room) 
                   + "\nActivity Time:" +
                   str(obj.time) + "\nActivity Facilitator: " +
                   str(obj.facilitator) + "\nActivity Fitness: " + str(obj.fitness)
                   + "\n ------------------------\n")

