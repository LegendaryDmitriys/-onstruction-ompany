# Generated by Django 5.0.6 on 2024-06-05 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('сonstructionСompany', '0004_material_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='personnel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='сonstructionСompany.personnel', verbose_name='Персонал'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='material',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cтоимость'),
        ),
        migrations.AlterField(
            model_name='material',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='material',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='сonstructionСompany.project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='material',
            name='purchase',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Закупка'),
        ),
        migrations.AlterField(
            model_name='material',
            name='quantity',
            field=models.IntegerField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='material',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='сonstructionСompany.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='order',
            name='completion_date',
            field=models.DateField(verbose_name='Дата завершения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='order',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='сonstructionСompany.project', verbose_name='Проект'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='сonstructionСompany.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='experience',
            field=models.IntegerField(verbose_name='Стаж'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='position',
            field=models.CharField(max_length=255, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='сonstructionСompany.material', verbose_name='Материал'),
        ),
    ]
