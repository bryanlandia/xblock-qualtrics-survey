"""
Handle view logic for the XBlock
"""
from __future__ import absolute_import
from six import text_type
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin
from xblock.core import XBlock
from xblockutils.settings import XBlockWithSettingsMixin
from .mixins.fragment import XBlockFragmentBuilderMixin
from django.utils.safestring import mark_safe


@XBlock.wants("user")
@XBlock.wants("settings")
class QualtricsSurveyViewMixin(
        XBlock,
        XBlockWithSettingsMixin,
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for the XBlock
    """

    loader = ResourceLoader(__name__)
    show_in_read_only_mode = True

    # pylint: disable=no-member
    def user_data(self):
        """
        This method initializes the user's parameters
        """
        runtime = self.runtime  # pylint: disable=no-member
        user = runtime.service(self, 'user').get_current_user()
        user_data = {}
        user_data["user_id"] = user.opt_attrs["edx-platform.user_id"]
        user_data["email"] = user.emails[0]
        user_data["role"] = runtime.get_user_role()
        user_data["username"] = user.opt_attrs['edx-platform.username']
        user_data["anonymous_student_id"] = runtime.anonymous_student_id
        return user_data

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context = dict(context)
        student_id = self.user_data().get("user_id", "")
        student_email = mark_safe("&email={}".format(self.user_data().get("email", "")))
        user_id_string = ''
        user_id_string = ("?edxuid={student_id}").format(
            student_id=student_id,
        )
        extra_params_string = mark_safe("&{}".format(self.extra_params))
        context.update({
            'xblock_id': text_type(self.scope_ids.usage_id),
            'survey_id': self.survey_id,
            'your_university': self.your_university,
            'link_text': self.link_text,
            'user_id_string': user_id_string,
            'student_email': student_email,
            'extra_params_string': extra_params_string,
            'message': self.message,
        })
        return context
