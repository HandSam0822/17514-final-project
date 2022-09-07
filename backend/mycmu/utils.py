from django.contrib.auth.models import User
from mycmu.models import *
from django.db import models
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
import pytz


local_tz = pytz.timezone('US/Eastern')


def _isCMUEmail(mail):
    return mail.endswith("@andrew.cmu.edu")


def _userExist(email):
    return User.objects.filter(email=email).last()


# serialize course post
def _course_post_serialize_helper(course_post, many=False):
    # specify many = True if want to serialize multiple objects
    serializer = CoursePostSerializer(course_post, many=many)
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)
    return JSONParser().parse(stream)

# serialize career post


def _career_post_serialize_helper(career_post, many):
    serializer = CareerPostSerializer(career_post,
                                      many=many)  # specify many = True if want to serialize multiple objects
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)
    return JSONParser().parse(stream)


# serialize course
def _course_serialize_helper(course, many=False):
    serializer = CourseSerializer(course, many=many)
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)
    return JSONParser().parse(stream)


# serialize course
def _course_post_comment_serialize_helper(course_comment, many=False):
    serializer = CourseCommentSerializer(course_comment, many=many)
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)
    return JSONParser().parse(stream)


def _career_post_comment_serialize_helper(carrer_comment, many=False):
    serializer = CareerCommentSerializer(carrer_comment, many=many)
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)
    return JSONParser().parse(stream)

# serialize course post


def _profile_serialize_helper(profile):
    serializer = ProfileSerializer(profile)
    # convert model object to byte array
    json_data = JSONRenderer().render(serializer.data)
    stream = io.BytesIO(json_data)  # convert byte array to json(dict)

    return JSONParser().parse(stream)


# def _send_error(context, message):
#     context['error'] = message
#     context['status'] = 404
#     return JsonResponse(context, safe=False)

def _send_error(message, status):
    return Response({'error': message}, status=status)


"""Transform utc time to local(US/Eastern) timezone"""


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)


def base64ToImageInstance(data, username):
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]
    # You can save this as file instance.
    return ContentFile(base64.b64decode(imgstr), name=username + ".png")
