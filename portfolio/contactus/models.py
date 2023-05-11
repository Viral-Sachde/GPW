from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Form Details"

    def __str__(self):
        return str(self.name) + " --- " + str(self.email)

