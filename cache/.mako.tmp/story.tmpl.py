# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1403627669.638
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/story.tmpl'
_template_uri = u'story.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


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
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        helper = _mako_get_namespace(context, 'helper')
        title = context.get('title', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        enable_comments = context.get('enable_comments', UNDEFINED)
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
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        enable_comments = context.get('enable_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if title:
            __M_writer(u'    <h1>')
            __M_writer(unicode(title))
            __M_writer(u'</h1>\n')
        __M_writer(u'    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n')
        if enable_comments and not post.meta('nocomments'):
            __M_writer(u'    ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n')
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
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"22": 4, "25": 3, "31": 0, "45": 2, "46": 3, "47": 4, "52": 7, "57": 16, "63": 8, "73": 8, "74": 9, "75": 10, "76": 10, "77": 10, "78": 12, "79": 12, "80": 12, "81": 13, "82": 14, "83": 14, "84": 14, "90": 5, "98": 5, "99": 6, "100": 6, "106": 100}, "uri": "story.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/story.tmpl"}
__M_END_METADATA
"""
