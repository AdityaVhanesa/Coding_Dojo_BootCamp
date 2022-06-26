from django.db import models


# Create your models here.
class player(models.Model):
    player_name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not player.objects.filter(player_name=self.player_name).exists():
            super().save(*args, **kwargs)

    def __str__(self):
        return self.player_name


class player_score(models.Model):
    player_id = models.ForeignKey(player, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User --> {self.player_id}  |  Score --> {self.score}"
