from pathlib import Path
import uvicorn



# Project Root
ROOT_DIR = Path(__file__).resolve().parent


# Downloads Folder
DOWNLOADS_DIR = ROOT_DIR / "downloads"


# Create folder only if it does not exist
if not DOWNLOADS_DIR.exists():
    DOWNLOADS_DIR.mkdir(
        parents=True
    )


if __name__ == "__main__":
    uvicorn.run(
        "src.backend.api.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )