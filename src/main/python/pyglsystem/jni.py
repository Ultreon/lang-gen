from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.jni.JNINativeMethod as __JNINativeMethod_Buffer
__Buffer = __JNINativeMethod_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.jni.JNINativeMethod as __JNINativeMethod
__JNINativeMethod = __JNINativeMethod
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
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JNINativeMethod(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.jni.JNINativeMethod"""
 
    @staticmethod
    def __wrap(java_value: __JNINativeMethod) -> 'JNINativeMethod':
        return JNINativeMethod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JNINativeMethod):
        """
        Dynamic initializer for JNINativeMethod.
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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.malloc(__int.valueOf(arg0), arg1))

    @overload
    def fnPtr(self) -> int:
        """public long org.lwjgl.system.jni.JNINativeMethod.fnPtr()"""
        return int.__wrap(super(JNINativeMethod, self).fnPtr())

    @overload
    def fnPtr(self, arg0: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.fnPtr(long)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).fnPtr(__long.valueOf(arg0)))

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.name(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).name(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int)"""
        return Buffer.__wrap(__JNINativeMethod.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.malloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.createSafe(long,int)"""
        return Buffer.__wrap(__JNINativeMethod.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.name()"""
        return 'ByteBuffer'.__wrap(super(JNINativeMethod, self).name())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.jni.JNINativeMethod(java.nio.ByteBuffer)"""
        val = __JNINativeMethod(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nfnPtr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long,long)"""
        __JNINativeMethod.nfnPtr(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.nameString()"""
        return str.__wrap(super(JNINativeMethod, self).nameString())

    @overload
    def signature(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.signature()"""
        return 'ByteBuffer'.__wrap(super(JNINativeMethod, self).signature())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nfnPtr(arg0: int) -> int:
        """public static long org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long)"""
        return int.__wrap(__JNINativeMethod.nfnPtr(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.jni.JNINativeMethod.sizeof()"""
        return int.__wrap(super(JNINativeMethod, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.mallocStack(arg0))

    @overload
    def signature(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.signature(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).signature(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int)"""
        return Buffer.__wrap(__JNINativeMethod.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.createSafe(long)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).set(arg0, arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int)"""
        return Buffer.__wrap(__JNINativeMethod.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create(long)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int)"""
        return Buffer.__wrap(__JNINativeMethod.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(long,int)"""
        return Buffer.__wrap(__JNINativeMethod.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.calloc())

    @staticmethod
    @overload
    def callocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.callocStack())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.callocStack(arg0))

    @staticmethod
    @overload
    def nname(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nname(long,java.nio.ByteBuffer)"""
        __JNINativeMethod.nname(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nsignatureString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nsignatureString(long)"""
        return str.__wrap(__JNINativeMethod.nsignatureString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nnameString(long)"""
        return str.__wrap(__JNINativeMethod.nnameString(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nsignature(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nsignature(long,java.nio.ByteBuffer)"""
        __JNINativeMethod.nsignature(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.calloc(arg0))

    @overload
    def set(self, arg0: 'JNINativeMethod') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(org.lwjgl.system.jni.JNINativeMethod)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).set(arg0))

    @overload
    def signatureString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.signatureString()"""
        return str.__wrap(super(JNINativeMethod, self).signatureString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nname(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nname(long)"""
        return ByteBuffer.__wrap(__JNINativeMethod.nname(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.validate(long)"""
        __JNINativeMethod.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nsignature(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nsignature(long)"""
        return ByteBuffer.__wrap(__JNINativeMethod.nsignature(__long.valueOf(arg0)))

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
    def mallocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(int)"""
        return Buffer.__wrap(__JNINativeMethod.create(__int.valueOf(arg0)))

 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeMethod
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.jni.JNINativeMethod as __JNINativeMethod_Buffer
__Buffer = __JNINativeMethod_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.jni.JNINativeMethod as __JNINativeMethod
__JNINativeMethod = __JNINativeMethod
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
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class JNINativeMethod(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.jni.JNINativeMethod"""
 
    @staticmethod
    def __wrap(java_value: __JNINativeMethod) -> 'JNINativeMethod':
        return JNINativeMethod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JNINativeMethod):
        """
        Dynamic initializer for JNINativeMethod.
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
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.malloc(__int.valueOf(arg0), arg1))

    @overload
    def fnPtr(self) -> int:
        """public long org.lwjgl.system.jni.JNINativeMethod.fnPtr()"""
        return int.__wrap(super(JNINativeMethod, self).fnPtr())

    @overload
    def fnPtr(self, arg0: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.fnPtr(long)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).fnPtr(__long.valueOf(arg0)))

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.name(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).name(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.malloc(int)"""
        return Buffer.__wrap(__JNINativeMethod.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.malloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.malloc()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.malloc())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.createSafe(long,int)"""
        return Buffer.__wrap(__JNINativeMethod.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.name()"""
        return 'ByteBuffer'.__wrap(super(JNINativeMethod, self).name())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.jni.JNINativeMethod(java.nio.ByteBuffer)"""
        val = __JNINativeMethod(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def nfnPtr(arg0: int, arg1: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long,long)"""
        __JNINativeMethod.nfnPtr(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.nameString()"""
        return str.__wrap(super(JNINativeMethod, self).nameString())

    @overload
    def signature(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.signature()"""
        return 'ByteBuffer'.__wrap(super(JNINativeMethod, self).signature())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nfnPtr(arg0: int) -> int:
        """public static long org.lwjgl.system.jni.JNINativeMethod.nfnPtr(long)"""
        return int.__wrap(__JNINativeMethod.nfnPtr(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.jni.JNINativeMethod.sizeof()"""
        return int.__wrap(super(JNINativeMethod, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.mallocStack(arg0))

    @overload
    def signature(self, arg0: 'ByteBuffer') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.signature(java.nio.ByteBuffer)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).signature(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.mallocStack(int)"""
        return Buffer.__wrap(__JNINativeMethod.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.createSafe(long)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'ByteBuffer', arg2: int) -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).set(arg0, arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int)"""
        return Buffer.__wrap(__JNINativeMethod.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.create(long)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.calloc(int)"""
        return Buffer.__wrap(__JNINativeMethod.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(long,int)"""
        return Buffer.__wrap(__JNINativeMethod.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.calloc())

    @staticmethod
    @overload
    def callocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.callocStack())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.callocStack(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.callocStack(arg0))

    @staticmethod
    @overload
    def nname(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nname(long,java.nio.ByteBuffer)"""
        __JNINativeMethod.nname(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nsignatureString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nsignatureString(long)"""
        return str.__wrap(__JNINativeMethod.nsignatureString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.jni.JNINativeMethod.nnameString(long)"""
        return str.__wrap(__JNINativeMethod.nnameString(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nsignature(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeMethod.nsignature(long,java.nio.ByteBuffer)"""
        __JNINativeMethod.nsignature(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.calloc(org.lwjgl.system.MemoryStack)"""
        return JNINativeMethod.__wrap(__JNINativeMethod.calloc(arg0))

    @overload
    def set(self, arg0: 'JNINativeMethod') -> 'JNINativeMethod':
        """public org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.set(org.lwjgl.system.jni.JNINativeMethod)"""
        return 'JNINativeMethod'.__wrap(super(__JNINativeMethod, self).set(arg0))

    @overload
    def signatureString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod.signatureString()"""
        return str.__wrap(super(JNINativeMethod, self).signatureString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nname(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nname(long)"""
        return ByteBuffer.__wrap(__JNINativeMethod.nname(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeMethod.validate(long)"""
        __JNINativeMethod.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nsignature(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod.nsignature(long)"""
        return ByteBuffer.__wrap(__JNINativeMethod.nsignature(__long.valueOf(arg0)))

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
    def mallocStack() -> 'JNINativeMethod':
        """public static org.lwjgl.system.jni.JNINativeMethod org.lwjgl.system.jni.JNINativeMethod.mallocStack()"""
        return JNINativeMethod.__wrap(__JNINativeMethod.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__JNINativeMethod.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod.create(int)"""
        return Buffer.__wrap(__JNINativeMethod.create(__int.valueOf(arg0)))

 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeMethod 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeMethod$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.jni.JNINativeMethod as __JNINativeMethod_Buffer
__Buffer = __JNINativeMethod_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.jni.JNINativeMethod.Buffer"""
 
    @staticmethod
    def __wrap(java_value: __Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Buffer):
        """
        Dynamic initializer for Buffer.
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
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod$Buffer.nameString()"""
        return str.__wrap(super(Buffer, self).nameString())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def signature(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.signature(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).signature(arg0))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int.__wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @overload
    def fnPtr(self) -> int:
        """public long org.lwjgl.system.jni.JNINativeMethod$Buffer.fnPtr()"""
        return int.__wrap(super(Buffer, self).fnPtr())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def signature(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod$Buffer.signature()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).signature())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool.__wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def signatureString(self) -> str:
        """public java.lang.String org.lwjgl.system.jni.JNINativeMethod$Buffer.signatureString()"""
        return str.__wrap(super(Buffer, self).signatureString())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeMethod$Buffer.name()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).name())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.name(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).name(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'.__wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str.__wrap(super(pyglsystem.CustomBuffer, self).toString())

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
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).apply(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).stream())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def fnPtr(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.jni.JNINativeMethod$Buffer org.lwjgl.system.jni.JNINativeMethod$Buffer.fnPtr(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).fnPtr(__long.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.jni.JNINativeInterface
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.nio.IntBuffer as IntBuffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.lang.reflect.Field as Field
import java.nio.ShortBuffer as ShortBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Class as __Class
__Class = __Class
import java.lang.reflect.Field as __Field
__Field = __Field
import java.lang.String as __string
from builtins import bool
from builtins import str
import java.nio.DoubleBuffer as DoubleBuffer
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import float
import java.nio.LongBuffer as LongBuffer
import java.nio.IntBuffer as __IntBuffer
__IntBuffer = __IntBuffer
import org.lwjgl.system.jni.JNINativeInterface as __JNINativeInterface
__JNINativeInterface = __JNINativeInterface
import java.lang.Long as __long
import java.nio.LongBuffer as __LongBuffer
__LongBuffer = __LongBuffer
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.nio.Buffer as Buffer
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import java.nio.DoubleBuffer as __DoubleBuffer
__DoubleBuffer = __DoubleBuffer
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
import java.lang.reflect.Method as Method
 
class JNINativeInterface():
    """org.lwjgl.system.jni.JNINativeInterface"""
 
    @staticmethod
    def __wrap(java_value: __JNINativeInterface) -> 'JNINativeInterface':
        return JNINativeInterface(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JNINativeInterface):
        """
        Dynamic initializer for JNINativeInterface.
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
    def GetDoubleArrayElements(arg0: 'double', arg1: 'ByteBuffer') -> 'DoubleBuffer':
        """public static java.nio.DoubleBuffer org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayElements(double[],java.nio.ByteBuffer)"""
        return DoubleBuffer.__wrap(__JNINativeInterface.GetDoubleArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nReleaseBooleanArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseBooleanArrayElements(byte[],long,int)"""
        __JNINativeInterface.nReleaseBooleanArrayElements(bytes, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def SetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        __JNINativeInterface.SetBooleanArrayRegion(bytes, __int.valueOf(arg1), arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def NewGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewGlobalRef(java.lang.Object)"""
        return int.__wrap(__JNINativeInterface.NewGlobalRef(arg0))

    @staticmethod
    @overload
    def GetCharArrayElements(arg0: 'char', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetCharArrayElements(char[],java.nio.ByteBuffer)"""
        return ShortBuffer.__wrap(__JNINativeInterface.GetCharArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nReleaseLongArrayElements(arg0: 'long', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseLongArrayElements(long[],long,int)"""
        __JNINativeInterface.nReleaseLongArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nReleaseByteArrayElements(arg0: bytes, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseByteArrayElements(byte[],long,int)"""
        __JNINativeInterface.nReleaseByteArrayElements(bytes, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def SetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        __JNINativeInterface.SetByteArrayRegion(bytes, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nSetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetShortArrayRegion(short[],int,int,long)"""
        __JNINativeInterface.nSetShortArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def SetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        __JNINativeInterface.SetFloatArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseFloatArrayElements(arg0: 'float', arg1: 'FloatBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseFloatArrayElements(float[],java.nio.FloatBuffer,int)"""
        __JNINativeInterface.ReleaseFloatArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def SetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        __JNINativeInterface.SetLongArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nSetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetIntArrayRegion(int[],int,int,long)"""
        __JNINativeInterface.nSetIntArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def SetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        __JNINativeInterface.SetCharArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nSetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetLongArrayRegion(long[],int,int,long)"""
        __JNINativeInterface.nSetLongArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def NewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.NewDirectByteBuffer(long,long)"""
        return ByteBuffer.__wrap(__JNINativeInterface.NewDirectByteBuffer(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def ReleaseIntArrayElements(arg0: 'int', arg1: 'IntBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseIntArrayElements(int[],java.nio.IntBuffer,int)"""
        __JNINativeInterface.ReleaseIntArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def GetVersion() -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetVersion()"""
        return int.__wrap(__JNINativeInterface.GetVersion())

    @staticmethod
    @overload
    def GetLongArrayRegion(arg0: 'long', arg1: int, arg2: 'LongBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetLongArrayRegion(long[],int,java.nio.LongBuffer)"""
        __JNINativeInterface.GetLongArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetObjectRefType(arg0: object) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.GetObjectRefType(java.lang.Object)"""
        return int.__wrap(__JNINativeInterface.GetObjectRefType(arg0))

    @staticmethod
    @overload
    def SetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        __JNINativeInterface.SetShortArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def FromReflectedMethod(arg0: 'Method') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedMethod(java.lang.reflect.Method)"""
        return int.__wrap(__JNINativeInterface.FromReflectedMethod(arg0))

    @staticmethod
    @overload
    def ToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.ToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method.__wrap(__JNINativeInterface.ToReflectedMethod(arg0, __long.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetStringRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringRegion(java.lang.String,int,int,long)"""
        __JNINativeInterface.nGetStringRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def GetDirectBufferAddress(arg0: 'Buffer') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.GetDirectBufferAddress(java.nio.Buffer)"""
        return int.__wrap(__JNINativeInterface.GetDirectBufferAddress(arg0))

    @staticmethod
    @overload
    def GetFloatArrayElements(arg0: 'float', arg1: 'ByteBuffer') -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayElements(float[],java.nio.ByteBuffer)"""
        return FloatBuffer.__wrap(__JNINativeInterface.GetFloatArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nToReflectedMethod(arg0: 'Class', arg1: int, arg2: bool) -> 'Method':
        """public static native java.lang.reflect.Method org.lwjgl.system.jni.JNINativeInterface.nToReflectedMethod(java.lang.Class<?>,long,boolean)"""
        return Method.__wrap(__JNINativeInterface.nToReflectedMethod(arg0, __long.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def SetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        __JNINativeInterface.SetDoubleArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nReleaseIntArrayElements(arg0: 'int', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseIntArrayElements(int[],long,int)"""
        __JNINativeInterface.nReleaseIntArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def GetByteArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetByteArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        __JNINativeInterface.GetByteArrayRegion(bytes, __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nReleaseFloatArrayElements(arg0: 'float', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseFloatArrayElements(float[],long,int)"""
        __JNINativeInterface.nReleaseFloatArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def GetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetDoubleArrayRegion(double[],int,java.nio.DoubleBuffer)"""
        __JNINativeInterface.GetDoubleArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayRegion(byte[],int,int,long)"""
        __JNINativeInterface.nGetByteArrayRegion(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def GetStringRegion(arg0: str, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringRegion(java.lang.String,int,java.nio.ByteBuffer)"""
        __JNINativeInterface.GetStringRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def ReleaseBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseBooleanArrayElements(byte[],java.nio.ByteBuffer,int)"""
        __JNINativeInterface.ReleaseBooleanArrayElements(bytes, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nGetDoubleArrayElements(arg0: 'double', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayElements(double[],long)"""
        return int.__wrap(__JNINativeInterface.nGetDoubleArrayElements(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def GetFloatArrayRegion(arg0: 'float', arg1: int, arg2: 'FloatBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetFloatArrayRegion(float[],int,java.nio.FloatBuffer)"""
        __JNINativeInterface.GetFloatArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def GetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        __JNINativeInterface.GetIntArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetLongArrayElements(arg0: 'long', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayElements(long[],long)"""
        return int.__wrap(__JNINativeInterface.nGetLongArrayElements(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayRegion(byte[],int,int,long)"""
        __JNINativeInterface.nGetBooleanArrayRegion(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nGetLongArrayRegion(arg0: 'long', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetLongArrayRegion(long[],int,int,long)"""
        __JNINativeInterface.nGetLongArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def DeleteWeakGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteWeakGlobalRef(long)"""
        __JNINativeInterface.DeleteWeakGlobalRef(__long.valueOf(arg0))

        @staticmethod
        @overload
        def noop():
            """public static native void org.lwjgl.system.jni.JNINativeInterface.noop()"""
            __JNINativeInterface.noop()

    @staticmethod
    @overload
    def GetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayRegion(byte[],int,java.nio.ByteBuffer)"""
        __JNINativeInterface.GetBooleanArrayRegion(bytes, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetByteArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetByteArrayElements(byte[],long)"""
        return int.__wrap(__JNINativeInterface.nGetByteArrayElements(bytes, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nSetByteArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetByteArrayRegion(byte[],int,int,long)"""
        __JNINativeInterface.nSetByteArrayRegion(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetIntArrayRegion(arg0: 'int', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayRegion(int[],int,int,long)"""
        __JNINativeInterface.nGetIntArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def GetByteArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetByteArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__JNINativeInterface.GetByteArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def nGetFloatArrayElements(arg0: 'float', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayElements(float[],long)"""
        return int.__wrap(__JNINativeInterface.nGetFloatArrayElements(arg0, __long.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nSetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetFloatArrayRegion(float[],int,int,long)"""
        __JNINativeInterface.nSetFloatArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def ReleaseDoubleArrayElements(arg0: 'double', arg1: 'DoubleBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseDoubleArrayElements(double[],java.nio.DoubleBuffer,int)"""
        __JNINativeInterface.ReleaseDoubleArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nSetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetDoubleArrayRegion(double[],int,int,long)"""
        __JNINativeInterface.nSetDoubleArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nReleaseCharArrayElements(arg0: 'char', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseCharArrayElements(char[],long,int)"""
        __JNINativeInterface.nReleaseCharArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def ReleaseCharArrayElements(arg0: 'char', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseCharArrayElements(char[],java.nio.ShortBuffer,int)"""
        __JNINativeInterface.ReleaseCharArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def ReleaseLongArrayElements(arg0: 'long', arg1: 'LongBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseLongArrayElements(long[],java.nio.LongBuffer,int)"""
        __JNINativeInterface.ReleaseLongArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def nToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static native java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.nToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field.__wrap(__JNINativeInterface.nToReflectedField(arg0, __long.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def GetShortArrayRegion(arg0: 'short', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetShortArrayRegion(short[],int,java.nio.ShortBuffer)"""
        __JNINativeInterface.GetShortArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def RegisterNatives(arg0: 'Class', arg1: 'Buffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.RegisterNatives(java.lang.Class<?>,org.lwjgl.system.jni.JNINativeMethod$Buffer)"""
        return int.__wrap(__JNINativeInterface.RegisterNatives(arg0, arg1))

    @staticmethod
    @overload
    def GetJavaVM(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.jni.JNINativeInterface.GetJavaVM(org.lwjgl.PointerBuffer)"""
        return int.__wrap(__JNINativeInterface.GetJavaVM(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetLongArrayElements(arg0: 'long', arg1: 'ByteBuffer') -> 'LongBuffer':
        """public static java.nio.LongBuffer org.lwjgl.system.jni.JNINativeInterface.GetLongArrayElements(long[],java.nio.ByteBuffer)"""
        return LongBuffer.__wrap(__JNINativeInterface.GetLongArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nSetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetCharArrayRegion(char[],int,int,long)"""
        __JNINativeInterface.nSetCharArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nRegisterNatives(arg0: 'Class', arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nRegisterNatives(java.lang.Class<?>,long,int)"""
        return int.__wrap(__JNINativeInterface.nRegisterNatives(arg0, __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def GetShortArrayElements(arg0: 'short', arg1: 'ByteBuffer') -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.system.jni.JNINativeInterface.GetShortArrayElements(short[],java.nio.ByteBuffer)"""
        return ShortBuffer.__wrap(__JNINativeInterface.GetShortArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nGetFloatArrayRegion(arg0: 'float', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetFloatArrayRegion(float[],int,int,long)"""
        __JNINativeInterface.nGetFloatArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nGetCharArrayElements(arg0: 'char', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayElements(char[],long)"""
        return int.__wrap(__JNINativeInterface.nGetCharArrayElements(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetIntArrayElements(arg0: 'int', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetIntArrayElements(int[],long)"""
        return int.__wrap(__JNINativeInterface.nGetIntArrayElements(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nDeleteWeakGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteWeakGlobalRef(long)"""
        __JNINativeInterface.nDeleteWeakGlobalRef(__long.valueOf(arg0))

    @staticmethod
    @overload
    def GetCharArrayRegion(arg0: 'char', arg1: int, arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetCharArrayRegion(char[],int,java.nio.ShortBuffer)"""
        __JNINativeInterface.GetCharArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetDoubleArrayRegion(arg0: 'double', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetDoubleArrayRegion(double[],int,int,long)"""
        __JNINativeInterface.nGetDoubleArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def GetBooleanArrayElements(arg0: bytes, arg1: 'ByteBuffer') -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.GetBooleanArrayElements(byte[],java.nio.ByteBuffer)"""
        return ByteBuffer.__wrap(__JNINativeInterface.GetBooleanArrayElements(bytes, arg1))

    @staticmethod
    @overload
    def nGetShortArrayRegion(arg0: 'short', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayRegion(short[],int,int,long)"""
        __JNINativeInterface.nGetShortArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nSetBooleanArrayRegion(arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nSetBooleanArrayRegion(byte[],int,int,long)"""
        __JNINativeInterface.nSetBooleanArrayRegion(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def nDeleteGlobalRef(arg0: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nDeleteGlobalRef(long)"""
        __JNINativeInterface.nDeleteGlobalRef(__long.valueOf(arg0))

    @staticmethod
    @overload
    def UnregisterNatives(arg0: 'Class') -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.UnregisterNatives(java.lang.Class<?>)"""
        return int.__wrap(__JNINativeInterface.UnregisterNatives(arg0))

    @staticmethod
    @overload
    def nReleaseDoubleArrayElements(arg0: 'double', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseDoubleArrayElements(double[],long,int)"""
        __JNINativeInterface.nReleaseDoubleArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def ReleaseByteArrayElements(arg0: bytes, arg1: 'ByteBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseByteArrayElements(byte[],java.nio.ByteBuffer,int)"""
        __JNINativeInterface.ReleaseByteArrayElements(bytes, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def ToReflectedField(arg0: 'Class', arg1: int, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.lwjgl.system.jni.JNINativeInterface.ToReflectedField(java.lang.Class<?>,long,boolean)"""
        return Field.__wrap(__JNINativeInterface.ToReflectedField(arg0, __long.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def NewWeakGlobalRef(arg0: object) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.NewWeakGlobalRef(java.lang.Object)"""
        return int.__wrap(__JNINativeInterface.NewWeakGlobalRef(arg0))

    @staticmethod
    @overload
    def nNewDirectByteBuffer(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static native java.nio.ByteBuffer org.lwjgl.system.jni.JNINativeInterface.nNewDirectByteBuffer(long,long)"""
        return ByteBuffer.__wrap(__JNINativeInterface.nNewDirectByteBuffer(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetShortArrayElements(arg0: 'short', arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetShortArrayElements(short[],long)"""
        return int.__wrap(__JNINativeInterface.nGetShortArrayElements(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nReleaseShortArrayElements(arg0: 'short', arg1: int, arg2: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nReleaseShortArrayElements(short[],long,int)"""
        __JNINativeInterface.nReleaseShortArrayElements(arg0, __long.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def GetIntArrayElements(arg0: 'int', arg1: 'ByteBuffer') -> 'IntBuffer':
        """public static java.nio.IntBuffer org.lwjgl.system.jni.JNINativeInterface.GetIntArrayElements(int[],java.nio.ByteBuffer)"""
        return IntBuffer.__wrap(__JNINativeInterface.GetIntArrayElements(arg0, arg1))

    @staticmethod
    @overload
    def nGetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetStringUTFRegion(java.lang.String,int,int,long)"""
        __JNINativeInterface.nGetStringUTFRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def FromReflectedField(arg0: 'Field') -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.FromReflectedField(java.lang.reflect.Field)"""
        return int.__wrap(__JNINativeInterface.FromReflectedField(arg0))

    @staticmethod
    @overload
    def DeleteGlobalRef(arg0: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.DeleteGlobalRef(long)"""
        __JNINativeInterface.DeleteGlobalRef(__long.valueOf(arg0))

    @staticmethod
    @overload
    def GetStringUTFRegion(arg0: str, arg1: int, arg2: int, arg3: 'ByteBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.GetStringUTFRegion(java.lang.String,int,int,java.nio.ByteBuffer)"""
        __JNINativeInterface.GetStringUTFRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nGetJavaVM(arg0: int) -> int:
        """public static native int org.lwjgl.system.jni.JNINativeInterface.nGetJavaVM(long)"""
        return int.__wrap(__JNINativeInterface.nGetJavaVM(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetBooleanArrayElements(arg0: bytes, arg1: int) -> int:
        """public static native long org.lwjgl.system.jni.JNINativeInterface.nGetBooleanArrayElements(byte[],long)"""
        return int.__wrap(__JNINativeInterface.nGetBooleanArrayElements(bytes, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def ReleaseShortArrayElements(arg0: 'short', arg1: 'ShortBuffer', arg2: int):
        """public static void org.lwjgl.system.jni.JNINativeInterface.ReleaseShortArrayElements(short[],java.nio.ShortBuffer,int)"""
        __JNINativeInterface.ReleaseShortArrayElements(arg0, arg1, __int.valueOf(arg2))

    @staticmethod
    @overload
    def SetIntArrayRegion(arg0: 'int', arg1: int, arg2: 'IntBuffer'):
        """public static void org.lwjgl.system.jni.JNINativeInterface.SetIntArrayRegion(int[],int,java.nio.IntBuffer)"""
        __JNINativeInterface.SetIntArrayRegion(arg0, __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nGetCharArrayRegion(arg0: 'char', arg1: int, arg2: int, arg3: int):
        """public static native void org.lwjgl.system.jni.JNINativeInterface.nGetCharArrayRegion(char[],int,int,long)"""
        __JNINativeInterface.nGetCharArrayRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3))