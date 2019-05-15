
import mysql.connector
from mysql.connector import MySQLConnection, Error
from mysql import connector
from selenium import webdriver
from bs4 import BeautifulSoup

class DataLayer():
    def __init__(self):
        self.SalvarNaBase()

    def SalvarNaBase(self):


        con = connector.Connect(user='admin',password='c299792458MS',database='RyanAirCrawler',host='ryanaircrawler.cc4lk5lhz49s.us-east-2.rds.amazonaws.com')

        try:

            cursor = con.cursor()
            cursor.execute("INSERT INTO TBL_COUNTRIES(CountryName) VALUES ('Teste Git 5 - Aqui é Brasil porra!');")
            con.commit()

        except expression as identifier:
            pass


insert = DataLayer()