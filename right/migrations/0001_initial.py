# Generated by Django 4.2.4 on 2023-08-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('left', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('availability', models.IntegerField()),
                ('date_of_producing', models.DateField()),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='left.category')),
            ],
        ),
    ]