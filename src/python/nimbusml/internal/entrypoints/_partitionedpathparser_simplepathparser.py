# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
SimplePathParser
"""


from ..utils.entrypoints import Component
from ..utils.utils import try_set


def simple_path_parser(
        columns=None,
        type='TX',
        **params):
    """
    **Description**
        A simple parser that extracts directory names as column values.
        Column names are defined as arguments.

    :param columns: Column definitions used to override the
        Partitioned Path Parser. Expected with the format
        name:type:numeric-source, for example, col=MyFeature:R4:1
        (settings).
    :param type: Data type of each column. (settings).
    """

    entrypoint_name = 'SimplePathParser'
    settings = {}

    if columns is not None:
        settings['Columns'] = try_set(
            obj=columns,
            none_acceptable=True,
            is_of_type=list,
            is_column=True)
    if type is not None:
        settings['Type'] = try_set(
            obj=type,
            none_acceptable=True,
            is_of_type=str,
            values=[
                'I1',
                'U1',
                'I2',
                'U2',
                'I4',
                'U4',
                'I8',
                'U8',
                'R4',
                'Num',
                'R8',
                'TX',
                'Text',
                'TXT',
                'BL',
                'Bool',
                'TimeSpan',
                'TS',
                'DT',
                'DateTime',
                'DZ',
                'DateTimeZone',
                'UG',
                'U16'])

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='PartitionedPathParser')
    return component
