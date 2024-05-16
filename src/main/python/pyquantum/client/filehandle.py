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
import dev.ultreon.quantum.client.filehandle.DataFileHandle as __DataFileHandle
__DataFileHandle = __DataFileHandle
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
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
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
 
class DataFileHandle(pygdx.__FileHandle, files.FileHandle):
    """dev.ultreon.quantum.client.filehandle.DataFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __DataFileHandle) -> 'DataFileHandle':
        return DataFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataFileHandle):
        """
        Dynamic initializer for DataFileHandle.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.filehandle.DataFileHandle(java.lang.String)"""
        val = __DataFileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.child(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__files.FileHandle, self).child(arg0))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.parent()"""
        return 'files.FileHandle'.__wrap(super(files.FileHandle, self).parent())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool.__wrap(super(files.FileHandle, self).delete())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__files.FileHandle, self).readString(arg0))

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(files.FileHandle, self).readBytes())

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
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__files.FileHandle, self).sibling(arg0))

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

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'.__wrap(super(files.FileHandle, self).file())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.filehandle.DataFileHandle
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
import dev.ultreon.quantum.client.filehandle.DataFileHandle as __DataFileHandle
__DataFileHandle = __DataFileHandle
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
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
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
 
class DataFileHandle(pygdx.__FileHandle, files.FileHandle):
    """dev.ultreon.quantum.client.filehandle.DataFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __DataFileHandle) -> 'DataFileHandle':
        return DataFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DataFileHandle):
        """
        Dynamic initializer for DataFileHandle.
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.client.filehandle.DataFileHandle(java.lang.String)"""
        val = __DataFileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.child(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__files.FileHandle, self).child(arg0))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.parent()"""
        return 'files.FileHandle'.__wrap(super(files.FileHandle, self).parent())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool.__wrap(super(files.FileHandle, self).delete())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__files.FileHandle, self).readString(arg0))

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(files.FileHandle, self).readBytes())

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
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__files.FileHandle, self).sibling(arg0))

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

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'.__wrap(super(files.FileHandle, self).file())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.filehandle.DataFileHandle