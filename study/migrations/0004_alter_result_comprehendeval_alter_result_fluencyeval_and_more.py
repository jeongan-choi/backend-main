# Generated by Django 5.0 on 2024-01-09 00:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("study", "0003_rename_ko_text_audiofile_sentence_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="ComprehendEval",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="result",
            name="FluencyEval",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="result",
            name="PronunProfEval",
            field=models.FloatField(),
        ),
    ]
