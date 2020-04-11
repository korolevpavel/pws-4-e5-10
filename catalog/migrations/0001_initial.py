from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_of_car', models.CharField(max_length=150, null=True, verbose_name='Модель')),
                ('year', models.IntegerField(null=True, verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[(1, 'механика'), (2, 'автомат'), (3, 'робот')], null=True, verbose_name='Коробка передач')),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Color')),
                ('producer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Producer')),
            ],
        ),
    ]
