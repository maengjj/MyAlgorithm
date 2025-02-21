import heapq

def calculate_satisfaction_and_days(N, M, K, priorities):
    max_heap = [-p for p in priorities]
    heapq.heapify(max_heap)
    
    satisfaction = 0
    days = 0 
    satisfaction_list = []

    while max_heap:
        current_priority = -heapq.heappop(max_heap)

        satisfaction = (satisfaction // 2) + current_priority
        satisfaction_list.append(satisfaction)
        days += 1

        current_priority -= M

        if current_priority > K:
            heapq.heappush(max_heap, -current_priority)

    return days, satisfaction_list

N, M, K = map(int, input().split())
priorities = [int(input()) for _ in range(N)]

days, satisfaction_list = calculate_satisfaction_and_days(N, M, K, priorities)

print(days)
for s in satisfaction_list:
    print(s)
