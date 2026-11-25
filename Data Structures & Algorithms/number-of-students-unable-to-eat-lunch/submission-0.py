class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(sandwiches)

        counter = defaultdict(int)
        for s in students: counter[s] += 1

        for s in sandwiches:
            if counter[s] > 0:
                counter[s] -= 1
                result -= 1
            else:
                return result
        return result