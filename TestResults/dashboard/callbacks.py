from dashboard.apps.home.homeCB import register_home_callbacks
from dashboard.apps.views.viewsCB import register_views_callbacks
from dashboard.apps.failures.failuresCB import register_failures_callbacks

from dashboard.app import app

register_home_callbacks(app)
register_views_callbacks(app)
register_failures_callbacks(app)
