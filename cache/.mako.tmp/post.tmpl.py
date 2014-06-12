# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589166.283
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        messages = context.get('messages', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="postbox">\n    ')
        __M_writer(unicode(helper.html_title()))
        __M_writer(u'\n    <hr>\n    <small>\n        ')
        __M_writer(unicode(messages("Posted")))
        __M_writer(u': <time class="published" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time>\n        ')
        __M_writer(unicode(helper.html_translations(post)))
        __M_writer(u'\n        ')
        __M_writer(unicode(helper.html_tags(post)))
        __M_writer(u'\n    </small>\n    <hr>\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n')
        if not post.meta('nocomments'):
            __M_writer(u'        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'    <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'"/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if not post.meta('password'):
            __M_writer(u'    <li>\n    <a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"130": 30, "150": 144, "138": 30, "139": 31, "140": 32, "141": 33, "142": 33, "143": 33, "144": 33, "22": 3, "25": 2, "31": 0, "47": 2, "48": 3, "49": 4, "54": 10, "59": 28, "64": 36, "70": 11, "81": 11, "82": 13, "83": 13, "84": 16, "85": 16, "86": 16, "87": 16, "88": 16, "89": 16, "90": 17, "91": 17, "92": 18, "93": 18, "94": 21, "95": 21, "96": 22, "97": 22, "98": 23, "99": 24, "100": 24, "101": 24, "102": 26, "103": 26, "104": 26, "110": 5, "118": 5, "119": 6, "120": 6, "121": 7, "122": 8, "123": 8, "124": 8}, "uri": "post.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/post.tmpl"}
__M_END_METADATA
"""
