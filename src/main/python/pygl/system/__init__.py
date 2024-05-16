from __future__ import annotations
from overload import overload


 
import org.lwjgl.system.Pointer as __Pointer
__Pointer = __Pointer
from abc import abstractmethod, ABC
 
class Pointer(ABC):
    """org.lwjgl.system.Pointer"""
 
    @staticmethod
    def __wrap(java_value: __Pointer) -> 'Pointer':
        return Pointer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pointer):
        """
        Dynamic initializer for Pointer.
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
    def address(self, ):
        """public abstract long org.lwjgl.system.Pointer.address()"""
        pass

 
 
 
# CLASS: org.lwjgl.system.Pointer
import org.lwjgl.system.Pointer as __Pointer
__Pointer = __Pointer
from abc import abstractmethod, ABC
 
class Pointer(ABC):
    """org.lwjgl.system.Pointer"""
 
    @staticmethod
    def __wrap(java_value: __Pointer) -> 'Pointer':
        return Pointer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pointer):
        """
        Dynamic initializer for Pointer.
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
    def address(self, ):
        """public abstract long org.lwjgl.system.Pointer.address()"""
        pass

 
 
 
# CLASS: org.lwjgl.system.Pointer 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocator
import org.lwjgl.system.MemoryUtil as __MemoryUtil_MemoryAllocator
__MemoryAllocator = __MemoryUtil_MemoryAllocator.MemoryAllocator
from abc import abstractmethod, ABC
 
