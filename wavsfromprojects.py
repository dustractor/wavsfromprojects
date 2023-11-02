import pathlib
from xml.dom import minidom
from hashlib import md5

home = pathlib.Path.home()
here = pathlib.Path(__file__).parent
projects = home / "Documents" / "Image-Line" / "FL Studio" / "Projects"
outputfile = here / "output.html"
_file = lambda _:"file:///{}".format(str(_))

def _elem_inplace_addition(self,other):
    self.appendChild(other)
    return self
def _elem_textnode(self,text):
    textnode = self.ownerDocument.createTextNode(text)
    self.appendChild(textnode)
    return self
def _elem_set_attributes_from_tuple(self,*args):
    for k,v in args:
        self.setAttribute(k,str(v))
    return self
minidom.Element.__iadd__ = _elem_inplace_addition
minidom.Element.txt = _elem_textnode
minidom.Element.attrt = _elem_set_attributes_from_tuple
minidom.Element.__str__ = lambda s:s.toprettyxml().strip()

doc = minidom.Document()
elem = doc.createElement

root = elem("html")
head = elem("head")
root += head
title = elem("title")
head += title
title.txt("Wavs and Projects")
style = elem("style")
head += style
style.txt("{css}")
body = elem("body")
root += body
body.attrt(("onload","myLoad()"),("onbeforeunload","mySave()"))

h3 = elem("h3")
body += h3
a = elem("a")
h3 += a
a.attrt(("href",_file(projects)))
a.txt(str(projects))

table = elem("table")
body += table

for path in projects.iterdir():
    if path.is_dir():
        flps = []
        wavs = []
        for pp in path.iterdir():
            if pp.suffix == ".flp":
                flps.append(pp)
            elif pp.suffix == ".wav":
                wavs.append(pp)
        if not len(wavs):
            continue
        tr = elem("tr")
        table += tr
        td = elem("td")
        tr += td
        td.txt(path.name)
        td = elem("td")
        tr += td
        flp_ul = elem("ul")
        tr += flp_ul
        td = elem("td")
        tr += td
        wav_ul = elem("ul")
        td += wav_ul
        for f in flps:
            li = elem("li")
            flp_ul += li
            cbox = elem("input")
            li += cbox
            cbox.attrt(
                ("type","checkbox"),
                ("value",md5(str(f).encode("utf-8")).hexdigest()),
                ("onclick","checkChange(this)"))
            a = elem("a")
            li += a
            a.attrt(("href",_file(f)))
            a.txt(f.name)
        for f in wavs:
            li = elem("li")
            wav_ul += li
            cbox = elem("input")
            li += cbox
            cbox.attrt(
                ("type","checkbox"),
                ("value",md5(str(f).encode("utf-8")).hexdigest()),
                ("onclick","checkChange(this)"))
            a = elem("a")
            li += a
            a.attrt(("href",_file(f)))
            a.txt(f.name)
textarea = elem("textarea")
body += textarea
textarea.attrt(("id","myTextarea"),("rows",4),("cols",40))
textarea.txt("")
# savebutton = elem("button")
# body += savebutton
# savebutton.attrt(("onclick","mySave()"))
# savebutton.txt("save")
# loadbutton = elem("button")
# body += loadbutton
# loadbutton.attrt(("onclick","myLoad()"))
# loadbutton.txt("load")

script = elem("script")
body += script
script.txt("{js}")

js = """
function mySave() {
    var myContent = document.getElementById("myTextarea").value;
    localStorage.setItem("myContent", myContent);
    console.log("saved");
    }

function myLoad() {
    var myContent = localStorage.getItem("myContent");
    document.getElementById("myTextarea").value = myContent;
    var checkboxes = document.getElementsByTagName("input");
    console.log(checkboxes);
    for (var x in checkboxes){
        var stored = localStorage.getItem(checkboxes[x].value);
        if (stored == "x") {
            checkboxes[x].checked = true;
        }
    }
    console.log("loaded");
    }

function checkChange(cbox){
    console.log(cbox.value,cbox.checked);
    if (cbox.checked == true){
        localStorage.setItem(cbox.value,"x");
    } else {
        localStorage.removeItem(cbox.value);
    }
}
"""
css = """
body {
    margin-top:5em;
}
#myTextarea{
    position:fixed;
    top:0;
    left:0;
}
"""
output_text = "<!DOCTYPE html>\n" + str(root).format(js=js,css=css)
print(output_text)
with open(outputfile,"w",encoding="utf8") as f:
    f.write(output_text)

