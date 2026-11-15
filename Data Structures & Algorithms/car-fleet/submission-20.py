class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        eta_stack = []

        for car_position, car_speed in cars:
            eta = (target - car_position) / car_speed
            eta_stack.append(eta)
            while len(eta_stack) > 1 and eta_stack[-1] <= eta_stack[-2]:
                eta_stack.pop()

        return len(eta_stack)
            