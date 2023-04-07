import createLists
import firstRandSchedules
import fitness
import random

# Set the seed value
random.seed(1234)

activityList = createLists.return_activityList()
roomList = createLists.return_roomList()
timeList = createLists.return_timeList()
Facilitators = createLists.return_Facilitators()

rand_activity_list = firstRandSchedules.generate(activityList, roomList, timeList, Facilitators)

# for obj in rand_activity_list:
#     print(obj.activityName, obj.room, obj.time, obj.facilitator, obj.fitness, sep=', ')

# Find the fitness of the random list
rand_activity_list = fitness.facilitator_choice_score(rand_activity_list, activityList)
rand_activity_list = fitness.room_score(rand_activity_list, activityList, roomList)
rand_activity_list = fitness.facilitator_load_score(rand_activity_list)
rand_activity_list = fitness.activity_adjustment(rand_activity_list)


for obj in rand_activity_list:
    print(obj.activityName, obj.room, obj.time, obj.facilitator, obj.fitness, sep=', ')


