from flask import Flask
from flask_restful import Api, Resource

from base import detector
app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self, cod, img1, img2):
        if cod == '7weuog87o8g87t86tg6ogt76tugo76tg67tg67tgyb':
            response = detector(img1,img2)
        else:
            response = 'Does not run'
        return {'response' : response}
api.add_resource(Main, '/imgimg/<string:cod>/<string:img1>/<string:img2>')

if __name__ == '__main__':
    app.run(debug=True)
