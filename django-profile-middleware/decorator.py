from functools import wraps

def iterator(extra_value):
	def _iterator(view_func):
		def _decorator(request, *args, **kwargs):
			for n in range(1,extra_value,+1):
				view_func(request, *args, **kwargs) 
			response = view_func(request, *args, **kwargs)
			return response
		return wraps(view_func)(_decorator)
	return _iterator
