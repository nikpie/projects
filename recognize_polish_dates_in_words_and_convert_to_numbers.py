#!/usr/bin/env python

import re

day_dict = {'^pierwsz.*': 1,'^drug.*': 2,'^trzec.*': 3,'^czwart.*': 4,'^piąt.*': 5,'^szóst.*': 6,'^siódm.*': 7,
'^ósm.*': 8,'^dziewiąt.*': 9,'^dziesiąt.*': 10,'^jedenast.*': 11,'^dwunast.*': 12,'^trzynast.*': 13,
'^czternast.*': 14,'^piętnast.*': 15,'^szesnast.*': 16,'^siedemnast.*': 17,'^osiemnast.*': 18,'^dziewiętnast.*': 19,
'^dwudziest[yego]+$': 20,'^dwudziest.*\spierwsz.*': 21,'^dwudziest.*\sdrug.*': 22,'^dwudziest.*\strzeci.*': 23,
'^dwudziest.*\sczwart.*': 24,'^dwudziest.*\spiąt.*': 25,'^dwudziest.*\sszóst.*': 26,'^dwudziest.*\ssiódm.*': 27,
'^dwudziest.*\sósm.*': 28,'^dwudziest.*\sdziewiąt.*': 29,'^trzydziest[yego]+$': 30,'^trzydziest.*\spierwsz.*': 31
}

month_dict = {'styczeń|stycznia|styczniu|zero pierw|pierwszy|pierwszego':1,
'luty|lutego|lutym|zero drug|drugi|drugiego':2,
'marzec|marca|marcu|zero trzec|trzeci|trzeciego':3,
'kwiecień|kwietnia|kwietniu|zero czwart|czwarty|czwartego':4,
'maj|maja|maju|zero piąt|piąty|piątego':5,
'czerwiec|czerwca|czerwcu|zero szóst|szósty|szóstego':6,
'lipiec|lipca|lipcu|zero siódm|siódmy|siódmego':7,
'sierpień|sierpnia|sierpniu|zero ósm|ósmy|ósmego':8,
'wrzesień|września|wrześniu|zero dziewiąt|dziewiąty|dziewiątego':9,
'październik|października|październiku|dziesiąt':10,
'listopad|listopada|listopadzie|jedenast':11,
'grudzień|grudnia|grudniu|dwunast':12
}

minute_dict={'kwadrans':15,'jeden' :1,'dwa' :2, 'dwie':2, 'trzy' :3,'cztery' :4,'pięć' :5,'sześć' :6,'siedem' :7,'osiem' :8,'dziewięć' :9,
'dziesięć' :10,'jedenaście' :11,'dwanaście' :12,'trzynaście' :13,'czternaście' :14,'piętnaście' :15,'szesnaście' :16,
'siedemnaście' :17,'osiemnaście' :18,'dziewiętnaście' :19,'dwadzieścia' :20,'dwadzieścia jeden':21,'dwadzieścia dwa':22,
'dwadzieścia trzy':23,'dwadzieścia cztery':24,'dwadzieścia pięć':25,'dwadzieścia sześć':26,'dwadzieścia siedem':27,
'dwadzieścia osiem':28,'dwadzieścia dziewięć':29,'trzydzieści' :30,'trzydzieści jeden':31,'trzydzieści dwa':32,
'trzydzieści trzy':33,'trzydzieści cztery':34,'trzydzieści pięć':35,'trzydzieści sześć':36,'trzydzieści siedem':37,
'trzydzieści osiem':38,'trzydzieści dziewięć':39,'czterdzieści' :40,'czterdzieści jeden':41,'czterdzieści dwa':42,
'czterdzieści trzy':43,'czterdzieści cztery':44,'czterdzieści pięć':45,'czterdzieści sześć':46,'czterdzieści siedem':47,
'czterdzieści osiem':48,'czterdzieści dziewięć':49,'pięćdziesiąt' :50,'pięćdziesiąt jeden':51,'pięćdziesiąt dwa':52,
'pięćdziesiąt trzy':53,'pięćdziesiąt cztery':54,'pięćdziesiąt pięć':55,'pięćdziesiąt sześć':56,'pięćdziesiąt siedem':57,
'pięćdziesiąt osiem':58,'pięćdziesiąt dziewięć':59
}


