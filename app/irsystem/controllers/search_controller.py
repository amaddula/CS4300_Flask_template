from . import *
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "CocktailCalc"
net_id = "Diana Bank (dmb469) , Ninad Thanawala (nat36) , Anirudh Maddula (aam252) ,Jordan Stern (js2595)"

@irsystem.route('/', methods=['GET'])
def search():
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
		#data=["yoooo", "I got shit to work"]
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)
