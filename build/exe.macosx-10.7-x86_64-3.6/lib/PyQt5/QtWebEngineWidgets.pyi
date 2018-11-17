# The PEP 484 type hints stub file for the QtWebEngineWidgets module.
#
# Generated by SIP 4.18.1
#
# Copyright (c) 2016 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing
import sip

from PyQt5 import QtWebEngineCore
from PyQt5 import QtWidgets
from PyQt5 import QtWebChannel
from PyQt5 import QtNetwork
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QWebEngineCertificateError(sip.simplewrapper):

    class Error(int): ...
    SslPinnedKeyNotInCertificateChain = ... # type: 'QWebEngineCertificateError.Error'
    CertificateCommonNameInvalid = ... # type: 'QWebEngineCertificateError.Error'
    CertificateDateInvalid = ... # type: 'QWebEngineCertificateError.Error'
    CertificateAuthorityInvalid = ... # type: 'QWebEngineCertificateError.Error'
    CertificateContainsErrors = ... # type: 'QWebEngineCertificateError.Error'
    CertificateNoRevocationMechanism = ... # type: 'QWebEngineCertificateError.Error'
    CertificateUnableToCheckRevocation = ... # type: 'QWebEngineCertificateError.Error'
    CertificateRevoked = ... # type: 'QWebEngineCertificateError.Error'
    CertificateInvalid = ... # type: 'QWebEngineCertificateError.Error'
    CertificateWeakSignatureAlgorithm = ... # type: 'QWebEngineCertificateError.Error'
    CertificateNonUniqueName = ... # type: 'QWebEngineCertificateError.Error'
    CertificateWeakKey = ... # type: 'QWebEngineCertificateError.Error'
    CertificateNameConstraintViolation = ... # type: 'QWebEngineCertificateError.Error'

    def errorDescription(self) -> str: ...
    def isOverridable(self) -> bool: ...
    def url(self) -> QtCore.QUrl: ...
    def error(self) -> 'QWebEngineCertificateError.Error': ...


