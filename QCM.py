
from collections import OrderedDict
from ipywidgets.widgets import *
from IPython.display import *

answers = OrderedDict()

def register(name, widget):
    if name in answers:
        widget.value = answers[name].value
    answers[name] = widget    
        
def question(name, *choices, style="select"):
    choices = [""] + list(choices)
    if style == "select":
        widget = Select(options=choices,description=u"Réponse")
    elif style == "toggle":
        widget = ToggleButtons(options=choices,description=u"Réponse")
    register(name, widget)
    return widget

def couleur(name):
    widget = ColorPicker(
    concise=False,
    description='Pick a color',
    value='blue',
    disabled=False)
    register(name, widget)
    return widget

def identification():
    given = Text(description="Prénom:")
    family = Text(description="Nom:")
    register("Nom", given)
    register("Prénom", family)
    return Box([given, family])

def bilingual():
    tab_contents = ['P0', 'P1']
    children = [Text(description=name) for name in tab_contents]
    tab = Tab()
    tab.children = children
    tab.set_title(0, "Français")
    tab.set_title(1, "Anglais")
    return tab

def bilan():
    markdown = ""
    critical = 0
    for field, widget in answers.items():
        value = widget.value
        _class = "bg-info"
        if not value:
            value = "Pas de réponse"
            if field in ["Nom", "Prénom"]:
                _class = "bg-danger"
                critical += 1
            else:
                _class = "bg-warning"
        value = "<span class='{0}'>{1}</span>".format(_class, value)
        markdown += field + ": " + value + "\n\n"
    markdown += "--------\n\n"
    if critical:
      markdown += \
      "<span class='bg-danger'>QCM invalide: {0} question(s) obligatoire(s) sans réponse</span>".format(critical)
    
    return Markdown(markdown)

