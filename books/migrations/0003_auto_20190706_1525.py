# Generated by Django 2.2.3 on 2019-07-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_uploader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.AddField(
            model_name='book',
            name='image_path',
            field=models.URLField(default='static/books/pic.jpg', verbose_name='封面保存路径'),
        ),
        migrations.AlterField(
            model_name='book',
            name='content_path',
            field=models.URLField(verbose_name='书籍保存路径'),
        ),
        migrations.AlterField(
            model_name='book',
            name='type_id',
            field=models.SmallIntegerField(choices=[(1, 'Python'), (2, 'Javascript'), (3, '数据结构与算法'), (4, '机器学习'), (5, '操作系统'), (6, '数据库')], default=1, verbose_name='书的种类'),
        ),
    ]