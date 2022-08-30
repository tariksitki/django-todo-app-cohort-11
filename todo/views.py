from django.shortcuts import render, redirect
from todo.forms import TodoForm

from todo.models import Todo

# Create your views here.


    ### CRUD OPERATIONS:

#### read:

def home(request):
    todos = Todo.objects.all()
    context = {
        "todos" : todos
    }
    return render(request, "todo/home.html", context)





##   create:

### create icin user dan bilgi almak maksadiyla bir form a ihtiyacimiz var:
## Önemli:  template de formun methoduna post yazilir. yani submitbutonuna basildiginda method olarak post calisir. bu durumda if döngüsü ici calisir. ama submit butonuna basilmadiginda if döngüsüne girmez ve get methodu calisir dolayisi ile de bos form return edilir. 

def todo_add(request):
    form = TodoForm
    context = {
        "form" : form
    }

    if request.method == "POST":
        form = TodoForm(request.POST) ## formu gelen istek bilgisi ile dolduruyoruz
        if form.is_valid():
            form.save()
            return redirect("home")  ## return ile birlikte kullanilir.
                                     ## icine de url deki name yazilir.

    return render(request, "todo/todo_add.html", context)







    #####   update:
    ## update etmek icin spesific bir todo ya ihtiyac var. bunun icin id kullanilir

def todo_update(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
        #### Önemli: ilk etap da formun ici bos olmaz. instance olur. eger method get den post a dönerse, bu durumda birde request girer icine 
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo) ## create den tek farki instance
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form" : form,
        "todo" : todo
    }

    return render(request, "todo/todo_update.html", context)






    #### delete:
    ### Önemli:  delete isleminin template inde form kullanilir ama view in de olmaz.
    ### burada form.delete denmez, todo.delete denir.

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.delete()
        return redirect("home")
    context = {
        "todo" : todo
    }

    return render(request, "todo/todo_delete.html", context)
