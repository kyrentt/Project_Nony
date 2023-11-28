# Generated by Django 4.2.4 on 2023-11-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_post_fecha_post_alter_post_titulo_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='amigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('list_amigos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='e_c',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cinéfilo', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_jm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jm', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_k',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kpop', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_p',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_pg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_pp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_s',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Soltero', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='e_t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tecnología', models.TextField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='e_o',
            new_name='e_a',
        ),
        migrations.RenameField(
            model_name='e_a',
            old_name='Otaku',
            new_name='Anime',
        ),
        migrations.RenameField(
            model_name='e_l',
            old_name='LQBTQ',
            new_name='LGBTQ',
        ),
        migrations.RenameField(
            model_name='e_m',
            old_name='Musica',
            new_name='Música',
        ),
    ]
