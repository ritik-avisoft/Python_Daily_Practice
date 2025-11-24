import csv
import json

# Part 1: Working with a Text File
with open("employees.txt", "w") as file:
    file.write("Ritik, HR\n")
    file.write("Raj, IT\n")
    file.write("Ashu, Finance\n")
    file.write("Karu, QA\n")
    file.write("Harsh, Testing\n")

# Read and print the entire file using read()
print("Reading entire file:")
print("****"*5)
with open("employees.txt", "r") as file:
    content = file.read()
    print(content)

# Read line-by-line using readline()
line_no =0
print("Reading line by line:")
with open("employees.txt", "r") as file:
    content = file.readlines()
    print("****"*5)
    for line in content:
      print(line.strip())
      
      line_no +=1
      print(f"line no {line_no} printed")
      print("-----"*5)

# Add 1 new employee using append mode
with open("employees.txt", "a") as f:
    f.write("Tanni, Marketing\n")

#Creating a csv file 
with open("employees.csv",'w',newline='') as file:
    writer=csv.writer(file) 
    writer.writerow(["Name","Department","Salary"])
    writer.writerow(["Ritik","HR",35000])
    writer.writerow(["Raj","IT",45000])
    writer.writerow(["Ashu","Finance",55000])
    writer.writerow(["Karu","QA",35000])
    writer.writerow(["Harsh","Testing",40000])

#reading the csv file and printing the data...
print("Reading CSV file:")
print("****"*5)
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)    
    for row in reader:
      print(f"Name: {row[0]}, Department: {row[1]}, Salary: {row[2]}")

# Converting CSV data to JSON format (emplpoyees.csv to employees.json)...
print("\nConverting CSV to JSON:")

with open("employees.csv","r") as f:
  #  #  reader=csv.DictReader(f)
  #   reader=csv.reader(f)
  #   next(reader)
  #   data={"employees":[]}
  #   for i in reader:
  #     #   print(i)
  #     data=["employees"].append({
  #           "name":i[0],
  #           "department":i[1],
  #           "salary":int(i[2])})

  reader=csv.DictReader(f)
  data={"employees":[]}
  for row in reader:
    data["employees"].append({
        "name": row["Name"],
        "department": row["Department"],
        "salary": int(row["Salary"])
    })

with open("employees.json","w") as f:
    json.dump(data,f,indent=4)
    print("----"*12)
    print("Data successfully written to employees.json")
    print("----"*12)
# Loading json file and printing...
print("Loading JSON file:")
with open("employees.json","r") as f:
    data=json.load(f) 
    print(json.dumps(data,indent=4))
    print("****"*5)

#creating a list of emp earning more than 40000
high_earners = [emp for emp in data["employees"] if emp["salary"] > 40000] 
print("Employees earning more than 40000:")
for emp in high_earners:
    print(f"Name: {emp['name']}, Salary: {emp['salary']}")
print("****"*5)
# Creating a dictionary {employee_name: salary}
salary_dict = {emp["name"]: emp["salary"] for emp in data["employees"]}
print("Employee Salary Dictionary:")
print(salary_dict)

print(f"{"-"*20}\nEnd of Assignment\n{"-"*20}")