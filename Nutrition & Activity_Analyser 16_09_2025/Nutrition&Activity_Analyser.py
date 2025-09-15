import numpy as np
from requests import get

#assigning default variables for future use
nutrition_url=f"https://api.api-ninjas.com/v1/nutrition?query={{}}"

#calorie_burn_url=f'https://api.api-ninjas.com/v1/caloriesburned?activity={{}}'

#using my api key right now for practice right now maybe get removed in future
api_key='8gW7fEhuptixfADOroTg3g==wd1qPc86ZEDtBJAn'

#meta data for accessing data through api
head={"X-Api-Key":f'{api_key}'}

class Data:
    def __init__(self,activity,duration,food,age,weight,height):

        #assigning value for computation
        self.age=age
        self.activity=activity
        self.duration=duration
        self.food=food
        self.weight=weight
        self.height=height
    

    def bmi(self):
        # using bmi formula got from google
        return np.round(float(self.weight)/(float(self.height)/100)**2,2)
    # Cannot get much data as it need premium subscription


    def query(self,query):
        
        #Error Handling
        try:
            #got to know about headers through documentation
            info=get(nutrition_url.format(self.food),headers=head)

            #make list out from data to get useful info out of it
            info_json=info.json()
            data_query=np.array([])

            for i in range(0,len(info_json)):
                #collecting all values in numpy array for quick calculation
                data_query=np.append(data_query,info_json[i][f'{query}_total_g'])

            return np.round(np.sum(data_query),2)
        except Exception as e:
            #telling user what error occurred so can be managed during update
            print(f"An {e} occurred while getting food data")
            return None




    '''def calorie_burned(self):
        #https://www.verywellfit.com/pedometer-steps-to-calories-converter-3882595 for numpy array which can make calculation easier
        #still using above api for more precise calculation
        data_activity=np.array([])
        calorie_burn_info=requests.get(calorie_burn_url,headers=head)
        calorie_burn_info_json=calorie_burn_info.json()
        activity=self.activity.split(',')
        duratiom=self.duration.split(',')
        for i in range(0,len(activity)):
            data_activity=np.append(data_activity,calorie_burn_info_json[i]['total_calories'])'''
    #api is looking for proper wording so dropped the idea to code it further
    #only left with giving the info about calories burned


#taking user's input for calculation and giving results
age=input("Enter the activity")
height=input("Enter the height (in cm): ")
weight=input("Enter the weight (in kg): ")
activity=input("Enter the activity each separated with ',': ")
duration=input("Enter the duration of acitivity u did respectively in same format: ")
food=input("Enter the food u ate with portion being first then the food: ")
query=input("Enter what u wanna know about food (As per API for free u get only Fat,Carbohydrate,Protein, Fiber,Sugar)")


#defining person with atributes
person=Data(activity,duration,food.lower(),age,weight,height)


print(f'BMI : {person.bmi()}')
print(f'Total {query.capitalize()} in grams : {person.query(query.lower())}')
