There is a "tag", "patterns", "responses" columns in csv pattern. 

There could be multiple patterns and responses separated by commas. 

First, remove the commas inside the single reponses that are inside double quotes

Pattern for patterns. 

"patterns 1", "pattern 2", "patter 2"


CSV format is like this:
tag,patterns,responses
f_1,"""Kakšne so koristi uživanja feenugreek kapsul?"", ""Katere zdravstvene koristi ponujajo fenugreek kapsule?"",
""Zakaj bi se odločil za uživanje fenugreek kapsul?"",
""Kakšni so pozitivni učinki uživanja fenugreek kapsul?"",
""Zakaj so fenugreek kapsule koristne za zdravje?"",
""Katere prednosti prinaša uživanje fenugreek kapsul?"",Kakšni so benefiti feenugreeka"",""Zakaj je fenugreek koristen za zdravje?"",
""Katere so glavne zdravstvene prednosti uživanja fenugreek?"",
""Kako fenugreek prispeva k mojemu dobremu počutju?"",
""Kateri so največji benefiti uživanja fenugreek?"",
""Zakaj je fenugreek priljubljeno zeliščno dopolnilo?"",""Koristi feenugrek"", ""Katere koristi prinaša redno uživanje fenugreek?"",
""Zakaj je fenugreek cenjen v zeliščni medicini?"",
""Kako fenugreek vpliva na splošno zdravje?"",
""Kaj so ključni razlogi za vključitev fenugreek v prehrano?"",
""Kakšni so pozitivni učinki fenugreek na telo?""","""Koristi: Feenugreek kapsule so znane po tem, da spodbujajo splošno dobro počutje, uravnavajo krvni sladkor in povečujejo energijo. Veliko naših strank poroča o odličnih rezultatih!"""
f_2,"""Kakšna je priporočena dnevna doza Fenugreeka?"",""Koliko Fenugreeka naj zaužijem na dan?"",
""Kakšno količino Fenugreeka je priporočljivo zaužiti dnevno?"",
""Kakšna je dnevna priporočena količina Fenugreeka?"",
""Koliko kapsul Fenugreeka je varno zaužiti na dan?"",
""Kakšna je optimalna dnevna doza za Fenugreek?"",""Kakšne je dnevna doza fenugreek"", ""Koliko fenugreek naj dnevno vnesem v svojo prehrano?"",
""Kaj je dnevno priporočena količina fenugreek?"",
""Koliko fenugreek je varno za dnevno uživanje?"",
""Kakšna je največja količina fenugreek, ki jo lahko zaužijem v enem dnevu?"",
""Kakšno količino fenugreek naj zaužijem vsak dan?""","""Doza: Priporočena dnevna doza je 2 kapsuli dnevno, kar je idealno za maksimalne koristi."""


If commas are missing between ""reponse"", please add one, but in the last cell, don't put comma, since it is the last reponse in the cell. 

and ouput format should be like this:
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hi",
                "Hey",
                "How are you",
                "Is anyone there?",
                "Hello",
                "Good day"
            ],
            "responses": [
                "Hey :-)",
                "Hello, thanks for visiting",
                "Hi there, what can I do for you?",
                "Hi there, how can I help?"
            ]
        },
        {
            "tag": "goodbye",
            "patterns": [
                "Goodbye",
                "Bye",
                "See you later",
                "Take care",
                "Farewell",
                "Until next time"
            ],
            "responses": [
                "Goodbye! Have a great day!",
                "Bye! Take care and come back soon.",
                "See you later. If you need any further assistance, feel free to ask.",
                "Farewell! It was nice talking to you."
            ]
        }
    
    ]
}


Write me a python code.