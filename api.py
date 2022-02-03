from ast import arg
from enum import auto
from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Parcours(Resource):
    def calc_dist(self, dist, tps_recharge, autonomy):
        vitesse = 100
        if(autonomy > dist):
            return dist * 60 / vitesse
        else:
            nb_arrets = dist // autonomy
            reste = dist % autonomy
            return (((autonomy * 60 / vitesse) + tps_recharge) * nb_arrets) + (reste * 60 / vitesse)

    def get(self):
        dist = int(request.args.get('dist'))
        tps_recharge = int(request.args.get('tps_recharge'))
        autonomy = int(request.args.get('autonomy'))
        return {'res': self.calc_dist(dist, tps_recharge, autonomy)}

api.add_resource(Parcours, '/parcours')

if __name__ == '__main__':
    app.run(debug=False)