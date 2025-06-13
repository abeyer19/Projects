This project is meant to teach myself the ETL/ELT process through web scraping practices using python, database creation and management, and dashboarding capabalities to provide realtime data insights.
I am using the YouTube API web scrapers through Google (https://developers.google.com/youtube/v3) to gather information about one of my favorite learning and entertainment tools.
I hope to finally learn and show people that I am capable of creating a database, extract data using webscrapers, transform and load data into a database, maintain and optimize the database, use cron scheduling for command prompt scripting, create realtime dashboards, provide meaningful insights gracefully.


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
3. Create 'config.env' file in local disk directory 
    a. open terminal
    b. cd path/to/your/directory
    c. type in -> echo "API_KEY=your_api_key_here" > config.env
    *IMPORTANT -- .env file is not called config.env, github will not ignore when making any commits to your repository*


Folder structure of the project:
1. Scrapers
    - Scrapers are the main tools used for searching, collecting, and interacting data from the YouTube_v3 API.
    - The python files are used for individual functions designed to give users the ability to pull data easily and seamlessly together.
2. Writers
    - Writers are used to connect to and interact with PGAdmin4 database and create tables, insert data to tables, and query data from tables (without searching again using the API quota).
    - The python files are the main powerhouse of the code that will run daily.
3. Lifters (in progress)
    - Lifters will be used to pull data from PGAdmin4 database and do more complex calculations and tasks that PostgreSQL isn't as efficient for, or have the tools necessary.
        - Thoughts are to use this on different algorithms for advanced data analytics.