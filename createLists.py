class room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class activity:
    def __init__(self, name, expectedEnroll, perFacilitator, crossoverFacilitators):
        self.name = name
        self.expectedEnroll = expectedEnroll
        self.perFacilitator = perFacilitator
        self.crossoverFacilitators = crossoverFacilitators


Facilitators = ["Lock", "Glen", "Banks", "Richard",
                "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]

time = [10, 11, 12, 1, 2, 3]

activityList = []
activityList.append(activity("SLA100A", 50, [
    "Glen", "Lock", "Banks", "Zeldin", "Other"], ["Numen", "Richards"]))
activityList.append(activity("SLA100B", 50, [
    "Glen", "Lock", "Banks", "Zeldin", "Other"], ["Numen", "Richards"]))
activityList.append(activity("SLA191A", 50, [
    "Glen", "Lock", "Banks", "Zeldin", "Other"], ["Numen", "Richards"]))
activityList.append(activity("SLA191B", 50, [
    "Glen", "Lock", "Banks", "Zeldin", "Other"], ["Numen", "Richards"]))
activityList.append(activity("SLA201", 50, [
    "Glen", "Banks", "Zeldin", "Shaw", "Other"], ["Numen", "Richards", "Singer"]))
activityList.append(activity("SLA291", 50, [
    "Lock", "Banks", "Zeldin", "Singer"], ["Numen", "Richards", "Shaw", "Tyler"]))
activityList.append(activity("SLA303", 60, [
    "Glen", "Zeldin", "Banks" "Other"], ["Numen", "Singer", "Shaw"]))
activityList.append(activity("SLA304", 25, [
    "Glen", "Banks", "Tyler"], ["Numen", "Singer", "Shaw", "Richards", "Uther", "Zeldin"]))
activityList.append(activity("SLA394", 20, [
    "Tyler", "Singer"], ["Richards", "Zeldin"]))
activityList.append(activity("SLA449", 60, [
    "Tyler", "Singer", "Shaw"], ["Zeldin", "Uther"]))
activityList.append(activity("SLA451", 100, [
    "Tyler", "Singer", "Shaw"], ["Zeldin", "Uther", "Richards", "Banks"]))

roomList = []
roomList.append(room("Roman 216", 30))
roomList.append(room("Slater 003", 45))
roomList.append(room("Roman 201", 50))
roomList.append(room("Beach 201", 60))
roomList.append(room("Frank 119", 60))
roomList.append(room("Beach 301", 75))
roomList.append(room("Loft 206", 75))
roomList.append(room("Loft 310", 108))
roomList.append(room("Logos 325", 450))

def return_activityList():
    return activityList

def return_roomList():
    return roomList

def return_timeList():
    return time

def return_Facilitators():
    return Facilitators


