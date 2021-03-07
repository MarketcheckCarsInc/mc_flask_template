"""
Demo API route handlers

"""

from .demoService import DemoHelloWorld,DemoBigTableGet,DemoServiceReadiness,DemoServiceLiveness,DemoServiceHealth

##
## Actually setup the Api resource routing here
##
def initialize_routes(api): 
    api.add_resource(DemoHelloWorld, '/api/v1/demo/1')
    api.add_resource(DemoBigTableGet, '/api/v1/demo/2')
    api.add_resource(DemoServiceReadiness, '/readiness_check')
    api.add_resource(DemoServiceLiveness, '/liveness_check')
    api.add_resource(DemoServiceHealth, '/health')