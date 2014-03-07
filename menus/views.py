from django.http import Http404
from django.http import HttpResponse
from menus.models import User
from menus.models import Menu
from menus.models import Option
import json
from pprint import *

english = ["Not Yet", "Already Filed Report", "Website - Earn Miles", "Website - Redeem Miles", "Website - Offers", "Skip", "500 Mile Upgrade", "Flight Number", "Reservation", "New", "Existing", "Upgrade", "Flight Info", "Departure", "Arrival", "Awards Travel", "New Reservation", "Existing Reservation", "Account", "Mileage Questions", "Balance", "Credit Request", "Redeem Mileage", "Other Flights Credit", "Other Participants Credit", "Purchased Miles", "Bonus Offers", "Update Account", "Mileage Balance", "Change Account Information", "Edit Account Info", "Change Name", "Combine Accounts", "Enroll / Locate Number", "Other Updates", "Elite Status", "Gold", "Platinum", "Executive Platinum", "Promotions", "More Options", "Baggage", "Delayed Baggage", "Website - Baggage", "Make Call", "General Baggage", "Within US", "Outside US", "Travel Tips", "Security / CheckIn", "Travel with Children", "Children Flying Alone", "Travel with Pets", "Phone Numbers", "Delayed Bags", "Ticket Refund", "Web Services", "Vacation", "Cargo & Parcel", "Employment", "Web Support", "Remember Me"]
spanish = ["No", "Report fin", "Sitioweb - Earn Miles", "Sitioweb - Canjear Miles", "Sitioweb - Ofrecer", "Pasa", "500 Mile Mejoramiento", "Numero Vuelo", "Reservacion", "Nueva", "Existente", "Mejoramiento", "Informacion sobre el Vuelo", "Salida", "Llegada", "Los Premios de Viaje", "Reserva Nueva", "Reserva Existente", "Cuenta", "Preguntas Kilometraje", "Saldo", "Solicitad de Credito", "Canjear Millas", "Credito Otros Vuelos", "Credito Otros Participantes", "Millos Comprado", "Ofertas de Bonos", "Actualiza Cuenta", "Saldo de Millas", "Cambia Informasion", "La Cuenta", "Cambia el Nombre", "Combina Cuentas", "Memorizar / Numero Localizar", "Otros Actualizaciones", "Estatus de Elite", "Oro", "Platino", "Platino Ejecutivo", "Promociones", "Mas Opciones", "Equipaje", "Equipaje Demorado", "Sitioweb - Equipje", "Llamar", "Equipaje General", "En US", "Fuera US", "Consejos de Viaje", "Cheque de Seguridad / Registrarse", "Viajar con Ninos", "Ninos Volando Solo", "Viajar con Mascotas", "Numeros de Telefono", "Equipaje Demorado", "Reembolso de Boletas", "Servicio de Web", "Vacaciones", "Carga y Paqueteria", "Empleo", "Soporte Web", "Acuerdate de Mi"]

def home(request):
    return HttpResponse("Home works")

def is_user(request, num):
    try:
        User.objects.get(number=num)
    except User.DoesNotExist:
        return HttpResponse(False)
    return HttpResponse(True)

def get_menu(request, num, lan):
    json_menu = None
    try:
        menu = Menu.objects.get(number=num)
        json_menu = menu_to_json(menu,lan)
    except Menu.DoesNotExist:
        return HttpResponse(False)
    return HttpResponse(json.dumps(json_menu), content_type="application/json")
    #return HttpResponse(num)

