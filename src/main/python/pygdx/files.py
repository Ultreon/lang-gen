from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import com.badlogic.gdx.Files as _Files_FileType
_FileType = _Files_FileType.FileType
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.io.FileFilter as FileFilter
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.io.BufferedInputStream as _BufferedInputStream
_BufferedInputStream = _BufferedInputStream
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.files.FileHandleStream as _FileHandleStream
_FileHandleStream = _FileHandleStream
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.BufferedReader as BufferedReader
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileHandleStream():
    """com.badlogic.gdx.files.FileHandleStream"""
 
    @staticmethod
    def _wrap(java_value: _FileHandleStream) -> 'FileHandleStream':
        return FileHandleStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileHandleStream):
        """
        Dynamic initializer for FileHandleStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileHandleStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileHandleStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1))

    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str._wrap(super(FileHandle, self).readString())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempFile(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str._wrap(super(FileHandle, self).toString())

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0), arg1))

    @overload
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.sibling(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandleStream, self).sibling(arg0))

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

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.exists()"""
        return bool._wrap(super(FileHandleStream, self).exists())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.delete()"""
        return bool._wrap(super(FileHandleStream, self).delete())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int._wrap(super(FileHandle, self).hashCode())

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _boolean.valueOf(arg1))

    @override
    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandleStream.list()"""
        return List['FileHandle']._wrap(super(FileHandleStream, self).list())

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.child(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandleStream, self).child(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool._wrap(super(_FileHandle, self).equals(arg0))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0)))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1), arg2)

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandleStream.length()"""
        return int._wrap(super(FileHandleStream, self).length())

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempDirectory(arg0))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'._wrap(super(_FileHandle, self).read(_int.valueOf(arg0)))

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str._wrap(super(FileHandle, self).name())

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0), arg1))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int._wrap(super(_FileHandle, self).readBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory()"""
        super(FileHandleStream, self).emptyDirectory()

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'._wrap(super(FileHandle, self).reader())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'._wrap(super(_FileHandle, self).map(arg0))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str._wrap(super(FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.parent()"""
        return 'FileHandle'._wrap(super(FileHandleStream, self).parent())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'._wrap(super(FileHandle, self).file())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'._wrap(super(FileHandle, self).type())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'._wrap(super(_FileHandle, self).write(_boolean.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str._wrap(super(FileHandle, self).extension())

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.deleteDirectory()"""
        return bool._wrap(super(FileHandleStream, self).deleteDirectory())

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandleStream.read()"""
        return 'InputStream'._wrap(super(FileHandleStream, self).read())

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandleStream.mkdirs()"""
        super(FileHandleStream, self).mkdirs()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandleStream(java.lang.String)"""
        val = _FileHandleStream(arg0)
        self.__wrapper = val

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0)))

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandleStream, self).copyTo(arg0)

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str._wrap(super(FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(_FileHandle, self).write(arg0, _boolean.valueOf(arg1))

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'._wrap(super(_FileHandle, self).reader(arg0))

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int]._wrap(super(FileHandle, self).readBytes())

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'._wrap(super(FileHandle, self).map())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str._wrap(super(FileHandle, self).path())

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory(boolean)"""
        super(_FileHandleStream, self).emptyDirectory(_boolean.valueOf(arg0))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandleStream.write(boolean)"""
        return 'OutputStream'._wrap(super(_FileHandleStream, self).write(_boolean.valueOf(arg0)))

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.isDirectory()"""
        return bool._wrap(super(FileHandleStream, self).isDirectory())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandleStream, self).moveTo(arg0)

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int._wrap(super(FileHandle, self).lastModified())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str._wrap(super(_FileHandle, self).readString(arg0))

 
 
 
# CLASS: com.badlogic.gdx.files.FileHandleStream
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import com.badlogic.gdx.Files as _Files_FileType
_FileType = _Files_FileType.FileType
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.io.FileFilter as FileFilter
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.io.BufferedInputStream as _BufferedInputStream
_BufferedInputStream = _BufferedInputStream
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import com.badlogic.gdx.files.FileHandleStream as _FileHandleStream
_FileHandleStream = _FileHandleStream
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.BufferedReader as BufferedReader
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileHandleStream():
    """com.badlogic.gdx.files.FileHandleStream"""
 
    @staticmethod
    def _wrap(java_value: _FileHandleStream) -> 'FileHandleStream':
        return FileHandleStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileHandleStream):
        """
        Dynamic initializer for FileHandleStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileHandleStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileHandleStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1))

    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str._wrap(super(FileHandle, self).readString())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempFile(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str._wrap(super(FileHandle, self).toString())

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0), arg1))

    @overload
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.sibling(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandleStream, self).sibling(arg0))

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

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.exists()"""
        return bool._wrap(super(FileHandleStream, self).exists())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.delete()"""
        return bool._wrap(super(FileHandleStream, self).delete())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int._wrap(super(FileHandle, self).hashCode())

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _boolean.valueOf(arg1))

    @override
    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandleStream.list()"""
        return List['FileHandle']._wrap(super(FileHandleStream, self).list())

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.child(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandleStream, self).child(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool._wrap(super(_FileHandle, self).equals(arg0))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0)))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1), arg2)

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandleStream.length()"""
        return int._wrap(super(FileHandleStream, self).length())

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempDirectory(arg0))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'._wrap(super(_FileHandle, self).read(_int.valueOf(arg0)))

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str._wrap(super(FileHandle, self).name())

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0), arg1))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int._wrap(super(_FileHandle, self).readBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory()"""
        super(FileHandleStream, self).emptyDirectory()

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'._wrap(super(FileHandle, self).reader())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'._wrap(super(_FileHandle, self).map(arg0))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str._wrap(super(FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandleStream.parent()"""
        return 'FileHandle'._wrap(super(FileHandleStream, self).parent())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'._wrap(super(FileHandle, self).file())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'._wrap(super(FileHandle, self).type())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'._wrap(super(_FileHandle, self).write(_boolean.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str._wrap(super(FileHandle, self).extension())

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.deleteDirectory()"""
        return bool._wrap(super(FileHandleStream, self).deleteDirectory())

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandleStream.read()"""
        return 'InputStream'._wrap(super(FileHandleStream, self).read())

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandleStream.mkdirs()"""
        super(FileHandleStream, self).mkdirs()

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandleStream(java.lang.String)"""
        val = _FileHandleStream(arg0)
        self.__wrapper = val

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0)))

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandleStream, self).copyTo(arg0)

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str._wrap(super(FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(_FileHandle, self).write(arg0, _boolean.valueOf(arg1))

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'._wrap(super(_FileHandle, self).reader(arg0))

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int]._wrap(super(FileHandle, self).readBytes())

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'._wrap(super(FileHandle, self).map())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str._wrap(super(FileHandle, self).path())

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandleStream.emptyDirectory(boolean)"""
        super(_FileHandleStream, self).emptyDirectory(_boolean.valueOf(arg0))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandleStream.write(boolean)"""
        return 'OutputStream'._wrap(super(_FileHandleStream, self).write(_boolean.valueOf(arg0)))

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandleStream.isDirectory()"""
        return bool._wrap(super(FileHandleStream, self).isDirectory())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandleStream.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandleStream, self).moveTo(arg0)

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int._wrap(super(FileHandle, self).lastModified())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str._wrap(super(_FileHandle, self).readString(arg0))

 
 
 
# CLASS: com.badlogic.gdx.files.FileHandleStream 
 
 
# CLASS: com.badlogic.gdx.files.FileHandle
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import com.badlogic.gdx.Files as _Files_FileType
_FileType = _Files_FileType.FileType
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.io.FilenameFilter as FilenameFilter
from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.Reader as _Reader
_Reader = _Reader
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.io.FileFilter as FileFilter
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.io.BufferedInputStream as _BufferedInputStream
_BufferedInputStream = _BufferedInputStream
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.BufferedReader as BufferedReader
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileHandle():
    """com.badlogic.gdx.files.FileHandle"""
 
    @staticmethod
    def _wrap(java_value: _FileHandle) -> 'FileHandle':
        return FileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileHandle):
        """
        Dynamic initializer for FileHandle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileHandle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileHandle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def list(self, arg0: str) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'._wrap(super(FileHandle, self).reader())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempFile(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str._wrap(super(FileHandle, self).toString())

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0), arg1))

    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1))

    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str._wrap(super(FileHandle, self).pathWithoutExtension())

    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandle, self).copyTo(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.files.FileHandle(java.lang.String)"""
        val = _FileHandle(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.deleteDirectory()"""
        return bool._wrap(super(FileHandle, self).deleteDirectory())

    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool._wrap(super(FileHandle, self).delete())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int._wrap(super(FileHandle, self).hashCode())

    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(_FileHandle, self).write(arg0, _boolean.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'File'):
        """public com.badlogic.gdx.files.FileHandle(java.io.File)"""
        val = _FileHandle(arg0)
        self.__wrapper = val

    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandle.read()"""
        return 'InputStream'._wrap(super(FileHandle, self).read())

    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool._wrap(super(_FileHandle, self).equals(arg0))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'._wrap(super(_FileHandle, self).reader(_int.valueOf(arg0)))

    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str._wrap(super(FileHandle, self).readString())

    @overload
    def parent(self) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.parent()"""
        return 'FileHandle'._wrap(super(FileHandle, self).parent())

    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.files.FileHandle.file()"""
        return 'File'._wrap(super(FileHandle, self).file())

    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory()"""
        super(FileHandle, self).emptyDirectory()

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return FileHandle._wrap(_FileHandle.tempDirectory(arg0))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'._wrap(super(_FileHandle, self).read(_int.valueOf(arg0)))

    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str._wrap(super(FileHandle, self).path())

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0), arg1))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int._wrap(super(_FileHandle, self).readBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'._wrap(super(_FileHandle, self).map(arg0))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean)"""
        return 'OutputStream'._wrap(super(_FileHandle, self).write(_boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def child(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.child(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandle, self).child(arg0))

    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(_FileHandle, self).writeBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))

    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.exists()"""
        return bool._wrap(super(FileHandle, self).exists())

    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str._wrap(super(FileHandle, self).nameWithoutExtension())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'._wrap(super(_FileHandle, self).write(_boolean.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(_FileHandle, self).writeString(arg0, _boolean.valueOf(arg1), arg2)

    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandle.mkdirs()"""
        super(FileHandle, self).mkdirs()

    @overload
    def sibling(self, arg0: str) -> 'FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.sibling(java.lang.String)"""
        return 'FileHandle'._wrap(super(_FileHandle, self).sibling(arg0))

    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(_FileHandle, self).moveTo(arg0)

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'._wrap(super(_FileHandle, self).writer(_boolean.valueOf(arg0)))

    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'._wrap(super(FileHandle, self).type())

    @overload
    def list(self) -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list()"""
        return List['FileHandle']._wrap(super(FileHandle, self).list())

    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str._wrap(super(FileHandle, self).extension())

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'._wrap(super(_FileHandle, self).reader(arg0))

    @overload
    def list(self, arg0: 'FileFilter') -> List['FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['FileHandle']._wrap(super(_FileHandle, self).list(arg0))

    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.isDirectory()"""
        return bool._wrap(super(FileHandle, self).isDirectory())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str._wrap(super(FileHandle, self).name())

    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int]._wrap(super(FileHandle, self).readBytes())

    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.length()"""
        return int._wrap(super(FileHandle, self).length())

    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int._wrap(super(FileHandle, self).lastModified())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory(boolean)"""
        super(_FileHandle, self).emptyDirectory(_boolean.valueOf(arg0))

    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'._wrap(super(FileHandle, self).map())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str._wrap(super(_FileHandle, self).readString(arg0))