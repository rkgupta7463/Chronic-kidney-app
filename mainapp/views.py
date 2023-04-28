from django.shortcuts import render,HttpResponse
import pandas as pd
import pickle as pkl

model=pkl.load(open("kidney_model_upgrade.pkl","rb"))

# Create your views here.
def main(request):
    prediction=None
    fname=""
    lname=""
    fullname=None
    address=None
    email=None
    rs=None
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        bp=request.POST.get('bp')
        sg=request.POST.get('sg')
        al=request.POST.get('Aluminum')
        su=request.POST.get('su')
        Rbc=request.POST.get('Rbc')
        bu=request.POST.get('bu')
        Sc=request.POST.get('Sc')
        Sod=request.POST.get('Sod')
        Pot=request.POST.get('Pot')
        Hemo=request.POST.get('Hemo')
        Wbcc=request.POST.get('Wbcc')
        Rbcc=request.POST.get('Rbcc')
        Htn=request.POST.get('Htn')


        # print(bp)    
        # print(type(bp))    
        # print(sg)    
        # print(type(sg)) 
        # print(al)   
        # print(type(al))    
        ##converting into int
        # BP=int(bp)
        # SG=int(sg)
        # AL=int(al)
        # SU=int(su)
        # RBC=int(Rbc)
        # BU=int(bu)
        # SC=int(Sc)
        # SOD=int(Sod)
        # POT=int(Pot)
        # HEMO=int(Hemo)
        # WBCC=int(Wbcc)
        # RBCC=int(Rbcc)
        # HTN=int(Htn)
        # print(BP)    
        # print(type(BP))    
        # print(SG)    
        # print(type(SG)) 
        # print(AL)   
        # print(type(AL))  

        ##converting integer into float dtype  
        BPF=float(bp)
        SGF=float(sg)
        ALF=float(al)
        SUF=float(su)
        RBCF=float(Rbc)
        BUF=float(bu)
        SCF=float(Sc)
        SODF=float(Sod)
        POTF=float(Pot)
        HEMOF=float(Hemo)
        WBCCF=float(Wbcc)
        RBCCF=float(Rbcc)
        HTNF=float(Htn)
        print(BPF)    
        print(type(BPF))    
        print(SGF)    
        print(type(SGF)) 
        print(ALF)   
        print(type(ALF)) 
        # SU=float(su)
        # RBC=float(Rbc)
        # BU=float(bu)
        # SC=float(Sc)
        # SOD=float(Sod)
        # POT=float(Pot)
        # HEMO=float(Hemo)
        # WBCC=float(Wbcc)
        # RBCC=float(Rbcc)
        # HTN=float(Htn)


    #     print(bp)

        prediction=model.predict(pd.DataFrame([[BPF,SGF,ALF,SUF,RBCF,BUF,SCF,SODF,POTF,HEMOF,WBCCF,RBCCF,HTNF]],columns=['Bp','Sg','Al','Su','Rbc','Bu','Sc','Sod','Pot','Hemo','Wbcc','Rbcc','Htn']))
    
        if prediction == 1:
            rs='Patients has no kidney Problem'

        else:
            rs='Patients has kidney Problem'

    print(rs)    

    context={
        "fullname":fname+" "+lname,
        "rs":rs,
        "address":address,
        "email":email, 
    }    

    return render(request,"index.html",context)