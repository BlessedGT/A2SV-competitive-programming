class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixsm = [0]
        for nm in nums:
            prefixsm.append(nm + prefixsm[-1])

        que = deque()
        ans = len(nums)+1

        for i in range(len(prefixsm)):
            while que and prefixsm[i] - prefixsm[que[0]] >= k:
                ans = min(ans,i-que.popleft())

            while que and prefixsm[i] <= prefixsm[que[-1]]:
                que.pop()
            que.append(i)

        return ans if ans != len(nums)+1 else -1
