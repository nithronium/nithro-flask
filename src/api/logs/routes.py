from src import db
from src.api.logs import blueprint
from src.modules.logs.models import Logs
from flask import request
from src.decorators.apikey_validator import apikey_required

from src.modules.apps.models import Apps
from src.modules.logs.models import Logs

from src.api.responses import error_response, success_response
from src.api.utils import check_fields


@blueprint.route("/", methods=["POST"])
@apikey_required
def post():
    public_key = request.headers.get("X-API-KEY")

    required_fields = ["message", "status"]

    if not check_fields(request, required_fields):
        return error_response("Missing required fields", 400)

    data = request.json

    app = Apps.query.filter_by(public_key=public_key).first()

    log = Logs()
    log.app_id = app.id
    log.message = data["message"]
    log.status = data["status"]
    log.created_at = db.func.current_timestamp()
    db.session.add(log)
    db.session.commit()

    return success_response("Log created", 201)
