import json
import logging

from helga.plugins.webhooks import route


logger = logging.getLogger(__name__)


VALID_EVENTS = [
    'commit_comment',
    'create',
    'delete',
    'deployment',
    'deployment_status',
    'fork',
    'gollum',
    'issue_comment',
    'issues',
    'member',
    'membership',
    'page_build',
    'ping',
    'public',
    'pull_request_review_comment',
    'pull_request',
    'push',
    'repository',
    'release',
    'status',
    'team_add',
    'watch',
]


@route(r'/github_alerts', methods=['POST'])
def ghithub_alerts(request, client):
    event_name = request.getHeader('X-Github-Event')
    payload = json.load(request.content)

    if event_name not in VALID_EVENTS:
        # Bad request. An invalid event name
        logger.warning('Received bad github event: %s', event_name)
        request.setResponseCode(400)
        return 'Bad Request'

    # Setting up a webhook: github will send a 'ping' event
    # See: https://developer.github.com/webhooks/#ping-event
    if event_name == 'ping':
        logger.info('Responding to github webhook PING: %s', payload)
        return 'PONG'

    logger.debug('Received github event %s. Payload: %s', event_name, payload)

    return 'Success!'
