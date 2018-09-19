from flask import Flask
from flask_prometheus import monitor
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Loan(Resource):
    def get(self):
        return {
            'loan_amount_due': 5000
        }

api.add_resource(Loan, '/')

monitor(app, port=9000)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)