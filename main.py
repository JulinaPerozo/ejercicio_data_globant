from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="1234",
  database="trabajo_practico"
)

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           parseCSV(file_path)
          # save the file
      return redirect(url_for('index'))

def parseCSV(filePath):
    # CVS Column Names
    col_names = ['id','NAME', 'datetime', 'department_id' , 'job_id']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    # Loop through the Rows
    mycursor = mydb.cursor()
    for i,row in csvData.iterrows():
            sql = "INSERT INTO hired_employees (id,NAME,datetime,department_id,job_id) VALUES (%s, %s, %s, %s, %s)"
            value = (row['id'],row['NAME'],row['datetime'],row['department_id'],row['job_id'])
            mycursor.execute(sql, value)
            mydb.commit()

def parseCSV(filePath):
    # CVS Column Names
    col_names = ['id','department']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    # Loop through the Rows
    mycursor = mydb.cursor()
    for i,row in csvData.iterrows():
            sql = "INSERT INTO departments (id,department) VALUES (%s, %s)"
            value = (row['id'],row['department'])
            mycursor.execute(sql, value)
            mydb.commit()

def parseCSV(filePath):
    # CVS Column Names
    col_names = ['id','job']
    # Use Pandas to parse the CSV file
    csvData = pd.read_csv(filePath,names=col_names, header=None)
    # Loop through the Rows
    mycursor = mydb.cursor()
    for i,row in csvData.iterrows():
            sql = "INSERT INTO jobs (id,job) VALUES (%s, %s)"
            value = (row['id'],row['job'])
            mycursor.execute(sql, value)
            mydb.commit()

if file_path== 'hired_employees.csv':
    sql='INSERT INTO hired_employees (id,NAME,datetime,department_id,job_id) VALUES (%s, %s, %s, %s, %s)'
    value = (row['id'],row['NAME'],row['datetime'],row['department_id'],row['job_id'])
elif file_path== 'deparments.csv':
    sql='INSERT INTO departments (id,department) VALUES (%s, %s)'
    value = (row['id'],row['department'])
elif file_path== 'jobs.csv':
    sql='INSERT INTO jobs (id,job) VALUES (%s, %s)'
    value = (row['id'],row['job'])


if (__name__ == "__main__"):
     app.run(port = 5000)