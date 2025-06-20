This project is meant to teach myself the ETL/ELT process through web scraping practices using python, database creation and management, and dashboarding capabalities to provide realtime data insights.
I am using the YouTube API web scrapers through Google (https://developers.google.com/youtube/v3) to gather information about one of my favorite learning and entertainment tools.
I hope to finally learn and show people that I am capable of creating a database, extract data using webscrapers/APIs, transform and load data into a database, maintain and optimize the database, use cron scheduling for command prompt scripting, create realtime dashboards, provide meaningful insights gracefully.

This project is meant to be very simply in practice, having almost no experience with data engineering, this should be replicable and easy for anyone (including myself) who is trying to get a better understanding of how to break into data engineering.


Tools used:
1. Languages
    a. Python
    b. PostgreSQL
2. Packages
    a. pandas
    b. psycopg3
    c. dotenv
    d. sys
    e. os
    f. googleapiclient.discovery
3. Software
    a. VSCode
    b. PGAdmin4
    c. Metabase


Documentation:
API Documentation - https://developers.google.com/youtube/v3/docs
psycopg3 Documentation - https://www.psycopg.org/psycopg3/docs/index.html
Metabase Documentation - https://www.metabase.com/docs/latest/


Set up for Cloning Repository and using Google API key:
1. Create Google API Key for YouTube_v3
2. Clone repository on local disk
3. Edit 'config.env' file in local disk directory 
    a. open config.env file
    b. replace -> API_KEY="your_api_key_here" -- with your actual API key given.
    *IMPORTANT -- if the .env file is not called config.env, github will not ignore when making any commits to your repository, if you want to call it something different your will need to add the file name to .gitignore*
4. Set up PGAdmin4 server
    a. open config.env file
    b. replace -> "" -- with your database information
5. Set up cronjob in Terminal
    a. Open terminal
    b. Type "crontab -e"
    c. Provide cronjob schedule and save
    d. Check that cronjob is saved by typing "crontab -l"

Folder structure of the project:
1. Scrapers
    - Scrapers are the main tools used for searching, collecting, and interacting with data from the YouTube_v3 API.
    - The python files are used for individual functions designed to give users the ability to pull data easily and seamlessly together.
        a. api_connection.py -> used for connection to Google's API tool.
        b. categories.py -> used to pull categories from YouTube (not used each time, only ran once).
        c. search.py -> used to search for video or channel id's based on arguments passed into the search() function.
        d. collector_video.py -> used to collect video data from search.py results.
        e. collector_channel.py -> used to collect channel data from search.py results or collector_video results.
2. Writers
    - Writers are used to connect to and interact with PGAdmin4 database and create tables, insert data to tables, and query data from tables (without searching again using the API quota).
    - The python files are the main powerhouse of the code that will run daily.
        a. writer.py -> used to write all the data to PGAdmin4 database using search.py, collector_video.py, and collector_channel.py in tandum.
        b. write_categories.py -> used to write category data to PGAdmin4 database (not used each time, only ran once).
3. Lifters (in progress)
    - Lifters will be used to pull data from PGAdmin4 database and do more complex calculations and tasks that PostgreSQL isn't as efficient for, or have the tools necessary.
        - Thoughts are to use this on different algorithms for advanced data analytics.
        a. pully.py -> used to extract data from the PGAdmin4 database and be dynamic to use on any database or table.
