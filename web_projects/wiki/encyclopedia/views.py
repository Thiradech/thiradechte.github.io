from django.shortcuts import render
from markdown2 import Markdown
from . import util

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
        return render(request, "encyclopedia/error.html", {
            "title": title
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
        if content_html is None:
            return render(request, "encyclopedia/error.html", {
                "title": title
            })
        else: 
            return render(request, "encyclopedia/entry.html", {
                "entry": content_html,
                "title": title
            })
