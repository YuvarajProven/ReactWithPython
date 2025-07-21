from django.views import View
from django.http import HttpResponse
import mysql.connector

class APICheck(View):
    def get(self, request):
        print("API Checked")
        return HttpResponse("Successfully Tested")
    
class Hi(View):
    def get(self,request):
        print("hello")
        return HttpResponse("hekko")
    
class DBCheck(View):
     def get(self, request):
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="" ,
                port=3306,
                db="ipv",
                ssl_disabled=True
            )
            print("Connected")
            return HttpResponse("Connected to database successfully.")
        except mysql.connector.Error as err:
            print("Not connected:", err)
            return HttpResponse("Failed to connect to the database.")