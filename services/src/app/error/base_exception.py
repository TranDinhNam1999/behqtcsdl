from fastapi.responses import JSONResponse


class CustomHTTPException(Exception):
    def __init__(self, *, code: int, msg: str):
        self.code = code
        self.msg = msg

    def to_json(self):
        return JSONResponse(
            status_code=self.code, content={"code": self.code, "msg": self.msg}
        )
