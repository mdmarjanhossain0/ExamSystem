from django.db import models

from mptt.models import MPTTModel, TreeForeignKey



class Exam(models.Model):
	name                    = models.CharField(max_length=150)
	rulse                   = models.TextField(null=True, blank=True)





QUESTION = "question"
POOL = "pool"
GROUP = "group"

TEXT_BLOCK = "text_block"
class Question(MPTTModel):
	question                    = models.CharField(max_length=150)
	options                     = models.JSONField()
	answer                      = models.CharField(max_length=31)
	mark 						= models.IntegerField(default=1)

	#Question, Pool, Group, Text Block
	type                        = models.CharField(max_length=100)






	random_show 				= models.IntegerField(null=True, blank=True)
	parent                      = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
	exam                        = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True, blank=True)







	class MPTTMeta :
		order_insertion_by=['question']

	def get_name(self):
		if self.parent is None:
			return self.question
		else:
			return self.parent.get_name() + ' -> ' + self.question
	
	def __str__(self):
			return self.get_name()