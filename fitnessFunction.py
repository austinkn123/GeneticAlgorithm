def facilitator_score(rand_activity_list, activityList):
    for activity in rand_activity_list:
        for set_activity in activityList:
            if activity.activityName == set_activity.name:
                if activity.facilitator in set_activity.perFacilitator:
                    activity.fitness += .5
                elif activity.facilitator in set_activity.crossoverFacilitators:
                    activity.fitness += .2
                else:
                    activity.fitness -= .1
    return rand_activity_list

def room_score(rand_activity_list, activityList, roomList):
    # for the random list
    for activity in rand_activity_list:
        # for the set list
        for set_activity in activityList:
            # if the activity name is the same
            if activity.activityName == set_activity.name:
                # for the room list (now checking room from matching activity name)
                for room in roomList:
                    # if the room name is the same
                    if activity.room == room.name:
                        # if the room capacity is less than the expected enrollment
                        if room.capacity < set_activity.expectedEnroll:
                            activity.fitness -= .5
                        # if the room capacity is greater than the expected enrollment * 3
                        elif room.capacity > set_activity.expectedEnroll *3:
                            activity.fitness -= .2
                        # if the room capacity is greater than the expected enrollment * 6
                        elif room.capacity > set_activity.expectedEnroll *6:
                            activity.fitness -= .4
                        else:
                            activity.fitness += .3
    return rand_activity_list


