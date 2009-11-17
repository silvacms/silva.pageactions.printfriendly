# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from silva.pageactions.base.base import PageAction
from silva.core.views import views as silvaviews
from silva.core.layout.interfaces import ISilvaLayer, ISilvaSkin

from zope.publisher.browser import applySkin
from five import grok


class IPrintLayer(ISilvaLayer):
    pass


class IPrintSkin(IPrintLayer, ISilvaSkin):
    pass


class PrintFriendly(silvaviews.View):

    grok.name('print.html')

    def update(self):
        self.response.setHeader(
            'Content-Type', 'text/html;charset=utf-8')
        self.response.setHeader(
            'Cache-Control','max-age=7200, must-revalidate')
        applySkin(self.request, IPrintSkin)


class PrintAction(PageAction):

    grok.order(20)

