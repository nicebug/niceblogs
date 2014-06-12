# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1402589123.16
_enable_loop = True
_template_filename = u'd:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/post_helper.tmpl'
_template_uri = u'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_title', 'html_tags', 'html_pager', 'twitter_card_information', 'html_translations', 'mathjax_script']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        link = context.get('link', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <h1>')
        __M_writer(filters.html_escape(unicode(title)))
        __M_writer(u'</h1>\n')
        if link:
            __M_writer(u"            <p><a href='")
            __M_writer(unicode(link))
            __M_writer(u"'>")
            __M_writer(unicode(messages("Original site")))
            __M_writer(u'</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.tags:
            __M_writer(u'        &nbsp;&nbsp;|&nbsp;&nbsp;')
            __M_writer(unicode(messages("More posts about")))
            __M_writer(u'\n')
            for tag in post.tags:
                __M_writer(u'            <a class="tag" href="')
                __M_writer(unicode(_link('tag', tag)))
                __M_writer(u'"><span class="badge badge-info">')
                __M_writer(unicode(tag))
                __M_writer(u'</span></a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <ul class="pager">\n')
        if post.prev_post:
            __M_writer(u'        <li class="previous">\n            <a href="')
            __M_writer(unicode(post.prev_post.permalink()))
            __M_writer(u'">&larr; ')
            __M_writer(unicode(messages("Previous post")))
            __M_writer(u'</a>\n        </li>\n')
        if post.next_post:
            __M_writer(u'        <li class="next">\n            <a href="')
            __M_writer(unicode(post.next_post.permalink()))
            __M_writer(u'">')
            __M_writer(unicode(messages("Next post")))
            __M_writer(u' &rarr;</a>\n        </li>\n')
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer(u'        <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(unicode(twitter_card.get('card', 'summary'))))
            __M_writer(u'">\n        <meta name="og:url" content="')
            __M_writer(unicode(post.permalink(absolute=True)))
            __M_writer(u'">\n')
            if 'site:id' in twitter_card:
                __M_writer(u'            <meta name="twitter:site:id" content="')
                __M_writer(unicode(twitter_card['site:id']))
                __M_writer(u'">\n')
            elif 'site' in twitter_card:
                __M_writer(u'            <meta name="twitter:site" content="')
                __M_writer(unicode(twitter_card['site']))
                __M_writer(u'">\n')
            if 'creator:id' in twitter_card:
                __M_writer(u'            <meta name="twitter:creator:id" content="')
                __M_writer(unicode(twitter_card['creator:id']))
                __M_writer(u'">\n')
            elif 'creator' in twitter_card:
                __M_writer(u'            <meta name="twitter:creator" content="')
                __M_writer(unicode(twitter_card['creator']))
                __M_writer(u'">\n')
            __M_writer(u'        <meta name="og:title" content="')
            __M_writer(filters.html_escape(unicode(post.title()[:70])))
            __M_writer(u'">\n')
            if post.description():
                __M_writer(u'            <meta name="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.description()[:200])))
                __M_writer(u'">\n')
            else:
                __M_writer(u'            <meta name="og:description" content="')
                __M_writer(filters.html_escape(unicode(post.text(strip_html=True)[:200])))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                &nbsp;&nbsp;|&nbsp;&nbsp;\n                <a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'">')
                    __M_writer(unicode(messages("Read in English", langname)))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.is_mathjax:
            __M_writer(u'        <script src="/assets/js/mathjax.js" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 7, "21": 19, "22": 29, "23": 44, "24": 67, "25": 73, "31": 2, "38": 2, "39": 3, "40": 3, "41": 4, "42": 5, "43": 5, "44": 5, "45": 5, "46": 5, "52": 22, "58": 22, "59": 23, "60": 24, "61": 24, "62": 24, "63": 25, "64": 26, "65": 26, "66": 26, "67": 26, "68": 26, "74": 31, "79": 31, "80": 33, "81": 34, "82": 35, "83": 35, "84": 35, "85": 35, "86": 38, "87": 39, "88": 40, "89": 40, "90": 40, "91": 40, "92": 43, "98": 46, "103": 46, "104": 47, "105": 48, "106": 48, "107": 48, "108": 49, "109": 49, "110": 50, "111": 51, "112": 51, "113": 51, "114": 52, "115": 53, "116": 53, "117": 53, "118": 55, "119": 56, "120": 56, "121": 56, "122": 57, "123": 58, "124": 58, "125": 58, "126": 60, "127": 60, "128": 60, "129": 61, "130": 62, "131": 62, "132": 62, "133": 63, "134": 64, "135": 64, "136": 64, "142": 10, "150": 10, "151": 11, "152": 12, "153": 13, "154": 14, "155": 15, "156": 15, "157": 15, "158": 15, "164": 69, "168": 69, "169": 70, "170": 71, "176": 170}, "uri": "post_helper.tmpl", "filename": "d:\\Python27\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/post_helper.tmpl"}
__M_END_METADATA
"""
