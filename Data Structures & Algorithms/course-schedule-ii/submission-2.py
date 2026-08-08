from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency_map = defaultdict(list)

        # dependency_count
        dep_count_map = defaultdict(int)

        for a, b in prerequisites:
            dep_count_map[a] += 1
            print(a, dep_count_map[a])
            dependency_map[b].append(a)

        # initial seed courses which don't have prereq
        queue = deque(course for course in range(numCourses) if dep_count_map[course] == 0)
        result = []

        while queue:
            size = len(queue)
            while size:
                course = queue.popleft()
                result.append(course)

                for next_course in dependency_map[course]:
                    dep_count_map[next_course] -= 1

                    if dep_count_map[next_course] == 0:
                        queue.append(next_course)

                size -= 1
        return result if len(result) == numCourses else []
