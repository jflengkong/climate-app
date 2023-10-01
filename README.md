# SQLalchemy-Challenge
## Week 10 - UWA Data Analytics SQL Alchemy Challenge 

This week we were introduced to the use of Advanced SQL techniques and the use of Flask to create our own API. 

# Background 
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Content 
1. <b>`Output`</b> - All figures completed in Climate Starter Analysis
2. <b>`Resources`</b> -[`hawaii.sqlite`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite) and two csv files [`hawai_measurements.csv`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/Resources/hawaii_measurements.csv) , [`hawaii_stations.csv`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/Resources/hawaii_stations.csv)
3. <b>[`Flask Code`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/app.py)</b> - app.py. Python code for Flask "Climate App" 
4. <b>[`Jupyter Notebook`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/climate_starter.ipynb)</b> - Jupyter Notebook Climate analysis

# Part 1: Analysis 
<b>[`Jupyter Notebook`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/climate_starter.ipynb)</b>  

In this section, we used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database.  SQLAlchemy ORM queries, Pandas, and Matplotlib were used in this analysis. 

## Precipitation Analysis 
- <b> Find the most recent date in the data set.
- Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data and plot the results.
- Print the summary statistics for the precipitation data </b>

![PRCP](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/Output/fig1.png) 

## Station Analysis 
- <b> Design a query to calculate the total number of stations in the dataset.
- <b> Design a query to find the most-active stations and using the most active station ID (USC00519281) , calculate the lowest, highest, and average temperatures.
- <b> Design a query to get the previous 12 months TOBS and plot on histogram </b> 

![TOBS](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/Output/fig2.png)

# Part 2: Designing a Climate App
<b>[`Flask Code`](https://github.com/jflengkong/sqlalchemy-challenge/blob/main/app.py)</b>

Following the initial analysis, a Flask API was created based on the queries just developed. 
The following routes were created:
  - Homepage
    -- List all the available routes 
  - /api/v1.0/precipitation
    -- A JSON of date and prcp in the last 12 months 
  - /api/v1.0/stations
    -- List of stations from the dataset 
  - /api/v1.0/tobs
    -- Dates and temperature observations of the most-active station for the previous year of data 
  - /api/v1.0/y-m-d(startdate)
    -- JSON list of the min, avg and max temp for a specified start range 
  - /api/v1.0/y-m-d(startdate)/y-m-d(enddate)
    -- JSON list of the min, avg and max temp for a specific start-end range 

# Reference
Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://doi.org/10.1175/JTECH-D-11-00103.1Links to an external site., measurements converted to metric in Pandas. 
