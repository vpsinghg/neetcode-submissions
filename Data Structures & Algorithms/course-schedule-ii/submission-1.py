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
        queue = deque([])

        for i in range(numCourses):
            if dep_count_map[i] == 0:
                queue.append(i)
        result = []
        print(queue)
        
        while(queue):
            size = len(queue)
            next_courses = []
            while(size):
                course = queue.popleft()
                result.append(course)

                for next_course in dependency_map[course]:
                    dep_count_map[next_course] -= 1

                    if(dep_count_map[next_course] == 0):
                        next_courses.append(next_course)
                
                size -= 1
            
            for course in next_courses:
                queue.append(course)
        
        return result if len(result) == numCourses else []




        