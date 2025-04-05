from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clubs')
    president = models.CharField(max_length=255, blank=True, null=True)
    coach = models.CharField(max_length=255, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    price = models.FloatField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club_from = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_from')
    club_to = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_to')
    price = models.FloatField()
    price_tft = models.FloatField()
    date = models.DateField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name}: {self.club_from.name} - {self.club_to.name}"
