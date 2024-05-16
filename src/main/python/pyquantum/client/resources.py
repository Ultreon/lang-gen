from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.resources.ResourceLoader as __ResourceLoader
__ResourceLoader = __ResourceLoader
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client.model import model
except ImportError:
    model = __import_once__("pyquantum.client.model.model")

import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ResourceLoader():
    """dev.ultreon.quantum.client.resources.ResourceLoader"""
 
    @staticmethod
    def __wrap(java_value: __ResourceLoader) -> 'ResourceLoader':
        return ResourceLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceLoader):
        """
        Dynamic initializer for ResourceLoader.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def loadG3D(arg0: 'Identifier') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.resources.ResourceLoader.loadG3D(dev.ultreon.quantum.util.Identifier)"""
        return g3d.Model.__wrap(__ResourceLoader.loadG3D(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.resources.ResourceLoader()"""
        val = __ResourceLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def init(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.resources.ResourceLoader.init(dev.ultreon.quantum.client.QuantumClient)"""
        __ResourceLoader.init(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.resources.ResourceLoader()"""
        val = __ResourceLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def loadG3D(arg0: 'Resource', arg1: 'ModelType', arg2: 'TextureProvider') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.resources.ResourceLoader.loadG3D(dev.ultreon.quantum.resources.Resource,dev.ultreon.quantum.client.model.model.ModelType,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return g3d.Model.__wrap(__ResourceLoader.loadG3D(arg0, arg1, arg2))

 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ResourceLoader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import dev.ultreon.quantum.client.resources.ResourceLoader as __ResourceLoader
__ResourceLoader = __ResourceLoader
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import com.badlogic.gdx.graphics.g3d.Model as __Model
__Model = __Model
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pyquantum.client.model import model
except ImportError:
    model = __import_once__("pyquantum.client.model.model")

import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ResourceLoader():
    """dev.ultreon.quantum.client.resources.ResourceLoader"""
 
    @staticmethod
    def __wrap(java_value: __ResourceLoader) -> 'ResourceLoader':
        return ResourceLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceLoader):
        """
        Dynamic initializer for ResourceLoader.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def loadG3D(arg0: 'Identifier') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.resources.ResourceLoader.loadG3D(dev.ultreon.quantum.util.Identifier)"""
        return g3d.Model.__wrap(__ResourceLoader.loadG3D(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.resources.ResourceLoader()"""
        val = __ResourceLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def init(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.client.resources.ResourceLoader.init(dev.ultreon.quantum.client.QuantumClient)"""
        __ResourceLoader.init(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.resources.ResourceLoader()"""
        val = __ResourceLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def loadG3D(arg0: 'Resource', arg1: 'ModelType', arg2: 'TextureProvider') -> 'g3d.Model':
        """public static com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.resources.ResourceLoader.loadG3D(dev.ultreon.quantum.resources.Resource,dev.ultreon.quantum.client.model.model.ModelType,com.badlogic.gdx.graphics.g3d.utils.TextureProvider)"""
        return g3d.Model.__wrap(__ResourceLoader.loadG3D(arg0, arg1, arg2))

 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ResourceLoader 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ByteArrayFileHandle
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
import dev.ultreon.quantum.client.resources.ByteArrayFileHandle as __ByteArrayFileHandle
__ByteArrayFileHandle = __ByteArrayFileHandle
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
 
class ByteArrayFileHandle(pygdx.__FileHandle, files.FileHandle):
    """dev.ultreon.quantum.client.resources.ByteArrayFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __ByteArrayFileHandle) -> 'ByteArrayFileHandle':
        return ByteArrayFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteArrayFileHandle):
        """
        Dynamic initializer for ByteArrayFileHandle.
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

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.client.resources.ByteArrayFileHandle.read()"""
        return 'InputStream'.__wrap(super(ByteArrayFileHandle, self).read())

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__files.FileHandle, self).read(__int.valueOf(arg0)))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.resources.ByteArrayFileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__ByteArrayFileHandle, self).equals(arg0))

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.resources.ByteArrayFileHandle.hashCode()"""
        return int.__wrap(super(ByteArrayFileHandle, self).hashCode())

    @overload
    def list(self, arg0: str) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

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
    def __init__(self, arg0: str, arg1: bytes):
        """public dev.ultreon.quantum.client.resources.ByteArrayFileHandle(java.lang.String,byte[])"""
        val = __ByteArrayFileHandle(arg0, bytes)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] dev.ultreon.quantum.client.resources.ByteArrayFileHandle.readBytes()"""
        return List[int].__wrap(super(ByteArrayFileHandle, self).readBytes())

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
 
 
# CLASS: dev.ultreon.quantum.client.resources.LoadableResource
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.resources.LoadableResource as __LoadableResource
__LoadableResource = __LoadableResource
 
class LoadableResource(ABC):
    """dev.ultreon.quantum.client.resources.LoadableResource"""
 
    @staticmethod
    def __wrap(java_value: __LoadableResource) -> 'LoadableResource':
        return LoadableResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoadableResource):
        """
        Dynamic initializer for LoadableResource.
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
 
    @abstractmethod
    def resourceId(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.resources.LoadableResource.resourceId()"""
        pass

    @abstractmethod
    def load(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.resources.LoadableResource.load(dev.ultreon.quantum.client.QuantumClient)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ResourceNotFoundException
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.resources.ResourceNotFoundException as __ResourceNotFoundException
__ResourceNotFoundException = __ResourceNotFoundException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ResourceNotFoundException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.client.resources.ResourceNotFoundException"""
 
    @staticmethod
    def __wrap(java_value: __ResourceNotFoundException) -> 'ResourceNotFoundException':
        return ResourceNotFoundException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceNotFoundException):
        """
        Dynamic initializer for ResourceNotFoundException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.resources.ResourceNotFoundException(dev.ultreon.quantum.util.Identifier)"""
        val = __ResourceNotFoundException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ContextAwareReloadable
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.client.resources.ContextAwareReloadable as __ContextAwareReloadable
__ContextAwareReloadable = __ContextAwareReloadable
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

from abc import abstractmethod, ABC
 
class ContextAwareReloadable(ABC):
    """dev.ultreon.quantum.client.resources.ContextAwareReloadable"""
 
    @staticmethod
    def __wrap(java_value: __ContextAwareReloadable) -> 'ContextAwareReloadable':
        return ContextAwareReloadable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ContextAwareReloadable):
        """
        Dynamic initializer for ContextAwareReloadable.
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
 
    @abstractmethod
    def reload(self, arg0: 'ResourceManager', arg1: 'ReloadContext'):
        """public abstract void dev.ultreon.quantum.client.resources.ContextAwareReloadable.reload(dev.ultreon.quantum.resources.ResourceManager,dev.ultreon.quantum.resources.ReloadContext)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.resources.ResourceFileHandle
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
import dev.ultreon.quantum.resources.Resource as __Resource
__Resource = __Resource
import java.lang.Class as __Class
__Class = __Class
import java.io.File as __File
__File = __File
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.io.FilenameFilter as FilenameFilter
import dev.ultreon.quantum.client.resources.ResourceFileHandle as __ResourceFileHandle
__ResourceFileHandle = __ResourceFileHandle
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
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class ResourceFileHandle(pygdx.__FileHandle, files.FileHandle):
    """dev.ultreon.quantum.client.resources.ResourceFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __ResourceFileHandle) -> 'ResourceFileHandle':
        return ResourceFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceFileHandle):
        """
        Dynamic initializer for ResourceFileHandle.
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
    def getResource(self) -> 'resources.Resource':
        """public dev.ultreon.quantum.resources.Resource dev.ultreon.quantum.client.resources.ResourceFileHandle.getResource()"""
        return 'resources.Resource'.__wrap(super(ResourceFileHandle, self).getResource())

    @overload
    def list(self, arg0: str) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(files.FileHandle, self).hashCode())

    @overload
    def __init__(self, arg0: 'Resource'):
        """public dev.ultreon.quantum.client.resources.ResourceFileHandle(dev.ultreon.quantum.resources.Resource)"""
        val = __ResourceFileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.resources.ResourceFileHandle.getId()"""
        return 'util.Identifier'.__wrap(super(ResourceFileHandle, self).getId())

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

    @override
    @overload
    def exists(self) -> bool:
        """public boolean dev.ultreon.quantum.client.resources.ResourceFileHandle.exists()"""
        return bool.__wrap(super(ResourceFileHandle, self).exists())

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

    @overload
    def __init__(self, arg0: 'Identifier'):
        """public dev.ultreon.quantum.client.resources.ResourceFileHandle(dev.ultreon.quantum.util.Identifier)"""
        val = __ResourceFileHandle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def read(self) -> 'InputStream':
        """public java.io.InputStream dev.ultreon.quantum.client.resources.ResourceFileHandle.read()"""
        return 'InputStream'.__wrap(super(ResourceFileHandle, self).read())

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
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__files.FileHandle, self).copyTo(arg0)