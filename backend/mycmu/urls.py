from unicodedata import name
from django.contrib import admin
from django.urls import path, re_path, include
from mycmu import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login", views.login_action, name="login"),
    # course
    path("course", views.course_action, name='course'),
    path("course/<id>", views.course_action_by_id, name='course_action_by_id'),
    # course post
    path("course_post", views.course_post_action, name='course_post_action'),
    path("course_post/<id>", views.course_post_action_by_postid,
         name='course_post_action_by_postid'),

    # course post comment
    path("course_post_comment_by_postid/<id>", views.course_post_comment_action_by_postid,
         name="course_post_comment_action_by_postid"),
    path("course_post_comment_by_commentid/<id>", views.course_post_comment_action_by_commentid,
         name="course_post_comment_action_by_commentid"),


    # career post
    path("career_post_search", views.career_post_search, name='career_post_search'),
    path("career_post", views.career_post_action, name='career_post_action'),
    path("career_post/<id>", views.career_post_action_by_postid,
         name='career_post_action_by_postid'),

    # career post comment
    path("career_post_comment_by_postid/<id>", views.career_post_comment_action_by_postid,
         name="career_post_comment_action_by_postid"),
    path("career_post_comment_by_commentid/<id>", views.career_post_comment_action_by_commentid,
         name="career_post_comment_action_by_commentid"),

    # views.profile_action handles POST request on
    path("profile/<username>", views.profile_action, name='profile'),

    # message
    path("messages/<id>", views.messages_action, name='messages_action'),
    path("send_message/<id>", views.send_message_action, name='send_message'),
    path("delete_message/<id>", views.delete_message_action, name='delete_message'),

    # following posts
    path("follow_course_post", views.get_follow_course_post_action,
         name='get_follow_course_post'),
    path("follow_career_post", views.get_follow_career_post_action,
         name='get_follow_career_post'),


]

# imp for what you want to achieve.
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
