from properties.resultcodes import ResultCodes


class Workflow:
    class Result:
        def __init__(self, code: int):
            self.code = code
            self.config_result = ResultCodes.Workflow.get(code, 'Unknown')
