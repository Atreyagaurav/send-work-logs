import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import datetime
from jinja2 import Template
import json

class WorkLog:
    def __init__(self,name='Your Name',email="yourmail@eydean.com"):
        self.name=name
        self.email=email
        self.mailto='samplemail@eydean.com'
        self.cc=None
        self.date=datetime.date.today()
        self.worklog={
        'task_of_today':[],
        'task_completed':[],
        'problems_faced':[],
        'solved_problems':[],
        'unsolved_problems':[],
        'planning_for_tomorrow':[]}
        self.html_body=None
        self.rendered_html=None
    
    def load_html(self):
        with open("mail_template.html") as reader:
            self.html_body=reader.read()
        html_template=Template(self.html_body)
        self.rendered_html=html_template.render(date=self.date, \
            task_today=self.worklog['task_of_today'], \
                task_completed=self.worklog['task_completed'], \
                    issues=self.worklog['problems_faced'], \
                        solved_problems=self.worklog['solved_problems'], \
                            unsolved_problems=self.worklog['unsolved_problems'], \
                                plans_tomorrow=self.worklog['planning_for_tomorrow'])
    
    def save_worklog(self):
        with open("worklog.json","r") as json_file:
            log=json.load(json_file)
        log.append({str(self.date):self.worklog})
        with open("worklog.json","w") as json_file:
            json.dump(log,json_file)
    
    def input_logs(self):
        for key in self.worklog:
            print("Enter: "+key+":<enter twice to end>:")
            input_string=None
            while (input_string!=''):
                if input_string:
                    self.worklog[key].append(input_string)
                input_string=input(">")

    def send_mail(self):
        print("Creating email.... Please wait...")
        MY_KEY=os.getenv('MY_ZOHO_KEY')
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.mailto
        msg['Subject'] = "Work Log: "+self.name
        msg.attach(MIMEText(self.rendered_html, 'html'))
        server = smtplib.SMTP('smtp.zoho.com:587')
        server.starttls()
        server.login(self.email,MY_KEY)
        text = msg.as_string()
        print("Sending email.... Please wait...")
        server.sendmail(self.email, self.mailto, text)
        server.quit()
        print("Process completed, your email is sent.")

if __name__=="__main__":
    try:
        log=WorkLog()
        log.input_logs()
        log.save_worklog()
        log.load_html()
        log.send_mail()
    except KeyboardInterrupt:
        print("Process terminated..")
