class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        final_score = 0

        for operation in operations:
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                record.append(record[-1] * 2)
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))
            print(record)

        while record:
            final_score += record.pop()

        return final_score