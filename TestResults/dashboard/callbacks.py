from apps.home.homeCB import register_home_callbacks
from apps.views.viewsCB import register_views_callbacks
from apps.failures.failuresCB import register_failures_callbacks

from app import app

register_home_callbacks(app)
register_views_callbacks(app)
register_failures_callbacks(app)
