# -*- coding: utf-8 -*-

from google.appengine.ext import db
from resources_kind import ResourcesKind

class Resources(db.Model):
	name = db.StringProperty()
	kind = db.ReferenceProperty(ResourcesKind)
	is_used = db.BooleanProperty()
	room_returned = db.StringProperty()
	room_used = db.StringProperty()
	till = db.DateTimeProperty()
