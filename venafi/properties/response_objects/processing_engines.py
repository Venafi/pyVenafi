class ProcessingEngines:
    class Engine:
        def __init__(self, proc_eng_dict: dict):
            if not isinstance(proc_eng_dict, dict):
                proc_eng_dict = {}

            self.links = ProcessingEngines.Link(proc_eng_dict.get('_links'))
            self.engine_dn = proc_eng_dict.get('EngineDN')  # type: str
            self.engine_guid = proc_eng_dict.get('EngineGuid')  # type: str
            self.engine_name = proc_eng_dict.get('EngineName')  # type: str

    class Folder:
        def __init__(self, folder_dict: dict):
            if not isinstance(folder_dict, dict):
                folder_dict = {}

            self.folder_dn = folder_dict.get('FolderDN')  # type: str
            self.folder_guid = folder_dict.get('FolderGuid')  # type: str
            self.folder_name = folder_dict.get('FolderName')  # type: str

    class Link:
        def __init__(self, link_dict: dict):
            if not isinstance(link_dict, dict):
                link_dict = {}

            self.self = ProcessingEngines.Self(link_dict.get('self'))

    class Self:
        def __init__(self, self_dict: dict):
            if not isinstance(self_dict, dict):
                self_dict = {}

            self.href = self_dict.get('href')  # type: str