def recognize(text):
    
    text = text.lower()
    text = text.strip()
    re.sub(r'\s*', ' ', text)
    dicta = dict.fromkeys(['day', 'month', 'hour', 'minute'])
    
    regex = re.compile(r'((pierwsz|drug|trzec|czwart|piąt|szóst|siódm|ósm|dziewiąt|dziesiąt|jede|dwu|trzy|czter|pięt|szes|siedem|osiem|dziewiet|nast|dziest){1,2}(ego|y|i|\spierwsz|\sdrug|\strzeci|\sczwart|\spiąt|\sszóst|\ssiódm|\sósm|\sdziewiąt){1,2})')
    day = regex.search(text)
    for key in day_dict.keys():
        try:
            regextwo = re.compile(key)
            if regextwo.search(day.group()) is not None:
                dicta.update({'day':day_dict[key]})
        except:
            pass
        
    try:
        text = re.sub(day.group(), '', text, count=1)
        text = text.strip()
    except:
        pass 
        
    regexthree = re.compile(r'zero\s\w+|styczeń|stycznia|styczniu|luty|lutego|lutym|marzec|marca|marcu|kwiecień|kwietnia|kwietniu|maj|maja|maju|czerwiec|czerwca|czerwcu|lipiec|lipca|lipcu|sierpień|sierpnia|sierpniu|wrzesień|września|wrześniu|październik|października|październiku|listopad|listopada|listopadzie|grudzień|grudnia|grudniu|dziesiątego|dziesiąty|jedenstego|jedenasty|dwunastego|dwunasty|pierwszego|drugiego|trzeciego|czwartego|piątego|szóstego|siódmego|ósmego|dziewiątego|pierwszy|drugi|trzeci|czwarty|piąty|szósty|siódmy|ósmy|dziewiąty')
    month = regexthree.search(text)
    for key in month_dict.keys():
        try:
            regexfour = re.compile(key)
            if regexfour.search(month.group()) is not None:
                dicta.update({'month':month_dict[key]})
        except:
            dicta.update({'month':1})
            
    regexfive = re.compile(r'((pierwsz|drug|trzeci|czwart|piąt|szóst|siódm|ósm|dziewiąt|dziesiąt|jede|dwu|trzy|czter|pięt|szes|siedem|osiem|dziewiet|nast|dziest)+(a|ej|iej|\spierwsz|\sdrug|\strzeci|\sczwart)+)')
    hour = regexfive.search(text)
    for key in day_dict.keys():
        try:
            regexsix = re.compile(key)
            if regexsix.search(hour.group()) is not None:
                dicta.update({'hour':day_dict[key]})
                hourforminute = day_dict[key]
        except:
            pass
            
    regexseven = re.compile(r'kwadrans|wpół do\s\w*|za\s\w*|jeden\s|dwa\s|dwie\s|trzy\s|cztery|pięć\s|sześć|siedem\s|osiem\s|dziewięć|dziesięć|jedenaście|dwanaście|trzynaście|czternaście|piętnaście|szesnaście|siedemnaście|osiemnaście|dziewiętnaście|dwadzieścia$|dwadzieścia jeden|dwadzieścia dwa|dwadzieścia trzy|dwadzieścia cztery|dwadzieścia pięć|dwadzieścia sześć|dwadzieścia siedem|dwadzieścia osiem|dwadzieścia dziewięć|trzydzieści$|trzydzieści jeden|trzydzieści dwa|trzydzieści trzy|trzydzieści cztery|trzydzieści pięć|trzydzieści sześć|trzydzieści siedem|trzydzieści osiem|trzydzieści dziewięć|czterdzieści$|czterdzieści jeden|czterdzieści dwa|czterdzieści trzy|czterdzieści cztery|czterdzieści pięć|czterdzieści sześć|czterdzieści siedem|czterdzieści osiem|czterdzieści dziewięć|pięćdziesiąt$|pięćdziesiąt jeden|pięćdziesiąt dwa|pięćdziesiąt trzy|pięćdziesiąt cztery|pięćdziesiąt pięć|pięćdziesiąt sześć|pięćdziesiąt siedem|pięćdziesiąt osiem|pięćdziesiąt dziewięć')
    minute = regexseven.search(text)
    
    for key in minute_dict.keys():
            try:
                regexeight = re.compile(key)
                if regexeight.search(minute.group()) is not None:
                    dicta.update({'minute':minute_dict[key]})
            except:
                dicta.update({'minute':0})
    
    try: 
        if re.search(r'wpół do\s\w*', minute.group()) is not None:
            dicta.update({'minute':30})
            dicta.update({'hour':hourforminute-1})           
    except:
        pass 

    try:
        if re.search(r'za\s\w*', minute.group()) is not None:
   
            for key in minute_dict.keys():
                try:
                    regexeight = re.compile(key)
                    if regexeight.search(minute.group()) is not None:
                        dicta.update({'minute':60-minute_dict[key]})
                        dicta.update({'hour':hourforminute-1})
                except:
                    pass
    except:
        pass
    
    print(dicta)
    
