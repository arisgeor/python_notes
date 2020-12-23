#! python3

#A list of all the libraries I' ve used.
#those that need to be istalled have a comment next to them.

#Standard Library
import time
import datetime
import json
import tkinter
import pprint
import os
import shelve
import re
import webbrowser
import pyperclip
import smtplib 

#
import pyautogui                #pip install pyautogui
import PyPDF2                   #pip install PyPDF2
import docx                     #pip install python-docx
import openpyxl                 #pip install openpyxl 
import requests                 #pip install requests
import bs4                      #pip install beautifulsoup4
from selenium import webdriver  #pip install selenium
import rich                     #pip install rich
import PIL                      #pip install Pillow 
import numpy                    #pip install numpy
import pandas                   #pip install pandas
import cv2                      #pip install opencv-python
import pygame                   #pip install -U pygame --user #python3 -m pygame.examples.aliens to check if it worked :P
from pyowm.owm import OWM       #pip install pyowm

from flask import Flask         #pip install Flask
#for Flask, first open the powershell as an admin and type: 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine #then choose 'A'
#then, create your project folder and inside it
py -m venv env                  #to create the virtual enviroment "env"
# Then, env\Scripts\activate 
#to activate it and finaly after you create 'yourfile.py'
set FLASK_APP=yourfile.py
flask run


