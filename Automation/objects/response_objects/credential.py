from apilibs.websdk.resultcodes import ResultCodes


class Credentials:
    class Result:
        def __init__(self, code):
            self.code = code
            self.credential_result = ResultCodes.Credential.get(code, {})
