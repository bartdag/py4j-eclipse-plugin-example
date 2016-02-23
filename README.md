Py4J Eclipse Example
====================

This is a small eclipse plug-in that starts a Py4J Client Server and that
calls the Python side when you click on "Action 1" on an item in "Sample
View".

The Python code then calls Java to open a MessageDialog.

This works because the call is initiated from the UI thread and the threading
model implemented by ClientServer ensures that calls are executed in the same
thread on both sides.

The Python code is in python\_code.py and must be executed before the Java
code is started. This is another novelty of ClientServer: the Java side can
drive the Python side.
