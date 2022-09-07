from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from mycmu.utils import _isCMUEmail, _userExist, _course_post_comment_serialize_helper, _course_serialize_helper, _career_post_comment_serialize_helper, _career_post_serialize_helper, _course_post_serialize_helper, _profile_serialize_helper,  _send_error
from mycmu.utils import *
from mycmu.services import google_validate_id_token
from datetime import datetime
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json
from mycmu.models import *
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import *
from django.db.models import Q
from django.utils import timezone

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def test2(request):
    try:
        print(request.GET)
        id = request.GET.get('id')
        print(id)
        return Response({"id": id}, HTTP_200_OK)
    except:
        return Response({"id": id}, HTTP_400_BAD_REQUEST)


""" The reason add @csrf_exempt annotation is because the frontend is
running on different port(3000) than backend(8000). It would trigger unsafe
'Cross-site request forgery'. Although we could silent this error in development status,
it is better solve it in a more safe and descent way.
"""

"""please do login verification here. If pass, sent a token"""


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_action(request):
    """ Create new user if user does not exist
    Create a Profile when creating a user
    Return the user and profile information

    :method POST
    :param request:
        :: first_name = login user's first name
        :: last_name = login user's last name
        :: email = login user's email
    :return:
        :: status = 200(OK) / 400(BAD REQUEST)
        :: token = token key
        :: id = user id
        :: first_name = login user's first name
        :: last_name = login user's last name
        :: username = login user's username
        :: email = login user's email
        :: last_login = last login time
        :: date_joined = data the user joined
        :: location = location info in the user profile
        :: bio = user profile bio
        :: user_point = user's current point
    """
    context = {}
    id_token = request.headers.get('Authorization')
    # validate the token is authorized
    google_validate_id_token(id_token=id_token)

    # data sent from Google, include <email>, <first_name>, <last_name>
    data = json.loads(request.body)

    # check CMU email

    if not _isCMUEmail(data["email"]):
        return _send_error('Please login with CMU email', HTTP_400_BAD_REQUEST)

    username = data["first_name"] + data["last_name"]
    now = timezone.now()
    user = _userExist(data["email"])

    if not user:
        user = User.objects.create_user(
            username=username,
            last_login=now,
            date_joined=now,
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"])
        user.save()
        profile = Profile.objects.create(
            user_id_id=user.id,
            created_at=now,
            location="Pttsburgh",
            bio="",
            user_point=0,
        )

        profile.save()
    else:
        user.last_login = now
        user.save()

    auth_user = authenticate(request, email=user.email)
    if not auth_user:
        return _send_error('Invalid Credentials', HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    profile = Profile.objects.filter(user_id=auth_user).last()
    context['status'] = 200
    context['token'] = token.key
    context["id"] = auth_user.id
    context['first_name'] = auth_user.first_name
    context['last_name'] = auth_user.last_name
    context['username'] = auth_user.username
    context['email'] = auth_user.email
    context['last_login'] = auth_user.last_login
    context['date_joined'] = auth_user.date_joined
    context['location'] = profile.location
    context['bio'] = profile.bio
    context['user_point'] = profile.user_point

    return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def course_action(request):
    """ GET all the course information fetched from FCE
    Return the course data

    :method GET
    :param request:
    :return:
        :: status = 200 (OK)
    """
    context = {}
    if request.method == "GET":
        print(request.user.id)
        print(request.user.first_name)
        course = Course.objects.all()
        context["course"] = _course_serialize_helper(course, many=True)
        return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def get_follow_career_post_action(request):
    """ Return all career_post that USER is following

    :method GET
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK)
        :: post = all the following career post
    """
    context = {}
    career_post = Profile.objects.filter(
        user_id=request.user).last().following_career_post.all()
    post_data = _career_post_serialize_helper(career_post, many=True)

    context['post'] = post_data
    return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def get_follow_course_post_action(request):
    """ Return all course_post that USER is following

    :method GET
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK)
        :: post = all the following course post
    """
    context = {}

    course_post = Profile.objects.filter(
        user_id=request.user).last().following_course_post.all()
    post_data = _course_post_serialize_helper(course_post, many=True)

    context['post'] = post_data
    return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def messages_action(request, id):
    """ Get the message between current user and USER w/ id=id

    :method POST
    :param request:
        :: user = USER that send the request
    :param id: the id of another USER
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
        :: message = all the messages between request user and another user w/ id=id (order by creation_time)
    """
    context = {}
    sender = request.user
    receiver = User.objects.filter(id=id).last()

    # check whether the user exist
    if not sender or not receiver:
        return _send_error('The user does not exist', HTTP_404_NOT_FOUND)

    # complex filter
    messages = Message.objects.filter(Q(from_user_id=sender, to_user_id=receiver) |
                                      Q(from_user_id=receiver, to_user_id=sender)).order_by("creation_time").all()

    # check whether the message exist
    if not messages:
        return _send_error("Message does not exist", HTTP_404_NOT_FOUND)

    context['message'] = message_serializer(messages, many=True)
    # context['receiver'] = profile_serializer(id)
    return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def send_message_action(request, id):
    """ Send a message to user with id=id

    :method POST
    :param request:
        :: user = USER that send the request
    :param id: the id of the USER that current user want to send message to
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
        :: message = message that the current user want to send to USER w/ id=id
    """
    context = {}
    data = json.loads(request.body)
    sender = request.user
    receiver = User.objects.filter(id=id).last()
    # check whether the user exist
    if not sender or not receiver:
        return _send_error('The user does not exist', HTTP_404_NOT_FOUND)

    new_message = Message(
        from_user_id=sender, to_user_id=receiver, message=data['message_text'])
    new_message.save()
    context['message'] = message_serializer(new_message, many=False)
    # context['receiver'] = profile_serializer(id)
    return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def delete_message_action(request, id):
    """ Delete the message by message id

    :method POST
    :param request:
        :: user = USER that send the request
    :param id: the message id of the message that user want to delete
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND) / 400 (BAD REQUEST)
    """
    context = {}
    user = request.user

    messages = Message.objects.filter(id=id).last()
    if not messages:
        return _send_error("Message does not exist", HTTP_404_NOT_FOUND)
    if user != messages.from_user_id:
        return _send_error("User does not own this message", HTTP_400_BAD_REQUEST)
    messages.delete()
    return Response(context, HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def profile_action(request, username):
    """ Profile related functions

    ** Get the profile info
    :method GET
    :param request:
        :: user = USER that send the request
    :param username: username of the profile
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
        :: profile = profile information
        :: is_following = whether the user is following this profile
        :: is_self = whether the profile belongs to request user
    ==========================================================================
    ** Edit the profile info or Follow/Unfollow a profile
    :method POST
    :param request:
        :: user = USER that send the request
        :: username = username of the profile
        :: image = image of the profile
        :: location = location of the profile
        :: bio = bio of the profile
    :param username: username of the profile
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
    """
    context = {}
    # check follow/unfollow and isSelf status
    # return profile data to frontend
    target_user = User.objects.filter(username__iexact=username).last()

    # check whether the user exist
    if not target_user:
        return _send_error("no such user", HTTP_404_NOT_FOUND)

    is_following = False
    is_self = True
    followers = Profile.objects.filter(user_id=request.user).last().followers
    if request.user != target_user:
        is_self = False
        is_following = followers.filter(id=target_user.id).exists()

    if request.method == "GET":
        context['profile'] = _profile_serialize_helper(
            Profile.objects.filter(user_id=target_user).last())
        context['is_following'] = is_following
        context['is_self'] = is_self
        context['email'] = target_user.email
        return Response(context, status=HTTP_200_OK)

    elif request.method == "POST":
        # situtuation 1: click edit profile button
        user = request.user
        if not user:
            return _send_error("no such user", HTTP_404_NOT_FOUND)

        if user.username == username:
            profile = Profile.objects.filter(user_id=request.user).last()
            data = json.loads(request.body)
            user.username = data['username']
            user.save()
            image = None if not data["image"] else base64ToImageInstance(
                data["image"], user.username)

            """
            user could have only one profile_picture stored in db
            I set the file name as <username>.png However, if same file 
            exist in FileField, django would append 7 random character 
            ex SamGGAx82sd8.png, which isn't what I desired, 
            I decide to delete original file before saved.
            Another seemingly feasible solution is place
            'django_cleanup.apps.CleanupConfig', after your app in 
            settings.py' -> INSTALLED_APPS 
            """
            if image:
                profile.profile_picture.delete()
                profile.profile_picture = image

            # profile.user_point = data['points']
            profile.location = data['location']
            profile.bio = data['bio']

            profile.created_at = data['created_at']
            profile.save()

            return Response(context, HTTP_200_OK)

        # situtuation 2: follow/unfollow an user
        else:
            if is_following:  # remove from following
                followers.remove(target_user)
            else:
                followers.add(target_user)

            return Response(context, status=HTTP_200_OK)


"""Get all course data to allow frontend populate the search table
Since the filtering job is done in frontend, there's no POST request
to filter data.

Also, since course data is in download from FC2 and stored in database,
users cannot do PUT or DELETE request
"""


@csrf_exempt
@api_view(["GET"])
def course_action_by_id(request, id):
    """ Course post related functions
    ** Given a course id, return all coursepost that has mentioned that course
    :method GET
    :param request:
        :: user = USER that send the request
    :param id: the course id
    :return:
        :: status = 200 (OK)
        :: post = course posts that realated to course_id
    """
    context = {}
    # check whether that course exist
    current_course = Course.objects.all().filter(id=id)
    if not current_course:
        return _send_error('course does not exist', HTTP_400_BAD_REQUEST)

    # get related posts
    course_post = CoursePost.objects.all().filter(course_id=id)

    post = _course_post_serialize_helper(course_post, many=True)
    context['post'] = post
    return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def course_post_action(request):
    """ Course post related functions

    ** Get the course post
    :method GET
    :param request:
        :: user = USER that send the request
        :: username = post user for searching
        :: title = course post title to search
        :: text = text in course post to search
    :return:
        :: status = 200 (OK)
        :: post = course posts that meet the filter requirement
        :: is_following = whether the user is following this post
    ==========================================================================
    ** Create a new course post
    :method POST
    :param request:
        :: user = USER that send the request
        :: course_post_title = title of the post
        :: course_post_text = text of the course
        :: course_number = course number that the post belongs to
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}
    if request.method == "GET":
        param = request.GET
        title, text, username, sort = param.get(
            "title"), param.get("text"), param.get("username"), param.get("sort")
        course_post = CoursePost.objects.all().order_by("update_time")
        if title and not title.isspace():
            course_post = course_post.filter(
                course_post_title__icontains=title)

        if text and not text.isspace():
            course_post = course_post.filter(course_post_text__icontains=text)

        if username and not username.isspace():
            course_post = course_post.filter(
                course_post_user__username__icontains=username)

        # sort would be passed as one of the param. It's value could be
        # update_time, followers, name
        # if update_time, have to order_by update_time(in descending order)
        # if followers, the most followers post at top
        # if name, post title alphabetically on top (A...)
        if sort and not sort.isspace():
            if (sort == "update_time"):
                course_post = course_post.order_by("-update_time")
            elif (sort == "followers"):
                course_post = course_post.order_by("-number_of_follower")
            elif (sort == "name"):
                course_post = course_post.order_by("course_post_title")

        post = _course_post_serialize_helper(course_post, many=True)
        context['post'] = post
        """retrieve global post's following status to render corresponding icon"""

        # profile = Profile.objects.filter(user_id = request.user).last()
        # all_following = profile.following_course_post.all()
        # following_status = []
        # for p in course_post:
        #     following_status.append(True if p in all_following else False)

        # context["is_following"] = following_status
        return Response(context, status=HTTP_200_OK)

    if request.method == "POST":
        data = json.loads(request.body)
        if 'course_post_title' not in data:
            return _send_error('The post title should not be empty', HTTP_400_BAD_REQUEST)
        if 'course_post_text' not in data:
            return _send_error('The post text should not be empty', HTTP_400_BAD_REQUEST)
        user = request.user
        if not user:
            return _send_error('User does not exist', HTTP_400_BAD_REQUEST)
        # add user points

        if not data["course_number"] or data["course_number"] < "00000" and data["course_number"] > "99999":
            return Response({"error": "Course number must be 5 digit number"}, status=HTTP_400_BAD_REQUEST)

        # course = Course.objects.filter(id=data["course_id"]).last()
        course = Course.objects.filter(
            course_number=int(data["course_number"])).last()
        if not course:
            return Response({"error": "No such course"}, status=HTTP_400_BAD_REQUEST)
        new_post = CoursePost(course_id=course, course_post_title=data['course_post_title'], course_post_text=data['course_post_text'],
                              course_post_user=user, creation_time=timezone.now(), update_time=timezone.now(), number_of_follower=0)
        new_post.save()
        add_user_point(user, 3)
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST", "PUT", "DELETE"])
def course_post_action_by_postid(request, id):
    """ Course post related functions with post id

    ** Get the course posts
    :method GET
    :param request:
        :: user = USER that send the request
    :param id: course post id
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
        :: post = course posts with this post id
        :: following = whether the user is following this post
    ==========================================================================
    ** Follow or unfollow a course post
    :method POST
    :param request:
        :: user = USER that send the request
    :param id: course post id
    :return:
        :: status = 200 (OK)
    ==========================================================================
    ** Edit a course post
    :method PUT
    :param request:
        :: user = USER that send the request
        :: course_post_text = text of the course post
    :param id: course post id
    :return:
        :: status = 200 (OK)
    ==========================================================================
    ** Delete a course post
    :method DELETE
    :param request:
        :: user = USER that send the request
    :param id: course post id
    :return:
        :: status = 200 (OK)
    """
    # get the post with post_id = id and validate it exists
    context = {}

    current_course_post = CoursePost.objects.filter(id=id).last()
    if not current_course_post:
        return _send_error("The post desn't exist", HTTP_404_NOT_FOUND)

    current_user_profile = Profile.objects.filter(user_id=request.user).last()

    is_following = current_user_profile.following_course_post.filter(
        id=id).exists()
    #  get a course posts (not use GET because need to pass user id to verify following status)
    if request.method == "GET":
        context['post'] = _course_post_serialize_helper(
            current_course_post, many=False)
        context['following'] = is_following
        return Response(context, status=HTTP_200_OK)

    # follow/unfollow a post
    elif request.method == "POST":
        if is_following:  # remove from following
            current_user_profile.following_course_post.remove(
                current_course_post)
            current_course_post.number_of_follower = current_course_post.number_of_follower - 1
        else:
            current_user_profile.following_course_post.add(current_course_post)
            current_course_post.number_of_follower = current_course_post.number_of_follower + 1

        return Response(context, status=HTTP_200_OK)

    # edit a course post
    elif request.method == "PUT":
        data = json.loads(request.body)
        if 'course_post_text' not in data:
            return _send_error('The post text should not be empty', HTTP_400_BAD_REQUEST)
        current_course_post.course_post_text = data['course_post_text']
        current_course_post.update_time = timezone.now()
        current_course_post.save()
        return Response(context, status=HTTP_200_OK)

    # delete a course post
    elif request.method == "DELETE":
        # find all comment related to this course post
        # current_course_post_comments = CourseComment.objects.filter(
        #     course_post_id=current_course_post).all()
        # current_course_post_comments.delete()
        current_course_post.delete()
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def course_post_comment_action_by_postid(request, id):
    """ Course comment related functions with post id

    ** Get all comments related to post_id = id
    :method GET
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK)
        :: comments = course comments of course post with post_id=id
    ==========================================================================
    ** Post a comment under a post with post_id = id
    :method POST
    :param request:
        :: user = USER that send the request
        :: course_comment_text = text of the course comment
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}
    current_post = CoursePost.objects.filter(id=id).last()

    # get comments for a post
    # return: {comments, status}
    if request.method == "GET":
        course_comments = CourseComment.objects.filter(course_post_id=id).all()
        context['comments'] = _course_post_comment_serialize_helper(
            course_comments, many=True)
        return Response(context, status=HTTP_200_OK)

    # create comments for a post
    # return: {status}
    elif (request.method == "POST"):
        data = json.loads(request.body)
        if 'course_comment_text' not in data or not data['course_comment_text']:
            return _send_error('The comment text should not be empty', HTTP_400_BAD_REQUEST)
        # add user points
        user = request.user
        add_user_point(user, 3)

        # course_post = CoursePost.objects.filter(id=id).last()
        new_comment = CourseComment(
            course_post_id=current_post, course_comment_text=data['course_comment_text'], course_comment_user=user, creation_time=timezone.now())
        new_comment.save()

        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["PUT", "DELETE"])
def course_post_comment_action_by_commentid(request, id):
    """ Course comment related functions with comment id

    ** Edit a comment with comment_id = id
    :method PUT
    :param request:
        :: user = USER that send the request
        :: course_comment_text = text of the course comment
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    ==========================================================================
    ** Delete a comment with comment_id = id
    :method DELETE
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}
    # validate comment exist
    current_comment = CourseComment.objects.all().filter(id=id)
    if not current_comment:
        return _send_error('comment does not exist', HTTP_400_BAD_REQUEST)
    # validate user
    user = request.user
    if user != current_comment.course_comment_user:
        return _send_error('user does not own it', HTTP_400_BAD_REQUEST)

    # edit comments
    # return: {status}
    if (request.method == "PUT"):
        data = json.loads(request.body)
        if 'course_comment_text' not in data or not data['course_comment_text']:
            return _send_error('The comment text should not be empty', HTTP_400_BAD_REQUEST)
        current_comment.course_comment_text = data['course_comment_text']
        current_comment.save()
        return Response(context, status=HTTP_200_OK)

    # delete comments
    # return: {status}
    if request.method == "DELETE":
        current_comment.delete()
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def career_post_search(request):
    """ Search Career Posts

    ** Get career posts based on filter (if have any)
    :method POST
    :param request:
        :: user = USER that send the request
        :: career_post_title = title of career post
        :: career_post_text = text of the career post
        :: type = type of the career post
        :: company_name = company name of the career post
        :: job_title = job title of the career post
        :: visa_sponsor = visa sponsor of the career post
        :: location = location of the career post
        :: career_post_user_id = user id of the career post
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
        :: post_limit = message if user's point are lower than view limit
        :: post = career posts
    """
    context = {}
    # getting filtered career posts, serialize the data, and return
    if request.method == "POST":
        data = json.loads(request.body)
        career_post = CareerPost.objects.all().order_by("update_time")
        user_point = Profile.objects.filter(
            user_id=request.user).last().user_point
        # check user point
        if user_point <= 5:
            career_post = career_post.filter(Q(type='Interview') |
                                             Q(type='Ask')).all()
            context['post_limit'] = 'Referral posts are available for user points > 5.'
        elif user_point <= 3:
            career_post = career_post.filter(type='Ask').all()
            context['post_limit'] = 'Referral & Interview posts are available for user points > 3.'

        if "career_post_title" in data:
            career_post = career_post.filter(
                career_post_title__icontains=data['career_post_title'])
        if "career_post_text" in data:
            career_post = career_post.filter(
                career_post_text__icontains=data['career_post_text'])
        if "type" in data:
            career_post = career_post.filter(type=data['type'])
        if "company_name" in data:
            career_post = career_post.filter(
                company_name__icontains=data['company_name'])
        if "job_title" in data:
            career_post = career_post.filter(
                job_title__icontains=data['job_title'])
        if "location" in data:
            career_post = career_post.filter(
                location__icontains=data['location'])
        if "visa_sponsor" in data:
            career_post = career_post.filter(
                visa_sponsor=data['visa_sponsor'])
        if "career_post_user_id" in data:
            career_post = career_post.filter(
                career_post_user_id__icontains=data['career_post_user_id'])

        post = _career_post_serialize_helper(career_post, many=True)
        context['post'] = post
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def career_post_action(request):
    """ Career Post Creation

    ** create a new career post
    :method POST
    :param request:
        :: user = USER that send the request
        :: title = title of career post
        :: post_text = text of the career post
        :: type = type of the career post
        :: company_name = company name of the career post
        :: position = job title of the career post
        :: visa_sponsor = visa sponsor of the career post
        :: location = location of the career post
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}

    if request.method == "POST":
        data = json.loads(request.body)
        if 'title' not in data:
            return _send_error('The post title should not be empty', HTTP_400_BAD_REQUEST)
        if 'post_text' not in data:
            return _send_error('The post text should not be empty', HTTP_400_BAD_REQUEST)

        # add user points
        add_user_point(request.user, 3)

        new_post = CareerPost(career_post_title=data["title"],
                              type=data["type"],
                              career_post_text=data["post_text"],
                              career_post_user=request.user,
                              company_name=data["company_name"],
                              job_title=data["position"],
                              location=data["location"],
                              visa_sponsor=data["visa_sponsor"],
                              creation_time=timezone.now(),
                              update_time=timezone.now()
                              )
        new_post.save()
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST", "PUT", "DELETE"])
def career_post_action_by_postid(request, id):
    """ Career post related functions with post id

    ** Get the career posts
    :method GET
    :param request:
        :: user = USER that send the request
    :param id: career post id
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
        :: post = career posts with this post id
        :: following = whether the user is following this post
    ==========================================================================
    ** Follow or unfollow a career post
    :method POST
    :param request:
        :: user = USER that send the request
    :param id: career post id
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
    ==========================================================================
    ** Edit a career post
    :method PUT
    :param request:
        :: user = USER that send the request
        :: career_post_text = text of the career post
    :param id: career post id
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
    ==========================================================================
    ** Delete a career post
    :method DELETE
    :param request:
        :: user = USER that send the request
    :param id: career post id
    :return:
        :: status = 200 (OK) / 404 (NOT FOUND)
    """
    # get the post with post_id = id and validate it exists
    context = {}

    current_career_post = CareerPost.objects.filter(id=id).last()
    if not current_career_post:
        return _send_error("post does not exist", HTTP_404_NOT_FOUND)

    current_user_profile = Profile.objects.filter(user_id=request.user).last()

    is_following = current_user_profile.following_career_post.filter(
        id=id).exists()
    #  get a career posts (not use GET because need to pass user id to verify following status)
    if request.method == "GET":
        context['post'] = _career_post_serialize_helper(
            current_career_post, many=False)
        context['following'] = is_following
        return JsonResponse(context, safe=False)

    # follow/unfollow a post
    elif request.method == "POST":
        if is_following:  # remove from following
            current_user_profile.following_career_post.remove(
                current_career_post)
        else:
            current_user_profile.following_career_post.add(current_career_post)

        return Response(context, status=HTTP_200_OK)

    # edit a course post
    # return: {status, (error)}
    elif request.method == "PUT":
        data = json.loads(request.body)
        if 'career_post_text' not in data or not data['career_post_text']:
            return _send_error('The post should not be empty', HTTP_400_BAD_REQUEST)
        current_career_post.career_post_text = data['career_post_text']
        current_career_post.update_time = timezone.now()
        current_career_post.save()
        return Response(context, status=HTTP_200_OK)

    # delete a course post
    # return: {status, (error)}
    elif request.method == "DELETE":
        # current_career_post_comment = CareerComment.objects.filter(
        #     career_post_id=current_career_post).all()
        # current_career_post_comment.delete()
        current_career_post.delete()
        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def career_post_comment_action_by_postid(request, id):
    """ Career comment related functions with post id

    ** Get all comments related to post_id = id
    :method GET
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK)
        :: comments = career comments of career post with post_id=id
    ==========================================================================
    ** Post a comment under a post with post_id = id
    :method POST
    :param request:
        :: user = USER that send the request
        :: career_comment_text = text of the career comment
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}
    current_post = CareerPost.objects.filter(id=id).last()

    # get comments for a post
    # return: {comments, status}
    if request.method == "GET":
        career_comments = CareerComment.objects.filter(career_post_id=id).all()
        context['comments'] = _career_post_comment_serialize_helper(
            career_comments, many=True)
        return Response(context, status=HTTP_200_OK)

    # create comments for a post
    # return: {status}
    elif (request.method == "POST"):
        data = json.loads(request.body)
        if 'career_comment_text' not in data or not data['career_comment_text']:
            return _send_error('The comment text should not be empty', HTTP_400_BAD_REQUEST)
        # add user points
        user = request.user
        add_user_point(user, 3)

        new_comment = CareerComment(
            career_post_id=current_post,
            career_comment_text=data['career_comment_text'],
            career_comment_user=user,
            creation_time=timezone.now())
        new_comment.save()

        return Response(context, status=HTTP_200_OK)


