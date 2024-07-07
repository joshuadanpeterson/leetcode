class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the preferences of students
        count0 = students.count(0)
        count1 = students.count(1)

        # Iterate through the sandwiches
        for sandwich in sandwiches:
            # If the sandwich is 0 and there are students who prefer 0
            if sandwich == 0 and count0 > 0:
                count0 -= 1
            # If the sandwich is 1 and there are students who prefer 1
            elif sandwich == 1 and count1 > 0:
                count1 -= 1
            # If there are no students who prefer the sandwich
            else:
                break

        # Return the number of students who haven't eaten
        return count0 + count1