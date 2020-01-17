# Generated by Django 2.2.5 on 2019-11-23 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagerie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cnn',
            name='training_images',
        ),
        migrations.CreateModel(
            name='CNNType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.DecimalField(decimal_places=3, max_digits=4)),
                ('cnn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='imagerie.CNN')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cnns_specialiazed_in', to='imagerie.BackgroundType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CNNContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy', models.DecimalField(decimal_places=3, max_digits=4)),
                ('cnn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='imagerie.CNN')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cnns_specialiazed_in', to='imagerie.PlantOrgan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
