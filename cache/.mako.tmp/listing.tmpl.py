# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589123.106
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/listing.tmpl'
_template_uri = u'listing.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'ui', context._clean_inheritance_tokens(), templateuri=u'crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'ui')._populate(_import_ns, [u'bar'])
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(ui.bar(crumbs)))
        __M_writer(u'\n<ul class="list-unstyled">\n')
        for name in folders:
            __M_writer(u'    <li><a href="')
            __M_writer(unicode(name))
            __M_writer(u'"><i class="icon-folder-open"></i> ')
            __M_writer(unicode(name))
            __M_writer(u'</a>\n')
        for name in files:
            __M_writer(u'    <li><a href="')
            __M_writer(unicode(name))
            __M_writer(u'.html"><i class="icon-file"></i> ')
            __M_writer(unicode(name))
            __M_writer(u'</a>\n')
        __M_writer(u'</ul>\n')
        if code:
            __M_writer(u'    ')
            __M_writer(unicode(code))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 3, "28": 0, "42": 2, "43": 3, "48": 17, "54": 4, "67": 4, "68": 5, "69": 5, "70": 7, "71": 8, "72": 8, "73": 8, "74": 8, "75": 8, "76": 10, "77": 11, "78": 11, "79": 11, "80": 11, "81": 11, "82": 13, "83": 14, "84": 15, "85": 15, "86": 15, "92": 86}, "uri": "listing.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/listing.tmpl"}
__M_END_METADATA
"""
