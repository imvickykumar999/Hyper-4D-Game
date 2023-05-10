
import json, sys

try:
	data = sys.argv[1]
except:
	data = 'new'
        
path = f"worlds/{data}.json"

def world():
    with open(path,"w") as of:
        json.dump({"position": []}, of)

world()
