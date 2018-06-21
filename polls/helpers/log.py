from polls.models import Log


def log(message, long_message=None, log_level=1):
    assert 0 < log_level <= 5
    if long_message is None: long_message = message

    obj = Log(short=message, long=long_message, log_level=log_level)

    print(obj.short)

    obj.save()

    return obj
