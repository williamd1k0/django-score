from django.db import models

# Create your models here.

class ScoreData(models.Model):

    name = models.CharField(max_length=255)
    points = models.FloatField()


    def __repr__(self):
        return 'ScoreData<{0.name}:{0.points}>'.format(self)

    def __str__(self):
        return 'Score by {0}'.format(self.name)

