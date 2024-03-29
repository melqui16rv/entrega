# Generated by Django 4.2.7 on 2024-03-22 01:55

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
                ('nombre', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('educacion', models.TextField()),
                ('Certificado', models.FileField(upload_to='educacion_pdfs/')),
                ('experiencia', models.TextField()),
                ('profesion', models.CharField(max_length=100)),
                ('curriculum', models.FileField(upload_to='curriculums/')),
            ],
        ),
    ]
