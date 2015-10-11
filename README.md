#Hi, this is Noteify!
Save precious study seconds by making your text do all the work.

This web app optimizes reading efficiency and study recall by analyzing input text for significance on a word-by-word basis. Words are evaluated based on their frequency in the English language, and consequently assigned a score. More uncommon words are then blown up in physical text size to make them stand out, while more common words remain smaller.

To run this website with Flask, just cd into this folder and run:
<br />
$ python app.py
<br />
It will be available on http://localhost:5000/

If you haven’t installed pip:
<br />
$ sudo easy_install pip
<br />
If you run into an error with OS permissions:
<br />
$ sudo chown -R $USER /Library/Python/2.7
<br />
To download Flask (terminal instructions only):
<br />
$ pip install Flask

Screenshots:
<br />
![alt tag](screenshots/home.png)
<br />
![alt tag](screenshots/home_input_text.png)
<br />
![alt tag](screenshots/noteified.png)
