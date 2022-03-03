import json
import numpy as np
count = 0
with open('timeseriesdata') as json_file:
    data = json.load(json_file)
    #for k in np.arange(1000):
       # if str((data['_items'][k]["userInputs"])) == 'None':
       #     count=count+1
      #      print(k)
     #       print("null")
    #print(count)
    ignored_values = set(["null", "", None])
    data = [elem for elem in data['_items'] if elem['doneChargingTime'] and  elem['userID']  not in ignored_values]
    for k in np.arange(1000):
        if str((data[k]["doneChargingTime"])) == 'None':
            count = count + 1
    print(count)


