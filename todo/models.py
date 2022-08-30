from django.db import models

# Create your models here.


class Todo(models.Model):
    PRIORITY = (
        ("1", "first"),
        ("2", "second"),
        ("3", "third"),
        ("4", "fourth")
    )
    status_choices = [
    ('C', 'Completed'),
    ('P', 'Pending'),
    ('I', 'In-Progress')
    ]
    title = models.CharField(max_length=40, help_text="This field is required")
    description = models.TextField(db_column="aciklama")
    # number = models.IntegerField(unique=True, db_index=True) 
    ## index;  unique ile kullanilir ve performans icindir
    number = models.IntegerField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=20, choices=PRIORITY)
    status = models.CharField(max_length=20, choices=status_choices)

    def __str__(self):
        return f"{self.number} - {self.title} - {self.status}"

    class Meta:
        verbose_name_plural = "Todoss"
        ordering = ["number"]


