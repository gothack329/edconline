#-*- coding:UTF-8 -*-
from article.models import *
import xadmin
from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction


class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "Notice", "content": "<h3> Welcome to Xadmin! </h3><p>this is html text</p>"},
     #       {"type": "chart", "model": "app.accessrecord", 'chart': 'user_count', 'params': {'_p_date__gte': '2013-01-08', 'p': 1, '_p_date__lt': '2013-01-29'}},
            {"type": "list", "model": "cmdb.device", 'params': {'o':'-uptime'}},
        ],
        [
            {"type": "qbutton", "title": "Quick Start", "btns": [{'model': Article}, {'model':Article}, {'title': "Google", 'url': "http://www.google.com"}]},
            {"type": "addform", "model": Article},
        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSetting(object):
    #global_search_models = [Host, IDC]
   # global_models_icon = {
   #     MemoStaff:'fa fa-user'
   # }
    menu_style = 'accordion'
    site_title = '物志'
#    def get_site_menu(self):
#        return ({'title':'友情链接', 'menus':(
#            {'title':'百度','url':'test'},
#            )},
#        )
xadmin.site.register(views.CommAdminView, GlobalSetting)

class ArticleAdminx(object):
    list_display = ('id','title','author','publish_date') 
    list_display_links = ('title',)
    list_editable = ['tag']

    search_fields = ['title','detail','tag']
    relfield_style = 'fk-ajax'
    reversion_enable = True
xadmin.site.register(Article,ArticleAdminx)

