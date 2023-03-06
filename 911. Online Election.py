class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        leader = persons[0]
        for i, time in enumerate(times):
            person = persons[i]
            vote_count[person] += 1
            if vote_count[person] >= vote_count[leader]:
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        low, high = 0, len(self.times) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.times[mid] == t:
                return self.leaders[mid]
            elif self.times[mid] < t:
                low = mid + 1
            else:
                high = mid - 1
        return self.leaders[high]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
