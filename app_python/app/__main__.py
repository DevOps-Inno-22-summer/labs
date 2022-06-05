from uvicorn import Config, Server
from . import config
from . import factory


if __name__ == '__main__':
    settings = config.get_settings()
    app = factory.build_app(settings)
    server = Server(
        Config(
            app,
            host="0.0.0.0",
            port=8080,
            log_level='info',
        ),
    )
    server.run()
