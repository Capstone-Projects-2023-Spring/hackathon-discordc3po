# Main.py
import os
import random
import requests
import json
from datetime import datetime
from datetime import date
# py -3 -m pip install requests


import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

url = "https://courses.ianapplebaum.com/api/syllabus/1"

headers = {
    "Authorization": "Bearer Fx0DqSXhWUHIdZV6AdJb7lowPgXrEVxPHX6YZ9tk",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# response = requests.request("GET", url, headers=headers)

# print(response.json()["events"])

# print("\n-----ASSIGNMENTS-----")
# for ass in response.json()["events"]:
#     if ass["class_type"] == "Assignment":
#         print(ass["event_name"])

# print("\n-----LAB-----")
# for ass in response.json()["events"]:
#     if ass["class_type"] == "Lab":
#         print(ass["event_name"])


@client.event
async def on_message(message):
    if message.author == client.user: # Prevent response to self (bot)
        return

    if message.content == '!week':
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n-----ASSIGNMENTS DUE THIS WEEK-----\n"

        eventsFound = 0 # Set events found to 0 on request 

        # Loop through API and find all entries where class_type in Assignment
        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                if todaysCalendarWeek == eventsCalendarWeek:
                    eventsFound = eventsFound+1
                    print("eventsFound= ", eventsFound)

        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events this week: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        # Loop through API and find all entries where class_type in Assignment
        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if todaysCalendarWeek == eventsCalendarWeek:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!next':
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n-----ASSIGNMENTS DUE NEXT WEEK-----\n"

        eventsFound = 0

        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                if todaysCalendarWeek+1 == eventsCalendarWeek:
                    eventsFound = eventsFound+1
                    print("eventsFound= ", eventsFound)
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events next week: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if todaysCalendarWeek+1 == eventsCalendarWeek:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!lab':
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL LABS-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Lab":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Lab":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + "\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!lecture':
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL LECTURES-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Lecture":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Lecture":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + "\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!sprint':
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL SPRINTS-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Sprint":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Sprint":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!all':
        # Add: Labs/ Sprints/ Lectures / N\/A
        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL ASSIGNMENTS-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Assignment":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL LABS-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Lab":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Lab":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + "\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL LECTURES-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Lecture":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Lecture":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + "\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL SPRINTS-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "Sprint":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                print(ass["event_name"])
                print("todaysCalendarWeek=", todaysCalendarWeek)
                print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "Sprint":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

        response = requests.request("GET", url, headers=headers)
        megaText = "```c\n"
        megaText = megaText + "-----ALL N/A-----\n"

        eventsFound = 0
        for ass in response.json()["events"]:
            if ass["class_type"] == "N\/A":
                # date_object = datetime.strptime(
                #     ass["event_date"], '%Y-%m-%d').date()
                # today = date.today()
                # todaysCalendarWeek = today.isocalendar().week
                # eventsCalendarWeek = date_object.isocalendar().week
                # print(ass["event_name"])
                # print("todaysCalendarWeek=", todaysCalendarWeek)
                # print("eventsCalendarWeek=", eventsCalendarWeek)
                eventsFound = eventsFound+1
        # await message.channel.send("Total events next week: "+ str(eventsFound))
        addtoOutput = "Total events found: " + str(eventsFound) + "\n"
        megaText = megaText + addtoOutput

        for ass in response.json()["events"]:
            if ass["class_type"] == "N\/A":
                date_object = datetime.strptime(
                    ass["event_date"], '%Y-%m-%d').date()
                today = date.today()
                todaysCalendarWeek = today.isocalendar().week
                eventsCalendarWeek = date_object.isocalendar().week
                timeToAssignment = (date_object - today)  # int
                if 1 == 1:
                    # await message.channel.send(ass["event_date"] + " - " + ass["event_name"] + " is due in " + str(timeToAssignment.days) + " days!")
                    addEventsOutput = ass["event_date"] + " - " + ass["event_name"] + \
                        " is due in " + str(timeToAssignment.days) + " days!\n"
                    megaText = megaText + addEventsOutput

        megaText = megaText + "```"
        await message.channel.send(megaText)

    if message.content == '!help':
        print(
            f'{client.user} has received a !help from the server:\n'
        )
        response = '''```!week - all events that take place this calendar week (1-52)\n!next - all events that take place next calendar week (1-52)\n!all - all events\n```'''
        await message.channel.send(response)

    if message.content == '!debug':
        response = requests.request("GET", url, headers=headers)
        await message.channel.send("Nothing to debug")

client.run(TOKEN)
