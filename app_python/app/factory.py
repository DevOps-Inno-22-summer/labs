from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import config
from .middleware import CacheControlHeader
from .api import router


def build_app(settings: config.Settings):
    app = FastAPI(
        title='APP API',
        description=settings.description,
        version=settings.version,
        openapi_url=settings.prefix + '/openapi.json',
        docs_url='/',
        redoc_url='/redoc',
    )
    app.add_middleware(CacheControlHeader, header_value='no-store')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        router,
        prefix=settings.prefix,
    )
    return app


def prod_app():
    settings = config.get_settings()
    app = build_app(settings)
    return app
