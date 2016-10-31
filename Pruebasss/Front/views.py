from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from Front.models import UsuariosUaq, ModelCruzEstefania, Book, BookAuthor

# Create your views here.

def VistaIndex(request):
    contexto={}
    return render(request, 'Front/index.html',contexto)

def VistaPrueba2(request):
    contexto={}
    alumnos=UsuariosUaq.objects.all()
    sumatotal=0
    for alumno in alumnos:
        sumatotal=sumatotal+alumno.promedio
    print "Esta es una linea"
    promedioGeneral=sumatotal/alumnos.count()
    contexto['PromedioGeneral']=promedioGeneral
    contexto['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
    contexto['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=8.0)

    contexto['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)

    return render(request, 'Front/prueba.html',contexto)

def JoseCruzEstefaniaAlmanza(request):
    contexto={}

    try:
        alumnos=UsuariosUaq.objects.all()
        sumatotal=0
        for alumno in alumnos:
            sumatotal=sumatotal+alumno.promedio
        promedioGeneral=sumatotal/alumnos.count()
        contexto['PromedioGeneral']=promedioGeneral
        contexto['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
        contexto['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=8.0)

        contexto['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)

        try:
            contexto['Reportes']=ModelCruzEstefania.objects.all()
        except Exception, e:
            raise e


    except Exception, e:
        return render(request, 'Front/JoseCruzEstefaniaAlmanza.html',contexto)

    return render(request, 'Front/JoseCruzEstefaniaAlmanza.html',contexto)

class AldoRodriguezMoralesView(TemplateView):

    template_name = "Front/AldoRodriguezMorales.html"

    def get_context_data(self, **kwargs):
        context = super(AldoRodriguezMoralesView, self).get_context_data(**kwargs)
        alumnos=UsuariosUaq.objects.all()
        sumatotal=0
        for alumno in alumnos:
            sumatotal=sumatotal+alumno.promedio
        promedioGeneral=sumatotal/alumnos.count()
        context['PromedioGeneral']=promedioGeneral
        context['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
        context['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=8.0)

        context['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)
        return context


def diego(request):
    alumnos=UsuariosUaq.objects.all()
    sumatotal=0
    for alumno in alumnos:
        sumatotal=sumatotal+alumno.promedio
    promedioGeneral=sumatotal/alumnos.count()
    context= {}
    context['PromedioGeneral']=promedioGeneral
    context['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
    context['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=8.0)
    context['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)

    return render(request, 'Front/diego.html', context)

def EfrenPachecoSanchez(request):
    alumnos=UsuariosUaq.objects.all()
    sumatotal=0
    contexto={}

    for alumno in alumnos:
        sumatotal=sumatotal+alumno.promedio

    promedioGeneral=sumatotal/alumnos.count()
    context['PromedioGeneral']=promedioGeneral
    context['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
    context['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=8.0)
    context['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)

    return render(request, 'Front/diego.html', context)


class AlejandroMadariagaAngelesView(View):

    def get(self, request):
        booksPerAuthor = self.getBooksPerAuthor()
        context = {
            'booksPerAuthor': booksPerAuthor
        }

        return render(request, 'Front/alejandroMadariagaAngeles.html', context)

    def getBooksPerAuthor(self):
        authors = BookAuthor.objects.all()
        books = Book.objects.all()

        booksPerAuthor = []

        for author in authors:
            booksByAuthor = {
                'author': author,
                'books': []
            }

            for book in books:
                if book.author == author:
                    booksByAuthor['books'].append(book)

            booksPerAuthor.append(booksByAuthor)

        return booksPerAuthor

def AbrahamPorterMastache(request):
    alumnos=UsuariosUaq.objects.all()
    sumatotal=0
    for alumno in alumnos:
        sumatotal=sumatotal+alumno.promedio
    promedioGeneral=sumatotal/alumnos.count()
    context= {}
    context['PromedioGeneral']=promedioGeneral
    context['usersFuture']=UsuariosUaq.objects.filter(promedio__gte=8.0)
    context['usersNoFuture']=UsuariosUaq.objects.filter(promedio__lte=7.9)
    context['NoHope']=UsuariosUaq.objects.filter(dado_de_bajo=True)

    return render(request, 'Front/AbrahamPorterMastache.html', context)
