from database.functions_db import *


class DB_Application():
    """
    Application object, issued of the local database
    """

    def __init__(self, id=None, nom_application=None):
        self.id = id
        self.name_app = nom_application
        self.validity = None
        self.remark = None
        if self.id is not None and self.name_app is not None:
            self._set_properties()

    def _set_properties(self):
        datas = get_application_for_id(self.id, self.name_app)
        if datas != {}:
            self.validity = datas["validite"]
            self.remark = datas["remarque"]