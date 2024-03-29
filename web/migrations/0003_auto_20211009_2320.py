# Generated by Django 3.2.8 on 2021-10-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='path',
            field=models.CharField(default='/data/prod/', max_length=255, verbose_name='线上项目地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='servers',
            field=models.ManyToManyField(to='web.Server', verbose_name='关联服务器'),
        ),
    ]
