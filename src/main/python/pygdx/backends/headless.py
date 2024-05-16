from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
import com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration as __HeadlessApplicationConfiguration
__HeadlessApplicationConfiguration = __HeadlessApplicationConfiguration
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessApplicationConfiguration():
    """com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessApplicationConfiguration) -> 'HeadlessApplicationConfiguration':
        return HeadlessApplicationConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessApplicationConfiguration):
        """
        Dynamic initializer for HeadlessApplicationConfiguration.
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
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = __HeadlessApplicationConfiguration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = __HeadlessApplicationConfiguration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration
from builtins import str
import java.lang.Long as __long
import com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration as __HeadlessApplicationConfiguration
__HeadlessApplicationConfiguration = __HeadlessApplicationConfiguration
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessApplicationConfiguration():
    """com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessApplicationConfiguration) -> 'HeadlessApplicationConfiguration':
        return HeadlessApplicationConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessApplicationConfiguration):
        """
        Dynamic initializer for HeadlessApplicationConfiguration.
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
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = __HeadlessApplicationConfiguration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = __HeadlessApplicationConfiguration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessNativesLoader
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.backends.headless.HeadlessNativesLoader as __HeadlessNativesLoader
__HeadlessNativesLoader = __HeadlessNativesLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessNativesLoader():
    """com.badlogic.gdx.backends.headless.HeadlessNativesLoader"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessNativesLoader) -> 'HeadlessNativesLoader':
        return HeadlessNativesLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessNativesLoader):
        """
        Dynamic initializer for HeadlessNativesLoader.
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
 
    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

        @staticmethod
        @overload
        def load():
            """public static void com.badlogic.gdx.backends.headless.HeadlessNativesLoader.load()"""
            __HeadlessNativesLoader.load()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessNativesLoader()"""
        val = __HeadlessNativesLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessNativesLoader()"""
        val = __HeadlessNativesLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplicationLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.backends.headless.HeadlessApplicationLogger as __HeadlessApplicationLogger
