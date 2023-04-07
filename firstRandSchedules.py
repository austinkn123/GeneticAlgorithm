import random

class offcialActivity:
    def __init__(self, activityName, room, time, facilitator, fitness):
        self.activityName = activityName
        self.room = room
        self.time = time
        self.facilitator = facilitator
        self.fitness = fitness

def generate(activityList, roomList, timeList, Facilitators):
    randActivityList = []
    i = 0
    while i <= 500:
        random_actvitiy = random.choice(activityList)
        random_room = random.choice(roomList)
        random_time = random.choice(timeList)
        random_facilitator = random.choice(Facilitators)
        randActivityList.append(offcialActivity(
            random_actvitiy.name, random_room.name, random_time, random_facilitator, 0))
        i += 1
    
    return randActivityList
    
        
