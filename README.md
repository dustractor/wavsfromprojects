# wavsfromprojects
python script that creates a webpage with links to wav files and flps found in your FL Studio projects folder. Also stores notes using localstorage

Clone this repo, cd to the directory, run this command:

    python wavsfromprojects.py
	
This will scan your projects folder for wav files one level deep and create a web page with links to them as well as any flp files found alongside.  The webpage will be created in the same folder as this script.

(Firefox) To be able to click the flps and have them automatically in FL Studio:

1. Find the user profile folder. Enter "about:support" in URL and click "open folder" button in the section labeled "profile folder"
2. Edit the "handlers.json" file
3. Insert the following code in the mimetypes section:  

``,"application/flp":{"action":4,"extensions":["flp"]}``
