import pathlib,subprocess,sys

if sys.platform == "win32":
    fl = "C:\\Program Files\\Image-Line\\FL Studio 21\\FL64.exe"
elif sys.platform == "darwin":
    # I'm totally guessing here since I don't have a mac:
    fl = "/Applications/Fl Studio.app"
home = pathlib.Path.home()
projects = home / "Documents" / "Image-Line" / "FL Studio" / "Projects"
flps = set()

for p in projects.iterdir():
    if p.is_dir():
        has_wavs = False
        for subp in p.iterdir():
            if subp.suffix == ".wav":
                has_wavs = True
                break
        if not has_wavs:
            for subp in p.iterdir():
                if subp.suffix == ".flp":
                    flps.add(subp)
print(len(flps))

if sys.platform == "win32":
    renderflag = "/r"
elif sys.platform == "darwin":
    # i'm guessing here too:
    renderflag = "-r"

for p in sorted(flps):
    print("rendering flp:",p)
    subprocess.run([fl,renderflag,str(p)])
    # comment the next line if you think it can run w/o encountering missing plugins or samples
    break
    

