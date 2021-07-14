# Bot.py
import discord
from discord.ext import commands
import asyncio
from datetime import date
import calendar

curr_date = date.today()
client = commands.Bot(command_prefix = '/', case_insensitive = True)

@client.event
async def on_ready():
  print('Bot online')

@client.command()
async def ola(ctx):
  if ctx.author.name == 'ͳʋʐ⁝ͷ':
    await ctx.send(f'oi {ctx.author.name} meu criador :)')
  else:
    await ctx.send(f'Olá {ctx.author.name}')


@client.command()
async def aula(ctx):
  if Bd == ('Hoje é Segunda') and ctx.author.name == 'ͳʋʐ⁝ͷ':
    await ctx.send('Oii os seus horários hoje são: Matemática,Ed. Física,Matemática,Química,História,Inglês')
  elif Bd == ('Hoje é Segunda') and ctx.author.name == 'Brenovick':
    await ctx.send('Oii os seus horários hoje são: Inglês, Química, Sociologia, Literatura, Matemática e História')
  elif Bd == ('Hoje é Segunda') and ctx.author.name == 'luvas':
    await ctx.send('Oii os seus horários hoje são: Inglês, Química, Sociologia, Literatura, Matemática e História')
  elif Bd == ('Hoje é Terça') and ctx.author.name == 'ͳʋʐ⁝ͷ':
    await ctx.send('Oii os seus horários hoje são: Religião,Matemática,Sociologia,Prod. de Texto,Geografia,Biologia,Química,Biologia,Arte,Química.')
  elif Bd == ('Hoje é Terça') and ctx.author.name == 'Brenovick':
    await ctx.send('Oii os seus horários hoje são: Filosofia, Produção, Geografia, Matemática, Biologia, Matemática, Inglês, Química, Biologia e Artes.')
  elif Bd == ('Hoje é Terça') and ctx.author.name == 'luvas':
    await ctx.send('Oii os seus horários hoje são: Filosofia, Produção, Geografia, Matemática, Biologia, Matemática, Inglês, Química, Biologia e Artes.')
  elif Bd == ('Hoje é Quarta') and ctx.author.name == 'ͳʋʐ⁝ͷ':
    await ctx.send('Oii os seus horários hoje são: História, Literatura, Lingua portuguesa, Geografia, Prod. de Texto,Filosofia')
  elif Bd == ('Hoje é Quarta') and ctx.author.name == 'luvas':
    await ctx.send('Oii os seus horários hoje são: Português, Educação Física, Históra, Literatura, Geografia, Produção')
  elif Bd == ('Hoje é Quarta') and ctx.author.name == 'Brenovick':
    await ctx.send('Oii os seus horários hoje são: Português, Educação Física, Históra, Literatura, Geografia, Produção')
  else:
    await ctx.send('Calma amigão estamos trabalhando para que seus horários sejam fornecidos')

@client.command()
async def bomdia(ctx):
    await ctx.send(f'Bom dia {ctx.author.name} {Bd}')

@client.command()
async def dia(ctx):
    await ctx.send(f'{Bd}')

@client.command()
async def nome(ctx):
    await ctx.send('Meu nome é robot')


if (calendar.day_name[curr_date.weekday()]) == 'Monday':
  Bd = ('Hoje é Segunda')
elif (calendar.day_name[curr_date.weekday()]) == 'Tuesday':
  Bd = ('Hoje é Terça')
elif (calendar.day_name[curr_date.weekday()]) == 'Wednesday':
  Bd = ('Hoje é Quarta')
elif (calendar.day_name[curr_date.weekday()]) == 'Thursday':
  Bd = ('Hoje é Quinta')
elif (calendar.day_name[curr_date.weekday()]) == 'Friday':
  Bd = ('Hoje é Sexta VAMOOOOOOOOO')
elif (calendar.day_name[curr_date.weekday()]) == 'Saturday':
  Bd = ('Hoje é Sabadin')
elif (calendar.day_name[curr_date.weekday()]) == 'Sunday':
  Bd = ('Hoje é Domingo')

print(Bd)

client.run('Token do seu Bot')
