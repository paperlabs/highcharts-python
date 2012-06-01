'''
The different types of series that can be charted.
'''
import options
import types
import config_sections
from common import *


class Point(DictBacked):
    '''
    A specific data point in a series.

    Points can be defined as Point objects, numbers, or (x, y) pairs of numbers.
    See http://www.highcharts.com/ref/#point for available options.
    '''
    available_options = options.POINT

    def __init__(self, data=None, **kwargs):
        super(Point, self).__init__(**kwargs)
        if data == None:
            return
        if not isinstance(data, basestring) and hasattr(data, '__iter__') and len(data) == 2:
            if isinstance(data[0], basestring):
                self.name = data[0]
            else:
                self.x = data[0]
            self.y = data[1]
        else:
            self.y = data


class Series(DictBacked):
    '''
    The base class for any series type.

    See http://www.highcharts.com/ref/#plotOptions-series for available options.
    '''
    def __init__(self, data=[], **kwargs):
        if self.defaults is None:
            self.defaults = {}
        self.defaults['type'] = self.series_type
        self.available_options += options.SERIES
        super(Series, self).__init__(**kwargs)
        self.data = data

    def __setattr__(self, attr, val):
        '''Custom behavior for setting "data"'''
        if attr == 'data':
            self.options['data'] = [x if isinstance(x, (Point, types.NoneType)) else Point(x) for x in val]
        else:
            super(Series, self).__setattr__(attr, val)


class SplineSeries(Series):
    series_type = 'spline'
    available_options = ['step', 'marker']
    defaults = {
        'marker': config_sections.MarkerConfig
    }


class AreaSplineSeries(Series):
    series_type = 'areaspline'
    available_options = ['fillColor', 'fillOpacity', 'lineColor', 'threshold',  'marker']
    defaults = {
        'marker': config_sections.MarkerConfig
    }


class AreaSeries(Series):
    '''
    An area chart series.

    See http://www.highcharts.com/ref/#plotOptions-area for available options.
    '''
    series_type = 'area'
    available_options = ['fillColor', 'fillOpacity', 'lineColor', 'threshold']


class ColumnSeries(Series):
    '''
    A column chart series.

    See http://www.highcharts.com/ref/#plotOptions-column for available options.
    '''
    series_type = 'column'
    available_options = ['borderColor', 'borderRadius', 'borderWidth', 'colorByPoint', 'groupPadding', 'minPointLength', 'pointPadding', 'pointWidth']


class LineSeries(Series):
    '''
    A line chart series.

    See http://www.highcharts.com/ref/#plotOptions-line for available options.
    '''
    series_type = 'line'
    available_options = ['step']


class PieSeries(Series):
    '''
    A pie chart series.

    See http://www.highcharts.com/ref/#plotOptions-pie for available options.
    '''
    series_type = 'pie'
    available_options = ['size', 'sliced', 'slicedOffset', 'center']
