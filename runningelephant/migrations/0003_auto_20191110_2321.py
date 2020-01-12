# Generated by Django 2.2.5 on 2019-11-10 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('runningelephant', '0002_auto_20191110_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='thoughts',
        ),
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoughts', models.CharField(blank=True, max_length=140, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runningelephant.Player')),
            ],
        ),
    ]