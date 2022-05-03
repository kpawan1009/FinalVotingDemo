import uuid

# views.py
from django.shortcuts import redirect,HttpResponseRedirect
from django.shortcuts import render

from . import models
from . import vote
from .sendsms import sendsms


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def home(request):

    if request.method=='POST':
        name2 = request.POST['name2']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        feedback = request.POST['feedback']
        ins = models.Feedback(name2=name2, email=email, phonenumber=phonenumber, feedback=feedback)
        ins.save()

    return render(request,'index.html')

def about(request):

    return render(request,'about.html')

def candidateaura(request):
    allTasks = models.Candidateaura.objects.all()
    context = {'task': allTasks}
    return render(request,'candidateaura.html',context)

def candidatepalg(request):
    allTasks = models.Candidatepalg.objects.all()
    context = {'task': allTasks}
    return render(request,'candidatepalg.html',context)

def amroha(request):

    success = False
    x=1
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name3'):
            uniqueid=request.POST['name3']
            address=request.POST['address3']
            phonenumber=request.POST['phonenumber3']
            email=request.POST['email3']
            alluid=models.UIDamroha.objects.get(uniqueid=uniqueid)
            pannumber =alluid.pannumber
            allobjects =models.Voterregisteredamroha.objects.get(pannumber=pannumber)
            name=allobjects.name
            age=allobjects.age
            ins = models.Voterregisteredamroha(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)

            ins2=models.Voterregisteredamroha.objects.get(pannumber=pannumber)
            ins2.delete()
            ins.save()


        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Amroha"

            allTasks = models.Votergovt.objects.all()
            # uidcheck=models.UIDamroha.objects.all()
            x = str(uuid.uuid1())
            while models.UIDamroha.objects.filter(uniqueid=x):
                x = str(uuid.uuid1())
            x=str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDamroha(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredamroha(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency,age=age).exists())and (not models.Voterregisteredamroha.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                vote.abcd()
                vote.vote(name,age,pannumber,x)
                success = True
                ins2.save()
                y="+91"+str(phonenumber)
                sendsms(mess=x,ph=y)
                context = {'success': success, 'uid': x}

            else:
                 success = False
        if request.POST.get('uid'):
            print('form 2')
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDamroha.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidateaura.objects.all()
                context={'task':allTasks}
                return render(request,'voteaura.html',context)
        if request.POST.get('phonenumber2'):
            print('form 2')
            phonenumber=request.POST['phonenumber2']
            pannumber=str(request.POST['pan2'])
            name=str(request.POST['name2'])
            if models.Voterregisteredamroha.objects.filter(pannumber=pannumber,name=name):
                UIDN=models.UIDamroha.objects.all()
                context={'task':UIDN}
                return render(request,'')

    return render(request,'amroha.html',context)
# context = {'success': 'success', 'uid': 'x'}
# global uniqueid
def palghar(request):
    success = False
    x=1
    # global uniqueid
    # uniqueid=""
    context = {'success': success, 'uid': x}
    print(success)
    if request.method == "POST":
        if request.POST.get('name3'):
            # global uniqueid
            uniqueid = str(request.POST['name3'])

            address = request.POST['address3']
            phonenumber = request.POST['phonenumber3']
            email = request.POST['email3']
            alluid = models.UIDpalghar.objects.get(uniqueid=uniqueid)
            pannumber = alluid.pannumber
            allobjects = models.Voterregisteredpalghar.objects.get(pannumber=pannumber)
            name = allobjects.name
            age = allobjects.age
            ins = models.Voterregisteredpalghar(name=name, age=age, address=address, pannumber=pannumber, email=email,
                                               phonenumber=phonenumber)

            ins2 = models.Voterregisteredpalghar.objects.get(pannumber=pannumber)
            ins2.delete()
            ins.save()



        if request.POST.get('name'):
            print("yesss")
            name = request.POST['name']
            age = int(request.POST['age'])
            address = request.POST['address']
            pannumber = request.POST['pannumber']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            constituency = "Palghar"
            allTasks = models.Votergovt.objects.all()
            x = str(uuid.uuid1())
            while models.UIDpalghar.objects.filter(uniqueid=x):
                x = str(uuid.uuid1())
            x = str(x[0:10])
            # send_mail(
            #     'UID Generated for evoting',
            #     x,
            #     'noreplyvamp@yahoo.com',
            #     [email],
            #     fail_silently=False,
            # )

            ins2 = models.UIDpalghar(pannumber=pannumber, uniqueid=x)
            ins = models.Voterregisteredpalghar(name=name, age=age, address=address, pannumber=pannumber, email=email,phonenumber=phonenumber)
            if (models.Votergovt.objects.filter(name=name, pannumber=pannumber,constituency=constituency,age=age).exists())and (not models.Voterregisteredpalghar.objects.filter(name=name,pannumber=pannumber).exists())and(age>=18):
                ins.save()
                success = True
                ins2.save()
                vote.abcd()
                vote.vote(name,age,pannumber,x)
                y = "+91" + str(phonenumber)
                sendsms(mess=x, ph=y)
                context = {'success': success, 'uid': x}

            else:
                 success = False
        if request.POST.get('uid'):
            print('form 2')
            # global uniqueid
            uniqueid=str(request.POST['uid'])
            pannumber=str(request.POST['pan'])
            if models.UIDpalghar.objects.filter(uniqueid=uniqueid,pannumber=pannumber).exists():
                print("Yes you are on correct page")
                allTasks = models.Candidatepalg.objects.all()
                context={'task':allTasks}
                # return render(request, 'votepalg.html', context)
            # if request.POST.get('pannumber1'):
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     print("YES YES YES YES")
            #     print("______________")
            #     print("______________")
            #     print("______________")
            #     vote.Voting1(uniqueid)
            #
            # if request.POST.get('pannumber2'):
            #     vote.Voting2(uniqueid)
            # if request.POST.get('VOTE 3'):
            #     vote.Voting3(uniqueid)
            # return render(request,'votepalg.html',context)
            return redirect('votehere/')
        # def getid():
        #     return uniqueid

    return render(request,'palghar.html',context)

def votepalghar(request):
    allTasks = models.Candidatepalg.objects.all()
    context = {'task': allTasks}
    # if request.method=='POST':
    #     if request.POST.get('VOTE 1'):
    #         print("*************")
    #         print("*************")
    #         print("*************")
    #
    #         # uniqueid=request.POST['uniqueid1']
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         #
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #     if request.POST.get('VOTE 2'):
    #         print("2222222222222")
    #         print("2222222222222")
    #         print("2222222222222")
    #         # uniqueid = request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #
    #     if request.POST.get('VOTE 3'):
    #         pass
    #         # uniqueid=request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    if request.method=="POST":
        if request.POST.get('UID1'):
            uid1 = request.POST['UID1']
            if models.UIDpalghar.objects.filter(uniqueid=uid1).exists():

                vote.Voting1(uid1)
        if request.POST.get('UID2'):
            uid2 = request.POST['UID2']
            if models.UIDpalghar.objects.filter(uniqueid=uid2).exists():

                vote.Voting2(uid2)
        if request.POST.get('UID3'):
            uid3 = request.POST['UID3']

            if models.UIDpalghar.objects.filter(uniqueid=uid3).exists():
                vote.Voting3(uid3)
        return HttpResponseRedirect('/')
    return render(request,'votepalg.html',context)


def voteamroha(request):
    allTasks = models.Candidateamroha.objects.all()
    context = {'task': allTasks}
    # if request.method=='POST':
    #     if request.POST.get('VOTE 1'):
    #         print("*************")
    #         print("*************")
    #         print("*************")
    #
    #         # uniqueid=request.POST['uniqueid1']
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         #
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #     if request.POST.get('VOTE 2'):
    #         print("2222222222222")
    #         print("2222222222222")
    #         print("2222222222222")
    #         # uniqueid = request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # print(uniqueid)
    #         # vote.Voting1(uniqueid)
    #
    #         # return HttpResponseRedirect('/')
    #
    #     if request.POST.get('VOTE 3'):
    #         pass
    #         # uniqueid=request.POST['uniqueid1']
    #
    #         # uniqueid=palghar(request).getId()
    if request.method=="POST":
        if request.POST.get('UID1'):
            uid1 = request.POST['UID1']
            if models.UIDpalghar.objects.filter(uniqueid=uid1).exists():
                pass
                # vote.Voting1(uid1)
        if request.POST.get('UID2'):
            uid2 = request.POST['UID2']
            if models.UIDpalghar.objects.filter(uniqueid=uid2).exists():
                pass
                # vote.Voting2(uid2)
        if request.POST.get('UID3'):
            uid3 = request.POST['UID3']

            if models.UIDpalghar.objects.filter(uniqueid=uid3).exists():
                pass
                # vote.Voting3(uid3)
        return HttpResponseRedirect('/')
    return render(request,'voteamroha.html',context)

def thankyou(request):
    return render(request,'thankyou.html')

def winnervote(request):

    win=vote.winner()
    winner={'sno':1,'name':'AMD - Manohar'}
    if win==1:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 1 \n AMD - Manohar')

    elif win == 2:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 2 \n AMD - Prashant')

    elif win==3:
        # winner = {'sno': 1, 'name': 'AMD - Manohar'}
        print('Party Serial Number : 3 \n CMD - Praveen')

    else :
        print('No winner its either a tie or no one has voted yet')

    return render(request,'winner.html',winner)

