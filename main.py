import createLists
import firstRandSchedules
import fitness
import geneticAlgo
import random

# Set the seed value
random.seed(1234)

activityList = createLists.return_activityList()
roomList = createLists.return_roomList()
timeList = createLists.return_timeList()
Facilitators = createLists.return_Facilitators()

rand_activity_list = firstRandSchedules.generate(activityList, roomList, timeList, Facilitators)

offcialActivityList = []

# Find the fitness of the random list
rand_activity_list = fitness.facilitator_choice_score(rand_activity_list, activityList)
rand_activity_list = fitness.room_score(rand_activity_list, activityList, roomList)
rand_activity_list = fitness.facilitator_load_score(rand_activity_list)
rand_activity_list = fitness.activity_adjustment(rand_activity_list)

# total sum of fitness
list_fitness_score = fitness.fitness_score(rand_activity_list)
print(list_fitness_score)

offcialActivityList += rand_activity_list

# for obj in rand_activity_list:
#     print(obj.activityName, obj.room, obj.time, obj.facilitator, obj.fitness, sep=', ')


selectedList = geneticAlgo.selection(rand_activity_list, 250)


childList = geneticAlgo.crossover(selectedList, activityList, roomList, timeList, Facilitators)

childList = fitness.facilitator_choice_score(childList, activityList)
childList = fitness.room_score(childList, activityList, roomList)
childList = fitness.facilitator_load_score(childList)
childList = fitness.activity_adjustment(childList)



offcialActivityList += childList
list_fitness_score = fitness.fitness_score(offcialActivityList)
print(list_fitness_score)

# for obj in offcialActivityList:
#     print(obj.activityName, obj.room, obj.time,
#           obj.facilitator, obj.fitness, sep=', ')

