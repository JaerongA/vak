import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "vak"
__summary__ = "automated annotation of vocalizations for everybody"
__uri__ = "https://github.com/NickleDave/vak"

__version__ = "0.3.0a1"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "David Nicholson, Yarden Cohen"
__email__ = "dnicho4@emory.edu"

__license__ = "BSD"
__copyright__ = "2019 %s" % __author__
