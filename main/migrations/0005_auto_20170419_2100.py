# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_kvartiry_kol_komnat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lgoty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Серия и номер льготы')),
                ('date_in', models.DateField(verbose_name='Дата начала действия льготы')),
                ('date_out', models.DateField(blank=True, verbose_name='Дата окончания действия льготы')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('document', models.IntegerField(choices=[(1, 'Паспорт'), (2, 'Вид на жительство'), (3, 'Справка')], verbose_name='Вид документа')),
                ('document_number', models.CharField(max_length=20, verbose_name='Номер документа')),
                ('dateOfBirdth', models.DateField(verbose_name='Дата рождения')),
                ('dateOfDeath', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('gender', models.SmallIntegerField(choices=[(1, 'Мужской'), (2, 'Женский')], verbose_name='Пол')),
                ('prim', models.TextField(blank=True, verbose_name='Примечание')),
            ],
        ),
        migrations.CreateModel(
            name='Tip_lgoty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Наименование льготы')),
            ],
        ),
        migrations.AddField(
            model_name='lics',
            name='email',
            field=models.CharField(blank=True, max_length=20, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='lics',
            name='kod_kvart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Kvartiry', verbose_name='Квартира'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lics',
            name='prim',
            field=models.TextField(blank=True, verbose_name='Примечание'),
        ),
        migrations.AddField(
            model_name='lics',
            name='tel',
            field=models.CharField(blank=True, max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='dom',
            name='nas_punkt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Nas_punkt', verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='dom',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Street', verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='kvartiry',
            name='kod_dom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dom', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='lics',
            name='kod_dom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dom', verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='person',
            name='lics',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Lics', verbose_name='Лицевой счет'),
        ),
        migrations.AddField(
            model_name='lgoty',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person', verbose_name='Физ лицо'),
        ),
        migrations.AddField(
            model_name='lgoty',
            name='tip_lgoty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tip_lgoty', verbose_name='Тип льготы'),
        ),
    ]
