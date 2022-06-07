from django.db import models


class PloggingLog(models.Model):
    userid = models.BigIntegerField(db_column='userId')  # Field name made lowercase.
    distance = models.IntegerField(blank=True, null=True)
    starttime = models.DateTimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    runningtime = models.TimeField(db_column='runningTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plogging_log'
