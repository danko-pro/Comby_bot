from aiogram import Router

router = Router()

# Import all routers
from .command_router import command_router
from .admin_router import admin_router

# Include all routers
router.include_router(command_router)
router.include_router(admin_router)