@csrf_exempt
@api_view(["PUT", "DELETE"])
def career_post_comment_action_by_commentid(request, id):
    """ Career comment related functions with comment id

    ** Edit a comment with comment_id = id
    :method PUT
    :param request:
        :: user = USER that send the request
        :: career_comment_text = text of the course comment
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    ==========================================================================
    ** Delete a comment with comment_id = id
    :method DELETE
    :param request:
        :: user = USER that send the request
    :return:
        :: status = 200 (OK) / 400 (BAD REQUEST)
    """
    context = {}
    # validate comment exist
    current_comment = CareerComment.objects.all().filter(id=id).last()
    if not current_comment:
        return _send_error('comment does not exist', HTTP_400_BAD_REQUEST)
    # validate user
    user = request.user
    if user != current_comment.career_comment_user:
        return _send_error('user does not own it', HTTP_400_BAD_REQUEST)

    # edit comments
    # return: {status}
    if (request.method == "PUT"):
        data = json.loads(request.body)
        if 'career_comment_text' not in data or not data['course_comment_text']:
            return _send_error('The text should not be empty', HTTP_400_BAD_REQUEST)
        current_comment.career_comment_text = data['career_comment_text']
        current_comment.save()
        return Response(context, status=HTTP_200_OK)

    # delete comments
    # return: {status}
    if request.method == "DELETE":
        current_comment.delete()
        return Response(context, status=HTTP_200_OK)


def message_serializer(messages, many=False):
    """ Serialize message QuerySet
    :param many: False if there's only one object
    :param messages: messages QuerySet
    :return: json message sata
    """
    # specify many = True if want to serialize multiple objects
    serializer = MessageSerializer(messages, many=many)
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)
    return JSONParser().parse(stream)


# add user points
def add_user_point(user, point):
    """ Add points to user's user_point
    :param user: user that need to be added points
    :param point: point that need to be added
    :return:
    """
    profile = Profile.objects.filter(user_id=user).last()
    profile.user_point += point
    profile.save()
