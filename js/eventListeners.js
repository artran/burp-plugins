importClass(java.io.PrintWriter);

importClass(Packages.burp.IHttpListener);
importClass(Packages.burp.IProxyListener);
importClass(Packages.burp.IScannerListener);
importClass(Packages.burp.IExtensionStateListener);

var privateApi = {};

// Implement IHttpListener
var httpListener = {
    processHttpMessage: function(toolFlag, messageIsRequest, messageInfo){
        var stdout = privateApi.stdout,
            callbacks = privateApi.callbacks,
            prefix = messageIsRequest ? "HTTP request to " : "HTTP response from ";

        stdout.println(prefix + messageInfo.getHttpService() +
            " [" + callbacks.getToolName(toolFlag) + "]");
    }
};

// Implement IProxyListener
var proxyListener = {
    processProxyMessage: function(messageIsRequest, message){
        var stdout = privateApi.stdout,
            prefix = messageIsRequest ? "Proxy request to " : "Proxy response from ";

        stdout.println(prefix + message.getMessageInfo().getHttpService());
    }
};

// Implement IScannerListener
var scannerListener = {
    newScanIssue: function(issue){
        privateApi.stdout.println("New scan issue: " + issue.getIssueName());
    }
};

// Implement IExtensionStateListener
var extensionStateListener = {
    extensionUnloaded: function(){
        privateApi.stdout.println("EventListener extension was unloaded");
    }
};

// Implement IBurpExtender & register listeners
var registerExtenderCallbacks = function(callbacks) {
    callbacks.setExtensionName("Event listeners");

    privateApi.callbacks = callbacks;
    privateApi.stdout = PrintWriter(callbacks.getStdout(), true);
    privateApi.stderr = PrintWriter(callbacks.getStderr(), true);

    callbacks.registerHttpListener(new IHttpListener(httpListener))
    callbacks.registerProxyListener(new IProxyListener(proxyListener))
    callbacks.registerScannerListener(new IScannerListener(scannerListener))
    callbacks.registerExtensionStateListener(new IExtensionStateListener(extensionStateListener))
};