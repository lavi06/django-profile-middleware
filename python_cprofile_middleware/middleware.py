 
from __future__ import with_statement

from cStringIO import StringIO
import cProfile, pstats, StringIO
from django.conf import settings


class ProfilerMiddleware(object):
    
    def can(self, request):
        return settings.DEBUG 

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.can(request):
            self.profiler = cProfile.Profile()
            self.profiler.enable()

            

    def process_response(self, request, response):
        if self.can(request):
            self.profiler.disable()

            s = StringIO.StringIO()
            sortby = 'time'
            ps = pstats.Stats(self.profiler, stream=s).sort_stats(sortby)
            ps.print_stats()
            print s.getvalue()


            file = open("profiling_results.txt","w") 

            with open('profiling_results.txt','r+') as f:
                counter = str(s.getvalue())
                f.write(counter)
         
            return response

       
