"""
File for processing the size chart of the boards, as well as the filters based on rider's preferences.
"""

# dictionary for mapping the free-ride boards sizes based on rider's height
freeride_size_chart = {
    'lt_160': '145-151',
    'gt_160_lt_170': '151-155',
    'gt_170_lt_180': '155-158',
    'gt_180': '158-160'
}

# dictionary for mapping the park boards sizes based on rider's height
park_size_chart = {
    'lt_160': '140-145',
    'gt_160_lt_170': '145-149',
    'gt_170_lt_180': '149-153',
    'gt_180': '153-156'
}


def process_size_range(height, style):
    """
     Processing the size range of a board, based on the rider's height and environment.
    :param height: rider's height in cm
    :param style: may be free-ride/freestyle/all-mountain
    :return: size range
    """
    size_range = None
    if height < 160:
        size_range = park_size_chart['lt_160'] if style == 'park' else freeride_size_chart['lt_160']
    elif 160 <= height < 170:
        size_range = park_size_chart['gt_160_lt_170'] if style == 'park' else freeride_size_chart['gt_160_lt_170']
    elif 170 <= height < 180:
        size_range = park_size_chart['gt_170_lt_180'] if style == 'park' else freeride_size_chart['gt_170_lt_180']
    elif height > 180:
        size_range = park_size_chart['gt_180'] if style == 'park' else freeride_size_chart['gt_180']
    return size_range


def process_queryset(gender, skills, style):
    """
    Processing filters for the Snowboards queryset.
    :param gender: rider's gender (male or female)
    :param skills: rider's skills (rookie, intermediate or pro-rider)
    :param style: free-ride or free-style or all mountain
    :return: dictionary containing all the necessary filters
    """
    filter_dict = {'gender': 'Female' if gender == 'girl' else 'Male',
                   'level': 'Beginner' if 'rookie' in skills else 'Intermediate-Advanced'}
    if style == 'freestyle':
        filter_dict['style'] = 'Park'
    elif style == 'freeride':
        filter_dict['style'] = 'Freeride'
    else:
        filter_dict['style'] = 'All mountain'
    return filter_dict
