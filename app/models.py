from django.db import models


class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)

    def get_full_name(self):
        return (self.first_name + ' '+ self.last_name).strip()

    @property
    def address(self):
        return (self.street + ', '+ self.city + ', ' + self.state + ', ' + self.zip).strip()

    def __str__(self):
        return self.get_full_name()


class Child(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    @property
    def get_parent(self):
        return self.parent.get_full_name

    def get_full_name(self):
        return (self.first_name + ' ' + self.last_name).strip()



    def __str__(self):
        return self.get_full_name()

    @property
    def address(self):
        return self.parent.address
