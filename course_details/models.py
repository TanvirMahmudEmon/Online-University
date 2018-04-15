from django.db import models

# Create your models here.


class CourseDetails(models.Model):
    course_code = models.CharField(max_length=250)
    course_title = models.CharField(max_length=250)
    credit_hours = models.IntegerField(default=3)
    contact_hours = models.CharField(max_length=100)
    pre_requisite = models.CharField(max_length=250)
    instructor_name = models.CharField(max_length=250)
    objectives = models.TextField()
    course_desc = models.TextField()
    recommended_books = models.TextField()

    def __str__(self):
        return self.course_title


# class Take_this_course(models.Model):
#     course_title = models.ForeignKey(Course_datails)
#     take_this_course = models.IntegerField(default=0)
#
#     def __str__(self):
#         return  self.course_title

