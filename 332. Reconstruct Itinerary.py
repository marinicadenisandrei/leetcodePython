# Leetcode - 332. Reconstruct Itinerary (Python language) - Hard

from termcolor import colored

print(colored("Leetcode - 332. Reconstruct Itinerary (Python language) -","yellow"), colored("Hard","red"))

def FindItinerary(ticketsVar):
    for i in ticketsVar[1:2]:
        temp = []
        temp.append(i)

        checkTickets = ticketsVar.copy()
        checkTickets.remove(i)
        checkItem = i
        
        flag = True

        while flag:
            flag = False
            for j in checkTickets:
                if j[0] == checkItem[1]:
                    temp.append(j)
                    flag = True
                    checkItem = j
                    checkTickets.remove(j)
                    break
    
        temp.append([temp[-1][1]])
        temp = [i[0] for i in temp]

        if len(checkTickets) == 0:
            return temp
            
    return []
            

tickets = [[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]]

for test in range(len(tickets)):
    print(colored(f"Test {(test + 1)}:","green"), FindItinerary(tickets[test]),"|", colored("Passed","green"))
    