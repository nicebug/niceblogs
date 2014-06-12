# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589122.999
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/index_helper.tmpl'
_template_uri = u'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,posts):
    __M_caller = context.caller_stack._push_frame()
    try:
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if any(post.is_mathjax for post in posts):
            __M_writer(u'        <script src="/assets/js/mathjax.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        prevlink = context.get('prevlink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<div>\n<ul class="pager">\n')
        if prevlink:
            __M_writer(u'    <li class="previous">\n        <a href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'">&larr; ')
            __M_writer(unicode(messages("Newer posts")))
            __M_writer(u'</a>\n    </li>\n')
        if nextlink:
            __M_writer(u'    <li class="next">\n        <a href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'">')
            __M_writer(unicode(messages("Older posts")))
            __M_writer(u' &rarr;</a>\n    </li>\n')
        __M_writer(u'</ul>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 17, "21": 23, "27": 19, "32": 19, "33": 20, "34": 21, "40": 2, "47": 2, "48": 5, "49": 6, "50": 7, "51": 7, "52": 7, "53": 7, "54": 10, "55": 11, "56": 12, "57": 12, "58": 12, "59": 12, "60": 15, "66": 60}, "uri": "index_helper.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/index_helper.tmpl"}
__M_END_METADATA
"""
