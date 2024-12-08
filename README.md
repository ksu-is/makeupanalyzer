# makeupanalyzer
About:
Together, Esmeralda and Alondra aim to create a Telegram bot that allows matching the correct type of makeup with other makeup through the analyses of ingredients. This bot would also look for poor-clogging and acne-aggrivating ingredients.
We will upload a database with comedogenic and irritable ingredients as well as ingredients that should match between products. The bot simplifies the process of making sure you avoid the unwanted ingredients in your makeup routine without the hassle and time wasted comparing the endless amount of makeup ingredients.

Try the Telegram bot @makeup_analyzer_bot!

Data: 
The project is based off of products listed from https://insolitbeauty.com/documentacion/Comedogenicidad%20e%20irritacion%20de%20los%20ingredientes%20de%20uso%20comun%20en%20productos%20para%20el%20cuidado%20de%20la%20piel.pdf and also from
https://clearstem.com/pages/pore-clogging-ingredients-list?srsltid=AfmBOopD3MOwWzIW4kopvPj9keRa8kp0uZPO26pBHZrrffZx3XvlGiD5 . 
Having tested the effectiveness of avoiding these ingredients as successful to keeping clear skin, Alondra found herself constantly using it when going to Sephora or Ulta to buy makeup. The problem was always having to take multiple steps to read each ingredient and compare it to the list of ingredients to avoid. 

Built With:
Telegram
Google Cloud Vision
Pandas
OS 

How To Use It:
After finding the bot @makeup_analyzer_bot , the conversation can be initiated with the command /sendphoto and it will prompt the user to take a picture. The Bot will then analyze it and list which ingredients are not acne-friendly and with a description as to what makes then comedogenic/irritable. 

Credits:
For the basis of the design, the use of the telegram, Google Cloud Vision, Pandas, and OS goes to https://github.com/normangalt/Cosmetics-Check .
For better understanding and implementation of Telegram into our project, the credit goes to https://youtu.be/vZtm1wuA2yc?si=DoCs8UyKjrwtN6jl. For better understanding of Google Cloud Vision, the credit goes to (insert link).
