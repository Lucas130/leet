class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if not five:
                    return False
                else:
                    five -= 1
                ten += 1
            else:
                if five and ten:
                    ten -= 1
                    five -= 1
                elif five >=3:
                    five -= 3
                else:
                    return False
        return True




