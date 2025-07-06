# Introduction
This project is meant to teach myself the ETL/ELT process through building out API connections, database creation and management, and dashboarding capabalities to provide realtime data insights.
I am using the YouTube API web scrapers through [Google](https://developers.google.com/youtube/v3) to gather information about one of my favorite learning and entertainment tools.
I hope to finally learn how to and show people that I am capable of creating a database, extract data using APIs, transform and load data into said database, maintain and optimize the database, create realtime dashboards, and provide meaningful insights gracefully.

This project is meant to be very simple in practice, having almost no experience with data engineering, this should be replicable and easy for anyone who is trying to break into data engineering.

## Overview
### Documentation:
API Documentation - https://developers.google.com/youtube/v3/docs \
psycopg3 Documentation - https://www.psycopg.org/psycopg3/docs/index.html \
Metabase Documentation - https://www.metabase.com/docs/latest/


### Set up for Cloning Repository and using Google API key:
1. Create Google API Key for YouTube_v3
2. Clone repository on local disk
3. Set up PGAdmin4 server
4. Edit 'config.env' file in local disk directory 
    - open config.env file
    - replace -> scrapers_path="YOUR PATH TO LOCAL SCRAPER FOLDER" -- with the local path to the 'scrapers' folder where you downloaded the repo
    - replace -> API_KEY="your_api_key_here" -- with your actual API key given.
    - replace -> host, port, user, dbname1 (2,3,4) with your database information


## Phase One
Phase one of the project is meant to be an introduction to data engineering for those who are looking to break into the space and to have the groundwork laid out for future iterations of improvement.

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
    - random
    - string
3. Software
    - VSCode - IDE
    - PGAdmin4 - Database management
    - Metabase - Dashboarding
    - Docker - Container for Metabase

### Folder structure of the project:
1. Scrapers
    - Scrapers are the main tools used for searching, collecting, and interacting with data from the YouTube_v3 API.
    - These python files are used for individual functions designed to give users the ability to pull data easily and seamlessly together.
        - api_connection.py -> used for connection to Google's API tool.
        - categories.py -> used to pull categories from YouTube (not used each time, only ran once for database table).
        - search.py -> used to search for video or channel IDs based on arguments passed into the search() function.
        - collector_video.py -> used to collect video data from search() results.
        - collector_channel.py -> used to collect channel data from search() results or collector_video() results.
2. Writers
    - Writers are used to connect to and interact with the PGAdmin4 database to; create tables, insert data to tables, and query data from tables (without searching again using the API quota).
    - These python files are the main powerhouse of the code that will run daily.
        - writer.py -> used to write all the data to the PGAdmin4 database using search(), collector_video(), and collector_channel() in tandum.
        - write_categories.py -> used to write category data to PGAdmin4 database (not used each time, only ran once).
3. Lifters (in progress)
    - Lifters will be used to pull data from PGAdmin4 database and do more complex calculations and tasks that PostgreSQL isn't as efficient for, or doesn't have the tools necessary.
        *Thoughts are to use this on different algorithms for advanced data analytics, while all other functions should be handled by stored prodecures or views.*
        - pully.py -> used to extract data from the PGAdmin4 database and be dynamic to use on any database or table.
4. SQL Code
    - SQL Code are stored the views that are stored within the PGAdmin4 database, but shown for those replicating the project.
        - channel_score.sql -> used to find the average view per video rate for each video collected from a channel, compared to the average view per video for the entire channel to see trend over time and if any videos stand out compared to the average of the channel.
        - top_videos_current -> used to show which videos have the highest interaction scores based on the most recent record date.
        - videos_engagement_rate.sql -> used to show the engagement rate by video for the most recent record date, allowing for common comparisons across different video interaction sizes.
        - channels_efficiency_score.sql -> this view shows the efficiency score for each channel showing which channels are efficient at maintaining views and subscribers in terms of their upload frequency, with lower scores showing little to no turn-over rate for both viewership and subscribers per video.
        - channels_view_per_sub.sql -> this view shows each channels view per subscriber, seeing how many of these channels can convert their viewership to subscribers based on the amount of views they receive.
5. Additional files
    - The additional files in the folder structure are used for documentation purposes or system files used for the project setup when replicating.
        - .gitignore -> used to tell GitHub which files to ignore when committing to the repo.
        - config.env -> used to store all the sensative information regarding the project such as; API key, database username and password, etc.
        - patch_notes.txt -> used to document everything I did over the project incase I forget, also could be funny if I ever program after a drink or two.
        - read_me.md -> the file you are currently looking at (insert circular reference error joke here), basic read me file for project structure.

### DAGs & ERDs:
1. DAG - YouTube ETL
 
<img width="769" alt="YouTube ETL - DAG" src="https://github.com/user-attachments/assets/73b9fa6f-5262-4e9f-9969-da4680b687e2" />

2. ERD - DBS1
 
<img width="824" alt="Screenshot 2025-07-06 at 15 21 23" src="https://github.com/user-attachments/assets/d735ac75-1f8e-4a6a-a43d-f2a866ef696a" />


### Dashboard:
1. Videos
 
![videos_dashb](https://github.com/user-attachments/assets/a7bbcbd4-5c2c-4258-8d5c-7f28c8fec338)


2. Channels
 
![channels_dashb](https://github.com/user-attachments/assets/cac288b3-cdaa-4516-9917-9f28607d6dbc)
   
