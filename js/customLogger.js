importClass(java.awt.Component);
importClass(java.io.PrintWriter);
importClass(java.lang.Class);
importClass(java.util.ArrayList);
importClass(javax.swing.JScrollPane);
importClass(javax.swing.JSplitPane);
importClass(javax.swing.JTabbedPane);
importClass(javax.swing.JTable);
importClass(javax.swing.SwingUtilities);
importClass(javax.swing.event.TableModelEvent);
importClass(javax.swing.table.TableModel);
importClass(javax.swing.SwingUtilities);

importClass(Packages.burp.IHttpListener);
importClass(Packages.burp.ITab);
importClass(Packages.burp.IMessageEditorController);

var privateApi = {
    callbacks: null,
    helpers: null,
    stdout: null,
    log: null,
    splitPane: null,
    logTable: null,
    currentlyDisplayedItem: null
};

// Implement ITab
var iTab = {
    getTabCaption: function(){
        return "Logger";
    },

    getUiComponent: function(){
        return privateApi.splitPane;
    }
};

// Implement iHttpListener
var httpListener = {
    processHttpMessage: function(toolFlag, messageIsRequest, messageInfo){
        if (!messageIsRequest){
            var tableModelEvent = new TableModelEvent(privateApi.logTable.getModel(), privateApi.log.size(), privateApi.log.size(), TableModelEvent.ALL_COLUMNS, TableModelEvent.INSERT),
                logEntry = {
                    tool: toolFlag,
                    requestResponse: privateApi.callbacks.saveBuffersToTempFiles(messageInfo),
                    url: privateApi.helpers.analyzeRequest(messageInfo).getUrl()
                };
//            privateApi.stdout.println("log entry: " + logEntry.tool + ", " + logEntry.url.toString());
            privateApi.log.add(logEntry);
            privateApi.stdout.println("Size is now " + privateApi.log.size());

            privateApi.logTable.tableChanged(tableModelEvent);
//            SwingUtilities.invokeLater(new Runnable({
//                run: function(){
//                    privateApi.stdout.println("Fire event");
//                }
//            }));
        }
    }
};

// implement IMessageEditorController
// this allows our request/response viewers to obtain details about the messages being displayed
var iMessageEditorController = {
    getHttpService: function(){
        return privateApi.currentlyDisplayedItem.getHttpService();
    },

    getRequest: function(){
        return privateApi.currentlyDisplayedItem.getRequest();
    },

    getResponse: function(){
        return privateApi.currentlyDisplayedItem.getResponse();
    }
};

var tableModelImpl = {
    getRowCount: function(){
        privateApi.stdout.println("getSize = " + privateApi.log.size());
        return privateApi.log.size();
    },

    getColumnCount: function () {
        return 2;
    },

    getColumnName: function(columnIndex){
        if (columnIndex === 0){
            return "Tool";
        } else if (columnIndex === 1){
            return "URL";
        } else {
            return "";
        }
    },

    setValueAt: function(aValue, rowIndex, columnIndex){
        privateApi.stdout.println("Add " + aValue);
    },

    getValueAt: function(rowIndex, columnIndex){
        privateApi.stdout.println("getValueAt " + rowIndex + ", " + columnIndex);
        return "asdf";
//        var logEntry = privateApi.log.get(rowIndex);
//        if (columnIndex === 0){
//            privateApi.stdout.println("col 0");
//            return "xxxxx";//privateApi.callbacks.getToolName(logEntry.tool);
//        } else if (columnIndex === 1){
//            privateApi.stdout.println("col 1");
//            return logEntry.url.toString();
//        } else {
//            privateApi.stdout.println("woops");
//            return "";
//        }
    },

    addTableModelListener: function(newListener){
        privateApi.stdout.println("add listener " + newListener);
    },
    removeTableModelListener: function(listener){},

    getColumnClass: function(columnIndex){
    },

    isCellEditable: function(rowIndex, columnIndex){
        privateApi.stdout.println("isEditable");
        return false;
    }
};

// Implement IBurpExtender
var registerExtenderCallbacks = function(callbacks) {
    callbacks.setExtensionName("Custom logger");

    privateApi.callbacks = callbacks;
    privateApi.helpers = callbacks.getHelpers();
    privateApi.stdout = PrintWriter(callbacks.getStdout(), true);

    privateApi.log = new ArrayList();
    privateApi.splitPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT);

    var tabs = new JTabbedPane(),
        messageEditorController = new IMessageEditorController(iMessageEditorController),
        requestViewer = callbacks.createMessageEditor(messageEditorController, false),
        responseViewer = callbacks.createMessageEditor(messageEditorController, false);

    tabs.addTab("Request", requestViewer.getComponent());
    tabs.addTab("Response", responseViewer.getComponent());
    privateApi.splitPane.setRightComponent(tabs);

    privateApi.log.add({tool: 4, url: "blah"});
    var tableModel = new TableModel(tableModelImpl);
    privateApi.logTable = new JTable(tableModel);
    var scrollPane = new JScrollPane(privateApi.logTable);
    privateApi.splitPane.setLeftComponent(scrollPane);

    callbacks.customizeUiComponent(privateApi.splitPane);
    callbacks.customizeUiComponent(privateApi.logTable);
    callbacks.customizeUiComponent(scrollPane);
    callbacks.customizeUiComponent(tabs);

    callbacks.addSuiteTab(new ITab(iTab));
    callbacks.registerHttpListener(new IHttpListener(httpListener))
};