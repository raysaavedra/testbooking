from rest_framework import routers

from .api import BookingModelViewSet

router = routers.SimpleRouter()
router.register(r'bookings', BookingModelViewSet)
