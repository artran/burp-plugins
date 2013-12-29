importClass(java.io.PrintWriter);
importClass(java.lang.RuntimeException);

var stdout, stderr;

var registerExtenderCallbacks = function(callbacks) {
    callbacks.setExtensionName("Hello world extension");

    // Set up output and error streams
    stdout = PrintWriter(callbacks.getStdout(), true);
    stderr = PrintWriter(callbacks.getStderr(), true);

    // Print messages to the output and error tabs for this extension
    stdout.println("Hello output");
    stderr.println("Hello errors");

    // Write a message to the Burp alerts tab
    callbacks.issueAlert("Hello alerts");

    // Throw an exception that will appear in the error tab for this extension
    throw RuntimeException("Hello exception");
}
