# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1398698391.297
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/base.tmpl'
_template_uri = u'base.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'sourcelink', u'extra_js', u'belowtitle']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

    # SOURCE LINE 3
    ns = runtime.TemplateNamespace(u'bootstrap', context._clean_inheritance_tokens(), templateuri=u'bootstrap_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'bootstrap')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        bootstrap = _mako_get_namespace(context, 'bootstrap')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        hide_sourcelink = _import_ns.get('hide_sourcelink', context.get('hide_sourcelink', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(unicode(set_locale(lang)))
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        # SOURCE LINE 7
        if comment_system == 'facebook':
            # SOURCE LINE 8
            __M_writer(u'xmlns:fb="http://ogp.me/ns/fb#"\n')
        # SOURCE LINE 10
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(bootstrap.html_head()))
        __M_writer(u'\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        # SOURCE LINE 15
        __M_writer(u'\n    ')
        # SOURCE LINE 16
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n</head>\n<body>\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand" href="')
        # SOURCE LINE 29
        __M_writer(unicode(abs_link('/')))
        __M_writer(u'">')
        __M_writer(unicode(blog_title))
        __M_writer(u'</a>\n    </div>\n    <div class="collapse navbar-collapse navbar-ex1-collapse">\n        <ul class="nav navbar-nav">\n            ')
        # SOURCE LINE 33
        __M_writer(unicode(bootstrap.html_navigation_links()))
        __M_writer(u'\n        </ul>\n')
        # SOURCE LINE 35
        if search_form:
            # SOURCE LINE 36
            __M_writer(u'            ')
            __M_writer(unicode(search_form))
            __M_writer(u'\n')
        # SOURCE LINE 38
        __M_writer(u'\n        <ul class="nav navbar-nav navbar-right">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45
        if not hide_sourcelink:
            # SOURCE LINE 46
            __M_writer(u'                ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer(u'\n')
        # SOURCE LINE 48
        __M_writer(u'        </ul>\n    </div><!-- /.navbar-collapse -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        # SOURCE LINE 58
        __M_writer(u'\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        # SOURCE LINE 63
        __M_writer(unicode(content_footer))
        __M_writer(u'\n        </footer>\n    </div>\n</div>\n\n')
        # SOURCE LINE 68
        __M_writer(unicode(bootstrap.late_load_js()))
        __M_writer(u'\n')
        # SOURCE LINE 69
        __M_writer(unicode(base.html_social()))
        __M_writer(u'\n    <script type="text/javascript">jQuery("a.image-reference").colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        # SOURCE LINE 71
        __M_writer(u'\n')
        # SOURCE LINE 72
        __M_writer(unicode(body_end))
        __M_writer(u'\n</body>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        # SOURCE LINE 14
        __M_writer(u'\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'bootstrap')._populate(_import_ns, [u'*'])
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n')
        # SOURCE LINE 41
        if len(translations) > 1:
            # SOURCE LINE 42
            __M_writer(u'                <li>')
            __M_writer(unicode(base.html_translations()))
            __M_writer(u'</li>\n')
        # SOURCE LINE 44
        __M_writer(u'            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


