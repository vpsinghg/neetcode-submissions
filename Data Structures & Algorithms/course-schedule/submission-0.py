from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        prereq_counts = [0] * numCourses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            prereq_counts[course] += 1

        q = deque(
            course
            for course in range(numCourses)
            if prereq_counts[course] == 0
        )

        courses_taken = 0

        while q:
            curr = q.popleft()
            courses_taken += 1

            for course in adjList[curr]:
                prereq_counts[course] -= 1

                if prereq_counts[course] == 0:
                    q.append(course)

        return courses_taken == numCourses