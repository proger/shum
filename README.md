# shum

This is a module for [Vulyk Crowdsourcing Platform](https://github.com/mrgambal/vulyk) that provides Utterance Verification task.

To get started, install the package first in editable mode:

```
pip3 install -e .
```

Provide local settings:

```bash
cat > local_settings.py << EOF
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

LANGUAGE = 'ua'

MONGODB_SETTINGS = {
    'DB': 'vulyk',
}

ENABLED_TASKS = {
    #'vulyk_declaration': 'DeclarationTaskType',
    #'vulyk_tagging': 'TaggingTaskType',
    #'vulyk_ner': 'NERTaggingTaskType',
    'shum': 'UtteranceVerificationTaskType',
}
EOF
```

Initialize MongoDB and start the web app:

```
python3 -m shum init utterance_verification_task
python3 -m shum.table wandb/artifact/here:v1 > utterances.json
python3 -m shum db load utterance_verification_task utterances.json
python3 -m shum run
```
