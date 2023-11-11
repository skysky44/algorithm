from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight = 0
    while len(truck_weights)!=0:
        time+=1

        currentWeight -= bridge.popleft()

        if currentWeight + truck_weights[0] <= weight:
            currentWeight+= truck_weights[0]
            bridge.append(truck_weights.popleft())

        else: 
            bridge.append(0)
            
    time += bridge_length
    
    return time
    
# 문제 설명이 조금 부족

# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     bridge = deque([])
#     truck_weights = deque(truck_weights)
#     sec = 0
#     while truck_weights or bridge:
        
#         if (sum(bridge) + truck_weights[0]) > weight or (len(bridge)+1) > bridge_length:       
#             if bridge:
#                 bridge.popleft()
#                 sec += 1

#         else:
#             while (sum(bridge) + truck_weights[0]) <= weight and (len(bridge)+1) <= bridge_length:
#                 temp = truck_weights.popleft()
#                 bridge.append(temp)
#                 sec += 1
            
#     answer = sec
#     return answer

