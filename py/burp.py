class IBurpExtender:
    def registerExtenderCallbacks(self, callbacks):
        pass


class IBurpExtenderCallbacks:
    TOOL_SUITE = 0x00000001
    TOOL_TARGET = 0x00000002
    TOOL_PROXY = 0x00000004
    TOOL_SPIDER = 0x00000008
    TOOL_SCANNER = 0x00000010
    TOOL_INTRUDER = 0x00000020
    TOOL_REPEATER = 0x00000040
    TOOL_SEQUENCER = 0x00000080
    TOOL_DECODER = 0x00000100
    TOOL_COMPARER = 0x00000200
    TOOL_EXTENDER = 0x00000400

    def setExtensionName(self, name):
        pass

    def getHelpers(self):
        pass

    def getStdout(self):
        pass

    def getStderr(self):
        pass

    def registerExtensionStateListener(self, listener):
        pass

    def registerHttpListener(self, listener):
        pass

    def registerProxyListener(self, listener):
        pass

    def registerScannerListener(self, listener):
        pass

    def registerScopeChangeListener(self, listener):
        pass

    def registerContextMenuFactory(self, factory):
        pass

    def registerMessageEditorTabFactory(self, factory):
        pass

    def registerScannerInsertionPointProvider(self, provider):
        pass

    def registerScannerCheck(self, check):
        pass

    def registerIntruderPayloadGeneratorFactory(self, factory):
        pass

    def registerIntruderPayloadProcessor(self, processor):
        pass

    def registerSessionHandlingAction(self, action):
        pass

    def unloadExtension(self):
        pass

    def addSuiteTab(self, tab):
        pass

    def removeSuiteTab(self, tab):
        pass

    def customizeUiComponent(self, component):
        pass

    def createMessageEditor(self, controller, editable):
        pass

    def getCommandLineArguments(self):
        pass

    def saveExtensionSetting(self, name, value):
        pass

    def loadExtensionSetting(self, name):
        pass

    def createTextEditor(self):
        pass

    def sendToRepeater(self, host, port, useHttps, request, tabCaption):
        pass

    def sendToIntruder(self, host, port, useHttps, request):
        pass

    def doActiveScan(self, host, port, useHttps, request):
        pass

    def doPassiveScan(self, host, port, useHttps, request, response):
        pass

    def makeHttpRequest(self, httpService, request):
        pass

    def makeHttpRequest(self, host, port, useHttps, request):
        pass

    def issueAlert(self, message):
        pass

    def getProxyHistory(self):
        pass

    def getSiteMap(self, urlPrefix):
        pass

    def getScanIssues(self, urlPrefix):
        pass

    def getCookieJarContents(self):
        pass

    def updateCookieJar(self, cookie):
        pass

    def addToSiteMap(self, item):
        pass

    def saveConfig(self):
        pass

    def setProxyInterceptionEnabled(self, enabled):
        pass

    def getBurpVersion(self):
        pass

    def exitSuite(self, promptUser):
        pass

    def saveToTempFile(self, buf):
        pass

    def saveBuffersToTempFiles(self, httpRequestResponse):
        pass

    def getToolName(self, toolFlag):
        pass

    def addScanIssue(self, issue):
        pass

    def getParameters(self, request):
        pass

    def getHeaders(self, message):
        pass

    def registerMenuItem(self, menuItemCaption, menuItemHandler):
        pass


class IContextMenuFactory:
    def createMenuItems(self, invocation):
        pass


class IContextMenuInvocation:
    CONTEXT_MESSAGE_EDITOR_REQUEST = 0
    CONTEXT_MESSAGE_EDITOR_RESPONSE = 1
    CONTEXT_MESSAGE_VIEWER_REQUEST = 2
    CONTEXT_MESSAGE_VIEWER_RESPONSE = 3
    CONTEXT_TARGET_SITE_MAP_TREE = 4
    CONTEXT_TARGET_SITE_MAP_TABLE = 5
    CONTEXT_PROXY_HISTORY = 6
    CONTEXT_SCANNER_RESULTS = 7
    CONTEXT_INTRUDER_PAYLOAD_POSITIONS = 8
    CONTEXT_INTRUDER_ATTACK_RESULTS = 9
    CONTEXT_SEARCH_RESULTS = 10

    def getInputEvent(self):
        pass

    def getToolFlag(self):
        pass

    def getInvocationContext(self):
        pass

    def getSelectionBounds(self):
        pass

    def getSelectedMessages(self):
        pass

    def getSelectedIssues(self):
        pass


