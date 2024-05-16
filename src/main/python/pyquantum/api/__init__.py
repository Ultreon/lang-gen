from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.api.FileIO as _FileIO
_FileIO = _FileIO
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileIO():
    """dev.ultreon.quantum.api.FileIO"""
 
    @staticmethod
    def _wrap(java_value: _FileIO) -> 'FileIO':
        return FileIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileIO):
        """
        Dynamic initializer for FileIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileIO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence', arg2: 'Charset'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence,java.nio.charset.Charset)"""
        _FileIO.writeString(arg0, arg1, arg2)

    @staticmethod
    @overload
    def writeBytes(arg0: 'Path', arg1: bytes):
        """public static void dev.ultreon.quantum.api.FileIO.writeBytes(java.nio.file.Path,byte[])"""
        _FileIO.writeBytes(arg0, bytes)

    @staticmethod
    @overload
    def readString(arg0: 'Path') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path) throws java.io.IOException"""
        return str._wrap(_FileIO.readString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence)"""
        _FileIO.writeString(arg0, arg1)

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def readBytes(arg0: 'Path') -> List[int]:
        """public static byte[] dev.ultreon.quantum.api.FileIO.readBytes(java.nio.file.Path) throws java.io.IOException"""
        return List[int]._wrap(_FileIO.readBytes(arg0))

    @staticmethod
    @overload
    def readString(arg0: 'Path', arg1: 'Charset') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path,java.nio.charset.Charset) throws java.io.IOException"""
        return str._wrap(_FileIO.readString(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.api.FileIO
import dev.ultreon.quantum.api.FileIO as _FileIO
_FileIO = _FileIO
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.nio.file.Path as Path
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FileIO():
    """dev.ultreon.quantum.api.FileIO"""
 
    @staticmethod
    def _wrap(java_value: _FileIO) -> 'FileIO':
        return FileIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileIO):
        """
        Dynamic initializer for FileIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileIO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence', arg2: 'Charset'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence,java.nio.charset.Charset)"""
        _FileIO.writeString(arg0, arg1, arg2)

    @staticmethod
    @overload
    def writeBytes(arg0: 'Path', arg1: bytes):
        """public static void dev.ultreon.quantum.api.FileIO.writeBytes(java.nio.file.Path,byte[])"""
        _FileIO.writeBytes(arg0, bytes)

    @staticmethod
    @overload
    def readString(arg0: 'Path') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path) throws java.io.IOException"""
        return str._wrap(_FileIO.readString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence)"""
        _FileIO.writeString(arg0, arg1)

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def readBytes(arg0: 'Path') -> List[int]:
        """public static byte[] dev.ultreon.quantum.api.FileIO.readBytes(java.nio.file.Path) throws java.io.IOException"""
        return List[int]._wrap(_FileIO.readBytes(arg0))

    @staticmethod
    @overload
    def readString(arg0: 'Path', arg1: 'Charset') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path,java.nio.charset.Charset) throws java.io.IOException"""
        return str._wrap(_FileIO.readString(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.api.FileIO