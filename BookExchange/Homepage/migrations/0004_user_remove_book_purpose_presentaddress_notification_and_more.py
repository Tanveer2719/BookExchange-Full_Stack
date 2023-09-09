# Generated by Django 4.2.1 on 2023-09-07 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_rename_authorofbook_book_authorsofbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('passwordHash', models.CharField(max_length=500)),
                ('institution', models.CharField(max_length=100)),
                ('dateOfRes', models.DateField(auto_now_add=True)),
                ('phoneNo', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='purpose',
        ),
        migrations.CreateModel(
            name='PresentAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('upzilla', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=500)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='BooksRequested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(max_length=255)),
                ('requesterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
        migrations.CreateModel(
            name='BooksForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('availability', models.CharField(max_length=50)),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.book')),
                ('ownerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.user')),
            ],
        ),
    ]
