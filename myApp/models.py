from django.db import models
SCHOOL_LIST =(
    ('CSUC','Chico State'),
    ('CSUCI','Cal State Channel Islands'),
    ('UCLA','UCLA'),
)
#class User(models.Model):
#  FirstName = models.CharField(max_length=40)

#  LastName = models.CharField(max_length=40)
#  school = models.CharField(max_length=3,choices=SCHOOL_LIST)
#  email = models.EmailField(max_length=100)

  #def __str__(self):
  #  return_list = {FirstName,LastName}
  #  return return_list
#  profile_image = models.ImageField(upload_to='media/user_pics/')
#  def __str__(self):
 #   return_list = {FirstName,LastName}
#    return self.objects.all()

# Create your models here.
class Extended_user(models.Model):
  school = models.CharField(max_length=200)
  years = models.IntegerField()

#class Room(models.Model):
#	name = models.TextField()
#	label = models.SlugField(unique=True)

#class Message(models.Model):
#	room = models.ForeignKey(Room,related_name="messages")
#	handle = models.TextField()
#	message = models.TextField()
#	timestamp = models.DateTimeField(default=timezone.now,db_index=True)

