from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.api.routes.health import router as health_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.api.routes.chat import router as chat_router
from backend.api.routes.session import session_router
from backend.lifecycle.startup import startup
from backend.lifecycle.shutdown import shutdown



# Application lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Application startup
    startup()

    yield

    # Application shutdown
    shutdown()


def create_app() -> FastAPI:
    app = FastAPI(
        title = 'Agentic Research Assistant API',
        description = 'Backend API for the Agentic Research Assistant.',
        version = '1.0.0.',
        lifespan = lifespan
    )

    # Fast API router
    app.include_router(health_router)
    app.include_router(chat_router)
    app.include_router(session_router)

    # Mounting the static files
    app.mount(
        '/static',
        StaticFiles(directory = 'src/frontend/ui'),
        name = 'static'
    )

    @app.get('/', include_in_schema = False)
    async def serve_frontend():
        # Serving the applications frontend
        return FileResponse('src/frontend/ui/AutoResearch.html')

    # Middleware will be registered here.

    # API routes will be registere here.
    



    return app