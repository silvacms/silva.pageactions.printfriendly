# -*- coding: utf-8 -*-
# Copyright (c) 2009 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from silva.pageactions.base.base import PageAction
from silva.core.views import views as silvaviews

from five import grok


class PrintFriendly(silvaviews.Template):

    grok.name('print.html')


class PrintAction(PageAction):

    grok.order(20)

