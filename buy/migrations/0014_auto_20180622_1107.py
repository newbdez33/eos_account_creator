# Generated by Django 2.0.6 on 2018-06-22 09:07

from django.db import migrations


class Migration(migrations.Migration):
    def migrate_keys(apps, schema_editor):
        Purchase = apps.get_model('buy', 'Purchase')
        for p in Purchase.objects.all():
            p.owner_key = p.public_key
            p.active_key = p.public_key
            p.save()

    dependencies = [
        ('buy', '0013_auto_20180622_1107'),
    ]

    operations = [
        migrations.RunPython(migrate_keys),
    ]
