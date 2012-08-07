# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from five import grok
from silva.core.layout.interfaces import ISilvaLayer, ISilvaSkin
from silva.core.views import views as silvaviews
from silva.pageactions.base.base import PageAction
from silva.core.views.interfaces import IView
from zope.publisher.browser import applySkin
from zope.component import queryMultiAdapter

from zExceptions import NotFound


class IPrintLayer(ISilvaLayer):
    pass


class IPrintSkin(IPrintLayer, ISilvaSkin):
    pass


class PrintFriendly(silvaviews.View):
    grok.name('print.html')

    def update(self):
        applySkin(self.request, IPrintSkin)
        self.html = None
        view = queryMultiAdapter(
            (self.context, self.request), name='content.html')
        if view is None:
            raise NotFound('content.html')
        if IView.providedBy(view) and view.content is not None:
            self.html = view()


class PrintAction(PageAction):
    grok.order(20)
