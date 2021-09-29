# Generated by Django 3.2.7 on 2021-09-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_settings', '0005_auto_20210915_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='paragraph_image1_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image1_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image1_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image2_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image2_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image2_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image3_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image3_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image3_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image4_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image4_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image4_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image5_1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image5_2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_image5_3',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_subtitle_1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_subtitle_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_subtitle_3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_subtitle_4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_subtitle_5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_text_1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_text_2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_text_3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_text_4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_text_5',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_video_1',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_video_2',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_video_3',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_video_4',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
        migrations.AddField(
            model_name='project',
            name='paragraph_video_5',
            field=models.FileField(null=True, upload_to='video/%y'),
        ),
        migrations.DeleteModel(
            name='ProjectVideo',
        ),
    ]
