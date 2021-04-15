class ProcessingEngines:
    class Engine:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.links = ProcessingEngines.Link(response_object.get('_links'))
            self.engine_dn = response_object.get('EngineDN')  # type: str
            self.engine_guid = response_object.get('EngineGuid')  # type: str
            self.engine_name = response_object.get('EngineName')  # type: str

    class Folder:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.folder_dn = response_object.get('FolderDN')  # type: str
            self.folder_guid = response_object.get('FolderGuid')  # type: str
            self.folder_name = response_object.get('FolderName')  # type: str

    class Link:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.self = ProcessingEngines.Self(response_object.get('self'))

    class Self:
        def __init__(self, response_object: dict):
            if not isinstance(response_object, dict):
                response_object = {}

            self.href = response_object.get('href')  # type: str
