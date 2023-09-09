# Generated by Django 4.2.1 on 2023-09-07 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_user_remove_book_purpose_presentaddress_notification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.book')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
    ]
