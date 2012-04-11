from datetime import date, time
import calendar
import json


class ObjectEncoder(json.JSONEncoder):
    '''
    Encode any object with the method as_json on it.
    '''
    def default(self, obj):
        if hasattr(obj, 'as_json'):
            return obj.as_json()
        elif isinstance(obj, (datetime, date)):
            return calendar.timegm(obj.timetuple()) * 1000
        else:
            return super(ObjectEncoder, self).default(obj)


def dump_json(chart):
    '''Dumps a chart to json'''
    return json.dumps(chart, cls=ObjectEncoder)
