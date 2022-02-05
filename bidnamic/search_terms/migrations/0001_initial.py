# Generated by Django 3.2.11 on 2022-02-05 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ad_groups', '0001_initial'),
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('date', models.DateField()),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conversion_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('conversions', models.PositiveIntegerField()),
                ('search_term', models.CharField(max_length=250)),
                ('ad_group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ad_groups.adgroup')),
                ('campaign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.campaign')),
            ],
        ),
        migrations.AddIndex(
            model_name='searchterm',
            index=models.Index(fields=['search_term'], name='search_term_search__c8adbc_idx'),
        ),
        migrations.AddIndex(
            model_name='searchterm',
            index=models.Index(fields=['date', 'search_term'], name='search_term_date_511613_idx'),
        ),
    ]