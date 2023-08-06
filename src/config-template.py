config = {
    'host': "",
    'user': "",
    'password': "",
    'database': ""
}
selfref = {
    'root_url': "http://127.0.0.1:5000"
}
discord = {
    'redir_url': selfref["root_url"] + "/discord/redirected",
    'client_id': '',
    'client_secret': '',
    'api_endpoint': 'https://discord.com/api',
    'state_ttl': 300,
    'token_ttl': 15*60,
    'userid_claim': selfref["root_url"] + "/discord/userid"
}