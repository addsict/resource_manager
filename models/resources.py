# -*- coding: utf-8 -*-

from google.appengine.ext import db
from resources_kind import ResourcesKind

class Resources(db.Model):
	# meta data
	name = db.StringProperty()
	category = db.StringProperty()
	detail = db.StringProperty()
	room_returned = db.StringProperty()

	# utility data
	is_used = db.BooleanProperty()
	user = db.StringProperty()
	room_used = db.StringProperty()
	using_date = db.StringProperty()

	def to_dict(self):
		return {'id': self.key().id(),
				'name': self.name,
				'category': self.category,
				'detail': self.detail,
				'room_returned': self.room_returned,
				'is_used': self.is_used,
				'user': self.user,
				'room_used': self.room_used,
				'using_date': self.using_date}
