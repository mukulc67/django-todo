from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection
# Create your views here.
def list_todo(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM ptodoapp_ptodos')
        record=cursor.fetchall()
        li=['gg','khkh']
        dict={'records':record}
        print(record)
        return render(request,'list.html',context=dict)
def insert_todo(request):
    if(request.method=="POST"):
        print("1")
        item=request.POST['content']
        print("2")
        with connection.cursor() as cursor:
            print("3")
            cursor.execute('INSERT INTO ptodoapp_ptodos (item) VALUES (%s)',[item])
            print("4")
            print("5")       
    return redirect('/ptodoapp/list/')  
def delete_item(request,todo_id):
           print(todo_id)
           with connection.cursor() as cursor:
            print("3")
            cursor.execute('DELETE FROM ptodoapp_ptodos WHERE id=%s',[todo_id])
            return redirect('/ptodoapp/list/') 
