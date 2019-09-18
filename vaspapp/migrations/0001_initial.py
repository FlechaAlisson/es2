# Generated by Django 2.2.4 on 2019-09-17 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('rg', models.PositiveIntegerField(blank=True, default=None, null=True, unique=True)),
                ('cpf', models.PositiveIntegerField(default=None, unique=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('duracao', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('periodo', models.CharField(choices=[('INTEGRAL', 'Integral'), ('MATUTINO', 'Matutino'), ('VESPERTINO', 'Vespertino'), ('NOTURNO', 'Noturno')], max_length=10)),
                ('cargaHoraria', models.PositiveIntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('serie', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('tipo', models.CharField(choices=[('ANUAL', 'Anual'), ('SEMESTRAL', 'Semestral')], max_length=10)),
                ('cargaHoraria', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaspapp.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('rg', models.PositiveIntegerField(blank=True, default=None, null=True, unique=True)),
                ('cpf', models.PositiveIntegerField(default=None, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaspapp.Curso')),
                ('disciplinas', models.ManyToManyField(blank=True, related_name='professores', to='vaspapp.Disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Disciplina')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(blank=True, default=None, null=True)),
                ('data', models.DateField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Matricula')),
            ],
        ),
        migrations.AddField(
            model_name='matricula',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Turma'),
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('presenca', models.BooleanField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vaspapp.Matricula')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaspapp.Instituicao'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaspapp.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='turmas',
            field=models.ManyToManyField(blank=True, related_name='alunos', through='vaspapp.Matricula', to='vaspapp.Turma'),
        ),
    ]
