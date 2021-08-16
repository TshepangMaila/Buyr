from flask_restful import Api
from resources.UserResource import LoginResource, RegisterResource

routes = [
    '/login',
    '/register'
]

routeResources = [
    LoginResource,
    RegisterResource
]


def register_routes(api) -> None:

    for route, routeResource in zip(routes, routeResources):

        api.add_resource(routeResource, route)