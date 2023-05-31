Error: MonitoredItemCreateRequest.__init__() got an unexpected keyword argument 'client_handle'
ServiceFault from server received while waiting for publish response
exception calling callback for <Future at 0x1c449e21750 state=finished returned Buffer>
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\concurrent\futures\_base.py", line 342, in _invoke_callbacks
    callback(self)
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\ua_client.py", line 493, in _call_publish_callback
    self._uasocket.check_answer(data, "while waiting for publish response")
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\client\ua_client.py", line 93, in check_answer
    hdr.ServiceResult.check()
  File "C:\Users\40020507\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\opcua\ua\uatypes.py", line 218, in check
    raise UaStatusCodeError(self.value)
opcua.ua.uaerrors._auto.BadSessionClosed: "The session was closed by the client."(BadSessionClosed)
ServiceFault from server received while waiting for publish response
Client disconnected
