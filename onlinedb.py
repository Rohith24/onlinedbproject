import os,django,sys,click,openpyxl
sys.path.append("F:\Summer\onlinedbproject")
os.environ["DJANGO_SETTINGS_MODULE"] = "onlinedbproject.settings"
django.setup()
import MySQLdb
from mrnd.models import *
from django.shortcuts import *
from django.db.models import *
db = MySQLdb.connect(host="localhost", port=90, user="root", passwd="admin", db="mysql")
cursor = db.cursor()
@click.group()
def cli():
    pass

@cli.command()
#@click.argument('username',nargs=1,click.Path.type)
def createdb():
    try:
        cursor.execute("create database classproject")
        print "database created"
    except:
        print "database alreay exits"
    os.system("python manage.py makemigrations")
    os.system("python manage.py migrate")

@cli.command()
def dropdb():
    cursor.execute("DROP DATABASE IF EXISTS classproject")
    print "database droped"

@cli.command(help="store data in database")
@click.argument('studentsfile',nargs=1,type=click.Path(exists=True))
@click.argument('marksfile',nargs=1,type=click.Path(exists=True))
def populate(studentsfile,marksfile):
    wb=openpyxl.load_workbook(studentsfile)
    college_sheet = wb["Colleges"]
    for row in range(2, college_sheet.max_row+1):
        c=College(name=college_sheet.cell(row=row,column=1).value,Acronym=college_sheet.cell(row=row,column=2).value,
                   location=college_sheet.cell(row=row,column=3).value,contact=college_sheet.cell(row=row,column=4).value)
        c.save()
    c=College.objects.all()
    current_students_sheet = wb["Current"]
    for row in range(2, current_students_sheet.max_row + 1):
        s = Student(name=current_students_sheet.cell(row=row, column=1).value,
                     college_id=c.get(Acronym=current_students_sheet.cell(row=row, column=2).value).id,
                     emailid=current_students_sheet.cell(row=row, column=3).value,
                     dbnames=current_students_sheet.cell(row=row, column=4).value,
                     droppedout=0)
        s.save()
    deleted_students_sheet = wb["Deletions"]
    for row in range(2, deleted_students_sheet.max_row + 1):
        s = Student(name=deleted_students_sheet.cell(row=row, column=1).value,
                     college_id=c.get(Acronym=deleted_students_sheet.cell(row=row, column=2).value).id,
                     emailid=deleted_students_sheet.cell(row=row, column=3).value,
                     dbnames=deleted_students_sheet.cell(row=row, column=4).value,
                     droppedout=1)
        s.save()
    s=Student.objects.all()
    marks_wb=openpyxl.load_workbook(marksfile)
    marks_sheet = marks_wb.active
    for row in range(2, marks_sheet.max_row + 1):
        m = Mark(student_id=s.get(dbnames=marks_sheet.cell(row=row, column=1).value.split('_')[2]).id,
                  transform=marks_sheet.cell(row=row, column=2).value,
                  from_custom_base26=marks_sheet.cell(row=row, column=3).value,
                  get_pig_latin=marks_sheet.cell(row=row, column=4).value,
                  top_chars=marks_sheet.cell(row=row, column=5).value,
                  total = marks_sheet.cell(row=row, column=6).value)
        m.save()

@cli.command(help="clear data in database")
def clear():
    Student.objects.all().delete()
    Mark.objects.all().delete()
    College.objects.all().delete()

@cli.command(help="send mail")
@click.argument('clg_acronym',nargs=1,type=click.Path())
@click.argument('emailid',nargs=1,type=click.Path())
def sendsummary(clg_acronym,emailid):
    from django.template.loader import render_to_string
    import smtplib
    to = emailid
    from_email = 'krishna.rohith.sai@gmail.com'
    password = 'Rohith24sai31&@1996'
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(from_email, password)
    from email.mime.text import MIMEText
    colleges = College.objects.get(Acronym=clg_acronym)
    students = colleges.student_set.all()
    message = render_to_string('emailid.html', {"students": students,
                                                "total_Avg":Mark.objects.all().aggregate(Min('total'),Max('total'),Avg('total'))['total__avg'],
                                                "clg_avg":Mark.objects.filter(student__college__Acronym=clg_acronym).values_list('student__college__Acronym').annotate(avg=Avg('total'),min=Min('total'),max=Max('total'))[0][2]})

    msg = MIMEText(message,'html')
    msg['Subject'] = "Results of Students"
    msg['From'] = from_email
    msg['To'] = to

    #msg.get_content_type()
    s.sendmail(from_email, [to], msg.as_string())
    s.quit()

if __name__ =='__main__':
    cli()