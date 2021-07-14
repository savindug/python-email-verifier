import threading

from validate_email import validate_email


def verify_email(email):
    return validate_email(email_address=email, check_format=True, check_blacklist=True, check_dns=True,
                          dns_timeout=10, check_smtp=True, smtp_timeout=10, smtp_helo_host='noreply.host',
                          smtp_from_address='noreply@noreply21.com', smtp_debug=False)



