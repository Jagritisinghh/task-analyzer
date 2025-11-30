from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    # Importance: 1 (Low) to 5 (Critical)
    importance = models.IntegerField(default=3) 
    # Effort: 1 (Quick) to 5 (Huge Project)
    effort = models.IntegerField(default=3)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title