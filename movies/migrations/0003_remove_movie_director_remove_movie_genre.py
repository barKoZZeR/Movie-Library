from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
    ]
