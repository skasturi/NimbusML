# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
PlattCalibrator
"""


from ..utils.entrypoints import Component


def platt_calibrator(
        **params):
    """
    **Description**
        Platt calibration.

    """

    entrypoint_name = 'PlattCalibrator'
    settings = {}

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='CalibratorTrainer')
    return component