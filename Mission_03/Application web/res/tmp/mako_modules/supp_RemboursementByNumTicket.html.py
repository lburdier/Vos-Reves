# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1702243118.9118552
_enable_loop = True
_template_filename = 'res/templates/supp_RemboursementByNumTicket.html'
_template_uri = 'supp_RemboursementByNumTicket.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        message = context.get('message', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h3 class="center">Suppression d\'un remboursement</h3>\r\n<style>\r\n  body {\r\n    background: linear-gradient(to right, #ff905c, #ff6347)\r\n  }\r\n  p {\r\n      color: white;\r\n  }\r\nh3.center {\r\n      color : white;\r\n      font-weight: 900 ;\r\n  }\r\n</style>\r\n<pre>\r\nSuppression de données contenues dans la base.\r\n1 seul type de suppression : suppression par numéro du ticket\r\n</pre>\r\n\r\n<h3 class="center">Suppression d\'un ticket de remboursement par le numéro de ticket</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="suppressByNumTicket" method="POST">\r\n  <div class="form-group">\r\n    <label for="titre">Numéro de ticket:</label>\r\n    <input type="text" class="form-control" placeholder="Numéro du ticket" name="numticket" id="numticket">\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Supprimer</button>\r\n</form> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supp_RemboursementByNumTicket.html", "uri": "supp_RemboursementByNumTicket.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 22, "36": 22, "37": 22, "38": 22, "44": 38}}
__M_END_METADATA
"""
