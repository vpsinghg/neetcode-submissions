class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # course -> prerequisites
        adjacency_list = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)

        visited = [False] * numCourses
        visiting = set()  # courses currently in the DFS path
        sol = []

        def dfs(course):
            # Cycle detected
            if course in visiting:
                return False

            # Already completely processed
            if visited[course]:
                return True

            visiting.add(course)

            for prereq in adjacency_list[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited[course] = True

            # Add after prerequisites
            sol.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return sol