class ICookie:
    def getDomain(self):
        pass

    def getExpiration(self):
        pass

    def getName(self):
        pass

    def getValue(self):
        pass


class IExtensionHelpers:
    def analyzeRequest(self, request):
        pass

    def analyzeRequest(self, httpService, request):
        pass

    def analyzeRequest(self, request):
        pass

    def analyzeResponse(self, response):
        pass

    def getRequestParameter(self, request, parameterName):
        pass

    def urlDecode(self, data):
        pass

    def urlEncode(self, data):
        pass

    def urlDecode(self, data):
        pass

    def urlEncode(self, data):
        pass

    def base64Decode(self, data):
        pass

    def base64Decode(self, data):
        pass

    def base64Encode(self, data):
        pass

    def base64Encode(self, data):
        pass

    def stringToBytes(self, data):
        pass

    def bytesToString(self, data):
        pass

    def indexOf(self, data, pattern, caseSensitive, frm, to):
        pass

    def buildHttpRequest(self, url):
        pass

    def addParameter(self, request, parameter):
        pass

    def removeParameter(self, request, parameter):
        pass

    def updateParameter(self, request, parameter):
        pass

    def toggleRequestMethod(self, request):
        pass

    def buildHttpService(self, host, port, protocol):
        pass

    def buildHttpService(self, host, port, useHttps):
        pass

    def buildParameter(self, name, value, typ):
        pass

    def makeScannerInsertionPoint(self, insertionPointName, baseRequest, frm, to):
        pass


class IExtensionStateListener:
    def extensionUnloaded(self):
        pass


class IHttpListener:
    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        pass


class IHttpRequestResponse:
    def getRequest(self):
        pass

    def setRequest(self, message):
        pass

    def getResponse(self):
        pass

    def setResponse(self, message):
        pass

    def getComment(self):
        pass

    def setComment(self, comment):
        pass

    def getHighlight(self):
        pass

    def setHighlight(self, color):
        pass

    def getHttpService(self):
        pass

    def setHttpService(self, httpService):
        pass


class IHttpRequestResponsePersisted:
    def deleteTempFiles(self):
        pass


class IHttpRequestResponseWithMarkers:
    def getRequestMarkers(self):
        pass

    def getResponseMarkers(self):
        pass


class IHttpService:
    def getHost(self):
        pass

    def getPort(self):
        pass

    def getProtocol(self):
        pass


class IInterceptedProxyMessage:
    ACTION_FOLLOW_RULES = 0
    ACTION_DO_INTERCEPT = 1
    ACTION_DONT_INTERCEPT = 2
    ACTION_DROP = 3
    ACTION_FOLLOW_RULES_AND_REHOOK = 0x10
    ACTION_DO_INTERCEPT_AND_REHOOK = 0x11
    ACTION_DONT_INTERCEPT_AND_REHOOK = 0x12

    def getMessageReference(self):
        pass

    def getMessageInfo(self):
        pass

    def getInterceptAction(self):
        pass

    def setInterceptAction(self, interceptAction):
        pass

    def getListenerInterface(self):
        pass

    def getClientIpAddress(self):
        pass


class IIntruderAttack:
    def getHttpService(self):
        pass

    def getRequestTemplate(self):
        pass


class IIntruderPayloadGenerator:
    def hasMorePayloads(self):
        pass

    def getNextPayload(self, baseValue):
        pass

    def reset(self):
        pass


class IIntruderPayloadGeneratorFactory:
    def getGeneratorName(self):
        pass

    def createNewInstance(self, attack):
        pass


class IIntruderPayloadProcessor:
    def getProcessorName(self):
        pass

    def processPayload(self, currentPayload, originalPayload, baseValue):
        pass


class IMenuItemHandler:
    def message(self, s):
        pass

    def menuItemClicked(self, menuItemCaption, messageInfo):
        pass


class IMessageEditor:
    def getComponent(self):
        pass

    def setMessage(self, message, isRequest):
        pass

    def getMessage(self):
        pass

    def isMessageModified(self):
        pass

    def getSelectedData(self):
        pass


class IMessageEditorController:
    def getHttpService(self):
        pass

    def getRequest(self):
        pass

    def getResponse(self):
        pass


class IMessageEditorTab:
    def getTabCaption(self):
        pass

    def getUiComponent(self):
        pass

    def isEnabled(self, content, isRequest):
        pass

    def setMessage(self, content, isRequest):
        pass

    def getMessage(self):
        pass

    def isModified(self):
        pass

    def getSelectedData(self):
        pass


