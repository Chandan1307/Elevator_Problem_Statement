from django.db import models

class Elevator(models.Model):
    RUNNING = 'running'
    STOPPED = 'stopped'
    STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (STOPPED, 'Stopped'),
    ]
    
    current_floor = models.IntegerField(default=0)
    direction = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STOPPED)
    available = models.BooleanField(default=True)
    operational = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Elevator {self.id}"


class UserRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    requested_floor = models.IntegerField()

    def __str__(self):
        return f"Request {self.id}"