# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589166.373
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/tag.tmpl'
_template_uri = u'tag.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


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
    return runtime._inherit_from(context, u'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        tag = context.get('tag', UNDEFINED)
        len = context.get('len', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        date_format = context.get('date_format', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def content():
            return render_content(context)
        tag = context.get('tag', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n        <!--Body content-->\n        <div class="postbox">\n        <h1>')
        __M_writer(unicode(title))
        __M_writer(u'</h1>\n')
        if len(translations) > 1:
            for language in translations:
                __M_writer(u'                <a href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">RSS (')
                __M_writer(unicode(language))
                __M_writer(u')</a>&nbsp;\n')
        else:
            __M_writer(u'            <a href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">RSS</a>\n')
        __M_writer(u'        <br>\n        <ul class="unstyled">\n')
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


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        kind = context.get('kind', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for language in translations:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(unicode(kind))
                __M_writer(u' ')
                __M_writer(unicode(tag))
                __M_writer(u' (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link(kind + "_rss", tag, language)))
                __M_writer(u'">\n')
        else:
            __M_writer(u'        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(unicode(kind))
            __M_writer(u' ')
            __M_writer(unicode(tag))
            __M_writer(u'" href="')
            __M_writer(unicode(_link(kind + "_rss", tag)))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 9, "129": 9, "130": 9, "131": 9, "132": 9, "138": 132, "26": 0, "43": 2, "48": 11, "53": 32, "59": 13, "73": 13, "74": 16, "75": 16, "76": 17, "77": 18, "78": 19, "79": 19, "80": 19, "81": 19, "82": 19, "83": 21, "84": 22, "85": 22, "86": 22, "87": 24, "88": 26, "89": 27, "90": 27, "91": 27, "92": 27, "93": 27, "94": 27, "95": 27, "96": 29, "102": 3, "113": 3, "114": 4, "115": 5, "116": 6, "117": 6, "118": 6, "119": 6, "120": 6, "121": 6, "122": 6, "123": 6, "124": 6, "125": 8, "126": 9, "127": 9}, "uri": "tag.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/tag.tmpl"}
__M_END_METADATA
"""
