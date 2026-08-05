import uvicorn
from backend.api_main import create_app



# System's entry point
app = create_app()


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host = '127.0.0.1',
        port = 8000,
        reload = True
    )