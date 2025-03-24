# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1702236580.1578314
_enable_loop = True
_template_filename = 'res/templates/aff_index.html'
_template_uri = 'aff_index.html'
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
        Remboursement = context.get('Remboursement', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<h3 class="center">Affichage</h3>\r\n<style>\r\n    body{ \r\n    background: linear-gradient(to right, #ff905c, #ff6347)\r\n  }\r\n\tp {\r\n\t\tcolor :white;\r\n\t}\r\n    h3.center {\r\n        color : white;\r\n        font-weight: 900 ;\r\n    }\r\n</style>\r\n<pre>\r\n    Affichage des données contenues dans la base.\r\n    </pre>\r\n\r\n')
        for remboursement in Remboursement:
            __M_writer('    <p>')
            __M_writer(str(remboursement))
            __M_writer('</p>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/aff_index.html", "uri": "aff_index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 2, "35": 20, "36": 21, "37": 21, "38": 21, "39": 23, "45": 39}}
__M_END_METADATA
"""
