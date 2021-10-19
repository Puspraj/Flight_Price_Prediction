from flask import Flask, render_template, request
from flask_cors import cross_origin
import pandas as pd
import numpy as np
import requests
import pickle
import jsonify
import sklearn

app = Flask(__name__)
model = pickle.load(open('rfr_flight_price.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == "POST":
        #Date of Journey
        dep_time = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").month)

        #Departure time
        Dep_hour = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(dep_time, format="%Y-%m-%dT%H:%M").minute)

        #Arrival time
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration time
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        #Total stops
        Toal_stop = request.form["Total_Stops"]
        
        #Airlines

        Airline = request.form["Airline"]
        if (Airline=="Jet Airways"):
            Jet_Airways=1
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="IndiGo"):
            Jet_Airways=0
            IndiGo=1
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Air_India"):
            Jet_Airways=0
            IndiGo=0
            Air_India=1
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Multiple_carriers"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=1
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0
        
        elif(Airline=="SpiceJet"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=1
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Vistara"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=1
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Air_Asia"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=1
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="GoAir"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=1
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Multiple_carriers_Premium_economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=1
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Jet_Airways_Business"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=1
            Vistara_Premium_economy=0
            Trujet=0

        elif(Airline=="Vistara_Premium_economy"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=1
            Trujet=0

        elif(Airline=="Trujet"):
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=1

        else:
            Jet_Airways=0
            IndiGo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            Air_Asia=0
            GoAir=0 
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        Source = request.form["Source"]
        if(Source=="Chennai"):
            source_Chennai=1
            source_Delhi=0
            source_Kolkata=0
            source_Mumbai=0
            
        elif(Source=="Delhi"):
            source_Chennai=0
            source_Delhi=1
            source_Kolkata=0
            source_Mumbai=0

        elif(Source=="Kolkata"):
            source_Chennai=0
            source_Delhi=0
            source_Kolkata=1
            source_Mumbai=0

        elif(Source=="Mumbai"):
            source_Chennai=0
            source_Delhi=0
            source_Kolkata=0
            source_Mumbai=1

        else:
            source_Chennai=0
            source_Delhi=0
            source_Kolkata=0
            source_Mumbai=0

        Source = request.form["Destination"]
        if(Source=="Cochin"):
            destination_Cochin=1
            destination_Delhi=0
            destination_Hyderabad=0
            destination_Kolkata=0

        elif(Source=="Delhi"):
            destination_Cochin=0
            destination_Delhi=1
            destination_Hyderabad=0
            destination_Kolkata=0

        elif(Source=="Hyderabad"):
            destination_Cochin=0
            destination_Delhi=0
            destination_Hyderabad=1
            destination_Kolkata=0
        
        elif(Source=="Kolkata"):
            destination_Cochin=0
            destination_Delhi=0
            destination_Hyderabad=0
            destination_Kolkata=1

        else:
            destination_Cochin=0
            destination_Delhi=0
            destination_Hyderabad=0
            destination_Kolkata=0

        prediction = model.predict([[Journey_day, Journey_month, Dep_hour, Dep_min,
                                    Arrival_hour, Arrival_min, dur_hour, dur_min,
                                    Toal_stop, Jet_Airways, IndiGo, Air_India, Multiple_carriers,
                                    SpiceJet, Vistara, Air_Asia, GoAir, Multiple_carriers_Premium_economy,
                                    Jet_Airways_Business, Vistara_Premium_economy, Trujet,
                                    source_Chennai, source_Delhi, source_Kolkata, source_Mumbai,
                                    destination_Cochin, destination_Delhi, destination_Hyderabad,
                                    destination_Kolkata]])

        output = round(prediction[0],2)

        return render_template('index.html', prediction_text="Your flight price in Rs {}".format(output))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)







