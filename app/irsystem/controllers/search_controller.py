from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder
import helper
import json_extraction

<<<<<<< HEAD

project_name = "Flask Filler"
net_id = ""


ingredients = ["151 proof rum",
"190 Proof Everclear",
"7-Up",
"Absinthe",
"Absolut Peppar",
"Acerola",
"Advocaat",
"Aftershock",
"Ale",
"Aliz\u00e9",
"Allspice",
"Almond",
"Almond flavoring",
"Almond syrup",
"Amaretto",
"Amarula Cream",
"Amer Picon",
"Angelica root",
"Angostura bitters",
"Anise",
"Anisette",
"Aperol",
"Apfelkorn",
"Apple",
"Apple brandy",
"Apple cider",
"Apple juice",
"Apple schnapps",
"Apple-cranberry juice",
"Apricot",
"Apricot brandy",
"Apricot liqueur",
"Apricot nectar",
"Aquavit",
"Asafoetida",
"Avocado",
"A\u00f1ejo rum",
"Bailey's irish cream",
"Banana",
"Banana liqueur",
"Banana rum",
"Banana syrup",
"Batida de Coco",
"Battery",
"Beef bouillon",
"Beer",
"Berries",
"Bitter lemon",
"Bitters",
"Black Sambuca",
"Black pepper",
"Black rum",
"Black vodka",
"Blackberries",
"Blackberry brandy",
"Blackberry schnapps",
"Blackcurrant cordial",
"Blackcurrant schnapps",
"Blackcurrant squash",
"Blackcurrant vodka",
"Blended whiskey",
"Bloody mary mix",
"Blue Curacao",
"Blueberries",
"Blueberry schnapps",
"Bourbon",
"Brandy",
"Bread",
"Brown sugar",
"Butter",
"Butterscotch schnapps",
"Cachaca",
"Cactus Juice liqueur",
"Campari",
"Canadian whisky",
"Candy",
"Cantaloupe",
"Cappuccino",
"Caramel",
"Caramel coloring",
"Caramel liqueur",
"Carbonated soft drink",
"Carbonated water",
"Cardamom",
"Carrot",
"Cayenne pepper",
"Celery",
"Celery salt",
"Chambord raspberry liqueur",
"Champagne",
"Cherries",
"Cherry",
"Cherry Cola",
"Cherry Heering",
"Cherry brandy",
"Cherry juice",
"Cherry liqueur",
"Cherry syrup",
"Cherry vodka",
"Chocolate",
"Chocolate ice-cream",
"Chocolate liqueur",
"Chocolate milk",
"Chocolate mint liqueur",
"Chocolate syrup",
"Cider",
"Cinnamon",
"Cinnamon schnapps",
"Cinzano Bitters",
"Citrus rum",
"Citrus vodka",
"Clamato juice",
"Cloves",
"Club soda",
"Coca-Cola",
"Cocktail onion",
"Cocoa powder",
"Coconut",
"Coconut cream",
"Coconut liqueur",
"Coconut milk",
"Coconut rum",
"Coconut syrup",
"Coffee",
"Coffee brandy",
"Coffee liqueur",
"Coffeemate",
"Cognac",
"Cola",
"Collins mix",
"Condensed milk",
"Coriander",
"Corn syrup",
"Cornstarch",
"Corona",
"Cranberries",
"Cranberry juice",
"Cranberry liqueur",
"Cranberry vodka",
"Cream",
"Cream of coconut",
"Cream soda",
"Creme de Almond",
"Creme de Banane",
"Creme de Cacao",
"Creme de Cassis",
"Creme de Fraise",
"Creme de Fraise des Bois",
"Creme de Noyaux",
"Crown Royal",
"Crystal light",
"Cucumber",
"Cumin seed",
"Curacao",
"Cynar",
"Daiquiri mix",
"Dark Creme de Cacao",
"Dark rum",
"Dr. Pepper",
"Drambuie",
"Dry Vermouth",
"Dubonnet Blanc",
"Dubonnet Rouge",
"Egg",
"Egg white",
"Egg yolk",
"Eggnog",
"Erin Cream",
"Espresso",
"Everclear",
"Fanta",
"Fennel seeds",
"Fernet Branca",
"Firewater",
"Food coloring",
"Forbidden Fruit",
"Frangelico",
"Fresca",
"Fruit",
"Fruit cocktail",
"Fruit juice",
"Fruit punch",
"Fruit syrup",
"Galliano",
"Gatorade",
"Gelatin",
"Genever",
"George Dickel",
"Gin",
"Ginger",
"Ginger ale",
"Ginger beer",
"Glycerine",
"Godiva liqueur",
"Gold rum",
"Gold tequila",
"Goldschlager",
"Grain alcohol",
"Grand Marnier",
"Grape Pucker",
"Grape juice",
"Grape schnapps",
"Grape soda",
"Grapefruit",
"Grapefruit juice",
"Grapefruit schnapps",
"Grapefruit-lemon soda",
"Grapes",
"Grappa",
"Green Chartreuse",
"Green Creme de Menthe",
"Green Curacao",
"Grenadine",
"Guava juice",
"Guava syrup",
"Guinness stout",
"Half-and-half",
"Hawaiian Punch",
"Hazelnut liqueur",
"Heavy cream",
"Herbal liqueur",
"Honey",
"Honey liqueur",
"Hoopers Hooch",
"Horseradish",
"Hot Damn",
"Hot chocolate",
"Hot red pepper flakes",
"Hpnotiq",
"Ice",
"Ice 101",
"Ice-cream",
"Iced tea",
"Irish Mist",
"Irish cream",
"Irish whiskey",
"Jack Daniels",
"Jalapeno",
"Jello",
"Jim Beam",
"Johnnie Walker",
"Jolt Cola",
"Jose Cuervo",
"J\u00e4germeister",
"Kahlua",
"Key Largo schnapps",
"Kirschwasser",
"Kiwi",
"Kiwi liqueur",
"Kool-Aid",
"Kummel",
"Lager",
"Lakka",
"Lemon",
"Lemon gin",
"Lemon juice",
"Lemon liqueur",
"Lemon peel",
"Lemon schnapps",
"Lemon soda",
"Lemon vodka",
"Lemon-lime mix",
"Lemon-lime sherbet",
"Lemon-lime soda",
"Lemonade",
"Licor 43",
"Light cream",
"Light rum",
"Lillet",
"Lime",
"Lime juice",
"Lime juice cordial",
"Lime liqueur",
"Lime peel",
"Lime vodka",
"Limeade",
"Limoncello",
"Lingonberry jam",
"Mad Dog 20/20",
"Madeira",
"Malibu rum",
"Malt liquor",
"Mandarin",
"Mandarine Napoleon",
"Mango",
"Mango juice",
"Mango liqueur",
"Mango syrup",
"Maple syrup",
"Maraschino cherry",
"Maraschino cherry juice",
"Maraschino liqueur",
"Margarita mix",
"Marjoram leaves",
"Marshmallows",
"Maui",
"Mello Yello",
"Melon liqueur",
"Melon vodka",
"Metaxa",
"Mezcal",
"Midori melon liqueur",
"Milk",
"Mint",
"Mint syrup",
"Molasses",
"Monin bitter",
"Mountain Dew",
"Nutmeg",
"Nuts",
"Olive",
"Olive juice",
"Orange",
"Orange Curacao",
"Orange Vermouth",
"Orange bitters",
"Orange juice",
"Orange liqueur",
"Orange peel",
"Orange rum",
"Orange soda",
"Orange spiral",
"Orange vodka",
"Orange-flower water",
"Oreo cookie",
"Orgeat syrup",
"Ouzo",
"Papaya",
"Papaya juice",
"Parfait d'Amour",
"Passion fruit juice",
"Passion fruit syrup",
"Passoa",
"Peach",
"Peach Vodka",
"Peach brandy",
"Peach juice",
"Peach liqueur",
"Peach nectar",
"Peach schnapps",
"Peachtree schnapps",
"Peanut liqueur",
"Pear",
"Pear brandy",
"Pear juice",
"Pear liqueur",
"Pear soft drink",
"Pepper sauce",
"Peppermint extract",
"Peppermint schnapps",
"Pepsi Cola",
"Pernod",
"Peychaud bitters",
"Pickled pepper",
"Pimm's No. 1",
"Pina colada mix",
"Pineapple",
"Pineapple juice",
"Pineapple rum",
"Pineapple soda",
"Pineapple vodka",
"Pineapple-coconut juice",
"Pineapple-orange juice",
"Pineapple-orange-banana juice",
"Pineau des Charentes",
"Pink lemonade",
"Pisang Ambon",
"Pisco",
"Pistachio liqueur",
"Pi\u00f1a Colada",
"Plums",
"Port",
"Powdered sugar",
"Prune juice",
"Pumpkin",
"Purple passion",
"Raisins",
"Raspberries",
"Raspberry cordial",
"Raspberry jam",
"Raspberry juice",
"Raspberry liqueur",
"Raspberry schnapps",
"Raspberry syrup",
"Raspberry vodka",
"Razzmatazz",
"Red Bull",
"Red wine",
"RedRum",
"Rhubarb",
"Ricard",
"Rock and rye",
"Root beer",
"Root beer schnapps",
"Rose's sweetened lime juice",
"Rosewater",
"Rum",
"Rum cream liqueur",
"Rumple Minze",
"Rye whiskey",
"Safari",
"Sake",
"Salt",
"Sambuca",
"Sarsaparilla",
"Saurer apfel",
"Schnapps",
"Schweppes Lemon",
"Schweppes Russchian",
"Scotch",
"Seagram 7",
"Sherbet",
"Sherry",
"Shochu",
"Sirup of roses",
"Sloe gin",
"Snapple",
"Soda water",
"Sour Apple Pucker",
"Sour apple liqueur",
"Sour mix",
"Southern Comfort",
"Soy milk",
"Soy sauce",
"Sparkling white wine",
"Spiced rum",
"Sprite",
"Squirt",
"St. Hallvard",
"Stout",
"Strawberries",
"Strawberry juice",
"Strawberry liqueur",
"Strawberry schnapps",
"Strawberry syrup",
"Strawberry vodka",
"Strega",
"Sugar",
"Sugar syrup",
"Sunny delight",
"Surge",
"Swedish Punsch",
"Sweet Tea",
"Sweet Vermouth",
"Sweet and sour",
"Swiss Mocha Cream liqueur",
"Tabasco sauce",
"Taboo",
"Tang",
"Tawny port",
"Tea",
"Tennessee whiskey",
"Tequila",
"Tequila Rose",
"Thunderbird",
"Tia maria",
"Tomato juice",
"Tonic water",
"Triple sec",
"Tropical fruit schnapps",
"Tuaca",
"V8 juice",
"Vanilla",
"Vanilla extract",
"Vanilla ice-cream",
"Vanilla liqueur",
"Vanilla schnapps",
"Vanilla syrup",
"Vanilla vodka",
"Vermouth",
"Vinegar",
"Vodka",
"Water",
"Watermelon",
"Watermelon liqueur",
"Watermelon schnapps",
"Whipped cream",
"Whipping cream",
"Whiskey",
"Whisky",
"White Creme de Menthe",
"White chocolate liqueur",
"White cranberry juice",
"White grape juice",
"White port",
"White rum",
"White wine",
"Wild Spirit liqueur",
"Wild Turkey",
"Wildberry schnapps",
"Wine",
"Worcestershire sauce",
"Wormwood",
"Yeast",
"Yellow Chartreuse",
"Yoghurt",
"Yukon Jack",
"Zima"]


