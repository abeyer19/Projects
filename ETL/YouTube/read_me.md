# Introduction
This project is meant to teach myself the ETL/ELT process through web scraping practices using python, database creation and management, and dashboarding capabalities to provide realtime data insights.
I am using the YouTube API web scrapers through [Google](https://developers.google.com/youtube/v3) to gather information about one of my favorite learning and entertainment tools.
I hope to finally learn and show people that I am capable of creating a database, extract data using webscrapers/APIs, transform and load data into a database, maintain and optimize the database, use cron scheduling for command prompt scripting, create realtime dashboards, provide meaningful insights gracefully.

This project is meant to be very simply in practice, having almost no experience with data engineering, this should be replicable and easy for anyone (including myself) who is trying to break into data engineering.

## Overview
### Documentation:
API Documentation - https://developers.google.com/youtube/v3/docs \
psycopg3 Documentation - https://www.psycopg.org/psycopg3/docs/index.html \
Metabase Documentation - https://www.metabase.com/docs/latest/


### Set up for Cloning Repository and using Google API key:
1. Create Google API Key for YouTube_v3
2. Clone repository on local disk
3. Edit 'config.env' file in local disk directory 
    - open config.env file
    - replace -> API_KEY="your_api_key_here" -- with your actual API key given.\
    *IMPORTANT -- if the .env file is not called config.env, github will not ignore when making any commits to your repository, if you want to call it something different you will need to add the file name to .gitignore*
4. Set up PGAdmin4 server
    - open config.env file
    - replace -> host, port, user, dbname1 (2,3,4) with your database information


### Folder structure of the project:
1. Scrapers
    - Scrapers are the main tools used for searching, collecting, and interacting with data from the YouTube_v3 API.
    - The python files are used for individual functions designed to give users the ability to pull data easily and seamlessly together.
        - api_connection.py -> used for connection to Google's API tool.
        - categories.py -> used to pull categories from YouTube (not used each time, only ran once for database table).
        - search.py -> used to search for video or channel id's based on arguments passed into the search() function.
        - collector_video.py -> used to collect video data from search() results.
        - collector_channel.py -> used to collect channel data from search() results or collector_video() results.
2. Writers
    - Writers are used to connect to and interact with PGAdmin4 database and create tables, insert data to tables, and query data from tables (without searching again using the API quota).
    - The python files are the main powerhouse of the code that will run daily.
        - writer.py -> used to write all the data to PGAdmin4 database using search.py, collector_video.py, and collector_channel.py in tandum.
        - write_categories.py -> used to write category data to PGAdmin4 database (not used each time, only ran once).
3. Lifters (in progress)
    - Lifters will be used to pull data from PGAdmin4 database and do more complex calculations and tasks that PostgreSQL isn't as efficient for, or doesn't have the tools necessary.
        *Thoughts are to use this on different algorithms for advanced data analytics, while all other functions should be handled by stored prodecures or views.*
        - pully.py -> used to extract data from the PGAdmin4 database and be dynamic to use on any database or table.     


## Phase One
Phase one of the project is meant to be an introduction to data engineering for those who are looking to break into the space, including myself, and to have the groundwork laid out for future iterations of improvement.


### Tools used:
1. Languages
    - Python
    - PostgreSQL
2. Packages
    - pandas
    - psycopg3
    - dotenv
    - sys
    - os
    - googleapiclient.discovery
3. Software
    - VSCode
    - PGAdmin4
    - Metabase
