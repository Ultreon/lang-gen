from __future__ import annotations
from overload import overload


 
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import java.io.OutputStream as OutputStream
from builtins import bool
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream as _AlternateDataStream
_AlternateDataStream = _AlternateDataStream
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AlternateDataStream():
    """dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream"""
 
    @staticmethod
    def _wrap(java_value: _AlternateDataStream) -> 'AlternateDataStream':
        return AlternateDataStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlternateDataStream):
        """
        Dynamic initializer for AlternateDataStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlternateDataStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlternateDataStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def file(self) -> 'File':
        """public java.io.File dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.file()"""
        return 'File'._wrap(super(AlternateDataStream, self).file())

    @overload
    def openOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openOutputStream() throws java.io.FileNotFoundException"""
        return 'OutputStream'._wrap(super(AlternateDataStream, self).openOutputStream())

    @overload
    def openInputStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openInputStream() throws java.io.FileNotFoundException"""
        return 'InputStream'._wrap(super(AlternateDataStream, self).openInputStream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.hashCode()"""
        return int._wrap(super(AlternateDataStream, self).hashCode())

    @overload
    def openReader(self) -> 'Reader':
        """public java.io.Reader dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openReader() throws java.io.FileNotFoundException"""
        return 'Reader'._wrap(super(AlternateDataStream, self).openReader())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toString()"""
        return str._wrap(super(AlternateDataStream, self).toString())

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.getPath()"""
        return str._wrap(super(AlternateDataStream, self).getPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.equals(java.lang.Object)"""
        return bool._wrap(super(_AlternateDataStream, self).equals(arg0))

    @overload
    def openWriter(self) -> 'Writer':
        """public java.io.Writer dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openWriter() throws java.io.IOException"""
        return 'Writer'._wrap(super(AlternateDataStream, self).openWriter())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toPath()"""
        return 'Path'._wrap(super(AlternateDataStream, self).toPath())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.id()"""
        return str._wrap(super(AlternateDataStream, self).id())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'File', arg1: str):
        """public dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream(java.io.File,java.lang.String)"""
        val = _AlternateDataStream(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import java.nio.file.Path as _Path
_Path = _Path
import java.lang.String as _string
import java.io.OutputStream as OutputStream
from builtins import bool
from builtins import str
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream as _AlternateDataStream
_AlternateDataStream = _AlternateDataStream
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AlternateDataStream():
    """dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream"""
 
    @staticmethod
    def _wrap(java_value: _AlternateDataStream) -> 'AlternateDataStream':
        return AlternateDataStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlternateDataStream):
        """
        Dynamic initializer for AlternateDataStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlternateDataStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlternateDataStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def file(self) -> 'File':
        """public java.io.File dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.file()"""
        return 'File'._wrap(super(AlternateDataStream, self).file())

    @overload
    def openOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openOutputStream() throws java.io.FileNotFoundException"""
        return 'OutputStream'._wrap(super(AlternateDataStream, self).openOutputStream())

    @overload
    def openInputStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openInputStream() throws java.io.FileNotFoundException"""
        return 'InputStream'._wrap(super(AlternateDataStream, self).openInputStream())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.hashCode()"""
        return int._wrap(super(AlternateDataStream, self).hashCode())

    @overload
    def openReader(self) -> 'Reader':
        """public java.io.Reader dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openReader() throws java.io.FileNotFoundException"""
        return 'Reader'._wrap(super(AlternateDataStream, self).openReader())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toString()"""
        return str._wrap(super(AlternateDataStream, self).toString())

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.getPath()"""
        return str._wrap(super(AlternateDataStream, self).getPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.equals(java.lang.Object)"""
        return bool._wrap(super(_AlternateDataStream, self).equals(arg0))

    @overload
    def openWriter(self) -> 'Writer':
        """public java.io.Writer dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openWriter() throws java.io.IOException"""
        return 'Writer'._wrap(super(AlternateDataStream, self).openWriter())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def toPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toPath()"""
        return 'Path'._wrap(super(AlternateDataStream, self).toPath())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.id()"""
        return str._wrap(super(AlternateDataStream, self).id())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'File', arg1: str):
        """public dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream(java.io.File,java.lang.String)"""
        val = _AlternateDataStream(arg0, arg1)
        self.__wrapper = val

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream