from __future__ import annotations
from overload import overload


 
import java.nio.file.Path as __Path
__Path = __Path
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.io.File as File
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream as __AlternateDataStream
__AlternateDataStream = __AlternateDataStream
import java.io.File as __File
__File = __File
import java.io.OutputStream as OutputStream
import java.lang.String as __string
from builtins import bool
from builtins import str
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as Path
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.Reader as __Reader
__Reader = __Reader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class AlternateDataStream():
    """dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream"""
 
    @staticmethod
    def __wrap(java_value: __AlternateDataStream) -> 'AlternateDataStream':
        return AlternateDataStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlternateDataStream):
        """
        Dynamic initializer for AlternateDataStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.id()"""
        return str.__wrap(super(AlternateDataStream, self).id())

    @overload
    def toPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toPath()"""
        return 'Path'.__wrap(super(AlternateDataStream, self).toPath())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.getPath()"""
        return str.__wrap(super(AlternateDataStream, self).getPath())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.equals(java.lang.Object)"""
        return bool.__wrap(super(__AlternateDataStream, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toString()"""
        return str.__wrap(super(AlternateDataStream, self).toString())

    @overload
    def file(self) -> 'File':
        """public java.io.File dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.file()"""
        return 'File'.__wrap(super(AlternateDataStream, self).file())

    @overload
    def openOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openOutputStream() throws java.io.FileNotFoundException"""
        return 'OutputStream'.__wrap(super(AlternateDataStream, self).openOutputStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'File', arg1: str):
        """public dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream(java.io.File,java.lang.String)"""
        val = __AlternateDataStream(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.hashCode()"""
        return int.__wrap(super(AlternateDataStream, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def openWriter(self) -> 'Writer':
        """public java.io.Writer dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openWriter() throws java.io.IOException"""
        return 'Writer'.__wrap(super(AlternateDataStream, self).openWriter())

    @overload
    def openReader(self) -> 'Reader':
        """public java.io.Reader dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openReader() throws java.io.FileNotFoundException"""
        return 'Reader'.__wrap(super(AlternateDataStream, self).openReader())

    @overload
    def openInputStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openInputStream() throws java.io.FileNotFoundException"""
        return 'InputStream'.__wrap(super(AlternateDataStream, self).openInputStream())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream
import java.nio.file.Path as __Path
__Path = __Path
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.io.File as File
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream as __AlternateDataStream
__AlternateDataStream = __AlternateDataStream
import java.io.File as __File
__File = __File
import java.io.OutputStream as OutputStream
import java.lang.String as __string
from builtins import bool
from builtins import str
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as Path
import java.io.InputStream as __InputStream
__InputStream = __InputStream
import java.io.Reader as __Reader
__Reader = __Reader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class AlternateDataStream():
    """dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream"""
 
    @staticmethod
    def __wrap(java_value: __AlternateDataStream) -> 'AlternateDataStream':
        return AlternateDataStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlternateDataStream):
        """
        Dynamic initializer for AlternateDataStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.id()"""
        return str.__wrap(super(AlternateDataStream, self).id())

    @overload
    def toPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toPath()"""
        return 'Path'.__wrap(super(AlternateDataStream, self).toPath())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getPath(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.getPath()"""
        return str.__wrap(super(AlternateDataStream, self).getPath())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.equals(java.lang.Object)"""
        return bool.__wrap(super(__AlternateDataStream, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.toString()"""
        return str.__wrap(super(AlternateDataStream, self).toString())

    @overload
    def file(self) -> 'File':
        """public java.io.File dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.file()"""
        return 'File'.__wrap(super(AlternateDataStream, self).file())

    @overload
    def openOutputStream(self) -> 'OutputStream':
        """public java.io.OutputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openOutputStream() throws java.io.FileNotFoundException"""
        return 'OutputStream'.__wrap(super(AlternateDataStream, self).openOutputStream())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'File', arg1: str):
        """public dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream(java.io.File,java.lang.String)"""
        val = __AlternateDataStream(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.hashCode()"""
        return int.__wrap(super(AlternateDataStream, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def openWriter(self) -> 'Writer':
        """public java.io.Writer dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openWriter() throws java.io.IOException"""
        return 'Writer'.__wrap(super(AlternateDataStream, self).openWriter())

    @overload
    def openReader(self) -> 'Reader':
        """public java.io.Reader dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openReader() throws java.io.FileNotFoundException"""
        return 'Reader'.__wrap(super(AlternateDataStream, self).openReader())

    @overload
    def openInputStream(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream.openInputStream() throws java.io.FileNotFoundException"""
        return 'InputStream'.__wrap(super(AlternateDataStream, self).openInputStream())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.platform.win32.AlternateDataStream