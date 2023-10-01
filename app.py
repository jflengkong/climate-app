
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt, timedelta

from flask import Flask, jsonify

### Database Setup ###
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

 # Reflect an existing database into a new model 
Base = automap_base() 
Base.prepare(autoload_with=engine)

# Save references to classess names station and measurement 
measurement = Base.classes.measurement
station= Base.classes.station

# Create the date time variable for calculations 
most_recent_date = dt.date(2017, 8, 23)
date_between = most_recent_date - dt.timedelta(days=365)
                                               
app = Flask(__name__) 
app.json.sort_keys = False

# Link Python to the database by Creating SQLalchemy session
session = Session(engine)

# Create a Flask route to the homepage with available routes 
@app.route("/") 
def home(): 
    print("Available Routes") 
    return( 
    f" Welcome to the Climate API for vacation!<br/>" 
    f" Available Routes<br/>"
    f" /api/v1.0/precipitation<br/>"
    f" /api/v1.0/stations<br/>"
    f" /api/v1.0/tobs<br/>"
    f" /api/v1.0/y-m-d(startdate)<br/>"
    f" /api/v1.0/y-m-d(startdate)/y-m-d(enddate)<br/>"
    )

# Create a Flask route for the prcp 
@app.route("/api/v1.0/precipitation")
def precipitation(): 
    
    # Query session results to dictionary by using date as key and prcp as value 
    results = session.query(measurement.date, measurement.prcp).\
        filter(measurement.date >= date_between).all() 
    
    prcp = [{result[0]: result[1]} for result in results ]

    # Return a JSON representation of the dictionary 
    return jsonify(prcp)


# Create a flask to create a list of the stations 
@app.route("/api/v1.0/stations")
def stations(): 
    
    station_results = session.query(station.station).all()
    
    station_result = [result[0] for result in station_results]
        
    return jsonify(station_result)

# Second way to create list of stations with all information :) 
# @app.route("/api/v1.0/stations")
# def stations(): 
    
#     # Query session to gather all stations and information 
#     station_results = session.query(station.id, station.station, station.name, station.latitude, station.longitude, station.elevation).all()
    
#     all_stations = []
#     for station_id, station_code, station_name, station_latitude, station_longitude, station_elevation in station_results:
#         station_dict = {}
#         station_dict["ID"] = station_id
#         station_dict["Station"] = station_code
#         station_dict["Name"] = station_name
#         station_dict["Latitude"] = station_latitude
#         station_dict["Longitude"] = station_longitude
#         station_dict["Elevation"] = station_elevation
#         all_stations.append(station_dict)
    
#     # Return a JSON representation of list 
#     return jsonify(all_stations)

# Create a flask route for the TOBS 
@app.route("/api/v1.0/tobs")
def tobs():
    
    # Query to find the most activate station 
    active_stations = session.query(measurement.station, func.count(measurement.station)).\
        group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()
    
    # Create variable for most active station
    most_active_station = active_stations[0][0]   
    
    # Create a query for the dates and tobs for the most active station 
    tobs_results= session.query(measurement.date, measurement.tobs).\
    filter(measurement.date >= date_between).\
    filter(measurement.station == most_active_station).all() 
    
    # Create values and keys for results found 
    one_year_tobs = [{"date": result[0], "temperature": result[1]} for result in tobs_results]
    
    # Return jsonify result 
    return jsonify(one_year_tobs)

# Create a flask route for specified start date 
@app.route("/api/v1.0/<start>")
def temp_stats_start(start): 
    
    # Convert the inpurt start date to a datetime object 
    start_date = dt.datetime.strptime(start,"%Y-%m-%d")
    
    # Query to calculate TMIN, TAVG, TMAX for dates after and equal to input date 
    temp_stats = session.query(measurement.station, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).all()
        
    
    # Create a variable for temperature statistics and create a dictionary 
    temp_dict = {}
    for station_name, minimum, average, maximum in temp_stats:
        temp_dict= {"Station" : station_name,
                    "Start Date" : start_date,
                    "Minimum Temperature" : minimum,
                    "Average Temperature" : average,
                    "Maximum Temperature" : maximum}
        
    # Return a JSON representation of the dictionary     
    return jsonify(temp_dict)

#Create a flask route for specified start date and end date  
@app.route("/api/v1.0/<start>/<end>")
def temp_start_end(start,end): 
    
    #Convert the inpurt start date to a datetime object 
    start_date = dt.datetime.strptime(start,"%Y-%m-%d")
    end_date = dt.datetime.strptime(end,"%Y-%m-%d")
    
    # Query to calculate TMIN, TAVG, TMAX 
    temp_stats = session.query(measurement.station, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).\
        filter(measurement.date >= start_date).\
        filter(measurement.date <= end_date).all()
        
    # Create a variable for temperature statistics 
    temp_dict = {}
    for station_name, minimum, average, maximum in temp_stats:
        temp_dict= {"Station" : station_name,
                    "Start Date" : start_date,
                    "End Date" : end_date, 
                    "Minimum Temperature" : minimum,
                    "Average Temperature" : average,
                    "Maximum Temperature" : maximum}
        
    # Return a JSON representation of the dictionary       
    return jsonify(temp_dict)

# Check if the script is being run directly and  automatically reloads when code is changed. 
if __name__ == "__main__": 
    app.run(debug=True) 
    
# Close session 
session.close() 
    
    