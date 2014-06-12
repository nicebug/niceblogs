# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589122.835
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


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
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
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
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n        <!--Body content-->\n        <div class="postbox">\n        <h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n        <ul class="list-unstyled">\n')
        for post in posts:
            __M_writer(u'            <li><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">[')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'] ')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a>\n')
        __M_writer(u'        </ul>\n        </div>\n        <!--End of body content-->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 9, "65": 9, "66": 9, "67": 11, "36": 2, "41": 14, "61": 9, "47": 3, "73": 67, "56": 3, "57": 6, "26": 0, "59": 8, "60": 9, "58": 6, "62": 9, "63": 9}, "uri": "list_post.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/list_post.tmpl"}
__M_END_METADATA
"""
