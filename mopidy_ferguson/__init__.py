from __future__ import unicode_literals

import os

import pygst
pygst.require('0.10')
import gst
import gobject

from mopidy import config, exceptions, ext


__version__ = '0.1'


class Extension(ext.Extension):

    dist_name = 'Mopidy-Ferguson'
    ext_name = 'ferguson'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__, 'ext.conf'))
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['username'] = config.String()
        schema['password'] = config.Secret()
        return schema

    def validate_environment(self):
        # try:
        #     import pysoundspot
        # except ImportError as e:
        #     raise exceptions.ExtensionError('pysoundspot library not found', e)

    # You will typically only implement one of the next three methods
    # in a single extension.

    def get_frontend_classes(self):
        from .frontend import FergusonFrontend
        return [FergusonFrontend]

    # def get_backend_classes(self):
    #     from .backend import SoundspotBackend
    #     return [SoundspotBackend]

    # def get_command(self):
    #    from .commands import SoundspotCommand
    #    return SoundspotCommand()

    # def register_gstreamer_elements(self):
    #     from .mixer import SoundspotMixer
    #     gobject.type_register(SoundspotMixer)
    #     gst.element_register(
    #         SoundspotMixer, 'soundspotmixer', gst.RANK_MARGINAL)