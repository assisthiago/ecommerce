from django.db import models


class AvailablilityProductQuerySet(models.QuerySet):
    def availables(self):
        return self.filter(available=True)
