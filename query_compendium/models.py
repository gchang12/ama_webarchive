from django.db import models

from .constants import CC_NAME_LIST, LONGEST_CCNAME_LEN

# Create your models here.

class ContentCreator(models.Model):
    url_name = models.CharField(
        primary_key=True,
        max_length=LONGEST_CCNAME_LEN,
        )
    display_name = models.CharField(
        unique=True,
        max_length=LONGEST_CCNAME_LEN,
        )


class RedditQuery(models.Model):
    content_creator = models.ForeignKey(
        ContentCreator,
        on_delete=models.PROTECT,
        )
    url_id = models.CharField(
        primary_key=True,
        max_length=20,
        )
    fan_name = models.TextField()
    question_text = models.TextField()
    answer_text = models.TextField()

if __name__ == '__main__':
    pass
