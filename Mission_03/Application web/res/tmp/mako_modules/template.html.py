# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1702243832.7689939
_enable_loop = True
_template_filename = 'res/templates/template.html'
_template_uri = 'template.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\r\n<html lang="fr">\r\n  <head>\r\n    <meta charset="utf-8">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\r\n    <link rel="icon" href="/static/images/VosReves.ico" type="image/x-icon">\r\n    <!-- Bootstrap CSS -->\r\n\t<!--\r\n    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\r\n\t-->\r\n    <link rel="stylesheet" href="/static/css/bootstrap.min.css" >\r\n    <!-- CSS Perso -->\r\n    <link rel="stylesheet" href="/static/css/style.css" >\r\n\r\n    <title>Saisie des prix pour le remboursement</title>\r\n  </head>\r\n  <body>\r\n\r\n    <!-- Optional JavaScript -->\r\n    <!-- jQuery first, then Popper.js, then Bootstrap JS -->\r\n    <script src="/static/js/jquery-3.5.0.min.js"></script>\r\n\t<!-- Pas utile ?\r\n    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>\r\n\t-->\r\n    <script src="/static/js/bootstrap.min.js"></script>\r\n\t\r\n    <style>\r\n      body {\r\n          background-color:linear-gradient(to right, #ff905c, #ff6347);\r\n          font-family: \'Courier New\', Courier, monospace;\r\n          font-size: 24px;\r\n      }\r\n  </style>\t\r\n<div class="container-fluid" style="background: linear-gradient(to right, #ff905c, #ff6347); color: #2d1e47; padding-top: 30px;">\r\n<h1 class="text-center" style="color: rgb(235, 235, 235); font-size: 45px;">\r\n          <img src="static/images/VosReves.png" alt="Logo" class="logo-image" width="275" height="175">\r\n          Remboursement\r\n      </h1>  \r\n      <nav class="navbar navbar-expand-lg navbar-dark mt-5" style="background: linear-gradient(to right, #00008B, #88627e); font-size: 20px;">\r\n   <div class="collapse navbar-collapse" id="navbarNavDropdown">\r\n    <ul class="navbar-nav">\r\n      <li class="nav-item active">\r\n        <a class="nav-link" href="index">Accueil <span class="sr-only">(page courante)</span></a>\r\n      </li>\r\n      <li class="nav-item">\r\n        <a class="nav-link" href="insertPage">Insertion</a>\r\n      </li>\r\n      <li class="nav-item">\r\n        <a class="nav-link" href="affRemboursement">Par ordre dans la base </a>\r\n      </li>\r\n      <li class="nav-item">\r\n        <a class="nav-link" href="suppressByNumTicket">Suppression </a>\r\n      </li>\r\n       \r\n      </li>\r\n    </ul>\r\n  </div>\r\n</nav>\r\n\r\n\t')
        __M_writer(str( self.body() ))
        __M_writer('\r\n\r\n\r\n  </div>\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/template.html", "uri": "template.html", "source_encoding": "utf-8", "line_map": {"16": 0, "22": 1, "23": 60, "24": 60, "30": 24}}
__M_END_METADATA
"""
