import csv
from collections import defaultdict

def ConvertToObject(filename):
	#Employee = defaultdict(list)
	Employee =[]	
	with open(filename, mode='r') as infile:
		reader = csv.DictReader(infile)
		for row in reader:
			Employee.append(row)
		
		
		
		
		#for row in reader:
			#for (k,v) in row.items():
				#Employee[k].append(v)
		#print (Employee)
		#for row in zip(*([key] + value for key, value in sorted(Employee.items()))):
			#print (*row)
            
		print (Employee[1])
ConvertToObject("/home/guest/Downloads/sample.csv")
