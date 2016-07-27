from flask import Blueprint, render_template
from flask.views import MethodView
import pymongo


citys = Blueprint('city', __name__, template_folder='templates')


class ListView(MethodView):

    def get(self):
        city = pymongo.Connection("localhost", 27017)["city"]["citys"]
        citys = city.find().sort('pop', pymongo.DESCENDING).limit(20)

        return render_template('city/index.html', citys=citys)



# Register the urls
citys.add_url_rule('/', view_func=ListView.as_view('list'))