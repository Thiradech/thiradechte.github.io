from django.shortcuts import render
from markdown2 import Markdown
from . import util
import re

def convert_md_to_html(title):
    content_md = util.get_entry(title)
    if content_md is None:
        return None
    else:
        markdowner = Markdown()
        content_html = markdowner.convert(content_md)
        return content_html

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content_html = convert_md_to_html(title)
    if content_html is None:
        error_message = f"this title ({title}) does not exist!"
        return render(request, "encyclopedia/error.html", {
            "error": error_message
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": content_html,
            "title": title
        })
        
def search(request):
    if request.method == "POST":
        title = request.POST['q']
        content_html = convert_md_to_html(title)
        entries = util.list_entries()
        new_entries = []
        if content_html is None:
            for entry in entries:
                if re.search(title.lower(), entry.lower()) is not None:
                    new_entries.append(entry)
            return render(request, "encyclopedia/related_entries.html", {
                "entries": new_entries,
                "title": title
            })
        else:
            return render(request, "encyclopedia/entry.html", {
            "entry": content_html,
            "title": title
        })
            
def set_NewPage(request):
    return render(request, "encyclopedia/new_page.html")

def create_NewPage(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content_md')
        
        if title in util.list_entries():
            error_message = f"Please input valid title (this {title} is already exist!)"
            return render(request, "encyclopedia/error.html", {
                "error": error_message
            })
        else:
            util.save_entry(title=title, content=content)
            return render(request, "encyclopedia/entry.html", {
            "entry": content,
            "title": title
            })
            
def edit_page(request, title):
    title = 
    return render(request, "encyclopedia/edit_entry.html", {
        "entry": 
        "content": 
    })
    
                    
