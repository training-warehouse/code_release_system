# Generated by Django 3.2.8 on 2021-10-13 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_node_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='status',
            field=models.CharField(choices=[('lightgrey', '待发布'), ('green', '发布成功'), ('red', '发布失败')], default='lightgrey', max_length=16, verbose_name='状态'),
        ),
    ]