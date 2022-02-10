# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 22:39:29 2021

Project: streamlit-test

# conda activate genius
# change to the project's root directory
# streamlit run app.py

pickle.format_version
'4.0'
"""

import streamlit as st
from streamlit import caching
import pickle
import numpy as np

def predict(x1, x2, x3):
    
    # get inputs
    X_new = [x1, x2, x3]
    X_new.extend([0,1,0,0,1,0,0,0,0,0,0,0])
    # change X_new to a 2-dim array
    X_new = np.reshape(X_new, (1, -1))
    
    # load model
    filename = r"model.pkl"
    [loaded_model, feature_names] = pickle.load(open(filename, 'rb'))
    
    # obtain PD predictions    
    y_pr = loaded_model.predict_proba(X_new)
    pd_raw = y_pr[0, 1]
    PD = round(pd_raw, 2)
    
    # obtain class predictions 
    y_p = loaded_model.predict(X_new)
    if y_p == 0:
        decision = 'APPROVED'
    elif y_p == 1:
        decision = 'REJECTED'    
    else:
        decision = 'ON-HOLD'
        
    return (PD, decision)



# =============================================================================
# interface
# =============================================================================

st.title("Streamlit Test - Prediction")

options = ['0', '1', '2', '3', '4']
points = [0, 1, 2, 3, 4]
x_dict = dict(zip(options, points))
x1 = st.selectbox(
        """
        Saving accounts
        """,
        options)
x1 = x_dict[x1]
x2 = st.number_input("Credit amount")
x3 = st.number_input("Duration") 


left_column, right_column = st.beta_columns(2)
pressed = right_column.button('Done!')
if pressed:
    
    (PD, decision) = predict(x1, x2, x3)
      
    f""" Your PD is {PD}!!  
    Your loan application is {decision}!"""
      
    caching.clear_cache()
    

    
    