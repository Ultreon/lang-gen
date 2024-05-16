from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.files.FileHandleStream as __FileHandleStream
__FileHandleStream = __FileHandleStream
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.io.File as __File
__File = __File
import java.lang.String as __string
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
import java.io.BufferedInputStream as __BufferedInputStream
__BufferedInputStream = __BufferedInputStream
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.FileFilter as FileFilter
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
 
class FileHandleStream(ABC):
    """com.badlogic.gdx.files.FileHandleStream"""
 
    @staticmethod
    def __wrap(java_value: __FileHandleStream) -> 'FileHandleStream':
        return FileHandleStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileHandleStream):
        """
        Dynamic initializer for FileHandleStream.
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
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempDirectory(arg0))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0), arg1))

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__FileHandle, self).readString(arg0))

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str.__wrap(super(FileHandle, self).name())

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __boolean.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.exists()"""
        return bool.__wrap(super(FileHandleStream, self).exists())

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0)))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0)))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str.__wrap(super(FileHandle, self).extension())

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str.__wrap(super(FileHandle, self).readString())

    @override
    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.parent()"""
        return 'FileHandle'.__wrap(super(FileHandleStream, self).parent())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'.__wrap(super(FileHandle, self).type())

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'.__wrap(super(FileHandle, self).file())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'.__wrap(super(__FileHandle, self).map(arg0))

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory(boolean)"""
        super(__FileHandleStream, self).emptyDirectory(__boolean.valueOf(arg0))

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0), arg1))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandleStream.write(boolean)"""
        return 'OutputStream'.__wrap(super(__FileHandleStream, self).write(__boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(FileHandle, self).hashCode())

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory()"""
        super(FileHandleStream, self).emptyDirectory()

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'.__wrap(super(__FileHandle, self).write(__boolean.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str.__wrap(super(FileHandle, self).path())

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandleStream.read()"""
        return 'InputStream'.__wrap(super(FileHandleStream, self).read())

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'.__wrap(super(__FileHandle, self).reader(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int.__wrap(super(FileHandle, self).lastModified())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandleStream.list()"""
        return List['FileHandle'].__wrap(super(FileHandleStream, self).list())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandleStream(java.lang.String)"""
        val = __FileHandleStream(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandleStream.mkdirs()"""
        super(FileHandleStream, self).mkdirs()

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1), arg2)

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'.__wrap(super(FileHandle, self).map())

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__FileHandle, self).read(__int.valueOf(arg0)))

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.isDirectory()"""
        return bool.__wrap(super(FileHandleStream, self).isDirectory())

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandleStream, self).moveTo(arg0)

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandleStream.length()"""
        return int.__wrap(super(FileHandleStream, self).length())

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(FileHandle, self).readBytes())

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'.__wrap(super(FileHandle, self).reader())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.delete()"""
        return bool.__wrap(super(FileHandleStream, self).delete())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempFile(arg0))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int.__wrap(super(__FileHandle, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.child(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandleStream, self).child(arg0))

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
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.sibling(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandleStream, self).sibling(arg0))

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.deleteDirectory()"""
        return bool.__wrap(super(FileHandleStream, self).deleteDirectory())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__FileHandle, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str.__wrap(super(FileHandle, self).toString())

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(__FileHandle, self).write(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandleStream, self).copyTo(arg0)

 
 
 
# CLASS: com.badlogic.gdx.files.FileHandleStream
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
import com.badlogic.gdx.files.FileHandleStream as __FileHandleStream
__FileHandleStream = __FileHandleStream
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.io.File as __File
__File = __File
import java.lang.String as __string
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
import java.io.BufferedInputStream as __BufferedInputStream
__BufferedInputStream = __BufferedInputStream
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.FileFilter as FileFilter
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
 
class FileHandleStream(ABC):
    """com.badlogic.gdx.files.FileHandleStream"""
 
    @staticmethod
    def __wrap(java_value: __FileHandleStream) -> 'FileHandleStream':
        return FileHandleStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileHandleStream):
        """
        Dynamic initializer for FileHandleStream.
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
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempDirectory(arg0))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0), arg1))

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__FileHandle, self).readString(arg0))

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str.__wrap(super(FileHandle, self).name())

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __boolean.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.exists()"""
        return bool.__wrap(super(FileHandleStream, self).exists())

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0)))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0)))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str.__wrap(super(FileHandle, self).extension())

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str.__wrap(super(FileHandle, self).readString())

    @override
    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.parent()"""
        return 'FileHandle'.__wrap(super(FileHandleStream, self).parent())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'.__wrap(super(FileHandle, self).type())

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'.__wrap(super(FileHandle, self).file())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'.__wrap(super(__FileHandle, self).map(arg0))

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory(boolean)"""
        super(__FileHandleStream, self).emptyDirectory(__boolean.valueOf(arg0))

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0), arg1))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandleStream.write(boolean)"""
        return 'OutputStream'.__wrap(super(__FileHandleStream, self).write(__boolean.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(FileHandle, self).hashCode())

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory()"""
        super(FileHandleStream, self).emptyDirectory()

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'.__wrap(super(__FileHandle, self).write(__boolean.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str.__wrap(super(FileHandle, self).path())

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandleStream.read()"""
        return 'InputStream'.__wrap(super(FileHandleStream, self).read())

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'.__wrap(super(__FileHandle, self).reader(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int.__wrap(super(FileHandle, self).lastModified())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandleStream.list()"""
        return List['FileHandle'].__wrap(super(FileHandleStream, self).list())

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandleStream(java.lang.String)"""
        val = __FileHandleStream(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandleStream.mkdirs()"""
        super(FileHandleStream, self).mkdirs()

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1), arg2)

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'.__wrap(super(FileHandle, self).map())

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__FileHandle, self).read(__int.valueOf(arg0)))

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.isDirectory()"""
        return bool.__wrap(super(FileHandleStream, self).isDirectory())

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandleStream, self).moveTo(arg0)

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandleStream.length()"""
        return int.__wrap(super(FileHandleStream, self).length())

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(FileHandle, self).readBytes())

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'.__wrap(super(FileHandle, self).reader())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.delete()"""
        return bool.__wrap(super(FileHandleStream, self).delete())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempFile(arg0))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int.__wrap(super(__FileHandle, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.child(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandleStream, self).child(arg0))

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
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.sibling(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandleStream, self).sibling(arg0))

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.deleteDirectory()"""
        return bool.__wrap(super(FileHandleStream, self).deleteDirectory())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__FileHandle, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str.__wrap(super(FileHandle, self).toString())

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(__FileHandle, self).write(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandleStream, self).copyTo(arg0)

 
 
 
# CLASS: com.badlogic.gdx.files.FileHandleStream 
 
 
# CLASS: com.badlogic.gdx.files.FileHandle
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
 
class FileHandle():
    """com.badlogic.gdx.files.FileHandle"""
 
    @staticmethod
    def __wrap(java_value: __FileHandle) -> 'FileHandle':
        return FileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileHandle):
        """
        Dynamic initializer for FileHandle.
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
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempDirectory(arg0))

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0), arg1))

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__FileHandle, self).readString(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandle(java.lang.String)"""
        val = __FileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str.__wrap(super(FileHandle, self).extension())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool.__wrap(super(FileHandle, self).delete())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str.__wrap(super(FileHandle, self).name())

    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'.__wrap(super(FileHandle, self).type())

    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'.__wrap(super(FileHandle, self).reader())

    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int.__wrap(super(FileHandle, self).lastModified())

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'.__wrap(super(__FileHandle, self).writer(__boolean.valueOf(arg0)))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0)))

    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandle, self).moveTo(arg0)

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean)"""
        return 'OutputStream'.__wrap(super(__FileHandle, self).write(__boolean.valueOf(arg0)))

    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str.__wrap(super(FileHandle, self).path())

    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandle.read()"""
        return 'InputStream'.__wrap(super(FileHandle, self).read())

    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list()"""
        return List['FileHandle'].__wrap(super(FileHandle, self).list())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'.__wrap(super(__FileHandle, self).map(arg0))

    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1))

    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory()"""
        super(FileHandle, self).emptyDirectory()

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'.__wrap(super(__FileHandle, self).reader(__int.valueOf(arg0), arg1))

    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(__FileHandle, self).writeString(arg0, __boolean.valueOf(arg1), arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(FileHandle, self).hashCode())

    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory(boolean)"""
        super(__FileHandle, self).emptyDirectory(__boolean.valueOf(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'.__wrap(super(__FileHandle, self).write(__boolean.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'.__wrap(super(__FileHandle, self).reader(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'File'):
        """public com.badlogic.gdx.files.FileHandle(java.io.File)"""
        val = __FileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))

    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__FileHandle, self).copyTo(arg0)

    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandle.mkdirs()"""
        super(FileHandle, self).mkdirs()

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle'].__wrap(super(__FileHandle, self).list(arg0))

    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(FileHandle, self).readBytes())

    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(__FileHandle, self).writeBytes(bytes, __boolean.valueOf(arg1))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__FileHandle, self).read(__int.valueOf(arg0)))

    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.length()"""
        return int.__wrap(super(FileHandle, self).length())

    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'.__wrap(super(FileHandle, self).map())

    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.isDirectory()"""
        return bool.__wrap(super(FileHandle, self).isDirectory())

    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.parent()"""
        return 'FileHandle'.__wrap(super(FileHandle, self).parent())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle.__wrap(__FileHandle.tempFile(arg0))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int.__wrap(super(__FileHandle, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.exists()"""
        return bool.__wrap(super(FileHandle, self).exists())

    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str.__wrap(super(FileHandle, self).readString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'.__wrap(super(FileHandle, self).file())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__FileHandle, self).equals(arg0))

    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(__FileHandle, self).write(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str.__wrap(super(FileHandle, self).toString())

    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.deleteDirectory()"""
        return bool.__wrap(super(FileHandle, self).deleteDirectory())

    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(FileHandle, self).nameWithoutExtension())

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.child(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandle, self).child(arg0))

    @overload
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.sibling(java.lang.String)"""
        return 'FileHandle'.__wrap(super(__FileHandle, self).sibling(arg0))