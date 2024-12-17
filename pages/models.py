from django.db import models

class Movie_tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ярлык"
        verbose_name_plural = "Ярлыки"

class Movie_image(models.Model):
    image = models.ImageField(upload_to="media/movie_images/", blank=True, null=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="images")
    
    def __str__(self):
        return self.movie.title
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class Movie_dup_title(models.Model):
    title = models.CharField(max_length=255, unique=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="duptitles")
    
    def __str__(self):
        return self.movie.title
    
    class Meta:
        verbose_name = "Доп. название"
        verbose_name_plural = "Доп. названия"

class Movie_link(models.Model):
    link = models.URLField()
    origin = models.CharField(max_length=255, blank=True)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE, related_name="links")
    
    def __str__(self):
        return self.movie.title
    
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1023, blank=True)
    translit_title = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField("Movie_tag", related_name="Movies", blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"