
from __future__ import with_statement

import pstats
from django.conf import settings
try:
    import cProfile 
except ImportError:
    import profile
    
import StringIO



class ProfilerMiddleware(object):
    
    def can(self, request):
        if settings.DEBUG and settings.Profiler["enable"]:
            return True

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.can(request):
            self.profiler = cProfile.Profile()
            self.profiler.enable()

           
    def process_response(self, request, response):
        if self.can(request):
            self.profiler.disable()

            StringIO = StringIO.StringIO()
            
            sortby = settings.Profiler.get('sort', 'time')  
            count = int(setting.Profiler.get('count', 50))
            output = settings.Profiler.get('output', ['console'])
            
            ps = pstats.Stats(self.profiler, stream=s).sort_stats(sortby).print_stats(count)

            for output in settings.Profiler.get('output', ['console','file']):
                
                if output == 'console':
                    print StringIO.getvalue()

                if output == 'file':
                    file_loc = settings.Profiler.get('file_location', 'profiling_results.txt')
                    with open(file_loc,'a+') as file:
                        counter = str(s.getvalue())
                        file.write(counter)
         
        return response

       
