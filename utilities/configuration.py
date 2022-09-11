"""
config
"""
import os
from selenium import webdriver
import pytest
import  requests
import configparser
from csv import DictReader
os.linesep


def getConfig():
	config = configparser.ConfigParser()
	config.read('..//utilities/properties.ini')
	return config