#!/usr/bin/env python
# coding: utf-8

# In[33]:


class Vehicle():
    def __init__(self, type): 
        self.type = type # The Class Objects 
    def description(self):
        print("I'm a", self.type, "Vehicle")

# subclass
class Automobile(Vehicle):
    def __init__(self, type, year, make, model,doors, roof):
        super().__init__(type)    # The  Vehicle’s __init__() methods
        self.year = year
        self.model = model
        self.doors = doors
        self.roof = roof
    def description(self):
        print("Vehicle Type", self.type)
        print("Year", self.year)
        print("Model", self.model)
        print("Number of Doors", self.doors)
        print("Type of Roof", self.roof)
#  My inputs
vehicletype = input('What is the Vehicle Type?\n')
autoyear = input('What is the year?\n')
automake = input('What is the make?\n')
automodel = input('What is the model?\n')
autodoors = input('How many doors?\n')
autoroof = input('What type of roof?\n')

c = Automobile(vehicletype, autoyear, automake, automodel, autodoors, autoroof)

# Print Details
print(c.description())
    
    


        


# In[ ]:





# In[ ]:





# In[ ]:




