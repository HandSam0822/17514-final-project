# MyCMU
> A platform that is exclusive to CMU students and faculty. Our goal is to connect CMU students and alumni in various ways. We plan to provide 4 main features that our target users probably care about the most, they are 1. CMU Course, 2. CMU Housing, 3. CMU Career, 4. CMU Match. 


## CMU Course (Liao)
Rather than leaving only the score on the FCE. We want to build a platform for students to share their detailed reviews on courses. We hope that the CMU Course could provide a better User Interface, User Experience, and information sharing compared to CMU FCE. Students can be easier to collect the course information needed. 

Expected outlook

Implementation steps: 
1. Download csv file from FCE after login with andrew id
2. Use tool from [ScottyLabs Repo](https://github.com/ScottyLabs) to call the api
3. Render result at backend & send data to front end


## CMU Career (Elaine)
Unlike handshake that focuses on feeding information on jobs or each department’s career service that shares career information only for their department. CMU career focuses more on connecting CMU alumni and CMU students without the department boundary. In CMU careers, Alumni could post job or referral opportunities. Students could connect with alumni through direct messages. 

Expected Outlook
              

## Global feature (on hold)
To encourage users to use the website, we want to introduce Award Mechanism

- Award Mechanism  
Users could get credit scores through some actions to help the platform and users grow
Encouraged actions include:
Decorate your account by providing more personal info to let others know you better. For example: telling people your habits, favorite playlist, the value of life, relationship status, etc.
Provide informative data points such as experience in course/internship/housing/entertainment

- Premium Services  
Users need higher credit scores to unlock advanced features
What kind of features requires scores to unlock?
Direct message (DM)
Create private club 
Referral request


## Tech Stack  
We plan to host the backend service with Django because we want to apply what we learn from the courses. To improve the performance and the usability of our web application, we would probably introduce Ajax or some frontend framework such as React.js. Besides, some external package such as Bootstrap is expected to be used to simplify UI design.
 

## Database's Schma Design  
Reference to [db diagram](https://dbdiagram.io/d/62328ced0ac038740c4a8e03), and feel free to edit it.  

## API design
Reference the [route table](./route_table.md)

## Team Member
Kimberly Huang hsinyah@andrew.cmu.edu  
Elaine Ku yku@andrew.cmu.edu  
Shousan Liao shousanl@andrew.cmu.edu   

## References  
[airbnb photo](https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&date_picker_type=flexible_dates&search_mode=flex_destinations_search&search_type=filter_change&tab_id=home_tab&flexible_trip_lengths%5B%5D=seven_days_starting_long_weekend&location_search=MIN_MAP_BOUNDS&category_tag=Tag%3A5348)  
[CMB photo](https://techcrunch.com/2018/12/11/coffee-meets-bagel-goes-anti-tinder-with-a-redesign-focused-on-profiles-conversations/)


