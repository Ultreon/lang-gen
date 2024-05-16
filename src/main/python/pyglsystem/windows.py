from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.Crypt32 as __Crypt32
__Crypt32 = __Crypt32
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Crypt32():
    """org.lwjgl.system.windows.Crypt32"""
 
    @staticmethod
    def __wrap(java_value: __Crypt32) -> 'Crypt32':
        return Crypt32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Crypt32):
        """
        Dynamic initializer for Crypt32.
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
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int,long)"""
        return int.__wrap(__Crypt32.nCryptProtectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CryptUnprotectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectMemory(java.nio.ByteBuffer,int)"""
        return bool.__wrap(__Crypt32.CryptUnprotectMemory(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

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
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'ByteBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.nio.ByteBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptProtectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

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

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.Crypt32.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__Crypt32.getLibrary())

    @staticmethod
    @overload
    def CryptProtectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectMemory(java.nio.ByteBuffer,int)"""
        return bool.__wrap(__Crypt32.CryptProtectMemory(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def CryptUnprotectData(arg0: 'DATA_BLOB', arg1: 'PointerBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectData(org.lwjgl.system.windows.DATA_BLOB,org.lwjgl.PointerBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptUnprotectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'CharSequence', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.lang.CharSequence,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptProtectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long,long)"""
        return int.__wrap(__Crypt32.nCryptProtectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int)"""
        return int.__wrap(__Crypt32.nCryptUnprotectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long)"""
        return int.__wrap(__Crypt32.nCryptProtectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int)"""
        return int.__wrap(__Crypt32.nCryptProtectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: org.lwjgl.system.windows.Crypt32
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.Crypt32 as __Crypt32
__Crypt32 = __Crypt32
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Crypt32():
    """org.lwjgl.system.windows.Crypt32"""
 
    @staticmethod
    def __wrap(java_value: __Crypt32) -> 'Crypt32':
        return Crypt32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Crypt32):
        """
        Dynamic initializer for Crypt32.
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
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int,long)"""
        return int.__wrap(__Crypt32.nCryptProtectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CryptUnprotectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectMemory(java.nio.ByteBuffer,int)"""
        return bool.__wrap(__Crypt32.CryptUnprotectMemory(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

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
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'ByteBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.nio.ByteBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptProtectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

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

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.Crypt32.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__Crypt32.getLibrary())

    @staticmethod
    @overload
    def CryptProtectMemory(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectMemory(java.nio.ByteBuffer,int)"""
        return bool.__wrap(__Crypt32.CryptProtectMemory(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def CryptUnprotectData(arg0: 'DATA_BLOB', arg1: 'PointerBuffer', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptUnprotectData(org.lwjgl.system.windows.DATA_BLOB,org.lwjgl.PointerBuffer,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptUnprotectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CryptProtectData(arg0: 'DATA_BLOB', arg1: 'CharSequence', arg2: 'DATA_BLOB', arg3: int, arg4: 'CRYPTPROTECT_PROMPTSTRUCT', arg5: int, arg6: 'DATA_BLOB') -> bool:
        """public static boolean org.lwjgl.system.windows.Crypt32.CryptProtectData(org.lwjgl.system.windows.DATA_BLOB,java.lang.CharSequence,org.lwjgl.system.windows.DATA_BLOB,long,org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT,int,org.lwjgl.system.windows.DATA_BLOB)"""
        return bool.__wrap(__Crypt32.CryptProtectData(arg0, arg1, arg2, __long.valueOf(arg3), arg4, __int.valueOf(arg5), arg6))

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long,long)"""
        return int.__wrap(__Crypt32.nCryptProtectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nCryptUnprotectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.Crypt32.nCryptUnprotectData(long,long,long,long,long,int,long,long)"""
        return int.__wrap(__Crypt32.nCryptUnprotectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nCryptUnprotectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptUnprotectMemory(long,int,int)"""
        return int.__wrap(__Crypt32.nCryptUnprotectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nCryptProtectData(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectData(long,long,long,long,long,int,long)"""
        return int.__wrap(__Crypt32.nCryptProtectData(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nCryptProtectMemory(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.Crypt32.nCryptProtectMemory(long,int,int)"""
        return int.__wrap(__Crypt32.nCryptProtectMemory(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

 
 
 
# CLASS: org.lwjgl.system.windows.Crypt32 
 
 
# CLASS: org.lwjgl.system.windows.LARGE_INTEGER
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.LARGE_INTEGER as __LARGE_INTEGER
__LARGE_INTEGER = __LARGE_INTEGER
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.system.windows.LARGE_INTEGER as __LARGE_INTEGER_Buffer
__Buffer = __LARGE_INTEGER_Buffer.Buffer
from builtins import int
 
class LARGE_INTEGER():
    """org.lwjgl.system.windows.LARGE_INTEGER"""
 
    @staticmethod
    def __wrap(java_value: __LARGE_INTEGER) -> 'LARGE_INTEGER':
        return LARGE_INTEGER(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LARGE_INTEGER):
        """
        Dynamic initializer for LARGE_INTEGER.
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
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.create(int)"""
        return Buffer.__wrap(__LARGE_INTEGER.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__LARGE_INTEGER.malloc(__int.valueOf(arg0), arg1))

    @overload
    def QuadPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.QuadPart(long)"""
        return 'LARGE_INTEGER'.__wrap(super(__LARGE_INTEGER, self).QuadPart(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nu_LowPart(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.LARGE_INTEGER.nu_LowPart(long)"""
        return int.__wrap(__LARGE_INTEGER.nu_LowPart(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def u_HighPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.u_HighPart(int)"""
        return 'LARGE_INTEGER'.__wrap(super(__LARGE_INTEGER, self).u_HighPart(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.malloc(int)"""
        return Buffer.__wrap(__LARGE_INTEGER.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.malloc()"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.malloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def u_HighPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.u_HighPart()"""
        return int.__wrap(super(LARGE_INTEGER, self).u_HighPart())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.sizeof()"""
        return int.__wrap(super(LARGE_INTEGER, self).sizeof())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.LARGE_INTEGER(java.nio.ByteBuffer)"""
        val = __LARGE_INTEGER(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.calloc(org.lwjgl.system.MemoryStack)"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.calloc(arg0))

    @overload
    def u_LowPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER.u_LowPart()"""
        return int.__wrap(super(LARGE_INTEGER, self).u_LowPart())

    @staticmethod
    @overload
    def nu_HighPart(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.LARGE_INTEGER.nu_HighPart(long)"""
        return int.__wrap(__LARGE_INTEGER.nu_HighPart(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'LARGE_INTEGER') -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.set(org.lwjgl.system.windows.LARGE_INTEGER)"""
        return 'LARGE_INTEGER'.__wrap(super(__LARGE_INTEGER, self).set(arg0))

    @staticmethod
    @overload
    def create() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.create()"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.create())

    @staticmethod
    @overload
    def calloc() -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.calloc()"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.calloc())

    @overload
    def u_LowPart(self, arg0: int) -> 'LARGE_INTEGER':
        """public org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.u_LowPart(int)"""
        return 'LARGE_INTEGER'.__wrap(super(__LARGE_INTEGER, self).u_LowPart(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.createSafe(long)"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.calloc(int)"""
        return Buffer.__wrap(__LARGE_INTEGER.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nu_HighPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nu_HighPart(long,int)"""
        __LARGE_INTEGER.nu_HighPart(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.create(long)"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nQuadPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nQuadPart(long,long)"""
        __LARGE_INTEGER.nQuadPart(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nQuadPart(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.LARGE_INTEGER.nQuadPart(long)"""
        return int.__wrap(__LARGE_INTEGER.nQuadPart(__long.valueOf(arg0)))

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
    def nu_LowPart(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.LARGE_INTEGER.nu_LowPart(long,int)"""
        __LARGE_INTEGER.nu_LowPart(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__LARGE_INTEGER.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.createSafe(long,int)"""
        return Buffer.__wrap(__LARGE_INTEGER.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def QuadPart(self) -> int:
        """public long org.lwjgl.system.windows.LARGE_INTEGER.QuadPart()"""
        return int.__wrap(super(LARGE_INTEGER, self).QuadPart())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER.create(long,int)"""
        return Buffer.__wrap(__LARGE_INTEGER.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'LARGE_INTEGER':
        """public static org.lwjgl.system.windows.LARGE_INTEGER org.lwjgl.system.windows.LARGE_INTEGER.malloc(org.lwjgl.system.MemoryStack)"""
        return LARGE_INTEGER.__wrap(__LARGE_INTEGER.malloc(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.POINT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import org.lwjgl.system.windows.POINT as __POINT_Buffer
__Buffer = __POINT_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.POINT.Buffer"""
 
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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINT$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINT$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public org.lwjgl.system.windows.POINT$Buffer(long,int)"""
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
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT$Buffer.y(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

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
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT$Buffer.x(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x(__int.valueOf(arg0)))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.MOUSEINPUT
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.MOUSEINPUT as __MOUSEINPUT_Buffer
__Buffer = __MOUSEINPUT_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.system.windows.MOUSEINPUT as __MOUSEINPUT
__MOUSEINPUT = __MOUSEINPUT
from builtins import int
 
class MOUSEINPUT():
    """org.lwjgl.system.windows.MOUSEINPUT"""
 
    @staticmethod
    def __wrap(java_value: __MOUSEINPUT) -> 'MOUSEINPUT':
        return MOUSEINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MOUSEINPUT):
        """
        Dynamic initializer for MOUSEINPUT.
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
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MOUSEINPUT.ndwExtraInfo(long)"""
        return int.__wrap(__MOUSEINPUT.ndwExtraInfo(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.create()"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.create())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.callocStack(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.createSafe(long,int)"""
        return Buffer.__wrap(__MOUSEINPUT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def callocStack() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.callocStack()"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.callocStack())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.malloc(arg0))

    @staticmethod
    @overload
    def malloc() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.malloc()"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.malloc())

    @overload
    def dx(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dx(int)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).dx(__int.valueOf(arg0)))

    @overload
    def mouseData(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mouseData(int)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).mouseData(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndwFlags(long)"""
        return int.__wrap(__MOUSEINPUT.ndwFlags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndx(long,int)"""
        __MOUSEINPUT.ndx(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.time()"""
        return int.__wrap(super(MOUSEINPUT, self).time())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dwFlags()"""
        return int.__wrap(super(MOUSEINPUT, self).dwFlags())

    @overload
    def mouseData(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.mouseData()"""
        return int.__wrap(super(MOUSEINPUT, self).mouseData())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MOUSEINPUT.calloc(__int.valueOf(arg0), arg1))

    @overload
    def dy(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dy(int)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).dy(__int.valueOf(arg0)))

    @overload
    def dwFlags(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dwFlags(int)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).dwFlags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nmouseData(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.nmouseData(long)"""
        return int.__wrap(__MOUSEINPUT.nmouseData(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmouseData(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.nmouseData(long,int)"""
        __MOUSEINPUT.nmouseData(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MOUSEINPUT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.mallocStack(int)"""
        return Buffer.__wrap(__MOUSEINPUT.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ntime(long)"""
        return int.__wrap(__MOUSEINPUT.ntime(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MOUSEINPUT(java.nio.ByteBuffer)"""
        val = __MOUSEINPUT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def time(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.time(int)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).time(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.callocStack(int)"""
        return Buffer.__wrap(__MOUSEINPUT.callocStack(__int.valueOf(arg0)))

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.MOUSEINPUT.dwExtraInfo()"""
        return int.__wrap(super(MOUSEINPUT, self).dwExtraInfo())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.sizeof()"""
        return int.__wrap(super(MOUSEINPUT, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.calloc(int)"""
        return Buffer.__wrap(__MOUSEINPUT.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndwExtraInfo(long,long)"""
        __MOUSEINPUT.ndwExtraInfo(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ntime(long,int)"""
        __MOUSEINPUT.ntime(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def dy(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dy()"""
        return int.__wrap(super(MOUSEINPUT, self).dy())

    @overload
    def dx(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT.dx()"""
        return int.__wrap(super(MOUSEINPUT, self).dx())

    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndwFlags(long,int)"""
        __MOUSEINPUT.ndwFlags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.create(long,int)"""
        return Buffer.__wrap(__MOUSEINPUT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.create(int)"""
        return Buffer.__wrap(__MOUSEINPUT.create(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'MOUSEINPUT') -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.set(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).set(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MOUSEINPUT.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.malloc(int)"""
        return Buffer.__wrap(__MOUSEINPUT.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MOUSEINPUT.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.set(int,int,int,int,int,long)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5)))

    @staticmethod
    @overload
    def mallocStack() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.mallocStack()"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.mallocStack())

    @staticmethod
    @overload
    def calloc() -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.calloc()"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.calloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.create(long)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.calloc(arg0))

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
    def ndx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndx(long)"""
        return int.__wrap(__MOUSEINPUT.ndx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def dwExtraInfo(self, arg0: int) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.dwExtraInfo(long)"""
        return 'MOUSEINPUT'.__wrap(super(__MOUSEINPUT, self).dwExtraInfo(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndy(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MOUSEINPUT.ndy(long,int)"""
        __MOUSEINPUT.ndy(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.MOUSEINPUT.createSafe(long)"""
        return MOUSEINPUT.__wrap(__MOUSEINPUT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndy(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MOUSEINPUT.ndy(long)"""
        return int.__wrap(__MOUSEINPUT.ndy(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.GDI32
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import org.lwjgl.system.windows.GDI32 as __GDI32
__GDI32 = __GDI32
from builtins import bool
from builtins import int
 
class GDI32():
    """org.lwjgl.system.windows.GDI32"""
 
    @staticmethod
    def __wrap(java_value: __GDI32) -> 'GDI32':
        return GDI32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GDI32):
        """
        Dynamic initializer for GDI32.
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
    def DescribePixelFormat(arg0: int, arg1: int, arg2: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.DescribePixelFormat(long,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int.__wrap(__GDI32.DescribePixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def nSetPixelFormat(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nSetPixelFormat(long,int,long,long)"""
        return int.__wrap(__GDI32.nSetPixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nSwapBuffers(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nSwapBuffers(long,long)"""
        return int.__wrap(__GDI32.nSwapBuffers(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def SetPixelFormat(arg0: int, arg1: int, arg2: 'PIXELFORMATDESCRIPTOR') -> bool:
        """public static boolean org.lwjgl.system.windows.GDI32.SetPixelFormat(long,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return bool.__wrap(__GDI32.SetPixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), arg2))

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

    @staticmethod
    @overload
    def nGetPixelFormat(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nGetPixelFormat(long,long)"""
        return int.__wrap(__GDI32.nGetPixelFormat(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.GDI32.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__GDI32.getLibrary())

    @staticmethod
    @overload
    def nChoosePixelFormat(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nChoosePixelFormat(long,long,long)"""
        return int.__wrap(__GDI32.nChoosePixelFormat(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nDescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.GDI32.nDescribePixelFormat(long,int,int,long,long)"""
        return int.__wrap(__GDI32.nDescribePixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nDescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nDescribePixelFormat(long,int,int,long)"""
        return int.__wrap(__GDI32.nDescribePixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def ChoosePixelFormat(arg0: int, arg1: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.ChoosePixelFormat(long,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int.__wrap(__GDI32.ChoosePixelFormat(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nChoosePixelFormat(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nChoosePixelFormat(long,long)"""
        return int.__wrap(__GDI32.nChoosePixelFormat(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def SwapBuffers(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.GDI32.SwapBuffers(long)"""
        return bool.__wrap(__GDI32.SwapBuffers(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetPixelFormat(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.nSetPixelFormat(long,int,long)"""
        return int.__wrap(__GDI32.nSetPixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def DescribePixelFormat(arg0: int, arg1: int, arg2: int, arg3: 'PIXELFORMATDESCRIPTOR') -> int:
        """public static int org.lwjgl.system.windows.GDI32.DescribePixelFormat(long,int,int,org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return int.__wrap(__GDI32.DescribePixelFormat(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def GetPixelFormat(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.GDI32.GetPixelFormat(long)"""
        return int.__wrap(__GDI32.GetPixelFormat(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.User32
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.windows.User32 as __User32
__User32 = __User32
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class User32():
    """org.lwjgl.system.windows.User32"""
 
    @staticmethod
    def __wrap(java_value: __User32) -> 'User32':
        return User32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __User32):
        """
        Dynamic initializer for User32.
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
    def LoadIcon(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadIcon(long,java.lang.CharSequence)"""
        return int.__wrap(__User32.LoadIcon(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nLoadCursor(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nLoadCursor(long,long,long)"""
        return int.__wrap(__User32.nLoadCursor(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def CallWindowProc(arg0: 'WindowProcI', arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CallWindowProc(org.lwjgl.system.windows.WindowProcI,long,int,long,long)"""
        return int.__wrap(__User32.CallWindowProc(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def WaitMessage() -> bool:
        """public static boolean org.lwjgl.system.windows.User32.WaitMessage()"""
        return bool.__wrap(__User32.WaitMessage())

    @staticmethod
    @overload
    def SetLayeredWindowAttributes(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetLayeredWindowAttributes(long,int,byte,int)"""
        return bool.__wrap(__User32.SetLayeredWindowAttributes(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ChangeDisplaySettingsEx(arg0: 'CharSequence', arg1: 'DEVMODE', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.ChangeDisplaySettingsEx(java.lang.CharSequence,org.lwjgl.system.windows.DEVMODE,long,int,long)"""
        return int.__wrap(__User32.ChangeDisplaySettingsEx(arg0, arg1, __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nCallWindowProc(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nCallWindowProc(long,long,int,long,long)"""
        return int.__wrap(__User32.nCallWindowProc(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def SetCursorPos(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetCursorPos(int,int)"""
        return bool.__wrap(__User32.SetCursorPos(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nUnregisterClass(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nUnregisterClass(long,long)"""
        return int.__wrap(__User32.nUnregisterClass(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def DispatchMessage(arg0: 'MSG') -> int:
        """public static long org.lwjgl.system.windows.User32.DispatchMessage(org.lwjgl.system.windows.MSG)"""
        return int.__wrap(__User32.DispatchMessage(arg0))

    @staticmethod
    @overload
    def nUnregisterTouchWindow(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nUnregisterTouchWindow(long,long)"""
        return int.__wrap(__User32.nUnregisterTouchWindow(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def IsIconic(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsIconic(long)"""
        return bool.__wrap(__User32.IsIconic(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nGetMonitorInfo(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetMonitorInfo(long,long)"""
        return int.__wrap(__User32.nGetMonitorInfo(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetWindowRect(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetWindowRect(long,long)"""
        return int.__wrap(__User32.nGetWindowRect(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetWindowLongPtr(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetWindowLongPtr(long,int)"""
        return int.__wrap(__User32.GetWindowLongPtr(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def DestroyWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.DestroyWindow(long)"""
        return bool.__wrap(__User32.DestroyWindow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def EnumDisplayDevices(arg0: 'ByteBuffer', arg1: int, arg2: 'DISPLAY_DEVICE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplayDevices(java.nio.ByteBuffer,int,org.lwjgl.system.windows.DISPLAY_DEVICE,int)"""
        return bool.__wrap(__User32.EnumDisplayDevices(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def LoadIcon(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadIcon(long,java.nio.ByteBuffer)"""
        return int.__wrap(__User32.LoadIcon(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nSetWindowLongPtr(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nSetWindowLongPtr(long,int,long,long)"""
        return int.__wrap(__User32.nSetWindowLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def GetMessageExtraInfo() -> int:
        """public static long org.lwjgl.system.windows.User32.GetMessageExtraInfo()"""
        return int.__wrap(__User32.GetMessageExtraInfo())

    @staticmethod
    @overload
    def GetThreadDpiAwarenessContext() -> int:
        """public static long org.lwjgl.system.windows.User32.GetThreadDpiAwarenessContext()"""
        return int.__wrap(__User32.GetThreadDpiAwarenessContext())

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.User32.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__User32.getLibrary())

    @staticmethod
    @overload
    def ShowWindow(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ShowWindow(long,int)"""
        return bool.__wrap(__User32.ShowWindow(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def GetMessage(arg0: 'MSG', arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetMessage(org.lwjgl.system.windows.MSG,long,int,int)"""
        return bool.__wrap(__User32.GetMessage(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetWindowPlacement(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSetWindowPlacement(long,long)"""
        return int.__wrap(__User32.nSetWindowPlacement(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetClassLongPtr(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetClassLongPtr(long,int)"""
        return int.__wrap(__User32.GetClassLongPtr(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ClientToScreen(arg0: int, arg1: 'POINT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ClientToScreen(long,org.lwjgl.system.windows.POINT)"""
        return bool.__wrap(__User32.ClientToScreen(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def GetWindowPlacement(arg0: int, arg1: 'WINDOWPLACEMENT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetWindowPlacement(long,org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return bool.__wrap(__User32.GetWindowPlacement(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ShowCursor(arg0: bool) -> int:
        """public static int org.lwjgl.system.windows.User32.ShowCursor(boolean)"""
        return int.__wrap(__User32.ShowCursor(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def nAdjustWindowRectEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nAdjustWindowRectEx(long,int,int,int,long)"""
        return int.__wrap(__User32.nAdjustWindowRectEx(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nWaitMessage(arg0: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nWaitMessage(long)"""
        return int.__wrap(__User32.nWaitMessage(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def PostMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.PostMessage(long,int,long,long)"""
        return bool.__wrap(__User32.PostMessage(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def LoadCursor(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadCursor(long,java.nio.ByteBuffer)"""
        return int.__wrap(__User32.LoadCursor(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def DefWindowProc(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.windows.User32.DefWindowProc(long,int,long,long)"""
        return int.__wrap(__User32.DefWindowProc(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nChangeDisplaySettingsEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nChangeDisplaySettingsEx(long,long,long,int,long)"""
        return int.__wrap(__User32.nChangeDisplaySettingsEx(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nCloseTouchInputHandle(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nCloseTouchInputHandle(long,long)"""
        return int.__wrap(__User32.nCloseTouchInputHandle(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def IsTouchWindow(arg0: int, arg1: 'IntBuffer') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsTouchWindow(long,java.nio.IntBuffer)"""
        return bool.__wrap(__User32.IsTouchWindow(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nLoadIcon(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nLoadIcon(long,long,long)"""
        return int.__wrap(__User32.nLoadIcon(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def GetSystemMetrics(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetSystemMetrics(int)"""
        return int.__wrap(__User32.GetSystemMetrics(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nUnregisterClass(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nUnregisterClass(long,long,long)"""
        return int.__wrap(__User32.nUnregisterClass(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def SetClassLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetClassLongPtr(long,int,long)"""
        return int.__wrap(__User32.SetClassLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def RegisterTouchWindow(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.RegisterTouchWindow(long,int)"""
        return bool.__wrap(__User32.RegisterTouchWindow(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def IsTouchWindow(arg0: int, arg1: 'int') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsTouchWindow(long,int[])"""
        return bool.__wrap(__User32.IsTouchWindow(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def MonitorFromWindow(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.MonitorFromWindow(long,int)"""
        return int.__wrap(__User32.MonitorFromWindow(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def RegisterClassEx(arg0: 'WNDCLASSEX') -> int:
        """public static short org.lwjgl.system.windows.User32.RegisterClassEx(org.lwjgl.system.windows.WNDCLASSEX)"""
        return int.__wrap(__User32.RegisterClassEx(arg0))

    @staticmethod
    @overload
    def ChangeDisplaySettingsEx(arg0: 'ByteBuffer', arg1: 'DEVMODE', arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.ChangeDisplaySettingsEx(java.nio.ByteBuffer,org.lwjgl.system.windows.DEVMODE,long,int,long)"""
        return int.__wrap(__User32.ChangeDisplaySettingsEx(arg0, arg1, __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nLoadIcon(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nLoadIcon(long,long)"""
        return int.__wrap(__User32.nLoadIcon(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def ReleaseDC(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ReleaseDC(long,long)"""
        return bool.__wrap(__User32.ReleaseDC(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def MoveWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: bool) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.MoveWindow(long,int,int,int,int,boolean)"""
        return bool.__wrap(__User32.MoveWindow(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5)))

    @staticmethod
    @overload
    def IsValidDpiAwarenessContext(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsValidDpiAwarenessContext(long)"""
        return bool.__wrap(__User32.IsValidDpiAwarenessContext(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nMoveWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nMoveWindow(long,int,int,int,int,int,long)"""
        return int.__wrap(__User32.nMoveWindow(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __long.valueOf(arg6)))

    @staticmethod
    @overload
    def EnumDisplaySettingsEx(arg0: 'ByteBuffer', arg1: int, arg2: 'DEVMODE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplaySettingsEx(java.nio.ByteBuffer,int,org.lwjgl.system.windows.DEVMODE,int)"""
        return bool.__wrap(__User32.EnumDisplaySettingsEx(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nGetClassLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nGetClassLongPtr(long,int,long)"""
        return int.__wrap(__User32.nGetClassLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nCreateWindowEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nCreateWindowEx(int,long,long,int,int,int,int,int,long,long,long,long,long)"""
        return int.__wrap(__User32.nCreateWindowEx(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11), __long.valueOf(arg12)))

    @staticmethod
    @overload
    def nCreateWindowEx(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nCreateWindowEx(int,long,long,int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__User32.nCreateWindowEx(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def SendInput(arg0: 'Buffer', arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.SendInput(org.lwjgl.system.windows.INPUT$Buffer,int)"""
        return int.__wrap(__User32.SendInput(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetWindowPlacement(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetWindowPlacement(long,long)"""
        return int.__wrap(__User32.nGetWindowPlacement(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nRegisterClassEx(arg0: int, arg1: int) -> int:
        """public static native short org.lwjgl.system.windows.User32.nRegisterClassEx(long,long)"""
        return int.__wrap(__User32.nRegisterClassEx(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nGetWindowPlacement(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetWindowPlacement(long,long,long)"""
        return int.__wrap(__User32.nGetWindowPlacement(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetMessage(long,long,int,int)"""
        return int.__wrap(__User32.nGetMessage(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def GetMonitorInfo(arg0: int, arg1: 'MONITORINFOEX') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetMonitorInfo(long,org.lwjgl.system.windows.MONITORINFOEX)"""
        return bool.__wrap(__User32.GetMonitorInfo(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nPostMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nPostMessage(long,int,long,long,long)"""
        return int.__wrap(__User32.nPostMessage(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def UnregisterTouchWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterTouchWindow(long)"""
        return bool.__wrap(__User32.UnregisterTouchWindow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def EnumDisplayDevices(arg0: 'CharSequence', arg1: int, arg2: 'DISPLAY_DEVICE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplayDevices(java.lang.CharSequence,int,org.lwjgl.system.windows.DISPLAY_DEVICE,int)"""
        return bool.__wrap(__User32.EnumDisplayDevices(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nEnumDisplayDevices(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nEnumDisplayDevices(long,int,long,int)"""
        return int.__wrap(__User32.nEnumDisplayDevices(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def SetThreadDpiAwarenessContext(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetThreadDpiAwarenessContext(long)"""
        return int.__wrap(__User32.SetThreadDpiAwarenessContext(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetWindowLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nGetWindowLongPtr(long,int,long)"""
        return int.__wrap(__User32.nGetWindowLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def GetWindowRect(arg0: int, arg1: 'RECT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetWindowRect(long,org.lwjgl.system.windows.RECT)"""
        return bool.__wrap(__User32.GetWindowRect(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def IsWindowVisible(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsWindowVisible(long)"""
        return bool.__wrap(__User32.IsWindowVisible(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetWindowText(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowText(long,long,long)"""
        return int.__wrap(__User32.nSetWindowText(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nClipCursor(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nClipCursor(long)"""
        return int.__wrap(__User32.nClipCursor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def TranslateMessage(arg0: 'MSG') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.TranslateMessage(org.lwjgl.system.windows.MSG)"""
        return bool.__wrap(__User32.TranslateMessage(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def SetWindowPos(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowPos(long,long,int,int,int,int,int)"""
        return bool.__wrap(__User32.SetWindowPos(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6)))

    @staticmethod
    @overload
    def SendMessage(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SendMessage(long,int,long,long)"""
        return bool.__wrap(__User32.SendMessage(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetLayeredWindowAttributes(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetLayeredWindowAttributes(long,int,byte,int,long)"""
        return int.__wrap(__User32.nSetLayeredWindowAttributes(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nAdjustWindowRectEx(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nAdjustWindowRectEx(long,int,int,int)"""
        return int.__wrap(__User32.nAdjustWindowRectEx(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nGetWindowRect(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetWindowRect(long,long,long)"""
        return int.__wrap(__User32.nGetWindowRect(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def EnumDisplaySettingsEx(arg0: 'CharSequence', arg1: int, arg2: 'DEVMODE', arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.EnumDisplaySettingsEx(java.lang.CharSequence,int,org.lwjgl.system.windows.DEVMODE,int)"""
        return bool.__wrap(__User32.EnumDisplaySettingsEx(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nSetWindowPlacement(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowPlacement(long,long,long)"""
        return int.__wrap(__User32.nSetWindowPlacement(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nGetCursorPos(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetCursorPos(long)"""
        return int.__wrap(__User32.nGetCursorPos(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def LoadCursor(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.User32.LoadCursor(long,java.lang.CharSequence)"""
        return int.__wrap(__User32.LoadCursor(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nDestroyWindow(arg0: int, arg1: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nDestroyWindow(long,long)"""
        return int.__wrap(__User32.nDestroyWindow(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetWindowDpiAwarenessContext(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetWindowDpiAwarenessContext(long)"""
        return int.__wrap(__User32.GetWindowDpiAwarenessContext(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ClipCursor(arg0: 'RECT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.ClipCursor(org.lwjgl.system.windows.RECT)"""
        return bool.__wrap(__User32.ClipCursor(arg0))

    @staticmethod
    @overload
    def UnregisterClass(arg0: 'ByteBuffer', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterClass(java.nio.ByteBuffer,long)"""
        return bool.__wrap(__User32.UnregisterClass(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nTranslateMessage(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nTranslateMessage(long)"""
        return int.__wrap(__User32.nTranslateMessage(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetClassLongPtr(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.windows.User32.nSetClassLongPtr(long,int,long,long)"""
        return int.__wrap(__User32.nSetClassLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nGetMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetMessage(long,long,int,int,long)"""
        return int.__wrap(__User32.nGetMessage(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nRegisterTouchWindow(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nRegisterTouchWindow(long,int,long)"""
        return int.__wrap(__User32.nRegisterTouchWindow(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nLoadCursor(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nLoadCursor(long,long)"""
        return int.__wrap(__User32.nLoadCursor(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def SetWindowText(arg0: int, arg1: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowText(long,java.lang.CharSequence)"""
        return bool.__wrap(__User32.SetWindowText(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def CreateWindowEx(arg0: int, arg1: 'CharSequence', arg2: 'CharSequence', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CreateWindowEx(int,java.lang.CharSequence,java.lang.CharSequence,int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__User32.CreateWindowEx(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def nSetWindowPos(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSetWindowPos(long,long,int,int,int,int,int,long)"""
        return int.__wrap(__User32.nSetWindowPos(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __long.valueOf(arg7)))

    @staticmethod
    @overload
    def nRegisterClassEx(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.User32.nRegisterClassEx(long)"""
        return int.__wrap(__User32.nRegisterClassEx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetTouchInputInfo(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nGetTouchInputInfo(long,int,long,int)"""
        return int.__wrap(__User32.nGetTouchInputInfo(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def IsZoomed(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.IsZoomed(long)"""
        return bool.__wrap(__User32.IsZoomed(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def SetCursor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetCursor(long)"""
        return int.__wrap(__User32.SetCursor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nPeekMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nPeekMessage(long,long,int,int,int)"""
        return int.__wrap(__User32.nPeekMessage(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def AdjustWindowRectEx(arg0: 'RECT', arg1: int, arg2: bool, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.AdjustWindowRectEx(org.lwjgl.system.windows.RECT,int,boolean,int)"""
        return bool.__wrap(__User32.AdjustWindowRectEx(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def GetDpiForSystem() -> int:
        """public static int org.lwjgl.system.windows.User32.GetDpiForSystem()"""
        return int.__wrap(__User32.GetDpiForSystem())

    @staticmethod
    @overload
    def GetAsyncKeyState(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.User32.GetAsyncKeyState(int)"""
        return int.__wrap(__User32.GetAsyncKeyState(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nSetWindowText(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSetWindowText(long,long)"""
        return int.__wrap(__User32.nSetWindowText(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def GetTouchInputInfo(arg0: int, arg1: 'Buffer', arg2: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetTouchInputInfo(long,org.lwjgl.system.windows.TOUCHINPUT$Buffer,int)"""
        return bool.__wrap(__User32.GetTouchInputInfo(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def nSendInput(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nSendInput(int,long,int)"""
        return int.__wrap(__User32.nSendInput(__int.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def PeekMessage(arg0: 'MSG', arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.PeekMessage(org.lwjgl.system.windows.MSG,long,int,int,int)"""
        return bool.__wrap(__User32.PeekMessage(arg0, __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def GetAwarenessFromDpiAwarenessContext(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetAwarenessFromDpiAwarenessContext(long)"""
        return int.__wrap(__User32.GetAwarenessFromDpiAwarenessContext(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nClientToScreen(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nClientToScreen(long,long)"""
        return int.__wrap(__User32.nClientToScreen(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nDispatchMessage(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.nDispatchMessage(long)"""
        return int.__wrap(__User32.nDispatchMessage(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetDpiForWindow(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.User32.GetDpiForWindow(long)"""
        return int.__wrap(__User32.GetDpiForWindow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def SetWindowPlacement(arg0: int, arg1: 'WINDOWPLACEMENT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowPlacement(long,org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return bool.__wrap(__User32.SetWindowPlacement(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def CloseTouchInputHandle(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.CloseTouchInputHandle(long)"""
        return bool.__wrap(__User32.CloseTouchInputHandle(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def UnregisterClass(arg0: 'CharSequence', arg1: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UnregisterClass(java.lang.CharSequence,long)"""
        return bool.__wrap(__User32.UnregisterClass(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nIsTouchWindow(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nIsTouchWindow(long,long)"""
        return int.__wrap(__User32.nIsTouchWindow(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def UpdateWindow(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.UpdateWindow(long)"""
        return bool.__wrap(__User32.UpdateWindow(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nGetTouchInputInfo(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nGetTouchInputInfo(long,int,long,int,long)"""
        return int.__wrap(__User32.nGetTouchInputInfo(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def GetCursorPos(arg0: 'POINT') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.GetCursorPos(org.lwjgl.system.windows.POINT)"""
        return bool.__wrap(__User32.GetCursorPos(arg0))

    @staticmethod
    @overload
    def CreateWindowEx(arg0: int, arg1: 'ByteBuffer', arg2: 'ByteBuffer', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int) -> int:
        """public static long org.lwjgl.system.windows.User32.CreateWindowEx(int,java.nio.ByteBuffer,java.nio.ByteBuffer,int,int,int,int,int,long,long,long,long)"""
        return int.__wrap(__User32.CreateWindowEx(__int.valueOf(arg0), arg1, arg2, __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __long.valueOf(arg8), __long.valueOf(arg9), __long.valueOf(arg10), __long.valueOf(arg11)))

    @staticmethod
    @overload
    def BringWindowToTop(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.User32.BringWindowToTop(long)"""
        return bool.__wrap(__User32.BringWindowToTop(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def SetWindowLongPtr(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.windows.User32.SetWindowLongPtr(long,int,long)"""
        return int.__wrap(__User32.SetWindowLongPtr(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nEnumDisplaySettingsEx(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static int org.lwjgl.system.windows.User32.nEnumDisplaySettingsEx(long,int,long,int)"""
        return int.__wrap(__User32.nEnumDisplaySettingsEx(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def GetDC(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.User32.GetDC(long)"""
        return int.__wrap(__User32.GetDC(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def SetWindowText(arg0: int, arg1: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.windows.User32.SetWindowText(long,java.nio.ByteBuffer)"""
        return bool.__wrap(__User32.SetWindowText(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nSendMessage(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native int org.lwjgl.system.windows.User32.nSendMessage(long,int,long,long,long)"""
        return int.__wrap(__User32.nSendMessage(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))) 
 
 
# CLASS: org.lwjgl.system.windows.DATA_BLOB$Buffer
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
import org.lwjgl.system.windows.DATA_BLOB as __DATA_BLOB_Buffer
__Buffer = __DATA_BLOB_Buffer.Buffer
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
 
class Buffer():
    """org.lwjgl.system.windows.DATA_BLOB.Buffer"""
 
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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def pbData(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB$Buffer.pbData(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pbData(arg0))

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
    def cbData(self) -> int:
        """public int org.lwjgl.system.windows.DATA_BLOB$Buffer.cbData()"""
        return int.__wrap(super(Buffer, self).cbData())

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
    def pbData(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB$Buffer.pbData()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).pbData())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DATA_BLOB$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.LARGE_INTEGER$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.LARGE_INTEGER as __LARGE_INTEGER_Buffer
__Buffer = __LARGE_INTEGER_Buffer.Buffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.LARGE_INTEGER.Buffer"""
 
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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def u_LowPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_LowPart(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).u_LowPart(__int.valueOf(arg0)))

    @overload
    def QuadPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.QuadPart(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).QuadPart(__long.valueOf(arg0)))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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

    @overload
    def u_HighPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_HighPart()"""
        return int.__wrap(super(Buffer, self).u_HighPart())

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
    def u_HighPart(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_HighPart(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).u_HighPart(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def u_LowPart(self) -> int:
        """public int org.lwjgl.system.windows.LARGE_INTEGER$Buffer.u_LowPart()"""
        return int.__wrap(super(Buffer, self).u_LowPart())

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

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.LARGE_INTEGER$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def QuadPart(self) -> int:
        """public long org.lwjgl.system.windows.LARGE_INTEGER$Buffer.QuadPart()"""
        return int.__wrap(super(Buffer, self).QuadPart())

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import org.lwjgl.system.windows.RECT as __RECT
__RECT = __RECT
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.windows.WINDOWPLACEMENT as __WINDOWPLACEMENT_Buffer
__Buffer = __WINDOWPLACEMENT_Buffer.Buffer
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
import org.lwjgl.system.windows.POINT as __POINT
__POINT = __POINT
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.WINDOWPLACEMENT.Buffer"""
 
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
    def showCmd(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.showCmd()"""
        return int.__wrap(super(Buffer, self).showCmd())

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

    @overload
    def ptMaxPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition()"""
        return 'POINT'.__wrap(super(Buffer, self).ptMaxPosition())

    @overload
    def showCmd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.showCmd(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).showCmd(__int.valueOf(arg0)))

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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def flags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.flags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).flags(__int.valueOf(arg0)))

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
    def ptMaxPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ptMaxPosition(arg0))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def ptMinPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition()"""
        return 'POINT'.__wrap(super(Buffer, self).ptMinPosition())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def rcNormalPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition(java.util.function.Consumer<org.lwjgl.system.windows.RECT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).rcNormalPosition(arg0))

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.flags()"""
        return int.__wrap(super(Buffer, self).flags())

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
    def length(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.length(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).length(__int.valueOf(arg0)))

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

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def ptMinPosition(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ptMinPosition(arg0))

    @overload
    def length(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.length()"""
        return int.__wrap(super(Buffer, self).length())

    @overload
    def rcNormalPosition(self, arg0: 'RECT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition(org.lwjgl.system.windows.RECT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).rcNormalPosition(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def ptMinPosition(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMinPosition(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ptMinPosition(arg0))

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

    @overload
    def rcNormalPosition(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.rcNormalPosition()"""
        return 'RECT'.__wrap(super(Buffer, self).rcNormalPosition())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def ptMaxPosition(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer.ptMaxPosition(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).ptMaxPosition(arg0))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WindowProcI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.system.windows.WindowProcI as __WindowProcI
__WindowProcI = __WindowProcI
import java.lang.Long as __long
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class WindowProcI(ABC):
    """org.lwjgl.system.windows.WindowProcI"""
 
    @staticmethod
    def __wrap(java_value: __WindowProcI) -> 'WindowProcI':
        return WindowProcI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowProcI):
        """
        Dynamic initializer for WindowProcI.
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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.windows.WindowProcI.callback(long,long)"""
        super(__WindowProcI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.windows.WindowProcI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(WindowProcI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.windows.WindowProcI.invoke(long,int,long,long)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.system.windows.User32$Functions
from builtins import str
import org.lwjgl.system.windows.User32 as __User32_Functions
__Functions = __User32_Functions.Functions
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
from builtins import int
 
class Functions():
    """org.lwjgl.system.windows.User32.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
 
 
# CLASS: org.lwjgl.system.windows.KEYBDINPUT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import java.lang.Short as __short
import org.lwjgl.system.windows.KEYBDINPUT as __KEYBDINPUT_Buffer
__Buffer = __KEYBDINPUT_Buffer.Buffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.KEYBDINPUT.Buffer"""
 
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

    @overload
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwFlags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwFlags(__int.valueOf(arg0)))

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
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwExtraInfo()"""
        return int.__wrap(super(Buffer, self).dwExtraInfo())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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

    @overload
    def wVk(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT$Buffer.wVk()"""
        return int.__wrap(super(Buffer, self).wVk())

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
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.time(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).time(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def wVk(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.wVk(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wVk(__short.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT$Buffer.time()"""
        return int.__wrap(super(Buffer, self).time())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def wScan(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.wScan(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wScan(__short.valueOf(arg0)))

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

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwFlags()"""
        return int.__wrap(super(Buffer, self).dwFlags())

    @overload
    def wScan(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT$Buffer.wScan()"""
        return int.__wrap(super(Buffer, self).wScan())

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

    @overload
    def dwExtraInfo(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT$Buffer.dwExtraInfo(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwExtraInfo(__long.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.DATA_BLOB
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.DATA_BLOB as __DATA_BLOB_Buffer
__Buffer = __DATA_BLOB_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.windows.DATA_BLOB as __DATA_BLOB
__DATA_BLOB = __DATA_BLOB
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class DATA_BLOB():
    """org.lwjgl.system.windows.DATA_BLOB"""
 
    @staticmethod
    def __wrap(java_value: __DATA_BLOB) -> 'DATA_BLOB':
        return DATA_BLOB(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DATA_BLOB):
        """
        Dynamic initializer for DATA_BLOB.
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
    def malloc(arg0: 'MemoryStack') -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.malloc(org.lwjgl.system.MemoryStack)"""
        return DATA_BLOB.__wrap(__DATA_BLOB.malloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.calloc(int)"""
        return Buffer.__wrap(__DATA_BLOB.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.createSafe(long,int)"""
        return Buffer.__wrap(__DATA_BLOB.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

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
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DATA_BLOB.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.malloc(int)"""
        return Buffer.__wrap(__DATA_BLOB.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.create(int)"""
        return Buffer.__wrap(__DATA_BLOB.create(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'DATA_BLOB') -> 'DATA_BLOB':
        """public org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.set(org.lwjgl.system.windows.DATA_BLOB)"""
        return 'DATA_BLOB'.__wrap(super(__DATA_BLOB, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.calloc(org.lwjgl.system.MemoryStack)"""
        return DATA_BLOB.__wrap(__DATA_BLOB.calloc(arg0))

    @overload
    def cbData(self) -> int:
        """public int org.lwjgl.system.windows.DATA_BLOB.cbData()"""
        return int.__wrap(super(DATA_BLOB, self).cbData())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.createSafe(long)"""
        return DATA_BLOB.__wrap(__DATA_BLOB.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.create(long,int)"""
        return Buffer.__wrap(__DATA_BLOB.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ncbData(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DATA_BLOB.ncbData(long,int)"""
        __DATA_BLOB.ncbData(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DATA_BLOB$Buffer org.lwjgl.system.windows.DATA_BLOB.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DATA_BLOB.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def pbData(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB.pbData()"""
        return 'ByteBuffer'.__wrap(super(DATA_BLOB, self).pbData())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def npbData(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.DATA_BLOB.npbData(long,java.nio.ByteBuffer)"""
        __DATA_BLOB.npbData(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.calloc()"""
        return DATA_BLOB.__wrap(__DATA_BLOB.calloc())

    @staticmethod
    @overload
    def npbData(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DATA_BLOB.npbData(long)"""
        return ByteBuffer.__wrap(__DATA_BLOB.npbData(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DATA_BLOB(java.nio.ByteBuffer)"""
        val = __DATA_BLOB(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.DATA_BLOB.validate(long)"""
        __DATA_BLOB.validate(__long.valueOf(arg0))

    @overload
    def pbData(self, arg0: 'ByteBuffer') -> 'DATA_BLOB':
        """public org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.pbData(java.nio.ByteBuffer)"""
        return 'DATA_BLOB'.__wrap(super(__DATA_BLOB, self).pbData(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.create()"""
        return DATA_BLOB.__wrap(__DATA_BLOB.create())

    @staticmethod
    @overload
    def create(arg0: int) -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.create(long)"""
        return DATA_BLOB.__wrap(__DATA_BLOB.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ncbData(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DATA_BLOB.ncbData(long)"""
        return int.__wrap(__DATA_BLOB.ncbData(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'DATA_BLOB':
        """public static org.lwjgl.system.windows.DATA_BLOB org.lwjgl.system.windows.DATA_BLOB.malloc()"""
        return DATA_BLOB.__wrap(__DATA_BLOB.malloc())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.DATA_BLOB.sizeof()"""
        return int.__wrap(super(DATA_BLOB, self).sizeof()) 
 
 
# CLASS: org.lwjgl.system.windows.MONITORINFOEX
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.RECT as __RECT
__RECT = __RECT
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.MONITORINFOEX as __MONITORINFOEX_Buffer
__Buffer = __MONITORINFOEX_Buffer.Buffer
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.system.windows.MONITORINFOEX as __MONITORINFOEX
__MONITORINFOEX = __MONITORINFOEX
from builtins import int
 
class MONITORINFOEX():
    """org.lwjgl.system.windows.MONITORINFOEX"""
 
    @staticmethod
    def __wrap(java_value: __MONITORINFOEX) -> 'MONITORINFOEX':
        return MONITORINFOEX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MONITORINFOEX):
        """
        Dynamic initializer for MONITORINFOEX.
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
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.sizeof()"""
        return int.__wrap(super(MONITORINFOEX, self).sizeof())

    @staticmethod
    @overload
    def create() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.create()"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.create())

    @staticmethod
    @overload
    def nrcMonitor(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.nrcMonitor(long)"""
        return RECT.__wrap(__MONITORINFOEX.nrcMonitor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.calloc()"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.mallocStack(int)"""
        return Buffer.__wrap(__MONITORINFOEX.mallocStack(__int.valueOf(arg0)))

    @overload
    def szDevice(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX.szDevice()"""
        return 'ByteBuffer'.__wrap(super(MONITORINFOEX, self).szDevice())

    @staticmethod
    @overload
    def nszDeviceString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.MONITORINFOEX.nszDeviceString(long)"""
        return str.__wrap(__MONITORINFOEX.nszDeviceString(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.callocStack(int)"""
        return Buffer.__wrap(__MONITORINFOEX.callocStack(__int.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MONITORINFOEX.ndwFlags(long)"""
        return int.__wrap(__MONITORINFOEX.ndwFlags(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MONITORINFOEX.ncbSize(long,int)"""
        __MONITORINFOEX.ncbSize(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.calloc(int)"""
        return Buffer.__wrap(__MONITORINFOEX.calloc(__int.valueOf(arg0)))

    @overload
    def cbSize(self, arg0: int) -> 'MONITORINFOEX':
        """public org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.cbSize(int)"""
        return 'MONITORINFOEX'.__wrap(super(__MONITORINFOEX, self).cbSize(__int.valueOf(arg0)))

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.dwFlags()"""
        return int.__wrap(super(MONITORINFOEX, self).dwFlags())

    @staticmethod
    @overload
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MONITORINFOEX.ncbSize(long)"""
        return int.__wrap(__MONITORINFOEX.ncbSize(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MONITORINFOEX(java.nio.ByteBuffer)"""
        val = __MONITORINFOEX(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.calloc(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.calloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MONITORINFOEX.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.malloc()"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.malloc())

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
    def rcMonitor(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.rcMonitor()"""
        return 'RECT'.__wrap(super(MONITORINFOEX, self).rcMonitor())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MONITORINFOEX.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.malloc(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.malloc(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.createSafe(long)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.create(int)"""
        return Buffer.__wrap(__MONITORINFOEX.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.mallocStack(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.malloc(int)"""
        return Buffer.__wrap(__MONITORINFOEX.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MONITORINFOEX.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.createSafe(long,int)"""
        return Buffer.__wrap(__MONITORINFOEX.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.mallocStack()"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.create(long,int)"""
        return Buffer.__wrap(__MONITORINFOEX.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def callocStack() -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.callocStack()"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.callocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.create(long)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MONITORINFOEX.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nszDevice(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX.nszDevice(long)"""
        return ByteBuffer.__wrap(__MONITORINFOEX.nszDevice(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX.cbSize()"""
        return int.__wrap(super(MONITORINFOEX, self).cbSize())

    @overload
    def set(self, arg0: 'MONITORINFOEX') -> 'MONITORINFOEX':
        """public org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.set(org.lwjgl.system.windows.MONITORINFOEX)"""
        return 'MONITORINFOEX'.__wrap(super(__MONITORINFOEX, self).set(arg0))

    @overload
    def szDeviceString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.MONITORINFOEX.szDeviceString()"""
        return str.__wrap(super(MONITORINFOEX, self).szDeviceString())

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
    def callocStack(arg0: 'MemoryStack') -> 'MONITORINFOEX':
        """public static org.lwjgl.system.windows.MONITORINFOEX org.lwjgl.system.windows.MONITORINFOEX.callocStack(org.lwjgl.system.MemoryStack)"""
        return MONITORINFOEX.__wrap(__MONITORINFOEX.callocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nrcWork(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.nrcWork(long)"""
        return RECT.__wrap(__MONITORINFOEX.nrcWork(__long.valueOf(arg0)))

    @overload
    def rcWork(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX.rcWork()"""
        return 'RECT'.__wrap(super(MONITORINFOEX, self).rcWork()) 
 
 
# CLASS: org.lwjgl.system.windows.POINT
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.windows.POINT as __POINT_Buffer
__Buffer = __POINT_Buffer.Buffer
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.windows.POINT as __POINT
__POINT = __POINT
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class POINT():
    """org.lwjgl.system.windows.POINT"""
 
    @staticmethod
    def __wrap(java_value: __POINT) -> 'POINT':
        return POINT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __POINT):
        """
        Dynamic initializer for POINT.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINT.y()"""
        return int.__wrap(super(POINT, self).y())

    @staticmethod
    @overload
    def calloc() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.calloc()"""
        return POINT.__wrap(__POINT.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.calloc(int)"""
        return Buffer.__wrap(__POINT.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.create(long)"""
        return POINT.__wrap(__POINT.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.mallocStack()"""
        return POINT.__wrap(__POINT.mallocStack())

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINT.nx(long)"""
        return int.__wrap(__POINT.nx(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINT(java.nio.ByteBuffer)"""
        val = __POINT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return POINT.__wrap(__POINT.mallocStack(arg0))

    @overload
    def set(self, arg0: int, arg1: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.set(int,int)"""
        return 'POINT'.__wrap(super(__POINT, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.calloc(org.lwjgl.system.MemoryStack)"""
        return POINT.__wrap(__POINT.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.create(int)"""
        return Buffer.__wrap(__POINT.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINT.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.create()"""
        return POINT.__wrap(__POINT.create())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.callocStack()"""
        return POINT.__wrap(__POINT.callocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINT.x()"""
        return int.__wrap(super(POINT, self).x())

    @staticmethod
    @overload
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINT.nx(long,int)"""
        __POINT.nx(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.POINT.sizeof()"""
        return int.__wrap(super(POINT, self).sizeof())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.callocStack(org.lwjgl.system.MemoryStack)"""
        return POINT.__wrap(__POINT.callocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.callocStack(int)"""
        return Buffer.__wrap(__POINT.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINT.ny(long,int)"""
        __POINT.ny(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.createSafe(long)"""
        return POINT.__wrap(__POINT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.mallocStack(int)"""
        return Buffer.__wrap(__POINT.mallocStack(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'POINT') -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.set(org.lwjgl.system.windows.POINT)"""
        return 'POINT'.__wrap(super(__POINT, self).set(arg0))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINT.ny(long)"""
        return int.__wrap(__POINT.ny(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.malloc(org.lwjgl.system.MemoryStack)"""
        return POINT.__wrap(__POINT.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.create(long,int)"""
        return Buffer.__wrap(__POINT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.malloc(int)"""
        return Buffer.__wrap(__POINT.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.malloc()"""
        return POINT.__wrap(__POINT.malloc())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINT.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def x(self, arg0: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.x(int)"""
        return 'POINT'.__wrap(super(__POINT, self).x(__int.valueOf(arg0)))

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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINT$Buffer org.lwjgl.system.windows.POINT.createSafe(long,int)"""
        return Buffer.__wrap(__POINT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def y(self, arg0: int) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.POINT.y(int)"""
        return 'POINT'.__wrap(super(__POINT, self).y(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.system.windows.DEVMODE$Buffer
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
import java.lang.Short as __short
from builtins import bool
from builtins import str
import org.lwjgl.system.windows.POINTL as __POINTL
__POINTL = __POINTL
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
import org.lwjgl.system.windows.DEVMODE as __DEVMODE_Buffer
__Buffer = __DEVMODE_Buffer.Buffer
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
 
class Buffer():
    """org.lwjgl.system.windows.DEVMODE.Buffer"""
 
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
    def dmPosition(self) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE$Buffer.dmPosition()"""
        return 'POINTL'.__wrap(super(Buffer, self).dmPosition())

    @overload
    def dmFormName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE$Buffer.dmFormName()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).dmFormName())

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def dmDriverExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverExtra(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dmDriverExtra(__short.valueOf(arg0)))

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
    def dmPaperWidth(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperWidth()"""
        return int.__wrap(super(Buffer, self).dmPaperWidth())

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

    @overload
    def dmPrintQuality(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPrintQuality()"""
        return int.__wrap(super(Buffer, self).dmPrintQuality())

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
    def dmCopies(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmCopies()"""
        return int.__wrap(super(Buffer, self).dmCopies())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def dmNup(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmNup()"""
        return int.__wrap(super(Buffer, self).dmNup())

    @overload
    def dmLogPixels(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmLogPixels()"""
        return int.__wrap(super(Buffer, self).dmLogPixels())

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
    def dmBitsPerPel(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmBitsPerPel()"""
        return int.__wrap(super(Buffer, self).dmBitsPerPel())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def dmPelsHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPelsHeight()"""
        return int.__wrap(super(Buffer, self).dmPelsHeight())

    @overload
    def dmPaperSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperSize()"""
        return int.__wrap(super(Buffer, self).dmPaperSize())

    @overload
    def dmOrientation(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmOrientation()"""
        return int.__wrap(super(Buffer, self).dmOrientation())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DEVMODE$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def dmDeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE$Buffer.dmDeviceNameString()"""
        return str.__wrap(super(Buffer, self).dmDeviceNameString())

    @overload
    def dmDriverVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverVersion()"""
        return int.__wrap(super(Buffer, self).dmDriverVersion())

    @overload
    def dmMediaType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmMediaType()"""
        return int.__wrap(super(Buffer, self).dmMediaType())

    @overload
    def dmDisplayFlags(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFlags()"""
        return int.__wrap(super(Buffer, self).dmDisplayFlags())

    @overload
    def dmPanningHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPanningHeight()"""
        return int.__wrap(super(Buffer, self).dmPanningHeight())

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
    def dmReserved2(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmReserved2()"""
        return int.__wrap(super(Buffer, self).dmReserved2())

    @overload
    def dmCollate(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmCollate()"""
        return int.__wrap(super(Buffer, self).dmCollate())

    @overload
    def dmSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmSize()"""
        return int.__wrap(super(Buffer, self).dmSize())

    @overload
    def dmDisplayFixedOutput(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFixedOutput()"""
        return int.__wrap(super(Buffer, self).dmDisplayFixedOutput())

    @overload
    def dmDitherType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDitherType()"""
        return int.__wrap(super(Buffer, self).dmDitherType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dmFormNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE$Buffer.dmFormNameString()"""
        return str.__wrap(super(Buffer, self).dmFormNameString())

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
    def dmPaperLength(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmPaperLength()"""
        return int.__wrap(super(Buffer, self).dmPaperLength())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def dmSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmSize(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dmSize(__short.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def dmColor(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmColor()"""
        return int.__wrap(super(Buffer, self).dmColor())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def dmDisplayFrequency(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayFrequency()"""
        return int.__wrap(super(Buffer, self).dmDisplayFrequency())

    @overload
    def dmSpecVersion(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE$Buffer.dmSpecVersion(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dmSpecVersion(__short.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def dmICMMethod(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmICMMethod()"""
        return int.__wrap(super(Buffer, self).dmICMMethod())

    @overload
    def dmICMIntent(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmICMIntent()"""
        return int.__wrap(super(Buffer, self).dmICMIntent())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def dmYResolution(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmYResolution()"""
        return int.__wrap(super(Buffer, self).dmYResolution())

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

    @overload
    def dmDriverExtra(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDriverExtra()"""
        return int.__wrap(super(Buffer, self).dmDriverExtra())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DEVMODE$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dmTTOption(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmTTOption()"""
        return int.__wrap(super(Buffer, self).dmTTOption())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def dmDisplayOrientation(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmDisplayOrientation()"""
        return int.__wrap(super(Buffer, self).dmDisplayOrientation())

    @overload
    def dmPanningWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPanningWidth()"""
        return int.__wrap(super(Buffer, self).dmPanningWidth())

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

    @overload
    def dmDefaultSource(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDefaultSource()"""
        return int.__wrap(super(Buffer, self).dmDefaultSource())

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
    def dmScale(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmScale()"""
        return int.__wrap(super(Buffer, self).dmScale())

    @overload
    def dmPelsWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmPelsWidth()"""
        return int.__wrap(super(Buffer, self).dmPelsWidth())

    @overload
    def dmFields(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmFields()"""
        return int.__wrap(super(Buffer, self).dmFields())

    @overload
    def dmSpecVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmSpecVersion()"""
        return int.__wrap(super(Buffer, self).dmSpecVersion())

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

    @overload
    def dmDeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE$Buffer.dmDeviceName()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).dmDeviceName())

    @overload
    def dmDuplex(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE$Buffer.dmDuplex()"""
        return int.__wrap(super(Buffer, self).dmDuplex())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def dmReserved1(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE$Buffer.dmReserved1()"""
        return int.__wrap(super(Buffer, self).dmReserved1())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.TOUCHINPUT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import org.lwjgl.system.windows.TOUCHINPUT as __TOUCHINPUT_Buffer
__Buffer = __TOUCHINPUT_Buffer.Buffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.TOUCHINPUT.Buffer"""
 
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.TOUCHINPUT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.TOUCHINPUT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def cxContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.cxContact()"""
        return int.__wrap(super(Buffer, self).cxContact())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwID(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwID()"""
        return int.__wrap(super(Buffer, self).dwID())

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

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
    def hSource(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT$Buffer.hSource()"""
        return int.__wrap(super(Buffer, self).hSource())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwFlags()"""
        return int.__wrap(super(Buffer, self).dwFlags())

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
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwExtraInfo()"""
        return int.__wrap(super(Buffer, self).dwExtraInfo())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def cyContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.cyContact()"""
        return int.__wrap(super(Buffer, self).cyContact())

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
    def dwMask(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwMask()"""
        return int.__wrap(super(Buffer, self).dwMask())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def dwTime(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT$Buffer.dwTime()"""
        return int.__wrap(super(Buffer, self).dwTime())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WindowsUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.windows.WindowsUtil as __WindowsUtil
__WindowsUtil = __WindowsUtil
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WindowsUtil():
    """org.lwjgl.system.windows.WindowsUtil"""
 
    @staticmethod
    def __wrap(java_value: __WindowsUtil) -> 'WindowsUtil':
        return WindowsUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowsUtil):
        """
        Dynamic initializer for WindowsUtil.
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
    def windowsThrowException(arg0: str):
        """public static void org.lwjgl.system.windows.WindowsUtil.windowsThrowException(java.lang.String)"""
        __WindowsUtil.windowsThrowException(arg0)

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
 
 
# CLASS: org.lwjgl.system.windows.HARDWAREINPUT
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.HARDWAREINPUT as __HARDWAREINPUT_Buffer
__Buffer = __HARDWAREINPUT_Buffer.Buffer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.windows.HARDWAREINPUT as __HARDWAREINPUT
__HARDWAREINPUT = __HARDWAREINPUT
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class HARDWAREINPUT():
    """org.lwjgl.system.windows.HARDWAREINPUT"""
 
    @staticmethod
    def __wrap(java_value: __HARDWAREINPUT) -> 'HARDWAREINPUT':
        return HARDWAREINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HARDWAREINPUT):
        """
        Dynamic initializer for HARDWAREINPUT.
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
    def calloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc()"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.calloc())

    @staticmethod
    @overload
    def nwParamL(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long,short)"""
        __HARDWAREINPUT.nwParamL(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create()"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.create())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nuMsg(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long)"""
        return int.__wrap(__HARDWAREINPUT.nuMsg(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(int,short,short)"""
        return 'HARDWAREINPUT'.__wrap(super(__HARDWAREINPUT, self).set(__int.valueOf(arg0), __short.valueOf(arg1), __short.valueOf(arg2)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.HARDWAREINPUT(java.nio.ByteBuffer)"""
        val = __HARDWAREINPUT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def mallocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack()"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.mallocStack())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.mallocStack(arg0))

    @overload
    def wParamL(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamL(short)"""
        return 'HARDWAREINPUT'.__wrap(super(__HARDWAREINPUT, self).wParamL(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(long,int)"""
        return Buffer.__wrap(__HARDWAREINPUT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int)"""
        return Buffer.__wrap(__HARDWAREINPUT.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__HARDWAREINPUT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.malloc(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack()"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.callocStack())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def wParamL(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamL()"""
        return int.__wrap(super(HARDWAREINPUT, self).wParamL())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int)"""
        return Buffer.__wrap(__HARDWAREINPUT.callocStack(__int.valueOf(arg0)))

    @overload
    def uMsg(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.uMsg()"""
        return int.__wrap(super(HARDWAREINPUT, self).uMsg())

    @staticmethod
    @overload
    def create(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.create(long)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.calloc(arg0))

    @overload
    def wParamH(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.wParamH(short)"""
        return 'HARDWAREINPUT'.__wrap(super(__HARDWAREINPUT, self).wParamH(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamH(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long,short)"""
        __HARDWAREINPUT.nwParamH(__long.valueOf(arg0), __short.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nwParamL(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamL(long)"""
        return int.__wrap(__HARDWAREINPUT.nwParamL(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__HARDWAREINPUT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.createSafe(long,int)"""
        return Buffer.__wrap(__HARDWAREINPUT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.malloc()"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.malloc())

    @overload
    def uMsg(self, arg0: int) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.uMsg(int)"""
        return 'HARDWAREINPUT'.__wrap(super(__HARDWAREINPUT, self).uMsg(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nwParamH(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.HARDWAREINPUT.nwParamH(long)"""
        return int.__wrap(__HARDWAREINPUT.nwParamH(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.mallocStack(int)"""
        return Buffer.__wrap(__HARDWAREINPUT.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nuMsg(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.HARDWAREINPUT.nuMsg(long,int)"""
        __HARDWAREINPUT.nuMsg(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.create(int)"""
        return Buffer.__wrap(__HARDWAREINPUT.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__HARDWAREINPUT.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT.sizeof()"""
        return int.__wrap(super(HARDWAREINPUT, self).sizeof())

    @overload
    def set(self, arg0: 'HARDWAREINPUT') -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.set(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'HARDWAREINPUT'.__wrap(super(__HARDWAREINPUT, self).set(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

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
    def wParamH(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT.wParamH()"""
        return int.__wrap(super(HARDWAREINPUT, self).wParamH())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__HARDWAREINPUT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT.malloc(int)"""
        return Buffer.__wrap(__HARDWAREINPUT.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.HARDWAREINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return HARDWAREINPUT.__wrap(__HARDWAREINPUT.callocStack(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.WINDOWPLACEMENT
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.RECT as __RECT
__RECT = __RECT
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.WINDOWPLACEMENT as __WINDOWPLACEMENT
__WINDOWPLACEMENT = __WINDOWPLACEMENT
import org.lwjgl.system.windows.WINDOWPLACEMENT as __WINDOWPLACEMENT_Buffer
__Buffer = __WINDOWPLACEMENT_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.windows.POINT as __POINT
__POINT = __POINT
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class WINDOWPLACEMENT():
    """org.lwjgl.system.windows.WINDOWPLACEMENT"""
 
    @staticmethod
    def __wrap(java_value: __WINDOWPLACEMENT) -> 'WINDOWPLACEMENT':
        return WINDOWPLACEMENT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WINDOWPLACEMENT):
        """
        Dynamic initializer for WINDOWPLACEMENT.
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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.create(long,int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'WINDOWPLACEMENT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.set(org.lwjgl.system.windows.WINDOWPLACEMENT)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.calloc(__int.valueOf(arg0), arg1))

    @overload
    def showCmd(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.showCmd()"""
        return int.__wrap(super(WINDOWPLACEMENT, self).showCmd())

    @staticmethod
    @overload
    def mallocStack() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack()"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.mallocStack())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.createSafe(long,int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nptMaxPosition(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.nptMaxPosition(long)"""
        return POINT.__wrap(__WINDOWPLACEMENT.nptMaxPosition(__long.valueOf(arg0)))

    @overload
    def length(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.length()"""
        return int.__wrap(super(WINDOWPLACEMENT, self).length())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.create(long)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.create(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

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
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.calloc()"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.calloc())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WINDOWPLACEMENT(java.nio.ByteBuffer)"""
        val = __WINDOWPLACEMENT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.callocStack(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nflags(long)"""
        return int.__wrap(__WINDOWPLACEMENT.nflags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def showCmd(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.showCmd(int)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).showCmd(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'POINT', arg4: 'POINT', arg5: 'RECT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.set(int,int,int,org.lwjgl.system.windows.POINT,org.lwjgl.system.windows.POINT,org.lwjgl.system.windows.RECT)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3, arg4, arg5))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nrcNormalPosition(arg0: int, arg1: 'RECT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nrcNormalPosition(long,org.lwjgl.system.windows.RECT)"""
        __WINDOWPLACEMENT.nrcNormalPosition(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.createSafe(long)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.malloc(int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.malloc(__int.valueOf(arg0)))

    @overload
    def ptMinPosition(self, arg0: 'POINT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition(org.lwjgl.system.windows.POINT)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).ptMinPosition(arg0))

    @overload
    def rcNormalPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition(java.util.function.Consumer<org.lwjgl.system.windows.RECT>)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).rcNormalPosition(arg0))

    @staticmethod
    @overload
    def nlength(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nlength(long)"""
        return int.__wrap(__WINDOWPLACEMENT.nlength(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def flags(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.flags()"""
        return int.__wrap(super(WINDOWPLACEMENT, self).flags())

    @staticmethod
    @overload
    def nptMinPosition(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.nptMinPosition(long)"""
        return POINT.__wrap(__WINDOWPLACEMENT.nptMinPosition(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.mallocStack(arg0))

    @overload
    def flags(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.flags(int)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).flags(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def callocStack() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.callocStack()"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.callocStack())

    @overload
    def ptMinPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition()"""
        return 'POINT'.__wrap(super(WINDOWPLACEMENT, self).ptMinPosition())

    @staticmethod
    @overload
    def malloc() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.malloc()"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.malloc())

    @overload
    def ptMaxPosition(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition()"""
        return 'POINT'.__wrap(super(WINDOWPLACEMENT, self).ptMaxPosition())

    @staticmethod
    @overload
    def create() -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.create()"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.create())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.WINDOWPLACEMENT.sizeof()"""
        return int.__wrap(super(WINDOWPLACEMENT, self).sizeof())

    @overload
    def length(self, arg0: int) -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.length(int)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).length(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nshowCmd(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WINDOWPLACEMENT.nshowCmd(long)"""
        return int.__wrap(__WINDOWPLACEMENT.nshowCmd(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.create(int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'WINDOWPLACEMENT':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(org.lwjgl.system.MemoryStack)"""
        return WINDOWPLACEMENT.__wrap(__WINDOWPLACEMENT.calloc(arg0))

    @overload
    def ptMaxPosition(self, arg0: 'POINT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition(org.lwjgl.system.windows.POINT)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).ptMaxPosition(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def ptMaxPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMaxPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).ptMaxPosition(arg0))

    @staticmethod
    @overload
    def nrcNormalPosition(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT.nrcNormalPosition(long)"""
        return RECT.__wrap(__WINDOWPLACEMENT.nrcNormalPosition(__long.valueOf(arg0)))

    @overload
    def rcNormalPosition(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition()"""
        return 'RECT'.__wrap(super(WINDOWPLACEMENT, self).rcNormalPosition())

    @staticmethod
    @overload
    def nptMinPosition(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nptMinPosition(long,org.lwjgl.system.windows.POINT)"""
        __WINDOWPLACEMENT.nptMinPosition(__long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nshowCmd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nshowCmd(long,int)"""
        __WINDOWPLACEMENT.nshowCmd(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.calloc(int)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WINDOWPLACEMENT$Buffer org.lwjgl.system.windows.WINDOWPLACEMENT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WINDOWPLACEMENT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def ptMinPosition(self, arg0: 'Consumer') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.ptMinPosition(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).ptMinPosition(arg0))

    @staticmethod
    @overload
    def nlength(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nlength(long,int)"""
        __WINDOWPLACEMENT.nlength(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rcNormalPosition(self, arg0: 'RECT') -> 'WINDOWPLACEMENT':
        """public org.lwjgl.system.windows.WINDOWPLACEMENT org.lwjgl.system.windows.WINDOWPLACEMENT.rcNormalPosition(org.lwjgl.system.windows.RECT)"""
        return 'WINDOWPLACEMENT'.__wrap(super(__WINDOWPLACEMENT, self).rcNormalPosition(arg0))

    @staticmethod
    @overload
    def nflags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nflags(long,int)"""
        __WINDOWPLACEMENT.nflags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nptMaxPosition(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.WINDOWPLACEMENT.nptMaxPosition(long,org.lwjgl.system.windows.POINT)"""
        __WINDOWPLACEMENT.nptMaxPosition(__long.valueOf(arg0), arg1) 
 
 
# CLASS: org.lwjgl.system.windows.WNDCLASSEX$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.WNDCLASSEX as __WNDCLASSEX_Buffer
__Buffer = __WNDCLASSEX_Buffer.Buffer
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.WindowProc as __WindowProc
__WindowProc = __WindowProc
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.WNDCLASSEX.Buffer"""
 
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
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def style(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.style()"""
        return int.__wrap(super(Buffer, self).style())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def cbClsExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbClsExtra()"""
        return int.__wrap(super(Buffer, self).cbClsExtra())

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
    def cbWndExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbWndExtra()"""
        return int.__wrap(super(Buffer, self).cbWndExtra())

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

    @overload
    def lpfnWndProc(self) -> 'WindowProc':
        """public org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpfnWndProc()"""
        return 'WindowProc'.__wrap(super(Buffer, self).lpfnWndProc())

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbSize()"""
        return int.__wrap(super(Buffer, self).cbSize())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).position())

    @overload
    def hIconSm(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIconSm()"""
        return int.__wrap(super(Buffer, self).hIconSm())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def hInstance(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hInstance()"""
        return int.__wrap(super(Buffer, self).hInstance())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hCursor(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hCursor()"""
        return int.__wrap(super(Buffer, self).hCursor())

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
    def lpszMenuName(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuName(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).lpszMenuName(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def hInstance(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hInstance(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hInstance(__long.valueOf(arg0)))

    @overload
    def hbrBackground(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hbrBackground(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hbrBackground(__long.valueOf(arg0)))

    @overload
    def style(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.style(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).style(__int.valueOf(arg0)))

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
    def lpszMenuNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuNameString()"""
        return str.__wrap(super(Buffer, self).lpszMenuNameString())

    @overload
    def hIcon(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIcon()"""
        return int.__wrap(super(Buffer, self).hIcon())

    @overload
    def hIconSm(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIconSm(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hIconSm(__long.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def lpszClassName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassName()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).lpszClassName())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def hbrBackground(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX$Buffer.hbrBackground()"""
        return int.__wrap(super(Buffer, self).hbrBackground())

    @overload
    def hCursor(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hCursor(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hCursor(__long.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def hIcon(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.hIcon(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hIcon(__long.valueOf(arg0)))

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

    @overload
    def lpszMenuName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszMenuName()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).lpszMenuName())

    @overload
    def lpszClassNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassNameString()"""
        return str.__wrap(super(Buffer, self).lpszClassNameString())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def cbClsExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbClsExtra(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cbClsExtra(__int.valueOf(arg0)))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @overload
    def cbWndExtra(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbWndExtra(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cbWndExtra(__int.valueOf(arg0)))

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

    @overload
    def lpfnWndProc(self, arg0: 'WindowProcI') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpfnWndProc(org.lwjgl.system.windows.WindowProcI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).lpfnWndProc(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def lpszClassName(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.lpszClassName(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).lpszClassName(arg0))

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def cbSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX$Buffer.cbSize(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cbSize(__int.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.MSG$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.MSG as __MSG_Buffer
__Buffer = __MSG_Buffer.Buffer
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
import org.lwjgl.system.windows.POINT as __POINT
__POINT = __POINT
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.MSG.Buffer"""
 
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
    def wParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.wParam()"""
        return int.__wrap(super(Buffer, self).wParam())

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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def lParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.lParam()"""
        return int.__wrap(super(Buffer, self).lParam())

    @overload
    def message(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.message(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).message(__int.valueOf(arg0)))

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
    def wParam(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.wParam(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wParam(__long.valueOf(arg0)))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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

    @overload
    def pt(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG$Buffer.pt()"""
        return 'POINT'.__wrap(super(Buffer, self).pt())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pt(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.pt(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pt(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MSG$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def hwnd(self) -> int:
        """public long org.lwjgl.system.windows.MSG$Buffer.hwnd()"""
        return int.__wrap(super(Buffer, self).hwnd())

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.MSG$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def lParam(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.lParam(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).lParam(__long.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def pt(self, arg0: 'POINT') -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.pt(org.lwjgl.system.windows.POINT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pt(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.time(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).time(__int.valueOf(arg0)))

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MSG$Buffer.time()"""
        return int.__wrap(super(Buffer, self).time())

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

    @overload
    def message(self) -> int:
        """public int org.lwjgl.system.windows.MSG$Buffer.message()"""
        return int.__wrap(super(Buffer, self).message())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def hwnd(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG$Buffer.hwnd(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).hwnd(__long.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WNDCLASSEX
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.WNDCLASSEX as __WNDCLASSEX_Buffer
__Buffer = __WNDCLASSEX_Buffer.Buffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.WindowProc as __WindowProc
__WindowProc = __WindowProc
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
import org.lwjgl.system.windows.WNDCLASSEX as __WNDCLASSEX
__WNDCLASSEX = __WNDCLASSEX
from builtins import bool
from builtins import int
 
class WNDCLASSEX():
    """org.lwjgl.system.windows.WNDCLASSEX"""
 
    @staticmethod
    def __wrap(java_value: __WNDCLASSEX) -> 'WNDCLASSEX':
        return WNDCLASSEX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WNDCLASSEX):
        """
        Dynamic initializer for WNDCLASSEX.
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
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WNDCLASSEX.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def cbWndExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbWndExtra()"""
        return int.__wrap(super(WNDCLASSEX, self).cbWndExtra())

    @overload
    def set(self, arg0: int, arg1: int, arg2: 'WindowProcI', arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: 'ByteBuffer', arg10: 'ByteBuffer', arg11: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.set(int,int,org.lwjgl.system.windows.WindowProcI,int,int,long,long,long,long,java.nio.ByteBuffer,java.nio.ByteBuffer,long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).set(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), __long.valueOf(arg5), __long.valueOf(arg6), __long.valueOf(arg7), __long.valueOf(arg8), arg9, arg10, __long.valueOf(arg11)))

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbSize()"""
        return int.__wrap(super(WNDCLASSEX, self).cbSize())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nhCursor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhCursor(long)"""
        return int.__wrap(__WNDCLASSEX.nhCursor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbClsExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbClsExtra(long,int)"""
        __WNDCLASSEX.ncbClsExtra(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nlpszClassName(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpszClassName(long,java.nio.ByteBuffer)"""
        __WNDCLASSEX.nlpszClassName(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nlpfnWndProc(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX.nlpfnWndProc(long)"""
        return WindowProc.__wrap(__WNDCLASSEX.nlpfnWndProc(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

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
    def calloc() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.calloc()"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.calloc())

    @overload
    def cbClsExtra(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.cbClsExtra()"""
        return int.__wrap(super(WNDCLASSEX, self).cbClsExtra())

    @staticmethod
    @overload
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbSize(long)"""
        return int.__wrap(__WNDCLASSEX.ncbSize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nhInstance(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhInstance(long)"""
        return int.__wrap(__WNDCLASSEX.nhInstance(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlpszMenuName(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuName(long,java.nio.ByteBuffer)"""
        __WNDCLASSEX.nlpszMenuName(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def ncbWndExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbWndExtra(long,int)"""
        __WNDCLASSEX.ncbWndExtra(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hInstance(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hInstance()"""
        return int.__wrap(super(WNDCLASSEX, self).hInstance())

    @staticmethod
    @overload
    def create(arg0: int) -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.create(long)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.callocStack(int)"""
        return Buffer.__wrap(__WNDCLASSEX.callocStack(__int.valueOf(arg0)))

    @overload
    def lpszClassName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.lpszClassName()"""
        return 'ByteBuffer'.__wrap(super(WNDCLASSEX, self).lpszClassName())

    @staticmethod
    @overload
    def create() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.create()"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.create())

    @overload
    def hIconSm(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hIconSm()"""
        return int.__wrap(super(WNDCLASSEX, self).hIconSm())

    @staticmethod
    @overload
    def nhIconSm(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhIconSm(long)"""
        return int.__wrap(__WNDCLASSEX.nhIconSm(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlpszClassName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.nlpszClassName(long)"""
        return ByteBuffer.__wrap(__WNDCLASSEX.nlpszClassName(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def hbrBackground(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hbrBackground()"""
        return int.__wrap(super(WNDCLASSEX, self).hbrBackground())

    @staticmethod
    @overload
    def nstyle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nstyle(long,int)"""
        __WNDCLASSEX.nstyle(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hIcon(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hIcon(long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).hIcon(__long.valueOf(arg0)))

    @overload
    def style(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.style()"""
        return int.__wrap(super(WNDCLASSEX, self).style())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.createSafe(long)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.createSafe(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'WNDCLASSEX') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.set(org.lwjgl.system.windows.WNDCLASSEX)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).set(arg0))

    @staticmethod
    @overload
    def nlpszMenuNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuNameString(long)"""
        return str.__wrap(__WNDCLASSEX.nlpszMenuNameString(__long.valueOf(arg0)))

    @overload
    def lpszClassName(self, arg0: 'ByteBuffer') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpszClassName(java.nio.ByteBuffer)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).lpszClassName(arg0))

    @staticmethod
    @overload
    def nhIconSm(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhIconSm(long,long)"""
        __WNDCLASSEX.nhIconSm(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nhIcon(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhIcon(long,long)"""
        __WNDCLASSEX.nhIcon(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def hCursor(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hCursor(long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).hCursor(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.WNDCLASSEX(java.nio.ByteBuffer)"""
        val = __WNDCLASSEX(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.validate(long)"""
        __WNDCLASSEX.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.callocStack()"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.callocStack())

    @overload
    def hIconSm(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hIconSm(long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).hIconSm(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.malloc(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.malloc(arg0))

    @staticmethod
    @overload
    def ncbWndExtra(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbWndExtra(long)"""
        return int.__wrap(__WNDCLASSEX.ncbWndExtra(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.malloc()"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.malloc())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.WNDCLASSEX.sizeof()"""
        return int.__wrap(super(WNDCLASSEX, self).sizeof())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.calloc(int)"""
        return Buffer.__wrap(__WNDCLASSEX.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nhbrBackground(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhbrBackground(long,long)"""
        __WNDCLASSEX.nhbrBackground(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WNDCLASSEX.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nhCursor(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhCursor(long,long)"""
        __WNDCLASSEX.nhCursor(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def hInstance(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hInstance(long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).hInstance(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.mallocStack()"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.mallocStack())

    @overload
    def cbSize(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbSize(int)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).cbSize(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.malloc(int)"""
        return Buffer.__wrap(__WNDCLASSEX.malloc(__int.valueOf(arg0)))

    @overload
    def hbrBackground(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.hbrBackground(long)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).hbrBackground(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.create(long,int)"""
        return Buffer.__wrap(__WNDCLASSEX.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WNDCLASSEX.malloc(__int.valueOf(arg0), arg1))

    @overload
    def style(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.style(int)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).style(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def lpszMenuName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.lpszMenuName()"""
        return 'ByteBuffer'.__wrap(super(WNDCLASSEX, self).lpszMenuName())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.mallocStack(int)"""
        return Buffer.__wrap(__WNDCLASSEX.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.createSafe(long,int)"""
        return Buffer.__wrap(__WNDCLASSEX.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.ncbSize(long,int)"""
        __WNDCLASSEX.ncbSize(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nhIcon(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhIcon(long)"""
        return int.__wrap(__WNDCLASSEX.nhIcon(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.create(int)"""
        return Buffer.__wrap(__WNDCLASSEX.create(__int.valueOf(arg0)))

    @overload
    def lpszMenuName(self, arg0: 'ByteBuffer') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpszMenuName(java.nio.ByteBuffer)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).lpszMenuName(arg0))

    @staticmethod
    @overload
    def nhInstance(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nhInstance(long,long)"""
        __WNDCLASSEX.nhInstance(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def cbClsExtra(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbClsExtra(int)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).cbClsExtra(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nlpszMenuName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.WNDCLASSEX.nlpszMenuName(long)"""
        return ByteBuffer.__wrap(__WNDCLASSEX.nlpszMenuName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbClsExtra(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.ncbClsExtra(long)"""
        return int.__wrap(__WNDCLASSEX.ncbClsExtra(__long.valueOf(arg0)))

    @overload
    def lpszMenuNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX.lpszMenuNameString()"""
        return str.__wrap(super(WNDCLASSEX, self).lpszMenuNameString())

    @staticmethod
    @overload
    def nhbrBackground(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WNDCLASSEX.nhbrBackground(long)"""
        return int.__wrap(__WNDCLASSEX.nhbrBackground(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.callocStack(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.callocStack(arg0))

    @overload
    def lpfnWndProc(self) -> 'WindowProc':
        """public org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WNDCLASSEX.lpfnWndProc()"""
        return 'WindowProc'.__wrap(super(WNDCLASSEX, self).lpfnWndProc())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def hIcon(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hIcon()"""
        return int.__wrap(super(WNDCLASSEX, self).hIcon())

    @overload
    def lpszClassNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WNDCLASSEX.lpszClassNameString()"""
        return str.__wrap(super(WNDCLASSEX, self).lpszClassNameString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nstyle(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.WNDCLASSEX.nstyle(long)"""
        return int.__wrap(__WNDCLASSEX.nstyle(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.WNDCLASSEX$Buffer org.lwjgl.system.windows.WNDCLASSEX.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__WNDCLASSEX.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nlpszClassNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WNDCLASSEX.nlpszClassNameString(long)"""
        return str.__wrap(__WNDCLASSEX.nlpszClassNameString(__long.valueOf(arg0)))

    @overload
    def cbWndExtra(self, arg0: int) -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.cbWndExtra(int)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).cbWndExtra(__int.valueOf(arg0)))

    @overload
    def hCursor(self) -> int:
        """public long org.lwjgl.system.windows.WNDCLASSEX.hCursor()"""
        return int.__wrap(super(WNDCLASSEX, self).hCursor())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.calloc(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.calloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'WNDCLASSEX':
        """public static org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.mallocStack(org.lwjgl.system.MemoryStack)"""
        return WNDCLASSEX.__wrap(__WNDCLASSEX.mallocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def lpfnWndProc(self, arg0: 'WindowProcI') -> 'WNDCLASSEX':
        """public org.lwjgl.system.windows.WNDCLASSEX org.lwjgl.system.windows.WNDCLASSEX.lpfnWndProc(org.lwjgl.system.windows.WindowProcI)"""
        return 'WNDCLASSEX'.__wrap(super(__WNDCLASSEX, self).lpfnWndProc(arg0))

    @staticmethod
    @overload
    def nlpfnWndProc(arg0: int, arg1: 'WindowProcI'):
        """public static void org.lwjgl.system.windows.WNDCLASSEX.nlpfnWndProc(long,org.lwjgl.system.windows.WindowProcI)"""
        __WNDCLASSEX.nlpfnWndProc(__long.valueOf(arg0), arg1) 
 
 
# CLASS: org.lwjgl.system.windows.MSG
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.MSG as __MSG_Buffer
__Buffer = __MSG_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.system.windows.MSG as __MSG
__MSG = __MSG
import org.lwjgl.system.windows.POINT as __POINT
__POINT = __POINT
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class MSG():
    """org.lwjgl.system.windows.MSG"""
 
    @staticmethod
    def __wrap(java_value: __MSG) -> 'MSG':
        return MSG(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MSG):
        """
        Dynamic initializer for MSG.
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
    def message(self) -> int:
        """public int org.lwjgl.system.windows.MSG.message()"""
        return int.__wrap(super(MSG, self).message())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.callocStack(org.lwjgl.system.MemoryStack)"""
        return MSG.__wrap(__MSG.callocStack(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MSG.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MSG.malloc(__int.valueOf(arg0), arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def message(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.message(int)"""
        return 'MSG'.__wrap(super(__MSG, self).message(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nlParam(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nlParam(long,long)"""
        __MSG.nlParam(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nhwnd(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nhwnd(long)"""
        return int.__wrap(__MSG.nhwnd(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def lParam(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.lParam(long)"""
        return 'MSG'.__wrap(super(__MSG, self).lParam(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MSG.ntime(long)"""
        return int.__wrap(__MSG.ntime(__long.valueOf(arg0)))

    @overload
    def pt(self) -> 'POINT':
        """public org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG.pt()"""
        return 'POINT'.__wrap(super(MSG, self).pt())

    @overload
    def hwnd(self) -> int:
        """public long org.lwjgl.system.windows.MSG.hwnd()"""
        return int.__wrap(super(MSG, self).hwnd())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MSG.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nwParam(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nwParam(long,long)"""
        __MSG.nwParam(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: 'POINT') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.set(long,int,long,long,int,org.lwjgl.system.windows.POINT)"""
        return 'MSG'.__wrap(super(__MSG, self).set(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __int.valueOf(arg4), arg5))

    @overload
    def hwnd(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.hwnd(long)"""
        return 'MSG'.__wrap(super(__MSG, self).hwnd(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.malloc(int)"""
        return Buffer.__wrap(__MSG.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.calloc(org.lwjgl.system.MemoryStack)"""
        return MSG.__wrap(__MSG.calloc(arg0))

    @overload
    def set(self, arg0: 'MSG') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.set(org.lwjgl.system.windows.MSG)"""
        return 'MSG'.__wrap(super(__MSG, self).set(arg0))

    @staticmethod
    @overload
    def nhwnd(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nhwnd(long,long)"""
        __MSG.nhwnd(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MSG(java.nio.ByteBuffer)"""
        val = __MSG(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.callocStack(int)"""
        return Buffer.__wrap(__MSG.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.create()"""
        return MSG.__wrap(__MSG.create())

    @staticmethod
    @overload
    def npt(arg0: int, arg1: 'POINT'):
        """public static void org.lwjgl.system.windows.MSG.npt(long,org.lwjgl.system.windows.POINT)"""
        __MSG.npt(__long.valueOf(arg0), arg1)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.createSafe(long)"""
        return MSG.__wrap(__MSG.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.callocStack()"""
        return MSG.__wrap(__MSG.callocStack())

    @staticmethod
    @overload
    def npt(arg0: int) -> 'POINT':
        """public static org.lwjgl.system.windows.POINT org.lwjgl.system.windows.MSG.npt(long)"""
        return POINT.__wrap(__MSG.npt(__long.valueOf(arg0)))

    @overload
    def wParam(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.wParam(long)"""
        return 'MSG'.__wrap(super(__MSG, self).wParam(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__MSG.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.create(long,int)"""
        return Buffer.__wrap(__MSG.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.malloc()"""
        return MSG.__wrap(__MSG.malloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.mallocStack(int)"""
        return Buffer.__wrap(__MSG.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nwParam(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nwParam(long)"""
        return int.__wrap(__MSG.nwParam(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.create(long)"""
        return MSG.__wrap(__MSG.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.createSafe(long,int)"""
        return Buffer.__wrap(__MSG.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def wParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG.wParam()"""
        return int.__wrap(super(MSG, self).wParam())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.MSG.sizeof()"""
        return int.__wrap(super(MSG, self).sizeof())

    @staticmethod
    @overload
    def mallocStack() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.mallocStack()"""
        return MSG.__wrap(__MSG.mallocStack())

    @overload
    def time(self, arg0: int) -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.time(int)"""
        return 'MSG'.__wrap(super(__MSG, self).time(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.mallocStack(org.lwjgl.system.MemoryStack)"""
        return MSG.__wrap(__MSG.mallocStack(arg0))

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.ntime(long,int)"""
        __MSG.ntime(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.malloc(org.lwjgl.system.MemoryStack)"""
        return MSG.__wrap(__MSG.malloc(arg0))

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MSG.time()"""
        return int.__wrap(super(MSG, self).time())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nmessage(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.MSG.nmessage(long,int)"""
        __MSG.nmessage(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def lParam(self) -> int:
        """public long org.lwjgl.system.windows.MSG.lParam()"""
        return int.__wrap(super(MSG, self).lParam())

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
    def pt(self, arg0: 'Consumer') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.pt(java.util.function.Consumer<org.lwjgl.system.windows.POINT>)"""
        return 'MSG'.__wrap(super(__MSG, self).pt(arg0))

    @overload
    def pt(self, arg0: 'POINT') -> 'MSG':
        """public org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.pt(org.lwjgl.system.windows.POINT)"""
        return 'MSG'.__wrap(super(__MSG, self).pt(arg0))

    @staticmethod
    @overload
    def nlParam(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.MSG.nlParam(long)"""
        return int.__wrap(__MSG.nlParam(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.create(int)"""
        return Buffer.__wrap(__MSG.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.MSG$Buffer org.lwjgl.system.windows.MSG.calloc(int)"""
        return Buffer.__wrap(__MSG.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'MSG':
        """public static org.lwjgl.system.windows.MSG org.lwjgl.system.windows.MSG.calloc()"""
        return MSG.__wrap(__MSG.calloc())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nmessage(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.MSG.nmessage(long)"""
        return int.__wrap(__MSG.nmessage(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.Kernel32
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.windows.Kernel32 as __Kernel32
__Kernel32 = __Kernel32
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
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
 
class Kernel32():
    """org.lwjgl.system.windows.Kernel32"""
 
    @staticmethod
    def __wrap(java_value: __Kernel32) -> 'Kernel32':
        return Kernel32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Kernel32):
        """
        Dynamic initializer for Kernel32.
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
    def GetCurrentThread() -> int:
        """public static long org.lwjgl.system.windows.Kernel32.GetCurrentThread()"""
        return int.__wrap(__Kernel32.GetCurrentThread())

    @staticmethod
    @overload
    def GetCurrentThreadId() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentThreadId()"""
        return int.__wrap(__Kernel32.GetCurrentThreadId())

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.windows.Kernel32.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__Kernel32.getLibrary())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetThreadId(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetThreadId(long)"""
        return int.__wrap(__Kernel32.GetThreadId(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def GetProcessId(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetProcessId(long)"""
        return int.__wrap(__Kernel32.GetProcessId(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetCurrentProcessorNumber() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentProcessorNumber()"""
        return int.__wrap(__Kernel32.GetCurrentProcessorNumber())

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

    @staticmethod
    @overload
    def GetCurrentProcess() -> int:
        """public static long org.lwjgl.system.windows.Kernel32.GetCurrentProcess()"""
        return int.__wrap(__Kernel32.GetCurrentProcess())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def GetCurrentProcessId() -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetCurrentProcessId()"""
        return int.__wrap(__Kernel32.GetCurrentProcessId())

    @staticmethod
    @overload
    def GetProcessIdOfThread(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.Kernel32.GetProcessIdOfThread(long)"""
        return int.__wrap(__Kernel32.GetProcessIdOfThread(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.INPUT$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.windows.INPUT as __INPUT_Buffer
__Buffer = __INPUT_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import org.lwjgl.system.windows.MOUSEINPUT as __MOUSEINPUT
__MOUSEINPUT = __MOUSEINPUT
import org.lwjgl.system.windows.KEYBDINPUT as __KEYBDINPUT
__KEYBDINPUT = __KEYBDINPUT
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import org.lwjgl.system.windows.HARDWAREINPUT as __HARDWAREINPUT
__HARDWAREINPUT = __HARDWAREINPUT
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.INPUT.Buffer"""
 
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

    @overload
    def type(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.type(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).type(__int.valueOf(arg0)))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'KEYBDINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_ki(arg0))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.INPUT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def DUMMYUNIONNAME_ki(self) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki()"""
        return 'KEYBDINPUT'.__wrap(super(Buffer, self).DUMMYUNIONNAME_ki())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi(java.util.function.Consumer<org.lwjgl.system.windows.HARDWAREINPUT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_hi(arg0))

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
    def DUMMYUNIONNAME_mi(self) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi()"""
        return 'MOUSEINPUT'.__wrap(super(Buffer, self).DUMMYUNIONNAME_mi())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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
    def DUMMYUNIONNAME_mi(self, arg0: 'MOUSEINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_mi(arg0))

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'HARDWAREINPUT') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_hi(arg0))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.INPUT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_ki(java.util.function.Consumer<org.lwjgl.system.windows.KEYBDINPUT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_ki(arg0))

    @overload
    def DUMMYUNIONNAME_hi(self) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_hi()"""
        return 'HARDWAREINPUT'.__wrap(super(Buffer, self).DUMMYUNIONNAME_hi())

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

    @overload
    def type(self) -> int:
        """public int org.lwjgl.system.windows.INPUT$Buffer.type()"""
        return int.__wrap(super(Buffer, self).type())

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
    def DUMMYUNIONNAME_mi(self, arg0: 'Consumer') -> 'Buffer':
        """public org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT$Buffer.DUMMYUNIONNAME_mi(java.util.function.Consumer<org.lwjgl.system.windows.MOUSEINPUT>)"""
        return 'Buffer'.__wrap(super(__Buffer, self).DUMMYUNIONNAME_mi(arg0))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT as __CRYPTPROTECT_PROMPTSTRUCT
__CRYPTPROTECT_PROMPTSTRUCT = __CRYPTPROTECT_PROMPTSTRUCT
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
 
class CRYPTPROTECT_PROMPTSTRUCT():
    """org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT"""
 
    @staticmethod
    def __wrap(java_value: __CRYPTPROTECT_PROMPTSTRUCT) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        return CRYPTPROTECT_PROMPTSTRUCT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CRYPTPROTECT_PROMPTSTRUCT):
        """
        Dynamic initializer for CRYPTPROTECT_PROMPTSTRUCT.
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
    def nszPrompt(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(long)"""
        return ByteBuffer.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.calloc(org.lwjgl.system.MemoryStack)"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.calloc(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nszPromptString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPromptString(long)"""
        return str.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.nszPromptString(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.sizeof()"""
        return int.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).sizeof())

    @overload
    def dwPromptFlags(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.dwPromptFlags(int)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).dwPromptFlags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.calloc()"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT(java.nio.ByteBuffer)"""
        val = __CRYPTPROTECT_PROMPTSTRUCT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def createSafe(arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.createSafe(long)"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.createSafe(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.set(int,int,long,java.nio.ByteBuffer)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), arg3))

    @overload
    def cbSize$Default(self) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize$Default()"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).cbSize$Default())

    @staticmethod
    @overload
    def ncbSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ncbSize(long,int)"""
        __CRYPTPROTECT_PROMPTSTRUCT.ncbSize(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.create()"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize()"""
        return int.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).cbSize())

    @overload
    def dwPromptFlags(self) -> int:
        """public int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.dwPromptFlags()"""
        return int.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).dwPromptFlags())

    @overload
    def szPrompt(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPrompt()"""
        return 'ByteBuffer'.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).szPrompt())

    @overload
    def set(self, arg0: 'CRYPTPROTECT_PROMPTSTRUCT') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.set(org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).set(arg0))

    @overload
    def szPrompt(self, arg0: 'ByteBuffer') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPrompt(java.nio.ByteBuffer)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).szPrompt(arg0))

    @overload
    def hwndApp(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.hwndApp(long)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).hwndApp(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncbSize(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ncbSize(long)"""
        return int.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.ncbSize(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def szPromptString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.szPromptString()"""
        return str.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).szPromptString())

    @staticmethod
    @overload
    def nszPrompt(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(long,java.nio.ByteBuffer)"""
        __CRYPTPROTECT_PROMPTSTRUCT.nszPrompt(__long.valueOf(arg0), arg1)

    @overload
    def hwndApp(self) -> int:
        """public long org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.hwndApp()"""
        return int.__wrap(super(CRYPTPROTECT_PROMPTSTRUCT, self).hwndApp())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def ndwPromptFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(long)"""
        return int.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.malloc(org.lwjgl.system.MemoryStack)"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.malloc(arg0))

    @staticmethod
    @overload
    def ndwPromptFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(long,int)"""
        __CRYPTPROTECT_PROMPTSTRUCT.ndwPromptFlags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nhwndApp(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(long,long)"""
        __CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.validate(long)"""
        __CRYPTPROTECT_PROMPTSTRUCT.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nhwndApp(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(long)"""
        return int.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.nhwndApp(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.create(long)"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.create(__long.valueOf(arg0)))

    @overload
    def cbSize(self, arg0: int) -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.cbSize(int)"""
        return 'CRYPTPROTECT_PROMPTSTRUCT'.__wrap(super(__CRYPTPROTECT_PROMPTSTRUCT, self).cbSize(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'CRYPTPROTECT_PROMPTSTRUCT':
        """public static org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT org.lwjgl.system.windows.CRYPTPROTECT_PROMPTSTRUCT.malloc()"""
        return CRYPTPROTECT_PROMPTSTRUCT.__wrap(__CRYPTPROTECT_PROMPTSTRUCT.malloc()) 
 
 
# CLASS: org.lwjgl.system.windows.KEYBDINPUT
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.windows.KEYBDINPUT as __KEYBDINPUT
__KEYBDINPUT = __KEYBDINPUT
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.system.windows.KEYBDINPUT as __KEYBDINPUT_Buffer
__Buffer = __KEYBDINPUT_Buffer.Buffer
from builtins import bool
from builtins import int
 
class KEYBDINPUT():
    """org.lwjgl.system.windows.KEYBDINPUT"""
 
    @staticmethod
    def __wrap(java_value: __KEYBDINPUT) -> 'KEYBDINPUT':
        return KEYBDINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KEYBDINPUT):
        """
        Dynamic initializer for KEYBDINPUT.
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
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.calloc(int)"""
        return Buffer.__wrap(__KEYBDINPUT.calloc(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.set(short,short,int,int,long)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).set(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.create(int)"""
        return Buffer.__wrap(__KEYBDINPUT.create(__int.valueOf(arg0)))

    @overload
    def wScan(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT.wScan()"""
        return int.__wrap(super(KEYBDINPUT, self).wScan())

    @overload
    def dwExtraInfo(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.dwExtraInfo(long)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).dwExtraInfo(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.malloc(int)"""
        return Buffer.__wrap(__KEYBDINPUT.malloc(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.KEYBDINPUT(java.nio.ByteBuffer)"""
        val = __KEYBDINPUT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.time()"""
        return int.__wrap(super(KEYBDINPUT, self).time())

    @staticmethod
    @overload
    def ntime(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ntime(long,int)"""
        __KEYBDINPUT.ntime(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nwVk(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.nwVk(long,short)"""
        __KEYBDINPUT.nwVk(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.create(long,int)"""
        return Buffer.__wrap(__KEYBDINPUT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.mallocStack()"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.mallocStack())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.create()"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.KEYBDINPUT.dwExtraInfo()"""
        return int.__wrap(super(KEYBDINPUT, self).dwExtraInfo())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ndwFlags(long,int)"""
        __KEYBDINPUT.ndwFlags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.createSafe(long)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__KEYBDINPUT.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'KEYBDINPUT') -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.set(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).set(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.calloc(arg0))

    @overload
    def wVk(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.wVk(short)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).wVk(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.callocStack(int)"""
        return Buffer.__wrap(__KEYBDINPUT.callocStack(__int.valueOf(arg0)))

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
    def wScan(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.wScan(short)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).wScan(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.createSafe(long,int)"""
        return Buffer.__wrap(__KEYBDINPUT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.create(long)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.callocStack(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.sizeof()"""
        return int.__wrap(super(KEYBDINPUT, self).sizeof())

    @overload
    def time(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.time(int)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).time(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__KEYBDINPUT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.ndwExtraInfo(long,long)"""
        __KEYBDINPUT.ndwExtraInfo(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def nwScan(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.KEYBDINPUT.nwScan(long,short)"""
        __KEYBDINPUT.nwScan(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def wVk(self) -> int:
        """public short org.lwjgl.system.windows.KEYBDINPUT.wVk()"""
        return int.__wrap(super(KEYBDINPUT, self).wVk())

    @staticmethod
    @overload
    def callocStack() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.callocStack()"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.callocStack())

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.KEYBDINPUT.ndwFlags(long)"""
        return int.__wrap(__KEYBDINPUT.ndwFlags(__long.valueOf(arg0)))

    @overload
    def dwFlags(self, arg0: int) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.dwFlags(int)"""
        return 'KEYBDINPUT'.__wrap(super(__KEYBDINPUT, self).dwFlags(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.mallocStack(int)"""
        return Buffer.__wrap(__KEYBDINPUT.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__KEYBDINPUT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.KEYBDINPUT.ndwExtraInfo(long)"""
        return int.__wrap(__KEYBDINPUT.ndwExtraInfo(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.calloc()"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.KEYBDINPUT$Buffer org.lwjgl.system.windows.KEYBDINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__KEYBDINPUT.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

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
    def malloc() -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.malloc()"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.malloc())

    @staticmethod
    @overload
    def nwScan(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.KEYBDINPUT.nwScan(long)"""
        return int.__wrap(__KEYBDINPUT.nwScan(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.KEYBDINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return KEYBDINPUT.__wrap(__KEYBDINPUT.malloc(arg0))

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.KEYBDINPUT.dwFlags()"""
        return int.__wrap(super(KEYBDINPUT, self).dwFlags())

    @staticmethod
    @overload
    def ntime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.KEYBDINPUT.ntime(long)"""
        return int.__wrap(__KEYBDINPUT.ntime(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nwVk(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.KEYBDINPUT.nwVk(long)"""
        return int.__wrap(__KEYBDINPUT.nwVk(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.RECT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import org.lwjgl.system.windows.RECT as __RECT_Buffer
__Buffer = __RECT_Buffer.Buffer
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.RECT.Buffer"""
 
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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def left(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.left()"""
        return int.__wrap(super(Buffer, self).left())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def right(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.right()"""
        return int.__wrap(super(Buffer, self).right())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.RECT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def top(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.top(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).top(__int.valueOf(arg0)))

    @overload
    def bottom(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.bottom(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bottom(__int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.RECT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def bottom(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.bottom()"""
        return int.__wrap(super(Buffer, self).bottom())

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

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def right(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.right(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).right(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def top(self) -> int:
        """public int org.lwjgl.system.windows.RECT$Buffer.top()"""
        return int.__wrap(super(Buffer, self).top())

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

    @overload
    def left(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT$Buffer.left(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).left(__int.valueOf(arg0)))

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.POINTL$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.POINTL as __POINTL_Buffer
__Buffer = __POINTL_Buffer.Buffer
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.POINTL.Buffer"""
 
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
 
    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINTL$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def x(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL$Buffer.x(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x(__int.valueOf(arg0)))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINTL$Buffer.x()"""
        return int.__wrap(super(Buffer, self).x())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.POINTL$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINTL$Buffer.y()"""
        return int.__wrap(super(Buffer, self).y())

    @overload
    def y(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL$Buffer.y(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y(__int.valueOf(arg0)))

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.TOUCHINPUT
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.TOUCHINPUT as __TOUCHINPUT
__TOUCHINPUT = __TOUCHINPUT
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import org.lwjgl.system.windows.TOUCHINPUT as __TOUCHINPUT_Buffer
__Buffer = __TOUCHINPUT_Buffer.Buffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class TOUCHINPUT():
    """org.lwjgl.system.windows.TOUCHINPUT"""
 
    @staticmethod
    def __wrap(java_value: __TOUCHINPUT) -> 'TOUCHINPUT':
        return TOUCHINPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TOUCHINPUT):
        """
        Dynamic initializer for TOUCHINPUT.
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.TOUCHINPUT(java.nio.ByteBuffer)"""
        val = __TOUCHINPUT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT.dwExtraInfo()"""
        return int.__wrap(super(TOUCHINPUT, self).dwExtraInfo())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__TOUCHINPUT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwFlags(long)"""
        return int.__wrap(__TOUCHINPUT.ndwFlags(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.createSafe(long)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.calloc(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.calloc()"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.calloc())

    @staticmethod
    @overload
    def ndwTime(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwTime(long)"""
        return int.__wrap(__TOUCHINPUT.ndwTime(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.createSafe(long,int)"""
        return Buffer.__wrap(__TOUCHINPUT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ncxContact(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ncxContact(long)"""
        return int.__wrap(__TOUCHINPUT.ncxContact(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.mallocStack()"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.mallocStack())

    @staticmethod
    @overload
    def ndwMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwMask(long)"""
        return int.__wrap(__TOUCHINPUT.ndwMask(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.sizeof()"""
        return int.__wrap(super(TOUCHINPUT, self).sizeof())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.create(long,int)"""
        return Buffer.__wrap(__TOUCHINPUT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__TOUCHINPUT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.callocStack()"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.callocStack())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwID(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwID()"""
        return int.__wrap(super(TOUCHINPUT, self).dwID())

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.x()"""
        return int.__wrap(super(TOUCHINPUT, self).x())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def hSource(self) -> int:
        """public long org.lwjgl.system.windows.TOUCHINPUT.hSource()"""
        return int.__wrap(super(TOUCHINPUT, self).hSource())

    @staticmethod
    @overload
    def malloc() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.malloc()"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.malloc())

    @staticmethod
    @overload
    def ndwID(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ndwID(long)"""
        return int.__wrap(__TOUCHINPUT.ndwID(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.callocStack(int)"""
        return Buffer.__wrap(__TOUCHINPUT.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.create(int)"""
        return Buffer.__wrap(__TOUCHINPUT.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.create(long)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.create(__long.valueOf(arg0)))

    @overload
    def y(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.y()"""
        return int.__wrap(super(TOUCHINPUT, self).y())

    @staticmethod
    @overload
    def nhSource(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.TOUCHINPUT.nhSource(long)"""
        return int.__wrap(__TOUCHINPUT.nhSource(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.calloc(int)"""
        return Buffer.__wrap(__TOUCHINPUT.calloc(__int.valueOf(arg0)))

    @overload
    def dwMask(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwMask()"""
        return int.__wrap(super(TOUCHINPUT, self).dwMask())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__TOUCHINPUT.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ny(long)"""
        return int.__wrap(__TOUCHINPUT.ny(__long.valueOf(arg0)))

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwFlags()"""
        return int.__wrap(super(TOUCHINPUT, self).dwFlags())

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.nx(long)"""
        return int.__wrap(__TOUCHINPUT.nx(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create() -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.create()"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.create())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def cyContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.cyContact()"""
        return int.__wrap(super(TOUCHINPUT, self).cyContact())

    @staticmethod
    @overload
    def ndwExtraInfo(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.TOUCHINPUT.ndwExtraInfo(long)"""
        return int.__wrap(__TOUCHINPUT.ndwExtraInfo(__long.valueOf(arg0)))

    @overload
    def cxContact(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.cxContact()"""
        return int.__wrap(super(TOUCHINPUT, self).cxContact())

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
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.mallocStack(int)"""
        return Buffer.__wrap(__TOUCHINPUT.mallocStack(__int.valueOf(arg0)))

    @overload
    def dwTime(self) -> int:
        """public int org.lwjgl.system.windows.TOUCHINPUT.dwTime()"""
        return int.__wrap(super(TOUCHINPUT, self).dwTime())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.malloc(int)"""
        return Buffer.__wrap(__TOUCHINPUT.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.callocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.TOUCHINPUT$Buffer org.lwjgl.system.windows.TOUCHINPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__TOUCHINPUT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'TOUCHINPUT':
        """public static org.lwjgl.system.windows.TOUCHINPUT org.lwjgl.system.windows.TOUCHINPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return TOUCHINPUT.__wrap(__TOUCHINPUT.mallocStack(arg0))

    @staticmethod
    @overload
    def ncyContact(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.TOUCHINPUT.ncyContact(long)"""
        return int.__wrap(__TOUCHINPUT.ncyContact(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.Crypt32$Functions
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
import org.lwjgl.system.windows.Crypt32 as __Crypt32_Functions
__Functions = __Crypt32_Functions.Functions
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.system.windows.Crypt32.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
 
 
# CLASS: org.lwjgl.system.windows.WindowProc
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
import org.lwjgl.system.windows.WindowProcI as __WindowProcI
__WindowProcI = __WindowProcI
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.WindowProc as __WindowProc
__WindowProc = __WindowProc
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
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
 
class WindowProc(ABC):
    """org.lwjgl.system.windows.WindowProc"""
 
    @staticmethod
    def __wrap(java_value: __WindowProc) -> 'WindowProc':
        return WindowProc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowProc):
        """
        Dynamic initializer for WindowProc.
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
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.windows.WindowProcI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(WindowProcI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.createSafe(long)"""
        return WindowProc.__wrap(__WindowProc.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.create(long)"""
        return WindowProc.__wrap(__WindowProc.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.windows.WindowProcI.callback(long,long)"""
        super(__WindowProcI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.windows.WindowProcI.invoke(long,int,long,long)"""
        pass

    @staticmethod
    @overload
    def create(arg0: 'WindowProcI') -> 'WindowProc':
        """public static org.lwjgl.system.windows.WindowProc org.lwjgl.system.windows.WindowProc.create(org.lwjgl.system.windows.WindowProcI)"""
        return WindowProc.__wrap(__WindowProc.create(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.system.windows.MOUSEINPUT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.MOUSEINPUT as __MOUSEINPUT_Buffer
__Buffer = __MOUSEINPUT_Buffer.Buffer
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.MOUSEINPUT.Buffer"""
 
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
    def time(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.time(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).time(__int.valueOf(arg0)))

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

    @overload
    def dy(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dy(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dy(__int.valueOf(arg0)))

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
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwFlags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwFlags(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def mouseData(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.mouseData()"""
        return int.__wrap(super(Buffer, self).mouseData())

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
    def dy(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dy()"""
        return int.__wrap(super(Buffer, self).dy())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwFlags()"""
        return int.__wrap(super(Buffer, self).dwFlags())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def dx(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dx(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dx(__int.valueOf(arg0)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def mouseData(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.mouseData(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).mouseData(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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
    def dx(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.dx()"""
        return int.__wrap(super(Buffer, self).dx())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dwExtraInfo(self) -> int:
        """public long org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwExtraInfo()"""
        return int.__wrap(super(Buffer, self).dwExtraInfo())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def dwExtraInfo(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer org.lwjgl.system.windows.MOUSEINPUT$Buffer.dwExtraInfo(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwExtraInfo(__long.valueOf(arg0)))

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

    @overload
    def time(self) -> int:
        """public int org.lwjgl.system.windows.MOUSEINPUT$Buffer.time()"""
        return int.__wrap(super(Buffer, self).time())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MOUSEINPUT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.INPUT
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.windows.KEYBDINPUT as __KEYBDINPUT
__KEYBDINPUT = __KEYBDINPUT
import org.lwjgl.system.windows.INPUT as __INPUT_Buffer
__Buffer = __INPUT_Buffer.Buffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.INPUT as __INPUT
__INPUT = __INPUT
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.windows.HARDWAREINPUT as __HARDWAREINPUT
__HARDWAREINPUT = __HARDWAREINPUT
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
import org.lwjgl.system.windows.MOUSEINPUT as __MOUSEINPUT
__MOUSEINPUT = __MOUSEINPUT
 
class INPUT():
    """org.lwjgl.system.windows.INPUT"""
 
    @staticmethod
    def __wrap(java_value: __INPUT) -> 'INPUT':
        return INPUT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __INPUT):
        """
        Dynamic initializer for INPUT.
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
    def createSafe(arg0: int) -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.createSafe(long)"""
        return INPUT.__wrap(__INPUT.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.mallocStack(int)"""
        return Buffer.__wrap(__INPUT.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.callocStack(org.lwjgl.system.MemoryStack)"""
        return INPUT.__wrap(__INPUT.callocStack(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_ki(arg0: int, arg1: 'KEYBDINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_ki(long,org.lwjgl.system.windows.KEYBDINPUT)"""
        __INPUT.nDUMMYUNIONNAME_ki(__long.valueOf(arg0), arg1)

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def type(self) -> int:
        """public int org.lwjgl.system.windows.INPUT.type()"""
        return int.__wrap(super(INPUT, self).type())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi(java.util.function.Consumer<org.lwjgl.system.windows.HARDWAREINPUT>)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_hi(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__INPUT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.malloc(int)"""
        return Buffer.__wrap(__INPUT.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.createSafe(long,int)"""
        return Buffer.__wrap(__INPUT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.mallocStack()"""
        return INPUT.__wrap(__INPUT.mallocStack())

    @staticmethod
    @overload
    def ntype(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.INPUT.ntype(long,int)"""
        __INPUT.ntype(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def type(self, arg0: int) -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.type(int)"""
        return 'INPUT'.__wrap(super(__INPUT, self).type(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_mi(arg0: int) -> 'MOUSEINPUT':
        """public static org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_mi(long)"""
        return MOUSEINPUT.__wrap(__INPUT.nDUMMYUNIONNAME_mi(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.INPUT(java.nio.ByteBuffer)"""
        val = __INPUT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int) -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.create(long)"""
        return INPUT.__wrap(__INPUT.create(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.INPUT.sizeof()"""
        return int.__wrap(super(INPUT, self).sizeof())

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
    def DUMMYUNIONNAME_ki(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki(java.util.function.Consumer<org.lwjgl.system.windows.KEYBDINPUT>)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_ki(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__INPUT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.callocStack(int)"""
        return Buffer.__wrap(__INPUT.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_hi(arg0: int) -> 'HARDWAREINPUT':
        """public static org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_hi(long)"""
        return HARDWAREINPUT.__wrap(__INPUT.nDUMMYUNIONNAME_hi(__long.valueOf(arg0)))

    @overload
    def DUMMYUNIONNAME_hi(self, arg0: 'HARDWAREINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi(org.lwjgl.system.windows.HARDWAREINPUT)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_hi(arg0))

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_mi(arg0: int, arg1: 'MOUSEINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_mi(long,org.lwjgl.system.windows.MOUSEINPUT)"""
        __INPUT.nDUMMYUNIONNAME_mi(__long.valueOf(arg0), arg1)

    @overload
    def DUMMYUNIONNAME_mi(self, arg0: 'Consumer') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi(java.util.function.Consumer<org.lwjgl.system.windows.MOUSEINPUT>)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_mi(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.malloc(org.lwjgl.system.MemoryStack)"""
        return INPUT.__wrap(__INPUT.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.calloc()"""
        return INPUT.__wrap(__INPUT.calloc())

    @staticmethod
    @overload
    def callocStack() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.callocStack()"""
        return INPUT.__wrap(__INPUT.callocStack())

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_ki(arg0: int) -> 'KEYBDINPUT':
        """public static org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_ki(long)"""
        return KEYBDINPUT.__wrap(__INPUT.nDUMMYUNIONNAME_ki(__long.valueOf(arg0)))

    @overload
    def DUMMYUNIONNAME_mi(self, arg0: 'MOUSEINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi(org.lwjgl.system.windows.MOUSEINPUT)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_mi(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.create(long,int)"""
        return Buffer.__wrap(__INPUT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ntype(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.INPUT.ntype(long)"""
        return int.__wrap(__INPUT.ntype(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.create()"""
        return INPUT.__wrap(__INPUT.create())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.calloc(int)"""
        return Buffer.__wrap(__INPUT.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.create(int)"""
        return Buffer.__wrap(__INPUT.create(__int.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__INPUT.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.calloc(org.lwjgl.system.MemoryStack)"""
        return INPUT.__wrap(__INPUT.calloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return INPUT.__wrap(__INPUT.mallocStack(arg0))

    @overload
    def DUMMYUNIONNAME_ki(self) -> 'KEYBDINPUT':
        """public org.lwjgl.system.windows.KEYBDINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki()"""
        return 'KEYBDINPUT'.__wrap(super(INPUT, self).DUMMYUNIONNAME_ki())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.INPUT$Buffer org.lwjgl.system.windows.INPUT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__INPUT.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'INPUT':
        """public static org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.malloc()"""
        return INPUT.__wrap(__INPUT.malloc())

    @overload
    def DUMMYUNIONNAME_ki(self, arg0: 'KEYBDINPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_ki(org.lwjgl.system.windows.KEYBDINPUT)"""
        return 'INPUT'.__wrap(super(__INPUT, self).DUMMYUNIONNAME_ki(arg0))

    @overload
    def DUMMYUNIONNAME_mi(self) -> 'MOUSEINPUT':
        """public org.lwjgl.system.windows.MOUSEINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_mi()"""
        return 'MOUSEINPUT'.__wrap(super(INPUT, self).DUMMYUNIONNAME_mi())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nDUMMYUNIONNAME_hi(arg0: int, arg1: 'HARDWAREINPUT'):
        """public static void org.lwjgl.system.windows.INPUT.nDUMMYUNIONNAME_hi(long,org.lwjgl.system.windows.HARDWAREINPUT)"""
        __INPUT.nDUMMYUNIONNAME_hi(__long.valueOf(arg0), arg1)

    @overload
    def DUMMYUNIONNAME_hi(self) -> 'HARDWAREINPUT':
        """public org.lwjgl.system.windows.HARDWAREINPUT org.lwjgl.system.windows.INPUT.DUMMYUNIONNAME_hi()"""
        return 'HARDWAREINPUT'.__wrap(super(INPUT, self).DUMMYUNIONNAME_hi())

    @overload
    def set(self, arg0: 'INPUT') -> 'INPUT':
        """public org.lwjgl.system.windows.INPUT org.lwjgl.system.windows.INPUT.set(org.lwjgl.system.windows.INPUT)"""
        return 'INPUT'.__wrap(super(__INPUT, self).set(arg0)) 
 
 
# CLASS: org.lwjgl.system.windows.Kernel32$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.system.windows.Kernel32 as __Kernel32_Functions
__Functions = __Kernel32_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.system.windows.Kernel32.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
 
 
# CLASS: org.lwjgl.system.windows.HARDWAREINPUT$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import java.lang.Short as __short
from builtins import bool
from builtins import str
import org.lwjgl.system.windows.HARDWAREINPUT as __HARDWAREINPUT_Buffer
__Buffer = __HARDWAREINPUT_Buffer.Buffer
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.HARDWAREINPUT.Buffer"""
 
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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def uMsg(self) -> int:
        """public int org.lwjgl.system.windows.HARDWAREINPUT$Buffer.uMsg()"""
        return int.__wrap(super(Buffer, self).uMsg())

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def wParamL(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamL()"""
        return int.__wrap(super(Buffer, self).wParamL())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def wParamH(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamH(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wParamH(__short.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
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
    def uMsg(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.uMsg(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).uMsg(__int.valueOf(arg0)))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def wParamH(self) -> int:
        """public short org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamH()"""
        return int.__wrap(super(Buffer, self).wParamH())

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

    @overload
    def wParamL(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.HARDWAREINPUT$Buffer org.lwjgl.system.windows.HARDWAREINPUT$Buffer.wParamL(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).wParamL(__short.valueOf(arg0)))

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.WindowsLibrary
from builtins import str
import java.lang.CharSequence as CharSequence
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
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.FunctionProvider as __FunctionProvider
__FunctionProvider = __FunctionProvider
import org.lwjgl.system.SharedLibrary as __SharedLibrary_Default
__Default = __SharedLibrary_Default.Default
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
import org.lwjgl.system.windows.WindowsLibrary as __WindowsLibrary
__WindowsLibrary = __WindowsLibrary
from builtins import bool
from builtins import int
 
class WindowsLibrary():
    """org.lwjgl.system.windows.WindowsLibrary"""
 
    @staticmethod
    def __wrap(java_value: __WindowsLibrary) -> 'WindowsLibrary':
        return WindowsLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WindowsLibrary):
        """
        Dynamic initializer for WindowsLibrary.
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
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.windows.WindowsLibrary.free()"""
        super(WindowsLibrary, self).free()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.windows.WindowsLibrary(java.lang.String,long)"""
        val = __WindowsLibrary(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str.__wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.WindowsLibrary.getPath()"""
        return str.__wrap(super(WindowsLibrary, self).getPath())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

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
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.windows.WindowsLibrary.getFunctionAddress(java.nio.ByteBuffer)"""
        return int.__wrap(super(__WindowsLibrary, self).getFunctionAddress(arg0))

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

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public org.lwjgl.system.windows.WindowsLibrary(java.lang.String)"""
        val = __WindowsLibrary(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
import java.lang.Short as __short
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as __PIXELFORMATDESCRIPTOR_Buffer
__Buffer = __PIXELFORMATDESCRIPTOR_Buffer.Buffer
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.Buffer"""
 
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
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwFlags()"""
        return int.__wrap(super(Buffer, self).dwFlags())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def bReserved(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.bReserved()"""
        return int.__wrap(super(Buffer, self).bReserved())

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

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int.__wrap(super(__pyglsystem.CustomBuffer, self).address(__int.valueOf(arg0)))

    @overload
    def nSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nSize(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nSize(__short.valueOf(arg0)))

    @overload
    def dwDamageMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwDamageMask()"""
        return int.__wrap(super(Buffer, self).dwDamageMask())

    @overload
    def cAlphaBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAlphaBits(__byte.valueOf(arg0)))

    @overload
    def iLayerType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iLayerType()"""
        return int.__wrap(super(Buffer, self).iLayerType())

    @overload
    def cGreenBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cGreenBits(__byte.valueOf(arg0)))

    @overload
    def cAlphaShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaShift(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAlphaShift(__byte.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def cAccumRedBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumRedBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAccumRedBits(__byte.valueOf(arg0)))

    @overload
    def cStencilBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cStencilBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cStencilBits(__byte.valueOf(arg0)))

    @overload
    def nSize(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nSize()"""
        return int.__wrap(super(Buffer, self).nSize())

    @overload
    def cAccumBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBits()"""
        return int.__wrap(super(Buffer, self).cAccumBits())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwFlags(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwFlags(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwFlags(__int.valueOf(arg0)))

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
    def cColorBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cColorBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cColorBits(__byte.valueOf(arg0)))

    @overload
    def dwVisibleMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwVisibleMask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwVisibleMask(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def cRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedBits()"""
        return int.__wrap(super(Buffer, self).cRedBits())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def bReserved(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.bReserved(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bReserved(__byte.valueOf(arg0)))

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).limit(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def cRedShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedShift()"""
        return int.__wrap(super(Buffer, self).cRedShift())

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
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def cAccumGreenBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumGreenBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAccumGreenBits(__byte.valueOf(arg0)))

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def iLayerType(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iLayerType(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).iLayerType(__byte.valueOf(arg0)))

    @overload
    def cAlphaShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaShift()"""
        return int.__wrap(super(Buffer, self).cAlphaShift())

    @overload
    def cAccumAlphaBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumAlphaBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAccumAlphaBits(__byte.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(arg0))

    @overload
    def cDepthBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cDepthBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cDepthBits(__byte.valueOf(arg0)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

    @overload
    def cRedShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedShift(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cRedShift(__byte.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cAccumBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBlueBits()"""
        return int.__wrap(super(Buffer, self).cAccumBlueBits())

    @overload
    def iPixelType(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iPixelType(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).iPixelType(__byte.valueOf(arg0)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'.__wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def dwLayerMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwLayerMask()"""
        return int.__wrap(super(Buffer, self).dwLayerMask())

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
    def cGreenShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenShift(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cGreenShift(__byte.valueOf(arg0)))

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def cBlueShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueShift()"""
        return int.__wrap(super(Buffer, self).cBlueShift())

    @overload
    def cAccumAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumAlphaBits()"""
        return int.__wrap(super(Buffer, self).cAccumAlphaBits())

    @overload
    def cRedBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cRedBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cRedBits(__byte.valueOf(arg0)))

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

    @overload
    def cColorBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cColorBits()"""
        return int.__wrap(super(Buffer, self).cColorBits())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def cStencilBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cStencilBits()"""
        return int.__wrap(super(Buffer, self).cStencilBits())

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
    def cGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenBits()"""
        return int.__wrap(super(Buffer, self).cGreenBits())

    @overload
    def nVersion(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nVersion()"""
        return int.__wrap(super(Buffer, self).nVersion())

    @overload
    def cAuxBuffers(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAuxBuffers(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAuxBuffers(__byte.valueOf(arg0)))

    @overload
    def cBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueBits()"""
        return int.__wrap(super(Buffer, self).cBlueBits())

    @overload
    def cGreenShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cGreenShift()"""
        return int.__wrap(super(Buffer, self).cGreenShift())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def cAccumGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumGreenBits()"""
        return int.__wrap(super(Buffer, self).cAccumGreenBits())

    @overload
    def nVersion(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.nVersion(short)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nVersion(__short.valueOf(arg0)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def cAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAlphaBits()"""
        return int.__wrap(super(Buffer, self).cAlphaBits())

    @overload
    def cBlueShift(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueShift(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cBlueShift(__byte.valueOf(arg0)))

    @overload
    def dwDamageMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwDamageMask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwDamageMask(__int.valueOf(arg0)))

    @overload
    def iPixelType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.iPixelType()"""
        return int.__wrap(super(Buffer, self).iPixelType())

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def cAccumRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumRedBits()"""
        return int.__wrap(super(Buffer, self).cAccumRedBits())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def dwVisibleMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwVisibleMask()"""
        return int.__wrap(super(Buffer, self).dwVisibleMask())

    @overload
    def cDepthBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cDepthBits()"""
        return int.__wrap(super(Buffer, self).cDepthBits())

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).reset())

    @overload
    def cAuxBuffers(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAuxBuffers()"""
        return int.__wrap(super(Buffer, self).cAuxBuffers())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def cBlueBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cBlueBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cBlueBits(__byte.valueOf(arg0)))

    @overload
    def cAccumBlueBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBlueBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAccumBlueBits(__byte.valueOf(arg0)))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def cAccumBits(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.cAccumBits(byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cAccumBits(__byte.valueOf(arg0)))

    @overload
    def dwLayerMask(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer.dwLayerMask(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).dwLayerMask(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.RECT
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.RECT as __RECT
__RECT = __RECT
import org.lwjgl.system.windows.RECT as __RECT_Buffer
__Buffer = __RECT_Buffer.Buffer
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class RECT():
    """org.lwjgl.system.windows.RECT"""
 
    @staticmethod
    def __wrap(java_value: __RECT) -> 'RECT':
        return RECT(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RECT):
        """
        Dynamic initializer for RECT.
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
    def nleft(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nleft(long,int)"""
        __RECT.nleft(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.create(long)"""
        return RECT.__wrap(__RECT.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.create(int)"""
        return Buffer.__wrap(__RECT.create(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.set(int,int,int,int)"""
        return 'RECT'.__wrap(super(__RECT, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def top(self) -> int:
        """public int org.lwjgl.system.windows.RECT.top()"""
        return int.__wrap(super(RECT, self).top())

    @overload
    def right(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.right(int)"""
        return 'RECT'.__wrap(super(__RECT, self).right(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.createSafe(long,int)"""
        return Buffer.__wrap(__RECT.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def right(self) -> int:
        """public int org.lwjgl.system.windows.RECT.right()"""
        return int.__wrap(super(RECT, self).right())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.RECT(java.nio.ByteBuffer)"""
        val = __RECT(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__RECT.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.callocStack(org.lwjgl.system.MemoryStack)"""
        return RECT.__wrap(__RECT.callocStack(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__RECT.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'RECT') -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.set(org.lwjgl.system.windows.RECT)"""
        return 'RECT'.__wrap(super(__RECT, self).set(arg0))

    @overload
    def bottom(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.bottom(int)"""
        return 'RECT'.__wrap(super(__RECT, self).bottom(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.create(long,int)"""
        return Buffer.__wrap(__RECT.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.mallocStack()"""
        return RECT.__wrap(__RECT.mallocStack())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.malloc()"""
        return RECT.__wrap(__RECT.malloc())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nbottom(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nbottom(long)"""
        return int.__wrap(__RECT.nbottom(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def left(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.left(int)"""
        return 'RECT'.__wrap(super(__RECT, self).left(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nleft(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nleft(long)"""
        return int.__wrap(__RECT.nleft(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.calloc()"""
        return RECT.__wrap(__RECT.calloc())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.calloc(org.lwjgl.system.MemoryStack)"""
        return RECT.__wrap(__RECT.calloc(arg0))

    @staticmethod
    @overload
    def nright(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.nright(long)"""
        return int.__wrap(__RECT.nright(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.create()"""
        return RECT.__wrap(__RECT.create())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.malloc(int)"""
        return Buffer.__wrap(__RECT.malloc(__int.valueOf(arg0)))

    @overload
    def bottom(self) -> int:
        """public int org.lwjgl.system.windows.RECT.bottom()"""
        return int.__wrap(super(RECT, self).bottom())

    @staticmethod
    @overload
    def nright(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nright(long,int)"""
        __RECT.nright(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack() -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.callocStack()"""
        return RECT.__wrap(__RECT.callocStack())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__RECT.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__RECT.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.calloc(int)"""
        return Buffer.__wrap(__RECT.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.createSafe(long)"""
        return RECT.__wrap(__RECT.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.RECT.sizeof()"""
        return int.__wrap(super(RECT, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.mallocStack(org.lwjgl.system.MemoryStack)"""
        return RECT.__wrap(__RECT.mallocStack(arg0))

    @overload
    def top(self, arg0: int) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.top(int)"""
        return 'RECT'.__wrap(super(__RECT, self).top(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'RECT':
        """public static org.lwjgl.system.windows.RECT org.lwjgl.system.windows.RECT.malloc(org.lwjgl.system.MemoryStack)"""
        return RECT.__wrap(__RECT.malloc(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.callocStack(int)"""
        return Buffer.__wrap(__RECT.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def left(self) -> int:
        """public int org.lwjgl.system.windows.RECT.left()"""
        return int.__wrap(super(RECT, self).left())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ntop(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.ntop(long,int)"""
        __RECT.ntop(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nbottom(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.RECT.nbottom(long,int)"""
        __RECT.nbottom(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.RECT$Buffer org.lwjgl.system.windows.RECT.mallocStack(int)"""
        return Buffer.__wrap(__RECT.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntop(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.RECT.ntop(long)"""
        return int.__wrap(__RECT.ntop(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.system.windows.DEVMODE
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.POINTL as __POINTL
__POINTL = __POINTL
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.windows.DEVMODE as __DEVMODE_Buffer
__Buffer = __DEVMODE_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import org.lwjgl.system.windows.DEVMODE as __DEVMODE
__DEVMODE = __DEVMODE
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class DEVMODE():
    """org.lwjgl.system.windows.DEVMODE"""
 
    @staticmethod
    def __wrap(java_value: __DEVMODE) -> 'DEVMODE':
        return DEVMODE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DEVMODE):
        """
        Dynamic initializer for DEVMODE.
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
    def ndmDriverExtra(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmDriverExtra(long,short)"""
        __DEVMODE.ndmDriverExtra(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def ndmPrintQuality(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPrintQuality(long)"""
        return int.__wrap(__DEVMODE.ndmPrintQuality(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmOrientation(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmOrientation(long)"""
        return int.__wrap(__DEVMODE.ndmOrientation(__long.valueOf(arg0)))

    @overload
    def dmPelsHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPelsHeight()"""
        return int.__wrap(super(DEVMODE, self).dmPelsHeight())

    @staticmethod
    @overload
    def malloc() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.malloc()"""
        return DEVMODE.__wrap(__DEVMODE.malloc())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def dmReserved1(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmReserved1()"""
        return int.__wrap(super(DEVMODE, self).dmReserved1())

    @staticmethod
    @overload
    def ndmDuplex(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDuplex(long)"""
        return int.__wrap(__DEVMODE.ndmDuplex(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmPaperWidth(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperWidth(long)"""
        return int.__wrap(__DEVMODE.ndmPaperWidth(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmReserved1(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmReserved1(long)"""
        return int.__wrap(__DEVMODE.ndmReserved1(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.mallocStack()"""
        return DEVMODE.__wrap(__DEVMODE.mallocStack())

    @staticmethod
    @overload
    def ndmPelsHeight(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPelsHeight(long)"""
        return int.__wrap(__DEVMODE.ndmPelsHeight(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def dmICMIntent(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmICMIntent()"""
        return int.__wrap(super(DEVMODE, self).dmICMIntent())

    @overload
    def dmPrintQuality(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPrintQuality()"""
        return int.__wrap(super(DEVMODE, self).dmPrintQuality())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.createSafe(long)"""
        return DEVMODE.__wrap(__DEVMODE.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DEVMODE.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.calloc(int)"""
        return Buffer.__wrap(__DEVMODE.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.callocStack()"""
        return DEVMODE.__wrap(__DEVMODE.callocStack())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.malloc(int)"""
        return Buffer.__wrap(__DEVMODE.malloc(__int.valueOf(arg0)))

    @overload
    def dmSpecVersion(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmSpecVersion(short)"""
        return 'DEVMODE'.__wrap(super(__DEVMODE, self).dmSpecVersion(__short.valueOf(arg0)))

    @overload
    def dmPelsWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPelsWidth()"""
        return int.__wrap(super(DEVMODE, self).dmPelsWidth())

    @staticmethod
    @overload
    def ndmLogPixels(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmLogPixels(long)"""
        return int.__wrap(__DEVMODE.ndmLogPixels(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def ndmFields(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmFields(long)"""
        return int.__wrap(__DEVMODE.ndmFields(__long.valueOf(arg0)))

    @overload
    def dmDeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE.dmDeviceNameString()"""
        return str.__wrap(super(DEVMODE, self).dmDeviceNameString())

    @overload
    def dmDriverExtra(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDriverExtra()"""
        return int.__wrap(super(DEVMODE, self).dmDriverExtra())

    @overload
    def dmPaperSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperSize()"""
        return int.__wrap(super(DEVMODE, self).dmPaperSize())

    @staticmethod
    @overload
    def ndmPanningHeight(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPanningHeight(long)"""
        return int.__wrap(__DEVMODE.ndmPanningHeight(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.callocStack(org.lwjgl.system.MemoryStack)"""
        return DEVMODE.__wrap(__DEVMODE.callocStack(arg0))

    @overload
    def dmDisplayOrientation(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayOrientation()"""
        return int.__wrap(super(DEVMODE, self).dmDisplayOrientation())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.mallocStack(org.lwjgl.system.MemoryStack)"""
        return DEVMODE.__wrap(__DEVMODE.mallocStack(arg0))

    @overload
    def dmColor(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmColor()"""
        return int.__wrap(super(DEVMODE, self).dmColor())

    @staticmethod
    @overload
    def ndmSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmSize(long)"""
        return int.__wrap(__DEVMODE.ndmSize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmCollate(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmCollate(long)"""
        return int.__wrap(__DEVMODE.ndmCollate(__long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.create(long)"""
        return DEVMODE.__wrap(__DEVMODE.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmSpecVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmSpecVersion(long)"""
        return int.__wrap(__DEVMODE.ndmSpecVersion(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def dmPaperWidth(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperWidth()"""
        return int.__wrap(super(DEVMODE, self).dmPaperWidth())

    @staticmethod
    @overload
    def ndmDitherType(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDitherType(long)"""
        return int.__wrap(__DEVMODE.ndmDitherType(__long.valueOf(arg0)))

    @overload
    def dmBitsPerPel(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmBitsPerPel()"""
        return int.__wrap(super(DEVMODE, self).dmBitsPerPel())

    @staticmethod
    @overload
    def ndmDefaultSource(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDefaultSource(long)"""
        return int.__wrap(__DEVMODE.ndmDefaultSource(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmFormName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.ndmFormName(long)"""
        return ByteBuffer.__wrap(__DEVMODE.ndmFormName(__long.valueOf(arg0)))

    @overload
    def dmSpecVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmSpecVersion()"""
        return int.__wrap(super(DEVMODE, self).dmSpecVersion())

    @staticmethod
    @overload
    def ndmScale(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmScale(long)"""
        return int.__wrap(__DEVMODE.ndmScale(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmICMIntent(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmICMIntent(long)"""
        return int.__wrap(__DEVMODE.ndmICMIntent(__long.valueOf(arg0)))

    @overload
    def dmDitherType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDitherType()"""
        return int.__wrap(super(DEVMODE, self).dmDitherType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.create(int)"""
        return Buffer.__wrap(__DEVMODE.create(__int.valueOf(arg0)))

    @overload
    def dmCopies(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmCopies()"""
        return int.__wrap(super(DEVMODE, self).dmCopies())

    @overload
    def dmDriverExtra(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmDriverExtra(short)"""
        return 'DEVMODE'.__wrap(super(__DEVMODE, self).dmDriverExtra(__short.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def dmFormNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DEVMODE.dmFormNameString()"""
        return str.__wrap(super(DEVMODE, self).dmFormNameString())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DEVMODE.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndmMediaType(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmMediaType(long)"""
        return int.__wrap(__DEVMODE.ndmMediaType(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDriverExtra(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDriverExtra(long)"""
        return int.__wrap(__DEVMODE.ndmDriverExtra(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDriverVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmDriverVersion(long)"""
        return int.__wrap(__DEVMODE.ndmDriverVersion(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def dmSize(self, arg0: int) -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.dmSize(short)"""
        return 'DEVMODE'.__wrap(super(__DEVMODE, self).dmSize(__short.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmNup(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmNup(long)"""
        return int.__wrap(__DEVMODE.ndmNup(__long.valueOf(arg0)))

    @overload
    def dmDuplex(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDuplex()"""
        return int.__wrap(super(DEVMODE, self).dmDuplex())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def create() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.create()"""
        return DEVMODE.__wrap(__DEVMODE.create())

    @staticmethod
    @overload
    def ndmPaperSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperSize(long)"""
        return int.__wrap(__DEVMODE.ndmPaperSize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmPosition(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE.ndmPosition(long)"""
        return POINTL.__wrap(__DEVMODE.ndmPosition(__long.valueOf(arg0)))

    @overload
    def dmDriverVersion(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDriverVersion()"""
        return int.__wrap(super(DEVMODE, self).dmDriverVersion())

    @overload
    def dmPosition(self) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.DEVMODE.dmPosition()"""
        return 'POINTL'.__wrap(super(DEVMODE, self).dmPosition())

    @staticmethod
    @overload
    def ndmICMMethod(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmICMMethod(long)"""
        return int.__wrap(__DEVMODE.ndmICMMethod(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def dmLogPixels(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmLogPixels()"""
        return int.__wrap(super(DEVMODE, self).dmLogPixels())

    @staticmethod
    @overload
    def calloc() -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.calloc()"""
        return DEVMODE.__wrap(__DEVMODE.calloc())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ndmColor(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmColor(long)"""
        return int.__wrap(__DEVMODE.ndmColor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDisplayFrequency(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFrequency(long)"""
        return int.__wrap(__DEVMODE.ndmDisplayFrequency(__long.valueOf(arg0)))

    @overload
    def dmSize(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmSize()"""
        return int.__wrap(super(DEVMODE, self).dmSize())

    @overload
    def dmReserved2(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmReserved2()"""
        return int.__wrap(super(DEVMODE, self).dmReserved2())

    @overload
    def dmPanningHeight(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPanningHeight()"""
        return int.__wrap(super(DEVMODE, self).dmPanningHeight())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.malloc(org.lwjgl.system.MemoryStack)"""
        return DEVMODE.__wrap(__DEVMODE.malloc(arg0))

    @overload
    def dmFormName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.dmFormName()"""
        return 'ByteBuffer'.__wrap(super(DEVMODE, self).dmFormName())

    @overload
    def dmDisplayFixedOutput(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFixedOutput()"""
        return int.__wrap(super(DEVMODE, self).dmDisplayFixedOutput())

    @staticmethod
    @overload
    def ndmSpecVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmSpecVersion(long,short)"""
        __DEVMODE.ndmSpecVersion(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def ndmDeviceName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.ndmDeviceName(long)"""
        return ByteBuffer.__wrap(__DEVMODE.ndmDeviceName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DEVMODE.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def dmDefaultSource(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmDefaultSource()"""
        return int.__wrap(super(DEVMODE, self).dmDefaultSource())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def dmNup(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmNup()"""
        return int.__wrap(super(DEVMODE, self).dmNup())

    @overload
    def dmPaperLength(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmPaperLength()"""
        return int.__wrap(super(DEVMODE, self).dmPaperLength())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DEVMODE.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndmCopies(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmCopies(long)"""
        return int.__wrap(__DEVMODE.ndmCopies(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDisplayOrientation(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayOrientation(long)"""
        return int.__wrap(__DEVMODE.ndmDisplayOrientation(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.callocStack(int)"""
        return Buffer.__wrap(__DEVMODE.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.mallocStack(int)"""
        return Buffer.__wrap(__DEVMODE.mallocStack(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DEVMODE(java.nio.ByteBuffer)"""
        val = __DEVMODE(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ndmSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DEVMODE.ndmSize(long,short)"""
        __DEVMODE.ndmSize(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def dmDisplayFrequency(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFrequency()"""
        return int.__wrap(super(DEVMODE, self).dmDisplayFrequency())

    @overload
    def dmTTOption(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmTTOption()"""
        return int.__wrap(super(DEVMODE, self).dmTTOption())

    @overload
    def dmYResolution(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmYResolution()"""
        return int.__wrap(super(DEVMODE, self).dmYResolution())

    @overload
    def set(self, arg0: 'DEVMODE') -> 'DEVMODE':
        """public org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.set(org.lwjgl.system.windows.DEVMODE)"""
        return 'DEVMODE'.__wrap(super(__DEVMODE, self).set(arg0))

    @overload
    def dmDisplayFlags(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmDisplayFlags()"""
        return int.__wrap(super(DEVMODE, self).dmDisplayFlags())

    @staticmethod
    @overload
    def ndmPelsWidth(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPelsWidth(long)"""
        return int.__wrap(__DEVMODE.ndmPelsWidth(__long.valueOf(arg0)))

    @overload
    def dmICMMethod(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmICMMethod()"""
        return int.__wrap(super(DEVMODE, self).dmICMMethod())

    @overload
    def dmFields(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmFields()"""
        return int.__wrap(super(DEVMODE, self).dmFields())

    @staticmethod
    @overload
    def ndmBitsPerPel(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmBitsPerPel(long)"""
        return int.__wrap(__DEVMODE.ndmBitsPerPel(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmYResolution(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmYResolution(long)"""
        return int.__wrap(__DEVMODE.ndmYResolution(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmFormNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DEVMODE.ndmFormNameString(long)"""
        return str.__wrap(__DEVMODE.ndmFormNameString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDeviceNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DEVMODE.ndmDeviceNameString(long)"""
        return str.__wrap(__DEVMODE.ndmDeviceNameString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmTTOption(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmTTOption(long)"""
        return int.__wrap(__DEVMODE.ndmTTOption(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'DEVMODE':
        """public static org.lwjgl.system.windows.DEVMODE org.lwjgl.system.windows.DEVMODE.calloc(org.lwjgl.system.MemoryStack)"""
        return DEVMODE.__wrap(__DEVMODE.calloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.create(long,int)"""
        return Buffer.__wrap(__DEVMODE.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DEVMODE$Buffer org.lwjgl.system.windows.DEVMODE.createSafe(long,int)"""
        return Buffer.__wrap(__DEVMODE.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.sizeof()"""
        return int.__wrap(super(DEVMODE, self).sizeof())

    @overload
    def dmMediaType(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmMediaType()"""
        return int.__wrap(super(DEVMODE, self).dmMediaType())

    @overload
    def dmOrientation(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmOrientation()"""
        return int.__wrap(super(DEVMODE, self).dmOrientation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def dmDeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DEVMODE.dmDeviceName()"""
        return 'ByteBuffer'.__wrap(super(DEVMODE, self).dmDeviceName())

    @overload
    def dmScale(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmScale()"""
        return int.__wrap(super(DEVMODE, self).dmScale())

    @overload
    def dmPanningWidth(self) -> int:
        """public int org.lwjgl.system.windows.DEVMODE.dmPanningWidth()"""
        return int.__wrap(super(DEVMODE, self).dmPanningWidth())

    @staticmethod
    @overload
    def ndmPanningWidth(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmPanningWidth(long)"""
        return int.__wrap(__DEVMODE.ndmPanningWidth(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmReserved2(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmReserved2(long)"""
        return int.__wrap(__DEVMODE.ndmReserved2(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDisplayFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFlags(long)"""
        return int.__wrap(__DEVMODE.ndmDisplayFlags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmPaperLength(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.DEVMODE.ndmPaperLength(long)"""
        return int.__wrap(__DEVMODE.ndmPaperLength(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndmDisplayFixedOutput(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DEVMODE.ndmDisplayFixedOutput(long)"""
        return int.__wrap(__DEVMODE.ndmDisplayFixedOutput(__long.valueOf(arg0)))

    @overload
    def dmCollate(self) -> int:
        """public short org.lwjgl.system.windows.DEVMODE.dmCollate()"""
        return int.__wrap(super(DEVMODE, self).dmCollate()) 
 
 
# CLASS: org.lwjgl.system.windows.MONITORINFOEX$Buffer
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
import org.lwjgl.system.windows.MONITORINFOEX as __MONITORINFOEX_Buffer
__Buffer = __MONITORINFOEX_Buffer.Buffer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.CustomBuffer as __CustomBuffer
__CustomBuffer = __CustomBuffer
from builtins import bool
from builtins import str
import org.lwjgl.system.windows.RECT as __RECT
__RECT = __RECT
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.MONITORINFOEX.Buffer"""
 
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
    def cbSize(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer org.lwjgl.system.windows.MONITORINFOEX$Buffer.cbSize(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cbSize(__int.valueOf(arg0)))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def szDevice(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.MONITORINFOEX$Buffer.szDevice()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).szDevice())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.MONITORINFOEX$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def rcMonitor(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX$Buffer.rcMonitor()"""
        return 'RECT'.__wrap(super(Buffer, self).rcMonitor())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX$Buffer.dwFlags()"""
        return int.__wrap(super(Buffer, self).dwFlags())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def rcWork(self) -> 'RECT':
        """public org.lwjgl.system.windows.RECT org.lwjgl.system.windows.MONITORINFOEX$Buffer.rcWork()"""
        return 'RECT'.__wrap(super(Buffer, self).rcWork())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0)))

    @overload
    def szDeviceString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.MONITORINFOEX$Buffer.szDeviceString()"""
        return str.__wrap(super(Buffer, self).szDeviceString())

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

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

    @overload
    def cbSize(self) -> int:
        """public int org.lwjgl.system.windows.MONITORINFOEX$Buffer.cbSize()"""
        return int.__wrap(super(Buffer, self).cbSize())

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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as __PIXELFORMATDESCRIPTOR
__PIXELFORMATDESCRIPTOR = __PIXELFORMATDESCRIPTOR
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR as __PIXELFORMATDESCRIPTOR_Buffer
__Buffer = __PIXELFORMATDESCRIPTOR_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class PIXELFORMATDESCRIPTOR():
    """org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR"""
 
    @staticmethod
    def __wrap(java_value: __PIXELFORMATDESCRIPTOR) -> 'PIXELFORMATDESCRIPTOR':
        return PIXELFORMATDESCRIPTOR(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PIXELFORMATDESCRIPTOR):
        """
        Dynamic initializer for PIXELFORMATDESCRIPTOR.
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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.createSafe(long,int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack()"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.mallocStack())

    @staticmethod
    @overload
    def nnVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnVersion(long,short)"""
        __PIXELFORMATDESCRIPTOR.nnVersion(__long.valueOf(arg0), __short.valueOf(arg1))

    @staticmethod
    @overload
    def ncAccumBlueBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBlueBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAccumBlueBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ndwDamageMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwDamageMask(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ndwDamageMask(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnSize(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnSize(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.nnSize(__long.valueOf(arg0)))

    @overload
    def dwVisibleMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwVisibleMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).dwVisibleMask(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def ncBlueBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncBlueBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncRedBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncRedBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncAccumRedBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumRedBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAccumRedBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def cBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cBlueBits())

    @overload
    def cAuxBuffers(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAuxBuffers()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAuxBuffers())

    @staticmethod
    @overload
    def ndwFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwFlags(long,int)"""
        __PIXELFORMATDESCRIPTOR.ndwFlags(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def niLayerType(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niLayerType(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.niLayerType(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaShift(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAlphaShift(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def cAccumBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAccumBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwVisibleMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwVisibleMask(long,int)"""
        __PIXELFORMATDESCRIPTOR.ndwVisibleMask(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.sizeof()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(long)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.create(__long.valueOf(arg0)))

    @overload
    def cAccumAlphaBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumAlphaBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAccumAlphaBits(__byte.valueOf(arg0)))

    @overload
    def dwDamageMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwDamageMask()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).dwDamageMask())

    @staticmethod
    @overload
    def callocStack() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack()"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.callocStack())

    @overload
    def iLayerType(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iLayerType(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).iLayerType(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ndwLayerMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwLayerMask(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ndwLayerMask(__long.valueOf(arg0)))

    @overload
    def nVersion(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nVersion(short)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).nVersion(__short.valueOf(arg0)))

    @overload
    def nSize(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nSize()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).nSize())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def cDepthBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cDepthBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cDepthBits())

    @staticmethod
    @overload
    def ncAccumGreenBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumGreenBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAccumGreenBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncRedShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedShift(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncRedShift(__long.valueOf(arg0)))

    @overload
    def cAlphaShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAlphaShift(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def nnVersion(arg0: int) -> int:
        """public static short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnVersion(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.nnVersion(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cAccumGreenBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumGreenBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAccumGreenBits(__byte.valueOf(arg0)))

    @overload
    def cStencilBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cStencilBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cStencilBits())

    @staticmethod
    @overload
    def ncAccumRedBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumRedBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAccumRedBits(__long.valueOf(arg0)))

    @overload
    def cAccumAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumAlphaBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumAlphaBits())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueShift(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncBlueShift(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def niPixelType(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niPixelType(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.niPixelType(__long.valueOf(arg0)))

    @overload
    def cDepthBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cDepthBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cDepthBits(__byte.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def cAccumBlueBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBlueBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAccumBlueBits(__byte.valueOf(arg0)))

    @overload
    def nVersion(self) -> int:
        """public short org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nVersion()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).nVersion())

    @staticmethod
    @overload
    def ncGreenShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenShift(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncGreenShift(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAlphaBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def iPixelType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iPixelType()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).iPixelType())

    @staticmethod
    @overload
    def ndwVisibleMask(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwVisibleMask(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ndwVisibleMask(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(long,int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def cAlphaBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAlphaBits(__byte.valueOf(arg0)))

    @overload
    def cAuxBuffers(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAuxBuffers(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAuxBuffers(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.mallocStack(__int.valueOf(arg0)))

    @overload
    def nSize(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nSize(short)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).nSize(__short.valueOf(arg0)))

    @overload
    def cAccumBlueBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBlueBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumBlueBits())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def cBlueShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cBlueShift(__byte.valueOf(arg0)))

    @overload
    def cAccumRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumRedBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumRedBits())

    @overload
    def dwLayerMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwLayerMask()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).dwLayerMask())

    @staticmethod
    @overload
    def niPixelType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niPixelType(long,byte)"""
        __PIXELFORMATDESCRIPTOR.niPixelType(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncDepthBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncDepthBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncDepthBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.callocStack(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.callocStack(arg0))

    @staticmethod
    @overload
    def ncAccumAlphaBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def bReserved(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.bReserved(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).bReserved(__byte.valueOf(arg0)))

    @overload
    def cRedShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cRedShift(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncColorBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncColorBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncColorBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def nnSize(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nnSize(long,short)"""
        __PIXELFORMATDESCRIPTOR.nnSize(__long.valueOf(arg0), __short.valueOf(arg1))

    @overload
    def cColorBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cColorBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cColorBits())

    @overload
    def set(self, arg0: 'PIXELFORMATDESCRIPTOR') -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.set(org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).set(arg0))

    @staticmethod
    @overload
    def nbReserved(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nbReserved(long,byte)"""
        __PIXELFORMATDESCRIPTOR.nbReserved(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def nbReserved(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.nbReserved(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.nbReserved(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.calloc(__int.valueOf(arg0), arg1))

    @overload
    def cStencilBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cStencilBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cStencilBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAuxBuffers(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAuxBuffers(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAuxBuffers(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def cBlueShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueShift()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cBlueShift())

    @overload
    def cAccumBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumBits())

    @overload
    def dwLayerMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwLayerMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).dwLayerMask(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAccumBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAccumBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncGreenBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncGreenBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncRedBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncRedBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc()"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.calloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAccumBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAccumBits(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cRedBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cRedBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncBlueShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueShift(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncBlueShift(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ncAccumBlueBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumBlueBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAccumBlueBits(__long.valueOf(arg0)))

    @overload
    def cRedBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cRedBits())

    @staticmethod
    @overload
    def malloc() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc()"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.malloc())

    @overload
    def bReserved(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.bReserved()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).bReserved())

    @overload
    def dwFlags(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwFlags()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).dwFlags())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def iPixelType(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iPixelType(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).iPixelType(__byte.valueOf(arg0)))

    @overload
    def cGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cGreenBits())

    @staticmethod
    @overload
    def niLayerType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.niLayerType(long,byte)"""
        __PIXELFORMATDESCRIPTOR.niLayerType(__long.valueOf(arg0), __byte.valueOf(arg1))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def ncGreenBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncGreenBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def cGreenShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenShift()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cGreenShift())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def cGreenBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cGreenBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncStencilBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncStencilBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncStencilBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create(int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncGreenShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncGreenShift(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncGreenShift(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def cColorBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cColorBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cColorBits(__byte.valueOf(arg0)))

    @overload
    def cAlphaShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaShift()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAlphaShift())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR(java.nio.ByteBuffer)"""
        val = __PIXELFORMATDESCRIPTOR(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def dwDamageMask(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwDamageMask(int)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).dwDamageMask(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.malloc(arg0))

    @overload
    def cRedShift(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cRedShift()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cRedShift())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.calloc(arg0))

    @staticmethod
    @overload
    def ncAccumGreenBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumGreenBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncAccumGreenBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: int, arg10: int, arg11: int, arg12: int, arg13: int, arg14: int, arg15: int, arg16: int, arg17: int, arg18: int, arg19: int, arg20: int, arg21: int, arg22: int, arg23: int, arg24: int, arg25: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.set(short,short,int,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,byte,int,int,int)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).set(__short.valueOf(arg0), __short.valueOf(arg1), __int.valueOf(arg2), __byte.valueOf(arg3), __byte.valueOf(arg4), __byte.valueOf(arg5), __byte.valueOf(arg6), __byte.valueOf(arg7), __byte.valueOf(arg8), __byte.valueOf(arg9), __byte.valueOf(arg10), __byte.valueOf(arg11), __byte.valueOf(arg12), __byte.valueOf(arg13), __byte.valueOf(arg14), __byte.valueOf(arg15), __byte.valueOf(arg16), __byte.valueOf(arg17), __byte.valueOf(arg18), __byte.valueOf(arg19), __byte.valueOf(arg20), __byte.valueOf(arg21), __byte.valueOf(arg22), __int.valueOf(arg23), __int.valueOf(arg24), __int.valueOf(arg25)))

    @staticmethod
    @overload
    def ndwLayerMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwLayerMask(long,int)"""
        __PIXELFORMATDESCRIPTOR.ndwLayerMask(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.malloc(int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncDepthBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncDepthBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncDepthBits(__long.valueOf(arg0)))

    @overload
    def cAccumRedBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumRedBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cAccumRedBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAlphaBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.create()"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.create())

    @overload
    def dwFlags(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwFlags(int)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).dwFlags(__int.valueOf(arg0)))

    @overload
    def dwVisibleMask(self) -> int:
        """public int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.dwVisibleMask()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).dwVisibleMask())

    @overload
    def iLayerType(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.iLayerType()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).iLayerType())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR$Buffer org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.calloc(int)"""
        return Buffer.__wrap(__PIXELFORMATDESCRIPTOR.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.createSafe(long)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncRedShift(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncRedShift(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncRedShift(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'PIXELFORMATDESCRIPTOR':
        """public static org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.mallocStack(org.lwjgl.system.MemoryStack)"""
        return PIXELFORMATDESCRIPTOR.__wrap(__PIXELFORMATDESCRIPTOR.mallocStack(arg0))

    @overload
    def cBlueBits(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cBlueBits(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cBlueBits(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncAlphaShift(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAlphaShift(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAlphaShift(__long.valueOf(arg0)))

    @overload
    def cGreenShift(self, arg0: int) -> 'PIXELFORMATDESCRIPTOR':
        """public org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cGreenShift(byte)"""
        return 'PIXELFORMATDESCRIPTOR'.__wrap(super(__PIXELFORMATDESCRIPTOR, self).cGreenShift(__byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ncColorBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncColorBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncColorBits(__long.valueOf(arg0)))

    @overload
    def cAccumGreenBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAccumGreenBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAccumGreenBits())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def ncAccumAlphaBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAccumAlphaBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwDamageMask(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwDamageMask(long,int)"""
        __PIXELFORMATDESCRIPTOR.ndwDamageMask(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def cAlphaBits(self) -> int:
        """public byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.cAlphaBits()"""
        return int.__wrap(super(PIXELFORMATDESCRIPTOR, self).cAlphaBits())

    @staticmethod
    @overload
    def ncBlueBits(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncBlueBits(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncBlueBits(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ncStencilBits(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncStencilBits(long,byte)"""
        __PIXELFORMATDESCRIPTOR.ncStencilBits(__long.valueOf(arg0), __byte.valueOf(arg1))

    @staticmethod
    @overload
    def ncAuxBuffers(arg0: int) -> int:
        """public static byte org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ncAuxBuffers(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ncAuxBuffers(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndwFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.PIXELFORMATDESCRIPTOR.ndwFlags(long)"""
        return int.__wrap(__PIXELFORMATDESCRIPTOR.ndwFlags(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.DISPLAY_DEVICE
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.DISPLAY_DEVICE as __DISPLAY_DEVICE_Buffer
__Buffer = __DISPLAY_DEVICE_Buffer.Buffer
import java.lang.Long as __long
import org.lwjgl.system.windows.DISPLAY_DEVICE as __DISPLAY_DEVICE
__DISPLAY_DEVICE = __DISPLAY_DEVICE
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class DISPLAY_DEVICE():
    """org.lwjgl.system.windows.DISPLAY_DEVICE"""
 
    @staticmethod
    def __wrap(java_value: __DISPLAY_DEVICE) -> 'DISPLAY_DEVICE':
        return DISPLAY_DEVICE(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DISPLAY_DEVICE):
        """
        Dynamic initializer for DISPLAY_DEVICE.
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
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.create(long,int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def DeviceIDString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceIDString()"""
        return str.__wrap(super(DISPLAY_DEVICE, self).DeviceIDString())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.calloc(__int.valueOf(arg0), arg1))

    @overload
    def DeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceNameString()"""
        return str.__wrap(super(DISPLAY_DEVICE, self).DeviceNameString())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DISPLAY_DEVICE(java.nio.ByteBuffer)"""
        val = __DISPLAY_DEVICE(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.mallocStack(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def DeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceName()"""
        return 'ByteBuffer'.__wrap(super(DISPLAY_DEVICE, self).DeviceName())

    @staticmethod
    @overload
    def ncb(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.DISPLAY_DEVICE.ncb(long,int)"""
        __DISPLAY_DEVICE.ncb(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def nDeviceKey(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceKey(long)"""
        return ByteBuffer.__wrap(__DISPLAY_DEVICE.nDeviceKey(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack()"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.mallocStack())

    @overload
    def DeviceString(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceString()"""
        return 'ByteBuffer'.__wrap(super(DISPLAY_DEVICE, self).DeviceString())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.createSafe(long,int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nDeviceKeyString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceKeyString(long)"""
        return str.__wrap(__DISPLAY_DEVICE.nDeviceKeyString(__long.valueOf(arg0)))

    @overload
    def StateFlags(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.StateFlags()"""
        return int.__wrap(super(DISPLAY_DEVICE, self).StateFlags())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.create(int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ncb(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DISPLAY_DEVICE.ncb(long)"""
        return int.__wrap(__DISPLAY_DEVICE.ncb(__long.valueOf(arg0)))

    @overload
    def cb(self, arg0: int) -> 'DISPLAY_DEVICE':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.cb(int)"""
        return 'DISPLAY_DEVICE'.__wrap(super(__DISPLAY_DEVICE, self).cb(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def DeviceKeyString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceKeyString()"""
        return str.__wrap(super(DISPLAY_DEVICE, self).DeviceKeyString())

    @staticmethod
    @overload
    def nDeviceName(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceName(long)"""
        return ByteBuffer.__wrap(__DISPLAY_DEVICE.nDeviceName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDeviceString(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceString(long)"""
        return ByteBuffer.__wrap(__DISPLAY_DEVICE.nDeviceString(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.malloc(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.sizeof()"""
        return int.__wrap(super(DISPLAY_DEVICE, self).sizeof())

    @overload
    def set(self, arg0: 'DISPLAY_DEVICE') -> 'DISPLAY_DEVICE':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.set(org.lwjgl.system.windows.DISPLAY_DEVICE)"""
        return 'DISPLAY_DEVICE'.__wrap(super(__DISPLAY_DEVICE, self).set(arg0))

    @staticmethod
    @overload
    def calloc() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.calloc()"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.calloc())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(int)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nStateFlags(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.DISPLAY_DEVICE.nStateFlags(long)"""
        return int.__wrap(__DISPLAY_DEVICE.nStateFlags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDeviceNameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceNameString(long)"""
        return str.__wrap(__DISPLAY_DEVICE.nDeviceNameString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.calloc(org.lwjgl.system.MemoryStack)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.calloc(arg0))

    @overload
    def DeviceID(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceID()"""
        return 'ByteBuffer'.__wrap(super(DISPLAY_DEVICE, self).DeviceID())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.createSafe(long)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nDeviceIDString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceIDString(long)"""
        return str.__wrap(__DISPLAY_DEVICE.nDeviceIDString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def nDeviceID(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceID(long)"""
        return ByteBuffer.__wrap(__DISPLAY_DEVICE.nDeviceID(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def DeviceStringString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceStringString()"""
        return str.__wrap(super(DISPLAY_DEVICE, self).DeviceStringString())

    @staticmethod
    @overload
    def malloc() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.malloc()"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.malloc())

    @staticmethod
    @overload
    def callocStack() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack()"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.callocStack())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create() -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.create()"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.create())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: int) -> 'DISPLAY_DEVICE':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE org.lwjgl.system.windows.DISPLAY_DEVICE.create(long)"""
        return DISPLAY_DEVICE.__wrap(__DISPLAY_DEVICE.create(__long.valueOf(arg0)))

    @overload
    def DeviceKey(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE.DeviceKey()"""
        return 'ByteBuffer'.__wrap(super(DISPLAY_DEVICE, self).DeviceKey())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__DISPLAY_DEVICE.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def cb(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE.cb()"""
        return int.__wrap(super(DISPLAY_DEVICE, self).cb())

    @staticmethod
    @overload
    def nDeviceStringString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE.nDeviceStringString(long)"""
        return str.__wrap(__DISPLAY_DEVICE.nDeviceStringString(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as __SECURITY_ATTRIBUTES_Buffer
__Buffer = __SECURITY_ATTRIBUTES_Buffer.Buffer
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.SECURITY_ATTRIBUTES.Buffer"""
 
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
    def bInheritHandle(self, arg0: bool) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.bInheritHandle(boolean)"""
        return 'Buffer'.__wrap(super(__Buffer, self).bInheritHandle(__boolean.valueOf(arg0)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(__int.valueOf(arg0), arg1))

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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

    @overload
    def lpSecurityDescriptor(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.lpSecurityDescriptor(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).lpSecurityDescriptor(__long.valueOf(arg0)))

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
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer(long,int)"""
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

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

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
    def nLength(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.nLength(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).nLength(__int.valueOf(arg0)))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def bInheritHandle(self) -> bool:
        """public boolean org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.bInheritHandle()"""
        return bool.__wrap(super(Buffer, self).bInheritHandle())

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

    @overload
    def lpSecurityDescriptor(self) -> int:
        """public long org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.lpSecurityDescriptor()"""
        return int.__wrap(super(Buffer, self).lpSecurityDescriptor())

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
    def nLength(self) -> int:
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer.nLength()"""
        return int.__wrap(super(Buffer, self).nLength())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.SECURITY_ATTRIBUTES
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as __SECURITY_ATTRIBUTES
__SECURITY_ATTRIBUTES = __SECURITY_ATTRIBUTES
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.windows.SECURITY_ATTRIBUTES as __SECURITY_ATTRIBUTES_Buffer
__Buffer = __SECURITY_ATTRIBUTES_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class SECURITY_ATTRIBUTES():
    """org.lwjgl.system.windows.SECURITY_ATTRIBUTES"""
 
    @staticmethod
    def __wrap(java_value: __SECURITY_ATTRIBUTES) -> 'SECURITY_ATTRIBUTES':
        return SECURITY_ATTRIBUTES(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SECURITY_ATTRIBUTES):
        """
        Dynamic initializer for SECURITY_ATTRIBUTES.
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
    def malloc() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc()"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.malloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.validate(long)"""
        __SECURITY_ATTRIBUTES.validate(__long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack()"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.mallocStack())

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

    @overload
    def set(self, arg0: 'SECURITY_ATTRIBUTES') -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.set(org.lwjgl.system.windows.SECURITY_ATTRIBUTES)"""
        return 'SECURITY_ATTRIBUTES'.__wrap(super(__SECURITY_ATTRIBUTES, self).set(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.calloc(__int.valueOf(arg0), arg1))

    @overload
    def nLength(self) -> int:
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nLength()"""
        return int.__wrap(super(SECURITY_ATTRIBUTES, self).nLength())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.mallocStack(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.mallocStack(arg0))

    @overload
    def bInheritHandle(self) -> bool:
        """public boolean org.lwjgl.system.windows.SECURITY_ATTRIBUTES.bInheritHandle()"""
        return bool.__wrap(super(SECURITY_ATTRIBUTES, self).bInheritHandle())

    @overload
    def bInheritHandle(self, arg0: bool) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.bInheritHandle(boolean)"""
        return 'SECURITY_ATTRIBUTES'.__wrap(super(__SECURITY_ATTRIBUTES, self).bInheritHandle(__boolean.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def nnLength(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nnLength(long)"""
        return int.__wrap(__SECURITY_ATTRIBUTES.nnLength(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.sizeof()"""
        return int.__wrap(super(SECURITY_ATTRIBUTES, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.createSafe(long)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.createSafe(__long.valueOf(arg0)))

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
    def lpSecurityDescriptor(self, arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.lpSecurityDescriptor(long)"""
        return 'SECURITY_ATTRIBUTES'.__wrap(super(__SECURITY_ATTRIBUTES, self).lpSecurityDescriptor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.calloc(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.malloc(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc()"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.calloc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create()"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.create())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nbInheritHandle(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nbInheritHandle(long)"""
        return int.__wrap(__SECURITY_ATTRIBUTES.nbInheritHandle(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nlpSecurityDescriptor(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nlpSecurityDescriptor(long)"""
        return int.__wrap(__SECURITY_ATTRIBUTES.nlpSecurityDescriptor(__long.valueOf(arg0)))

    @overload
    def nLength(self, arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nLength(int)"""
        return 'SECURITY_ATTRIBUTES'.__wrap(super(__SECURITY_ATTRIBUTES, self).nLength(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES(java.nio.ByteBuffer)"""
        val = __SECURITY_ATTRIBUTES(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nlpSecurityDescriptor(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nlpSecurityDescriptor(long,long)"""
        __SECURITY_ATTRIBUTES.nlpSecurityDescriptor(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nbInheritHandle(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nbInheritHandle(long,int)"""
        __SECURITY_ATTRIBUTES.nbInheritHandle(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack()"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.callocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def lpSecurityDescriptor(self) -> int:
        """public long org.lwjgl.system.windows.SECURITY_ATTRIBUTES.lpSecurityDescriptor()"""
        return int.__wrap(super(SECURITY_ATTRIBUTES, self).lpSecurityDescriptor())

    @overload
    def set(self, arg0: int, arg1: int, arg2: bool) -> 'SECURITY_ATTRIBUTES':
        """public org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.set(int,long,boolean)"""
        return 'SECURITY_ATTRIBUTES'.__wrap(super(__SECURITY_ATTRIBUTES, self).set(__int.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.callocStack(org.lwjgl.system.MemoryStack)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.callocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(long,int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.calloc(int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES$Buffer org.lwjgl.system.windows.SECURITY_ATTRIBUTES.createSafe(long,int)"""
        return Buffer.__wrap(__SECURITY_ATTRIBUTES.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'SECURITY_ATTRIBUTES':
        """public static org.lwjgl.system.windows.SECURITY_ATTRIBUTES org.lwjgl.system.windows.SECURITY_ATTRIBUTES.create(long)"""
        return SECURITY_ATTRIBUTES.__wrap(__SECURITY_ATTRIBUTES.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nnLength(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.SECURITY_ATTRIBUTES.nnLength(long,int)"""
        __SECURITY_ATTRIBUTES.nnLength(__long.valueOf(arg0), __int.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.windows.GDI32$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import org.lwjgl.system.windows.GDI32 as __GDI32_Functions
__Functions = __GDI32_Functions.Functions
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.system.windows.GDI32.Functions"""
 
    @staticmethod
    def __wrap(java_value: __Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Functions):
        """
        Dynamic initializer for Functions.
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
 
 
# CLASS: org.lwjgl.system.windows.WinBase
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.windows.WinBase as __WinBase
__WinBase = __WinBase
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WinBase():
    """org.lwjgl.system.windows.WinBase"""
 
    @staticmethod
    def __wrap(java_value: __WinBase) -> 'WinBase':
        return WinBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WinBase):
        """
        Dynamic initializer for WinBase.
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
    def nLoadLibrary(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nLoadLibrary(long)"""
        return int.__wrap(__WinBase.nLoadLibrary(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nGetProcAddress(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nGetProcAddress(long,long)"""
        return int.__wrap(__WinBase.nGetProcAddress(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def GetModuleHandle(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetModuleHandle(java.lang.CharSequence)"""
        return int.__wrap(__WinBase.GetModuleHandle(arg0))

    @staticmethod
    @overload
    def LoadLibrary(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.LoadLibrary(java.lang.CharSequence)"""
        return int.__wrap(__WinBase.LoadLibrary(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def GetLastError() -> int:
        """public static native int org.lwjgl.system.windows.WinBase.GetLastError()"""
        return int.__wrap(__WinBase.GetLastError())

    @staticmethod
    @overload
    def GetModuleHandle(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetModuleHandle(java.nio.ByteBuffer)"""
        return int.__wrap(__WinBase.GetModuleHandle(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def GetModuleFileName(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static int org.lwjgl.system.windows.WinBase.GetModuleFileName(long,java.nio.ByteBuffer)"""
        return int.__wrap(__WinBase.GetModuleFileName(__long.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getLastError() -> int:
        """public static native int org.lwjgl.system.windows.WinBase.getLastError()"""
        return int.__wrap(__WinBase.getLastError())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def LocalFree(arg0: int) -> int:
        """public static long org.lwjgl.system.windows.WinBase.LocalFree(long)"""
        return int.__wrap(__WinBase.LocalFree(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nGetModuleFileName(arg0: int, arg1: int, arg2: int) -> int:
        """public static native int org.lwjgl.system.windows.WinBase.nGetModuleFileName(long,long,int)"""
        return int.__wrap(__WinBase.nGetModuleFileName(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def GetModuleFileName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.windows.WinBase.GetModuleFileName(long,int)"""
        return str.__wrap(__WinBase.GetModuleFileName(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def FreeLibrary(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.windows.WinBase.FreeLibrary(long)"""
        return bool.__wrap(__WinBase.FreeLibrary(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def GetProcAddress(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetProcAddress(long,java.lang.CharSequence)"""
        return int.__wrap(__WinBase.GetProcAddress(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nFreeLibrary(arg0: int) -> int:
        """public static native int org.lwjgl.system.windows.WinBase.nFreeLibrary(long)"""
        return int.__wrap(__WinBase.nFreeLibrary(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nLocalFree(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nLocalFree(long)"""
        return int.__wrap(__WinBase.nLocalFree(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def LoadLibrary(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.LoadLibrary(java.nio.ByteBuffer)"""
        return int.__wrap(__WinBase.LoadLibrary(arg0))

    @staticmethod
    @overload
    def GetProcAddress(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.windows.WinBase.GetProcAddress(long,java.nio.ByteBuffer)"""
        return int.__wrap(__WinBase.GetProcAddress(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nGetModuleHandle(arg0: int) -> int:
        """public static native long org.lwjgl.system.windows.WinBase.nGetModuleHandle(long)"""
        return int.__wrap(__WinBase.nGetModuleHandle(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer
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
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.DISPLAY_DEVICE as __DISPLAY_DEVICE_Buffer
__Buffer = __DISPLAY_DEVICE_Buffer.Buffer
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer():
    """org.lwjgl.system.windows.DISPLAY_DEVICE.Buffer"""
 
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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address0())

    @overload
    def DeviceID(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceID()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).DeviceID())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def cb(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.cb(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).cb(__int.valueOf(arg0)))

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
    def DeviceKey(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceKey()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).DeviceKey())

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
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).get(arg0))

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
    def cb(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.cb()"""
        return int.__wrap(super(Buffer, self).cb())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def DeviceNameString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceNameString()"""
        return str.__wrap(super(Buffer, self).DeviceNameString())

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
    def DeviceName(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceName()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).DeviceName())

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
    def StateFlags(self) -> int:
        """public int org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.StateFlags()"""
        return int.__wrap(super(Buffer, self).StateFlags())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @overload
    def DeviceStringString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceStringString()"""
        return str.__wrap(super(Buffer, self).DeviceStringString())

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

    @overload
    def DeviceString(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceString()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).DeviceString())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def DeviceKeyString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceKeyString()"""
        return str.__wrap(super(Buffer, self).DeviceKeyString())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def DeviceIDString(self) -> str:
        """public java.lang.String org.lwjgl.system.windows.DISPLAY_DEVICE$Buffer.DeviceIDString()"""
        return str.__wrap(super(Buffer, self).DeviceIDString())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.windows.POINTL
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.windows.POINTL as __POINTL
__POINTL = __POINTL
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.windows.POINTL as __POINTL_Buffer
__Buffer = __POINTL_Buffer.Buffer
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
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class POINTL():
    """org.lwjgl.system.windows.POINTL"""
 
    @staticmethod
    def __wrap(java_value: __POINTL) -> 'POINTL':
        return POINTL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __POINTL):
        """
        Dynamic initializer for POINTL.
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
    def nx(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINTL.nx(long,int)"""
        __POINTL.nx(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.createSafe(long,int)"""
        return Buffer.__wrap(__POINTL.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'POINTL') -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.set(org.lwjgl.system.windows.POINTL)"""
        return 'POINTL'.__wrap(super(__POINTL, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

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
    def calloc(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.calloc(org.lwjgl.system.MemoryStack)"""
        return POINTL.__wrap(__POINTL.calloc(arg0))

    @overload
    def x(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.x()"""
        return int.__wrap(super(POINTL, self).x())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.malloc(int)"""
        return Buffer.__wrap(__POINTL.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.create(int)"""
        return Buffer.__wrap(__POINTL.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: int):
        """public static void org.lwjgl.system.windows.POINTL.ny(long,int)"""
        __POINTL.ny(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.mallocStack()"""
        return POINTL.__wrap(__POINTL.mallocStack())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.create(long,int)"""
        return Buffer.__wrap(__POINTL.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.malloc(org.lwjgl.system.MemoryStack)"""
        return POINTL.__wrap(__POINTL.malloc(arg0))

    @staticmethod
    @overload
    def calloc() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.calloc()"""
        return POINTL.__wrap(__POINTL.calloc())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.calloc(int)"""
        return Buffer.__wrap(__POINTL.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.mallocStack(int)"""
        return Buffer.__wrap(__POINTL.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINTL.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.mallocStack(org.lwjgl.system.MemoryStack)"""
        return POINTL.__wrap(__POINTL.mallocStack(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int, arg1: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.set(int,int)"""
        return 'POINTL'.__wrap(super(__POINTL, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.callocStack(int)"""
        return Buffer.__wrap(__POINTL.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.callocStack(org.lwjgl.system.MemoryStack)"""
        return POINTL.__wrap(__POINTL.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINTL.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.callocStack()"""
        return POINTL.__wrap(__POINTL.callocStack())

    @staticmethod
    @overload
    def malloc() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.malloc()"""
        return POINTL.__wrap(__POINTL.malloc())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.create(long)"""
        return POINTL.__wrap(__POINTL.create(__long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINTL.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nx(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINTL.nx(long)"""
        return int.__wrap(__POINTL.nx(__long.valueOf(arg0)))

    @overload
    def y(self, arg0: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.y(int)"""
        return 'POINTL'.__wrap(super(__POINTL, self).y(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.windows.POINTL(java.nio.ByteBuffer)"""
        val = __POINTL(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create() -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.create()"""
        return POINTL.__wrap(__POINTL.create())

    @staticmethod
    @overload
    def ny(arg0: int) -> int:
        """public static int org.lwjgl.system.windows.POINTL.ny(long)"""
        return int.__wrap(__POINTL.ny(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.windows.POINTL$Buffer org.lwjgl.system.windows.POINTL.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__POINTL.callocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.sizeof()"""
        return int.__wrap(super(POINTL, self).sizeof())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def x(self, arg0: int) -> 'POINTL':
        """public org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.x(int)"""
        return 'POINTL'.__wrap(super(__POINTL, self).x(__int.valueOf(arg0)))

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
    def y(self) -> int:
        """public int org.lwjgl.system.windows.POINTL.y()"""
        return int.__wrap(super(POINTL, self).y())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'POINTL':
        """public static org.lwjgl.system.windows.POINTL org.lwjgl.system.windows.POINTL.createSafe(long)"""
        return POINTL.__wrap(__POINTL.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)