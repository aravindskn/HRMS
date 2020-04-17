"""
This module defines the environment to be activated.
"""

# pylint: disable=R0903
class EnvironmentSettings:
    """
    This class contains the definitions of the availabile environment profiles and
    also devines the one that is ative

    Attributes:
        production (str): Defines the module containing production environment settings
        staging (str): Defines the module containing staging environment settings
        local (str): Defines the module containing local environment settings
        environment (str): Defines the environment settings that should be effected
    """

    production = 'hrms.settings.prod'
    staging = 'hrms.settings.staging'
    local = 'hrms.settings.local'
    environment = staging
