import csv
import pandas as pd
class College():
    def __init__(self,college_id,college_name,course_type,city,fees,pin_code):
        self.college_id=college_id
        self.college_name=college_name
        self.college_type=college_type
        self.course_type=course_type
        self.city=city
        self.fees=fees
        self.pin_code=pin_code
    def register(self):
       with open('college.csv','a',newline="") as f1:
           w1=csv.writer(f1)
           data=[self.college_id,self.college_name,self.college_type,self.course_type,self.city,
                 self.fees,self.pin_code]
           w1.writerow(data)
    @classmethod
    def Display(self):
        with open('college.csv')as f2:
            data1=list(csv.reader(f2))
            #print(data1)
            for record in data1[1:]:
                if record[4]=="Mumbai" and record[2]=="Engineering":
                    for r in record:
                        print(r,end=" ")
            print()
    @classmethod
    def Remove(self,college_id):
        records=[]
        with open('college.csv','r') as f3:
            data=list(csv.reader(f3))
            for d in data:
                if d[0]!=college_id:
                    records.append(d)
        with open('college.csv','w',newline="") as f4:
            w1=csv.writer(f4)
            for record in records:
                w1.writerow(record)
            

while True:
    ch=input('a.Register, b.Display c.Remove')
    if ch=="a":
        college_id=input('Enter the College id:')
        college_name=input('Enter the College Name:')
        college_type=input('Enter the college type:')
        course_type=input('Enter the course type:')
        city=input('Enter the city:')
        fees=input('Enter the fees:')
        pin_code=input('Enter the pin_code:')
        std=College(college_id,college_name,college_type,city,fees,pin_code)
        std.register()
    elif ch=='b':
        College.Display()
    elif ch=="c":
        college_id=input('Enter college id:')
        College.Remove(college_id)
        
            
                

