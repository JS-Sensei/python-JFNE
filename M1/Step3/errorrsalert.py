alert_system = 'email' # other value can be 'email'
error_severity = 'medium' # other values: 'medium' or 'low'
error_message = 'OMG! Something Terrible happened!'


def send_email(email, msg): 
    print('Sending Email to: [', email, ']')
    print('Email Content: \n \t', msg)
    print('....End')

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_severity == 'medium':
        send_email('support.1@example.com', error_message)
    else:
        send_email('support.2@example.com', error_message)