class QWebEngineDownloadItem(QtCore.QObject):

    class DownloadState(int): ...
    DownloadRequested = ... # type: 'QWebEngineDownloadItem.DownloadState'
    DownloadInProgress = ... # type: 'QWebEngineDownloadItem.DownloadState'
    DownloadCompleted = ... # type: 'QWebEngineDownloadItem.DownloadState'
    DownloadCancelled = ... # type: 'QWebEngineDownloadItem.DownloadState'
    DownloadInterrupted = ... # type: 'QWebEngineDownloadItem.DownloadState'

    def mimeType(self) -> str: ...
    def downloadProgress(self, bytesReceived: int, bytesTotal: int) -> None: ...
    def stateChanged(self, state: 'QWebEngineDownloadItem.DownloadState') -> None: ...
    def finished(self) -> None: ...
    def cancel(self) -> None: ...
    def accept(self) -> None: ...
    def isFinished(self) -> bool: ...
    def setPath(self, path: str) -> None: ...
    def path(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def receivedBytes(self) -> int: ...
    def totalBytes(self) -> int: ...
    def state(self) -> 'QWebEngineDownloadItem.DownloadState': ...
    def id(self) -> int: ...


class QWebEngineFullScreenRequest(sip.simplewrapper):

    def __init__(self, a0: 'QWebEngineFullScreenRequest') -> None: ...

    def origin(self) -> QtCore.QUrl: ...
    def toggleOn(self) -> bool: ...
    def accept(self) -> None: ...
    def reject(self) -> None: ...


class QWebEngineHistoryItem(sip.simplewrapper):

    def __init__(self, other: 'QWebEngineHistoryItem') -> None: ...

    def swap(self, other: 'QWebEngineHistoryItem') -> None: ...
    def isValid(self) -> bool: ...
    def iconUrl(self) -> QtCore.QUrl: ...
    def lastVisited(self) -> QtCore.QDateTime: ...
    def title(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def originalUrl(self) -> QtCore.QUrl: ...


class QWebEngineHistory(sip.simplewrapper):

    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def currentItemIndex(self) -> int: ...
    def itemAt(self, i: int) -> QWebEngineHistoryItem: ...
    def forwardItem(self) -> QWebEngineHistoryItem: ...
    def currentItem(self) -> QWebEngineHistoryItem: ...
    def backItem(self) -> QWebEngineHistoryItem: ...
    def goToItem(self, item: QWebEngineHistoryItem) -> None: ...
    def forward(self) -> None: ...
    def back(self) -> None: ...
    def canGoForward(self) -> bool: ...
    def canGoBack(self) -> bool: ...
    def forwardItems(self, maxItems: int) -> typing.List[QWebEngineHistoryItem]: ...
    def backItems(self, maxItems: int) -> typing.List[QWebEngineHistoryItem]: ...
    def items(self) -> typing.Any: ...
    def clear(self) -> None: ...


class QWebEnginePage(QtCore.QObject):

    class RenderProcessTerminationStatus(int): ...
    NormalTerminationStatus = ... # type: 'QWebEnginePage.RenderProcessTerminationStatus'
    AbnormalTerminationStatus = ... # type: 'QWebEnginePage.RenderProcessTerminationStatus'
    CrashedTerminationStatus = ... # type: 'QWebEnginePage.RenderProcessTerminationStatus'
    KilledTerminationStatus = ... # type: 'QWebEnginePage.RenderProcessTerminationStatus'

    class NavigationType(int): ...
    NavigationTypeLinkClicked = ... # type: 'QWebEnginePage.NavigationType'
    NavigationTypeTyped = ... # type: 'QWebEnginePage.NavigationType'
    NavigationTypeFormSubmitted = ... # type: 'QWebEnginePage.NavigationType'
    NavigationTypeBackForward = ... # type: 'QWebEnginePage.NavigationType'
    NavigationTypeReload = ... # type: 'QWebEnginePage.NavigationType'
    NavigationTypeOther = ... # type: 'QWebEnginePage.NavigationType'

    class JavaScriptConsoleMessageLevel(int): ...
    InfoMessageLevel = ... # type: 'QWebEnginePage.JavaScriptConsoleMessageLevel'
    WarningMessageLevel = ... # type: 'QWebEnginePage.JavaScriptConsoleMessageLevel'
    ErrorMessageLevel = ... # type: 'QWebEnginePage.JavaScriptConsoleMessageLevel'

    class FileSelectionMode(int): ...
    FileSelectOpen = ... # type: 'QWebEnginePage.FileSelectionMode'
    FileSelectOpenMultiple = ... # type: 'QWebEnginePage.FileSelectionMode'

    class Feature(int): ...
    Geolocation = ... # type: 'QWebEnginePage.Feature'
    MediaAudioCapture = ... # type: 'QWebEnginePage.Feature'
    MediaVideoCapture = ... # type: 'QWebEnginePage.Feature'
    MediaAudioVideoCapture = ... # type: 'QWebEnginePage.Feature'
    MouseLock = ... # type: 'QWebEnginePage.Feature'

    class PermissionPolicy(int): ...
    PermissionUnknown = ... # type: 'QWebEnginePage.PermissionPolicy'
    PermissionGrantedByUser = ... # type: 'QWebEnginePage.PermissionPolicy'
    PermissionDeniedByUser = ... # type: 'QWebEnginePage.PermissionPolicy'

    class WebWindowType(int): ...
    WebBrowserWindow = ... # type: 'QWebEnginePage.WebWindowType'
    WebBrowserTab = ... # type: 'QWebEnginePage.WebWindowType'
    WebDialog = ... # type: 'QWebEnginePage.WebWindowType'

    class FindFlag(int): ...
    FindBackward = ... # type: 'QWebEnginePage.FindFlag'
    FindCaseSensitively = ... # type: 'QWebEnginePage.FindFlag'

    class WebAction(int): ...
    NoWebAction = ... # type: 'QWebEnginePage.WebAction'
    Back = ... # type: 'QWebEnginePage.WebAction'
    Forward = ... # type: 'QWebEnginePage.WebAction'
    Stop = ... # type: 'QWebEnginePage.WebAction'
    Reload = ... # type: 'QWebEnginePage.WebAction'
    Cut = ... # type: 'QWebEnginePage.WebAction'
    Copy = ... # type: 'QWebEnginePage.WebAction'
    Paste = ... # type: 'QWebEnginePage.WebAction'
    Undo = ... # type: 'QWebEnginePage.WebAction'
    Redo = ... # type: 'QWebEnginePage.WebAction'
    SelectAll = ... # type: 'QWebEnginePage.WebAction'
    ReloadAndBypassCache = ... # type: 'QWebEnginePage.WebAction'
    PasteAndMatchStyle = ... # type: 'QWebEnginePage.WebAction'
    OpenLinkInThisWindow = ... # type: 'QWebEnginePage.WebAction'
    OpenLinkInNewWindow = ... # type: 'QWebEnginePage.WebAction'
    OpenLinkInNewTab = ... # type: 'QWebEnginePage.WebAction'
    CopyLinkToClipboard = ... # type: 'QWebEnginePage.WebAction'
    DownloadLinkToDisk = ... # type: 'QWebEnginePage.WebAction'
    CopyImageToClipboard = ... # type: 'QWebEnginePage.WebAction'
    CopyImageUrlToClipboard = ... # type: 'QWebEnginePage.WebAction'
    DownloadImageToDisk = ... # type: 'QWebEnginePage.WebAction'
    CopyMediaUrlToClipboard = ... # type: 'QWebEnginePage.WebAction'
    ToggleMediaControls = ... # type: 'QWebEnginePage.WebAction'
    ToggleMediaLoop = ... # type: 'QWebEnginePage.WebAction'
    ToggleMediaPlayPause = ... # type: 'QWebEnginePage.WebAction'
    ToggleMediaMute = ... # type: 'QWebEnginePage.WebAction'
    DownloadMediaToDisk = ... # type: 'QWebEnginePage.WebAction'
    InspectElement = ... # type: 'QWebEnginePage.WebAction'
    ExitFullScreen = ... # type: 'QWebEnginePage.WebAction'
    RequestClose = ... # type: 'QWebEnginePage.WebAction'

    class FindFlags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QWebEnginePage.FindFlags', 'QWebEnginePage.FindFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QWebEnginePage.FindFlags') -> None: ...

        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QWebEnginePage.FindFlags': ...
        def __int__(self) -> int: ...

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, profile: 'QWebEngineProfile', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def renderProcessTerminated(self, terminationStatus: 'QWebEnginePage.RenderProcessTerminationStatus', exitCode: int) -> None: ...
    def fullScreenRequested(self, fullScreenRequest: QWebEngineFullScreenRequest) -> None: ...
    def setBackgroundColor(self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]) -> None: ...
    def backgroundColor(self) -> QtGui.QColor: ...
    def acceptNavigationRequest(self, url: QtCore.QUrl, type: 'QWebEnginePage.NavigationType', isMainFrame: bool) -> bool: ...
    def setWebChannel(self, a0: QtWebChannel.QWebChannel) -> None: ...
    def webChannel(self) -> QtWebChannel.QWebChannel: ...
    def scripts(self) -> 'QWebEngineScriptCollection': ...
    def profile(self) -> 'QWebEngineProfile': ...
    def certificateError(self, certificateError: QWebEngineCertificateError) -> bool: ...
    def javaScriptConsoleMessage(self, level: 'QWebEnginePage.JavaScriptConsoleMessageLevel', message: str, lineNumber: int, sourceID: str) -> None: ...
    def javaScriptPrompt(self, securityOrigin: QtCore.QUrl, msg: str, defaultValue: str, result: str) -> bool: ...
    def javaScriptConfirm(self, securityOrigin: QtCore.QUrl, msg: str) -> bool: ...
    def javaScriptAlert(self, securityOrigin: QtCore.QUrl, msg: str) -> None: ...
    def chooseFiles(self, mode: 'QWebEnginePage.FileSelectionMode', oldFiles: typing.Iterable[str], acceptedMimeTypes: typing.Iterable[str]) -> typing.List[str]: ...
    def createWindow(self, type: 'QWebEnginePage.WebWindowType') -> 'QWebEnginePage': ...
    def iconUrlChanged(self, url: QtCore.QUrl) -> None: ...
    def urlChanged(self, url: QtCore.QUrl) -> None: ...
    def titleChanged(self, title: str) -> None: ...
    def proxyAuthenticationRequired(self, requestUrl: QtCore.QUrl, authenticator: QtNetwork.QAuthenticator, proxyHost: str) -> None: ...
    def authenticationRequired(self, requestUrl: QtCore.QUrl, authenticator: QtNetwork.QAuthenticator) -> None: ...
    def featurePermissionRequestCanceled(self, securityOrigin: QtCore.QUrl, feature: 'QWebEnginePage.Feature') -> None: ...
    def featurePermissionRequested(self, securityOrigin: QtCore.QUrl, feature: 'QWebEnginePage.Feature') -> None: ...
    def windowCloseRequested(self) -> None: ...
    def geometryChangeRequested(self, geom: QtCore.QRect) -> None: ...
    def selectionChanged(self) -> None: ...
    def linkHovered(self, url: str) -> None: ...
    def loadFinished(self, ok: bool) -> None: ...
    def loadProgress(self, progress: int) -> None: ...
    def loadStarted(self) -> None: ...
    def settings(self) -> 'QWebEngineSettings': ...
    @typing.overload
    def runJavaScript(self, scriptSource: str) -> None: ...
    @typing.overload
    def runJavaScript(self, scriptSource: str, resultCallback: typing.Callable[..., None]) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def iconUrl(self) -> QtCore.QUrl: ...
    def requestedUrl(self) -> QtCore.QUrl: ...
    def url(self) -> QtCore.QUrl: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def title(self) -> str: ...
    def toPlainText(self, resultCallback: typing.Callable[..., None]) -> None: ...
    def toHtml(self, resultCallback: typing.Callable[..., None]) -> None: ...
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    def load(self, url: QtCore.QUrl) -> None: ...
    def setFeaturePermission(self, securityOrigin: QtCore.QUrl, feature: 'QWebEnginePage.Feature', policy: 'QWebEnginePage.PermissionPolicy') -> None: ...
    def createStandardContextMenu(self) -> QtWidgets.QMenu: ...
    def findText(self, subString: str, options: 'QWebEnginePage.FindFlags' = ..., resultCallback: typing.Optional[typing.Callable[..., None]] = ...) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def triggerAction(self, action: 'QWebEnginePage.WebAction', checked: bool = ...) -> None: ...
    def action(self, action: 'QWebEnginePage.WebAction') -> QtWidgets.QAction: ...
    def selectedText(self) -> str: ...
    def hasSelection(self) -> bool: ...
    def view(self) -> QtWidgets.QWidget: ...
    def setView(self, view: QtWidgets.QWidget) -> None: ...
    def history(self) -> QWebEngineHistory: ...


class QWebEngineProfile(QtCore.QObject):

    class PersistentCookiesPolicy(int): ...
    NoPersistentCookies = ... # type: 'QWebEngineProfile.PersistentCookiesPolicy'
    AllowPersistentCookies = ... # type: 'QWebEngineProfile.PersistentCookiesPolicy'
    ForcePersistentCookies = ... # type: 'QWebEngineProfile.PersistentCookiesPolicy'

    class HttpCacheType(int): ...
    MemoryHttpCache = ... # type: 'QWebEngineProfile.HttpCacheType'
    DiskHttpCache = ... # type: 'QWebEngineProfile.HttpCacheType'

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, name: str, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def removeAllUrlSchemeHandlers(self) -> None: ...
    def removeUrlSchemeHandler(self, a0: QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None: ...
    def removeUrlScheme(self, scheme: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def installUrlSchemeHandler(self, scheme: typing.Union[QtCore.QByteArray, bytes, bytearray], a1: QtWebEngineCore.QWebEngineUrlSchemeHandler) -> None: ...
    def urlSchemeHandler(self, a0: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> QtWebEngineCore.QWebEngineUrlSchemeHandler: ...
    def setRequestInterceptor(self, interceptor: QtWebEngineCore.QWebEngineUrlRequestInterceptor) -> None: ...
    def cookieStore(self) -> QtWebEngineCore.QWebEngineCookieStore: ...
    def httpAcceptLanguage(self) -> str: ...
    def setHttpAcceptLanguage(self, httpAcceptLanguage: str) -> None: ...
    def downloadRequested(self, download: QWebEngineDownloadItem) -> None: ...
    @staticmethod
    def defaultProfile() -> 'QWebEngineProfile': ...
    def scripts(self) -> 'QWebEngineScriptCollection': ...
    def settings(self) -> 'QWebEngineSettings': ...
    def visitedLinksContainsUrl(self, url: QtCore.QUrl) -> bool: ...
    def clearVisitedLinks(self, urls: typing.Iterable[QtCore.QUrl]) -> None: ...
    def clearAllVisitedLinks(self) -> None: ...
    def setHttpCacheMaximumSize(self, maxSize: int) -> None: ...
    def httpCacheMaximumSize(self) -> int: ...
    def setPersistentCookiesPolicy(self, a0: 'QWebEngineProfile.PersistentCookiesPolicy') -> None: ...
    def persistentCookiesPolicy(self) -> 'QWebEngineProfile.PersistentCookiesPolicy': ...
    def setHttpCacheType(self, a0: 'QWebEngineProfile.HttpCacheType') -> None: ...
    def httpCacheType(self) -> 'QWebEngineProfile.HttpCacheType': ...
    def setHttpUserAgent(self, userAgent: str) -> None: ...
    def httpUserAgent(self) -> str: ...
    def setCachePath(self, path: str) -> None: ...
    def cachePath(self) -> str: ...
    def setPersistentStoragePath(self, path: str) -> None: ...
    def persistentStoragePath(self) -> str: ...
    def isOffTheRecord(self) -> bool: ...
    def storageName(self) -> str: ...


class QWebEngineScript(sip.simplewrapper):

    class ScriptWorldId(int): ...
    MainWorld = ... # type: 'QWebEngineScript.ScriptWorldId'
    ApplicationWorld = ... # type: 'QWebEngineScript.ScriptWorldId'
    UserWorld = ... # type: 'QWebEngineScript.ScriptWorldId'

    class InjectionPoint(int): ...
    Deferred = ... # type: 'QWebEngineScript.InjectionPoint'
    DocumentReady = ... # type: 'QWebEngineScript.InjectionPoint'
    DocumentCreation = ... # type: 'QWebEngineScript.InjectionPoint'

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QWebEngineScript') -> None: ...

    def swap(self, other: 'QWebEngineScript') -> None: ...
    def setRunsOnSubFrames(self, on: bool) -> None: ...
    def runsOnSubFrames(self) -> bool: ...
    def setWorldId(self, a0: int) -> None: ...
    def worldId(self) -> int: ...
    def setInjectionPoint(self, a0: 'QWebEngineScript.InjectionPoint') -> None: ...
    def injectionPoint(self) -> 'QWebEngineScript.InjectionPoint': ...
    def setSourceCode(self, a0: str) -> None: ...
    def sourceCode(self) -> str: ...
    def setName(self, a0: str) -> None: ...
    def name(self) -> str: ...
    def isNull(self) -> bool: ...


class QWebEngineScriptCollection(sip.simplewrapper):

    def toList(self) -> typing.List[QWebEngineScript]: ...
    def clear(self) -> None: ...
    def remove(self, a0: QWebEngineScript) -> bool: ...
    @typing.overload
    def insert(self, a0: QWebEngineScript) -> None: ...
    @typing.overload
    def insert(self, list: typing.Iterable[QWebEngineScript]) -> None: ...
    def findScripts(self, name: str) -> typing.Any: ...
    def findScript(self, name: str) -> QWebEngineScript: ...
    def contains(self, value: QWebEngineScript) -> bool: ...
    def __len__(self) -> int: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...


class QWebEngineSettings(sip.simplewrapper):

    class FontSize(int): ...
    MinimumFontSize = ... # type: 'QWebEngineSettings.FontSize'
    MinimumLogicalFontSize = ... # type: 'QWebEngineSettings.FontSize'
    DefaultFontSize = ... # type: 'QWebEngineSettings.FontSize'
    DefaultFixedFontSize = ... # type: 'QWebEngineSettings.FontSize'

    class WebAttribute(int): ...
    AutoLoadImages = ... # type: 'QWebEngineSettings.WebAttribute'
    JavascriptEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    JavascriptCanOpenWindows = ... # type: 'QWebEngineSettings.WebAttribute'
    JavascriptCanAccessClipboard = ... # type: 'QWebEngineSettings.WebAttribute'
    LinksIncludedInFocusChain = ... # type: 'QWebEngineSettings.WebAttribute'
    LocalStorageEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    LocalContentCanAccessRemoteUrls = ... # type: 'QWebEngineSettings.WebAttribute'
    XSSAuditingEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    SpatialNavigationEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    LocalContentCanAccessFileUrls = ... # type: 'QWebEngineSettings.WebAttribute'
    HyperlinkAuditingEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    ScrollAnimatorEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    ErrorPageEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    PluginsEnabled = ... # type: 'QWebEngineSettings.WebAttribute'
    FullScreenSupportEnabled = ... # type: 'QWebEngineSettings.WebAttribute'

    class FontFamily(int): ...
    StandardFont = ... # type: 'QWebEngineSettings.FontFamily'
    FixedFont = ... # type: 'QWebEngineSettings.FontFamily'
    SerifFont = ... # type: 'QWebEngineSettings.FontFamily'
    SansSerifFont = ... # type: 'QWebEngineSettings.FontFamily'
    CursiveFont = ... # type: 'QWebEngineSettings.FontFamily'
    FantasyFont = ... # type: 'QWebEngineSettings.FontFamily'

    def defaultTextEncoding(self) -> str: ...
    def setDefaultTextEncoding(self, encoding: str) -> None: ...
    def resetAttribute(self, attr: 'QWebEngineSettings.WebAttribute') -> None: ...
    def testAttribute(self, attr: 'QWebEngineSettings.WebAttribute') -> bool: ...
    def setAttribute(self, attr: 'QWebEngineSettings.WebAttribute', on: bool) -> None: ...
    def resetFontSize(self, type: 'QWebEngineSettings.FontSize') -> None: ...
    def fontSize(self, type: 'QWebEngineSettings.FontSize') -> int: ...
    def setFontSize(self, type: 'QWebEngineSettings.FontSize', size: int) -> None: ...
    def resetFontFamily(self, which: 'QWebEngineSettings.FontFamily') -> None: ...
    def fontFamily(self, which: 'QWebEngineSettings.FontFamily') -> str: ...
    def setFontFamily(self, which: 'QWebEngineSettings.FontFamily', family: str) -> None: ...
    @staticmethod
    def globalSettings() -> 'QWebEngineSettings': ...
    @staticmethod
    def defaultSettings() -> 'QWebEngineSettings': ...


class QWebEngineView(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def hideEvent(self, a0: QtGui.QHideEvent) -> None: ...
    def showEvent(self, a0: QtGui.QShowEvent) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None: ...
    def createWindow(self, type: QWebEnginePage.WebWindowType) -> 'QWebEngineView': ...
    def renderProcessTerminated(self, terminationStatus: QWebEnginePage.RenderProcessTerminationStatus, exitCode: int) -> None: ...
    def iconUrlChanged(self, a0: QtCore.QUrl) -> None: ...
    def urlChanged(self, a0: QtCore.QUrl) -> None: ...
    def selectionChanged(self) -> None: ...
    def titleChanged(self, title: str) -> None: ...
    def loadFinished(self, a0: bool) -> None: ...
    def loadProgress(self, progress: int) -> None: ...
    def loadStarted(self) -> None: ...
    def reload(self) -> None: ...
    def forward(self) -> None: ...
    def back(self) -> None: ...
    def stop(self) -> None: ...
    def settings(self) -> QWebEngineSettings: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def findText(self, subString: str, options: QWebEnginePage.FindFlags = ..., resultCallback: typing.Optional[typing.Callable[..., None]] = ...) -> None: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def triggerPageAction(self, action: QWebEnginePage.WebAction, checked: bool = ...) -> None: ...
    def pageAction(self, action: QWebEnginePage.WebAction) -> QtWidgets.QAction: ...
    def selectedText(self) -> str: ...
    def hasSelection(self) -> bool: ...
    def iconUrl(self) -> QtCore.QUrl: ...
    def url(self) -> QtCore.QUrl: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def title(self) -> str: ...
    def history(self) -> QWebEngineHistory: ...
    def setContent(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray], mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    def load(self, url: QtCore.QUrl) -> None: ...
    def setPage(self, page: QWebEnginePage) -> None: ...
    def page(self) -> QWebEnginePage: ...