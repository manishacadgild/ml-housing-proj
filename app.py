from flask import Flask
import os,sys
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing=HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("The loggin is working for first page")
    return "Starting Machine Learning Project"

if __name__=="__main__":
    
    app.run(debug=True)