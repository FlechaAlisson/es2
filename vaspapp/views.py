from django.shortcuts import render

def aluno_list(request):
    return render(request, 'vaspp/post_list.html', {})
