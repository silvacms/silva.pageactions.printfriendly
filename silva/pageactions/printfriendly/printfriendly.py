# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from five import grok
from silva.core.layout.interfaces import ISilvaLayer, ISilvaSkin
from silva.core.views import views as silvaviews
from silva.pageactions.base.base import PageAction
from zope.publisher.browser import applySkin


class IPrintLayer(ISilvaLayer):
    pass


class IPrintSkin(IPrintLayer, ISilvaSkin):
    pass


class PrintFriendly(silvaviews.View):

    grok.name('print.html')

    def update(self):
        applySkin(self.request, IPrintSkin)


class PrintAction(PageAction):

    grok.order(20)
