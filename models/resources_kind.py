# -*- coding: utf-8 -*-

from google.appengine.ext import db

class ResourcesKind(db.Model):
	kind_name = db.StringProperty()

