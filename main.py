import createLists
import firstRandSchedules
import fitnessFunction
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


rand_activity_list = fitnessFunction.facilitator_score(rand_activity_list, activityList)
rand_activity_list = fitnessFunction.room_score(rand_activity_list, activityList, roomList)


for obj in rand_activity_list:
    print(obj.activityName, obj.room, obj.time, obj.facilitator, obj.fitness, sep=', ')


