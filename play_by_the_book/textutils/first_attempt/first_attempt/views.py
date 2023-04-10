
from django.http import HttpResponse
from django.shortcuts import render
# import string


def index(request):
    # return HttpResponse("<h1>Home</h1>")
    # data= {'name': 'Alfreat', 'place': 'Anton'}
    return render(request, 'index_copy.html')

# def files(request):
#     fh = open("ones.txt", "r+")
#     content = fh.read()
#     return HttpResponse(content)
#
#
# def exercise1(request):
#     output = '''<h1>Navigator</h1><br>
#                 <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Code with Harry Youtube</a> <br>
#                 <a href= "https://www.codewithharry.com/"> Code with Harry Website </a><br>
#                 <a href= "https://docs.python.org/3/"> Python Documentation </a><br>
#                 <a href= "https://stackoverflow.com/"> Stack Overflow </a><br>'''
#     return HttpResponse(output)


def about(request):
    about_page = '''<a href= "http://127.0.0.1:8000/"> Back to Home</a><br>
    <h2>About Page</h2>'''
    return HttpResponse(about_page)
# href tag for back in about works but use below one instead


# def titlecase(request):
#     titlecase_page = '''<a href= "/"> Back to Home</a><br>
#     <h2>Titlecase Page</h2>'''
#     return HttpResponse(titlecase_page)


def analyzer(request):
    # getting text from home page
    dj_text = request.GET.get('text_field', 'default')
    # getting checkboxes value
    rem_punc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newline_remover = request.GET.get('newline_remover', 'off')
    extraspace_remover = request.GET.get('extraspace_remover', 'off')
    char_count = request.GET.get('char_count', 'off')
    # analyse the text
    # removepunc_page = '''<a href= "/"> Back to Home</a><br>
    #                     <h2>Remove Punctuation Page</h2>'''
    # return HttpResponse(removepunc_page)
    analyzed = dj_text
    # punc_res = dj_text
    # upper_res = punc_res
    # newline_res = upper_res
    # extraspace_res = newline_res
    char_res = ""
    task = []
    print("djtext",dj_text)
    # params = {'task': "Remove Punctuation", 'punc_res': analyzed}
    if rem_punc == "on":
        task.append("Remove Punctuation")
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ""
        for char in dj_text:
            if char not in punctuations:
                result = result + char
        analyzed = result
        print(analyzed)
        # params = {'task': "Remove Punctuation", 'analyzed': analyzed}
        # return render(request, 'analyzed.html', params)

    if uppercase == "on":
        task.append("Changed to uppercase")
        result = ""
        for char in analyzed:
            result = result + char.upper()
        analyzed = result
        print(analyzed)
        # params = {'task': "Changed to Uppercase", 'analyzed': analyzed}
        # return render(request, 'analyzed.html', params)
        # use pre tag in textarea then below 2 function are useful  Hint: Use MirrorCode
    if newline_remover == "on":
        task.append("New line Removed")

        result = ""
        for char in analyzed:
            if char != "\n" and char != "\r":
                result = result + char
        analyzed = result
        print("newline",analyzed)
        # params = {'task': "New Line Removed", 'analyzed': analyzed}
        # return render(request, 'analyzed.html', params)

    if extraspace_remover == "on":
        task.append("Extra Spaces Removed")

        result = ""
        for index, char in enumerate(analyzed):

            if analyzed[index] == " " and analyzed[index+1] == " ":
                pass

            else:
                result = result + char
        analyzed = result
        print("extra",analyzed)
        # params = {'task': "Extra Spaces removed", 'analyzed': analyzed}
        # return render(request, 'analyzed.html', params)

    if char_count == "on":

        characters = len(analyzed)
        task.append("Characters Counted")

        char_res = "characters in your text = "+str(characters)

    params = {'task': task, 'analysis': analyzed, 'count': char_res}
    # if char_count != "on" and extraspace_remover != "on" and extraspace_remover != "on" and uppercase != "on" and rem_punc != "on":
    #     return HttpResponse("Error")
    return render(request, 'analyzed.html', params)
# def newlineremover(request):
#     output = '''<a href= '/'> Back to Home Page</a><br>
#     <h2>Newline Remover Page</h2>'''
#     return HttpResponse(output)
