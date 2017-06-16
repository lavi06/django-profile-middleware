import pstats
import cProfile as profile
from cStringIO import StringIO
import cProfile, pstats, StringIO
from django.conf import settings
from django.http import HttpResponse
from functools import wraps
# from django.utils.deprecation import MiddlewareMixin

class ProfilerMiddleware(object):
    
    def can(self, request):
        return settings.DEBUG 

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.can(request):
            self.profiler = profile.Profile()
            self.profiler.enable()


            



    def process_response(self, request, response):
        if self.can(request):
            self.profiler.disable()
            s = StringIO.StringIO()
            sortby = 'time'
            ps = pstats.Stats(self.profiler, stream=s).sort_stats(sortby)
            ps.print_stats(20)
            ps.dump_stats("profiling output")
            print s.getvalue()

            return response


       
