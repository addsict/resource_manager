#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import logging
import json
from base64 import b64decode
from google.appengine.ext.webapp import template
from models.resources import Resources

logging.basicConfig(level=logging.DEBUG)

BASIC_USERNAME = 'oscar'
BASIC_PASSWORD = 'apal'

class MainHandler(webapp2.RequestHandler):
	def get(self):
		if self._basicAuth():
			path = os.path.join(os.path.dirname(__file__), 
								'templates',
								'index.html')
			self.response.out.write(template.render(path, {}))
		else:
			# 401 unauthorized
			self.error(401)
			self.response.out.write(self.response.http_status_message(401))

	# Basic認証(参考: http://d.hatena.ne.jp/sugyan/20090311/1236724687)
	def _basicAuth(self):
		auth_header = self.request.headers.get('Authorization')
		if auth_header:
			try:
				(scheme, base64) = auth_header.split(' ')
				if scheme != 'Basic':
					return False
				(username, password) = b64decode(base64).split(':')
				if username == BASIC_USERNAME and password == BASIC_PASSWORD:
					return True
			except (ValueError, TypeError), err:
				logging.error(type(err))
				return False

		self.response.set_status(401)
		self.response.headers['WWW-Authenticate'] = 'Basic realm="BasicTest"'

class AdminHandler(webapp2.RequestHandler):
	def get(self):
		path = os.path.join(os.path.dirname(__file__),
							'templates',
							'admin.html')
		self.response.out.write(template.render(path, {}))

class ApiHandler(webapp2.RequestHandler):
	def get(self, category, resource_id=None):

		response = {
			'items': []
		}
		# all resources
		if resource_id is None:
			q = Resources.all()
			q.order('name')
			resources = q.fetch(1000)
			for resource in resources:
				response['items'].append(resource.to_dict())
		# specific resource
		
		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(response))

	def post(self, category, resource_id=None):
		name = self.request.get('name')
		category = self.request.get('category')
		detail = self.request.get('detail')
		room_returned = self.request.get('room_returned')
		self.redirect('/admin')

		resource = Resources(name=name,
							 category=category,
							 detail=detail,
							 room_returned=room_returned,
							 is_used=False)
		resource.put()
	
	def put(self, category, resource_id):
		entities = Resources.get_by_id([int(resource_id)])
		if len(entities) != 0:
			resource = entities[0]
			request_resource = json.loads(self.request.body)
			resource.is_used = request_resource['is_used']
			resource.user = request_resource['user']
			resource.room_used = request_resource['room_used']
			resource.using_date = request_resource['using_date']
			resource.put()

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/admin', AdminHandler),
	('/api/(.*)/(.*)', ApiHandler),
	('/api/(.*)', ApiHandler)
], debug=True)