def menu_to_json(menu, lan):
    translate = dict()
    eng = True
    if lan == str(1):
	eng = False
	for x in range(0,len(english)):
	    translate[english[x]] = spanish[x]
    json_menu = {}
    json_menu['name'] = menu.name
    print menu.name
    json_menu['number'] = menu.number
    print menu.number
    json_menu['type'] = menu.type
    try:
        all_options = Option.objects.filter(menu=menu)
    except Option.DoesNotExist:
        raise Http404

    def db_has(n):
	for option in all_options:
	    if option.num==n:
		return option
	return False

    def add_menu_to_hash(opt, key):
	try:
	    lagtime = ','*(opt.lag/2)
	    if (opt.xtra != "None"):
		lagtime = lagtime + opt.xtra
            if (key != '~') and len(lagtime) > 0:
		print key+'~', lagtime
                json_menu[key+'~'] = lagtime
	    if key == '~':
		print key, lagtime
		json_menu[key] = lagtime
		key = ''
	    else:
		if eng:
                    json_menu[key] = opt.name
		else:
		    json_menu[key] = translate[opt.name]
            i = 0
	    if opt.one != "None" and db_has(key+'1'):
		add_menu_to_hash(db_has(key+'1'), key+'1')
	    elif (opt.one != "None"):
		if eng:
		    json_menu[key+'1'] = opt.one
		else:
		    json_menu[key+'1'] = translate[opt.one]

            if opt.two != "None" and db_has(key+'2'):                
                add_menu_to_hash(db_has(key+'2'), key+'2')
	    elif (opt.two != "None"):
		if eng:
                    json_menu[key+'2'] = opt.two
		else:
		    json_menu[key+'2'] = translate[opt.two]

	    if opt.three != "None" and db_has(key+'3'):
                add_menu_to_hash(db_has(key+'3'), key+'3')
	    elif (opt.three != "None"):
		if eng:
                    json_menu[key+'3'] = opt.three
		else:
		    json_menu[key+'3'] = translate[opt.three]

	    if opt.four != "None" and db_has(key+'4'): 
		add_menu_to_hash(db_has(key+'4'), key+'4')
	    elif (opt.four != "None"):
		if eng:
                    json_menu[key+'4'] = opt.four
		else:
		    json_menu[key+'4'] = translate[opt.four]

	    if opt.five != "None" and db_has(key+'5'):
		add_menu_to_hash(db_has(key+'5'), key+'5')
	    elif (opt.five != "None"):
		if eng:
                    json_menu[key+'5'] = opt.five
		else:
		    json_menu[key+'5'] = translate[opt.five]

	    if opt.six != "None" and db_has(key+'6'):
		add_menu_to_hash(db_has(key+'6'), key+'6')
	    elif (opt.six != "None"):
		if eng:
                    json_menu[key+'6'] = opt.six
		else:
		    json_menu[key+'6'] = translate[opt.six]

	    if opt.seven != "None" and db_has(key+'7'):
		add_menu_to_hash(db_has(key+'7'), key+'7')
	    elif (opt.seven != "None"):
		if eng:
                    json_menu[key+'7'] = opt.seven
		else:
		    json_menu[key+'7'] = translate[opt.seven]


	    if opt.eight != "None" and db_has(key+'8'):
		add_menu_to_hash(db_has(key+'8'), key+'8')
	    elif (opt.eight != "None"):
		if eng:
                    json_menu[key+'8'] = opt.eight
		else:
		    json_menu[key+'8'] = translate[opt.eight]

	    if opt.nine != "None" and db_has(key+'9'):
		add_menu_to_hash(db_has(key+'9'), key+'9')
	    elif (opt.nine != "None"):
		if eng:
                    json_menu[key+'9'] = opt.nine
		else:
		    json_menu[key+'9'] = translate[opt.nine]


	    if opt.star != "None" and db_has(key+'*'):
		add_menu_to_hash(db_has(key+'*'), key+'*')
	    elif (opt.star != "None"):
		if eng:
                    json_menu[key+'*'] = opt.star
		else:
		    json_menu[key+'*'] = translate[opt.star]

	    if opt.zero != "None" and db_has(key+'0'):
		add_menu_to_hash(db_has(key+'0'), key+'0')
	    elif (opt.zero != "None"):
		if eng:
                    json_menu[key+'0'] = opt.zero
		else:
		    json_menu[key+'0'] = translate[opt.zero]

	    if opt.hash != "None" and db_has(key+'#'):
		add_menu_to_hash(db_has(key+'#'), key+'#')
	    elif (opt.hash != "None"):
		if eng:
                    json_menu[key+'#'] = opt.hash
		else:
		    json_menu[key+'#'] = translate[opt.hash]

	    if (opt.question != "None"):
		if eng:
		    json_menu[key+'?'] = opt.question
		else:
		    json_menu[key+'?'] = translate[opt.question]
		
	    if (opt.website != "None"):
		json_menu[key+'_'] = opt.website
	    if (opt.phone != "None"):
		json_menu[key+'|'] = opt.phone


	except Option.DoesNotExist:
	    raise Http404
        return

    try:
        for opt in all_options:
	    if opt.level == 0:
	        add_menu_to_hash(opt, opt.tag)  
    except Option.DoesNotExist:
	raise Http404
    print json.dumps(json_menu)
    return json_menu

#fn to add menus into db
#def add_menu:
