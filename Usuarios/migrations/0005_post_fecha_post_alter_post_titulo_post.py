# Generated by Django 4.2.4 on 2023-11-25 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_merge_0002_e_d_e_g_e_l_e_m_e_o_0003_post_titulo_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_post',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo_post',
            field=models.CharField(default='USMessage', max_length=255),
        ),
    ]