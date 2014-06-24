# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1403627669.488
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/disqus_helper.tmpl'
_template_uri = u'disqus_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_disqus_script', 'html_disqus_link', 'comment_form', 'comment_link_script', 'html_disqus', 'comment_link']



import json
translations = {
    'es': 'es_ES',
}


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_link_script():
            return render_comment_link_script(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(comment_link_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_link(link,identifier):
            return render_comment_link(context,link,identifier)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(comment_link(link, identifier)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'        <div id="disqus_thread"></div>\n        <script type="text/javascript">\n        var disqus_shortname ="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'";\n')
            if url:
                __M_writer(u'            var disqus_url="')
                __M_writer(unicode(url))
                __M_writer(u'";\n')
            __M_writer(u'        var disqus_title=')
            __M_writer(unicode(json.dumps(title)))
            __M_writer(u';\n        var disqus_identifier="')
            __M_writer(unicode(identifier))
            __M_writer(u'";\n        var disqus_config = function () {\n            this.language = "')
            __M_writer(unicode(translations.get(lang, lang)))
            __M_writer(u'";\n        };\n        (function() {\n            var dsq = document.createElement(\'script\'); dsq.type = \'text/javascript\'; dsq.async = true;\n            dsq.src = \'http://\' + disqus_shortname + \'.disqus.com/embed.js\';\n            (document.getElementsByTagName(\'head\')[0] || document.getElementsByTagName(\'body\')[0]).appendChild(dsq);\n        })();\n    </script>\n    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n    <a href="http://disqus.com" class="dsq-brlink">Comments powered by <span class="logo-disqus">Disqus</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if comment_system_id:
            __M_writer(u'       <script type="text/javascript">var disqus_shortname="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'";(function(){var a=document.createElement("script");a.async=true;a.type="text/javascript";a.src="http://"+disqus_shortname+".disqus.com/count.js";(document.getElementsByTagName("HEAD")[0]||document.getElementsByTagName("BODY")[0]).appendChild(a)}());</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_disqus(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        def comment_form(url,title,identifier):
            return render_comment_form(context,url,title,identifier)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(comment_form(url, title, identifier)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <p>\n')
        if comment_system_id:
            __M_writer(u'        <a href="')
            __M_writer(unicode(link))
            __M_writer(u'#disqus_thread" data-disqus-identifier="')
            __M_writer(unicode(identifier))
            __M_writer(u'">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 33, "129": 35, "130": 36, "131": 36, "132": 36, "133": 36, "134": 36, "140": 134, "15": 2, "22": 0, "27": 7, "28": 31, "29": 38, "30": 45, "31": 50, "32": 54, "33": 58, "39": 56, "45": 56, "46": 57, "47": 57, "53": 52, "59": 52, "60": 53, "61": 53, "67": 9, "73": 9, "74": 10, "75": 11, "76": 13, "77": 13, "78": 14, "79": 15, "80": 15, "81": 15, "82": 17, "83": 17, "84": 17, "85": 18, "86": 18, "87": 20, "88": 20, "94": 41, "99": 41, "100": 42, "101": 43, "102": 43, "103": 43, "109": 48, "115": 48, "116": 49, "117": 49, "123": 33}, "uri": "disqus_helper.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/disqus_helper.tmpl"}
__M_END_METADATA
"""
