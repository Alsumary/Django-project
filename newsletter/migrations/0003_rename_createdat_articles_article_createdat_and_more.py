# Generated by Django 4.2.3 on 2023-09-13 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_usermanage_role_alter_category_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='createdAt',
            new_name='article_createdAt',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='image',
            new_name='article_image',
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='title',
            new_name='article_title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='image',
            new_name='categody_image',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='content',
            new_name='category_content',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='category_title',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='category',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='content',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subscriptions',
            name='user',
        ),
        migrations.AddField(
            model_name='articles',
            name='article_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_category', to='newsletter.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='article_content',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_article', to='newsletter.articles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_content',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='subs_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_category', to='newsletter.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriptions',
            name='subs_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
