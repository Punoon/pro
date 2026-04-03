# archive/models.py
from django.db import models

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('SUM', 'สรุปบทเรียน'),
        ('EXAM', 'ข้อสอบเก่า'),
    ]
    subject_code = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    # เพิ่มฟิลด์นี้เพื่อเก็บไฟล์ (PDF/PNG)
    file = models.FileField(upload_to='documents/', null=True, blank=True) 
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title