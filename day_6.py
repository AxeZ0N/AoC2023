import math
with open('input.txt') as f:
    race_durations = f.readline().strip().split(':')[1].strip().split()
    race_records = f.readline().strip().split(':')[1].strip().split()

race_list = [(int(t),int(d)) for t,d in zip(race_durations,race_records)]

boat_init_vel = 0
boat_accel = 1

print(race_list)

def boatDistance(time_held, race_duration):
    final_accel = (boat_accel * time_held)
    time_left = race_duration - time_held

    distance_travelled = final_accel * time_left

    return distance_travelled if distance_travelled >= 0 else 0

beat_record_list = []

def partOne():
    for duration, record in race_list:
        beat_record_count = 0
        for i in range(0, duration + 1):
            bd = boatDistance(i, duration)

            if bd > record: beat_record_count += 1

        beat_record_list.append(beat_record_count)
        beat_record_count = 0

    print(beat_record_list)

    print(math.prod(beat_record_list))

def partTwo():
    race_time = ''.join([x for x in race_durations])
    race_record = ''.join([x for x in race_records])

    race_time = int(race_time)
    race_record = int(race_record)

    beat_record_count = 0

    for i in range(0, int(race_time) + 1):
        bd = boatDistance(i, race_time)

        if bd > race_record: beat_record_count += 1

    beat_record_list.append(beat_record_count)

    print(beat_record_list)

    print(sum(beat_record_list))






partTwo()
