from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.file.Path as Path
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.FileIO as __FileIO
__FileIO = __FileIO
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FileIO():
    """dev.ultreon.quantum.api.FileIO"""
 
    @staticmethod
    def __wrap(java_value: __FileIO) -> 'FileIO':
        return FileIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileIO):
        """
        Dynamic initializer for FileIO.
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

    @staticmethod
    @overload
    def readBytes(arg0: 'Path') -> List[int]:
        """public static byte[] dev.ultreon.quantum.api.FileIO.readBytes(java.nio.file.Path) throws java.io.IOException"""
        return List[int].__wrap(__FileIO.readBytes(arg0))

    @staticmethod
    @overload
    def writeBytes(arg0: 'Path', arg1: bytes):
        """public static void dev.ultreon.quantum.api.FileIO.writeBytes(java.nio.file.Path,byte[])"""
        __FileIO.writeBytes(arg0, bytes)

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence)"""
        __FileIO.writeString(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence', arg2: 'Charset'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence,java.nio.charset.Charset)"""
        __FileIO.writeString(arg0, arg1, arg2)

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

    @staticmethod
    @overload
    def readString(arg0: 'Path') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path) throws java.io.IOException"""
        return str.__wrap(__FileIO.readString(arg0))

    @staticmethod
    @overload
    def readString(arg0: 'Path', arg1: 'Charset') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path,java.nio.charset.Charset) throws java.io.IOException"""
        return str.__wrap(__FileIO.readString(arg0, arg1))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.api.FileIO
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.charset.Charset as Charset
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.file.Path as Path
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.FileIO as __FileIO
__FileIO = __FileIO
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FileIO():
    """dev.ultreon.quantum.api.FileIO"""
 
    @staticmethod
    def __wrap(java_value: __FileIO) -> 'FileIO':
        return FileIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileIO):
        """
        Dynamic initializer for FileIO.
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

    @staticmethod
    @overload
    def readBytes(arg0: 'Path') -> List[int]:
        """public static byte[] dev.ultreon.quantum.api.FileIO.readBytes(java.nio.file.Path) throws java.io.IOException"""
        return List[int].__wrap(__FileIO.readBytes(arg0))

    @staticmethod
    @overload
    def writeBytes(arg0: 'Path', arg1: bytes):
        """public static void dev.ultreon.quantum.api.FileIO.writeBytes(java.nio.file.Path,byte[])"""
        __FileIO.writeBytes(arg0, bytes)

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence)"""
        __FileIO.writeString(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def writeString(arg0: 'Path', arg1: 'CharSequence', arg2: 'Charset'):
        """public static void dev.ultreon.quantum.api.FileIO.writeString(java.nio.file.Path,java.lang.CharSequence,java.nio.charset.Charset)"""
        __FileIO.writeString(arg0, arg1, arg2)

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

    @staticmethod
    @overload
    def readString(arg0: 'Path') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path) throws java.io.IOException"""
        return str.__wrap(__FileIO.readString(arg0))

    @staticmethod
    @overload
    def readString(arg0: 'Path', arg1: 'Charset') -> str:
        """public static java.lang.String dev.ultreon.quantum.api.FileIO.readString(java.nio.file.Path,java.nio.charset.Charset) throws java.io.IOException"""
        return str.__wrap(__FileIO.readString(arg0, arg1))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.api.FileIO