__HeadlessApplicationLogger = __HeadlessApplicationLogger
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessApplicationLogger():
    """com.badlogic.gdx.backends.headless.HeadlessApplicationLogger"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessApplicationLogger) -> 'HeadlessApplicationLogger':
        return HeadlessApplicationLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessApplicationLogger):
        """
        Dynamic initializer for HeadlessApplicationLogger.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplicationLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationLogger()"""
        val = __HeadlessApplicationLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplicationLogger, self).log(arg0, arg1, arg2)

    @override
    @overload
    def log(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.log(java.lang.String,java.lang.String)"""
        super(__HeadlessApplicationLogger, self).log(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.debug(java.lang.String,java.lang.String)"""
        super(__HeadlessApplicationLogger, self).debug(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationLogger()"""
        val = __HeadlessApplicationLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplicationLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.error(java.lang.String,java.lang.String)"""
        super(__HeadlessApplicationLogger, self).error(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessFileHandle
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.io.File as File
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.io.BufferedReader as __BufferedReader
__BufferedReader = __BufferedReader
import java.lang.Class as __Class
__Class = __Class
import java.io.File as __File
__File = __File
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.io.FilenameFilter as FilenameFilter
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import java.io.BufferedInputStream as __BufferedInputStream
__BufferedInputStream = __BufferedInputStream
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.FileFilter as FileFilter
import com.badlogic.gdx.backends.headless.HeadlessFileHandle as __HeadlessFileHandle
__HeadlessFileHandle = __HeadlessFileHandle
import com.badlogic.gdx.Files as __Files_FileType
__FileType = __Files_FileType.FileType
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class HeadlessFileHandle():
    """com.badlogic.gdx.backends.headless.HeadlessFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessFileHandle) -> 'HeadlessFileHandle':
        return HeadlessFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessFileHandle):
        """
        Dynamic initializer for HeadlessFileHandle.
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
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'.__wrap(super(__files.FileHandle, self).writer(__boolean.valueOf(arg0)))

    @overload
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.child(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFileHandle, self).child(arg0))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__files.FileHandle, self).read(__int.valueOf(arg0)))

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandle.read()"""
        return 'InputStream'.__wrap(super(files.FileHandle, self).read())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.isDirectory()"""
        return bool.__wrap(super(files.FileHandle, self).isDirectory())

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.deleteDirectory()"""
        return bool.__wrap(super(files.FileHandle, self).deleteDirectory())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(__files.FileHandle, self).moveTo(arg0)

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str.__wrap(super(files.FileHandle, self).readString())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'.__wrap(super(files.FileHandle, self).type())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(__files.FileHandle, self).writeString(arg0, __boolean.valueOf(arg1))

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'.__wrap(super(__files.FileHandle, self).map(arg0))

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'.__wrap(super(__files.FileHandle, self).reader(arg0))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str.__wrap(super(files.FileHandle, self).extension())

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean)"""
        return 'OutputStream'.__wrap(super(__files.FileHandle, self).write(__boolean.valueOf(arg0)))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'.__wrap(super(__files.FileHandle, self).reader(__int.valueOf(arg0)))

    @overload
    def list(self, arg0: str) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(files.FileHandle, self).hashCode())

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(__files.FileHandle, self).writeString(arg0, __boolean.valueOf(arg1), arg2)

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory(boolean)"""
        super(__files.FileHandle, self).emptyDirectory(__boolean.valueOf(arg0))

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'.__wrap(super(__files.FileHandle, self).writer(__boolean.valueOf(arg0), arg1))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int.__wrap(super(__files.FileHandle, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'.__wrap(super(__files.FileHandle, self).reader(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return files.FileHandle.__wrap(__FileHandle.tempFile(arg0))

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandle.mkdirs()"""
        super(files.FileHandle, self).mkdirs()

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory()"""
        super(files.FileHandle, self).emptyDirectory()

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(__files.FileHandle, self).write(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int.__wrap(super(files.FileHandle, self).lastModified())

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str.__wrap(super(files.FileHandle, self).name())

    @overload
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFileHandle, self).sibling(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(__files.FileHandle, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool.__wrap(super(files.FileHandle, self).delete())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__files.FileHandle, self).readString(arg0))

    @overload
    def __init__(self, arg0: 'File', arg1: 'FileType'):
        """public com.badlogic.gdx.backends.headless.HeadlessFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        val = __HeadlessFileHandle(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(files.FileHandle, self).readBytes())

    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.parent()"""
        return 'files.FileHandle'.__wrap(super(HeadlessFileHandle, self).parent())

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return files.FileHandle.__wrap(__FileHandle.tempDirectory(arg0))

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'.__wrap(super(files.FileHandle, self).map())

    @overload
    def __init__(self, arg0: str, arg1: 'FileType'):
        """public com.badlogic.gdx.backends.headless.HeadlessFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        val = __HeadlessFileHandle(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.length()"""
        return int.__wrap(super(files.FileHandle, self).length())

    @overload
    def list(self, arg0: 'FileFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'.__wrap(super(__files.FileHandle, self).write(__boolean.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def list(self) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list()"""
        return List['files.FileHandle'].__wrap(super(files.FileHandle, self).list())

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.backends.headless.HeadlessFileHandle.file()"""
        return 'File'.__wrap(super(HeadlessFileHandle, self).file())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str.__wrap(super(files.FileHandle, self).toString())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__files.FileHandle, self).equals(arg0))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(__files.FileHandle, self).writeBytes(bytes, __boolean.valueOf(arg1))

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'.__wrap(super(files.FileHandle, self).reader())

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str.__wrap(super(files.FileHandle, self).path())

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.exists()"""
        return bool.__wrap(super(files.FileHandle, self).exists())

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__files.FileHandle, self).copyTo(arg0) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessNet
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import net
except ImportError:
    net = __import_once__("pygdx.net")

import com.badlogic.gdx.net.Socket as __Socket
__Socket = __Socket
import com.badlogic.gdx.net.ServerSocket as __ServerSocket
__ServerSocket = __ServerSocket
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.backends.headless.HeadlessNet as __HeadlessNet
__HeadlessNet = __HeadlessNet
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessNet():
    """com.badlogic.gdx.backends.headless.HeadlessNet"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessNet) -> 'HeadlessNet':
        return HeadlessNet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessNet):
        """
        Dynamic initializer for HeadlessNet.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newServerSocket(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints') -> 'net.ServerSocket':
        """public com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.backends.headless.HeadlessNet.newServerSocket(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        return 'net.ServerSocket'.__wrap(super(__HeadlessNet, self).newServerSocket(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def newServerSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints') -> 'net.ServerSocket':
        """public com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.backends.headless.HeadlessNet.newServerSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        return 'net.ServerSocket'.__wrap(super(__HeadlessNet, self).newServerSocket(arg0, arg1, __int.valueOf(arg2), arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newClientSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints') -> 'net.Socket':
        """public com.badlogic.gdx.net.Socket com.badlogic.gdx.backends.headless.HeadlessNet.newClientSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        return 'net.Socket'.__wrap(super(__HeadlessNet, self).newClientSocket(arg0, arg1, __int.valueOf(arg2), arg3))

    @overload
    def openURI(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessNet.openURI(java.lang.String)"""
        return bool.__wrap(super(__HeadlessNet, self).openURI(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessNet.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        super(__HeadlessNet, self).sendHttpRequest(arg0, arg1)

    @override
    @overload
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public void com.badlogic.gdx.backends.headless.HeadlessNet.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        super(__HeadlessNet, self).cancelHttpRequest(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'HeadlessApplicationConfiguration'):
        """public com.badlogic.gdx.backends.headless.HeadlessNet(com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration)"""
        val = __HeadlessNet(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplication
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.Files as __Files
__Files = __Files
from builtins import type
import com.badlogic.gdx.Input as __Input
__Input = __Input
import com.badlogic.gdx.ApplicationLogger as __ApplicationLogger
__ApplicationLogger = __ApplicationLogger
import com.badlogic.gdx.Net as __Net
__Net = __Net
import com.badlogic.gdx.backends.headless.HeadlessApplication as __HeadlessApplication
__HeadlessApplication = __HeadlessApplication
import com.badlogic.gdx.Graphics as __Graphics
__Graphics = __Graphics
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import com.badlogic.gdx.utils.Clipboard as __Clipboard
__Clipboard = __Clipboard
from builtins import bool
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.Preferences as __Preferences
__Preferences = __Preferences
import java.lang.Object as __object
import com.badlogic.gdx.Application as __Application_ApplicationType
__ApplicationType = __Application_ApplicationType.ApplicationType
import java.lang.Runnable as Runnable
import com.badlogic.gdx.Audio as __Audio
__Audio = __Audio
import java.lang.Long as __long
import com.badlogic.gdx.ApplicationListener as __ApplicationListener
__ApplicationListener = __ApplicationListener
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import int
 
class HeadlessApplication():
    """com.badlogic.gdx.backends.headless.HeadlessApplication"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessApplication) -> 'HeadlessApplication':
        return HeadlessApplication(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessApplication):
        """
        Dynamic initializer for HeadlessApplication.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def log(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.log(java.lang.String,java.lang.String)"""
        super(__HeadlessApplication, self).log(arg0, arg1)

    @override
    @overload
    def getAudio(self) -> 'pygdx.Audio':
        """public com.badlogic.gdx.Audio com.badlogic.gdx.backends.headless.HeadlessApplication.getAudio()"""
        return 'pygdx.Audio'.__wrap(super(HeadlessApplication, self).getAudio())

    @override
    @overload
    def getLogLevel(self) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessApplication.getLogLevel()"""
        return int.__wrap(super(HeadlessApplication, self).getLogLevel())

    @override
    @overload
    def getApplicationLogger(self) -> 'pygdx.ApplicationLogger':
        """public com.badlogic.gdx.ApplicationLogger com.badlogic.gdx.backends.headless.HeadlessApplication.getApplicationLogger()"""
        return 'pygdx.ApplicationLogger'.__wrap(super(HeadlessApplication, self).getApplicationLogger())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.debug(java.lang.String,java.lang.String)"""
        super(__HeadlessApplication, self).debug(arg0, arg1)

    @override
    @overload
    def setApplicationLogger(self, arg0: 'ApplicationLogger'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.setApplicationLogger(com.badlogic.gdx.ApplicationLogger)"""
        super(__HeadlessApplication, self).setApplicationLogger(arg0)

    @override
    @overload
    def getApplicationListener(self) -> 'pygdx.ApplicationListener':
        """public com.badlogic.gdx.ApplicationListener com.badlogic.gdx.backends.headless.HeadlessApplication.getApplicationListener()"""
        return 'pygdx.ApplicationListener'.__wrap(super(HeadlessApplication, self).getApplicationListener())

    @override
    @overload
    def getType(self) -> 'pygdx.Application$ApplicationType':
        """public com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.backends.headless.HeadlessApplication.getType()"""
        return 'pygdx.Application$ApplicationType'.__wrap(super(HeadlessApplication, self).getType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getVersion(self) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessApplication.getVersion()"""
        return int.__wrap(super(HeadlessApplication, self).getVersion())

    @overload
    def getPreferences(self, arg0: str) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessApplication.getPreferences(java.lang.String)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessApplication, self).getPreferences(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplication, self).error(arg0, arg1, arg2)

    @override
    @overload
    def postRunnable(self, arg0: 'Runnable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.postRunnable(java.lang.Runnable)"""
        super(__HeadlessApplication, self).postRunnable(arg0)

    @override
    @overload
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplication, self).log(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getFiles(self) -> 'pygdx.Files':
        """public com.badlogic.gdx.Files com.badlogic.gdx.backends.headless.HeadlessApplication.getFiles()"""
        return 'pygdx.Files'.__wrap(super(HeadlessApplication, self).getFiles())

    @overload
    def __init__(self, arg0: 'ApplicationListener', arg1: 'HeadlessApplicationConfiguration'):
        """public com.badlogic.gdx.backends.headless.HeadlessApplication(com.badlogic.gdx.ApplicationListener,com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration)"""
        val = __HeadlessApplication(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getNativeHeap(self) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessApplication.getNativeHeap()"""
        return int.__wrap(super(HeadlessApplication, self).getNativeHeap())

    @override
    @overload
    def getClipboard(self) -> 'utils.Clipboard':
        """public com.badlogic.gdx.utils.Clipboard com.badlogic.gdx.backends.headless.HeadlessApplication.getClipboard()"""
        return 'utils.Clipboard'.__wrap(super(HeadlessApplication, self).getClipboard())

    @override
    @overload
    def setLogLevel(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.setLogLevel(int)"""
        super(__HeadlessApplication, self).setLogLevel(__int.valueOf(arg0))

    @override
    @overload
    def removeLifecycleListener(self, arg0: 'LifecycleListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.removeLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        super(__HeadlessApplication, self).removeLifecycleListener(arg0)

    @override
    @overload
    def addLifecycleListener(self, arg0: 'LifecycleListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.addLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        super(__HeadlessApplication, self).addLifecycleListener(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def exit(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.exit()"""
        super(HeadlessApplication, self).exit()

    @override
    @overload
    def getInput(self) -> 'pygdx.Input':
        """public com.badlogic.gdx.Input com.badlogic.gdx.backends.headless.HeadlessApplication.getInput()"""
        return 'pygdx.Input'.__wrap(super(HeadlessApplication, self).getInput())

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__HeadlessApplication, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getJavaHeap(self) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessApplication.getJavaHeap()"""
        return int.__wrap(super(HeadlessApplication, self).getJavaHeap())

    @override
    @overload
    def getGraphics(self) -> 'pygdx.Graphics':
        """public com.badlogic.gdx.Graphics com.badlogic.gdx.backends.headless.HeadlessApplication.getGraphics()"""
        return 'pygdx.Graphics'.__wrap(super(HeadlessApplication, self).getGraphics())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getNet(self) -> 'pygdx.Net':
        """public com.badlogic.gdx.Net com.badlogic.gdx.backends.headless.HeadlessApplication.getNet()"""
        return 'pygdx.Net'.__wrap(super(HeadlessApplication, self).getNet())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ApplicationListener'):
        """public com.badlogic.gdx.backends.headless.HeadlessApplication(com.badlogic.gdx.ApplicationListener)"""
        val = __HeadlessApplication(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.error(java.lang.String,java.lang.String)"""
        super(__HeadlessApplication, self).error(arg0, arg1)

    @overload
    def executeRunnables(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessApplication.executeRunnables()"""
        return bool.__wrap(super(HeadlessApplication, self).executeRunnables()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessPreferences
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.Preferences as __Preferences
__Preferences = __Preferences
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.backends.headless.HeadlessPreferences as __HeadlessPreferences
__HeadlessPreferences = __HeadlessPreferences
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.util.Map as Map
from builtins import bool
from builtins import int
 
class HeadlessPreferences():
    """com.badlogic.gdx.backends.headless.HeadlessPreferences"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessPreferences) -> 'HeadlessPreferences':
        return HeadlessPreferences(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessPreferences):
        """
        Dynamic initializer for HeadlessPreferences.
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
    def getLong(self, arg0: str) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessPreferences.getLong(java.lang.String)"""
        return int.__wrap(super(__HeadlessPreferences, self).getLong(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessPreferences.getString(java.lang.String)"""
        return str.__wrap(super(__HeadlessPreferences, self).getString(arg0))

    @overload
    def putInteger(self, arg0: str, arg1: int) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putInteger(java.lang.String,int)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).putInteger(arg0, __int.valueOf(arg1)))

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.contains(java.lang.String)"""
        return bool.__wrap(super(__HeadlessPreferences, self).contains(arg0))

    @overload
    def getFloat(self, arg0: str) -> float:
        """public float com.badlogic.gdx.backends.headless.HeadlessPreferences.getFloat(java.lang.String)"""
        return float.__wrap(super(__HeadlessPreferences, self).getFloat(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def get(self) -> 'Map':
        """public java.util.Map<java.lang.String, ?> com.badlogic.gdx.backends.headless.HeadlessPreferences.get()"""
        return 'Map'.__wrap(super(HeadlessPreferences, self).get())

    @overload
    def putFloat(self, arg0: str, arg1: float) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putFloat(java.lang.String,float)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).putFloat(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.flush()"""
        super(HeadlessPreferences, self).flush()

    @overload
    def putBoolean(self, arg0: str, arg1: bool) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putBoolean(java.lang.String,boolean)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).putBoolean(arg0, __boolean.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getInteger(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessPreferences.getInteger(java.lang.String,int)"""
        return int.__wrap(super(__HeadlessPreferences, self).getInteger(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.backends.headless.HeadlessPreferences(com.badlogic.gdx.files.FileHandle)"""
        val = __HeadlessPreferences(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putLong(self, arg0: str, arg1: int) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putLong(java.lang.String,long)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).putLong(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def put(self, arg0: 'Map') -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.put(java.util.Map<java.lang.String, ?>)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).put(arg0))

    @overload
    def getString(self, arg0: str, arg1: str) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessPreferences.getString(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__HeadlessPreferences, self).getString(arg0, arg1))

    @override
    @overload
    def remove(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.remove(java.lang.String)"""
        super(__HeadlessPreferences, self).remove(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def putString(self, arg0: str, arg1: str) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putString(java.lang.String,java.lang.String)"""
        return 'pygdx.Preferences'.__wrap(super(__HeadlessPreferences, self).putString(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getInteger(self, arg0: str) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessPreferences.getInteger(java.lang.String)"""
        return int.__wrap(super(__HeadlessPreferences, self).getInteger(arg0))

    @overload
    def getLong(self, arg0: str, arg1: int) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessPreferences.getLong(java.lang.String,long)"""
        return int.__wrap(super(__HeadlessPreferences, self).getLong(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.clear()"""
        super(HeadlessPreferences, self).clear()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.getBoolean(java.lang.String)"""
        return bool.__wrap(super(__HeadlessPreferences, self).getBoolean(arg0))

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float com.badlogic.gdx.backends.headless.HeadlessPreferences.getFloat(java.lang.String,float)"""
        return float.__wrap(super(__HeadlessPreferences, self).getFloat(arg0, __float.valueOf(arg1)))

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.getBoolean(java.lang.String,boolean)"""
        return bool.__wrap(super(__HeadlessPreferences, self).getBoolean(arg0, __boolean.valueOf(arg1)))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.backends.headless.HeadlessPreferences(java.lang.String,java.lang.String)"""
        val = __HeadlessPreferences(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessFiles
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.backends.headless.HeadlessFiles as __HeadlessFiles
__HeadlessFiles = __HeadlessFiles
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class HeadlessFiles():
    """com.badlogic.gdx.backends.headless.HeadlessFiles"""
 
    @staticmethod
    def __wrap(java_value: __HeadlessFiles) -> 'HeadlessFiles':
        return HeadlessFiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HeadlessFiles):
        """
        Dynamic initializer for HeadlessFiles.
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
 
    @override
    @overload
    def isExternalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isExternalStorageAvailable()"""
        return bool.__wrap(super(HeadlessFiles, self).isExternalStorageAvailable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def local(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.local(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).local(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getExternalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getExternalStoragePath()"""
        return str.__wrap(super(HeadlessFiles, self).getExternalStoragePath())

    @overload
    def external(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.external(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).external(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = __HeadlessFiles()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def internal(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.internal(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).internal(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = __HeadlessFiles()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.getFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).getFileHandle(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

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

    @overload
    def classpath(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.classpath(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).classpath(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def absolute(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.absolute(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__HeadlessFiles, self).absolute(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getLocalStoragePath()"""
        return str.__wrap(super(HeadlessFiles, self).getLocalStoragePath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isLocalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isLocalStorageAvailable()"""
        return bool.__wrap(super(HeadlessFiles, self).isLocalStorageAvailable())