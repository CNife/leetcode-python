"""
1723. 完成所有工作的最短时间，困难
https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs/
"""


def minimum_time_required(jobs: list[int], k: int) -> int:
    n = len(jobs)
    sums = [0] * n
    result = 2 ** 31 - 1

    def dfs(u: int, used: int, curr_max: int) -> None:
        nonlocal result
        if curr_max >= result:
            return
        if u == n:
            result = curr_max
            return

        if used < k:
            sums[used] = jobs[u]
            dfs(u + 1, used + 1, max(curr_max, sums[used]))
            sums[used] = 0
        for i in range(used):
            sums[i] += jobs[u]
            dfs(u + 1, used, max(sums[i], curr_max))
            sums[i] -= jobs[u]

    dfs(0, 0, 0)
    return result


if __name__ == "__main__":
    assert minimum_time_required([3, 2, 3], 3) == 3
    assert minimum_time_required([1, 2, 4, 7, 8], 2) == 11
