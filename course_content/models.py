from django.db import models

# Create your models here.


class CourseContent(models.Model):
    # course_code = models.CharField(max_length=250)
    # course_title = models.CharField(max_length=250)
    # credit_hours = models.IntegerField(default=3)
    pdf_title = models.CharField("PDF Title 1", max_length=250)
    pdf = models.TextField("Embed Code 1")
    # pdf_title2 = models.CharField("PDF Title 2", max_length=250, null=True, blank=True)
    # pdf2 = models.TextField("Embed Code 2", null=True, blank=True)
    # pdf_title3 = models.CharField("PDF Title 3", max_length=250, null=True, blank=True)
    # pdf3 = models.TextField("Embed Code 3", null=True, blank=True)
    # pdf_title4 = models.CharField("PDF Title 4", max_length=250, null=True, blank=True)
    # pdf4 = models.TextField("Embed Code 4", null=True, blank=True)
    # pdf_title5 = models.CharField("PDF Title 5", max_length=250, null=True, blank=True)
    # pdf5 = models.TextField("Embed Code 5", null=True, blank=True)

    video_title = models.CharField("Video Title 1", max_length=250)
    video = models.TextField("Embed Code 1")
    # video_title2 = models.CharField("Video Title 2", max_length=250, null=True, blank=True)
    # video2 = models.TextField("Embed Code 2", null=True, blank=True)
    # video_title3 = models.CharField("Video Title 3", max_length=250, null=True, blank=True)
    # video3 = models.TextField("Embed Code 3", null=True, blank=True)
    # video_title4 = models.CharField("Video Title 4", max_length=250, null=True, blank=True)
    # video4 = models.TextField("Embed Code 4", null=True, blank=True)
    # video_title5 = models.CharField("Video Title 5", max_length=250, null=True, blank=True)
    # video5 = models.TextField("Embed Code 5", null=True, blank=True)
    # video_title6 = models.CharField("Video Title 6", max_length=250, blank=True)
    # video6 = models.TextField("Embed Code 6", blank=True)
    # video_title7 = models.CharField("Video Title 7", max_length=250, blank=True)
    # video7 = models.TextField("Embed Code 7", blank=True)
    # video_title8 = models.CharField("Video Title 8", max_length=250, blank=True)
    # video8 = models.TextField("Embed Code 8", blank=True)
    # video_title9 = models.CharField("Video Title 9", max_length=250, blank=True)
    # video9 = models.TextField("Embed Code 9", blank=True)
    # video_title10 = models.CharField("Video Title 10", max_length=250, blank=True)
    # video10 = models.TextField("Embed Code 10", blank=True)
    # video_title11 = models.CharField("Video Title 11", max_length=250, blank=True)
    # video11 = models.TextField("Embed Code 11", blank=True)
    # video_title12 = models.CharField("Video Title 12", max_length=250, blank=True)
    # video12 = models.TextField("Embed Code 12", blank=True)
    # video_title13 = models.CharField("Video Title 13", max_length=250, blank=True)
    # video13 = models.TextField("Embed Code 13", blank=True)
    # video_title14 = models.CharField("Video Title 14", max_length=250, blank=True)
    # video14 = models.TextField("Embed Code 14", blank=True)
    # video_title15 = models.CharField("Video Title 15", max_length=250, blank=True)
    # video15 = models.TextField("Embed Code 15", blank=True)

    def __str__(self):
        return self.course_title
