from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import  PatDoc,Patreg,patien_dise,Notifydatabase,Appoint,Treating
import pandas as pd
import numpy as np
from sklearn import tree
# Create your views here.
def pat(request):
    return render(request,'patsign.html')
def doc(request):
    return render(request,'docsign.html')

def doclog(request):
    return render(request,'doctor.html')
def patlog(request):
    return render(request,'patient.html')
def symptoms(request):
    return render(request,'symptoms.html')
# def predict(request):
#     if request.method=="GET":
#         s1=request.GET['s1']
#         s2=request.GET['s2']
#         s3=request.GET['s3']
#         s4=request.GET['s4']
#         pred_lis = [s1, s2, s3, s4]
#         list_of_dise=['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
#         pred_lis1 = [1 if symp in pred_lis else 0 for symp in list_of_dise]
#         pred_array = np.array(pred_lis1, dtype=np.uint8) # Reshape the input as (1, n_features) array
#         prediction=np.array()
#         print(prediction)

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        specialization = request.POST['specialization']
        hospital = request.POST['hospital']
        city = request.POST['city']
        pincode=request.POST['pincode']
        phno=request.POST['phno']
        if PatDoc.objects.filter(username=username).exists():
            return redirect('doc')
        elif PatDoc.objects.filter(email=email).exists():
            return redirect('doc')
        else:
            docauth = User.objects.create_user(username=username,password=password,is_staff=True)
            
            docauth.save()
            user = auth.authenticate(username=username,password=password)
            if user is not None :
                auth.login(request,user)
            t=request.user
            k=t.id
            user=PatDoc.objects.create(username=username,email=email,password=password,specialization=specialization,hospital=hospital,city=city,pincode=pincode,phno=phno,userid=k)
            
            user.save()
            return redirect('doclog')
    else:
        return render(request,'docsign.html')
    
