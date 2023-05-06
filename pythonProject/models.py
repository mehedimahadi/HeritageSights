class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    full_name = models.CharField(max_length=50)
    # Email = models.CharField(max_length=100)
    image = models.ImageField()
