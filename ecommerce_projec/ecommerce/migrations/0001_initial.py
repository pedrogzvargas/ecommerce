# Generated by Django 3.1 on 2020-08-23 22:34

from decimal import Decimal
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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.category')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iva', models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=20)),
                ('total', models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.product')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.purchase')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='products',
            field=models.ManyToManyField(through='ecommerce.PurchaseProducts', to='ecommerce.Product'),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.person'),
        ),
    ]
