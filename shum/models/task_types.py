from vulyk.models.task_types import AbstractTaskType
from shum.models.tasks import UtteranceVerificationDecision, UtteranceVerificationTask


class UtteranceVerificationTaskType(AbstractTaskType):
    answer_model = UtteranceVerificationDecision
    task_model = UtteranceVerificationTask

    name = 'Utterance Verification'
    description = "Does the text match the audio?"

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'utterance_verification'

    redundancy = 1

    JS_ASSETS = ['static/wavesurfer.js', 'static/wavesurfer.spectrogram.js', 'static/shum.js']
    CSS_ASSETS = ['static/shum.css']