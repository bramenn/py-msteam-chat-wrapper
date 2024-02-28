## Get a Microsoft Teams Chat WebSocket:
You need a Microsoft Teams Chat WebSocket to get all messages, 
for to get this yo need open your account in the browser
Login to microsoft teams and when you already made this you must add this string in the end URL: "/v2/" for exapmple https://teams.microsoft.com/v2/
and refresh the website.

Now you must open inspection tool [(CTRL + SHIFT + C) OR F12]   options and open "Netwok" window and click in "WS":


![Untitled](https://github.com/bramenn/py-msteam-chat-wrapper/assets/50601186/9dfeada9-b7f2-4513-b9e7-59e9baca498b)

Copy the WebSocke as cURL (bash)

and put this in the python code.
