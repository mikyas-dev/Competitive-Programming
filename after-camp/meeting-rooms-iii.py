class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        occupied_rooms = []
        cnt = defaultdict(int)
        for start, end in meetings:
            while len(occupied_rooms) > 0 and occupied_rooms[0][0] <= start:
                heapq.heappush(available_rooms, heapq.heappop(occupied_rooms)[1])
            if len(available_rooms) == 0:
                available_time, room = heapq.heappop(occupied_rooms)
            else:
                room = heapq.heappop(available_rooms)
                available_time = start
            cnt[room] += 1
            heapq.heappush(occupied_rooms, (max(start, available_time) + (end-start), room))
        max_meetings = max(cnt.values())
        return min(filter(lambda room: cnt[room] == max_meetings, range(n)))