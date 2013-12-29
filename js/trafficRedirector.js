importClass(Packages.burp.IHttpListener);

var privateApi = {
    hostFrom: "host1.example.org",
    hostTo: "host2.example.org"
};

// Implement IHttpListener
var httpListener = {
    processHttpMessage: function(toolFlag, messageIsRequest, messageInfo){
        var helpers = privateApi.helpers,
            httpService = messageInfo.getHttpService(),
            newHttpService;

        if (messageIsRequest && httpService.getHost().equals(privateApi.hostFrom)){
            newHttpService = helpers.buildHttpService(privateApi.hostTo, httpService.getPort(), httpService.getProtocol());
            messageInfo.setHttpService(newHttpService);
        }
    }
};

// Implement IBurpExtender & register listener
var registerExtenderCallbacks = function(callbacks) {
    callbacks.setExtensionName("Traffic redirector");

    privateApi.helpers = callbacks.getHelpers();

    callbacks.registerHttpListener(new IHttpListener(httpListener))
};