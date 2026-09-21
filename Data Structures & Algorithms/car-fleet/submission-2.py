from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_arrival_times = []

        for position, speed in zip(position, speed):
            arrival_time = (target - position) / speed
            car_arrival_times.append( (position, arrival_time) )

        car_arrival_times.sort()
        car_arrival_times = [car_position_time_pair[1] for car_position_time_pair in car_arrival_times]

        fleet_count = 1 # revisit

        for i in range(len(car_arrival_times)):
            if i == 0: 
                continue
            if len(car_arrival_times) == 1:
                return fleet_count
            if car_arrival_times[-2] > car_arrival_times[-1]:
                fleet_count += 1
            car_arrival_times.append(max(car_arrival_times.pop(), car_arrival_times.pop()))

        return fleet_count


