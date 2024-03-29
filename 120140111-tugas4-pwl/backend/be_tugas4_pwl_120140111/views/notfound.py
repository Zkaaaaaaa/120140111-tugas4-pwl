# Tugas Individu 4 - Pemrograman Web Lanjut
# 120140111 - azka muzhaffar
from pyramid.view import notfound_view_config
from pyramid.httpexceptions import (
    HTTPForbidden,
    HTTPNotFound,
    HTTPSeeOther,
)


@notfound_view_config(renderer="json")
def notfound_view(request):
    request.response.status = 404
    return {"message": "Not Found"}
