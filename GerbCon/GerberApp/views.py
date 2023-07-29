from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from gerber_renderer import Gerber

# Create your views here.
def home(request):

    return render(request, 'index.html')

def upload_gerber(request):
    files = request.FILES.getlist('gerberfiles')
    if files:

        file_dict = {
            'gbl' : {},
            'gbt' : {},
            'gbo' : {},
            'gto' : {},
            'gbp' : {},
            'gtp' : {},
            'gbs' : {},
            'gts' : {},
            'gml' : {},
            'txt' : {},
        }
        for file in files:
            filename = file.name
            base, extension = filename.split('.',1)

            file_dict_key = extension.lower()
            if file_dict_key in file_dict:
                file_dict[file_dict_key][base] = file

        filtered_files = {key: value for key, value in file_dict.items() if value}
        gerber_render(filtered_files)
    else:
        return JsonResponse({'error': 'No files selected'})
    
def gerber_render(files):
    gerberfile = files
    board = Gerber.Board(file=gerberfile)
    # PNG = board.render()
    return JsonResponse({'PNG': 'PNG'})