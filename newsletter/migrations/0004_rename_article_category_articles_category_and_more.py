# Generated by Django 4.2.3 on 2023-09-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_rename_createdat_articles_article_createdat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='article_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article_createdAt',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='article_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='categody_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment_article',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='subscriptions',
            old_name='subs_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subscriptions',
            old_name='subs_user',
            new_name='user',
        ),
    ]
