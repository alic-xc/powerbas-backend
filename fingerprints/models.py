from django.db import models

# Create your models here.


class Songs(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=250)
    fingerprinted = models.SmallIntegerField(blank=True, null=True)
    file_sha1 = models.BinaryField(blank=True, null=True)
    total_hashes = models.IntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'songs'


class Fingerprints(models.Model):
    hash = models.BinaryField()
    song = models.ForeignKey('Songs', models.DO_NOTHING)
    offset = models.IntegerField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'fingerprints'
        unique_together = (('song', 'offset', 'hash'),)
