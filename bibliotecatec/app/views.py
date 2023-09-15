from django.shortcuts import render
from . models  import*

def consulta(request):
    consultas = {
         'consultas':Livro.objects.all()
        }

    return render(request,'consulta/consulta.html',consultas)

def reserva(request):
     if request.POST:
        nova_reserva= Emprestimo()
        nova_reserva.data_emprestimo = request.POST.get('data')
        nova_reserva.data_devolucao = request.POST.get('data2')
        try:
            leitor = Leitor.objects.get(pk=request.POST.get('leitor'))
            livro = Livro.objects.get(pk=request.POST.get('livro'))
            nova_reserva.leitor = leitor
            nova_reserva.livro = livro
            nova_reserva.save() 
        except Leitor.DoesNotExist:
                print("Leitor não encontrado")
        except Livro.DoesNotExist:
                print("Livro não encontrado")
        except Exception as e:
                print("Erro de integridade:", e)
     reservas = {
         'leitor':Leitor.objects.all(),
         'livro':Livro.objects.all(),
        }
        
     return render(request,'reserva/reserva.html',reservas)

def index(request):
   context = {
         'Autor':Autor.objects.all(),
         'Gener':Genero.objects.all(),
         'Cidade':Cidade.objects.all(),
         'Editora':Editora.objects.all(),
         'Leitor':Leitor.objects.all(),
   }
   
   return render(request,'index.html',context)