class MemoryAllocator(ABC):
    """org.lwjgl.system.MemoryUtil.MemoryAllocator"""
 
    @staticmethod
    def __wrap(java_value: __MemoryAllocator) -> 'MemoryAllocator':
        return MemoryAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryAllocator):
        """
        Dynamic initializer for MemoryAllocator.
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
    def getAlignedFree(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getAlignedFree()"""
        pass

    @abstractmethod
    def getAlignedAlloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getAlignedAlloc()"""
        pass

    @abstractmethod
    def getCalloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getCalloc()"""
        pass

    @abstractmethod
    def realloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.realloc(long,long)"""
        pass

    @abstractmethod
    def getMalloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getMalloc()"""
        pass

    @abstractmethod
    def malloc(self, arg0: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.malloc(long)"""
        pass

    @abstractmethod
    def calloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.calloc(long,long)"""
        pass

    @abstractmethod
    def aligned_alloc(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.aligned_alloc(long,long)"""
        pass

    @abstractmethod
    def aligned_free(self, arg0: int):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocator.aligned_free(long)"""
        pass

    @abstractmethod
    def getRealloc(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getRealloc()"""
        pass

    @abstractmethod
    def free(self, arg0: int):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocator.free(long)"""
        pass

    @abstractmethod
    def getFree(self, ):
        """public abstract long org.lwjgl.system.MemoryUtil$MemoryAllocator.getFree()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Checks
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

import java.nio.IntBuffer as IntBuffer
from builtins import type
from builtins import float
import org.lwjgl.system.Checks as __Checks
__Checks = __Checks
import java.nio.LongBuffer as LongBuffer
from builtins import object
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class Checks():
    """org.lwjgl.system.Checks"""
 
    @staticmethod
    def __wrap(java_value: __Checks) -> 'Checks':
        return Checks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Checks):
        """
        Dynamic initializer for Checks.
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
 
    @staticmethod
    @overload
    def check(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.nio.Buffer,int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'float', arg1: int):
        """public static void org.lwjgl.system.Checks.check(float[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(org.lwjgl.PointerBuffer)"""
        __Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.IntBuffer,int)"""
        __Checks.checkNTSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkFunctions(*arg0: int) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(long...)"""
        return bool.__wrap(__Checks.checkFunctions(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'short', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(short[],int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkGT(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkGT(org.lwjgl.system.CustomBuffer<?>,int)"""
        __Checks.checkGT(arg0, __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def check(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(org.lwjgl.system.CustomBuffer<?>,long)"""
        __Checks.check(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'float'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(float[])"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def remainingSafe(arg0: 'CustomBuffer') -> int:
        """public static int org.lwjgl.system.Checks.remainingSafe(org.lwjgl.system.CustomBuffer<?>)"""
        return int.__wrap(__Checks.remainingSafe(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'float', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(float[],int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'int'):
        """public static void org.lwjgl.system.Checks.checkNT(int[])"""
        __Checks.checkNT(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def check(arg0: bytes, arg1: int):
        """public static void org.lwjgl.system.Checks.check(byte[],int)"""
        __Checks.check(bytes, __int.valueOf(arg1))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'short') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(short[])"""
        return int.__wrap(__Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def remainingSafe(arg0: 'Buffer') -> int:
        """public static int org.lwjgl.system.Checks.remainingSafe(java.nio.Buffer)"""
        return int.__wrap(__Checks.remainingSafe(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(java.nio.Buffer,long)"""
        __Checks.checkSafe(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'long') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(long[])"""
        return int.__wrap(__Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def checkSafe(arg0: 'double', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(double[],int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def check(arg0: 'double', arg1: int):
        """public static void org.lwjgl.system.Checks.check(double[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.FloatBuffer)"""
        __Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkSafe(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(org.lwjgl.system.CustomBuffer<?>,long)"""
        __Checks.checkSafe(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(int[],int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProviderLocal', arg1: int, arg2: 'PointerBuffer', arg3: 'int', *arg4: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProviderLocal,long,org.lwjgl.PointerBuffer,int[],java.lang.String...)"""
        return bool.__wrap(__Checks.checkFunctions(arg0, __long.valueOf(arg1), arg2, arg3, arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def check(arg0: 'CharSequence', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.lang.CharSequence,int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProvider', arg1: 'long', arg2: 'int', *arg3: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProvider,long[],int[],java.lang.String...)"""
        return bool.__wrap(__Checks.checkFunctions(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'PointerBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(org.lwjgl.PointerBuffer)"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkGT(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkGT(java.nio.Buffer,int)"""
        __Checks.checkGT(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'Object', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.lang.Object[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'FloatBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.FloatBuffer)"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def check(arg0: 'long', arg1: int):
        """public static void org.lwjgl.system.Checks.check(long[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.IntBuffer,int)"""
        __Checks.checkNT(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.IntBuffer)"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkSafe(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(org.lwjgl.system.CustomBuffer<?>,int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def reportMissing(arg0: str, arg1: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.reportMissing(java.lang.String,java.lang.String)"""
        return bool.__wrap(__Checks.reportMissing(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def checkNT(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.LongBuffer)"""
        __Checks.checkNT(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def lengthSafe(arg0: 'int') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(int[])"""
        return int.__wrap(__Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def check(arg0: 'CustomBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(org.lwjgl.system.CustomBuffer<?>,int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'IntBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT(java.nio.IntBuffer)"""
        __Checks.checkNT(arg0)

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'long'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(long[])"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'int'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(int[])"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkSafe(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(java.nio.Buffer,int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'PointerBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(org.lwjgl.PointerBuffer,long)"""
        __Checks.checkNT(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.Checks.check(int,int)"""
        return int.__wrap(__Checks.check(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def check(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.check(int[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT1(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT1(java.nio.ByteBuffer)"""
        __Checks.checkNT1(arg0)

    @staticmethod
    @overload
    def lengthSafe(arg0: 'double') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(double[])"""
        return int.__wrap(__Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def checkFunctions(arg0: 'FunctionProvider', arg1: 'PointerBuffer', arg2: 'int', *arg3: str) -> bool:
        """public static boolean org.lwjgl.system.Checks.checkFunctions(org.lwjgl.system.FunctionProvider,org.lwjgl.PointerBuffer,int[],java.lang.String...)"""
        return bool.__wrap(__Checks.checkFunctions(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def checkNT1Safe(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT1Safe(java.nio.ByteBuffer)"""
        __Checks.checkNT1Safe(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'PointerBuffer', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(org.lwjgl.PointerBuffer,long)"""
        __Checks.checkNTSafe(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT2(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT2(java.nio.ByteBuffer)"""
        __Checks.checkNT2(arg0)

    @staticmethod
    @overload
    def check(arg0: int) -> int:
        """public static long org.lwjgl.system.Checks.check(long)"""
        return int.__wrap(__Checks.check(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def check(arg0: 'short', arg1: int):
        """public static void org.lwjgl.system.Checks.check(short[],int)"""
        __Checks.check(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkSafe(arg0: 'long', arg1: int):
        """public static void org.lwjgl.system.Checks.checkSafe(long[],int)"""
        __Checks.checkSafe(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def check(arg0: 'Buffer', arg1: int):
        """public static void org.lwjgl.system.Checks.check(java.nio.Buffer,long)"""
        __Checks.check(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def checkNT(arg0: 'long'):
        """public static void org.lwjgl.system.Checks.checkNT(long[])"""
        __Checks.checkNT(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def checkNT2Safe(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.Checks.checkNT2Safe(java.nio.ByteBuffer)"""
        __Checks.checkNT2Safe(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def checkNT(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNT(int[],int)"""
        __Checks.checkNT(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'LongBuffer'):
        """public static void org.lwjgl.system.Checks.checkNTSafe(java.nio.LongBuffer)"""
        __Checks.checkNTSafe(arg0)

    @staticmethod
    @overload
    def checkNT(arg0: 'float'):
        """public static void org.lwjgl.system.Checks.checkNT(float[])"""
        __Checks.checkNT(arg0)

    @staticmethod
    @overload
    def lengthSafe(arg0: 'float') -> int:
        """public static int org.lwjgl.system.Checks.lengthSafe(float[])"""
        return int.__wrap(__Checks.lengthSafe(arg0))

    @staticmethod
    @overload
    def checkNTSafe(arg0: 'int', arg1: int):
        """public static void org.lwjgl.system.Checks.checkNTSafe(int[],int)"""
        __Checks.checkNTSafe(arg0, __int.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.Platform$Architecture
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import org.lwjgl.system.Platform as __Platform_Architecture
__Architecture = __Platform_Architecture.Architecture
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Architecture(__Enum, Enum):
    """org.lwjgl.system.Platform.Architecture"""
 
    @staticmethod
    def __wrap(java_value: __Architecture) -> 'Architecture':
        return Architecture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Architecture):
        """
        Dynamic initializer for Architecture.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def valueOf(arg0: str) -> 'Architecture':
        """public static org.lwjgl.system.Platform$Architecture org.lwjgl.system.Platform$Architecture.valueOf(java.lang.String)"""
        return Architecture.__wrap(__Architecture.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['Architecture']:
        """public static org.lwjgl.system.Platform$Architecture[] org.lwjgl.system.Platform$Architecture.values()"""
        return List[Architecture].__wrap(__Architecture.values())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.lwjgl.system.ThreadLocalUtil
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.ThreadLocalUtil as __ThreadLocalUtil
__ThreadLocalUtil = __ThreadLocalUtil
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import int
 
class ThreadLocalUtil():
    """org.lwjgl.system.ThreadLocalUtil"""
 
    @staticmethod
    def __wrap(java_value: __ThreadLocalUtil) -> 'ThreadLocalUtil':
        return ThreadLocalUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadLocalUtil):
        """
        Dynamic initializer for ThreadLocalUtil.
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

    @staticmethod
    @overload
    def setFunctionMissingAddresses(arg0: int):
        """public static void org.lwjgl.system.ThreadLocalUtil.setFunctionMissingAddresses(int)"""
        __ThreadLocalUtil.setFunctionMissingAddresses(__int.valueOf(arg0))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def setupEnvData() -> int:
        """public static long org.lwjgl.system.ThreadLocalUtil.setupEnvData()"""
        return int.__wrap(__ThreadLocalUtil.setupEnvData())

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
    def setupAddressBuffer(arg0: 'PointerBuffer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.ThreadLocalUtil.setupAddressBuffer(org.lwjgl.PointerBuffer)"""
        return pygl.PointerBuffer.__wrap(__ThreadLocalUtil.setupAddressBuffer(arg0))

    @staticmethod
    @overload
    def areCapabilitiesDifferent(arg0: 'PointerBuffer', arg1: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.system.ThreadLocalUtil.areCapabilitiesDifferent(org.lwjgl.PointerBuffer,org.lwjgl.PointerBuffer)"""
        return bool.__wrap(__ThreadLocalUtil.areCapabilitiesDifferent(arg0, arg1))

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

    @staticmethod
    @overload
    def setCapabilities(arg0: int):
        """public static void org.lwjgl.system.ThreadLocalUtil.setCapabilities(long)"""
        __ThreadLocalUtil.setCapabilities(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.system.Struct$Member
from builtins import str
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct_Member
__Member = __Struct_Member.Member
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
 
class Member():
    """org.lwjgl.system.Struct.Member"""
 
    @staticmethod
    def __wrap(java_value: __Member) -> 'Member':
        return Member(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Member):
        """
        Dynamic initializer for Member.
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
    def getAlignment(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment(int)"""
        return int.__wrap(super(__Member, self).getAlignment(__int.valueOf(arg0)))

    @overload
    def getSize(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getSize()"""
        return int.__wrap(super(Member, self).getSize())

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
    def getAlignment(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment()"""
        return int.__wrap(super(Member, self).getAlignment())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.system.Struct
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Struct(ABC, __Default, Default):
    """org.lwjgl.system.Struct"""
 
    @staticmethod
    def __wrap(java_value: __Struct) -> 'Struct':
        return Struct(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Struct):
        """
        Dynamic initializer for Struct.
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

    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

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

    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(Struct, self).free()

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

    @abstractmethod
    def sizeof(self, ):
        """public abstract int org.lwjgl.system.Struct.sizeof()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(Default, self).address())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.Library
import java.util.function.Supplier as Supplier
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.function.Consumer as Consumer
import org.lwjgl.system.Library as __Library
__Library = __Library
import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Library():
    """org.lwjgl.system.Library"""
 
    @staticmethod
    def __wrap(java_value: __Library) -> 'Library':
        return Library(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Library):
        """
        Dynamic initializer for Library.
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

    @staticmethod
    @overload
    def loadNative(arg0: str, arg1: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.String,java.lang.String)"""
        return SharedLibrary.__wrap(__Library.loadNative(arg0, arg1))

    @staticmethod
    @overload
    def loadSystem(arg0: str, arg1: str):
        """public static void org.lwjgl.system.Library.loadSystem(java.lang.String,java.lang.String) throws java.lang.UnsatisfiedLinkError"""
        __Library.loadSystem(arg0, arg1)

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
    def loadNative(arg0: 'Class', arg1: str, arg2: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,java.lang.String)"""
        return SharedLibrary.__wrap(__Library.loadNative(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: 'Configuration', *arg3: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.lang.String...)"""
        return SharedLibrary.__wrap(__Library.loadNative(arg0, arg1, arg2, arg3))

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
    def loadNative(arg0: 'Class', arg1: str, arg2: str, arg3: bool) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,java.lang.String,boolean)"""
        return SharedLibrary.__wrap(__Library.loadNative(arg0, arg1, arg2, __boolean.valueOf(arg3)))

        @staticmethod
        @overload
        def initialize():
            """public static void org.lwjgl.system.Library.initialize()"""
            __Library.initialize()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def loadNative(arg0: 'Class', arg1: str, arg2: 'Configuration', arg3: 'Supplier', *arg4: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.Library.loadNative(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.util.function.Supplier<org.lwjgl.system.SharedLibrary>,java.lang.String...)"""
        return SharedLibrary.__wrap(__Library.loadNative(arg0, arg1, arg2, arg3, arg4))

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
    def loadSystem(arg0: 'Consumer', arg1: 'Consumer', arg2: 'Class', arg3: str, arg4: str):
        """public static void org.lwjgl.system.Library.loadSystem(java.util.function.Consumer<java.lang.String>,java.util.function.Consumer<java.lang.String>,java.lang.Class<?>,java.lang.String,java.lang.String) throws java.lang.UnsatisfiedLinkError"""
        __Library.loadSystem(arg0, arg1, arg2, arg3, arg4) 
 
 
# CLASS: org.lwjgl.system.LibraryResource
from builtins import str
import java.util.function.Supplier as Supplier
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.nio.file.Path as Path
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.lwjgl.system.LibraryResource as __LibraryResource
__LibraryResource = __LibraryResource
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LibraryResource():
    """org.lwjgl.system.LibraryResource"""
 
    @staticmethod
    def __wrap(java_value: __LibraryResource) -> 'LibraryResource':
        return LibraryResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibraryResource):
        """
        Dynamic initializer for LibraryResource.
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

    @staticmethod
    @overload
    def load(arg0: str, arg1: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.String,java.lang.String)"""
        return Path.__wrap(__LibraryResource.load(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: str, arg3: bool) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,java.lang.String,boolean)"""
        return Path.__wrap(__LibraryResource.load(arg0, arg1, arg2, __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: 'Configuration', *arg3: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.lang.String...)"""
        return Path.__wrap(__LibraryResource.load(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: 'Configuration', arg3: 'Supplier', *arg4: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,org.lwjgl.system.Configuration<java.lang.String>,java.util.function.Supplier<java.nio.file.Path>,java.lang.String...)"""
        return Path.__wrap(__LibraryResource.load(arg0, arg1, arg2, arg3, arg4))

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

    @staticmethod
    @overload
    def load(arg0: 'Class', arg1: str, arg2: str) -> 'Path':
        """public static java.nio.file.Path org.lwjgl.system.LibraryResource.load(java.lang.Class<?>,java.lang.String,java.lang.String)"""
        return Path.__wrap(__LibraryResource.load(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.system.SharedLibrary$Default
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
from abc import abstractmethod, ABC
import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
import org.lwjgl.system.SharedLibrary as __SharedLibrary_Default
__Default = __SharedLibrary_Default.Default
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class Default(ABC, __Default, Default, __SharedLibrary, SharedLibrary):
    """org.lwjgl.system.SharedLibrary.Default"""
 
    @staticmethod
    def __wrap(java_value: __Default) -> 'Default':
        return Default(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Default):
        """
        Dynamic initializer for Default.
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str.__wrap(super(Default, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(Default, self).address())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.MemoryUtil
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.MemoryUtil as __MemoryUtil
__MemoryUtil = __MemoryUtil
import java.lang.Boolean as __boolean
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.CLongBuffer as __CLongBuffer
__CLongBuffer = __CLongBuffer
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import org.lwjgl.system.MemoryUtil as __MemoryUtil_MemoryAllocator
__MemoryAllocator = __MemoryUtil_MemoryAllocator.MemoryAllocator
import java.lang.Short as __short
import java.nio.CharBuffer as CharBuffer
import java.lang.Double as __double
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import java.nio.CharBuffer as __CharBuffer
__CharBuffer = __CharBuffer
from builtins import int
 
class MemoryUtil():
    """org.lwjgl.system.MemoryUtil"""
 
    @staticmethod
    def __wrap(java_value: __MemoryUtil) -> 'MemoryUtil':
        return MemoryUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryUtil):
        """
        Dynamic initializer for MemoryUtil.
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
 
    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memUTF16(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memAllocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memAllocCLong(int)"""
        return pygl.CLongBuffer.__wrap(__MemoryUtil.memAllocCLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemAlignedAlloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlignedAlloc(long,long)"""
        return int.__wrap(__MemoryUtil.nmemAlignedAlloc(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'LongBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.LongBuffer)"""
        return LongBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'LongBuffer', arg1: int, arg2: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.LongBuffer,int,int)"""
        return LongBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memSlice(arg0: 'ByteBuffer', arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ByteBuffer,int,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer,int,int)"""
        return str.__wrap(__MemoryUtil.memASCII(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF8(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memUTF16Safe(arg0))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int.__wrap(__MemoryUtil.memUTF16(arg0, __boolean.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'FloatBuffer', arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.FloatBuffer,int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT2Safe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2Safe(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT2Safe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memASCIISafe(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'LongBuffer', arg1: 'LongBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.LongBuffer,java.nio.LongBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memSet(arg0: 'CustomBuffer', arg1: int):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.system.MemoryUtil.memSet(T,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memPutByte(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutByte(long,byte)"""
        __MemoryUtil.memPutByte(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def memAllocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memAllocPointer(int)"""
        return pygl.PointerBuffer.__wrap(__MemoryUtil.memAllocPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemFree(arg0: int):
        """public static void org.lwjgl.system.MemoryUtil.nmemFree(long)"""
        __MemoryUtil.nmemFree(__long.valueOf(arg0))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(long)"""
        return str.__wrap(__MemoryUtil.memUTF8Safe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'LongBuffer', arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.LongBuffer,int)"""
        return LongBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'ShortBuffer', arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.ShortBuffer,int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memLengthNT2(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthNT2(java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memLengthNT2(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'IntBuffer', arg1: 'IntBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.IntBuffer,java.nio.IntBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memUTF16(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer,int,int)"""
        return str.__wrap(__MemoryUtil.memUTF16(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'LongBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.LongBuffer)"""
        return LongBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memLengthNT1(arg0: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthNT1(java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memLengthNT1(arg0))

    @staticmethod
    @overload
    def memSet(arg0: 'LongBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.LongBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memPutFloat(arg0: int, arg1: float):
        """public static void org.lwjgl.system.MemoryUtil.memPutFloat(long,float)"""
        __MemoryUtil.memPutFloat(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'IntBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.IntBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memASCII(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memCallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memCallocLong(int)"""
        return LongBuffer.__wrap(__MemoryUtil.memCallocLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'Pointer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(org.lwjgl.system.Pointer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memASCII(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memPutShort(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutShort(long,short)"""
        __MemoryUtil.memPutShort(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def memASCII(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(long)"""
        return str.__wrap(__MemoryUtil.memASCII(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferNT1(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT1(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getAllocator() -> 'MemoryAllocator':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocator org.lwjgl.system.MemoryUtil.getAllocator()"""
        return MemoryAllocator.__wrap(__MemoryUtil.getAllocator())

    @staticmethod
    @overload
    def memGetDouble(arg0: int) -> float:
        """public static double org.lwjgl.system.MemoryUtil.memGetDouble(long)"""
        return float.__wrap(__MemoryUtil.memGetDouble(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF16(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'IntBuffer', arg1: int, arg2: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.IntBuffer,int,int)"""
        return IntBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def memByteBufferNT2Safe(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2Safe(long)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT2Safe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memSlice(arg0: 'FloatBuffer', arg1: int, arg2: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.FloatBuffer,int,int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'CharBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.CharBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memUTF8Safe(arg0))

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCIISafe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memASCIISafe(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memUTF8(arg0))

    @staticmethod
    @overload
    def memRealloc(arg0: 'IntBuffer', arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.IntBuffer,int)"""
        return IntBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memShortBuffer(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memShortBuffer(long,int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memShortBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(long)"""
        return str.__wrap(__MemoryUtil.memUTF8(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memGlobalRefToObject(arg0: int) -> object:
        """public static native <T> T org.lwjgl.system.MemoryUtil.memGlobalRefToObject(long)"""
        return object.__wrap(__MemoryUtil.memGlobalRefToObject(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memPointerBufferSafe(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memPointerBufferSafe(long,int)"""
        return pygl.PointerBuffer.__wrap(__MemoryUtil.memPointerBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'Struct') -> 'ByteBuffer':
        """public static <T extends org.lwjgl.system.Struct<T>> java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(T)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def memAllocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memAllocInt(int)"""
        return IntBuffer.__wrap(__MemoryUtil.memAllocInt(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress0(arg0: 'Buffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress0(java.nio.Buffer)"""
        return int.__wrap(__MemoryUtil.memAddress0(arg0))

    @staticmethod
    @overload
    def memFloatBufferSafe(arg0: int, arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memFloatBufferSafe(long,int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memFloatBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memCallocShort(int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memCallocShort(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferNT1(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1(long)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CharBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.CharBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memLongBuffer(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memLongBuffer(long,int)"""
        return LongBuffer.__wrap(__MemoryUtil.memLongBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSet(arg0: 'ShortBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.ShortBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.LongBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memGetAddress(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetAddress(long)"""
        return int.__wrap(__MemoryUtil.memGetAddress(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer,int)"""
        return str.__wrap(__MemoryUtil.memUTF16(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memFree(arg0: 'CustomBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memFree(org.lwjgl.system.CustomBuffer<?>)"""
        __MemoryUtil.memFree(arg0)

    @staticmethod
    @overload
    def memDuplicate(arg0: 'FloatBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.FloatBuffer)"""
        return FloatBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memGetLong(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetLong(long)"""
        return int.__wrap(__MemoryUtil.memGetLong(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memCopy(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(long,long,long)"""
        __MemoryUtil.memCopy(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.ShortBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memAlloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memAlloc(int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memAlloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'CharBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.CharBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memAllocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memAllocLong(int)"""
        return LongBuffer.__wrap(__MemoryUtil.memAllocLong(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def memPointerBuffer(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memPointerBuffer(long,int)"""
        return pygl.PointerBuffer.__wrap(__MemoryUtil.memPointerBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memASCII(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.DoubleBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memAddress(arg0: 'FloatBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.FloatBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCIISafe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(long,int)"""
        return str.__wrap(__MemoryUtil.memASCIISafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memGetCLong(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memGetCLong(long)"""
        return int.__wrap(__MemoryUtil.memGetCLong(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memSlice(arg0: 'CharBuffer', arg1: int, arg2: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.CharBuffer,int,int)"""
        return CharBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memSlice(arg0: 'IntBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.IntBuffer)"""
        return IntBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memCalloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memCalloc(int,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memCalloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'FloatBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.FloatBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'CustomBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(org.lwjgl.system.CustomBuffer<?>)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memASCIISafe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCIISafe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memASCIISafe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8Safe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF8Safe(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF8(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memAllocShort(int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memAllocShort(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'LongBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.LongBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def nmemRealloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemRealloc(long,long)"""
        return int.__wrap(__MemoryUtil.nmemRealloc(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def memCharBuffer(arg0: int, arg1: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memCharBuffer(long,int)"""
        return CharBuffer.__wrap(__MemoryUtil.memCharBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAllocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memAllocFloat(int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memAllocFloat(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memCopy(arg0: 'Struct', arg1: 'Struct'):
        """public static <T extends org.lwjgl.system.Struct<T>> void org.lwjgl.system.MemoryUtil.memCopy(T,T)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def nmemAlignedFree(arg0: int):
        """public static void org.lwjgl.system.MemoryUtil.nmemAlignedFree(long)"""
        __MemoryUtil.nmemAlignedFree(__long.valueOf(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.IntBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memCopy(arg0: 'FloatBuffer', arg1: 'FloatBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memGetInt(arg0: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memGetInt(long)"""
        return int.__wrap(__MemoryUtil.memGetInt(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF16(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(long)"""
        return str.__wrap(__MemoryUtil.memUTF16(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memCalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memCalloc(int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memCalloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CustomBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(org.lwjgl.system.CustomBuffer<?>,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'IntBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.IntBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CharBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.CharBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'ShortBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.ShortBuffer)"""
        return ShortBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memAddress(arg0: 'DoubleBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.DoubleBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memShortBufferSafe(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memShortBufferSafe(long,int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memShortBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'ShortBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ShortBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memGetBoolean(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MemoryUtil.memGetBoolean(long)"""
        return bool.__wrap(__MemoryUtil.memGetBoolean(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memFloatBuffer(arg0: int, arg1: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memFloatBuffer(long,int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memFloatBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSlice(arg0: 'CustomBuffer', arg1: int, arg2: int) -> 'CustomBuffer':
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> T org.lwjgl.system.MemoryUtil.memSlice(T,int,int)"""
        return CustomBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memSlice(arg0: 'DoubleBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.DoubleBuffer)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def nmemReallocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemReallocChecked(long,long)"""
        return int.__wrap(__MemoryUtil.nmemReallocChecked(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT2(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT2(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF16Safe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'ByteBuffer', arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.ByteBuffer,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT2(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT2(long)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemAlignedAllocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlignedAllocChecked(long,long)"""
        return int.__wrap(__MemoryUtil.nmemAlignedAllocChecked(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'DoubleBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.DoubleBuffer)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memAddress(arg0: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.FloatBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(long,int)"""
        return str.__wrap(__MemoryUtil.memUTF8(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memGetShort(arg0: int) -> int:
        """public static short org.lwjgl.system.MemoryUtil.memGetShort(long)"""
        return int.__wrap(__MemoryUtil.memGetShort(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memGetByte(arg0: int) -> int:
        """public static byte org.lwjgl.system.MemoryUtil.memGetByte(long)"""
        return int.__wrap(__MemoryUtil.memGetByte(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memByteBufferSafe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferSafe(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCopy(arg0: 'ByteBuffer', arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memRealloc(arg0: 'PointerBuffer', arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memRealloc(org.lwjgl.PointerBuffer,int)"""
        return pygl.PointerBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memDoubleBufferSafe(arg0: int, arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDoubleBufferSafe(long,int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memDoubleBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memASCII(arg0))

    @staticmethod
    @overload
    def memCharBufferSafe(arg0: int, arg1: int) -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memCharBufferSafe(long,int)"""
        return CharBuffer.__wrap(__MemoryUtil.memCharBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAlignedAlloc(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memAlignedAlloc(int,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memAlignedAlloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memASCII(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(long,int)"""
        return str.__wrap(__MemoryUtil.memASCII(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCopy(arg0: 'CustomBuffer', arg1: 'CustomBuffer'):
        """public static <T extends org.lwjgl.system.CustomBuffer<T>> void org.lwjgl.system.MemoryUtil.memCopy(T,T)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memSlice(arg0: 'DoubleBuffer', arg1: int, arg2: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.DoubleBuffer,int,int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def memPutCLong(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutCLong(long,long)"""
        __MemoryUtil.memPutCLong(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nmemAlloc(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAlloc(long)"""
        return int.__wrap(__MemoryUtil.nmemAlloc(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemCallocChecked(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemCallocChecked(long,long)"""
        return int.__wrap(__MemoryUtil.nmemCallocChecked(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def memCopy(arg0: 'ShortBuffer', arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.ShortBuffer,java.nio.ShortBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memSet(arg0: 'IntBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.IntBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(long,int)"""
        return str.__wrap(__MemoryUtil.memUTF16Safe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16Safe(long)"""
        return str.__wrap(__MemoryUtil.memUTF16Safe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memLongBufferSafe(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryUtil.memLongBufferSafe(long,int)"""
        return LongBuffer.__wrap(__MemoryUtil.memLongBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memLengthASCII(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthASCII(java.lang.CharSequence,boolean)"""
        return int.__wrap(__MemoryUtil.memLengthASCII(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'LongBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.LongBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memCallocFloat(int)"""
        return FloatBuffer.__wrap(__MemoryUtil.memCallocFloat(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'CustomBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(org.lwjgl.system.CustomBuffer<?>)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer', arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer,int,int)"""
        return str.__wrap(__MemoryUtil.memUTF8(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memSet(arg0: 'CharBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.CharBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memSlice(arg0: 'CharBuffer') -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.CharBuffer)"""
        return CharBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memCallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryUtil.memCallocPointer(int)"""
        return pygl.PointerBuffer.__wrap(__MemoryUtil.memCallocPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF8Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF8Safe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memFree(arg0: 'Buffer'):
        """public static void org.lwjgl.system.MemoryUtil.memFree(java.nio.Buffer)"""
        __MemoryUtil.memFree(arg0)

    @staticmethod
    @overload
    def memPutDouble(arg0: int, arg1: float):
        """public static void org.lwjgl.system.MemoryUtil.memPutDouble(long,double)"""
        __MemoryUtil.memPutDouble(__long.valueOf(arg0), __double.valueOf(arg1))

    @staticmethod
    @overload
    def memIntBuffer(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memIntBuffer(long,int)"""
        return IntBuffer.__wrap(__MemoryUtil.memIntBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8Safe(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8Safe(long,int)"""
        return str.__wrap(__MemoryUtil.memUTF8Safe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCopy(arg0: 'CharBuffer', arg1: 'CharBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.CharBuffer,java.nio.CharBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memCLongBuffer(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCLongBuffer(long,int)"""
        return pygl.CLongBuffer.__wrap(__MemoryUtil.memCLongBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'ShortBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.ShortBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memAddressSafe(arg0: 'FloatBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddressSafe(java.nio.FloatBuffer)"""
        return int.__wrap(__MemoryUtil.memAddressSafe(arg0))

    @staticmethod
    @overload
    def memSlice(arg0: 'ShortBuffer', arg1: int, arg2: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ShortBuffer,int,int)"""
        return ShortBuffer.__wrap(__MemoryUtil.memSlice(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def memIntBufferSafe(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memIntBufferSafe(long,int)"""
        return IntBuffer.__wrap(__MemoryUtil.memIntBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'DoubleBuffer', arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memRealloc(java.nio.DoubleBuffer,int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memSet(arg0: 'Struct', arg1: int):
        """public static <T extends org.lwjgl.system.Struct<T>> void org.lwjgl.system.MemoryUtil.memSet(T,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memUTF16(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF16(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF16Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memUTF16Safe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryUtil.memUTF16Safe(arg0))

    @staticmethod
    @overload
    def memSet(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(long,int,long)"""
        __MemoryUtil.memSet(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def memDuplicate(arg0: 'CharBuffer') -> 'CharBuffer':
        """public static java.nio.CharBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.CharBuffer)"""
        return CharBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCII(java.nio.ByteBuffer,int)"""
        return str.__wrap(__MemoryUtil.memASCII(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ByteBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCopy(arg0: 'DoubleBuffer', arg1: 'DoubleBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memCopy(java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        __MemoryUtil.memCopy(arg0, arg1)

    @staticmethod
    @overload
    def memDuplicate(arg0: 'IntBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memDuplicate(java.nio.IntBuffer)"""
        return IntBuffer.__wrap(__MemoryUtil.memDuplicate(arg0))

    @staticmethod
    @overload
    def memASCII(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memASCII(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int.__wrap(__MemoryUtil.memASCII(arg0, __boolean.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def memLengthUTF16(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthUTF16(java.lang.CharSequence,boolean)"""
        return int.__wrap(__MemoryUtil.memLengthUTF16(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memLengthUTF8(arg0: 'CharSequence', arg1: bool) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memLengthUTF8(java.lang.CharSequence,boolean)"""
        return int.__wrap(__MemoryUtil.memLengthUTF8(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def memByteBufferNT1Safe(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1Safe(long,int)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT1Safe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memCallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCallocCLong(int)"""
        return pygl.CLongBuffer.__wrap(__MemoryUtil.memCallocCLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memReport(arg0: 'MemoryAllocationReport', arg1: 'Aggregate', arg2: bool):
        """public static void org.lwjgl.system.MemoryUtil.memReport(org.lwjgl.system.MemoryUtil$MemoryAllocationReport,org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate,boolean)"""
        __MemoryUtil.memReport(arg0, arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def memAddress(arg0: 'ShortBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.ShortBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def getAllocator(arg0: bool) -> 'MemoryAllocator':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocator org.lwjgl.system.MemoryUtil.getAllocator(boolean)"""
        return MemoryAllocator.__wrap(__MemoryUtil.getAllocator(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemAllocChecked(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemAllocChecked(long)"""
        return int.__wrap(__MemoryUtil.nmemAllocChecked(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean,java.nio.ByteBuffer)"""
        return int.__wrap(__MemoryUtil.memUTF8(arg0, __boolean.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def memASCIISafe(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memASCIISafe(long)"""
        return str.__wrap(__MemoryUtil.memASCIISafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memPutInt(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutInt(long,int)"""
        __MemoryUtil.memPutInt(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def memByteBuffer(arg0: 'DoubleBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBuffer(java.nio.DoubleBuffer)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBuffer(arg0))

    @staticmethod
    @overload
    def memUTF16(arg0: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(java.nio.ByteBuffer)"""
        return str.__wrap(__MemoryUtil.memUTF16(arg0))

    @staticmethod
    @overload
    def memAddress(arg0: 'DoubleBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.DoubleBuffer,int)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'Buffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.Buffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memCallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memCallocDouble(int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memCallocDouble(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmemCalloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryUtil.nmemCalloc(long,long)"""
        return int.__wrap(__MemoryUtil.nmemCalloc(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def memRealloc(arg0: 'CLongBuffer', arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memRealloc(org.lwjgl.CLongBuffer,int)"""
        return pygl.CLongBuffer.__wrap(__MemoryUtil.memRealloc(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memAddress(arg0: 'LongBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.LongBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memSet(arg0: 'ByteBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.ByteBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memCallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryUtil.memCallocInt(int)"""
        return IntBuffer.__wrap(__MemoryUtil.memCallocInt(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memAlignedFree(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.system.MemoryUtil.memAlignedFree(java.nio.ByteBuffer)"""
        __MemoryUtil.memAlignedFree(arg0)

    @staticmethod
    @overload
    def memReport(arg0: 'MemoryAllocationReport'):
        """public static void org.lwjgl.system.MemoryUtil.memReport(org.lwjgl.system.MemoryUtil$MemoryAllocationReport)"""
        __MemoryUtil.memReport(arg0)

    @staticmethod
    @overload
    def memSlice(arg0: 'ShortBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.ShortBuffer)"""
        return ShortBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memGetFloat(arg0: int) -> float:
        """public static float org.lwjgl.system.MemoryUtil.memGetFloat(long)"""
        return float.__wrap(__MemoryUtil.memGetFloat(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memAddress(arg0: 'IntBuffer') -> int:
        """public static long org.lwjgl.system.MemoryUtil.memAddress(java.nio.IntBuffer)"""
        return int.__wrap(__MemoryUtil.memAddress(arg0))

    @staticmethod
    @overload
    def memSet(arg0: 'DoubleBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.DoubleBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memUTF16(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF16(long,int)"""
        return str.__wrap(__MemoryUtil.memUTF16(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memPutAddress(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutAddress(long,long)"""
        __MemoryUtil.memPutAddress(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def memByteBufferNT1Safe(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryUtil.memByteBufferNT1Safe(long)"""
        return ByteBuffer.__wrap(__MemoryUtil.memByteBufferNT1Safe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def memSlice(arg0: 'FloatBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryUtil.memSlice(java.nio.FloatBuffer)"""
        return FloatBuffer.__wrap(__MemoryUtil.memSlice(arg0))

    @staticmethod
    @overload
    def memCLongBufferSafe(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryUtil.memCLongBufferSafe(long,int)"""
        return pygl.CLongBuffer.__wrap(__MemoryUtil.memCLongBufferSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'ByteBuffer', arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.MemoryUtil.memUTF8(java.nio.ByteBuffer,int)"""
        return str.__wrap(__MemoryUtil.memUTF8(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def memAllocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memAllocDouble(int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memAllocDouble(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def memSet(arg0: 'FloatBuffer', arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memSet(java.nio.FloatBuffer,int)"""
        __MemoryUtil.memSet(arg0, __int.valueOf(arg1))

    @staticmethod
    @overload
    def memDoubleBuffer(arg0: int, arg1: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryUtil.memDoubleBuffer(long,int)"""
        return DoubleBuffer.__wrap(__MemoryUtil.memDoubleBuffer(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def memUTF8(arg0: 'CharSequence', arg1: bool, arg2: 'ByteBuffer', arg3: int) -> int:
        """public static int org.lwjgl.system.MemoryUtil.memUTF8(java.lang.CharSequence,boolean,java.nio.ByteBuffer,int)"""
        return int.__wrap(__MemoryUtil.memUTF8(arg0, __boolean.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def memPutLong(arg0: int, arg1: int):
        """public static void org.lwjgl.system.MemoryUtil.memPutLong(long,long)"""
        __MemoryUtil.memPutLong(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.NativeResource
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
from abc import abstractmethod, ABC
 
class NativeResource(ABC, __AutoCloseable, AutoCloseable):
    """org.lwjgl.system.NativeResource"""
 
    @staticmethod
    def __wrap(java_value: __NativeResource) -> 'NativeResource':
        return NativeResource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NativeResource):
        """
        Dynamic initializer for NativeResource.
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
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass 
 
 
# CLASS: org.lwjgl.system.JNI
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import org.lwjgl.system.JNI as __JNI
__JNI = __JNI
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
from builtins import bool
from builtins import int
 
class JNI():
    """org.lwjgl.system.JNI"""
 
    @staticmethod
    def __wrap(java_value: __JNI) -> 'JNI':
        return JNI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JNI):
        """
        Dynamic initializer for JNI.
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
 
    @staticmethod
    @overload
    def invokeCCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCCUV(short,short,short,short,short,int,short,int,byte,long)"""
        __JNI.invokeCCCCCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __int.valueOf(arg5), __short.valueOf(arg6), __int.valueOf(arg7), __byte.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,int,int,float,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __float.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,int[],long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'long', arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long[],long[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int[],long[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPPI(long,int,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,long,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJJJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPJJJJJJV(long,long,long,long,int,long,long,long,long,long)"""
        __JNI.callPPJJJJJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,long,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPS(long,long,long,long)"""
        return int.__wrap(__JNI.callPPPS(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int[],int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), arg1, arg2, arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,int,long,long,long[],long)"""
        return int.__wrap(__JNI.callPJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,long,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPPV(long,int,long,long,long,long,long,long,long)"""
        __JNI.invokePPPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokeZ(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeZ(long)"""
        return bool.__wrap(__JNI.invokeZ(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNPI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,boolean,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPNPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,int[],short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPCPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPCPPV(long,long,short,long,long,long)"""
        __JNI.invokePPCPPV(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(int,int[],long,long)"""
        __JNI.invokePJV(__int.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(float,boolean,long)"""
        __JNI.callV(__float.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,long,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(int,long,long,long)"""
        __JNI.invokePJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,float,long,int,long)"""
        return float.__wrap(__JNI.invokePPF(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'double', arg3: 'double', arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,double[],double[],double[],long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCCCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCCC(short,short,short,short,long)"""
        return int.__wrap(__JNI.invokeCCCCC(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,int,long,long,long,long,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeV(arg0: int):
        """public static native void org.lwjgl.system.JNI.invokeV(long)"""
        __JNI.invokeV(__long.valueOf(arg0))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int[],int[],long[],long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,float,float,float,float,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: float, arg2: float, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,float,float,long)"""
        return float.__wrap(__JNI.invokePF(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJPPP(long,long,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,int,long,int,long,long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,long)"""
        __JNI.callJV(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'double', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPCPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPS(long,short,long,long)"""
        return int.__wrap(__JNI.callPCPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: 'float', arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(float[],float[],long)"""
        __JNI.callPPV(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUV(long,short,short,int,int,int,byte,long)"""
        __JNI.invokePCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __byte.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,long,long,long,long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(long,int,long,long,int,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), arg8, __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int[],long[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCV(short,short,short,short,short,long)"""
        __JNI.invokeCCCCCV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,long[],long,int,long)"""
        return int.__wrap(__JNI.callPJPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long[],long[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,int,int,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __int.valueOf(arg17), __long.valueOf(arg18))

    @staticmethod
    @overload
    def callJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callJJJJV(int,int,long,long,long,long,long)"""
        __JNI.callJJJJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPCV(long,long,int,long,short,long)"""
        __JNI.invokePPPCV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,long[],long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'double', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,double[],short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), arg2, __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int[],long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,int[],long)"""
        return int.__wrap(__JNI.callPPP(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,float[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,int,int,long,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,int,float,float,float,float,float,float,float,float,float,long)"""
        __JNI.callJV(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,long,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: 'short', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(short[],long,long,int,boolean,float,long)"""
        return int.__wrap(__JNI.invokePPPI(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,int,int,long)"""
        return bool.__wrap(__JNI.invokePZ(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJPI(long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPJJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,boolean,int,long,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPNPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNPP(long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPNPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,double[],int[],long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: 'int', arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long[],long,int,long,long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), arg9, arg10, __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'float', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10, __long.valueOf(arg11))

    @staticmethod
    @overload
    def callPP(arg0: 'int', arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int[],long)"""
        return int.__wrap(__JNI.callPP(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,int,long,long)"""
        return int.__wrap(__JNI.invokePJP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long[],long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCI(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCI(float[],short,long)"""
        return int.__wrap(__JNI.invokePCI(arg0, __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: int, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,long,long)"""
        return float.__wrap(__JNI.invokePPF(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'float', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,float[],byte,long)"""
        return int.__wrap(__JNI.invokeCPUI(__short.valueOf(arg0), arg1, __byte.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeUPC(arg0: int, arg1: 'short', arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeUPC(byte,short[],boolean,long)"""
        return int.__wrap(__JNI.invokeUPC(__byte.valueOf(arg0), arg1, __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPJI(long,long,long,long)"""
        return int.__wrap(__JNI.invokePPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCCUJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCCCUJP(short,short,short,byte,int,long,long)"""
        return int.__wrap(__JNI.invokeCCCUJP(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __byte.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,double[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePJJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJJ(long,long,long)"""
        return int.__wrap(__JNI.invokePJJ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJI(long,long,int,long)"""
        return int.__wrap(__JNI.invokePJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,boolean,long)"""
        __JNI.invokeCV(__short.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,float,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPPI(long,long,long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNNPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,int,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,short[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long[],long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJPPI(long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeZ(int,long)"""
        return bool.__wrap(__JNI.invokeZ(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,int,long)"""
        return int.__wrap(__JNI.callJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,float,long)"""
        return int.__wrap(__JNI.callJI(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,double,double,double,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,int,long,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNPN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPN(long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePNPN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeJPPP(int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokeJPPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPSPSPPPPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSPSPPPPPPPS(long,short,long,short,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPSPSPPPPPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(long,long,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPJP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPN(long,long,long)"""
        return int.__wrap(__JNI.invokePPN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNNV(long,long,long,long)"""
        __JNI.invokePNNV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,float[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,boolean,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callCV(int,int,short,long)"""
        __JNI.callCV(__int.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,long)"""
        __JNI.invokeCV(__short.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokeJC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeJC(int,int,long,long)"""
        return int.__wrap(__JNI.invokeJC(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePUP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePUP(long,int,byte,int,boolean,boolean,long)"""
        return int.__wrap(__JNI.invokePUP(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'long', arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long[],int[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,int,long,long,int,long)"""
        __JNI.callPJJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJ(long,long,int,int,long)"""
        return int.__wrap(__JNI.callPJJ(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'double', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,long,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callJJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJJI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,int,int,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCPI(long,short,long,long)"""
        return int.__wrap(__JNI.invokePCPI(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,int,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPI(long,long,long,int,long,float,float,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,long,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,boolean,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,int,int,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,long,long,long,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(int,long,long,int,int,int,int,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,int,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJI(long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPUPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPUPPI(long,long,byte,long,long,long)"""
        return int.__wrap(__JNI.callPPUPPI(__long.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,int,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,byte,long)"""
        __JNI.invokeCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPPPI(long,int,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,long,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int, arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long[],int,int[],long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,int,float,float,long)"""
        return bool.__wrap(__JNI.callZ(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPCPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPCPPPI(long,long,short,long,long,long,long)"""
        return int.__wrap(__JNI.callPPCPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,float[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int[],long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,long,int,int,int,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,boolean,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'double', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,double[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,long[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,int,boolean,long)"""
        return int.__wrap(__JNI.callJI(__long.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePP(arg0: 'double', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(double[],int,long)"""
        return int.__wrap(__JNI.invokePP(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,int,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPNV(long,long,long,long)"""
        __JNI.invokePPNV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,boolean,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __boolean.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,boolean,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5), __double.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'short', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,short[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), arg10, __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callSSSV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callSSSV(short,short,short,long)"""
        __JNI.callSSSV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: 'long', arg6: 'long', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,int,long[],long[],long[],long[],long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPPPI(long,long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.callJJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,int,long,long)"""
        return int.__wrap(__JNI.invokePP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int[],int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,long,long,long,long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int[],int,int[],long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,int,int,long)"""
        return int.__wrap(__JNI.callPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPBPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPBPPP(long,long,byte,long,long,long)"""
        return int.__wrap(__JNI.invokePPBPPP(__long.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def callBBBBV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callBBBBV(byte,byte,byte,byte,long)"""
        __JNI.callBBBBV(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,float,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJV(long,int,long)"""
        __JNI.callJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,int,long,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,int,int,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPF(int,int,long,long)"""
        return float.__wrap(__JNI.callPF(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJI(long,long,long)"""
        return int.__wrap(__JNI.invokePJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,int,int,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPP(long,long,long,long,int,long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int[],boolean,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,boolean,int,long)"""
        return bool.__wrap(__JNI.invokePPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callSSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callSSSSV(int,short,short,short,short,long)"""
        __JNI.callSSSSV(__int.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,boolean,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __short.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeUCV(byte,short,int,long)"""
        __JNI.invokeUCV(__byte.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPSPSPCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPSPSPCS(long,long,long,short,long,short,long,short,long)"""
        return int.__wrap(__JNI.callPPPSPSPCS(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6), __short.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,int,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCUV(long,short,short,short,int,byte,long)"""
        __JNI.invokePCCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __int.valueOf(arg4), __byte.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: 'int', arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int[],long)"""
        return bool.__wrap(__JNI.invokePPZ(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,float,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,long,int,long)"""
        return int.__wrap(__JNI.callPPS(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,int,long)"""
        return int.__wrap(__JNI.callP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,int,float[],float[],long,int,long,int,boolean,long)"""
        __JNI.invokePPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPSS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSS(long,long,short,long)"""
        return int.__wrap(__JNI.callPPSS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,float[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(int,long,long)"""
        __JNI.invokeJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,double[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,float[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int[],long,long)"""
        return int.__wrap(__JNI.callPPI(arg0, __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: bool, arg2: bool, arg3: bool, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,boolean,boolean,boolean,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), __long.valueOf(arg5))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def callUUUUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callUUUUV(byte,byte,byte,byte,long)"""
        __JNI.callUUUUV(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPCS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPCS(long,long,short,long)"""
        return int.__wrap(__JNI.callPPCS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,long)"""
        return bool.__wrap(__JNI.invokePZ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,int,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,int,long,long)"""
        __JNI.invokePJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,long,byte,long)"""
        return int.__wrap(__JNI.invokeCPUI(__short.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,float,float,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'int', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10, __long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,int,long,long,long,long,int,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callF(arg0: int) -> float:
        """public static native float org.lwjgl.system.JNI.callF(long)"""
        return float.__wrap(__JNI.callF(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,int,int,long,long)"""
        return int.__wrap(__JNI.callPJI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,int,long,int,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSS(long,long,short,long,short,long,short,long)"""
        return int.__wrap(__JNI.callPPSPSPSS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(int,long)"""
        return int.__wrap(__JNI.invokeP(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPSSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSPS(long,short,short,long,int,long)"""
        return int.__wrap(__JNI.callPSSPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,long,int,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,long,long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(int,short,long)"""
        __JNI.invokeCV(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int,long,long)"""
        return int.__wrap(__JNI.invokePP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,long)"""
        return int.__wrap(__JNI.invokePI(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,long,long,long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPI(short,int[],long)"""
        return int.__wrap(__JNI.invokeCPI(__short.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,double,long)"""
        __JNI.callV(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCCUCCCCUCCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUCCCCUCCCCCCV(long,short,short,byte,short,short,short,short,byte,short,short,short,short,short,short,long)"""
        __JNI.invokePCCUCCCCUCCCCCCV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __byte.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __short.valueOf(arg7), __byte.valueOf(arg8), __short.valueOf(arg9), __short.valueOf(arg10), __short.valueOf(arg11), __short.valueOf(arg12), __short.valueOf(arg13), __short.valueOf(arg14), __long.valueOf(arg15))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14), __long.valueOf(arg15)))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,long,long,long,long,int,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,int,long,int,int,long,long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPZ(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPZ(int,int,int,float,long,long,long,long,long)"""
        return bool.__wrap(__JNI.callPPPPZ(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,int,long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int, arg2: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,int,long)"""
        return float.__wrap(__JNI.invokePD(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPP(long,long,long,long,long,long,long,int,long,int,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __int.valueOf(arg12), __long.valueOf(arg13)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,long,int,int,long)"""
        __JNI.callJV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int[],int,long)"""
        return int.__wrap(__JNI.callPI(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'int', arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: 'int', arg22: 'long', arg23: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,int[],long[],int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int[],long[],long)"""
        return int.__wrap(__JNI.callPPPPI(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __int.valueOf(arg17), __int.valueOf(arg18), __int.valueOf(arg19), __int.valueOf(arg20), arg21, arg22, __long.valueOf(arg23)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: bool, arg2: bool, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,boolean,boolean,long,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long,int,int,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCCUV(long,short,short,short,short,short,int,short,int,byte,long)"""
        __JNI.invokePCCCCCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __int.valueOf(arg6), __short.valueOf(arg7), __int.valueOf(arg8), __byte.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,int[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,long,int,int,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,int[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int[],int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'double', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,long)"""
        __JNI.callPJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPD(arg0: int, arg1: int, arg2: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePPD(long,long,long)"""
        return float.__wrap(__JNI.invokePPD(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,boolean,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPJJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPJJPPP(long,long,long,long,int,long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPJJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPPPI(arg0: 'int', arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(int[],long,int[],long)"""
        return int.__wrap(__JNI.callPPPI(arg0, __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,int,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'double', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,double[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), arg10, __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPI(long,long,long,long,long[],long)"""
        return int.__wrap(__JNI.callPJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePNNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNNPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(int,int,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(long,int,long)"""
        __JNI.invokeJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCCUPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUPPV(short,short,byte,long,long,long)"""
        __JNI.invokeCCUPPV(__short.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPP(long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],long,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCPP(int,short,long,long)"""
        return int.__wrap(__JNI.invokeCPP(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePNNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNNPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNNPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,short[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPSS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSS(long,short,long)"""
        return int.__wrap(__JNI.callPSS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'int', arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int[],int[],int[],long)"""
        __JNI.invokePPPV(arg0, arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPSPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSPS(long,short,long,long)"""
        return int.__wrap(__JNI.callPSPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,int,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokeJ(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeJ(long)"""
        return int.__wrap(__JNI.invokeJ(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(long,int,long,int,long,int,long)"""
        __JNI.callPPJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPCPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPPPS(long,short,long,long,long,long)"""
        return int.__wrap(__JNI.callPCPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,int,int,long,long,long)"""
        __JNI.invokePPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: float, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,long,int,int,int,int,float,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __float.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,double[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callCCCCV(short,short,short,short,long)"""
        __JNI.callCCCCV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long,int,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,int,long,long,long,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,int,long,long,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: bool, arg1: bool, arg2: bool, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(boolean,boolean,boolean,boolean,long)"""
        __JNI.callV(__boolean.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int,int[],long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,int,long)"""
        return int.__wrap(__JNI.invokePI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPPV(int,int,int,long,int,long,long,long,long,long,long,long)"""
        __JNI.callPPPPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPJP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,int,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,float[],long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,int,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,boolean,long)"""
        return int.__wrap(__JNI.invokePI(__long.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCUV(short,short,short,short,short,byte,long)"""
        __JNI.invokeCCCCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __byte.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(int,int,int,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,int,int,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,long)"""
        return int.__wrap(__JNI.callI(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int[],long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(float,long)"""
        __JNI.invokeV(__float.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPPZ(long,long,long,long,long,long)"""
        return bool.__wrap(__JNI.callPPPPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJJJJJJJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJJJJJJJJV(long,long,long,long,long,long,long,long,long,long,long,long,int,int,int,long)"""
        __JNI.callPJJJJJJJJJJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __long.valueOf(arg15))

    @staticmethod
    @overload
    def invokeCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCPCV(short,short,short,short,long,short,long)"""
        __JNI.invokeCCCCPCV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeCCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCCPV(short,short,long,long)"""
        __JNI.invokeCCPV(__short.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePNNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNI(long,long,long,long)"""
        return int.__wrap(__JNI.invokePNNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,double,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPPP(long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePJPPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(int,int,int[],int[],int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5, __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: 'int', arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,int[],long,long)"""
        return bool.__wrap(__JNI.callPPZ(__int.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: 'int', arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(int[],long,long,int,boolean,float,long)"""
        return int.__wrap(__JNI.invokePPPI(arg0, __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callC(int,long)"""
        return int.__wrap(__JNI.callC(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,boolean,long)"""
        return int.__wrap(__JNI.invokeI(__int.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePNNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPPPI(long,long,long,int,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.invokePNNPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, arg6, __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,int,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callUUUUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callUUUUV(int,byte,byte,byte,byte,long)"""
        __JNI.callUUUUV(__int.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3), __byte.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: float, arg2: int, arg3: float, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,float,int,float,int,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,long,long)"""
        return int.__wrap(__JNI.invokePNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,float,float,float,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,boolean,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,long,float[],long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNPNN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPNN(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPNN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,long)"""
        return int.__wrap(__JNI.callJI(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'float', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,float[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), arg10, __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,int[],long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), arg7, arg8, __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,long,int,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: 'int', arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,int[],int,int[],float[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), arg6, arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,int,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int[],int[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,int[],int,int[],long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,short[],short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,long[],long[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,float,float,float,float,float,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,float,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'int', arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,int[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), arg10, __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokeCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCCCUV(short,short,short,short,short,int,byte,long)"""
        __JNI.invokeCCCCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __int.valueOf(arg5), __byte.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'int', arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,int[],int,float[],float[],long,int,int[],int,boolean,long)"""
        __JNI.invokePPPPPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5), __int.valueOf(arg6), arg7, __int.valueOf(arg8), __boolean.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeCP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCP(short,long)"""
        return int.__wrap(__JNI.invokeCP(__short.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,long,int,long)"""
        return bool.__wrap(__JNI.callPZ(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'double', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeUPU(arg0: int, arg1: int, arg2: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeUPU(byte,long,long)"""
        return int.__wrap(__JNI.invokeUPU(__byte.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,long,short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPPI(long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,int,long,long,long)"""
        __JNI.invokePPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,long[],short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), arg2, __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: float, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,double,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __double.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,float,float,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int[],long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(long,int,long[],int,long,int,long)"""
        __JNI.callPPJV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,int,long,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int[],int[],long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,double,double,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,int,int,long,int,boolean,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,boolean,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,long)"""
        return int.__wrap(__JNI.callPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPI(long,long,long,int,int,long,long,int,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPNV(long,long,long,long,long)"""
        __JNI.callPPPNV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,int,int,long,long,int,int,long)"""
        __JNI.callPJJV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePSSCCPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePSSCCPP(long,short,short,short,short,long,long)"""
        return int.__wrap(__JNI.invokePSSCCPP(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,long,long)"""
        return bool.__wrap(__JNI.invokePPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,int,long,int,int,int,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,short[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'float', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,int,long)"""
        return bool.__wrap(__JNI.invokePZ(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callSV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callSV(int,short,long)"""
        __JNI.callSV(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,int,int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNI(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJJ(long,long)"""
        return int.__wrap(__JNI.callJJ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,long,int,long)"""
        return int.__wrap(__JNI.callPPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,float,float,float,float,float,int,long,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,int,float,int,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUPV(long,byte,long,int,int,long)"""
        __JNI.invokePUPV(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int[],int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int,long,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int[],int,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPCS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCS(long,short,long)"""
        return int.__wrap(__JNI.callPCS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,float,long)"""
        __JNI.callPV(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCCUCCCCUCCCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUCCCCUCCCCCCV(short,short,byte,short,short,short,short,byte,short,short,short,short,short,short,long)"""
        __JNI.invokeCCUCCCCUCCCCCCV(__short.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __byte.valueOf(arg7), __short.valueOf(arg8), __short.valueOf(arg9), __short.valueOf(arg10), __short.valueOf(arg11), __short.valueOf(arg12), __short.valueOf(arg13), __long.valueOf(arg14))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePCI(long,short,long)"""
        return int.__wrap(__JNI.invokePCI(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,int,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callSPPS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPPS(short,long,long,long)"""
        return int.__wrap(__JNI.callSPPS(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,long,int,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,long,int,long)"""
        return bool.__wrap(__JNI.callPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeI(arg0: bool, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(boolean,long)"""
        return int.__wrap(__JNI.invokeI(__boolean.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokeCCCJPC(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCJPC(short,short,short,boolean,int,long,long,long)"""
        return int.__wrap(__JNI.invokeCCCJPC(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,int,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'short', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'long', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,int[],long[],long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,float,float,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'long', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(int,long,long[],int[],long)"""
        return int.__wrap(__JNI.callPPPP(__int.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPPI(int,int,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callJPPPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,float,float,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,int,long)"""
        __JNI.invokeCV(__short.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), arg7, arg8, __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePP(arg0: 'long', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long[],int,long)"""
        return int.__wrap(__JNI.invokePP(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(int,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'double', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPNI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,int,int,long,int,long,int,long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,int,int,long)"""
        return int.__wrap(__JNI.callI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCI(int,short,long)"""
        return int.__wrap(__JNI.invokeCI(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'long', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPPI(long,long,long,int,long,long,long[],long)"""
        return int.__wrap(__JNI.callPJJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPNV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPNV(long,long,long,long)"""
        __JNI.callPPNV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,float,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePUPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUPCV(long,byte,long,int,int,short,long)"""
        __JNI.invokePUPCV(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int,int,long,long)"""
        return bool.__wrap(__JNI.invokePPZ(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,long,int,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,float[],long)"""
        __JNI.invokeUPV(__byte.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: 'int', arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,int[],long)"""
        return bool.__wrap(__JNI.invokePPPZ(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePPCC(long,long,short,long)"""
        return int.__wrap(__JNI.invokePPCC(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,long,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,long[],int[],long,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPV(arg0: 'long', arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long[],int[],int[],int[],int,long)"""
        __JNI.callPPPPV(arg0, arg1, arg2, arg3, __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPCCPSPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCCPSPPS(long,short,short,long,short,long,long,long)"""
        return int.__wrap(__JNI.callPCCPSPPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,float,float,long,long)"""
        return bool.__wrap(__JNI.callPZ(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCUV(short,short,short,int,byte,long)"""
        __JNI.invokeCCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: 'int', arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int[],long)"""
        return int.__wrap(__JNI.callPI(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int[],long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,int,long,int,long,int,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long[],long,long,long,int,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPJPPPPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), arg7, __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callJJI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJI(long,float,float,float,float,long,long)"""
        return int.__wrap(__JNI.callJJI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPPS(long,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPS(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,long,long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: 'long', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int,int,float,int[],long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,int,long,long,long,long,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'short', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10, __long.valueOf(arg11))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,float[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,float,float,float,float,float,float,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,float,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJJJV(int,long,long,long,long)"""
        __JNI.callJJJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJV(long,long,int,int,long,long,long,int,long)"""
        __JNI.callPJJJJV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,int,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPCSSSPSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCSSSPSPPPS(long,short,short,short,short,long,short,long,long,long,long)"""
        return int.__wrap(__JNI.callPCSSSPSPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int[],long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePNPNPN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPNPN(long,long,int,int,int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPNPN(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(long,float,float,float,long)"""
        return int.__wrap(__JNI.callJI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPN(long,long)"""
        return int.__wrap(__JNI.callPN(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,int,long,long)"""
        return int.__wrap(__JNI.callPP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPSPSPSCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSCCS(long,long,short,long,short,long,short,short,short,long)"""
        return int.__wrap(__JNI.callPPSPSPSCCS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __short.valueOf(arg7), __short.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJ(long,int,long)"""
        return int.__wrap(__JNI.invokePJ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeP(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(long)"""
        return int.__wrap(__JNI.invokeP(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: 'double', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(double[],long)"""
        __JNI.callPV(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokeCPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPPV(short,long,long,long)"""
        __JNI.invokeCPPV(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePNPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePNPPV(long,long,long,long,long)"""
        __JNI.invokePNPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJ(long,long)"""
        return int.__wrap(__JNI.callPJ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(int,long,long)"""
        return int.__wrap(__JNI.invokePI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,int,long,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJPPJI(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callJPJPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long[],int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,long[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,int[],byte,long)"""
        return int.__wrap(__JNI.invokeCPUI(__short.valueOf(arg0), arg1, __byte.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPZ(long,int,long,long)"""
        return bool.__wrap(__JNI.invokePPZ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,long)"""
        return int.__wrap(__JNI.invokePI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int[],int,int,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPNNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNNPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long[],long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCV(short,int,int,long)"""
        __JNI.invokeCV(__short.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeNNN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNNN(long,long,long)"""
        return int.__wrap(__JNI.invokeNNN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(float,long)"""
        __JNI.callV(__float.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeCUC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCUC(short,byte,long)"""
        return int.__wrap(__JNI.invokeCUC(__short.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,int,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: 'int', arg2: int, arg3: 'int', arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,int[],int,int[],int,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJ(long,long,long)"""
        return int.__wrap(__JNI.callPPJ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,int,int,int,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: bool, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,boolean,long)"""
        return bool.__wrap(__JNI.invokePZ(__long.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePI(long,int,int,int,long)"""
        return int.__wrap(__JNI.invokePI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,long,int,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'float', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,int,long,int,long)"""
        return int.__wrap(__JNI.callPPS(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int):
        """public static native void org.lwjgl.system.JNI.callV(long)"""
        __JNI.callV(__long.valueOf(arg0))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,boolean,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePP(arg0: 'int', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(int[],int,long)"""
        return int.__wrap(__JNI.invokePP(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePB(arg0: int, arg1: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokePB(long,long)"""
        return int.__wrap(__JNI.invokePB(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: 'short', arg2: int, arg3: 'short', arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,short[],int,short[],int,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],long[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int[],long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPJPPI(long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJI(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: 'double', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double,double,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __double.valueOf(arg5), __double.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,long)"""
        __JNI.callV(__float.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'short', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,short[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,long[],long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,long)"""
        return bool.__wrap(__JNI.invokePPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,double[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,float,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(int,int,int,long,int,long,boolean,long,long)"""
        return int.__wrap(__JNI.callPPJI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __boolean.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPI(long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPNPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPS(long,long,long)"""
        return int.__wrap(__JNI.callPPS(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePUV(long,int,int,byte,long)"""
        __JNI.invokePUV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'double', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,double[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,float[],short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callJPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long,int,long,long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJ(int,int,long,long)"""
        return int.__wrap(__JNI.callPJ(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCCJZ(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeCCJZ(short,boolean,short,int,long,long)"""
        return bool.__wrap(__JNI.invokeCCJZ(__short.valueOf(arg0), __boolean.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,long,int,long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int,int,long,long,long,long,long,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int[],long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,long,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPUPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPUPPI(long,byte,long,long,long)"""
        return int.__wrap(__JNI.callPUPPI(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPV(long,long,long,long,long,long,long)"""
        __JNI.invokePPPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,float,float,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def invokeCCUUUUUUUUUV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUUUUUUUUUV(short,short,float,byte,byte,byte,byte,byte,byte,byte,byte,byte,long)"""
        __JNI.invokeCCUUUUUUUUUV(__short.valueOf(arg0), __short.valueOf(arg1), __float.valueOf(arg2), __byte.valueOf(arg3), __byte.valueOf(arg4), __byte.valueOf(arg5), __byte.valueOf(arg6), __byte.valueOf(arg7), __byte.valueOf(arg8), __byte.valueOf(arg9), __byte.valueOf(arg10), __byte.valueOf(arg11), __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,int,int,byte,long)"""
        __JNI.invokeCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __byte.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPCPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPS(long,short,long,short,long,long)"""
        return int.__wrap(__JNI.callPCPSPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,long,int,int,long)"""
        __JNI.invokeUPV(__byte.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,int,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int[],long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJJJV(long,long,long,long,long,int,int,long)"""
        __JNI.callPJJJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJPPPV(long,int,int,long,long,int,long,long,long)"""
        __JNI.callPJPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,long,int,int,int,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,long,long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePJPV(long,long,long,int,long)"""
        __JNI.invokePJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPPPF(long,long,long,long)"""
        return float.__wrap(__JNI.callPPPF(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPPS(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPS(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int[],long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,int,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'short', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeC(arg0: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeC(long)"""
        return int.__wrap(__JNI.invokeC(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: bool, arg12: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,int,int,int,int,long,boolean,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __boolean.valueOf(arg11), __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,long,long)"""
        return int.__wrap(__JNI.invokePPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,long,int,long)"""
        return int.__wrap(__JNI.callPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNI(long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callJPV(long,long,long)"""
        __JNI.callJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,int,boolean,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,double,double,double,long)"""
        __JNI.callV(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callSPSS(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSS(short,long,short,long)"""
        return int.__wrap(__JNI.callSPSS(__short.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,long)"""
        return bool.__wrap(__JNI.callZ(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeCPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPI(short,long,long)"""
        return int.__wrap(__JNI.invokeCPI(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePN(long,long)"""
        return int.__wrap(__JNI.invokePN(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,long)"""
        return float.__wrap(__JNI.invokePD(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPJPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPP(long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,float,float,float,float,float,float,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int[],int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,int,long,long,long,long,long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,long,long,long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,short[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,long,int[],long,long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCCC(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCC(short,short,boolean,long)"""
        return int.__wrap(__JNI.invokeCCC(__short.valueOf(arg0), __short.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int,long[],long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCJC(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCJC(int,boolean,short,int,long,long)"""
        return int.__wrap(__JNI.invokeCJC(__int.valueOf(arg0), __boolean.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,float[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,int,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long,boolean,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePNNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePNNV(long,long,int,int,long,long)"""
        __JNI.invokePNNV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,boolean,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,long,long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePUCV(long,byte,short,int,long)"""
        __JNI.invokePUCV(__long.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callSSSV(int,short,short,short,long)"""
        __JNI.callSSSV(__int.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,long,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePP(arg0: 'float', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(float[],int,long)"""
        return int.__wrap(__JNI.invokePP(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNI(long,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePNNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPJV(long,long,long,long,long,long,long)"""
        __JNI.callPPPPPJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,long,long,int,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCCPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCCPV(short,short,short[],long)"""
        __JNI.invokeCCPV(__short.valueOf(arg0), __short.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callJJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callJJJJV(int,long,long,long,long,long)"""
        __JNI.callJJJJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int,int,int,long,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,float[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'float', arg3: 'float', arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,float[],float[],float[],long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,int,long,int,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'long', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,long[],short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,int,long,int,int,int,int,int,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __long.valueOf(arg17)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,int,int[],int[],int[],long,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int[],boolean,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __boolean.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int[],long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), arg6, arg7, __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,float,float,float,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,int,long)"""
        __JNI.callPJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePJPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPJPP(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePJPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,long,long,long)"""
        return int.__wrap(__JNI.callPPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,int,int,int,int[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,int,int,float,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,int,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,long,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,double,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeU(arg0: int, arg1: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeU(int,long)"""
        return int.__wrap(__JNI.invokeU(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: 'int', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,long,long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: float, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,int,int,int,int,float,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __float.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,long,long,long,int,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,int,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'short', arg9: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), arg8, __long.valueOf(arg9))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,int,long,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,long,int,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,int,long)"""
        return float.__wrap(__JNI.invokePF(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,int[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'float', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(float[],int,long,long,int,long)"""
        __JNI.invokePPPV(arg0, __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJPV(int,int,long,long,long)"""
        __JNI.callJPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePUCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUCUV(long,byte,short,byte,int,int,long)"""
        __JNI.invokePUCUV(__long.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __byte.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,float,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'long', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long[],long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJI(int,long,int,int,long)"""
        return int.__wrap(__JNI.callJI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: 'double', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), arg10, __long.valueOf(arg11))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,int,long)"""
        return int.__wrap(__JNI.callPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,float[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPJPI(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPCPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPCPPI(long,short,long,long,long)"""
        return int.__wrap(__JNI.callPCPPI(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,long[],long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: float, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,int,int,int,float,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: bool, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,boolean,long)"""
        __JNI.invokeUV(__byte.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callJPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPJI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callJPPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,float[],float[],long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,int,int,int,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: float, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,long,int,int,float,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __float.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def invokeUPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokeUPZ(byte,long,long)"""
        return bool.__wrap(__JNI.invokeUPZ(__byte.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,int,long,int,long)"""
        return int.__wrap(__JNI.callPP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,long,int,int,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,long,long,long,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,float,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,int,int,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'float', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), arg8, arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13)))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,long)"""
        __JNI.invokeUV(__byte.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPUPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPUPPPI(long,long,byte,long,long,long,long)"""
        return int.__wrap(__JNI.callPPUPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,long,int[],long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int,int[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,float,float,float,long)"""
        return int.__wrap(__JNI.callP(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callZ(arg0: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(long)"""
        return bool.__wrap(__JNI.callZ(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'float', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int[],float[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,long,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPJPPZ(long,long,long,long,long,long)"""
        return bool.__wrap(__JNI.callPPJPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeC(int,long)"""
        return int.__wrap(__JNI.invokeC(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokeCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCCV(short,short,short,int,long)"""
        __JNI.invokeCCCV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeCPCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCPCC(short,long,short,long)"""
        return int.__wrap(__JNI.invokeCPCC(__short.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,int,short,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPNP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPNP(long,long,long)"""
        return int.__wrap(__JNI.callPNP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,long,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPNJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNJI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePUP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePUP(long,byte,long)"""
        return int.__wrap(__JNI.invokePUP(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJ(long,int,long,long)"""
        return int.__wrap(__JNI.callPPJ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'double', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,double[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,double,long)"""
        __JNI.callV(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,int[],int[],int[],int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), arg1, arg2, arg3, arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: 'short', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(short[],long)"""
        __JNI.callPV(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],int,int[],int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePD(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokePD(long,int,int,long)"""
        return float.__wrap(__JNI.invokePD(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJPPV(long,int,long,int,int,long,long,long)"""
        __JNI.callPJPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: float, arg2: float, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,float,float,long)"""
        return bool.__wrap(__JNI.callZ(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUCV(long,byte,short,int,int,long)"""
        __JNI.invokePUCV(__long.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,int,long,int,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,boolean,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,float,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'double', arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,double[],double[],long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,double[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int,int,long,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int[],long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,long)"""
        return float.__wrap(__JNI.invokePF(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePBV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePBV(long,int,int,byte,long)"""
        __JNI.invokePBV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int[],long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,long,long[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,int,int,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,int,long,int,long,int,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJPPP(long,long,int,long,long,int,long)"""
        return int.__wrap(__JNI.invokePJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeUCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUCV(byte,short,int,int,long)"""
        __JNI.invokeUCV(__byte.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,int[],int[],long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,int,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,int,int,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPPPP(long,int,long,long,long,int,long,long,int,long,long,int,int,int,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __long.valueOf(arg15), __long.valueOf(arg16), __long.valueOf(arg17), __long.valueOf(arg18), __long.valueOf(arg19)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,long,long)"""
        return bool.__wrap(__JNI.callPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: 'long', arg2: 'int', arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long[],int[],long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPCPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPPPPS(long,short,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPCPPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,float,float,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,long,int,int,int,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: 'int', arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int[],int[],long)"""
        __JNI.callPPV(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callI(arg0: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(long)"""
        return int.__wrap(__JNI.callI(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokeV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(double,long)"""
        __JNI.invokeV(__double.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int[],long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],long,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeUCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUCUV(byte,short,byte,int,int,long)"""
        __JNI.invokeUCUV(__byte.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,long,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJJV(int,int,long,long,long)"""
        __JNI.callJJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPPI(long,int,int,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __long.valueOf(arg17))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: 'int', arg13: 'int', arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPPPPPI(long,long,long,long,long,long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), arg12, arg13, __long.valueOf(arg14), __long.valueOf(arg15)))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(long,long)"""
        return bool.__wrap(__JNI.callJZ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPJJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJJPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPJJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,short[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), arg7, __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,long,int[],int[],int[],int,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, arg5, __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPZ(long,long,long,long,long)"""
        return bool.__wrap(__JNI.invokePPPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNNI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,long,boolean,boolean,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: 'int', arg2: 'float', arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int[],float[],int,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,long,int,long)"""
        return int.__wrap(__JNI.invokePNI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,boolean,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: 'float', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float,float,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,int,float,long,int,long,long)"""
        return int.__wrap(__JNI.callJPJI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,long,int,int,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeCPP(short,long,long)"""
        return int.__wrap(__JNI.invokeCPP(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPS(long,long,short,long,long)"""
        return int.__wrap(__JNI.callPPSPS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,float,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,long,int,long,int,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,int,int,int[],int[],long)"""
        return int.__wrap(__JNI.callPPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,long,long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,long,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePUCCV(long,byte,short,short,int,long)"""
        __JNI.invokePUCCV(__long.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePJJPV(long,int,long,long,long,long)"""
        __JNI.invokePJJPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPCPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPCPV(long,long,short,int,long,long)"""
        __JNI.invokePPCPV(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeJV(int,int,long,long)"""
        __JNI.invokeJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPSPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSPSS(long,long,short,long,short,long,short,long,short,long)"""
        return int.__wrap(__JNI.callPPSPSPSPSS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __short.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPJI(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callJPJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,int,long,long,long[],long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'short', arg2: int, arg3: 'float', arg4: 'float', arg5: int, arg6: int, arg7: 'short', arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,short[],int,float[],float[],long,int,short[],int,boolean,long)"""
        __JNI.invokePPPPPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5), __int.valueOf(arg6), arg7, __int.valueOf(arg8), __boolean.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePCP(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePCP(long,short,boolean,long)"""
        return int.__wrap(__JNI.invokePCP(__long.valueOf(arg0), __short.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,int,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), arg6, __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,int,long)"""
        return int.__wrap(__JNI.callPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int[],int[],int,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,int,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long[],int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPCI(arg0: int, arg1: 'float', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPCI(long,float[],short,long)"""
        return int.__wrap(__JNI.invokePPCI(__long.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,long,short[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callCV(int,short,long)"""
        __JNI.callCV(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePUCCV(long,byte,short,int,int,short,long)"""
        __JNI.invokePUCCV(__long.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int[],long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeCC(arg0: int, arg1: bool, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCC(short,boolean,long)"""
        return int.__wrap(__JNI.invokeCC(__short.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double,double,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __double.valueOf(arg5), __double.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,long,int,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,long,int,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeCC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCC(int,short,long)"""
        return int.__wrap(__JNI.invokeCC(__int.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,float[],long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,long,int[],int[],int[],int,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, arg4, __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeUCCV(byte,short,short,int,long)"""
        __JNI.invokeUCCV(__byte.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPJJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJPPPPPPP(long,long,long,long,long,int,long,int,long,int,long,long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __int.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14), __long.valueOf(arg15), __long.valueOf(arg16), __long.valueOf(arg17)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(long,int,long)"""
        return bool.__wrap(__JNI.callPZ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,long,int,int,long,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPJI(long,int,int,int,long,int,long,boolean,long,long)"""
        return int.__wrap(__JNI.callJPPJI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __boolean.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callUV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callUV(byte,long)"""
        __JNI.callUV(__byte.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePJJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJJP(long,long,long,long)"""
        return int.__wrap(__JNI.invokePJJP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,float[],int,int,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPUPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPUPZ(long,long,long,byte,long,long)"""
        return bool.__wrap(__JNI.invokePPPUPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePNPN(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNPN(long,long,long,long)"""
        return int.__wrap(__JNI.invokePNPN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,boolean,boolean,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPP(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,int,int,int[],long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,float,float,float,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callJJI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJI(long,long,long)"""
        return int.__wrap(__JNI.callJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPCV(long,int,short,long)"""
        __JNI.callPCV(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,int,long,long,long,int,long)"""
        return int.__wrap(__JNI.callJPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), arg6, arg7, __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: float, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,int,boolean,float,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePNI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNI(long,int,long,long)"""
        return int.__wrap(__JNI.invokePNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,long,int[],long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,int[],long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPPP(long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,boolean,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],int,int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,short[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: 'double', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'long', arg5: 'long', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,int,long[],long[],long[],long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,long,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: 'float', arg7: 'int', arg8: 'int', arg9: 'int', arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPPPI(long,int,int,long,int[],int[],float[],int[],int[],int[],long)"""
        return int.__wrap(__JNI.invokePPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, arg6, arg7, arg8, arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePNP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNP(long,long,long)"""
        return int.__wrap(__JNI.invokePNP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPPV(short,float[],float[],long)"""
        __JNI.invokeCPPV(__short.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,double[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(int,long,int,long)"""
        return bool.__wrap(__JNI.callJZ(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'int', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokeUPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUPV(byte,long,long)"""
        __JNI.invokeUPV(__byte.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePNPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNPV(long,long,long,long)"""
        __JNI.invokePNPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,int[],long,int,long)"""
        return int.__wrap(__JNI.callPJPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPPPPP(long,long,long,long,long,int,long,int,int,long,long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14), __long.valueOf(arg15), __long.valueOf(arg16)))

    @staticmethod
    @overload
    def callPPPPPP(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPP(long,long,long[],long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,long,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,long,int,long)"""
        __JNI.invokeCPV(__short.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,float,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(int,long,int,long)"""
        return int.__wrap(__JNI.callPI(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'float', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,float[],short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), arg2, __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,int,float[],int[],long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeP(arg0: bool, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(boolean,long)"""
        return int.__wrap(__JNI.invokeP(__boolean.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,int,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,double[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],long[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,int,long,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,float[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPSPSPSPSPSPSS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPSPSPSPSS(long,long,short,long,short,long,short,long,short,long,short,long,short,long)"""
        return int.__wrap(__JNI.callPPSPSPSPSPSPSS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __short.valueOf(arg8), __long.valueOf(arg9), __short.valueOf(arg10), __long.valueOf(arg11), __short.valueOf(arg12), __long.valueOf(arg13)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,float,float,int,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,long,long)"""
        return int.__wrap(__JNI.callPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callUUUV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callUUUV(byte,byte,byte,long)"""
        __JNI.callUUUV(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,int,int,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,int,int,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPP(long,long,long,long,long,long,long,int,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int, arg23: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,long,long,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __int.valueOf(arg15), __int.valueOf(arg16), __int.valueOf(arg17), __int.valueOf(arg18), __int.valueOf(arg19), __int.valueOf(arg20), __long.valueOf(arg21), __long.valueOf(arg22), __long.valueOf(arg23)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJJPI(long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJJJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPSPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPPSPSPS(long,long,short,long,short,long,long)"""
        return int.__wrap(__JNI.callPPSPSPS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: 'int', arg8: 'int', arg9: 'int', arg10: 'long', arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPPV(int,int,int,long,int,long,int[],int[],int[],int[],long[],long)"""
        __JNI.callPPPPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), arg6, arg7, arg8, arg9, arg10, __long.valueOf(arg11))

    @staticmethod
    @overload
    def callZ(arg0: bool, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(boolean,long)"""
        return bool.__wrap(__JNI.callZ(__boolean.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPPJJJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJJPP(long,long,long,long,long,int,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJJJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: bool, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPP(long,long,int,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,int,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePNNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNNPI(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePNNPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callJPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,short[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeUPC(arg0: int, arg1: int, arg2: bool, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeUPC(byte,long,boolean,long)"""
        return int.__wrap(__JNI.invokeUPC(__byte.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,float,boolean,long)"""
        __JNI.callV(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(long,int,long,long,long,long)"""
        __JNI.callPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePZ(long,int,long)"""
        return bool.__wrap(__JNI.invokePZ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callSPSSPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSSPSPS(short,long,short,short,long,short,long,long)"""
        return int.__wrap(__JNI.callSPSSPSPS(__short.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJJJJPI(long,long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePJJJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePF(long,int,int,long)"""
        return float.__wrap(__JNI.invokePF(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,int,long,long)"""
        return int.__wrap(__JNI.callPJI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'short', arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,short[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPNP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPNP(long,long,long,long)"""
        return int.__wrap(__JNI.callPPNP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPP(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPP(long,int,int[],long,long)"""
        return int.__wrap(__JNI.callPPPP(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPNPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPPI(long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(int,long)"""
        return int.__wrap(__JNI.callP(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,int,int,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callSV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callSV(short,long)"""
        __JNI.callSV(__short.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPUPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPUPI(long,byte,long,long)"""
        return int.__wrap(__JNI.callPUPI(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,long)"""
        __JNI.callV(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPI(long,long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: float, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,float,long,int,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,int,long,long,long,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJI(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJI(long,int,long[],int,long,long)"""
        return int.__wrap(__JNI.callPPJI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPPPP(long,long,int,long,long,long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,int[],long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'float', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,long,long,long,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,short[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,int,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callSPSPPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPSPPPSPS(short,long,short,long,long,long,short,long,long)"""
        return int.__wrap(__JNI.callSPSPPPSPS(__short.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJV(long,long,long,int,int,long)"""
        __JNI.callPJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,long,int,int,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,long)"""
        __JNI.callPV(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int[],long,long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(long,int,long,int,long)"""
        __JNI.callPJV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPP(long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(long,long)"""
        return bool.__wrap(__JNI.callPZ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: bool, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,boolean,long,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __boolean.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePP(arg0: 'short', arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(short[],int,long)"""
        return int.__wrap(__JNI.invokePP(arg0, __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPF(arg0: int, arg1: float, arg2: int) -> float:
        """public static native float org.lwjgl.system.JNI.callPF(long,float,long)"""
        return float.__wrap(__JNI.callPF(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,double[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,int,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'float', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int,int,float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int,long,int[],long,long,long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,long,long,long)"""
        return int.__wrap(__JNI.invokePPP(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,long,long,long)"""
        __JNI.invokePPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePCCCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCV(long,short,short,short,boolean,boolean,short,int,long)"""
        __JNI.invokePCCCCV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5), __short.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePCCUV(long,short,short,int,byte,long)"""
        __JNI.invokePCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __byte.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,int,int,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: 'int', arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: 'long', arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(int,int[],long[],int,int,int,int,long,long,long,int,int[],long[],long)"""
        return int.__wrap(__JNI.callPPPPPPPP(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __int.valueOf(arg10), arg11, arg12, __long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int[],long)"""
        return int.__wrap(__JNI.callPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,int,long,long)"""
        return bool.__wrap(__JNI.callPZ(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCUV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUV(short,short,int,float,byte,long)"""
        __JNI.invokeCCUV(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __byte.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeV(int,int,long)"""
        __JNI.invokeV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def invokeNNNN(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNNNN(long,long,long,long)"""
        return int.__wrap(__JNI.invokeNNNN(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPP(long,long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,int,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,long,long,int,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePN(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePN(long,int,long)"""
        return int.__wrap(__JNI.invokePN(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'long', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,long[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPCPSPSPSCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPSPSCCS(long,short,long,short,long,short,long,short,short,short,long)"""
        return int.__wrap(__JNI.callPCPSPSPSCCS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __short.valueOf(arg5), __long.valueOf(arg6), __short.valueOf(arg7), __short.valueOf(arg8), __short.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,int,int,long)"""
        return int.__wrap(__JNI.invokeI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,int,int,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,long,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: 'float', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(float[],long)"""
        __JNI.callPV(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,long,long,long,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,int,int,short,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,double,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'float', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],float[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,float,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,float[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: 'long', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long[],int,int,int,long,int,long,int,long,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def callPJCCS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPJCCS(long,long,short,short,long)"""
        return int.__wrap(__JNI.callPJCCS(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,int[],int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,int,long)"""
        return int.__wrap(__JNI.callJ(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPPZ(long,long,long,long,long,int,long)"""
        return bool.__wrap(__JNI.invokePPPPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJZ(int,long,long)"""
        return bool.__wrap(__JNI.callJZ(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'short', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokePPNPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNPPI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPJI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPUP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPUP(long,long,byte,long)"""
        return int.__wrap(__JNI.invokePPUP(__long.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(long,int,short,long)"""
        return int.__wrap(__JNI.invokePCC(__long.valueOf(arg0), __int.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,boolean,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPJPPP(long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPJPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeUV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeUV(byte,int,long)"""
        __JNI.invokeUV(__byte.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(double,double,long)"""
        __JNI.callV(__double.valueOf(arg0), __double.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPJPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPPPP(long,long,int,long,long,long,long,long,int,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), arg11, __long.valueOf(arg12)))

    @staticmethod
    @overload
    def invokeCCUPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUPV(short,short,byte,long,long)"""
        __JNI.invokeCCUPV(__short.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,boolean,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePNNNPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePNNNPP(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePNNNPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,int,long,long,long,long,long,int,int,long,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __long.valueOf(arg15)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,int[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,int[],int[],int[],long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), arg1, arg2, arg3, __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,long,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,long,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'float', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,float[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,int,long,int,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPS(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPS(long,long)"""
        return int.__wrap(__JNI.callPS(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,long,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,int,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: float, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,float,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPJP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPJP(long,long,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPJP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(int,long,int,long)"""
        return int.__wrap(__JNI.callPP(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callSPS(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.callSPS(short,long,long)"""
        return int.__wrap(__JNI.callSPS(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPSSPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSPPS(long,short,short,long,int,long,long)"""
        return int.__wrap(__JNI.callPSSPPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,long,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,long,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,boolean,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCUV(long,short,short,short,short,short,int,byte,long)"""
        __JNI.invokePCCCCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __int.valueOf(arg6), __byte.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,int,long)"""
        return int.__wrap(__JNI.invokeI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callS(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.callS(int,long)"""
        return int.__wrap(__JNI.callS(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPJPP(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPPV(long,long,long,int,int,long,long,long,long)"""
        __JNI.callPPPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callNV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callNV(long,int,int,int,long)"""
        __JNI.callNV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokePPF(long,int,long,long)"""
        return float.__wrap(__JNI.invokePPF(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,int,long,int,boolean,long)"""
        return bool.__wrap(__JNI.invokePPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,float,float,float,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,long,float[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(long,int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPPI(long,int,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJV(long,long,long,long,int,long)"""
        __JNI.callPJJJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callJJV(int,long,long,long)"""
        __JNI.callJJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePJUPC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePJUPC(long,long,byte,long,long)"""
        return int.__wrap(__JNI.invokePJUPC(__long.valueOf(arg0), __long.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,long,long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeCCCJPC(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCCJPC(short,short,boolean,short,int,long,long,long)"""
        return int.__wrap(__JNI.invokeCCCJPC(__short.valueOf(arg0), __short.valueOf(arg1), __boolean.valueOf(arg2), __short.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), arg8, arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'double', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,double[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callJPV(int,long,int,long,long)"""
        __JNI.callJPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), arg7, __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,float,float,int,int,float,float,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,long,int,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,int[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), arg7, __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPNI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: 'long', arg3: 'int', arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,long[],int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPJ(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJ(long,long,long)"""
        return int.__wrap(__JNI.invokePPJ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,short[],long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long,int,int,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePP(long,int,long)"""
        return int.__wrap(__JNI.invokePP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPPPI(long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCCC(long,short,short,int,int,long)"""
        return int.__wrap(__JNI.invokePCCC(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,long,long,long)"""
        return bool.__wrap(__JNI.callPPZ(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,int,long,long)"""
        __JNI.invokeCPV(__short.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJJJPI(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJJJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int[],long,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int, arg7: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPPZ(long,long,long,long,long,boolean,int,long)"""
        return bool.__wrap(__JNI.invokePPPPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __boolean.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,float,float,float,float,float,long)"""
        __JNI.callV(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,long)"""
        return int.__wrap(__JNI.callJ(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,long,int,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPCPSPPPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPPPPPS(long,short,long,short,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPCPSPPPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,float,float,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCCUUCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUUCCCCPCV(short,short,byte,byte,short,short,short,short,long,short,long)"""
        __JNI.invokeCCUUCCCCPCV(__short.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __short.valueOf(arg7), __long.valueOf(arg8), __short.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(int,int,long,long,long,long,long,long)"""
        __JNI.callPPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCCJC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCJC(short,short,int,long,long)"""
        return int.__wrap(__JNI.invokeCCJC(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,long,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: int, arg5: int, arg6: int, arg7: 'int', arg8: 'int', arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,long,float[],long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), arg7, arg8, __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,float,float,long)"""
        __JNI.callPV(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNI(long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long[],int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJI(arg0: int, arg1: int, arg2: float, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJI(long,long,float,long)"""
        return int.__wrap(__JNI.callPJI(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int,long,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokeCPUI(arg0: int, arg1: 'short', arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeCPUI(short,short[],byte,long)"""
        return int.__wrap(__JNI.invokeCPUI(__short.valueOf(arg0), arg1, __byte.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,long,int[],long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPJ(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPJ(long,long,int,long)"""
        return int.__wrap(__JNI.invokePPJ(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,long,long,long,int,int,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJJI(long,long,int,long,int,long)"""
        return int.__wrap(__JNI.callPJJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokeCPCC(arg0: int, arg1: 'short', arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCPCC(short,short[],short,long)"""
        return int.__wrap(__JNI.invokeCPCC(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,int,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,long,int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: 'int', arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int[],int,int[],long)"""
        __JNI.callPPV(arg0, __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNPI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: 'int', arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int[],boolean,long)"""
        __JNI.invokePV(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,int,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,long[],long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJJPPPP(long,long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPJJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePCCCCC(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCCCCC(long,short,short,short,short,long)"""
        return int.__wrap(__JNI.invokePCCCCC(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPCPSPPSPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCPSPPSPS(long,short,long,short,long,long,short,long,long)"""
        return int.__wrap(__JNI.callPCPSPPSPS(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,long,boolean,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,long,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPZ(int,long,long)"""
        return bool.__wrap(__JNI.callPZ(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,int,long,int,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPI(long,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPPP(long,long,long,long,long,int,long,int,int,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13), __long.valueOf(arg14)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPJPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'short', arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPPPP(long,long,long,long,long,long,long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), arg8, arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,int,long,int,long,long)"""
        return bool.__wrap(__JNI.callPPZ(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPP(long,long,long,long,long,int,long,int,long,int,long)"""
        return int.__wrap(__JNI.invokePPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,float,float,float,float,float,float,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,boolean,int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __boolean.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: bool, arg9: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __boolean.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def invokePNPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePNPI(long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePNPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,float,float,float,int,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPPZ(long,int,long,long,long,long)"""
        return bool.__wrap(__JNI.invokePPPPZ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,float,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'double', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,int,int,int,double[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJ(arg0: int, arg1: int, arg2: bool, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(int,int,boolean,int,int,long)"""
        return int.__wrap(__JNI.callJ(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePJPPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePJPPNI(long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePJPPNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,int,int,int,int,int,int,int,int,int,int,int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __int.valueOf(arg14), __long.valueOf(arg15))

    @staticmethod
    @overload
    def callSSV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callSSV(int,short,short,long)"""
        __JNI.callSSV(__int.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: bool, arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,boolean,float[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPV(arg0: 'int', arg1: int):
        """public static native void org.lwjgl.system.JNI.callPV(int[],long)"""
        __JNI.callPV(arg0, __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int[],int,long)"""
        __JNI.callPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,int,long,long,long,int,long,int,boolean,long)"""
        __JNI.invokePPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPCPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPCPPI(long,long,short,long,long,long)"""
        return int.__wrap(__JNI.callPPCPPI(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePUV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePUV(long,byte,long)"""
        __JNI.invokePUV(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'float', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,float[],int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJPPPP(arg0: int, arg1: int, arg2: int, arg3: 'float', arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPP(long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,long,int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPCPI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPCPI(long,short,long,long)"""
        return int.__wrap(__JNI.callPCPI(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'short', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,int[],short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), arg2, __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(long,long,long,long,int,long,long,int,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: 'int', arg9: 'int', arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPPI(long,long,long,long,long,long,long,int,int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), arg8, arg9, __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(long,int[],int[],int[],int[],long)"""
        __JNI.invokePPPPPV(__long.valueOf(arg0), arg1, arg2, arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callZ(arg0: int, arg1: int, arg2: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callZ(int,int,long)"""
        return bool.__wrap(__JNI.callZ(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeCPV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCPV(short,long,long)"""
        __JNI.invokeCPV(__short.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPPPP(long,long,long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def invokePPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPV(int,long,long,long,long,long,long)"""
        __JNI.invokePPPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJJPI(long,long,long,int,long)"""
        return int.__wrap(__JNI.callJJPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: float, arg3: float, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,float,float,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePNPV(arg0: int, arg1: int, arg2: 'short', arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePNPV(long,long,short[],long)"""
        __JNI.invokePNPV(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPPPI(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPJPPPPPI(long,long[],long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPPPI(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,boolean,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def callJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callJJJV(int,int,long,long,long,long)"""
        __JNI.callJJJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPJPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJPPP(long,int,long,long,long,long,int,int,long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12), __long.valueOf(arg13)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,long,long,int,int,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPZ(arg0: int, arg1: int, arg2: int, arg3: float, arg4: 'float', arg5: 'float', arg6: 'float', arg7: 'float', arg8: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPPZ(int,int,int,float,float[],float[],float[],float[],long)"""
        return bool.__wrap(__JNI.callPPPPZ(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7, __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,long,int,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPV(arg0: 'float', arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(float[],boolean,int,long,long,int,long)"""
        __JNI.invokePPPV(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,double,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callSSSSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callSSSSV(short,short,short,short,long)"""
        __JNI.callSSSSV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,short[],int,int,long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,int,int,int[],long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,int,int,long,long,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'float', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,float[],long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPI(long,long,long,long[],long)"""
        return int.__wrap(__JNI.invokePPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'float', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,float[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), arg7, __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,long,int,int,int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,int,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: 'int', arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int[],int,long,int,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCUV(long,short,int,short,short,short,byte,long)"""
        __JNI.invokePCCCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __byte.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,double,double,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,int,long,int[],long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,int,long,int,int,int,long,int,long,int,long,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11))

    @staticmethod
    @overload
    def invokePPCI(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPCI(long,long,short,long)"""
        return int.__wrap(__JNI.invokePPCI(__long.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,long,long,int,int,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,float,float,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,int,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPP(long,int,int,int,int[],long)"""
        return int.__wrap(__JNI.callPPP(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,long,long,int,boolean,boolean,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokeUCCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUCCV(byte,short,int,int,short,long)"""
        __JNI.invokeUCCV(__byte.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPNN(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPNN(long,int,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPNN(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPJPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPPPP(long,long,int,long,long,long,int,long,long,int[],long)"""
        return int.__wrap(__JNI.callPPJPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), arg9, __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,int,long,long,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,long,int,int,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPPI(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPI(int,int,int[],int[],int[],int[],int[],long,long)"""
        return int.__wrap(__JNI.callPPPPPPI(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, arg5, arg6, __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCV(long,short,int,int,long)"""
        __JNI.invokePCV(__long.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(long,int,long,long,long)"""
        __JNI.invokePPPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeD(arg0: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokeD(long)"""
        return float.__wrap(__JNI.invokeD(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokeF(arg0: int, arg1: int) -> float:
        """public static native float org.lwjgl.system.JNI.invokeF(int,long)"""
        return float.__wrap(__JNI.invokeF(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPJPV(arg0: int, arg1: int, arg2: 'long', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPJPV(long,long,long[],long)"""
        __JNI.callPJPV(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPNPI(arg0: int, arg1: int, arg2: int, arg3: 'long', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPNPI(long,long,long,long[],long)"""
        return int.__wrap(__JNI.callPPNPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,float,float,float,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePC(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePC(long,long)"""
        return int.__wrap(__JNI.invokePC(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'short', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,short[],int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeCCJPC(arg0: int, arg1: bool, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokeCCJPC(short,boolean,short,int,long,long,long)"""
        return int.__wrap(__JNI.invokeCCJPC(__short.valueOf(arg0), __boolean.valueOf(arg1), __short.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: 'double', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,double[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callJ(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.callJ(long)"""
        return int.__wrap(__JNI.callJ(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callPJPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPPJI(long,long,int,int,long,long,long,int,long)"""
        return int.__wrap(__JNI.callPJPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokeD(arg0: int, arg1: int) -> float:
        """public static native double org.lwjgl.system.JNI.invokeD(int,long)"""
        return float.__wrap(__JNI.invokeD(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,float,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,long,long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,long,long,int,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,short[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPV(arg0: 'short', arg1: 'short', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(short[],short[],long)"""
        __JNI.callPPV(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPJPI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callPJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPV(int,int,long,long,long,long,int,long)"""
        __JNI.callPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def invokePCPCV(arg0: int, arg1: int, arg2: 'short', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePCPCV(long,short,short[],short,long)"""
        __JNI.invokePCPCV(__long.valueOf(arg0), __short.valueOf(arg1), arg2, __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: 'double', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,double[],short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), arg1, __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(double,long)"""
        __JNI.callV(__double.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: 'int', arg12: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __int.valueOf(arg9), __int.valueOf(arg10), arg11, __long.valueOf(arg12))

    @staticmethod
    @overload
    def invokeCUCCCCCCPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCUCCCCCCPV(short,byte,short,short,short,short,short,short,long,long)"""
        __JNI.invokeCUCCCCCCPV(__short.valueOf(arg0), __byte.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __short.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(long,long,long,long,long,int,int,int,long)"""
        __JNI.callPPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPNNP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPNNP(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNNP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPPZ(long,long,long,long)"""
        return bool.__wrap(__JNI.callPPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int, arg10: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,float,float,float,float,float,float,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10))

    @staticmethod
    @overload
    def callV(arg0: float, arg1: float, arg2: float, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(float,float,float,long)"""
        __JNI.callV(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(long,int,long,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNI(long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPNI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,int[],long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,int,int,long,int,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokeCCUCCCCPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.invokeCCUCCCCPCV(short,short,byte,short,short,short,short,long,short,long)"""
        __JNI.invokeCCUCCCCPCV(__short.valueOf(arg0), __short.valueOf(arg1), __byte.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __short.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callCCCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callCCCV(short,short,short,long)"""
        __JNI.callCCCV(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: bool, arg3: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,boolean,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPV(long,long,long,long,long)"""
        __JNI.invokePPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'int', arg5: int, arg6: 'int', arg7: 'int', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int,int[],int,int[],int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), arg6, arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPJJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'double', arg5: int):
        """public static native void org.lwjgl.system.JNI.callPJJJPV(long,long,long,long,double[],long)"""
        __JNI.callPJJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,int,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'int', arg7: int, arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,int,int,int,int,int,int[],long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7), __long.valueOf(arg8))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,int,int,long,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePPPPPPPV(long,long,long,long,long,long,long,long)"""
        __JNI.invokePPPPPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(long,long,int,long,long)"""
        return int.__wrap(__JNI.callJPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: float, arg2: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,float,long)"""
        __JNI.callPV(__long.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(long,int,float,long,long)"""
        __JNI.callPPV(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPJV(int,long,long,int,long,boolean,long)"""
        __JNI.callPPJV(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __boolean.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPI(long,int,long,int,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,long,long[],long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeNN(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeNN(long,long)"""
        return int.__wrap(__JNI.invokeNN(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePNV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePNV(long,long,long)"""
        __JNI.invokePNV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(int,int,long,long,long)"""
        __JNI.invokePPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJPPI(long,int,long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPJPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPP(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPP(long,long)"""
        return int.__wrap(__JNI.callPP(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePNPPV(arg0: int, arg1: int, arg2: int, arg3: 'short', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePNPPV(long,long,long,short[],long)"""
        __JNI.invokePNPPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: 'int', arg3: 'int', arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int[],int[],long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(int,long,int,long,long)"""
        return bool.__wrap(__JNI.callPPZ(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: 'int', arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int[],int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokeUPCV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeUPCV(byte,long,int,int,short,long)"""
        __JNI.invokeUPCV(__byte.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __short.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: 'long', arg2: int, arg3: int, arg4: 'short', arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long[],long,long,short[],int[],long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __long.valueOf(arg3), arg4, arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: 'int', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(int,long,int[],long)"""
        return int.__wrap(__JNI.invokePPI(__int.valueOf(arg0), __long.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def invokePPPPPJJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPJJPP(long,long,long,long,long,int,long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPPPJJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __int.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePSV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePSV(long,int,int,short,long)"""
        __JNI.invokePSV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,int,int,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,long,int,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: float, arg2: float, arg3: float, arg4: int):
        """public static native void org.lwjgl.system.JNI.callV(int,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: int):
        """public static native void org.lwjgl.system.JNI.callV(int,int,int,double,double,double,double,long)"""
        __JNI.callV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __double.valueOf(arg3), __double.valueOf(arg4), __double.valueOf(arg5), __double.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPNNI(long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPNNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: float, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPPPI(long,long,long,int,int,int,float,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'int', arg10: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,int,int,int,int,int[],long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), arg9, __long.valueOf(arg10))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'short', arg8: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int,int,int,long,int,int,short[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), arg7, __long.valueOf(arg8))

    @staticmethod
    @overload
    def callPI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPI(long,int,long)"""
        return int.__wrap(__JNI.callPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPP(int,int,int,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPP(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePPUP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPUP(long,long,int,byte,long)"""
        return int.__wrap(__JNI.invokePPUP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPI(int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__JNI.callJPPI(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: 'float', arg2: 'float', arg3: 'float', arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,float[],float[],float[],long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), arg1, arg2, arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePPPZ(long,long,long,int,long)"""
        return bool.__wrap(__JNI.invokePPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPP(int,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def invokePPI(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPI(long,int,long,boolean,long)"""
        return int.__wrap(__JNI.invokePPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: int, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(int,long)"""
        __JNI.callV(__int.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def invokeJJJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokeJJJV(int,int,long,long,long,long)"""
        __JNI.invokeJJJV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,int,int[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPJPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPPPP(long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPSSSPSSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPSSSPSSPPPS(long,short,short,short,long,short,short,long,long,long,long)"""
        return int.__wrap(__JNI.callPSSSPSSPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __long.valueOf(arg4), __short.valueOf(arg5), __short.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPPP(long,int,long,long,int,long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.invokePPV(long,int,long,int,long)"""
        __JNI.invokePPV(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callJPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJPZ(long,long,int,long)"""
        return bool.__wrap(__JNI.callJPZ(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeI(arg0: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(long)"""
        return int.__wrap(__JNI.invokeI(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,long,long)"""
        __JNI.invokePJV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokeCCV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.invokeCCV(short,short,long)"""
        __JNI.invokeCCV(__short.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callSSV(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.JNI.callSSV(short,short,long)"""
        __JNI.callSSV(__short.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def invokePPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPP(long,long,long,int,long,int,int,long)"""
        return int.__wrap(__JNI.invokePPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'short', arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePV(int,int,int,int,int,int,short[],long)"""
        __JNI.invokePV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,float,float,float,float,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePBPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePBPPP(long,byte,long,long,long)"""
        return int.__wrap(__JNI.invokePBPPP(__long.valueOf(arg0), __byte.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,long,long)"""
        return int.__wrap(__JNI.invokePJP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokePPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPP(long,long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPI(long,long,long,long,int,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(int,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPI(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPP(long,long,int,int,int,int[],long)"""
        return int.__wrap(__JNI.callPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5, __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callF(arg0: int, arg1: int, arg2: int, arg3: int) -> float:
        """public static native float org.lwjgl.system.JNI.callF(int,int,int,long)"""
        return float.__wrap(__JNI.callF(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePJV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokePJV(long,long,int,long)"""
        __JNI.invokePJV(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePJPZ(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.invokePJPZ(long,long,long,int,long)"""
        return bool.__wrap(__JNI.invokePJPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: 'double', arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPPPPPI(long,long,int,long,long,long,long,double[],int,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), arg7, __int.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def invokePJ(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJ(long,long)"""
        return int.__wrap(__JNI.invokePJ(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callP(arg0: int) -> int:
        """public static native long org.lwjgl.system.JNI.callP(long)"""
        return int.__wrap(__JNI.callP(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,int,long)"""
        return int.__wrap(__JNI.callI(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,int,int,long,int,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def invokePPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPI(long,int,long,int,long,long)"""
        return int.__wrap(__JNI.invokePPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPP(long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPJI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPJI(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPJI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callJPPPPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPPPPPPPPI(long,long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.callJPPPPPPPPI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9)))

    @staticmethod
    @overload
    def invokePPPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPPPPP(long,long,long,long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8)))

    @staticmethod
    @overload
    def callPPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPPI(long,int,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.callPPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def invokeUPU(arg0: int, arg1: 'int', arg2: int) -> int:
        """public static native byte org.lwjgl.system.JNI.invokeUPU(byte,int[],long)"""
        return int.__wrap(__JNI.invokeUPU(__byte.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int, arg5: 'int', arg6: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,int,int,int[],long,int[],long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4), arg5, __long.valueOf(arg6))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(long,short,long)"""
        return int.__wrap(__JNI.invokePCC(__long.valueOf(arg0), __short.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callPV(long,int,int,int,int,int,long)"""
        __JNI.callPV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(int,long,int,long,long,long)"""
        __JNI.callPPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePCC(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native short org.lwjgl.system.JNI.invokePCC(int,long,short,long)"""
        return int.__wrap(__JNI.invokePCC(__int.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPJPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: 'float', arg7: 'int', arg8: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPJPPPPPPP(long,long,long,long,long,long,float[],int[],long)"""
        return int.__wrap(__JNI.callPJPPPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), arg6, arg7, __long.valueOf(arg8)))

    @staticmethod
    @overload
    def invokePV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePV(long,int,int,int,int,long)"""
        __JNI.invokePV(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def invokePPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPPP(long,long,long,int,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPPV(arg0: int, arg1: int, arg2: float, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPPV(long,long,float,long,long)"""
        __JNI.callPPPV(__long.valueOf(arg0), __long.valueOf(arg1), __float.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPPPPPPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'int', arg6: 'int', arg7: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPPPPPP(long,int,long,long,long,int[],int[],long)"""
        return int.__wrap(__JNI.callPPPPPPP(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), arg5, arg6, __long.valueOf(arg7)))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,long,int,int[],long)"""
        __JNI.callPPV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), arg3, __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePJP(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePJP(long,long,int,long)"""
        return int.__wrap(__JNI.invokePJP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePCCCCCUV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int):
        """public static native void org.lwjgl.system.JNI.invokePCCCCCUV(long,short,short,short,short,short,byte,long)"""
        __JNI.invokePCCCCCUV(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3), __short.valueOf(arg4), __short.valueOf(arg5), __byte.valueOf(arg6), __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: 'long', arg3: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,int,long[],long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callPPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'long', arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPPI(long,int,int,long,long[],long,long)"""
        return int.__wrap(__JNI.callPPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def invokeI(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokeI(int,long)"""
        return int.__wrap(__JNI.invokeI(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def callPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPI(long,long,int,int,long)"""
        return int.__wrap(__JNI.callPPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callPPV(arg0: 'double', arg1: 'double', arg2: int):
        """public static native void org.lwjgl.system.JNI.callPPV(double[],double[],long)"""
        __JNI.callPPV(arg0, arg1, __long.valueOf(arg2))

    @staticmethod
    @overload
    def callJPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callJPPZ(long,long,long,long)"""
        return bool.__wrap(__JNI.callJPPZ(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def invokePPPNNI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.invokePPPNNI(long,long,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPNNI(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJV(int,long,int,long,long)"""
        __JNI.callPJV(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def callPJJPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPJJPV(long,long,long,long,long)"""
        __JNI.callPJJPV(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokePPPPNP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokePPPPNP(long,long,int,long,long,long,long)"""
        return int.__wrap(__JNI.invokePPPPNP(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static native int org.lwjgl.system.JNI.callPPPI(long,int,int,long,long,long)"""
        return int.__wrap(__JNI.callPPPI(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def callPPPPPV(arg0: int, arg1: int, arg2: int, arg3: 'int', arg4: 'int', arg5: 'int', arg6: 'int', arg7: int):
        """public static native void org.lwjgl.system.JNI.callPPPPPV(int,int,long,int[],int[],int[],int[],long)"""
        __JNI.callPPPPPV(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3, arg4, arg5, arg6, __long.valueOf(arg7))

    @staticmethod
    @overload
    def callPPJPP(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.JNI.callPPJPP(long,long,long,long,long)"""
        return int.__wrap(__JNI.callPPJPP(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callI(arg0: int, arg1: float, arg2: int) -> int:
        """public static native int org.lwjgl.system.JNI.callI(int,float,long)"""
        return int.__wrap(__JNI.callI(__int.valueOf(arg0), __float.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def invokeP(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.JNI.invokeP(int,int,long)"""
        return int.__wrap(__JNI.invokeP(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callPV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPV(int,int,int,long,long)"""
        __JNI.callPV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def invokeCPCV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.invokeCPCV(short,long,short,long)"""
        __JNI.invokeCPCV(__short.valueOf(arg0), __long.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6))

    @staticmethod
    @overload
    def callBBBV(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.JNI.callBBBV(byte,byte,byte,long)"""
        __JNI.callBBBV(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def invokePPPV(arg0: int, arg1: int, arg2: 'long', arg3: 'long', arg4: 'long', arg5: int):
        """public static native void org.lwjgl.system.JNI.invokePPPV(int,int,long[],long[],long[],long)"""
        __JNI.invokePPPV(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, arg4, __long.valueOf(arg5))

    @staticmethod
    @overload
    def callPCSPPPS(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native short org.lwjgl.system.JNI.callPCSPPPS(long,short,short,long,long,long,long)"""
        return int.__wrap(__JNI.callPCSPPPS(__long.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def callPPZ(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static native boolean org.lwjgl.system.JNI.callPPZ(long,int,long,long)"""
        return bool.__wrap(__JNI.callPPZ(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def callJPI(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.JNI.callJPI(long,long,int,int,long)"""
        return int.__wrap(__JNI.callJPI(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def callV(arg0: bool, arg1: int):
        """public static native void org.lwjgl.system.JNI.callV(boolean,long)"""
        __JNI.callV(__boolean.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def callJV(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: bool, arg7: int, arg8: int, arg9: int):
        """public static native void org.lwjgl.system.JNI.callJV(int,int,int,int,int,int,boolean,int,long,long)"""
        __JNI.callJV(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9))

    @staticmethod
    @overload
    def callPPV(arg0: int, arg1: 'int', arg2: 'int', arg3: int, arg4: int):
        """public static native void org.lwjgl.system.JNI.callPPV(int,int[],int[],int,long)"""
        __JNI.callPPV(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __long.valueOf(arg4)) 
 
 
# CLASS: org.lwjgl.system.SharedLibrary
import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.CharSequence as CharSequence
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.Pointer as __Pointer
__Pointer = __Pointer
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
from abc import abstractmethod, ABC
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class SharedLibrary(ABC, __FunctionProvider, FunctionProvider, __NativeResource, NativeResource, __Pointer, Pointer):
    """org.lwjgl.system.SharedLibrary"""
 
    @staticmethod
    def __wrap(java_value: __SharedLibrary) -> 'SharedLibrary':
        return SharedLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SharedLibrary):
        """
        Dynamic initializer for SharedLibrary.
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
    def getName(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getName()"""
        pass

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass

    @abstractmethod
    def address(self, ):
        """public abstract long org.lwjgl.system.Pointer.address()"""
        pass 
 
 
# CLASS: org.lwjgl.system.SharedLibrary$Delegate
from builtins import str
import java.lang.CharSequence as CharSequence
import org.lwjgl.system.SharedLibrary as __SharedLibrary_Delegate
__Delegate = __SharedLibrary_Delegate.Delegate
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class Delegate(ABC, __SharedLibrary, SharedLibrary):
    """org.lwjgl.system.SharedLibrary.Delegate"""
 
    @staticmethod
    def __wrap(java_value: __Delegate) -> 'Delegate':
        return Delegate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Delegate):
        """
        Dynamic initializer for Delegate.
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
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Delegate.getName()"""
        return str.__wrap(super(Delegate, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.SharedLibrary$Delegate.address()"""
        return int.__wrap(super(Delegate, self).address())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.SharedLibrary$Delegate.free()"""
        super(Delegate, self).free()

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Delegate.getPath()"""
        return str.__wrap(super(Delegate, self).getPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.APIUtil$Encoder
import org.lwjgl.system.APIUtil as __APIUtil_Encoder
__Encoder = __APIUtil_Encoder.Encoder
import java.lang.CharSequence as CharSequence
from abc import abstractmethod, ABC
 
class Encoder(ABC):
    """org.lwjgl.system.APIUtil.Encoder"""
 
    @staticmethod
    def __wrap(java_value: __Encoder) -> 'Encoder':
        return Encoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Encoder):
        """
        Dynamic initializer for Encoder.
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
    def encode(self, arg0: 'CharSequence', arg1: bool):
        """public abstract java.nio.ByteBuffer org.lwjgl.system.APIUtil$Encoder.encode(java.lang.CharSequence,boolean)"""
        pass 
 
 
# CLASS: org.lwjgl.system.Pointer$Default
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Default(ABC, __Pointer, Pointer):
    """org.lwjgl.system.Pointer.Default"""
 
    @staticmethod
    def __wrap(java_value: __Default) -> 'Default':
        return Default(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Default):
        """
        Dynamic initializer for Default.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(Default, self).address())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.system.FunctionProvider
import java.lang.CharSequence as CharSequence
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
import java.nio.ByteBuffer as ByteBuffer
from abc import abstractmethod, ABC
from builtins import int
 
class FunctionProvider(ABC):
    """org.lwjgl.system.FunctionProvider"""
 
    @staticmethod
    def __wrap(java_value: __FunctionProvider) -> 'FunctionProvider':
        return FunctionProvider(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FunctionProvider):
        """
        Dynamic initializer for FunctionProvider.
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
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.MemoryStack
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import java.nio.IntBuffer as IntBuffer
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.CLongBuffer as __CLongBuffer
__CLongBuffer = __CLongBuffer
import org.lwjgl.system.MemoryStack as __MemoryStack
__MemoryStack = __MemoryStack
import java.lang.Short as __short
import java.lang.Double as __double
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class MemoryStack(__Default, Default, __AutoCloseable, AutoCloseable):
    """org.lwjgl.system.MemoryStack"""
 
    @staticmethod
    def __wrap(java_value: __MemoryStack) -> 'MemoryStack':
        return MemoryStack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryStack):
        """
        Dynamic initializer for MemoryStack.
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
 
    @staticmethod
    @overload
    def stackUTF8(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF8(arg0))

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long,long)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).longs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def UTF16(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF16(arg0, __boolean.valueOf(arg1)))

    @overload
    def clongs(self, arg0: int, arg1: int, arg2: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long,long)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).clongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stackPointers(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackASCIISafe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCIISafe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackASCIISafe(arg0))

    @overload
    def ASCIISafe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCIISafe(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).ASCIISafe(arg0))

    @staticmethod
    @overload
    def stackCallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackCallocInt(int)"""
        return IntBuffer.__wrap(__MemoryStack.stackCallocInt(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long,long,long)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCLongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @overload
    def shorts(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).shorts(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nstackMalloc(arg0: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackMalloc(int)"""
        return int.__wrap(__MemoryStack.nstackMalloc(__int.valueOf(arg0)))

    @overload
    def mallocDouble(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.mallocDouble(int)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).mallocDouble(__int.valueOf(arg0)))

    @overload
    def doubles(self, arg0: float, arg1: float, arg2: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double,double)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).doubles(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def mallocLong(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.mallocLong(int)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).mallocLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer', arg3: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0, arg1, arg2, arg3))

    @overload
    def shorts(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short,short,short)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).shorts(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3)))

    @staticmethod
    @overload
    def stackPush() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackPush()"""
        return MemoryStack.__wrap(__MemoryStack.stackPush())

    @overload
    def bytes(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).bytes(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def stackMallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackMallocPointer(int)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackMallocPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float, arg2: float, arg3: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float,float,float)"""
        return FloatBuffer.__wrap(__MemoryStack.stackFloats(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def ints(self, arg0: int, arg1: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).ints(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def calloc(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.calloc(int)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).calloc(__int.valueOf(arg0)))

    @overload
    def ints(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).ints(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(Default, self).toString())

    @staticmethod
    @overload
    def stackCallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackCallocLong(int)"""
        return LongBuffer.__wrap(__MemoryStack.stackCallocLong(__int.valueOf(arg0)))

    @overload
    def pointersOfElements(self, arg0: 'CustomBuffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointersOfElements(org.lwjgl.system.CustomBuffer<?>)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointersOfElements(arg0))

    @overload
    def doubles(self, *arg0: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double...)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).doubles(arg0))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int,int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).ints(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def floats(self, arg0: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).floats(__float.valueOf(arg0)))

    @overload
    def pointers(self, *arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer...)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0))

    @overload
    def doubles(self, arg0: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).doubles(__double.valueOf(arg0)))

    @overload
    def nlong(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nlong(long)"""
        return int.__wrap(super(__MemoryStack, self).nlong(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def UTF8(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF8(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackASCII(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCII(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackASCII(arg0, __boolean.valueOf(arg1)))

    @overload
    def nint(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nint(int)"""
        return int.__wrap(super(__MemoryStack, self).nint(__int.valueOf(arg0)))

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer', arg3: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def stackASCII(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCII(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackASCII(arg0))

    @overload
    def pop(self) -> 'MemoryStack':
        """public org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.pop()"""
        return 'MemoryStack'.__wrap(super(MemoryStack, self).pop())

    @staticmethod
    @overload
    def stackCallocPointer(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackCallocPointer(int)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackCallocPointer(__int.valueOf(arg0)))

    @overload
    def bytes(self, arg0: int, arg1: int, arg2: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte,byte)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).bytes(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2)))

    @staticmethod
    @overload
    def stackShorts(*arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short...)"""
        return ShortBuffer.__wrap(__MemoryStack.stackShorts(arg0))

    @overload
    def push(self) -> 'MemoryStack':
        """public org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.push()"""
        return 'MemoryStack'.__wrap(super(MemoryStack, self).push())

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float, arg2: float, arg3: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double,double,double)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackDoubles(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @overload
    def nUTF8Safe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF8Safe(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nUTF8Safe(arg0, __boolean.valueOf(arg1)))

    @overload
    def getPointerAddress(self) -> int:
        """public long org.lwjgl.system.MemoryStack.getPointerAddress()"""
        return int.__wrap(super(MemoryStack, self).getPointerAddress())

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def callocShort(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.callocShort(int)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).callocShort(__int.valueOf(arg0)))

    @overload
    def ints(self, *arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int...)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).ints(arg0))

    @overload
    def pointers(self, arg0: int, arg1: int, arg2: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long,long)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer', arg2: 'Buffer', arg3: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer,java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1, arg2, arg3))

    @overload
    def malloc(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.malloc(int)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).malloc(__int.valueOf(arg0)))

    @overload
    def calloc(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.calloc(int,int)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).calloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stackInts(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int)"""
        return IntBuffer.__wrap(__MemoryStack.stackInts(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF16Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF16Safe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackCallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCallocCLong(int)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCallocCLong(__int.valueOf(arg0)))

    @overload
    def npointer(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(long)"""
        return int.__wrap(super(__MemoryStack, self).npointer(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackGet() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackGet()"""
        return MemoryStack.__wrap(__MemoryStack.stackGet())

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int, arg2: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long,long)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCLongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @overload
    def shorts(self, arg0: int, arg1: int, arg2: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short,short)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).shorts(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer', arg2: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1, arg2))

    @overload
    def nASCII(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nASCII(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nASCII(arg0, __boolean.valueOf(arg1)))

    @overload
    def nUTF16Safe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF16Safe(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nUTF16Safe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte)"""
        return ByteBuffer.__wrap(__MemoryStack.stackBytes(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackDoubles(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def mallocShort(self, arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.mallocShort(int)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).mallocShort(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackMallocInt(arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackMallocInt(int)"""
        return IntBuffer.__wrap(__MemoryStack.stackMallocInt(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(*arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long...)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0))

    @overload
    def doubles(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double,double,double)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).doubles(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2), __double.valueOf(arg3)))

    @staticmethod
    @overload
    def stackMallocCLong(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackMallocCLong(int)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackMallocCLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF16(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF16(arg0, __boolean.valueOf(arg1)))

    @overload
    def setPointer(self, arg0: int):
        """public void org.lwjgl.system.MemoryStack.setPointer(int)"""
        super(__MemoryStack, self).setPointer(__int.valueOf(arg0))

    @staticmethod
    @overload
    def stackDoubles(*arg0: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double...)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackDoubles(arg0))

    @overload
    def pointers(self, arg0: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackCLongs(*arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long...)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCLongs(arg0))

    @overload
    def ints(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.ints(int,int,int,int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).ints(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def mallocPointer(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.mallocPointer(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).mallocPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nstackCalloc(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackCalloc(int,int,int)"""
        return int.__wrap(__MemoryStack.nstackCalloc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create(int)"""
        return MemoryStack.__wrap(__MemoryStack.create(__int.valueOf(arg0)))

    @overload
    def bytes(self, *arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte...)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).bytes(bytes))

    @overload
    def longs(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).longs(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int, arg2: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int,int)"""
        return IntBuffer.__wrap(__MemoryStack.stackInts(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def stackFloats(*arg0: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float...)"""
        return FloatBuffer.__wrap(__MemoryStack.stackFloats(arg0))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float, arg2: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float,float)"""
        return FloatBuffer.__wrap(__MemoryStack.stackFloats(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def nshort(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nshort(short)"""
        return int.__wrap(super(__MemoryStack, self).nshort(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int, arg2: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long,long)"""
        return LongBuffer.__wrap(__MemoryStack.stackLongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def stackCalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackCalloc(int)"""
        return ByteBuffer.__wrap(__MemoryStack.stackCalloc(__int.valueOf(arg0)))

    @overload
    def shorts(self, arg0: int, arg1: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short,short)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).shorts(__short.valueOf(arg0), __short.valueOf(arg1)))

    @overload
    def pointers(self, *arg0: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer...)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0))

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long)"""
        return LongBuffer.__wrap(__MemoryStack.stackLongs(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def stackLongs(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long)"""
        return LongBuffer.__wrap(__MemoryStack.stackLongs(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int)"""
        return IntBuffer.__wrap(__MemoryStack.stackInts(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ndouble(self, arg0: float) -> int:
        """public long org.lwjgl.system.MemoryStack.ndouble(double)"""
        return int.__wrap(super(__MemoryStack, self).ndouble(__double.valueOf(arg0)))

    @overload
    def floats(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float,float,float)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).floats(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def stackASCIISafe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackASCIISafe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackASCIISafe(arg0, __boolean.valueOf(arg1)))

    @overload
    def nfloat(self, arg0: float) -> int:
        """public long org.lwjgl.system.MemoryStack.nfloat(float)"""
        return int.__wrap(super(__MemoryStack, self).nfloat(__float.valueOf(arg0)))

    @overload
    def ncalloc(self, arg0: int, arg1: int, arg2: int) -> int:
        """public long org.lwjgl.system.MemoryStack.ncalloc(int,int,int)"""
        return int.__wrap(super(__MemoryStack, self).ncalloc(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(Default, self).address())

    @overload
    def floats(self, *arg0: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float...)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).floats(arg0))

    @staticmethod
    @overload
    def stackUTF16(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF16(arg0))

    @staticmethod
    @overload
    def create(arg0: 'ByteBuffer') -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create(java.nio.ByteBuffer)"""
        return MemoryStack.__wrap(__MemoryStack.create(arg0))

    @staticmethod
    @overload
    def stackMalloc(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackMalloc(int)"""
        return ByteBuffer.__wrap(__MemoryStack.stackMalloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackMallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackMallocFloat(int)"""
        return FloatBuffer.__wrap(__MemoryStack.stackMallocFloat(__int.valueOf(arg0)))

    @overload
    def shorts(self, *arg0: int) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.system.MemoryStack.shorts(short...)"""
        return 'ShortBuffer'.__wrap(super(__MemoryStack, self).shorts(arg0))

    @overload
    def npointer(self, arg0: 'Buffer') -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(java.nio.Buffer)"""
        return int.__wrap(super(__MemoryStack, self).npointer(arg0))

    @overload
    def UTF16Safe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16Safe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF16Safe(arg0, __boolean.valueOf(arg1)))

    @overload
    def callocCLong(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.callocCLong(int)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).callocCLong(__int.valueOf(arg0)))

    @overload
    def callocInt(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.callocInt(int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).callocInt(__int.valueOf(arg0)))

    @overload
    def pointers(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackCallocDouble(int)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackCallocDouble(__int.valueOf(arg0)))

    @overload
    def malloc(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.malloc(int,int)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).malloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clongs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long,long,long)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).clongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stackInts(*arg0: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int...)"""
        return IntBuffer.__wrap(__MemoryStack.stackInts(arg0))

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long,long,long)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def npointer(self, arg0: 'Pointer') -> int:
        """public long org.lwjgl.system.MemoryStack.npointer(org.lwjgl.system.Pointer)"""
        return int.__wrap(super(__MemoryStack, self).npointer(arg0))

    @overload
    def UTF8Safe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8Safe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF8Safe(arg0, __boolean.valueOf(arg1)))

    @overload
    def floats(self, arg0: float, arg1: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).floats(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @staticmethod
    @overload
    def stackMallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackMallocShort(int)"""
        return ShortBuffer.__wrap(__MemoryStack.stackMallocShort(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackPointers(*arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer...)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0))

    @overload
    def UTF8(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF8(arg0))

    @overload
    def doubles(self, arg0: float, arg1: float) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.doubles(double,double)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).doubles(__double.valueOf(arg0), __double.valueOf(arg1)))

    @overload
    def ASCII(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCII(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).ASCII(arg0, __boolean.valueOf(arg1)))

    @overload
    def getPointer(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getPointer()"""
        return int.__wrap(super(MemoryStack, self).getPointer())

    @staticmethod
    @overload
    def stackPointers(arg0: int, arg1: int, arg2: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(long,long,long)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @overload
    def UTF16(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF16(arg0))

    @overload
    def callocDouble(self, arg0: int) -> 'DoubleBuffer':
        """public java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.callocDouble(int)"""
        return 'DoubleBuffer'.__wrap(super(__MemoryStack, self).callocDouble(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackLongs(*arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long...)"""
        return LongBuffer.__wrap(__MemoryStack.stackLongs(arg0))

    @staticmethod
    @overload
    def stackBytes(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte)"""
        return ByteBuffer.__wrap(__MemoryStack.stackBytes(__byte.valueOf(arg0)))

    @overload
    def getSize(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getSize()"""
        return int.__wrap(super(MemoryStack, self).getSize())

    @overload
    def bytes(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte,byte,byte)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).bytes(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3)))

    @staticmethod
    @overload
    def stackCLongs(arg0: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCLongs(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nstackMalloc(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MemoryStack.nstackMalloc(int,int)"""
        return int.__wrap(__MemoryStack.nstackMalloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int, arg2: int, arg3: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short,short,short)"""
        return ShortBuffer.__wrap(__MemoryStack.stackShorts(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2), __short.valueOf(arg3)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int, arg2: int, arg3: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte,byte,byte)"""
        return ByteBuffer.__wrap(__MemoryStack.stackBytes(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2), __byte.valueOf(arg3)))

    @staticmethod
    @overload
    def stackCallocFloat(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackCallocFloat(int)"""
        return FloatBuffer.__wrap(__MemoryStack.stackCallocFloat(__int.valueOf(arg0)))

    @overload
    def UTF8Safe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF8Safe(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF8Safe(arg0))

    @overload
    def nbyte(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nbyte(byte)"""
        return int.__wrap(super(__MemoryStack, self).nbyte(__byte.valueOf(arg0)))

    @overload
    def pointers(self, arg0: int, arg1: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def nASCIISafe(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nASCIISafe(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nASCIISafe(arg0, __boolean.valueOf(arg1)))

    @overload
    def ASCIISafe(self, arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCIISafe(java.lang.CharSequence,boolean)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).ASCIISafe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0, arg1))

    @overload
    def nUTF8(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF8(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nUTF8(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackMallocLong(arg0: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackMallocLong(int)"""
        return LongBuffer.__wrap(__MemoryStack.stackMallocLong(__int.valueOf(arg0)))

    @overload
    def pointers(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long,long,long,long)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stackMallocDouble(arg0: int) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackMallocDouble(int)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackMallocDouble(__int.valueOf(arg0)))

    @overload
    def mallocInt(self, arg0: int) -> 'IntBuffer':
        """public java.nio.IntBuffer org.lwjgl.system.MemoryStack.mallocInt(int)"""
        return 'IntBuffer'.__wrap(super(__MemoryStack, self).mallocInt(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackBytes(*arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte...)"""
        return ByteBuffer.__wrap(__MemoryStack.stackBytes(bytes))

    @staticmethod
    @overload
    def stackUTF16Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF16Safe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF16Safe(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

    @overload
    def getFrameIndex(self) -> int:
        """public int org.lwjgl.system.MemoryStack.getFrameIndex()"""
        return int.__wrap(super(MemoryStack, self).getFrameIndex())

    @overload
    def pointers(self, arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0))

    @overload
    def mallocCLong(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.mallocCLong(int)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).mallocCLong(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackCLongs(arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public static org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.stackCLongs(long,long)"""
        return pygl.CLongBuffer.__wrap(__MemoryStack.stackCLongs(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float, arg1: float, arg2: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double,double,double)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackDoubles(__double.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2)))

    @overload
    def longs(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long,long,long)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).longs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stackUTF8Safe(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8Safe(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF8Safe(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.create()"""
        return MemoryStack.__wrap(__MemoryStack.create())

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0))

    @overload
    def floats(self, arg0: float, arg1: float, arg2: float) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.floats(float,float,float)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).floats(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def callocLong(self, arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.callocLong(int)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).callocLong(__int.valueOf(arg0)))

    @overload
    def bytes(self, arg0: int, arg1: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.bytes(byte,byte)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).bytes(__byte.valueOf(arg0), __byte.valueOf(arg1)))

    @overload
    def nclong(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nclong(long)"""
        return int.__wrap(super(__MemoryStack, self).nclong(__long.valueOf(arg0)))

    @overload
    def clongs(self, *arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long...)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).clongs(arg0))

    @overload
    def callocPointer(self, arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.callocPointer(int)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).callocPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackDoubles(arg0: float) -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.MemoryStack.stackDoubles(double)"""
        return DoubleBuffer.__wrap(__MemoryStack.stackDoubles(__double.valueOf(arg0)))

    @overload
    def longs(self, arg0: int, arg1: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long,long)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).longs(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def ASCII(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.ASCII(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).ASCII(arg0))

    @staticmethod
    @overload
    def stackInts(arg0: int, arg1: int, arg2: int, arg3: int) -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.MemoryStack.stackInts(int,int,int,int)"""
        return IntBuffer.__wrap(__MemoryStack.stackInts(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def stackFloats(arg0: float, arg1: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float,float)"""
        return FloatBuffer.__wrap(__MemoryStack.stackFloats(__float.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def stackUTF8(arg0: 'CharSequence', arg1: bool) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8(java.lang.CharSequence,boolean)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF8(arg0, __boolean.valueOf(arg1)))

    @overload
    def pointers(self, arg0: 'Pointer', arg1: 'Pointer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1))

    @overload
    def longs(self, *arg0: int) -> 'LongBuffer':
        """public java.nio.LongBuffer org.lwjgl.system.MemoryStack.longs(long...)"""
        return 'LongBuffer'.__wrap(super(__MemoryStack, self).longs(arg0))

    @staticmethod
    @overload
    def stackCallocShort(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackCallocShort(int)"""
        return ShortBuffer.__wrap(__MemoryStack.stackCallocShort(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int, arg2: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short,short)"""
        return ShortBuffer.__wrap(__MemoryStack.stackShorts(__short.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @overload
    def UTF16Safe(self, arg0: 'CharSequence') -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.MemoryStack.UTF16Safe(java.lang.CharSequence)"""
        return 'ByteBuffer'.__wrap(super(__MemoryStack, self).UTF16Safe(arg0))

    @staticmethod
    @overload
    def stackPop() -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.stackPop()"""
        return MemoryStack.__wrap(__MemoryStack.stackPop())

    @overload
    def nUTF16(self, arg0: 'CharSequence', arg1: bool) -> int:
        """public int org.lwjgl.system.MemoryStack.nUTF16(java.lang.CharSequence,boolean)"""
        return int.__wrap(super(__MemoryStack, self).nUTF16(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def stackPointers(arg0: 'Pointer', arg1: 'Pointer', arg2: 'Pointer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.stackPointers(org.lwjgl.system.Pointer,org.lwjgl.system.Pointer,org.lwjgl.system.Pointer)"""
        return pygl.PointerBuffer.__wrap(__MemoryStack.stackPointers(arg0, arg1, arg2))

    @override
    @overload
    def close(self):
        """public void org.lwjgl.system.MemoryStack.close()"""
        super(MemoryStack, self).close()

    @overload
    def pointers(self, *arg0: int) -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(long...)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0))

    @overload
    def getAddress(self) -> int:
        """public long org.lwjgl.system.MemoryStack.getAddress()"""
        return int.__wrap(super(MemoryStack, self).getAddress())

    @overload
    def clongs(self, arg0: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).clongs(__long.valueOf(arg0)))

    @overload
    def clongs(self, arg0: int, arg1: int) -> 'pygl.CLongBuffer':
        """public org.lwjgl.CLongBuffer org.lwjgl.system.MemoryStack.clongs(long,long)"""
        return 'pygl.CLongBuffer'.__wrap(super(__MemoryStack, self).clongs(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def nmalloc(self, arg0: int, arg1: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nmalloc(int,int)"""
        return int.__wrap(super(__MemoryStack, self).nmalloc(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def stackShorts(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short)"""
        return ShortBuffer.__wrap(__MemoryStack.stackShorts(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def stackUTF8Safe(arg0: 'CharSequence') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackUTF8Safe(java.lang.CharSequence)"""
        return ByteBuffer.__wrap(__MemoryStack.stackUTF8Safe(arg0))

    @overload
    def pointers(self, arg0: 'Buffer', arg1: 'Buffer') -> 'pygl.PointerBuffer':
        """public org.lwjgl.PointerBuffer org.lwjgl.system.MemoryStack.pointers(java.nio.Buffer,java.nio.Buffer)"""
        return 'pygl.PointerBuffer'.__wrap(super(__MemoryStack, self).pointers(arg0, arg1))

    @staticmethod
    @overload
    def ncreate(arg0: int, arg1: int) -> 'MemoryStack':
        """public static org.lwjgl.system.MemoryStack org.lwjgl.system.MemoryStack.ncreate(long,int)"""
        return MemoryStack.__wrap(__MemoryStack.ncreate(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def nmalloc(self, arg0: int) -> int:
        """public long org.lwjgl.system.MemoryStack.nmalloc(int)"""
        return int.__wrap(super(__MemoryStack, self).nmalloc(__int.valueOf(arg0)))

    @overload
    def mallocFloat(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.mallocFloat(int)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).mallocFloat(__int.valueOf(arg0)))

    @overload
    def callocFloat(self, arg0: int) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.system.MemoryStack.callocFloat(int)"""
        return 'FloatBuffer'.__wrap(super(__MemoryStack, self).callocFloat(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def stackShorts(arg0: int, arg1: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.MemoryStack.stackShorts(short,short)"""
        return ShortBuffer.__wrap(__MemoryStack.stackShorts(__short.valueOf(arg0), __short.valueOf(arg1)))

    @staticmethod
    @overload
    def stackFloats(arg0: float) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.MemoryStack.stackFloats(float)"""
        return FloatBuffer.__wrap(__MemoryStack.stackFloats(__float.valueOf(arg0)))

    @staticmethod
    @overload
    def stackLongs(arg0: int, arg1: int, arg2: int, arg3: int) -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.MemoryStack.stackLongs(long,long,long,long)"""
        return LongBuffer.__wrap(__MemoryStack.stackLongs(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def stackBytes(arg0: int, arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.MemoryStack.stackBytes(byte,byte,byte)"""
        return ByteBuffer.__wrap(__MemoryStack.stackBytes(__byte.valueOf(arg0), __byte.valueOf(arg1), __byte.valueOf(arg2))) 
 
 
# CLASS: org.lwjgl.system.NativeType
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import org.lwjgl.system.NativeType as __NativeType
__NativeType = __NativeType
 
class NativeType(ABC, __Annotation, Annotation):
    """org.lwjgl.system.NativeType"""
 
    @staticmethod
    def __wrap(java_value: __NativeType) -> 'NativeType':
        return NativeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NativeType):
        """
        Dynamic initializer for NativeType.
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
    def value(self, ):
        """public abstract java.lang.String org.lwjgl.system.NativeType.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Struct$StructValidation
import org.lwjgl.system.Struct as __Struct_StructValidation
__StructValidation = __Struct_StructValidation.StructValidation
from abc import abstractmethod, ABC
 
class StructValidation(ABC):
    """org.lwjgl.system.Struct.StructValidation"""
 
    @staticmethod
    def __wrap(java_value: __StructValidation) -> 'StructValidation':
        return StructValidation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StructValidation):
        """
        Dynamic initializer for StructValidation.
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
    def validate(self, arg0: int):
        """public abstract void org.lwjgl.system.Struct$StructValidation.validate(long)"""
        pass 
 
 
# CLASS: org.lwjgl.system.APIUtil$APIVersion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.APIUtil as __APIUtil_APIVersion
__APIVersion = __APIUtil_APIVersion.APIVersion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class APIVersion(__Comparable, Comparable):
    """org.lwjgl.system.APIUtil.APIVersion"""
 
    @staticmethod
    def __wrap(java_value: __APIVersion) -> 'APIVersion':
        return APIVersion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __APIVersion):
        """
        Dynamic initializer for APIVersion.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.APIUtil$APIVersion.hashCode()"""
        return int.__wrap(super(APIVersion, self).hashCode())

    @overload
    def compareTo(self, arg0: 'APIVersion') -> int:
        """public int org.lwjgl.system.APIUtil$APIVersion.compareTo(org.lwjgl.system.APIUtil$APIVersion)"""
        return int.__wrap(super(__APIVersion, self).compareTo(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str, arg3: str):
        """public org.lwjgl.system.APIUtil$APIVersion(int,int,java.lang.String,java.lang.String)"""
        val = __APIVersion(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.APIUtil$APIVersion.equals(java.lang.Object)"""
        return bool.__wrap(super(__APIVersion, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.APIUtil$APIVersion(int,int)"""
        val = __APIVersion(__int.valueOf(arg0), __int.valueOf(arg1))
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.APIUtil$APIVersion.toString()"""
        return str.__wrap(super(APIVersion, self).toString()) 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocationReport
import org.lwjgl.system.MemoryUtil as __MemoryUtil_MemoryAllocationReport
__MemoryAllocationReport = __MemoryUtil_MemoryAllocationReport.MemoryAllocationReport
from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
 
class MemoryAllocationReport(ABC):
    """org.lwjgl.system.MemoryUtil.MemoryAllocationReport"""
 
    @staticmethod
    def __wrap(java_value: __MemoryAllocationReport) -> 'MemoryAllocationReport':
        return MemoryAllocationReport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MemoryAllocationReport):
        """
        Dynamic initializer for MemoryAllocationReport.
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
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: str, *arg4: 'StackTraceElement'):
        """public abstract void org.lwjgl.system.MemoryUtil$MemoryAllocationReport.invoke(long,long,long,java.lang.String,java.lang.StackTraceElement...)"""
        pass 
 
 
# CLASS: org.lwjgl.system.Callback
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Callback(ABC, __Pointer, Pointer, __NativeResource, NativeResource):
    """org.lwjgl.system.Callback"""
 
    @staticmethod
    def __wrap(java_value: __Callback) -> 'Callback':
        return Callback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Callback):
        """
        Dynamic initializer for Callback.
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
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(Callback, self).free()

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(Callback, self).hashCode())

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

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
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(Callback, self).toString())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(NativeResource, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__Callback, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(Callback, self).address()) 
 
 
# CLASS: org.lwjgl.system.Platform
from builtins import str
import org.lwjgl.system.Platform as __Platform
__Platform = __Platform
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import org.lwjgl.system.Platform as __Platform_Architecture
__Architecture = __Platform_Architecture.Architecture
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Platform(ABC, __Enum, Enum):
    """org.lwjgl.system.Platform"""
 
    @staticmethod
    def __wrap(java_value: __Platform) -> 'Platform':
        return Platform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Platform):
        """
        Dynamic initializer for Platform.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['Platform']:
        """public static org.lwjgl.system.Platform[] org.lwjgl.system.Platform.values()"""
        return List[Platform].__wrap(__Platform.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def get() -> 'Platform':
        """public static org.lwjgl.system.Platform org.lwjgl.system.Platform.get()"""
        return Platform.__wrap(__Platform.get())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Platform':
        """public static org.lwjgl.system.Platform org.lwjgl.system.Platform.valueOf(java.lang.String)"""
        return Platform.__wrap(__Platform.valueOf(arg0))

    @staticmethod
    @overload
    def getArchitecture() -> 'Architecture':
        """public static org.lwjgl.system.Platform$Architecture org.lwjgl.system.Platform.getArchitecture()"""
        return Architecture.__wrap(__Platform.getArchitecture())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.Platform.getName()"""
        return str.__wrap(super(Platform, self).getName())

    @staticmethod
    @overload
    def mapLibraryNameBundled(arg0: str) -> str:
        """public static java.lang.String org.lwjgl.system.Platform.mapLibraryNameBundled(java.lang.String)"""
        return str.__wrap(__Platform.mapLibraryNameBundled(arg0)) 
 
 
# CLASS: org.lwjgl.system.FunctionProviderLocal
import java.lang.CharSequence as CharSequence
import java.lang.Long as __long
import org.lwjgl.system.FunctionProviderLocal as __FunctionProviderLocal
__FunctionProviderLocal = __FunctionProviderLocal
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
import java.nio.ByteBuffer as ByteBuffer
from abc import abstractmethod, ABC
from builtins import int
 
class FunctionProviderLocal(ABC, __FunctionProvider, FunctionProvider):
    """org.lwjgl.system.FunctionProviderLocal"""
 
    @staticmethod
    def __wrap(java_value: __FunctionProviderLocal) -> 'FunctionProviderLocal':
        return FunctionProviderLocal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FunctionProviderLocal):
        """
        Dynamic initializer for FunctionProviderLocal.
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
    def getFunctionAddress(self, arg0: int, arg1: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProviderLocal.getFunctionAddress(long,java.nio.ByteBuffer)"""
        pass

    @overload
    def getFunctionAddress(self, arg0: int, arg1: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProviderLocal.getFunctionAddress(long,java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProviderLocal, self).getFunctionAddress(__long.valueOf(arg0), arg1))

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__FunctionProvider, self).getFunctionAddress(arg0))

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.SharedLibraryUtil
from builtins import str
import java.lang.Long as __long
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
import org.lwjgl.system.SharedLibraryUtil as __SharedLibraryUtil
__SharedLibraryUtil = __SharedLibraryUtil
from builtins import int
 
class SharedLibraryUtil():
    """org.lwjgl.system.SharedLibraryUtil"""
 
    @staticmethod
    def __wrap(java_value: __SharedLibraryUtil) -> 'SharedLibraryUtil':
        return SharedLibraryUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SharedLibraryUtil):
        """
        Dynamic initializer for SharedLibraryUtil.
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getLibraryPath(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.SharedLibraryUtil.getLibraryPath(long)"""
        return str.__wrap(__SharedLibraryUtil.getLibraryPath(__long.valueOf(arg0)))

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
    def __init__(self, ):
        """public org.lwjgl.system.SharedLibraryUtil()"""
        val = __SharedLibraryUtil()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public org.lwjgl.system.SharedLibraryUtil()"""
        val = __SharedLibraryUtil()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.system.CheckIntrinsics
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CheckIntrinsics as __CheckIntrinsics
__CheckIntrinsics = __CheckIntrinsics
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CheckIntrinsics():
    """org.lwjgl.system.CheckIntrinsics"""
 
    @staticmethod
    def __wrap(java_value: __CheckIntrinsics) -> 'CheckIntrinsics':
        return CheckIntrinsics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CheckIntrinsics):
        """
        Dynamic initializer for CheckIntrinsics.
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

    @staticmethod
    @overload
    def checkFromToIndex(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkFromToIndex(int,int,int)"""
        return int.__wrap(__CheckIntrinsics.checkFromToIndex(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def checkIndex(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkIndex(int,int)"""
        return int.__wrap(__CheckIntrinsics.checkIndex(__int.valueOf(arg0), __int.valueOf(arg1)))

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

    @staticmethod
    @overload
    def checkFromIndexSize(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.CheckIntrinsics.checkFromIndexSize(int,int,int)"""
        return int.__wrap(__CheckIntrinsics.checkFromIndexSize(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: org.lwjgl.system.Struct$Layout
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.Struct as __Struct_Layout
__Layout = __Struct_Layout.Layout
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct_Member
__Member = __Struct_Member.Member
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Layout(__Member, Member):
    """org.lwjgl.system.Struct.Layout"""
 
    @staticmethod
    def __wrap(java_value: __Layout) -> 'Layout':
        return Layout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Layout):
        """
        Dynamic initializer for Layout.
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
    def offsetof(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Layout.offsetof(int)"""
        return int.__wrap(super(__Layout, self).offsetof(__int.valueOf(arg0)))

    @overload
    def getAlignment(self, arg0: int) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment(int)"""
        return int.__wrap(super(__Member, self).getAlignment(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getAlignment(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getAlignment()"""
        return int.__wrap(super(Member, self).getAlignment())

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

    @override
    @overload
    def getSize(self) -> int:
        """public int org.lwjgl.system.Struct$Member.getSize()"""
        return int.__wrap(super(Member, self).getSize()) 
 
 
# CLASS: org.lwjgl.system.CustomBuffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CustomBuffer(ABC, __Default, Default):
    """org.lwjgl.system.CustomBuffer"""
 
    @staticmethod
    def __wrap(java_value: __CustomBuffer) -> 'CustomBuffer':
        return CustomBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CustomBuffer):
        """
        Dynamic initializer for CustomBuffer.
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
    def rewind(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(CustomBuffer, self).hasRemaining())

    @overload
    def limit(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(CustomBuffer, self).address())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(CustomBuffer, self).position())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mark(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).mark())

    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(CustomBuffer, self).address0())

    @overload
    def reset(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).reset())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__CustomBuffer, self).address(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(CustomBuffer, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def position(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(CustomBuffer, self).capacity())

    @overload
    def duplicate(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).duplicate())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(CustomBuffer, self).free()

    @overload
    def clear(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).clear())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).put(arg0))

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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(CustomBuffer, self).remaining())

    @overload
    def flip(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).flip())

    @overload
    def compact(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).compact())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(CustomBuffer, self).limit())

    @overload
    def slice(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).slice())

    @abstractmethod
    def sizeof(self, ):
        """public abstract int org.lwjgl.system.CustomBuffer.sizeof()"""
        pass 
 
 
# CLASS: org.lwjgl.system.Configuration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.Configuration as __Configuration
__Configuration = __Configuration
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Configuration():
    """org.lwjgl.system.Configuration"""
 
    @staticmethod
    def __wrap(java_value: __Configuration) -> 'Configuration':
        return Configuration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Configuration):
        """
        Dynamic initializer for Configuration.
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

    @overload
    def set(self, arg0: object):
        """public void org.lwjgl.system.Configuration.set(T)"""
        super(__Configuration, self).set(arg0)

    @overload
    def get(self) -> object:
        """public T org.lwjgl.system.Configuration.get()"""
        return object.__wrap(super(Configuration, self).get())

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
    def get(self, arg0: object) -> object:
        """public T org.lwjgl.system.Configuration.get(T)"""
        return object.__wrap(super(__Configuration, self).get(arg0))

    @overload
    def getProperty(self) -> str:
        """public java.lang.String org.lwjgl.system.Configuration.getProperty()"""
        return str.__wrap(super(Configuration, self).getProperty())

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
 
 
# CLASS: org.lwjgl.system.CallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
from builtins import int
 
class CallbackI(ABC, __Pointer, Pointer):
    """org.lwjgl.system.CallbackI"""
 
    @staticmethod
    def __wrap(java_value: __CallbackI) -> 'CallbackI':
        return CallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CallbackI):
        """
        Dynamic initializer for CallbackI.
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
    def callback(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.system.CallbackI.callback(long,long)"""
        pass

    @abstractmethod
    def getCallInterface(self, ):
        """public abstract org.lwjgl.system.libffi.FFICIF org.lwjgl.system.CallbackI.getCallInterface()"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.system.StructBuffer
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.Spliterator as Spliterator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StructBuffer(ABC, __CustomBuffer, CustomBuffer, __Iterable, Iterable):
    """org.lwjgl.system.StructBuffer"""
 
    @staticmethod
    def __wrap(java_value: __StructBuffer) -> 'StructBuffer':
        return StructBuffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StructBuffer):
        """
        Dynamic initializer for StructBuffer.
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
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(CustomBuffer, self).remaining())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(CustomBuffer, self).hasRemaining())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def duplicate(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).duplicate())

    @overload
    def limit(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(StructBuffer, self).sizeof())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(CustomBuffer, self).address())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__Default, self).equals(arg0))

    @overload
    def get(self) -> 'Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'Struct'.__wrap(super(StructBuffer, self).get())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(Default, self).hashCode())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def get(self, arg0: int) -> 'Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'Struct'.__wrap(super(__StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def reset(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).reset())

    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(StructBuffer, self).stream())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(CustomBuffer, self).position())

    @overload
    def apply(self, arg0: 'Consumer') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).apply(arg0))

    @override
    @overload
    def compact(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).compact())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__CustomBuffer, self).address(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(CustomBuffer, self).toString())

    @override
    @overload
    def rewind(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).rewind())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def clear(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).clear())

    @overload
    def position(self, arg0: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def get(self, arg0: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).get(arg0))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'CustomBuffer'.__wrap(super(__CustomBuffer, self).put(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(StructBuffer, self).spliterator())

    @overload
    def put(self, arg0: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).put(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(StructBuffer, self).iterator())

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(CustomBuffer, self).limit())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(CustomBuffer, self).free()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__StructBuffer, self).forEach(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(StructBuffer, self).parallelStream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def slice(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).slice())

    @override
    @overload
    def mark(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).mark())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'StructBuffer'.__wrap(super(__StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(CustomBuffer, self).capacity())

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(CustomBuffer, self).address0())

    @override
    @overload
    def flip(self) -> 'CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'CustomBuffer'.__wrap(super(CustomBuffer, self).flip()) 
 
 
# CLASS: org.lwjgl.system.APIUtil
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import org.lwjgl.system.APIUtil as __APIUtil
__APIUtil = __APIUtil
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.Map as __Map
__Map = __Map
import org.lwjgl.system.APIUtil as __APIUtil_APIVersion
__APIVersion = __APIUtil_APIVersion.APIVersion
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
import java.lang.Double as __double
from builtins import bool
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.libffi.FFIType as __FFIType
__FFIType = __FFIType
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.util.Set as Set
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.util.function.BiPredicate as BiPredicate
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import java.util.Map as Map
from builtins import int
 
class APIUtil():
    """org.lwjgl.system.APIUtil"""
 
    @staticmethod
    def __wrap(java_value: __APIUtil) -> 'APIUtil':
        return APIUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __APIUtil):
        """
        Dynamic initializer for APIUtil.
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
 
    @staticmethod
    @overload
    def apiParseVersion(arg0: 'Configuration') -> 'APIVersion':
        """public static org.lwjgl.system.APIUtil$APIVersion org.lwjgl.system.APIUtil.apiParseVersion(org.lwjgl.system.Configuration<?>)"""
        return APIVersion.__wrap(__APIUtil.apiParseVersion(arg0))

    @staticmethod
    @overload
    def apiUnknownToken(arg0: str, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiUnknownToken(java.lang.String,int)"""
        return str.__wrap(__APIUtil.apiUnknownToken(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def apiClosureRetP(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRetP(long,long)"""
        __APIUtil.apiClosureRetP(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def apiCreateLibrary(arg0: str) -> 'SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.APIUtil.apiCreateLibrary(java.lang.String)"""
        return SharedLibrary.__wrap(__APIUtil.apiCreateLibrary(arg0))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,short)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def apiFindLibrary(arg0: str, arg1: str) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiFindLibrary(java.lang.String,java.lang.String)"""
        return str.__wrap(__APIUtil.apiFindLibrary(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: float):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,float)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int.__wrap(__APIUtil.apiArray(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiCreateStruct(*arg0: 'libffi.FFIType') -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateStruct(org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFIType.__wrap(__APIUtil.apiCreateStruct(arg0))

    @staticmethod
    @overload
    def apiClassTokens(arg0: 'BiPredicate', arg1: 'Map', *arg2: 'type.Class') -> 'Map':
        """public static java.util.Map<java.lang.Integer, java.lang.String> org.lwjgl.system.APIUtil.apiClassTokens(java.util.function.BiPredicate<java.lang.reflect.Field, java.lang.Integer>,java.util.Map<java.lang.Integer, java.lang.String>,java.lang.Class<?>...)"""
        return Map.__wrap(__APIUtil.apiClassTokens(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiCreateUnion(*arg0: 'libffi.FFIType') -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateUnion(org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFIType.__wrap(__APIUtil.apiCreateUnion(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def apiUnknownToken(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.APIUtil.apiUnknownToken(int)"""
        return str.__wrap(__APIUtil.apiUnknownToken(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,byte)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', *arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,java.nio.ByteBuffer...)"""
        return int.__wrap(__APIUtil.apiArray(arg0, arg1))

    @staticmethod
    @overload
    def apiCreateArray(arg0: 'FFIType', arg1: int) -> 'libffi.FFIType':
        """public static org.lwjgl.system.libffi.FFIType org.lwjgl.system.APIUtil.apiCreateArray(org.lwjgl.system.libffi.FFIType,int)"""
        return libffi.FFIType.__wrap(__APIUtil.apiCreateArray(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def apiLogMissing(arg0: str, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.APIUtil.apiLogMissing(java.lang.String,java.nio.ByteBuffer)"""
        __APIUtil.apiLogMissing(arg0, arg1)

    @staticmethod
    @overload
    def apiCheckAllocation(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiCheckAllocation(int,long,long)"""
        return int.__wrap(__APIUtil.apiCheckAllocation(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def apiFilterExtensions(arg0: 'Set', arg1: 'Configuration'):
        """public static void org.lwjgl.system.APIUtil.apiFilterExtensions(java.util.Set<java.lang.String>,org.lwjgl.system.Configuration<java.lang.Object>)"""
        __APIUtil.apiFilterExtensions(arg0, arg1)

    @staticmethod
    @overload
    def apiParseVersion(arg0: str) -> 'APIVersion':
        """public static org.lwjgl.system.APIUtil$APIVersion org.lwjgl.system.APIUtil.apiParseVersion(java.lang.String)"""
        return APIVersion.__wrap(__APIUtil.apiParseVersion(arg0))

    @staticmethod
    @overload
    def apiCreateCIFVar(arg0: int, arg1: int, arg2: 'FFIType', *arg3: 'libffi.FFIType') -> 'libffi.FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.APIUtil.apiCreateCIFVar(int,int,org.lwjgl.system.libffi.FFIType,org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFICIF.__wrap(__APIUtil.apiCreateCIFVar(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def apiLogMore(arg0: 'CharSequence'):
        """public static void org.lwjgl.system.APIUtil.apiLogMore(java.lang.CharSequence)"""
        __APIUtil.apiLogMore(arg0)

    @staticmethod
    @overload
    def apiClosureRetL(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRetL(long,long)"""
        __APIUtil.apiClosureRetL(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def apiArray(arg0: 'MemoryStack', *arg1: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiArray(org.lwjgl.system.MemoryStack,long...)"""
        return int.__wrap(__APIUtil.apiArray(arg0, arg1))

    @staticmethod
    @overload
    def apiStdcall() -> int:
        """public static int org.lwjgl.system.APIUtil.apiStdcall()"""
        return int.__wrap(__APIUtil.apiStdcall())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def apiCreateCIF(arg0: int, arg1: 'FFIType', *arg2: 'libffi.FFIType') -> 'libffi.FFICIF':
        """public static org.lwjgl.system.libffi.FFICIF org.lwjgl.system.APIUtil.apiCreateCIF(int,org.lwjgl.system.libffi.FFIType,org.lwjgl.system.libffi.FFIType...)"""
        return libffi.FFICIF.__wrap(__APIUtil.apiCreateCIF(__int.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,int)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def apiArrayi(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayi(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int.__wrap(__APIUtil.apiArrayi(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiGetFunctionAddressOptional(arg0: 'SharedLibrary', arg1: str) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetFunctionAddressOptional(org.lwjgl.system.SharedLibrary,java.lang.String)"""
        return int.__wrap(__APIUtil.apiGetFunctionAddressOptional(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: bool):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,boolean)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def apiClosureRet(arg0: int, arg1: float):
        """public static void org.lwjgl.system.APIUtil.apiClosureRet(long,double)"""
        __APIUtil.apiClosureRet(__long.valueOf(arg0), __double.valueOf(arg1))

    @staticmethod
    @overload
    def apiGetFunctionAddress(arg0: 'FunctionProvider', arg1: str) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetFunctionAddress(org.lwjgl.system.FunctionProvider,java.lang.String)"""
        return int.__wrap(__APIUtil.apiGetFunctionAddress(arg0, arg1))

    @staticmethod
    @overload
    def apiGetMappedBuffer(arg0: 'ByteBuffer', arg1: int, arg2: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.APIUtil.apiGetMappedBuffer(java.nio.ByteBuffer,long,int)"""
        return ByteBuffer.__wrap(__APIUtil.apiGetMappedBuffer(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def apiArrayp(arg0: 'MemoryStack', *arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayp(org.lwjgl.system.MemoryStack,java.nio.ByteBuffer...)"""
        return int.__wrap(__APIUtil.apiArrayp(arg0, arg1))

    @staticmethod
    @overload
    def apiArrayFree(arg0: int, arg1: int):
        """public static void org.lwjgl.system.APIUtil.apiArrayFree(long,int)"""
        __APIUtil.apiArrayFree(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def apiLog(arg0: 'CharSequence'):
        """public static void org.lwjgl.system.APIUtil.apiLog(java.lang.CharSequence)"""
        __APIUtil.apiLog(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def apiArrayp(arg0: 'MemoryStack', arg1: 'Encoder', *arg2: 'CharSequence') -> int:
        """public static long org.lwjgl.system.APIUtil.apiArrayp(org.lwjgl.system.MemoryStack,org.lwjgl.system.APIUtil$Encoder,java.lang.CharSequence...)"""
        return int.__wrap(__APIUtil.apiArrayp(arg0, arg1, arg2))

    @staticmethod
    @overload
    def apiGetBytes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.APIUtil.apiGetBytes(int,int)"""
        return int.__wrap(__APIUtil.apiGetBytes(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import org.lwjgl.system.MemoryUtil as __MemoryUtil_MemoryAllocationReport_Aggregate
__Aggregate = __MemoryUtil_MemoryAllocationReport_Aggregate.MemoryAllocationReport.Aggregate
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Aggregate(__Enum, Enum):
    """org.lwjgl.system.MemoryUtil.MemoryAllocationReport.Aggregate"""
 
    @staticmethod
    def __wrap(java_value: __Aggregate) -> 'Aggregate':
        return Aggregate(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Aggregate):
        """
        Dynamic initializer for Aggregate.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['Aggregate']:
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate[] org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate.values()"""
        return List[Aggregate].__wrap(__Aggregate.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Aggregate':
        """public static org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate org.lwjgl.system.MemoryUtil$MemoryAllocationReport$Aggregate.valueOf(java.lang.String)"""
        return Aggregate.__wrap(__Aggregate.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: org.lwjgl.system.NonnullDefault
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import org.lwjgl.system.NonnullDefault as __NonnullDefault
__NonnullDefault = __NonnullDefault
from abc import abstractmethod, ABC
 
class NonnullDefault(ABC, __Annotation, Annotation):
    """org.lwjgl.system.NonnullDefault"""
 
    @staticmethod
    def __wrap(java_value: __NonnullDefault) -> 'NonnullDefault':
        return NonnullDefault(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NonnullDefault):
        """
        Dynamic initializer for NonnullDefault.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.lwjgl.system.MathUtil
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.system.MathUtil as __MathUtil
__MathUtil = __MathUtil
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MathUtil():
    """org.lwjgl.system.MathUtil"""
 
    @staticmethod
    def __wrap(java_value: __MathUtil) -> 'MathUtil':
        return MathUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MathUtil):
        """
        Dynamic initializer for MathUtil.
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

    @staticmethod
    @overload
    def mathHasZeroByte(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroByte(int)"""
        return bool.__wrap(__MathUtil.mathHasZeroByte(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mathIsPoT(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathIsPoT(int)"""
        return bool.__wrap(__MathUtil.mathIsPoT(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def mathRoundPoT(arg0: int) -> int:
        """public static int org.lwjgl.system.MathUtil.mathRoundPoT(int)"""
        return int.__wrap(__MathUtil.mathRoundPoT(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mathHasZeroShort(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroShort(long)"""
        return bool.__wrap(__MathUtil.mathHasZeroShort(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mathDivideUnsigned(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathDivideUnsigned(long,long)"""
        return int.__wrap(__MathUtil.mathDivideUnsigned(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def mathRemainderUnsigned(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathRemainderUnsigned(long,long)"""
        return int.__wrap(__MathUtil.mathRemainderUnsigned(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def mathHasZeroShort(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroShort(int)"""
        return bool.__wrap(__MathUtil.mathHasZeroShort(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mathHasZeroByte(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.MathUtil.mathHasZeroByte(long)"""
        return bool.__wrap(__MathUtil.mathHasZeroByte(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def mathMultiplyHighS64(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathMultiplyHighS64(long,long)"""
        return int.__wrap(__MathUtil.mathMultiplyHighS64(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def mathMultiplyHighU64(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.MathUtil.mathMultiplyHighU64(long,long)"""
        return int.__wrap(__MathUtil.mathMultiplyHighU64(__long.valueOf(arg0), __long.valueOf(arg1)))

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