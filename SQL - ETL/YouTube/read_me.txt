This project is meant to teach myself the ETL/ELT process through web scraping practices using python, database creation and management, and dashboarding capabalities to provide realtime data insights.
I am using the YouTube API web scrapers through Google (https://developers.google.com/youtube/v3) to gather information about one of my favorite learning and entertainment tools.
I hope to finally learn and show people that I am capable of creating a database, extract data using webscrapers, transform and load data into a database, maintain and optimize the database, use cron scheduling for command prompt scripting, create realtime dashboards, provide meaningful insights gracefully and present said insights, and make further improvements to each step of the pipeline.


Tools used:
- Python (3)
- Google YouTube v3 API
- PGAdmin4 (PostgreSQL locally stored server)
- ...


Important Documentation:
YouTube v3 API Documentation -> https://developers.google.com/youtube/v3/docs
Psycopg3 Documentation -> https://www.psycopg.org/psycopg3/docs/


Set up for project replication:
1. Clone repository on local disk
2. Create Google API Key for YouTube_v3
3. Open 'config.env' file in local disk directory
    a. Replace "YOUR API KEY HERE" with your actual API key provided by Google
    b. Move the config.env file into the main directory that stores the 'SQL - ETL/YouTube' folder structure for this project.
        i. This will allow the API key to be called in each folders functions when Scraper functions are called elsewhere.
4. Create PGAdmin4 server and database
    a. Replace the database information in the config.env file such as host, port, user, and database name
    
    *IMPORTANT -- if the .env file is not called config.env, github will not ignore when making any commits to your repository and your personal API key will be exposed if loading this project back to your own repository*


Folder structure of the project:
1. Scrapers
    - Scrapers are used to gather information from Google YouTube API for extraction purposes to the database.
2. Writers
    - Writers are used to take the pulled data from the 'Scrapers' and write this data into the database.
3. Lifters
    - Lifters are used to prep, clean, manipulate, and add complex formulas to the data being pulled for data analysis and visualization purposes.
*Note: Writers and Lifters are completely up to the individual as to which way they want to process the data being pulled. One could extract and transform first, then load into the database or load the data in first, then extract back out for manipulation and reloading/usage.
