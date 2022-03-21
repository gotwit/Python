# Find minimum time difference
# O(1) Time | O(1) Space

class Solution:
    def timeDifferece(self, times):
        # "00:00" | 1 day | (24 * 60) | 1440 mins | 24 hours
        visited = [False] * (24 * 60) # visited | seen time in minutes for 1 day or 24 hours

        for time in times:
            n = self.timeToInt(time)
            if visited[n]:
                return 0
            visited[n] = True
        
        prev = -1

        # minDiff = 0
        minDiff = (24 * 60) + 1 # 1441 as base line instead of 0 as smallest diff 0 doesnt make sense
        first = -1

        for i in range(0, len(visited)):
            if visited[i] == True:
                if prev != -1:
                    minDiff = min(minDiff, i - prev) # i - prev is new diff
                else:
                    first = i
                prev = i
        # case which covers time over midnight i.e 24 hrs ex: 00:03
        minDiff = min(minDiff, (first + 1440) - prev)

        return minDiff

    # Convert string time to integer
    def timeToInt(self, time):
        # "hh:mm" | len("hh:mm") is 5
        # [0:2] is hh | [3:5] is mm last index are ignored here.
        hours = time[0:2]
        minutes = time[3:5]
        # hours * 60 + minutes => minutes
        timeInMin = int(hours) * 60 + int(minutes)
        return timeInMin

sln = Solution()
times = ["00:03", "23:59", "12:03"]
result = sln.timeDifferece(times)
print(f"Minimum time difference {times} is", result)