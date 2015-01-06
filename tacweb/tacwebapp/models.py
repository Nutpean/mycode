from django.db import models

# Create your models here.

class webtemp( models.Model ):
    ''' webtemp table '''
    domain = models.CharField( max_length=255 )
    url = models.CharField( max_length=255 )
    filehash = models.CharField( max_length=255 )
    ip = models.CharField( max_length=40 )
    port = models.IntegerField()
    protocol = models.CharField( max_length=20 )
    threat = models.IntegerField()
    risk = models.FloatField()
    createtime = models.TimeField()
    status = models.IntegerField()
    check = models.BooleanField( default=False )

    def __unicode__( self ):
        return self.domain