ingredients = [item.lower().encode('utf-8') for item in ingredients]
#print(ingredients)
=======
project_name = "CocktailCalc"
<<<<<<< HEAD
net_id = ""
=======
net_id = "Diana Bank (dmb469) , Ninad Thanawala (nat36) , Anirudh Maddula (aam252) ,Jordan Stern (js2595)"
>>>>>>> ab705fe9396d866f2df5d6ff697d8f68e66f38b0
>>>>>>> 5130ed09b96db048a2ca22a6d582842dcca407d9

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	#print(type(query))
	#query = query.decode('utf-8').lower()
	if not query:
		print("Blank space baby")
		data = []
		output_message = ''
	else:
		query = query.lower()
		print(query + "wasup")
		output_message = "ingredients: "
		ings = query.split(',')
		ings = [item.lstrip(' ') for item in ings]

		data = [] # change data to output list of drinks

		search_ing = []
		for ing in ings:
			if ing in ingredients:
				print(ing)
				search_ing.append(ing)
		for ing in search_ing:
			output_message += ing + ',  '
		print(search_ing)
		user_list = [x.lower().encode('utf-8') for x in search_ing]
		print("user list:")
		print(user_list)
		#drink_list = [x.encode('ascii', 'ignore') for x in search_ing]

		ranked_list = helper.drink_jaccard_sim(user_list)
		#ranked_list = json_extraction.drink_jaccard_sim(user_list)
		for i in range(10):
			print(ranked_list[i])

		data=(helper.get_top_k_drinks(ranked_list, 10))
		#data= json_extraction.get_top_k_drinks(ranked_list, 10)
		#data = [('Pineberry', 0.3333333333333333), ('CT', 0.3333333333333333), ("Tinyee's Orange Smoothie", 0.25), ('Fruit Cooler', 0.25), ("Laura's Surprise", 0.25), ('Hennyville Slugger', 0.2222222222222222), ('Belfast Bomber', 0.2222222222222222)]
		#data = [('Ice Pick #2', 0.3333333333333333), ('Christer Petterson', 0.3333333333333333), ('The Vaitkus', 0.3333333333333333), ('Naked Navel', 0.3333333333333333), ('Purple Cow', 0.3333333333333333), ('Zimartini', 0.3333333333333333), ('Frisky Witch', 0.3333333333333333), ('Vodka Russian', 0.3333333333333333), ('Copperhead', 0.3333333333333333), ('Ersh', 0.3333333333333333)]
		#data = [('Caribbean Orange Liqueur', 0.75), ('Saurian Brandy', 0.6), ('Stockholm "75"', 0.5), ('The Power of Milk', 0.4), ('Piggelin #1', 0.4), ('Top Banana', 0.4), ('Lemon Shooters', 0.4), ('St. Petersburg', 0.4), ('Sjarsk', 0.4), ('Raspberry Cordial', 0.4)]
		#data = [('Pine-Sol Shooter', 0.0), ('Black Army', 0.0), ('Cactus Juice', 0.0), ('Tidal Wave', 0.0), ('Drunk Watermelon', 0.0), ('The Seminole', 0.0), ('Dr. Pepper #1', 0.0), ('Pixie Stick', 0.0), ('Candy Corn #2', 0.0), ('Dark and Stormy #2', 0.0)]
		#print(data)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)
