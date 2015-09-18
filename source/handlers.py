# handlers.py
class EntryHandler(BaseHandler):
	model = Entry
	methods_allowed = ('GET')

	def read(self, request, slug):
		entry = get_object_or_404(Entry, slug=slug)
		return entry
