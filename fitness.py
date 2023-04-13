def facilitator_choice_score(rand_activity_list, activityList):
    for activity in rand_activity_list:
        for set_activity in activityList:
            if activity.activityName == set_activity.name:
                if activity.facilitator in set_activity.perFacilitator:
                    activity.fitness += .5
                elif activity.facilitator in set_activity.crossoverFacilitators:
                    activity.fitness += .2
                else:
                    activity.fitness -= .1

    # for the random list
    for activity in rand_activity_list:
        # for the inner random list
        for inner_activity in rand_activity_list:
            # if the activity room and time are the same
            if activity.room == inner_activity.room and activity.time == inner_activity.time:
                activity.fitness -= .5
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

def facilitator_load_score(rand_activity_list):
    counter = 0
    # for the random list
    for activity in rand_activity_list:
        # for the inner random list
        for inner_activity in rand_activity_list:
            # if the facilitator is the same
            if inner_activity.facilitator == activity.facilitator:
                # if the time is the same
                if inner_activity.time == activity.time:
                    counter += 1
                    activity.fitness -= .2
                # if the time is not the same
                else:
                    activity.fitness += .2
            # if the facilitator is scheduled for 4+ activities
            if counter > 4:
                activity.fitness -= .5
            elif counter >= 2:
                if activity.facilitator == 'Tyler':
                    activity.fitness += 0
                activity.fitness -= .4
            
            counter = 0
    return rand_activity_list

def activity_adjustment(rand_activity_list):
    # for the random list
    for activity in rand_activity_list:
        # for the inner random list
        for inner_activity in rand_activity_list:
            # if the activity name is the in the same section
            if activity.activityName == "SLA100A" and inner_activity.activityName == "SLA100B":
                # find the time difference
                timeDiff = abs(activity.time - inner_activity.time)
                # if the time difference is greater than 4
                if timeDiff > 4:
                    activity.fitness += .5
                # if there is no time difference (scheduled at the same time) 
                elif timeDiff == 0:
                    activity.fitness -= .5
            elif activity.activityName == "SLA100B" and inner_activity.activityName == "SLA100A":
                timeDiff = abs(activity.time - inner_activity.time)
                if timeDiff > 4:
                    activity.fitness += .5
                elif timeDiff == 0:
                    activity.fitness -= .5
            if activity.activityName == "SLA191A" and inner_activity.activityName == "SLA191B":
                timeDiff = abs(activity.time - inner_activity.time)
                if timeDiff > 4:
                    activity.fitness += .5
                elif timeDiff == 0:
                    activity.fitness -= .5
            elif activity.activityName == "SLA191B" and inner_activity.activityName == "SLA191A":
                timeDiff = abs(activity.time - inner_activity.time)
                if timeDiff > 4:
                    activity.fitness += .5
                elif timeDiff == 0:
                    activity.fitness -= .5
            # if the SLA191 section and SLA100 section are scheduled 1 hour apart or at the same time 
            if activity.activityName == "SLA191A" or activity.activityName == "SLA191B" and inner_activity.activityName == "SLA100A" or inner_activity.activityName == "SLA100B":
                timeDiff = abs(activity.time - inner_activity.time)
                if timeDiff > 1:
                    activity.fitness += .25
                elif timeDiff == 0:
                    activity.fitness -= .25
    
    for i in range(len(rand_activity_list) - 1):
        if rand_activity_list[i].activityName == "SLA100A" and rand_activity_list[i + 1].activityName == "SLA100B":
                # find the time difference
            timeDiff = abs(rand_activity_list[i].time - rand_activity_list[i].time)
                # if the time difference is greater than 4
            if timeDiff == 1:
                rand_activity_list[i].fitness += .5
                rand_activity_list[i + 1].fitness += .5
        elif rand_activity_list[i].activityName == "SLA100B" and rand_activity_list[i + 1].activityName == "SLA100A":
            timeDiff = abs(rand_activity_list[i].time - rand_activity_list[i].time)
            if timeDiff == 1:
                rand_activity_list[i].fitness += .5
                rand_activity_list[i + 1].fitness += .5
        if rand_activity_list[i].activityName == "SLA191A" and rand_activity_list[i + 1].activityName == "SLA191B":
            timeDiff = abs(rand_activity_list[i].time - rand_activity_list[i].time)
            if timeDiff == 1:
                rand_activity_list[i].fitness += .5
                rand_activity_list[i + 1].fitness += .5
        elif rand_activity_list[i].activityName == "SLA191B" and rand_activity_list[i + 1].activityName == "SLA191A":
            timeDiff = abs(rand_activity_list[i].time - rand_activity_list[i].time)
            if timeDiff == 1:
                rand_activity_list[i].fitness += .5
                rand_activity_list[i + 1].fitness += .5
    return rand_activity_list

def fitness_score_total(rand_activity_list):
    fitness_sum = 0
    # for the random list
    for activity in rand_activity_list:
         fitness_sum += activity.fitness
    return fitness_sum

def fitness_score_avg(fitness_score_total, rand_activity_list):
    return fitness_score_total / len(rand_activity_list)
