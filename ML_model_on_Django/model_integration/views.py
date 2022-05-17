from django.http import HttpResponse
from django.shortcuts import render
import joblib

#rendering home page
def home(request):
    return render(request,"index.html")

#integrating model and predicting output
def output(request):
    cls = joblib.load('model.sav')
    lis = []


    lis.append(request.GET['RI'])
    lis.append(request.GET['Na'])
    lis.append(request.GET['Mg'])
    lis.append(request.GET['AI'])
    lis.append(request.GET['Si'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Ca'])
    lis.append(request.GET['Ba'])
    lis.append(request.GET['Fe'])
    print(lis)

    ans = cls.predict([lis])
    if ans==1:

        return render(request,"results.html",{'ans':' building windows float processed'})
    elif ans==2:

        return render(request,"results.html",{'ans': 'building windows non float processed'})
    elif ans==3:

        return render(request,"results.html",{'ans':' vehicle windows float processed'})
    elif ans==4:

        return render(request,"results.html",{'ans':' vehicle windows non float processed(none in this database)'})
    elif ans==5:

        return render(request,"results.html",{'ans':' containers'})
    elif ans==6:

        return render(request,"results.html",{'ans':' tableware'})
    elif ans==7:

        return render(request,"results.html",{'ans':' headlamps'})
    else:
        return HttpResponse("Please enter correct Values")