class IMessageEditorTabFactory:
    def createNewInstance(self, controller, editable):
        pass


class IParameter:
    PARAM_URL = 0
    PARAM_BODY = 1
    PARAM_COOKIE = 2
    PARAM_XML = 3
    PARAM_XML_ATTR = 4
    PARAM_MULTIPART_ATTR = 5
    PARAM_JSON = 6

    def getType(self):
        pass

    def getName(self):
        pass

    def getValue(self):
        pass

    def getNameStart(self):
        pass

    def getNameEnd(self):
        pass

    def getValueStart(self):
        pass

    def getValueEnd(self):
        pass


class IProxyListener:
    def processProxyMessage(self, messageIsRequest, message):
        pass


class IRequestInfo:
    CONTENT_TYPE_NONE = 0
    CONTENT_TYPE_URL_ENCODED = 1
    CONTENT_TYPE_MULTIPART = 2
    CONTENT_TYPE_XML = 3
    CONTENT_TYPE_JSON = 4
    CONTENT_TYPE_AMF = 5

    def getMethod(self):
        pass

    def getUrl(self):
        pass

    def getHeaders(self):
        pass

    def getParameters(self):
        pass

    def getBodyOffset(self):
        pass

    def getContentType(self):
        pass


class IResponseInfo:
    def getHeaders(self):
        pass

    def getBodyOffset(self):
        pass

    def getStatusCode(self):
        pass

    def getCookies(self):
        pass

    def getStatedMimeType(self):
        pass

    def getInferredMimeType(self):
        pass


class IScanIssue:
    def getIssueName(self):
        pass

    def getIssueType(self):
        pass

    def getSeverity(self):
        pass

    def getConfidence(self):
        pass

    def getIssueBackground(self):
        pass

    def getRemediationBackground(self):
        pass

    def getIssueDetail(self):
        pass

    def getRemediationDetail(self):
        pass

    def getHttpMessages(self):
        pass

    def getHttpService(self):
        pass


class IScannerCheck:
    def doPassiveScan(self, baseRequestResponse):
        pass

    def doActiveScan(self, baseRequestResponse, insertionPoint):
        pass

    def issue(self, s):
        pass

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        pass


class IScannerInsertionPoint:
    INS_PARAM_URL = 0x00
    INS_PARAM_BODY = 0x01
    INS_PARAM_COOKIE = 0x02
    INS_PARAM_XML = 0x03
    INS_PARAM_XML_ATTR = 0x04
    INS_PARAM_MULTIPART_ATTR = 0x05
    INS_PARAM_JSON = 0x06
    INS_PARAM_AMF = 0x07
    INS_HEADER = 0x20
    INS_URL_REST = 0x21
    INS_PARAM_NAME_URL = 0x22
    INS_PARAM_NAME_BODY = 0x23
    INS_USER_PROVIDED = 0x40
    INS_EXTENSION_PROVIDED = 0x41
    INS_UNKNOWN = 0x7f

    def getInsertionPointName(self):
        pass

    def getBaseValue(self):
        pass

    def buildRequest(self, payload):
        pass

    def getPayloadOffsets(self, payload):
        pass

    def getInsertionPointType(self):
        pass


class IScannerInsertionPointProvider:
    def getInsertionPoints(self, baseRequestResponse):
        pass


class IScannerListener:
    def newScanIssue(self, issue):
        pass


class IScanQueueItem:
    def getStatus(self):
        pass

    def getPercentageComplete(self):
        pass

    def getNumRequests(self):
        pass

    def getNumErrors(self):
        pass

    def getNumInsertionPoints(self):
        pass

    def cancel(self):
        pass

    def getIssues(self):
        pass


class IScopeChangeListener:
    def scopeChanged(self):
        pass


class ISessionHandlingAction:
    def getActionName(self):
        pass

    def performAction(self, currentRequest, macroItems):
        pass


class ITab:
    def getTabCaption(self):
        pass

    def getUiComponent(self):
        pass


class ITempFile:
    def getBuffer(self):
        pass

    def delete(self):
        pass


class ITextEditor:
    def getComponent(self):
        pass

    def setEditable(self, editable):
        pass

    def setText(self, text):
        pass

    def getText(self):
        pass

    def isTextModified(self):
        pass

    def getSelectedText(self):
        pass

    def getSelectionBounds(self):
        pass

    def setSearchExpression(self, expression):
        pass