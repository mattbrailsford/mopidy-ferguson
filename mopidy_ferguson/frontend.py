import pykka

from mopidy.core import CoreListener

logger = logging.getLogger('mopidy_ferguson')

class FergusonFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, core):
        super(FergusonFrontend, self).__init__()
        self.core = core

    # Your frontend implementation