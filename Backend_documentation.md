### 1. <br />
**path: "career_post", views.get_all_career_post_action, name='career_post'** <br />
desc: get all the career post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['type'] = the type of the post <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['post'] = all the post <br />

### 2. <br />
**path: "edit_career_post", views.edit_career_post_action, name='edit_career_post'** <br />
desc: edit career post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id that need to be edited <br />
request['post_text'] = the post text <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />

### 3. <br />
**path: "edit_career_comment", views.edit_career_comment_action, name='edit_career_comment'** <br />
desc: edit career comment by post id & comment id <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['comment_id'] = the comment id <br />
request['comment_text'] = the comment text <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 4. <br />
**path: "create_career_post", views.create_career_post_action, name='create_career_post'** <br />
desc: create career post <br />
**request:**  <br />
request['user_id'] = the request user id <br />
request['post_text'] = the post text <br />
request['type'] = type of the career post <br />
request['company_name'] = the company name <br />
request['job_title'] = job title of the post <br />
request['location'] = location of the career(non-necessary) <br />
request['visa_sponsor'] = visa sponsor of the career(non-necessary) <br />
 
**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 5. <br />
**path: "create_career_comment", views.create_career_comment_action, name='create_career_comment'** <br />
desc: create career post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['comment_text'] = the comment text <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 6. <br />
**path: "get_follow_career_post", views.get_follow_career_post_action, name='get_follow_career_post'** <br />
desc: get all following career post <br />
**request:** <br />
request['user_id'] = the request user id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['post'] = all the post <br />

### 7. <br />
**path: "delete_career_post", views.delete_career_post_action, name='delete_career_post'** <br />
desc: get all following career post <br />
**request:**
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['post_id'] = the post id that need to be delete <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 8. <br />
**path: "delete_career_comment", views.delete_career_comment_action, name='delete_career_comment'** <br />
id = id of career post <br />
desc: create career post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['comment_id'] = the comment id that need to be delete <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 9. <br />
**path: "send_message/<id>", views.send_message_action, name='send_message'** <br />
id: the user_id of the receiver
desc: send message to another user <br />
**request:** <br />
request['user_id'] = the request user id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 10. <br />
**path: "message/<id>", views.get_receive_messages_action, name='get_messages'** <br />
id: the user_id of message sender
desc: get messages send to user from <id> <br />
**request:** <br />
request['user_id'] = the request user id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['message'] = messages <br />

### 11. <br />
**path: "get_send_message/<id>", views.get_send_message_action, name='get_send_messages'** <br />
desc: get all messages send by user to other user <br />
**request:** <br />
request['user_id'] = the request user id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['message'] = messages <br />

### 12. <br />
**path: "delete_message", views.delete_message_action, name='delete_message'** <br />
desc: get all messages from a specific user to this user <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['message_id'] = the id of the message that need to be delete <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />

### 13. <br />
**path: "get_profile/<id>", views.get_profile_action, name='get_profile'** <br />
id: the user id of the profile need to be queried <br />
desc: get all profile info of the specific user <br />
**request:** <br />
request['user_id'] = the request user id <br />

**response:** <br />
response['profile'] = profile of the user <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 14. <br />
**path: "edit_profile", views.edit_profile_action, name='edit_profile'** <br />
desc: edit the profile info of the specific user <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['full_name'] = profile full name <br />
request['user_name'] = profile user name <br />
request['points'] = user points <br />
request['location'] = user location <br />
request['bio'] = profile bio <br />
request['picture'] = profile picture directory <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />
 
 
### 15. <br />
**path: "get_course", views.get_course_action, name='get_course'** <br />
desc: get all the course information from the FCE <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['course_num'] = the course number of the query course <br />
request['course_name'] = the course name of the query course <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['course'] = all the course information <br />

 ### 16. <br />
**path: "get_course_post", views.get_course_post_action, name='get_course_post'** <br />
desc: get all the course post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['course_number'] = the course number of the post <br />
request['department'] = the course department of the post <br />
request['course_name'] = the course name of the post <br />
request['post_id'] = the post id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br />
response['user'] = current user info <br />
response['post'] = all the post <br />

### 17. <br />
**path: "edit_course_post", views.edit_course_post_action, name='edit_course_post'** <br />
desc: get the course post with specific id <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />
                                      

### 18. <br />
**path: "create_course_post", views.create_course_post_action, name='create_course_post'** <br />
desc: create a new course post <br />
**request:** <br />
request['user_id'] = the request user id <br />=

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />


### 19. <br />
**path: "create_course_comment", views.create_course_comment_action, name='create_course_comment'** <br />
desc: create a course comment <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['comment_text'] = the comment text <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />
                                      
                                      
### 20. <br />
**path: "get_follow_course_post", views.get_follow_course_post_action, name='get_follow_course_post'** <br />
desc: get the user's following course posts <br />
**request:** <br />
request['user_id'] = the request user id <br />=

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['error'] = error message <br /> 
response['user'] = current user info <br />
response['post'] = course post <br />
 
 
 ### 21. <br />
**path: "delete_course_post", views.delete_course_post_action, name='delete_course_post'** <br />
desc: get the user's following course posts <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />
 
### 22. <br />
**path: "edit_course_comment", views.edit_course_comment_action, name='edit_course_comment'** <br />
desc: edit course comment by post id & comment id <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['course_post_id'] = the post id <br />
request['course_comment_id'] = the comment id <br />
request['course_comment_text'] = the comment text <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />

### 23. <br />
**path: "delete_course_comment", views.delete_course_comment_action, name='delete_course_comment'** <br />
id = id of course post <br />
desc: delete course post <br />
**request:** <br />
request['user_id'] = the request user id <br />
request['post_id'] = the post id <br />
request['course_comment_id'] = the comment id that need to be delete <br />

**response:** <br />
response['status'] = 200(ok)/ 404(error) <br />
response['user'] = current user info <br />
response['error'] = error message <br />