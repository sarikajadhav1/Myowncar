import pickle
import json
import config
import numpy as np

class  CarPrice():
    
    def __init__(self,user_data):
        
        self.user_data = user_data
        self.model_file_path = config.MODEL_FILE_PATH
        self.proj_file_path = config.PROJECT_FILE_PATH
        
    def load_saved_data(self):
        
        with open (self.model_file_path,"rb") as f:
            self.model = pickle.load(f)
        
        with open ( self.proj_file_path,"r") as f:
            self.proj_data = json.load(f)
            
    def get_pred_price(self):
        
        self.load_saved_data()

        gear = self.user_data["gear"]
        fuel = self.user_data["fuel"]
        make = self.user_data["make"]
        
        gear = self.proj_data["gear"][gear]
        
        fuel = "fuel_"+fuel
        fuel_index = self.proj_data["columns"].index(fuel)

        make = "make_"+make
        make_index = self.proj_data["columns"].index(make)

        col_count = len(self.proj_data["columns"])
        test_array = np.zeros(col_count)
        test_array[0] = eval(self.user_data["year"])
        test_array[1] = eval(self.user_data["mileage"])
        test_array[2] = eval(self.user_data["hp"])
        test_array[3] = gear
        test_array[make_index]  = 1
        test_array[fuel_index]  = 1
        print(test_array)

        predicted_price = np.around(self.model.predict([test_array])[0],3)
        print("Predicted Price :",predicted_price)
        return predicted_price
    
if __name__ == "__main__":
    obj = CarPrice()
    obj