class student:
    def read(self,roll,name):
        self.roll=roll
        self.name=name
        print("Students Read")
    def write(self):
        print("student roll",self.roll)
        print("student name",self.name)
        print("Students Write")
        
s1=student()
s2=student()
s1.read(23,'moni')
s1.write()
s2.read(11,'atshaya')
s2.write()


