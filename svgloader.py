from PySide import QtGui, QtCore, QtNetwork, QtSvg


class SVGLoader(QtCore.QObject):
    """Provides signals and slots to asynchronously load an SVG from a URL.
    Classes that implement signals and slots must derive from QtCore.QObject, and call the superclass's __init__
    function."""
    loaded = QtCore.Signal(QtSvg.QGraphicsSvgItem)

    def __init__(self, parent=None):
        super(SVGLoader, self).__init__(parent)
        self.graphics_item = None
        self.renderer = None
        self.network_manager = QtNetwork.QNetworkAccessManager()
        self.network_manager.finished[QtNetwork.QNetworkReply].connect(self._image_loaded)

    @QtCore.Slot(str)
    def load(self, url):
        """Initiates fetching of the resource from the given URL."""
        self.network_manager.get(QtNetwork.QNetworkRequest(QtCore.QUrl(url)))

    @QtCore.Slot(QtNetwork.QNetworkReply)
    def _image_loaded(self, reply):
        """A 'private' slot that gets called once the network request has finished.
        Gets called regardless of the success or failure of the request."""
        if reply.error() == QtNetwork.QNetworkReply.NoError:
            self.renderer = QtSvg.QSvgRenderer(reply.readAll())
            self.graphics_item = QtSvg.QGraphicsSvgItem()
            self.graphics_item.setSharedRenderer(self.renderer)
        else:
            self.graphics_item = QtGui.QGraphicsTextItem()
            self.graphics_item.setHtml('<h1>Error loading image</h1>')

        self.loaded.emit(self.graphics_item)