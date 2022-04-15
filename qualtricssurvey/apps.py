# -*- coding: utf-8 -*-
"""
qualtricssurvey Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class QualtricsSurveyAppConfig(AppConfig):
    """
    Configuration for the qualtricssurvey Django application.
    """

    name = 'qualtricssurvey'
    plugin_app = { }

    def ready(self):
        """
        Handle any necessary actions when the app is ready.
        """
