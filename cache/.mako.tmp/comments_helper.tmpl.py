# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589123.017
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper.tmpl'
_template_uri = u'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link', 'comment_link_script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'googleplus', context._clean_inheritance_tokens(), templateuri=u'googleplus_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'googleplus')] = ns

    ns = runtime.TemplateNamespace(u'livefyre', context._clean_inheritance_tokens(), templateuri=u'livefyre_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'livefyre')] = ns

    ns = runtime.TemplateNamespace(u'disqus', context._clean_inheritance_tokens(), templateuri=u'disqus_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'disqus')] = ns

    ns = runtime.TemplateNamespace(u'intensedebate', context._clean_inheritance_tokens(), templateuri=u'intensedebate_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'intensedebate')] = ns

    ns = runtime.TemplateNamespace(u'moot', context._clean_inheritance_tokens(), templateuri=u'moot_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'moot')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'moot':
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_form(url, title, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'moot':
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_link(link, identifier)))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link(link, identifier)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        livefyre = _mako_get_namespace(context, 'livefyre')
        googleplus = _mako_get_namespace(context, 'googleplus')
        moot = _mako_get_namespace(context, 'moot')
        disqus = _mako_get_namespace(context, 'disqus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system == 'disqus':
            __M_writer(u'        ')
            __M_writer(unicode(disqus.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'livefyre':
            __M_writer(u'        ')
            __M_writer(unicode(livefyre.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'intensedebate':
            __M_writer(u'        ')
            __M_writer(unicode(intensedebate.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'moot':
            __M_writer(u'        ')
            __M_writer(unicode(moot.comment_link_script()))
            __M_writer(u'\n')
        elif comment_system == 'googleplus':
            __M_writer(u'        ')
            __M_writer(unicode(googleplus.comment_link_script()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 37, "150": 43, "138": 37, "139": 38, "140": 39, "141": 39, "142": 39, "143": 40, "144": 41, "145": 41, "146": 41, "147": 42, "148": 43, "149": 43, "22": 7, "151": 44, "152": 45, "25": 4, "154": 45, "155": 46, "28": 3, "157": 47, "158": 47, "31": 5, "34": 6, "164": 158, "37": 0, "156": 47, "42": 2, "43": 3, "44": 4, "45": 5, "46": 6, "47": 7, "48": 21, "49": 35, "50": 49, "56": 9, "66": 9, "67": 10, "68": 11, "69": 11, "70": 11, "71": 12, "72": 13, "73": 13, "74": 13, "75": 14, "76": 15, "77": 15, "78": 15, "79": 16, "80": 17, "81": 17, "82": 17, "83": 18, "84": 19, "85": 19, "86": 19, "153": 45, "92": 23, "102": 23, "103": 24, "104": 25, "105": 25, "106": 25, "107": 26, "108": 27, "109": 27, "110": 27, "111": 28, "112": 29, "113": 29, "114": 29, "115": 30, "116": 31, "117": 31, "118": 31, "119": 32, "120": 33, "121": 33, "122": 33}, "uri": "comments_helper.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper.tmpl"}
__M_END_METADATA
"""
