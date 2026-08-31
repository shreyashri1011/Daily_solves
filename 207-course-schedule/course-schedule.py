class Solution(object):

    def canFinish(self, numCourses, prerequisites):

        adj = {course: [] for course in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)

        checked = set()

        for course in range(numCourses):

            if course in checked:
                continue

            stack = [(course, set())]

            while stack:

                cur_course, visited = stack.pop()

                # Cycle found
                if cur_course in visited:
                    return False

                # Already completely checked
                if cur_course in checked:
                    continue

                visited.add(cur_course)

                for pre in adj[cur_course]:
                    stack.append((pre, visited.copy()))

                # Remember this course
                checked.add(cur_course)

        return True