from flask_restful import Resource, request
from models.user import UserModel
from utils.jws import jwsProtected
from models.role import RoleModel
from utils.role import hasRoleWithErrMsg
from models.user import UserModel
from utils.utils import postJson

class UserEndpoint(Resource):

    @jwsProtected()
    def get(self, authResult, uid):
        if uid == '@me':
            return str(UserModel.getById(authResult["userId"]))
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                return str(UserModel.getById(uid))
            else:
                return result
    
    @jwsProtected()
    @postJson
    def put(self, data, authResult, uid):
        if("name" not in data):
            data["name"] = ''
        if("surname" not in data):
            data["surname"] = ''
        if("adult" not in data):
            data["adult"] = ''
        if("school_id" not in data):
            data["school_id"] = ''
        try:
            if(uid == '@me'):
                UserModel.updateOrCreateUser(userid=authResult["userId"], refresh_token='', access_token='',  expires_in='', name=data["name"], surname=data["surname"], adult=data["adult"], school_id=data["school_id"])
                return {}, 205
        except:
            return {"kind": "USER", "msg": "User does not exist."}, 404

    @jwsProtected()
    def delete(self, authResult, uid):
        if(uid == '@me'):
            try:
                user = UserModel.getById(authResult["userId"])
                user.delete()
            except:
                return {}, 403
            return {}, 200
        else:
            result = hasRoleWithErrMsg(authResult['userId'], ["admin"])
            if result is True:
                try:
                    user = UserModel.getById(uid)
                    user.delete()
                except:
                    return {}, 403
            else:
                return result

class UserExistsEndpoint(Resource):
    def get(self, uid):
        return {"exits": UserModel.getById(uid) is not None}