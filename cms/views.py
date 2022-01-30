from django.shortcuts import render
from django.db.models import Sum, Avg
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import MP, Constituency, Work, Feedback
from django.template import loader


def index(request):
    template = loader.get_template('cms/index.html')
    constituency_list = Constituency.objects.all()
    
    bestconstirating = Feedback.objects.filter(against="CONSTITUENCY").values('against_id').annotate(Avg('rating')).order_by('-rating__avg')[:3]
    
    bestconstidic = []
    count = 1
    for item in bestconstirating:
        inlist = []
        cid = item['against_id']
        rate = item['rating__avg']
        constiInfo = Constituency.objects.get(pk=item['against_id'])
        name  = constiInfo.name
        mp = constiInfo.mp
        inlist=[count, name, rate, mp]
        bestconstidic.append(inlist)
        count = count + 1
    
    worstconstirating = Feedback.objects.filter(against="CONSTITUENCY").values('against_id').annotate(Avg('rating')).order_by('rating__avg')[:3]
    
    worstconstidic = []
    count = len(worstconstirating)
    for item in worstconstirating:
        inlist = []
        cid = item['against_id']
        rate = item['rating__avg']
        constiInfo = Constituency.objects.get(pk=item['against_id'])
        name  = constiInfo.name
        mp = constiInfo.mp
        inlist=[count, name, rate, mp]
        worstconstidic.append(inlist)
        count = count - 1
    
    context = {
        'constituency_list' : constituency_list,
        'bestconstidic' : bestconstidic,
        'worstconstidic' : worstconstidic,
    }

    return HttpResponse(template.render(context, request))
    

def mp(request, mp_id):
    MPDetail = MP.objects.get(pk=mp_id)

    template = loader.get_template('cms/mp.html') 
    context = {
        'MPDetail' : MPDetail,
    }

    return HttpResponse(template.render(context, request))

    
def constituency(request, constituency_id):
    constituencyDetail = Constituency.objects.get(pk=constituency_id)
    
    
    workdone = Work.objects.filter(constituency=constituency_id, status='DONE')
    workinprogress = Work.objects.filter(constituency=constituency_id, status='INPROGRESS')
    worknew = Work.objects.filter(constituency=constituency_id, status='NEW')
    
    rating = Feedback.objects.filter(against_id=constituency_id, against="CONSTITUENCY").aggregate(Avg('rating'))['rating__avg']

    comments = Feedback.objects.filter(against_id=constituency_id, against="CONSTITUENCY").values("detail", "rating").order_by("-id")[:3]
    
    template = loader.get_template('cms/constituency.html') 
    context = {
        'constituencyDetail' : constituencyDetail,
        'workdone' : workdone,
        'workinprogress' : workinprogress,
        'worknew' : worknew,
        'rating' : rating,
        'comments' : comments,
    }



    return HttpResponse(template.render(context, request))


def work(request, work_id):
    workDetail = Work.objects.get(pk=work_id)
    rating = Feedback.objects.filter(against_id=work_id, against="WORK").aggregate(Avg('rating'))['rating__avg']
    comments = Feedback.objects.filter(against_id=work_id, against="WORK").values("detail", "rating").order_by("-id")[:3]
 
    template = loader.get_template('cms/work.html') 
    
    context = {
        'workDetail' : workDetail,
        'rating' : rating,
        'comments' : comments,
    }
    
    return HttpResponse(template.render(context, request))
    
    
def feedback(request, item_id, item):
    
    if item == 'WORK':
        if request.method == 'POST':
        
            textarea = request.POST['textarea']
            rating = request.POST['rating']

            f = Feedback(against="WORK", against_id=item_id, detail=textarea, rating=rating)
            f.save()
        
            return work(request, item_id)
            # workDetail = Work.objects.get(pk=work_id)
            # rating = Feedback.objects.filter(against_id=work_id, against="WORK").aggregate(Avg('rating'))['rating__avg']
            # template = loader.get_template('cms/work.html') 
            # context = {
            #     'workDetail' : workDetail,
            #     'rating' : rating,
            # }
        
        else :
            workBrief = Work.objects.filter(pk=item_id).values('brief')
            template = loader.get_template('cms/feedback.html')
            context = {
                'workBrief' : workBrief[0]['brief'],
            }
    
    
    if item == 'CONSTITUENCY':
        if request.method == 'POST':
            textarea = request.POST['textarea']
            rating = request.POST['rating']

            f = Feedback(against="CONSTITUENCY", against_id=item_id, detail=textarea, rating=rating)
            f.save()
        
            return constituency(request, item_id)

        else :
            workBrief = Constituency.objects.filter(pk=item_id).values('name')
            template = loader.get_template('cms/feedback.html')
            context = {
                'workBrief' : workBrief[0]['name'],
            }
        
     
    

    return HttpResponse(template.render(context, request))
    
