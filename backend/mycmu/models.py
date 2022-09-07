import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Course(models.Model):
    course_year = models.IntegerField()
    course_semester = models.CharField(max_length=200)
    course_college = models.CharField(max_length=200)
    course_department = models.CharField(max_length=200)
    course_number = models.IntegerField()
    course_section = models.CharField(max_length=200)
    course_instructor_firstname = models.CharField(max_length=200)
    course_instructor_lastname = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    course_level = models.CharField(max_length=200)
    course_response_num = models.IntegerField()
    course_hour = models.FloatField(default=1.7514)
    course_teaching_rate = models.FloatField(default=1.7514)
    course_overall_rate = models.FloatField(default=1.7514)

    def __str__(self):
        return (
            " Course:(id="
            + str(self.id)
            + ")"
            + " Name: "
            + str(self.course_name)
            + "Instructor: "
            + str(self.course_instructor_firstname) +
            str(self.course_instructor_lastname)
        )


class CoursePost(models.Model):
    course_id = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_id"
    )

    course_post_title = models.CharField(max_length=200)
    course_post_text = models.CharField(max_length=200)
    course_post_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="course_post_user"
    )
    creation_time = models.DateTimeField()
    update_time = models.DateTimeField()
    number_of_follower = models.IntegerField()

    def __str__(self):
        return (
            "Course Post(id="
            + str(self.id)
            + ")"
            + " Course: "
            + str(self.course_id.course_name)
            + " Content: "
            + str(self.course_post_text)
            + "Post user: "
            + str(self.course_post_user)
        )


class CourseComment(models.Model):
    course_post_id = models.ForeignKey(
        CoursePost, on_delete=models.CASCADE, related_name="course_post_id"
    )
    course_comment_text = models.CharField(max_length=200)
    course_comment_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="course_comment_user"
    )
    creation_time = models.DateTimeField()

    def __str__(self):
        return (
            "Course Comment(id="
            + str(self.id)
            + ")"
            + " Content: "
            + str(self.course_comment_text)
            + "Comment User: "
            + str(self.course_comment_user)
            + "For post: "
            + str(self.course_post_id)
        )


class CareerPost(models.Model):
    career_post_title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    career_post_text = models.CharField(max_length=200)
    career_post_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="career_post_user"
    )
    company_name = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    visa_sponsor = models.BooleanField(null=True)
    creation_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return (
            "Career Post(id="
            + str(self.id)
            + ")"
            + " Company: "
            + str(self.company_name)
            + " Content: "
            + str(self.post_text)
            + "Post user: "
            + str(self.post_user)
        )


class CareerComment(models.Model):
    career_post_id = models.ForeignKey(
        CareerPost, on_delete=models.CASCADE, related_name="post_id"
    )
    career_comment_text = models.CharField(max_length=200)
    career_comment_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="career_comment_user"
    )
    creation_time = models.DateTimeField()

    def __str__(self):
        return (
            "Career Comment(id="
            + str(self.id)
            + ")"
            + " Content: "
            + str(self.comment_text)
            + "Comment User: "
            + str(self.comment_user)
            + "For post: "
            + str(self.post_id)
        )


class Message(models.Model):
    message = models.CharField(max_length=200)
    from_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_user_id"
    )
    to_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_user_id"
    )
    creation_time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return (
            " Message:(id="
            + str(self.id)
            + ")"
            + "From: "
            + str(self.from_user_id)
            + "To: "
            + str(self.to_user_id)
            + "Msg: "
            + str(self.message)
        )


class Profile(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_creators"
    )
    created_at = models.DateTimeField(default=now)
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    profile_picture = models.FileField(blank=True, default="default.png")
    user_point = models.IntegerField(default=0)
    followers = models.ManyToManyField(
        User, default=None, symmetrical=False, blank=True, related_name='follower')
    following_career_post = models.ManyToManyField(
        CareerPost, default=None, symmetrical=False, blank=True, related_name='career_post')
    following_course_post = models.ManyToManyField(
        CoursePost, default=None, symmetrical=False, blank=True, related_name='course_post')

    def __str__(self):
        return "Profile(id=" + str(self.id) + ")" + " user_id: " + str(self.user_id)
