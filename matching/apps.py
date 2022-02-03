from django.apps import AppConfig
from django.db.models.signals import post_save


class MatchingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "matching"

    def ready(self):
        super().ready()

        from . import signals

        # TODO: prevent multiple signals
        post_save.connect(
            signals.look_for_matches_for_offer, dispatch_uid="offer_matches"
        )

        post_save.connect(
            signals.look_for_matches_for_request,
            dispatch_uid="request_matches",
        )
