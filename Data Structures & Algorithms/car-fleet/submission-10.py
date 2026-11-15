class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        time_stack = []

        for p, s in sorted(cars, reverse=True):
            time_to_target = (target - p) / s
            time_stack.append(time_to_target)
            if len(time_stack) > 1 and time_stack[-1] <= time_stack[-2]:
                time_stack.pop()
            
        return len(time_stack)