from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Engine(PayloadModel):
    links: 'Link' = PayloadField(alias='Links', default=None)
    engine_dn: str = PayloadField(alias='EngineDn', default=None)
    engine_guid: str = PayloadField(alias='EngineGuid', default=None)
    engine_name: str = PayloadField(alias='EngineName', default=None)


class Folder(PayloadModel):
    folder_dn: str = PayloadField(alias='FolderDn', default=None)
    folder_guid: str = PayloadField(alias='FolderGuid', default=None)
    folder_name: str = PayloadField(alias='FolderName', default=None)


class Link(PayloadModel):
    self: 'Self' = PayloadField(alias='Self', default=None)


class Self(PayloadModel):
    href: str = PayloadField(alias='Href', default=None)
