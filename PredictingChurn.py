## Churn Prediction


import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/nagal/Desktop/Churn/TRAINED.sav','rb'))



#creating function for prediction

def churn_prediction(input_data):
    
    
    input_data_as_numpy_array=np.array(input_data)

    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'The person will be not be Churn'
    else:
        return 'The person will be Churn'


def main():
    
    
    #giving title
    st.title("Churn Prediction Web App")
    
    
    #getting the input data
    
    #'Age', 'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB'
    
    Age= st.text_input('Age of the customer')
    
    Subscription_Length_Months=st.text_input('Subscription Length in months')
    
    Monthly_Bill=st.text_input('Enter the monthly bill')
    
    Total_Usage_GB=st.text_input('Enter the Usage of data in GB')
    
    
    #code for prediction
    churn = ''
    
    if st.button('Churn Prediction'):
        churn = churn_prediction([Age,Subscription_Length_Months,Monthly_Bill,Total_Usage_GB])
    
    st.success(churn)
    
    
    
if __name__=='__main__':
    main()