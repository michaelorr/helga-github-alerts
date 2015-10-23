from helga.plugins import route


@route(r'/github_alerts', methods=['POST'])
def ghithub_alerts(request, client):
    return 'Success!'
