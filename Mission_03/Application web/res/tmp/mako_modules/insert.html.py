# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1702388080.585932
_enable_loop = True
_template_filename = 'res/templates/insert.html'
_template_uri = 'insert.html'
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
        __M_writer('\r\n<style>\r\n  h3.center {\r\n      color : white;\r\n      font-weight: 900 ;\r\n  }\r\n  h6{\r\n      color: white;\r\n      font-weight: 100 ;\r\n      font-size: 20px;\r\n  }\r\n</style>\r\n<h3 class="center">Insertion d\'un remboursement</h3>\r\n\r\n<h6>\r\nInsertion de données dans la base.\r\n</h6>\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n <form action="insertDone" method="POST" class="needs-validation" novalidate>\r\n  \r\n<div class="form-group">\r\n  <label for="numticket"><h6>Numéro de ticket (Suivre le procédé : 999_J99) :</h6></label>\r\n  <input type="text" class="form-control" id="numticket" placeholder="Saisir le numéro de ticket" name="numticket" required>\r\n  <div class="valid-feedback">Valid.</div>\r\n  <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n</div>\r\n<div class="form-group">\r\n    <label class="form">\r\n    <label for="date"><h6>Date pour le remboursement de cette journée :</h6></label>\r\n    <input type="date" class="form-control" id="date" placeholder="Date de la journée en question" name="date" required>\r\n    </label>\r\n    <div class="form-group">\r\n        <label for="prixnuit"><h6>Prix de la nuit :</h6></label>\r\n        <input type="number" class="form-control" id="prixnuit" placeholder="Saisir le prix de votre nuit" name="prixnuit" step="0.01" required>\r\n        <div class="valid-feedback">Valid.</div>\r\n        <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n      </div>\r\n      \r\n  </div>  \r\n  <div class="form-group">\r\n    <label for="premierrepas"><h6>Déjeuner :</h6></label>\r\n    <input type="number" class="form-control" id="premierrepas" placeholder="Saisir le prix de votre déjeuner" name="premierrepas" step="0.01" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="deuxiemerepas"><h6>Dîner :</h6></label>\r\n    <input type="number" class="form-control" id="deuxiemerepas" placeholder="Saisir le prix de votre nuit" name="deuxiemerepas" step="0.01" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n      <div class="form-group">\r\n        <label for="prixplein"><h6>Prix du plein :</h6></label>\r\n        <input type="number" class="form-control" id="prixplein" placeholder="Saisir le prix de votre plein" name="prixplein" step="0.01" required>\r\n        <div class="valid-feedback">Valid.</div>\r\n        <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n      </div>\r\n      <div class="form-group">\r\n        <label for="prixpeage"><h6>Prix total des péages :</h6></label>\r\n        <input type="number" class="form-control" id="prixpeage" placeholder="Saisir le prix total des péages" name="prixpeage" step="0.01" required>\r\n        <div class="valid-feedback">Valid.</div>\r\n        <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n      </div>\r\n      <button type="submit" class="btn btn-primary">Enregistrer</button>\r\n    </form>\r\n\r\n<script>\r\n// Disable form submissions if there are invalid fields\r\n(function() {\r\n  \'use strict\';\r\n  window.addEventListener(\'load\', function() {\r\n    // Get the forms we want to add validation styles to\r\n    var forms = document.getElementsByClassName(\'needs-validation\');\r\n    // Loop over them and prevent submission\r\n    var validation = Array.prototype.filter.call(forms, function(form) {\r\n      form.addEventListener(\'submit\', function(event) {\r\n        if (form.checkValidity() === false) {\r\n          event.preventDefault();\r\n          event.stopPropagation();\r\n        }\r\n        form.classList.add(\'was-validated\');\r\n      }, false);\r\n    });\r\n  }, false);\r\n})();\r\n</script> ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insert.html", "uri": "insert.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 18, "36": 18, "37": 18, "38": 18, "44": 38}}
__M_END_METADATA
"""
