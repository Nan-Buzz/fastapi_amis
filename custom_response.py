# 自定义返回的错误的响应体信息
from fastapi.responses import JSONResponse

class ApiResponse(JSONResponse):
    """ 自定义响应返回 """

    def __init__(self, data={}, status_code=200, status=0, msg='success', **options):
        # 返回码默认都是200
        body = { 'status': status, 'data': data, 'msg': msg }
        super(ApiResponse, self).__init__(status_code=status_code, content=body, **options)

