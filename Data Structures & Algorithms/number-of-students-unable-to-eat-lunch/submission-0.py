'''

'''

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        nonMatchStudents = 0
        studentQueue = deque(students)
        sandwichesQueue = deque(sandwiches)

        while nonMatchStudents < len(sandwichesQueue):
            curStudent = studentQueue.popleft() 
            print(f'curStudent {curStudent}')

            print(curStudent == sandwichesQueue[0])
            if curStudent == sandwichesQueue[0]:
                sandwichesQueue.popleft()
                nonMatchStudents = 0

                if len(sandwichesQueue) == 0: 
                    return 0
            else: 
                studentQueue.append(curStudent)
                nonMatchStudents += 1 
            
            print(studentQueue)
            print(sandwichesQueue)
        
        return nonMatchStudents