from py4j.clientserver import ClientServer, JavaParameters, PythonParameters


class EclipseAction(object):
    """Simple implementation of an EclipseRunnable that opens
    a MessageDialog in the current thread. It must thus be 
    called from a UI thread.
    """

    def __init__(self, clientserver):
        self.clientserver = clientserver

    def run(self, viewer):
        self.clientserver.jvm.org.eclipse.jface.dialogs.MessageDialog.openInformation(viewer.getControl().getShell(), "Sample View", "HELLO FROM PYTHON")

    class Java:
        implements = ["org.py4j.plugin_example.EclipseRunnable"]


action = EclipseAction(None)

clientServer = ClientServer(JavaParameters(), PythonParameters(), action)

# Small hack so that action can call Java
action.clientserver = clientServer

# For now, just kill the script once Eclipse has shutdown.