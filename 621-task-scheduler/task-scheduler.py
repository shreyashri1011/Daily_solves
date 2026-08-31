class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts=Counter(tasks)
        max_heap=[]
        for count in task_counts.values():
            max_heap.append(-count)
        heapq.heapify(max_heap)
        time=0
        wait_queue=deque()
        while max_heap or wait_queue:
            time+=1
            if max_heap:
                current_task=heapq.heappop(max_heap)
                current_task+=1
                if current_task!=0:
                    wait_queue.append((current_task,time+n))
            if wait_queue and wait_queue[0][1]==time:
                heapq.heappush(max_heap,wait_queue.popleft()[0])
        return time