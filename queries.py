import os,django,sys,click,openpyxl
sys.path.append("F:\Summer\onlinedbproject")
os.environ["DJANGO_SETTINGS_MODULE"] = "onlinedbproject.settings"
django.setup()
from mrnd.models import *
from django.db.models import *
clgs=College.objects.all()
print clgs
print clgs.count()
acronym_contact=College.objects.values('Acronym','contact')
print acronym_contact
clgs.filter(location__contains="Vizag").count()


print clgs.order_by('Acronym')
print clgs.order_by('-location')
print clgs.order_by('-location')[:5]
print clgs.order_by('-location')[5:10]
print clgs.order_by('-location')[10:]

print clgs.values('location').annotate(Count('location'))
print clgs.values('location').annotate(Count('location')).order_by('location')
print clgs.values('location').annotate(Count('location')).order_by('-location__count')
print College.objects.values('Acronym','contact').order_by('location')


stds=Student.objects
print stds.count()
print stds.filter(name__icontains="rohit")
print stds.filter(college__Acronym="bvritn")
print stds.values_list('college__Acronym').annotate(Count('college__Acronym'))
print stds.values_list('college__Acronym').annotate(count=Count('college__Acronym')).order_by('-count')
print stds.values_list('college__Acronym').annotate(count=Count('college__Acronym')-2).order_by('-count')
print stds.values_list('college__location').annotate(count=Count('college__location'))
print stds.values('college__location').annotate(count=Count('college__location')).order_by('-count')[0]
print Student.objects.mark_set.all()
print Student.objects.values_list('college__Acronym').annotate(count=Count('college__Acronym'))
print Teachers.objects.values_list('college__Acronym').annotate(count=Count('college__Acronym'))

print College.objects.annotate(std_count=Count('student')).values_list("Acronym","std_count")
print College.objects.annotate(tec_count=Count('teacher')).values_list("Acronym","tec_count")

print College.objects.annotate(std_count=Count('student',distinct=True), tec_count=Count('teacher',distinct=True)).values_list("Acronym", "std_count","tec_count").query
print College.objects.annotate(std_count=Count('student',distinct=True), tec_count=Count('teacher',distinct=True)).values_list("Acronym", "std_count","tec_count")




m=Mark.objects
print m.values_list('student__name','student__college__Acronym','total').order_by('-total')
print m.values_list('student__name','student__college__Acronym','total').filter(total__gte=30).order_by('-total')
print m.aggregate(Count('total'))
print m.all().filter(total__gte=30)
print Mark.objects.values_list('student__college__Acronym').annotate(std_count=Count('student__college__Acronym'),avg=Avg('total'))
print Mark.objects.all().aggregate(Min('total'),Max('total'),Avg('total'))
print College.objects.all()
print m.all().values_list('student__college__Acronym').annotate(avg=Avg('total'),min=Min('total'),max=Max('total'))
print Mark.objects.filter(student__college__Acronym='bec').annotate(avg=Avg('total'),min=Min('total'),max=Max('total'))

