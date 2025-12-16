from django.db import models

class Topic(models.Model):
    """ This class simulates the entry topic """
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

class Entry(models.Model):
    """ This class simulates the entry content """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'
    
    def __str__(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        return self.text
