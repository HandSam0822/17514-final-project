## Route Table 
| #  | Source | Method | Function to call | Destination  | Description |  Checkpoint |
|-------|-------|-------|-------|-------|-------|-------|
| **Root**   |             |     |        |   |       |      |
| 1 | /  |  GET | getHome() | /home or /login | route to /home if login, else /login |&#9744;|
| **Login**   |             |     |        |   |       |      |
| 1 | /login  | GET  | getLogin()  | /login  | render login.html |&#9744;|
| 2 | /login  | POST  | postLogin()  |  /{login} or /home  | if loginError, route to /login with error message, else /home | &#9744; |
| **Register**   |             |     |        |   |       |      |
| 1 | /rigister  | GET  | getRegister()  |  /register | render regiser.html  |&#9989;|
| 2 | /rigister  | POST  | postRegister()  |  /home or /register | if registerError, route to /register with error message, else /home |&#9989;|
| **Home**   |             |     |        |   |       |      |
| 1 | /home  | GET  | getGlobal()  |  /home or /login | if not login, route to /login, else render user.html  |&#9989;|
| 2 | /home  | POST  | - | /error | forbidden to do post request under /home |&#9989;|
| **Housing**  |      |   |     |  |   |   |
| 1 | /housing  | GET  | getHouse() | /housing | render housing.html |&#9744;|
| 2 | /housing  | POST  | postHouse() | /housing | create a housing post or leave comment on existing post  |&#9744;|
| 3 | /housing  | PATCH  | editHouse() | /housing | edit a housing post or comment |&#9744;|
| 3 | /housing  | DELETE  | deleteHouse() | /housing | delete a housing post or comment |&#9744;|
| **Course**  |      |   |     |  |   |   |
| 1 | /course  | GET  | getCourse() | /course | render course.html (user following's course) |&#9744;|
| 2 | /course/{course_id}  | GET  | getCourse(id) | /course/{course_id}  | render coursePage.html (visualized with data crawl from FCE!!!)|&#9744;|
| 3 | /course/{course_id}  | POST  | postCourse(id) | /course/{course_id}  | leave comment under the post |&#9744;|
| 4 | /course/{course_id}  | DELETE | deleteCourse(id) | /course | After deleting the post, goes go back to global course page |&#9744;|
| 5 | /course/{course_id}/edit  | GET | getEditCourse(id) | /course/{course_id}/edit  | pop up edit window of a post |&#9744;|
| 6 | /course/{course_id}/edit  | PATCH | editCourse(id) | /course/{course_id} | After editing the post, goes go back to /course/{course_id} |&#9744;|
| 7 | /course/search?q={keywords}  | GET  | getSearchCourse() | /course/search?q={keywords} | render courseSearch.html(maybe add advanced filter(date, deparment, credit, etc) if schedule allow ) |&#9744;|
| **Career** |      |   |     |  |   |   |
| 1 | /career  | GET  | getCareer() | /career | render career.html |&#9744;|
| 2 | /career  | POST  | postCareer() | /career | create a career post or leave comment on existing post
| **Profile**   |             |     |        |   |       |      |
| 1 | /{username}  | GET  | getProfile() | /{username} | render profile.html(view only) |&#9744;|
| 2 | /settings/profile | GET  | onClickEditProfile() | /settings/profile  | when click edit button, pop up profileEdit.html | &#9744; |
| 3 | /settings/profile | PATCH  | editProfile() | /{username} | edit profile data and rerender profile.html | &#9744; |
| **Match**  |      |   |     |  |   |   |
| 1 | /matches  | GET  | getMatches()| /matches | render matches.html |&#9744;|
| 2 | /matches  | POST  | postMatches()| /matches | send like to the crush and wait for the match |&#9744;|
| **Message**  |      |   |     |  |   |   |
| 1 | /messages  | GET  | getMessages()| /messages  | when # of chatroom = 0  |&#9744;|
| 2 | /messages{room_id}  | GET  | getMessages()| /messages{room_id}  | render message.html  |&#9744;|
| 3 | /messages{room_id}  | POST  | postMessages()| /messages{room_id} | send message to chatroom |&#9744;|
| 4 | /messages{room_id}  | DELETE  | deleteMessages()| /messages{room_id} | delete message of chatroom |&#9744;|


## Symbole table
|Status|Symbol|text|
|---|---|---|
|unfinish|&#9744;|`&#9744;`|
|unfinish|&#9989;|`&#9989;`|


---
Feel free to edit the table, but it is recommended to stick to same documentation convention to maintain consistency.

