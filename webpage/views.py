from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):

    return render_to_response('home.html')

def aboutme(request):

    return render_to_response('aboutme.html')

def resume(request):

    return render_to_response('resume.html')

def travels(request):
    #Let's pretend this data is an object retrieved from a database
    data_list = [{'latitude':'-18', 'longitude':'179', 'purpose':'reside', 'location':'Fiji',},
             {'latitude':'-14.1167', 'longitude':'27.6333', 'purpose':'reside', 'location':'Zambia',},
             {'latitude':'28.1', 'longitude':'-81.6', 'purpose':'reside', 'location':'Florida',},
             {'latitude':'31', 'longitude':'-100', 'purpose':'reside', 'location':'Texas',},
             {'latitude':'23.2167', 'longitude':'72.6833', 'purpose':'visit', 'location':'Gujarat',},
             {'latitude':'23.9167', 'longitude':'-77.6667', 'purpose':'visit', 'location':'Bahamas',},
             {'latitude':'19.3333', 'longitude':'-81.2167', 'purpose':'visit', 'location':'Grand Cayman',},
             {'latitude':'19', 'longitude':'-102.3667', 'purpose':'visit', 'location':'Mexico',},
             {'latitude':'40.67', 'longitude':'-73.94', 'purpose':'visit', 'location':'New York',},
             {'latitude':'31.0413', 'longitude':'-91.836', 'purpose':'visit', 'location':'Louisiana',},
             {'latitude':'39', 'longitude':'-105.5', 'purpose':'visit', 'location':'Colorado',},
             {'latitude':'32.9605', 'longitude':'-83.1132', 'purpose':'visit', 'location':'Georgia',},
             {'latitude':'55', 'longitude':'-115', 'purpose':'visit', 'location':'Alberta',},
             {'latitude':'25.2', 'longitude':'55.3', 'purpose':'visit', 'location':'Dubai',},
             {'latitude':'-30', 'longitude':'25', 'purpose':'visit', 'location':'South Africa',},
             {'latitude':'-20.2', 'longitude':'57.5', 'purpose':'visit', 'location':'Mauritius',},
             {'latitude':'-19.0167', 'longitude':'30.0167', 'purpose':'visit', 'location':'Zimbabwe',},       
    ]
    
    #Now we can check the purpose and assign bubble radius and fillkey value to the list of dicts
    places = []
    
    for place in data_list:
        
        if place['purpose'] == 'reside':
            place.update({'radius':'13', 'fillKey':'Resided'})
        elif place['purpose'] == 'visit':
            place.update({'radius':'7', 'fillKey':'Visited'})
        
        places.append(place)
    
    context = RequestContext(request)
    context['places'] = places
    return render_to_response('travels.html', context)

def contact(request):

    return render_to_response('contact.html')

