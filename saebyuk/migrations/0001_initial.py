# Generated by Django 3.2.7 on 2021-09-14 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='책 제목')),
                ('cover', models.TextField(verbose_name='책 커버 url')),
                ('author', models.CharField(max_length=10, verbose_name='책 저자')),
                ('introduce', models.TextField(verbose_name='책 소개글')),
                ('create_date', models.DateTimeField(blank=True, null=True, verbose_name='책 등록 시간')),
                ('available', models.TextField(verbose_name='대출 가능 여부')),
                ('rental_date', models.DateTimeField(blank=True, null=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('thief', models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]