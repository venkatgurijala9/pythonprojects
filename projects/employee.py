## read csv
import csv
import json


def create_json_file():
    data = []
    print("Initial data")
    print(data)
    with open("employee_data.csv", 'r') as cfile:
        csv_reader = csv.DictReader(cfile)
        print(csv_reader)
    
     ## Transform to json format   
        ##Loop through each record -- for, while or do while
        for row in csv_reader:
            # print(row)
            data.append(row)
    print("FInal data")
    print(data)

    json_data = json.dumps(data, indent=4)

    ## Load into JSON file
    with open("employee_data.json", 'w') as jfile:
        jfile.write(json_data)
        print("JSON File successfully written or loaded")


## analysis
"""
1. good employees
2. salary > 50,000
3. duplicates names
"""
def analysis():
    print("Analysis started")
    with open("employee_data.json", "r") as jfile:
        data = json.load(jfile)
        print(data)

        for doc in data:
            ### Check the good Person
            if doc["Feedback"]=="Good":
                print(f'{doc["First Name"]} is a very Good Person')
                 ## Check the salary is 50,000 or above
                if int(doc["Salary"]) > 50000:
                    print(f'{doc["First Name"]} salary is highly paid with {doc["Salary"]}')
            else:
                print(f"He is not good")

           

if __name__ == "__main__":
    # create_json_file()
    analysis()