# def login(request):
def patreg(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        city = request.POST['city']
        pincode=request.POST['pincode']
        phno=request.POST['phno']
        dof = request.POST['dof']
        age = request.POST['age']
        # if Patreg.objects.filter(username=username).exists():
        #     return redirect('pat')
        # elif PatDoc.objects.filter(email=email).exists():
        #     return redirect('pat')
        # else:
        patauth = User.objects.create_user(username=username,password=password,is_staff=False)
        patauth.save()
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
        t=request.user
        k=t.id
        user=Patreg.objects.create(username=username,email=email,city=city,pincode=pincode,phno=phno,dof=dof,age=age,userid=k)
        user.save()
            
        return redirect('patlog')
    else:
        return render(request,'patsign.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('intercall1')
        else:
            return redirect('login')
    else:
        return render(request,'docsign.html')



def intercall1(request):
    return render(request,'intermed1.html')


def inter1(request):
    n6 = request.POST['n6']
    if (n6 == "True"):
        return redirect('doclog')
    else:
        return redirect('login')
    
def patlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('intercall2')
        else:
            return redirect('patlogin')
    else:
        return render(request,'patsign.html')



def intercall2(request):
    return render(request,'intermed2.html')


def inter2(request):
    n6 = request.POST['n6']
    if (n6 == "False"):
        return redirect('patlog')
    else:
        return redirect('patlogin')
    

def patprofile(request):
    t=request.user
    k=t.id
    
    obj = Patreg.objects.filter(userid=k).values()
    
    return render(request,'patprofile.html',{'obj':obj})

def docprofile(request):
    cu=request.user
    k=cu.id
    obj = PatDoc.objects.filter(userid=k).values()
    return render(request,'docprofile.html',{'obj':obj})


def predict1(request):
    value = "None"
    name="None"
    if request.method == 'GET':
        l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
        'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
        'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
        'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
        'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
        'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
        'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
        'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
        'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
        'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
        'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
        'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
        'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
        'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
        'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
        'yellow_crust_ooze']

        disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
        'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
        'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
        'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
        'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
        'Impetigo']

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)

        # TESTING DATA df -------------------------------------------------------------------------------------
        df=pd.read_csv("training.csv")

        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        # print(df.head())

        X= df[l1]

        y = df[["prognosis"]]
        np.ravel(y)
        # print(y)
        # TRAINING DATA tr --------------------------------------------------------------------------------
        tr=pd.read_csv("testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        # from sklearn import tree

        clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
        clf3 = clf3.fit(X,y)

        # calculating accuracy-------------------------------------------------------------------
        # from sklearn.metrics import accuracy_score
        y_pred=clf3.predict(X_test)
        # print(accuracy_score(y_test, y_pred))
        # print(accuracy_score(y_test, y_pred,normalize=False))
        # -----------------------------------------------------
        psymptoms = []
        # psymptoms = [request.GET['s1'],request.GET['s2'],request.GET['s3'],request.GET['s4']]
        psymptoms.append(request.GET['s1'])
        psymptoms.append(request.GET['s2'])
        psymptoms.append(request.GET['s3'])
        psymptoms.append(request.GET['s4'])
        print(psymptoms)
        for k in range(0,len(l1)):
            # print (k,)
            for z in psymptoms:
                if(z==l1[k]):
                    l2[k]=1

        inputtest = [l2]
        mapping = {
    'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
    'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
    'Hypertension ': 10, 'Migraine': 11, 'Cervical spondylosis': 12, 'Paralysis (brain hemorrhage)': 13,
    'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16, 'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
    'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23, 'Alcoholic hepatitis': 24,
    'Tuberculosis': 25, 'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28,
    'Heart attack': 29, 'Varicose veins': 30, 'Hypothyroidism': 31, 'Hyperthyroidism': 32,
    'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35, '(vertigo) Paroymsal  Positional Vertigo': 36,
    'Acne': 37, 'Urinary tract infection': 38, 'Psoriasis': 39, 'Impetigo': 40
        }

       
        predict = clf3.predict(inputtest)
        predicted=predict[0]
        print(predicted)
        value = next(key for key, val in mapping.items() if val == predicted)
        print(value)
        Rheumatologist = [  'Osteoarthristis','Arthritis']
       
        Cardiologist = [ 'Heart attack','Bronchial Asthma','Hypertension ']
       
        ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo','Hypothyroidism' ]

        Orthopedist = []

        Neurologist = ['Varicose veins','Paralysis (brain hemorrhage)','Migraine','Cervical spondylosis']

        Allergist_Immunologist = ['Allergy','Pneumonia',
        'AIDS','Common Cold','Tuberculosis','Malaria','Dengue','Typhoid']

        Urologist = [ 'Urinary tract infection',
         'Dimorphic hemmorhoids(piles)']

        Dermatologist = [  'Acne','Chicken pox','Fungal infection','Psoriasis','Impetigo']
        Gastroenterologist = ['Peptic ulcer diseae', 'GERD','Chronic cholestasis','Drug Reaction','Gastroenteritis','Hepatitis E',
        'Alcoholic hepatitis','Jaundice','hepatitis A',
         'Hepatitis B', 'Hepatitis C', 'Hepatitis D','Diabetes','Hypoglycemia']
         
        if value in Rheumatologist :
           consultdoctor = "Rheumatologist"
           
        if  value in Cardiologist :
           consultdoctor = "Cardiologist"
           

        if value in ENT_specialist :
           consultdoctor = "ENT specialist"
     
        elif value in Orthopedist :
           consultdoctor = "Orthopedist"
     
        elif value in Neurologist :
           consultdoctor = "Neurologist"
     
        elif value in Allergist_Immunologist :
           consultdoctor = "Allergist/Immunologist"
     
        elif value  in Urologist :
           consultdoctor = "Urologist"
     
        elif value in Dermatologist :
           consultdoctor = "Dermatologist"
     
        elif value in Gastroenterologist :
           consultdoctor = "Gastroenterologist"
     
        else :
           consultdoctor = "other"
        cu=request.user
        k=cu.id
        user = patien_dise.objects.create(patient_id=k,disease=value,specilaist=consultdoctor)
        user.save()
        return redirect('suggest')
    return render(request,'symptoms.html')

def suggest(request):
    cu=request.user
    k=cu.id
    obj = patien_dise.objects.filter(patient_id=k).values()
    # docspec = PatDoc.objects.filter(specialization=obj.specilaist)
    # print(docspec)
    n = obj.count()
    obj1 = obj.values_list('disease')[n-1]
    pred = obj.values_list('specilaist')[n-1]
    print(obj1)
    print(pred)
    # patname=obj.values_list('use')
    docobj = PatDoc.objects.all()
    print(obj1)
    print(pred)
    print(docobj)
    return render(request,'suggest.html',{'objid':k,'obj1':obj1,'pred':pred,'docobj':docobj})

def notifydatabase(request):
    if request.method == 'POST':
        padid = request.POST['padid']
        docid = request.POST['docid']
        pred = request.POST['pred']
        patname=request.POST['patname']

        objects = Notifydatabase.objects.create(padid=padid,docid=docid,pred=pred,patname=patname)
        objects.save()
        return redirect('/')



def docnoc(request):
    cu = request.user
    k = cu.id

    objs = Notifydatabase.objects.filter(docid=k).values()
    checking = Appoint.objects.filter(docid=k).values()
    unique_ids = checking.values_list('unique_id', flat=True)
    objs1 = objs.exclude(id__in=unique_ids)
    print(objs1)
    print(checking.values_list('unique_id'))
    return render(request, 'docnoc.html', {'new': objs1})


        
def appoint(request):
    if request.method == 'POST':
        padid = request.POST['padid']
        patname = request.POST['patname']
        pred = request.POST['pred']
        date = request.POST['date']
        time = request.POST['time']
        booked = request.POST['booked']
        docid = request.POST['docid']
        doc_name = request.POST['doc_name']
        unique_id = request.POST['unique_id']
        objs=PatDoc.objects.filter(userid=docid).values()
        city1=objs[0]['city']
        phno=objs[0]['phno']
        hospital_name=objs[0]['hospital']
        patobjs = Patreg.objects.filter(userid=padid).values()
        patphno = patobjs[0]['phno']
        hospin = objs[0]['pincode']
        user = Appoint.objects.create(padid=padid,patname=patname,pred=pred,date=date,time=time,docid=docid,doc_name=doc_name,city1=city1,phno=phno,hospital_name=hospital_name,patphno=patphno,hospin=hospin,booked=booked,unique_id=unique_id)
        user.save()
        return redirect('docnoc')
    else:
        return redirect('docnoc')
    
def docappoint(request):
    if request.method == 'POST':
        cu = request.user
        k = cu.id
        patid = int(request.POST['patid'])
        treat = request.POST['treat']
        userobj = Treating.objects.create(patid=patid,docid=k,treat=treat)
        userobj.save()
        return redirect(docappoint)
    cu = request.user
    k = cu.id
    appointments = Appoint.objects.filter(docid=k).values()
    return render(request,'docappoint.html',{'appointobj':appointments})


def patappoint(request):
    cu = request.user
    k = cu.id
    patapp = Appoint.objects.filter(padid=k).values()
    return render(request,'patappoint.html',{'objs':patapp})

def dochistory(request):
    cu = request.user
    k = cu.id
    treat_list=Treating.objects.filter(docid=k).values()
    pat_list = Appoint.objects.all()
    return render(request,'dochist.html',{'treat_list':treat_list,'pat_list':pat_list})
    # n=treat_list.count()
    # print(n)
    # pat_id=treat_list[0]['patid']
    # print(pat_id)
    # return render(request,'dochist.html',{'objs':treat_list})


def pathist(request):
    cu = request.user
    k = cu.id
    treat_list = Treating.objects.filter(patid=k).values()
    doc_list = Appoint.objects.all()
    return render(request,'pathist.html',{'treat_list':treat_list,'doc_list':doc_list})


def logout(request):
    auth.logout(request)
    return redirect('/')