import json

maxCount = {"count" : float('-inf'), "airport" : "" }
minCount = {"count" : float('inf'), "airport" : "" }

def maxMinCounts(count, airport):
    if count > maxCount["count"]:
        maxCount["count"] = count
        maxCount["airport"] = airport
    elif count < minCount["count"]:
        minCount["count"] = count
        minCount["airport"] = airport

with open("airlines.csv", 'r+') as file:
    results = []
    airports = {}
    text  =  file.read()
    for line in text.split('\n')[1:-1:]:
        a = line.replace('"',"").split(',')
        # print(a)
        # Check if airport code exists in airports dictionary
        if a[1]+ ','+a[2] in airports.keys():
            airports[a[1]+ ','+a[2]] += 1
            maxMinCounts(airports[a[1]+ ','+a[2]], a[1]+ ','+a[2])
        else:
            airports[a[1]+ ','+a[2]]  = 1
            maxMinCounts(airports[a[1]+ ','+a[2]], a[1]+ ','+a[2])



print(json.dumps(airports, indent=0))
print(maxCount["airport"], maxCount["count"])
print(minCount["airport"], minCount["count"])