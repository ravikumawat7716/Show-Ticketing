from flask_restful import Resource
from flask import request
from instances.api import api
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.role_required import role_required
from utils.tasks import dailyreport



class dailyreportAPI(Resource):
    @jwt_required()
    @role_required('ADMIN')
    def get(self):
        dailyreport.delay()
        return {"message" : "Daily Report Sent on Email Successfully."}, 200

api.add_resource(dailyreportAPI, '/dailyreport')



