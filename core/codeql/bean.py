class CodeQLBean(object):
    def __init__(self, ql_path, database_path, database_name, project_path):
        self._ql_path = ql_path
        self._database_path = database_path
        self._database_name = database_name
        self._project_path = project_path

    @property
    def ql_path(self):
        return self._ql_path
    
    @property
    def database_path(self):
        return self._database_path
    
    @property
    def database_name(self):
        return self._database_name
    
    @property
    def project_path(self):
        return self._project_path