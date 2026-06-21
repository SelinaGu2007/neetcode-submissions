class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        maxf = max(task_count.values())
        idle = (maxf - 1) * n
        skipped = False

        for task, count in task_count.items():
            if not skipped and count == maxf:
                skipped = True
                continue
            idle -= min(maxf - 1, count)

        if idle > 0:
            total_time = len(tasks) + idle
        else:
            total_time = len(tasks)

        return total_time