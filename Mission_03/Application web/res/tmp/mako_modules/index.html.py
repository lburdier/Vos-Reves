# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1702386990.6184778
_enable_loop = True
_template_filename = 'res/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n<h3 class="center">Rappel de l\'utilité du site :</h3>\r\n\r\n<style>\r\n  body{ \r\n    background: linear-gradient(to right, #ff905c, #ff6347)\r\n  }\r\n\r\n    h3.center {\r\n        color : white;\r\n        font-weight: 900 ;\r\n    }\r\n    h6{\r\n        color: white;\r\n        font-weight: 100 ;\r\n        font-family: \'Arial\', sans-serif;\r\n        font-size: 24px;\r\n    }\r\n</style>\r\n<h6> Ce site permet de créer des tickets de remboursement pour l\'entreprise "Vos Rêves", dans le remboursement, on retrouve le prix de la nuit d\'hôtel, le prix des différents plats de la journée, le prix du plein d\'essence et le prix des péages.</h6>\r\n\r\n<h3 class="center">Les différentes pages du site :</h3>\r\n<h6> La partie insertion permet de créer notre numéro de ticket de remboursement en remplissant les informations nécessaires.</h5>\r\n<h6> La partie Affichage qui permet d\'afficher le remboursement du ticket de façon détaillé, car tout n\'est pas totalement remboursé</h5>\r\n<h6> Et il existe aussi une dernière page Suppresion afin de supprimer notre ticket de remboursement si nous avons fait une erreur d\'insertion </h5>\r\n\r\n\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "34": 30, "40": 34}}
__M_END_METADATA
"""
