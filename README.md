# Link-Static-files-in-Django-with-templates-HTML-



1- Making templates and static

In your App of Django Project , make a new folder and named in “templates” , in this templates folder you have to put your HTML file.

Similarly , make one more new folder in your App of Django Project and named it “static”, in static folder you have to put all CSS file for corresponding App.
2- Add HTML in templates and CSS in static folder.

We have made “templates” and “static“ folder , now we have to put HTML files in “templates” folder and CSS file in “static” folder.

Let’s make a new file in templates folder and named it “ok.htm” .

Similarly make a new file in static folder and named it “ok.css” like :

3- HTML and CSS File
4- Connect HTML with CSS :
    {% load static %}
    <link rel="stylesheet" href="{% static 'ok.css' %}">
5-Use HTML file from your view:
