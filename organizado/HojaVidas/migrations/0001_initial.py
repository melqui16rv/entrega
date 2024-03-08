# Generated by Django 5.0.3 on 2024-03-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HojaVida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('documento', models.CharField(max_length=20)),
                ('libreta_militar', models.BooleanField()),
                ('fecha_nacimiento', models.DateField()),
                ('estado_civil', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('habilidades', models.TextField()),
                ('estudios', models.TextField()),
                ('curriculum', models.FileField(upload_to='curriculums/')),
            ],
        ),
    ]
