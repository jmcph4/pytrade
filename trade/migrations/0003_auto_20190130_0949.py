# Generated by Django 2.1.5 on 2019-01-29 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20180328_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='market',
            name='traders',
        ),
        migrations.RemoveField(
            model_name='trader',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='trader',
            name='volume',
        ),
        migrations.AddField(
            model_name='participant',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.Market'),
        ),
        migrations.AddField(
            model_name='participant',
            name='trader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trade.Trader'),
        ),
    ]
