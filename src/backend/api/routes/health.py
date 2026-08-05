from fastapi import APIRouter



router = APIRouter()


@router.get('/health')
async def health_check():
    return {
        'Status': 'Healthy',
        'Message': 'Backend is running successfully.'
    }