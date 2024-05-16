from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
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

from abc import abstractmethod, ABC
import org.lwjgl.system.macosx.EnumerationMutationHandler as __EnumerationMutationHandler
__EnumerationMutationHandler = __EnumerationMutationHandler
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
import org.lwjgl.system.macosx.EnumerationMutationHandlerI as __EnumerationMutationHandlerI
__EnumerationMutationHandlerI = __EnumerationMutationHandlerI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EnumerationMutationHandler(ABC, pyglsystem.__Callback, pyglsystem.Callback, __EnumerationMutationHandlerI, EnumerationMutationHandlerI):
    """org.lwjgl.system.macosx.EnumerationMutationHandler"""
 
    @staticmethod
    def __wrap(java_value: __EnumerationMutationHandler) -> 'EnumerationMutationHandler':
        return EnumerationMutationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumerationMutationHandler):
        """
        Dynamic initializer for EnumerationMutationHandler.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.EnumerationMutationHandlerI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(EnumerationMutationHandlerI, self).getCallInterface())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'EnumerationMutationHandlerI') -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(org.lwjgl.system.macosx.EnumerationMutationHandlerI)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.create(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.EnumerationMutationHandlerI.callback(long,long)"""
        super(__EnumerationMutationHandlerI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def create(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(long)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.createSafe(long)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.createSafe(__long.valueOf(arg0)))

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
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.system.macosx.EnumerationMutationHandlerI.invoke(long)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString())

 
 
 
# CLASS: org.lwjgl.system.macosx.EnumerationMutationHandler
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
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

from abc import abstractmethod, ABC
import org.lwjgl.system.macosx.EnumerationMutationHandler as __EnumerationMutationHandler
__EnumerationMutationHandler = __EnumerationMutationHandler
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
import org.lwjgl.system.macosx.EnumerationMutationHandlerI as __EnumerationMutationHandlerI
__EnumerationMutationHandlerI = __EnumerationMutationHandlerI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EnumerationMutationHandler(ABC, pyglsystem.__Callback, pyglsystem.Callback, __EnumerationMutationHandlerI, EnumerationMutationHandlerI):
    """org.lwjgl.system.macosx.EnumerationMutationHandler"""
 
    @staticmethod
    def __wrap(java_value: __EnumerationMutationHandler) -> 'EnumerationMutationHandler':
        return EnumerationMutationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumerationMutationHandler):
        """
        Dynamic initializer for EnumerationMutationHandler.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.EnumerationMutationHandlerI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(EnumerationMutationHandlerI, self).getCallInterface())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'EnumerationMutationHandlerI') -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(org.lwjgl.system.macosx.EnumerationMutationHandlerI)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.create(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.EnumerationMutationHandlerI.callback(long,long)"""
        super(__EnumerationMutationHandlerI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def create(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.create(long)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'EnumerationMutationHandler':
        """public static org.lwjgl.system.macosx.EnumerationMutationHandler org.lwjgl.system.macosx.EnumerationMutationHandler.createSafe(long)"""
        return EnumerationMutationHandler.__wrap(__EnumerationMutationHandler.createSafe(__long.valueOf(arg0)))

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
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.system.macosx.EnumerationMutationHandlerI.invoke(long)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString())

 
 
 
# CLASS: org.lwjgl.system.macosx.EnumerationMutationHandler 
 
 
# CLASS: org.lwjgl.system.macosx.LibC
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.system.macosx.LibC as __LibC
__LibC = __LibC
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LibC():
    """org.lwjgl.system.macosx.LibC"""
 
    @staticmethod
    def __wrap(java_value: __LibC) -> 'LibC':
        return LibC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibC):
        """
        Dynamic initializer for LibC.
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

    @staticmethod
    @overload
    def getpid() -> int:
        """public static long org.lwjgl.system.macosx.LibC.getpid()"""
        return int.__wrap(__LibC.getpid())

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
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibraryBundle
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
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.lwjgl.system.macosx.MacOSXLibrary as __MacOSXLibrary
__MacOSXLibrary = __MacOSXLibrary
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
from builtins import bool
import org.lwjgl.system.macosx.MacOSXLibraryBundle as __MacOSXLibraryBundle
__MacOSXLibraryBundle = __MacOSXLibraryBundle
from builtins import int
 
class MacOSXLibraryBundle(__MacOSXLibrary, MacOSXLibrary):
    """org.lwjgl.system.macosx.MacOSXLibraryBundle"""
 
    @staticmethod
    def __wrap(java_value: __MacOSXLibraryBundle) -> 'MacOSXLibraryBundle':
        return MacOSXLibraryBundle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MacOSXLibraryBundle):
        """
        Dynamic initializer for MacOSXLibraryBundle.
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
    def getName(self) -> str:
        """public java.lang.String org.lwjgl.system.SharedLibrary$Default.getName()"""
        return str.__wrap(super(pyglsystem.SharedLibrary$Default, self).getName())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.macosx.MacOSXLibraryBundle.free()"""
        super(MacOSXLibraryBundle, self).free()

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.macosx.MacOSXLibraryBundle(java.lang.String,long)"""
        val = __MacOSXLibraryBundle(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.create(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibraryBundle':
        """public static org.lwjgl.system.macosx.MacOSXLibraryBundle org.lwjgl.system.macosx.MacOSXLibraryBundle.create(java.lang.String)"""
        return MacOSXLibraryBundle.__wrap(__MacOSXLibraryBundle.create(arg0))

    @overload
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.macosx.MacOSXLibraryBundle.getFunctionAddress(java.nio.ByteBuffer)"""
        return int.__wrap(super(__MacOSXLibraryBundle, self).getFunctionAddress(arg0))

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.getWithIdentifier(arg0))

    @override
    @overload
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.MacOSXLibraryBundle.getPath()"""
        return str.__wrap(super(MacOSXLibraryBundle, self).getPath())

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibraryBundle':
        """public static org.lwjgl.system.macosx.MacOSXLibraryBundle org.lwjgl.system.macosx.MacOSXLibraryBundle.getWithIdentifier(java.lang.String)"""
        return MacOSXLibraryBundle.__wrap(__MacOSXLibraryBundle.getWithIdentifier(arg0))

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.system.macosx.CoreFoundation
from builtins import str
import java.lang.Boolean as __boolean
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
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import org.lwjgl.system.macosx.CoreFoundation as __CoreFoundation
__CoreFoundation = __CoreFoundation
from builtins import int
 
class CoreFoundation():
    """org.lwjgl.system.macosx.CoreFoundation"""
 
    @staticmethod
    def __wrap(java_value: __CoreFoundation) -> 'CoreFoundation':
        return CoreFoundation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CoreFoundation):
        """
        Dynamic initializer for CoreFoundation.
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
    def nCFRetain(arg0: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFRetain(long)"""
        return int.__wrap(__CoreFoundation.nCFRetain(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCFBundleGetFunctionPointerForName(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleGetFunctionPointerForName(long,long)"""
        return int.__wrap(__CoreFoundation.nCFBundleGetFunctionPointerForName(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nCFStringCreateWithCStringNoCopy(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFStringCreateWithCStringNoCopy(long,long,int,long)"""
        return int.__wrap(__CoreFoundation.nCFStringCreateWithCStringNoCopy(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nCFURLCreateWithFileSystemPath(arg0: int, arg1: int, arg2: int, arg3: bool) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFURLCreateWithFileSystemPath(long,long,long,boolean)"""
        return int.__wrap(__CoreFoundation.nCFURLCreateWithFileSystemPath(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CFRelease(arg0: int):
        """public static void org.lwjgl.system.macosx.CoreFoundation.CFRelease(long)"""
        __CoreFoundation.CFRelease(__long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nCFStringCreateWithCString(arg0: int, arg1: int, arg2: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFStringCreateWithCString(long,long,int)"""
        return int.__wrap(__CoreFoundation.nCFStringCreateWithCString(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def CFStringCreateWithCString(arg0: int, arg1: 'ByteBuffer', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFStringCreateWithCString(long,java.nio.ByteBuffer,int)"""
        return int.__wrap(__CoreFoundation.CFStringCreateWithCString(__long.valueOf(arg0), arg1, __int.valueOf(arg2)))

    @staticmethod
    @overload
    def CFStringCreateWithCStringNoCopy(arg0: int, arg1: 'ByteBuffer', arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFStringCreateWithCStringNoCopy(long,java.nio.ByteBuffer,int,long)"""
        return int.__wrap(__CoreFoundation.CFStringCreateWithCStringNoCopy(__long.valueOf(arg0), arg1, __int.valueOf(arg2), __long.valueOf(arg3)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nCFBundleGetBundleWithIdentifier(arg0: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleGetBundleWithIdentifier(long)"""
        return int.__wrap(__CoreFoundation.nCFBundleGetBundleWithIdentifier(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCFRelease(arg0: int):
        """public static native void org.lwjgl.system.macosx.CoreFoundation.nCFRelease(long)"""
        __CoreFoundation.nCFRelease(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def CFBundleGetBundleWithIdentifier(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleGetBundleWithIdentifier(long)"""
        return int.__wrap(__CoreFoundation.CFBundleGetBundleWithIdentifier(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCFBundleCreate(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreFoundation.nCFBundleCreate(long,long)"""
        return int.__wrap(__CoreFoundation.nCFBundleCreate(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def CFURLCreateWithFileSystemPath(arg0: int, arg1: int, arg2: int, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFURLCreateWithFileSystemPath(long,long,long,boolean)"""
        return int.__wrap(__CoreFoundation.CFURLCreateWithFileSystemPath(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CFBundleGetFunctionPointerForName(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleGetFunctionPointerForName(long,long)"""
        return int.__wrap(__CoreFoundation.CFBundleGetFunctionPointerForName(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def CFBundleCreate(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFBundleCreate(long,long)"""
        return int.__wrap(__CoreFoundation.CFBundleCreate(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def CFRetain(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreFoundation.CFRetain(long)"""
        return int.__wrap(__CoreFoundation.CFRetain(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCRuntime$Functions
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
import org.lwjgl.system.macosx.ObjCRuntime as __ObjCRuntime_Functions
__Functions = __ObjCRuntime_Functions.Functions
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.system.macosx.ObjCRuntime.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapCallBack
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.macosx.CGEventTapCallBackI as __CGEventTapCallBackI
__CGEventTapCallBackI = __CGEventTapCallBackI
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import org.lwjgl.system.macosx.CGEventTapCallBack as __CGEventTapCallBack
__CGEventTapCallBack = __CGEventTapCallBack
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CGEventTapCallBack(ABC, pyglsystem.__Callback, pyglsystem.Callback, __CGEventTapCallBackI, CGEventTapCallBackI):
    """org.lwjgl.system.macosx.CGEventTapCallBack"""
 
    @staticmethod
    def __wrap(java_value: __CGEventTapCallBack) -> 'CGEventTapCallBack':
        return CGEventTapCallBack(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CGEventTapCallBack):
        """
        Dynamic initializer for CGEventTapCallBack.
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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.CGEventTapCallBackI.callback(long,long)"""
        super(__CGEventTapCallBackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.CGEventTapCallBackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(CGEventTapCallBackI, self).getCallInterface())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.macosx.CGEventTapCallBackI.invoke(long,int,long,long)"""
        pass

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
    def createSafe(arg0: int) -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.createSafe(long)"""
        return CGEventTapCallBack.__wrap(__CGEventTapCallBack.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.create(long)"""
        return CGEventTapCallBack.__wrap(__CGEventTapCallBack.create(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: 'CGEventTapCallBackI') -> 'CGEventTapCallBack':
        """public static org.lwjgl.system.macosx.CGEventTapCallBack org.lwjgl.system.macosx.CGEventTapCallBack.create(org.lwjgl.system.macosx.CGEventTapCallBackI)"""
        return CGEventTapCallBack.__wrap(__CGEventTapCallBack.create(arg0))

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapInformation$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.macosx.CGEventTapInformation as __CGEventTapInformation_Buffer
__Buffer = __CGEventTapInformation_Buffer.Buffer
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
from builtins import float
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
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.CGEventTapInformation.Buffer"""
 
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.CGEventTapInformation$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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
    def processBeingTapped(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.processBeingTapped()"""
        return int.__wrap(super(Buffer, self).processBeingTapped())

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
        """public org.lwjgl.system.macosx.CGEventTapInformation$Buffer(java.nio.ByteBuffer)"""
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
    def maxUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.maxUsecLatency()"""
        return float.__wrap(super(Buffer, self).maxUsecLatency())

    @overload
    def eventsOfInterest(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.eventsOfInterest()"""
        return int.__wrap(super(Buffer, self).eventsOfInterest())

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
    def tapPoint(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.tapPoint()"""
        return int.__wrap(super(Buffer, self).tapPoint())

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def minUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.minUsecLatency()"""
        return float.__wrap(super(Buffer, self).minUsecLatency())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def options(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.options()"""
        return int.__wrap(super(Buffer, self).options())

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
    def avgUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation$Buffer.avgUsecLatency()"""
        return float.__wrap(super(Buffer, self).avgUsecLatency())

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
    def eventTapID(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation$Buffer.eventTapID()"""
        return int.__wrap(super(Buffer, self).eventTapID())

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
    def enabled(self) -> bool:
        """public boolean org.lwjgl.system.macosx.CGEventTapInformation$Buffer.enabled()"""
        return bool.__wrap(super(Buffer, self).enabled())

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
    def tappingProcess(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation$Buffer.tappingProcess()"""
        return int.__wrap(super(Buffer, self).tappingProcess())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.macosx.EnumerationMutationHandlerI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.system.macosx.EnumerationMutationHandlerI as __EnumerationMutationHandlerI
__EnumerationMutationHandlerI = __EnumerationMutationHandlerI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class EnumerationMutationHandlerI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.system.macosx.EnumerationMutationHandlerI"""
 
    @staticmethod
    def __wrap(java_value: __EnumerationMutationHandlerI) -> 'EnumerationMutationHandlerI':
        return EnumerationMutationHandlerI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EnumerationMutationHandlerI):
        """
        Dynamic initializer for EnumerationMutationHandlerI.
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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.EnumerationMutationHandlerI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(EnumerationMutationHandlerI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.system.macosx.EnumerationMutationHandlerI.invoke(long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.system.macosx.EnumerationMutationHandlerI.callback(long,long)"""
        super(__EnumerationMutationHandlerI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCRuntime
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.macosx.ObjCRuntime as __ObjCRuntime
__ObjCRuntime = __ObjCRuntime
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

import org.lwjgl.system.macosx.ObjCMethodDescription as __ObjCMethodDescription_Buffer
__Buffer = __ObjCMethodDescription_Buffer.Buffer
from builtins import type
import org.lwjgl.system.macosx.ObjCPropertyAttribute as __ObjCPropertyAttribute_Buffer
__Buffer = __ObjCPropertyAttribute_Buffer.Buffer
import org.lwjgl.system.macosx.ObjCMethodDescription as __ObjCMethodDescription
__ObjCMethodDescription = __ObjCMethodDescription
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
import java.lang.Byte as __byte
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import bool
from builtins import int
 
class ObjCRuntime():
    """org.lwjgl.system.macosx.ObjCRuntime"""
 
    @staticmethod
    def __wrap(java_value: __ObjCRuntime) -> 'ObjCRuntime':
        return ObjCRuntime(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjCRuntime):
        """
        Dynamic initializer for ObjCRuntime.
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
    def objc_getClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getClass(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_getClass(arg0))

    @staticmethod
    @overload
    def nclass_getInstanceVariable(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getInstanceVariable(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_getInstanceVariable(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def method_setImplementation(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_setImplementation(long,long)"""
        return int.__wrap(__ObjCRuntime.method_setImplementation(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getName(long)"""
        return int.__wrap(__ObjCRuntime.nclass_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_registerName(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_registerName(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.sel_registerName(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def objc_lookUpClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_lookUpClass(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_lookUpClass(arg0))

    @staticmethod
    @overload
    def class_getClassVariable(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassVariable(long,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.class_getClassVariable(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def protocol_conformsToProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.protocol_conformsToProtocol(long,long)"""
        return bool.__wrap(__ObjCRuntime.protocol_conformsToProtocol(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nsel_getUid(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_getUid(long)"""
        return int.__wrap(__ObjCRuntime.nsel_getUid(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_addProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer,boolean,boolean)"""
        __ObjCRuntime.protocol_addProperty(__long.valueOf(arg0), arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def nclass_getProperty(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getProperty(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_getProperty(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobjc_copyClassList(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyClassList(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_copyClassList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getInstanceMethod(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceMethod(long,long)"""
        return int.__wrap(__ObjCRuntime.class_getInstanceMethod(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nmethod_copyArgumentType(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_copyArgumentType(long,int)"""
        return int.__wrap(__ObjCRuntime.nmethod_copyArgumentType(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nobjc_getMetaClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getMetaClass(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_getMetaClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmethod_getReturnType(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nmethod_getReturnType(long,long,long)"""
        __ObjCRuntime.nmethod_getReturnType(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def class_setVersion(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setVersion(long,int)"""
        __ObjCRuntime.class_setVersion(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def objc_getClassList(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.objc_getClassList(org.lwjgl.PointerBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_getClassList(arg0))

    @staticmethod
    @overload
    def object_getClassName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.object_getClassName(long)"""
        return str.__wrap(__ObjCRuntime.object_getClassName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_loadWeak(arg0: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_loadWeak(org.lwjgl.PointerBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_loadWeak(arg0))

    @staticmethod
    @overload
    def nprotocol_copyPropertyList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyPropertyList(long,long)"""
        return int.__wrap(__ObjCRuntime.nprotocol_copyPropertyList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_copyImageNames() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyImageNames()"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.objc_copyImageNames())

    @staticmethod
    @overload
    def class_setIvarLayout(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setIvarLayout(long,java.nio.ByteBuffer)"""
        __ObjCRuntime.class_setIvarLayout(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nobjc_constructInstance(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_constructInstance(long,long)"""
        return int.__wrap(__ObjCRuntime.nobjc_constructInstance(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def method_getReturnType(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_getReturnType(long,java.nio.ByteBuffer)"""
        __ObjCRuntime.method_getReturnType(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def property_getAttributes(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_getAttributes(long)"""
        return str.__wrap(__ObjCRuntime.property_getAttributes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_setAssociatedObject(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_setAssociatedObject(long,long,long,long)"""
        __ObjCRuntime.objc_setAssociatedObject(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @staticmethod
    @overload
    def class_getSuperclass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getSuperclass(long)"""
        return int.__wrap(__ObjCRuntime.class_getSuperclass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_copyProtocolList(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyProtocolList(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_copyProtocolList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_replaceMethod(long,long,long,java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.class_replaceMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def class_respondsToSelector(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_respondsToSelector(long,long)"""
        return bool.__wrap(__ObjCRuntime.class_respondsToSelector(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_getProperty(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getProperty(long,java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.class_getProperty(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def objc_registerClassPair(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_registerClassPair(long)"""
        __ObjCRuntime.objc_registerClassPair(__long.valueOf(arg0))

    @staticmethod
    @overload
    def method_getTypeEncoding(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getTypeEncoding(long)"""
        return str.__wrap(__ObjCRuntime.method_getTypeEncoding(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_copyClassList() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassList()"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.objc_copyClassList())

    @staticmethod
    @overload
    def method_getImplementation(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_getImplementation(long)"""
        return int.__wrap(__ObjCRuntime.method_getImplementation(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getClassVariable(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassVariable(long,java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.class_getClassVariable(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def protocol_isEqual(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.protocol_isEqual(long,long)"""
        return bool.__wrap(__ObjCRuntime.protocol_isEqual(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def imp_getBlock(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.imp_getBlock(long)"""
        return int.__wrap(__ObjCRuntime.imp_getBlock(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_conformsToProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_conformsToProtocol(long,long)"""
        return bool.__wrap(__ObjCRuntime.class_conformsToProtocol(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nmethod_getArgumentType(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nmethod_getArgumentType(long,int,long,long)"""
        __ObjCRuntime.nmethod_getArgumentType(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nprotocol_addProperty(arg0: int, arg1: int, arg2: int, arg3: int, arg4: bool, arg5: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_addProperty(long,long,long,int,boolean,boolean)"""
        __ObjCRuntime.nprotocol_addProperty(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5))

    @staticmethod
    @overload
    def method_getArgumentType(arg0: int, arg1: int, arg2: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getArgumentType(long,int,long)"""
        return str.__wrap(__ObjCRuntime.method_getArgumentType(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def objc_getAssociatedObject(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getAssociatedObject(long,long)"""
        return int.__wrap(__ObjCRuntime.objc_getAssociatedObject(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def imp_removeBlock(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.imp_removeBlock(long)"""
        return bool.__wrap(__ObjCRuntime.imp_removeBlock(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_getIvar(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getIvar(long,long)"""
        return int.__wrap(__ObjCRuntime.object_getIvar(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def protocol_copyProtocolList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyProtocolList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.protocol_copyProtocolList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_isEqual(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.sel_isEqual(long,long)"""
        return bool.__wrap(__ObjCRuntime.sel_isEqual(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_getImageName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getImageName(long)"""
        return int.__wrap(__ObjCRuntime.nclass_getImageName(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def class_addMethod(arg0: int, arg1: int, arg2: int, arg3: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addMethod(long,long,long,java.lang.CharSequence)"""
        return bool.__wrap(__ObjCRuntime.class_addMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def protocol_addProtocol(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProtocol(long,long)"""
        __ObjCRuntime.protocol_addProtocol(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nmethod_getTypeEncoding(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_getTypeEncoding(long)"""
        return int.__wrap(__ObjCRuntime.nmethod_getTypeEncoding(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_replaceMethod(long,long,long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_replaceMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def object_setClass(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setClass(long,long)"""
        return int.__wrap(__ObjCRuntime.object_setClass(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_setWeakIvarLayout(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setWeakIvarLayout(long,java.nio.ByteBuffer)"""
        __ObjCRuntime.class_setWeakIvarLayout(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def ivar_getOffset(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.ivar_getOffset(long)"""
        return int.__wrap(__ObjCRuntime.ivar_getOffset(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getRequiredClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getRequiredClass(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_getRequiredClass(arg0))

    @staticmethod
    @overload
    def sel_getUid(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_getUid(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.sel_getUid(arg0))

    @staticmethod
    @overload
    def objc_allocateProtocol(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateProtocol(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_allocateProtocol(arg0))

    @staticmethod
    @overload
    def nprotocol_addMethodDescription(arg0: int, arg1: int, arg2: int, arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_addMethodDescription(long,long,long,boolean,boolean)"""
        __ObjCRuntime.nprotocol_addMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def class_setWeakIvarLayout(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setWeakIvarLayout(long,java.lang.CharSequence)"""
        __ObjCRuntime.class_setWeakIvarLayout(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def object_dispose(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_dispose(long)"""
        return int.__wrap(__ObjCRuntime.object_dispose(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_replaceProperty(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_replaceProperty(long,long,long,int)"""
        __ObjCRuntime.nclass_replaceProperty(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def sel_registerName(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_registerName(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.sel_registerName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def object_setInstanceVariable(arg0: int, arg1: 'CharSequence', arg2: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setInstanceVariable(long,java.lang.CharSequence,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.object_setInstanceVariable(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def class_getInstanceVariable(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceVariable(long,java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.class_getInstanceVariable(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_getVersion(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.class_getVersion(long)"""
        return int.__wrap(__ObjCRuntime.class_getVersion(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_registerProtocol(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_registerProtocol(long)"""
        __ObjCRuntime.objc_registerProtocol(__long.valueOf(arg0))

    @staticmethod
    @overload
    def class_getImageName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getImageName(long)"""
        return str.__wrap(__ObjCRuntime.class_getImageName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_copyMethodDescriptionList(arg0: int, arg1: bool, arg2: bool, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyMethodDescriptionList(long,boolean,boolean,long)"""
        return int.__wrap(__ObjCRuntime.nprotocol_copyMethodDescriptionList(__long.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def objc_copyClassNamesForImage(arg0: 'CharSequence') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassNamesForImage(java.lang.CharSequence)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.objc_copyClassNamesForImage(arg0))

    @staticmethod
    @overload
    def sel_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.sel_getName(long)"""
        return str.__wrap(__ObjCRuntime.sel_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.protocol_getName(long)"""
        return str.__wrap(__ObjCRuntime.protocol_getName(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def objc_allocateProtocol(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateProtocol(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_allocateProtocol(arg0))

    @staticmethod
    @overload
    def class_replaceProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_replaceProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        __ObjCRuntime.class_replaceProperty(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nobjc_loadWeak(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_loadWeak(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_loadWeak(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_allocateClassPair(arg0: int, arg1: 'CharSequence', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateClassPair(long,java.lang.CharSequence,long)"""
        return int.__wrap(__ObjCRuntime.objc_allocateClassPair(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def class_getWeakIvarLayout(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getWeakIvarLayout(long)"""
        return str.__wrap(__ObjCRuntime.class_getWeakIvarLayout(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_setInstanceVariable(arg0: int, arg1: 'ByteBuffer', arg2: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_setInstanceVariable(long,java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.object_setInstanceVariable(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def class_replaceProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_replaceProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        __ObjCRuntime.class_replaceProperty(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nprotocol_getProperty(arg0: int, arg1: int, arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getProperty(long,long,boolean,boolean)"""
        return int.__wrap(__ObjCRuntime.nprotocol_getProperty(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def nclass_addMethod(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addMethod(long,long,long,long)"""
        return bool.__wrap(__ObjCRuntime.nclass_addMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3)))

    @staticmethod
    @overload
    def nprotocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int, arg5: int):
        """public static native void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getMethodDescription(long,long,boolean,boolean,long,long)"""
        __ObjCRuntime.nprotocol_getMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5))

    @staticmethod
    @overload
    def nclass_getClassVariable(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getClassVariable(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_getClassVariable(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_getMethodImplementation(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getMethodImplementation(long,long)"""
        return int.__wrap(__ObjCRuntime.class_getMethodImplementation(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nprotocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getMethodDescription(long,long,boolean,boolean,long)"""
        __ObjCRuntime.nprotocol_getMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def class_getProperty(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getProperty(long,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.class_getProperty(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nproperty_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_getName(long)"""
        return int.__wrap(__ObjCRuntime.nproperty_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getProtocol(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getProtocol(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_getProtocol(arg0))

    @staticmethod
    @overload
    def nobjc_allocateClassPair(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_allocateClassPair(long,long,long)"""
        return int.__wrap(__ObjCRuntime.nobjc_allocateClassPair(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def objc_setEnumerationMutationHandler(arg0: 'EnumerationMutationHandlerI'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_setEnumerationMutationHandler(org.lwjgl.system.macosx.EnumerationMutationHandlerI)"""
        __ObjCRuntime.objc_setEnumerationMutationHandler(arg0)

    @staticmethod
    @overload
    def objc_getClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getClass(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_getClass(arg0))

    @staticmethod
    @overload
    def class_getInstanceSize(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceSize(long)"""
        return int.__wrap(__ObjCRuntime.class_getInstanceSize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_getRequiredClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getRequiredClass(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_getRequiredClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_storeWeak(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_storeWeak(long,long)"""
        return int.__wrap(__ObjCRuntime.nobjc_storeWeak(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobjc_copyImageNames(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyImageNames(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_copyImageNames(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_getClassList(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.nobjc_getClassList(long,int)"""
        return int.__wrap(__ObjCRuntime.nobjc_getClassList(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def class_addProtocol(arg0: int, arg1: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProtocol(long,long)"""
        return bool.__wrap(__ObjCRuntime.class_addProtocol(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_destructInstance(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_destructInstance(long)"""
        return int.__wrap(__ObjCRuntime.objc_destructInstance(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def property_copyAttributeValue(arg0: int, arg1: 'ByteBuffer') -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeValue(long,java.nio.ByteBuffer)"""
        return str.__wrap(__ObjCRuntime.property_copyAttributeValue(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def objc_disposeClassPair(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_disposeClassPair(long)"""
        __ObjCRuntime.objc_disposeClassPair(__long.valueOf(arg0))

    @staticmethod
    @overload
    def protocol_getProperty(arg0: int, arg1: 'ByteBuffer', arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.protocol_getProperty(long,java.nio.ByteBuffer,boolean,boolean)"""
        return int.__wrap(__ObjCRuntime.protocol_getProperty(__long.valueOf(arg0), arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def nclass_addProperty(arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addProperty(long,long,long,int)"""
        return bool.__wrap(__ObjCRuntime.nclass_addProperty(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def method_getNumberOfArguments(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.ObjCRuntime.method_getNumberOfArguments(long)"""
        return int.__wrap(__ObjCRuntime.method_getNumberOfArguments(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_setIvar(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.object_setIvar(long,long,long)"""
        __ObjCRuntime.object_setIvar(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def nproperty_copyAttributeValue(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_copyAttributeValue(long,long)"""
        return int.__wrap(__ObjCRuntime.nproperty_copyAttributeValue(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def protocol_addProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer,boolean,boolean)"""
        __ObjCRuntime.protocol_addProperty(__long.valueOf(arg0), arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def protocol_addMethodDescription(arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addMethodDescription(long,long,java.nio.ByteBuffer,boolean,boolean)"""
        __ObjCRuntime.protocol_addMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def protocol_copyMethodDescriptionList(arg0: int, arg1: bool, arg2: bool) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyMethodDescriptionList(long,boolean,boolean)"""
        return Buffer.__wrap(__ObjCRuntime.protocol_copyMethodDescriptionList(__long.valueOf(arg0), __boolean.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def protocol_getProperty(arg0: int, arg1: 'CharSequence', arg2: bool, arg3: bool) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.protocol_getProperty(long,java.lang.CharSequence,boolean,boolean)"""
        return int.__wrap(__ObjCRuntime.protocol_getProperty(__long.valueOf(arg0), arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def nobjc_lookUpClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_lookUpClass(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_lookUpClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def method_exchangeImplementations(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_exchangeImplementations(long,long)"""
        __ObjCRuntime.method_exchangeImplementations(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nmethod_copyReturnType(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nmethod_copyReturnType(long)"""
        return int.__wrap(__ObjCRuntime.nmethod_copyReturnType(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_lookUpClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_lookUpClass(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_lookUpClass(arg0))

    @staticmethod
    @overload
    def class_createInstance(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_createInstance(long,long)"""
        return int.__wrap(__ObjCRuntime.class_createInstance(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def object_getInstanceVariable(arg0: int, arg1: 'CharSequence', arg2: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getInstanceVariable(long,java.lang.CharSequence,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__ObjCRuntime.object_getInstanceVariable(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def object_getClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getClass(long)"""
        return int.__wrap(__ObjCRuntime.object_getClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_copyMethodList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyMethodList(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_copyMethodList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nclass_setIvarLayout(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_setIvarLayout(long,long)"""
        __ObjCRuntime.nclass_setIvarLayout(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def class_addMethod(arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addMethod(long,long,long,java.nio.ByteBuffer)"""
        return bool.__wrap(__ObjCRuntime.class_addMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def objc_storeWeak(arg0: 'PointerBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_storeWeak(org.lwjgl.PointerBuffer,long)"""
        return int.__wrap(__ObjCRuntime.objc_storeWeak(arg0, __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobject_getInstanceVariable(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_getInstanceVariable(long,long,long)"""
        return int.__wrap(__ObjCRuntime.nobject_getInstanceVariable(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def objc_removeAssociatedObjects(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_removeAssociatedObjects(long)"""
        __ObjCRuntime.objc_removeAssociatedObjects(__long.valueOf(arg0))

    @staticmethod
    @overload
    def protocol_copyPropertyList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.protocol_copyPropertyList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.protocol_copyPropertyList(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nobjc_copyClassNamesForImage(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_copyClassNamesForImage(long,long)"""
        return int.__wrap(__ObjCRuntime.nobjc_copyClassNamesForImage(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def objc_getMetaClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getMetaClass(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_getMetaClass(arg0))

    @staticmethod
    @overload
    def nobjc_setEnumerationMutationHandler(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nobjc_setEnumerationMutationHandler(long)"""
        __ObjCRuntime.nobjc_setEnumerationMutationHandler(__long.valueOf(arg0))

    @staticmethod
    @overload
    def class_addProperty(arg0: int, arg1: 'CharSequence', arg2: 'Buffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProperty(long,java.lang.CharSequence,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        return bool.__wrap(__ObjCRuntime.class_addProperty(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def protocol_getMethodDescription(arg0: int, arg1: int, arg2: bool, arg3: bool, arg4: 'ObjCMethodDescription') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCRuntime.protocol_getMethodDescription(long,long,boolean,boolean,org.lwjgl.system.macosx.ObjCMethodDescription)"""
        return ObjCMethodDescription.__wrap(__ObjCRuntime.protocol_getMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def method_getReturnType(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_getReturnType(long,long)"""
        return str.__wrap(__ObjCRuntime.method_getReturnType(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobject_setInstanceVariable(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_setInstanceVariable(long,long,long)"""
        return int.__wrap(__ObjCRuntime.nobject_setInstanceVariable(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def property_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_getName(long)"""
        return str.__wrap(__ObjCRuntime.property_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def method_copyReturnType(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_copyReturnType(long)"""
        return str.__wrap(__ObjCRuntime.method_copyReturnType(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nprotocol_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_getName(long)"""
        return int.__wrap(__ObjCRuntime.nprotocol_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getName(long)"""
        return str.__wrap(__ObjCRuntime.class_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getInstanceVariable(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getInstanceVariable(long,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.class_getInstanceVariable(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def method_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.method_getName(long)"""
        return int.__wrap(__ObjCRuntime.method_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getRequiredClass(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getRequiredClass(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.objc_getRequiredClass(arg0))

    @staticmethod
    @overload
    def class_getIvarLayout(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.class_getIvarLayout(long)"""
        return str.__wrap(__ObjCRuntime.class_getIvarLayout(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ivar_getTypeEncoding(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.ivar_getTypeEncoding(long)"""
        return str.__wrap(__ObjCRuntime.ivar_getTypeEncoding(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_getClassMethod(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_getClassMethod(long,long)"""
        return int.__wrap(__ObjCRuntime.class_getClassMethod(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_copyIvarList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyIvarList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.class_copyIvarList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_getIvarLayout(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getIvarLayout(long)"""
        return int.__wrap(__ObjCRuntime.nclass_getIvarLayout(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def protocol_addMethodDescription(arg0: int, arg1: int, arg2: 'CharSequence', arg3: bool, arg4: bool):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.protocol_addMethodDescription(long,long,java.lang.CharSequence,boolean,boolean)"""
        __ObjCRuntime.protocol_addMethodDescription(__long.valueOf(arg0), __long.valueOf(arg1), arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @staticmethod
    @overload
    def ivar_getName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.ivar_getName(long)"""
        return str.__wrap(__ObjCRuntime.ivar_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobjc_allocateProtocol(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_allocateProtocol(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_allocateProtocol(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_setIvarLayout(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.class_setIvarLayout(long,java.lang.CharSequence)"""
        __ObjCRuntime.class_setIvarLayout(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.ObjCRuntime.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__ObjCRuntime.getLibrary())

    @staticmethod
    @overload
    def class_replaceMethod(arg0: int, arg1: int, arg2: int, arg3: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.class_replaceMethod(long,long,long,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.class_replaceMethod(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def class_addIvar(arg0: int, arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addIvar(long,java.lang.CharSequence,long,byte,java.lang.CharSequence)"""
        return bool.__wrap(__ObjCRuntime.class_addIvar(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __byte.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def objc_constructInstance(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_constructInstance(long,java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_constructInstance(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def class_copyPropertyList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyPropertyList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.class_copyPropertyList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_enumerationMutation(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.objc_enumerationMutation(long)"""
        __ObjCRuntime.objc_enumerationMutation(__long.valueOf(arg0))

    @staticmethod
    @overload
    def method_getArgumentType(arg0: int, arg1: int, arg2: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.method_getArgumentType(long,int,java.nio.ByteBuffer)"""
        __ObjCRuntime.method_getArgumentType(__long.valueOf(arg0), __int.valueOf(arg1), arg2)

    @staticmethod
    @overload
    def nsel_registerName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_registerName(long)"""
        return int.__wrap(__ObjCRuntime.nsel_registerName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def class_isMetaClass(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_isMetaClass(long)"""
        return bool.__wrap(__ObjCRuntime.class_isMetaClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def property_copyAttributeValue(arg0: int, arg1: 'CharSequence') -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeValue(long,java.lang.CharSequence)"""
        return str.__wrap(__ObjCRuntime.property_copyAttributeValue(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nprotocol_copyProtocolList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nprotocol_copyProtocolList(long,long)"""
        return int.__wrap(__ObjCRuntime.nprotocol_copyProtocolList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nproperty_getAttributes(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_getAttributes(long)"""
        return int.__wrap(__ObjCRuntime.nproperty_getAttributes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def imp_implementationWithBlock(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.imp_implementationWithBlock(long)"""
        return int.__wrap(__ObjCRuntime.imp_implementationWithBlock(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def property_copyAttributeList(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCRuntime.property_copyAttributeList(long)"""
        return Buffer.__wrap(__ObjCRuntime.property_copyAttributeList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_copyPropertyList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyPropertyList(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_copyPropertyList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_copyMethodList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyMethodList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.class_copyMethodList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_getIndexedIvars(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getIndexedIvars(long)"""
        return int.__wrap(__ObjCRuntime.object_getIndexedIvars(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_copyProtocolList() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyProtocolList()"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.objc_copyProtocolList())

    @staticmethod
    @overload
    def object_getInstanceVariable(arg0: int, arg1: 'ByteBuffer', arg2: 'PointerBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_getInstanceVariable(long,java.nio.ByteBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__ObjCRuntime.object_getInstanceVariable(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nivar_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nivar_getName(long)"""
        return int.__wrap(__ObjCRuntime.nivar_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nobject_getClassName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobject_getClassName(long)"""
        return int.__wrap(__ObjCRuntime.nobject_getClassName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_copyIvarList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyIvarList(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_copyIvarList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def objc_copyClassNamesForImage(arg0: 'ByteBuffer') -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.objc_copyClassNamesForImage(java.nio.ByteBuffer)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.objc_copyClassNamesForImage(arg0))

    @staticmethod
    @overload
    def objc_getMetaClass(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getMetaClass(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_getMetaClass(arg0))

    @staticmethod
    @overload
    def class_addProperty(arg0: int, arg1: 'ByteBuffer', arg2: 'Buffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addProperty(long,java.nio.ByteBuffer,org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer)"""
        return bool.__wrap(__ObjCRuntime.class_addProperty(__long.valueOf(arg0), arg1, arg2))

    @staticmethod
    @overload
    def nsel_getName(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nsel_getName(long)"""
        return int.__wrap(__ObjCRuntime.nsel_getName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_getProtocol(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_getProtocol(java.nio.ByteBuffer)"""
        return int.__wrap(__ObjCRuntime.objc_getProtocol(arg0))

    @staticmethod
    @overload
    def nobjc_getClass(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getClass(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_getClass(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def object_copy(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.object_copy(long,long)"""
        return int.__wrap(__ObjCRuntime.object_copy(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nobjc_getProtocol(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nobjc_getProtocol(long)"""
        return int.__wrap(__ObjCRuntime.nobjc_getProtocol(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def objc_allocateClassPair(arg0: int, arg1: 'ByteBuffer', arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.objc_allocateClassPair(long,java.nio.ByteBuffer,long)"""
        return int.__wrap(__ObjCRuntime.objc_allocateClassPair(__long.valueOf(arg0), arg1, __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nproperty_copyAttributeList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nproperty_copyAttributeList(long,long)"""
        return int.__wrap(__ObjCRuntime.nproperty_copyAttributeList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nclass_addIvar(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.nclass_addIvar(long,long,long,byte,long)"""
        return bool.__wrap(__ObjCRuntime.nclass_addIvar(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __byte.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nclass_setWeakIvarLayout(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.ObjCRuntime.nclass_setWeakIvarLayout(long,long)"""
        __ObjCRuntime.nclass_setWeakIvarLayout(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nclass_copyProtocolList(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_copyProtocolList(long,long)"""
        return int.__wrap(__ObjCRuntime.nclass_copyProtocolList(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def class_addIvar(arg0: int, arg1: 'ByteBuffer', arg2: int, arg3: int, arg4: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.system.macosx.ObjCRuntime.class_addIvar(long,java.nio.ByteBuffer,long,byte,java.nio.ByteBuffer)"""
        return bool.__wrap(__ObjCRuntime.class_addIvar(__long.valueOf(arg0), arg1, __long.valueOf(arg2), __byte.valueOf(arg3), arg4))

    @staticmethod
    @overload
    def class_copyProtocolList(arg0: int) -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.system.macosx.ObjCRuntime.class_copyProtocolList(long)"""
        return pygl.PointerBuffer.__wrap(__ObjCRuntime.class_copyProtocolList(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nclass_getWeakIvarLayout(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nclass_getWeakIvarLayout(long)"""
        return int.__wrap(__ObjCRuntime.nclass_getWeakIvarLayout(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nivar_getTypeEncoding(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.nivar_getTypeEncoding(long)"""
        return int.__wrap(__ObjCRuntime.nivar_getTypeEncoding(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def sel_getUid(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.ObjCRuntime.sel_getUid(java.lang.CharSequence)"""
        return int.__wrap(__ObjCRuntime.sel_getUid(arg0))

    @staticmethod
    @overload
    def method_copyArgumentType(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCRuntime.method_copyArgumentType(long,int)"""
        return str.__wrap(__ObjCRuntime.method_copyArgumentType(__long.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.macosx.DynamicLinkLoader
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
import org.lwjgl.system.macosx.DynamicLinkLoader as __DynamicLinkLoader
__DynamicLinkLoader = __DynamicLinkLoader
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class DynamicLinkLoader():
    """org.lwjgl.system.macosx.DynamicLinkLoader"""
 
    @staticmethod
    def __wrap(java_value: __DynamicLinkLoader) -> 'DynamicLinkLoader':
        return DynamicLinkLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicLinkLoader):
        """
        Dynamic initializer for DynamicLinkLoader.
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
    def dlclose(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.DynamicLinkLoader.dlclose(long)"""
        return int.__wrap(__DynamicLinkLoader.dlclose(__long.valueOf(arg0)))

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
    def dlopen(arg0: 'CharSequence', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlopen(java.lang.CharSequence,int)"""
        return int.__wrap(__DynamicLinkLoader.dlopen(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndlclose(arg0: int) -> int:
        """public static native int org.lwjgl.system.macosx.DynamicLinkLoader.ndlclose(long)"""
        return int.__wrap(__DynamicLinkLoader.ndlclose(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def dlopen(arg0: 'ByteBuffer', arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlopen(java.nio.ByteBuffer,int)"""
        return int.__wrap(__DynamicLinkLoader.dlopen(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def ndlerror() -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlerror()"""
        return int.__wrap(__DynamicLinkLoader.ndlerror())

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
    def dlerror() -> str:
        """public static java.lang.String org.lwjgl.system.macosx.DynamicLinkLoader.dlerror()"""
        return str.__wrap(__DynamicLinkLoader.dlerror())

    @staticmethod
    @overload
    def dlsym(arg0: int, arg1: 'ByteBuffer') -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlsym(long,java.nio.ByteBuffer)"""
        return int.__wrap(__DynamicLinkLoader.dlsym(__long.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ndlsym(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlsym(long,long)"""
        return int.__wrap(__DynamicLinkLoader.ndlsym(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def dlsym(arg0: int, arg1: 'CharSequence') -> int:
        """public static long org.lwjgl.system.macosx.DynamicLinkLoader.dlsym(long,java.lang.CharSequence)"""
        return int.__wrap(__DynamicLinkLoader.dlsym(__long.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def ndlopen(arg0: int, arg1: int) -> int:
        """public static native long org.lwjgl.system.macosx.DynamicLinkLoader.ndlopen(long,int)"""
        return int.__wrap(__DynamicLinkLoader.ndlopen(__long.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibraryDL
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
import org.lwjgl.system.macosx.MacOSXLibrary as __MacOSXLibrary
__MacOSXLibrary = __MacOSXLibrary
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
import org.lwjgl.system.macosx.MacOSXLibraryDL as __MacOSXLibraryDL
__MacOSXLibraryDL = __MacOSXLibraryDL
from builtins import bool
from builtins import int
 
class MacOSXLibraryDL(__MacOSXLibrary, MacOSXLibrary):
    """org.lwjgl.system.macosx.MacOSXLibraryDL"""
 
    @staticmethod
    def __wrap(java_value: __MacOSXLibraryDL) -> 'MacOSXLibraryDL':
        return MacOSXLibraryDL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MacOSXLibraryDL):
        """
        Dynamic initializer for MacOSXLibraryDL.
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
    def getPath(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.MacOSXLibraryDL.getPath()"""
        return str.__wrap(super(MacOSXLibraryDL, self).getPath())

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

    @overload
    def __init__(self, arg0: str):
        """public org.lwjgl.system.macosx.MacOSXLibraryDL(java.lang.String)"""
        val = __MacOSXLibraryDL(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

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

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.macosx.MacOSXLibraryDL.free()"""
        super(MacOSXLibraryDL, self).free()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.create(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.getWithIdentifier(arg0))

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
    def __init__(self, arg0: str, arg1: int):
        """public org.lwjgl.system.macosx.MacOSXLibraryDL(java.lang.String,long)"""
        val = __MacOSXLibraryDL(arg0, __long.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFunctionAddress(self, arg0: 'ByteBuffer') -> int:
        """public long org.lwjgl.system.macosx.MacOSXLibraryDL.getFunctionAddress(java.nio.ByteBuffer)"""
        return int.__wrap(super(__MacOSXLibraryDL, self).getFunctionAddress(arg0)) 
 
 
# CLASS: org.lwjgl.system.macosx.CGPoint$Buffer
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
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import float
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
import org.lwjgl.system.macosx.CGPoint as __CGPoint_Buffer
__Buffer = __CGPoint_Buffer.Buffer
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.CGPoint.Buffer"""
 
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
    def x(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint$Buffer.x()"""
        return float.__wrap(super(Buffer, self).x())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGPoint$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.CGPoint$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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

    @overload
    def y(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint$Buffer.y()"""
        return float.__wrap(super(Buffer, self).y())

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

    @overload
    def x(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint$Buffer.x(double)"""
        return 'Buffer'.__wrap(super(__Buffer, self).x(__double.valueOf(arg0)))

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
    def y(self, arg0: float) -> 'Buffer':
        """public org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint$Buffer.y(double)"""
        return 'Buffer'.__wrap(super(__Buffer, self).y(__double.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.system.macosx.LibSystem
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.macosx.LibSystem as __LibSystem
__LibSystem = __LibSystem
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
 
class LibSystem():
    """org.lwjgl.system.macosx.LibSystem"""
 
    @staticmethod
    def __wrap(java_value: __LibSystem) -> 'LibSystem':
        return LibSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LibSystem):
        """
        Dynamic initializer for LibSystem.
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
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.LibSystem.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__LibSystem.getLibrary())

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
 
 
# CLASS: org.lwjgl.system.macosx.MacOSXLibrary
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
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.lwjgl.system.macosx.MacOSXLibrary as __MacOSXLibrary
__MacOSXLibrary = __MacOSXLibrary
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
 
class MacOSXLibrary(ABC, pyglsystem.__SharedLibrary_Default, pyglsystem.SharedLibrary$Default):
    """org.lwjgl.system.macosx.MacOSXLibrary"""
 
    @staticmethod
    def __wrap(java_value: __MacOSXLibrary) -> 'MacOSXLibrary':
        return MacOSXLibrary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MacOSXLibrary):
        """
        Dynamic initializer for MacOSXLibrary.
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

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.create(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.create(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getWithIdentifier(arg0: str) -> 'MacOSXLibrary':
        """public static org.lwjgl.system.macosx.MacOSXLibrary org.lwjgl.system.macosx.MacOSXLibrary.getWithIdentifier(java.lang.String)"""
        return MacOSXLibrary.__wrap(__MacOSXLibrary.getWithIdentifier(arg0))

    @overload
    def getFunctionAddress(self, arg0: 'CharSequence') -> int:
        """public default long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.lang.CharSequence)"""
        return int.__wrap(super(__pyglsystem.FunctionProvider, self).getFunctionAddress(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def getPath(self, ):
        """public abstract java.lang.String org.lwjgl.system.SharedLibrary.getPath()"""
        pass

    @abstractmethod
    def free(self, ):
        """public abstract void org.lwjgl.system.NativeResource.free()"""
        pass

    @abstractmethod
    def getFunctionAddress(self, arg0: 'ByteBuffer'):
        """public abstract long org.lwjgl.system.FunctionProvider.getFunctionAddress(java.nio.ByteBuffer)"""
        pass 
 
 
# CLASS: org.lwjgl.system.macosx.CoreGraphics
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

import java.nio.IntBuffer as IntBuffer
from builtins import type
import org.lwjgl.system.macosx.CGPoint as __CGPoint
__CGPoint = __CGPoint
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.ShortBuffer as ShortBuffer
import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Short as __short
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Double as __double
import org.lwjgl.system.macosx.CoreGraphics as __CoreGraphics
__CoreGraphics = __CoreGraphics
from builtins import bool
from builtins import int
 
class CoreGraphics():
    """org.lwjgl.system.macosx.CoreGraphics"""
 
    @staticmethod
    def __wrap(java_value: __CoreGraphics) -> 'CoreGraphics':
        return CoreGraphics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CoreGraphics):
        """
        Dynamic initializer for CoreGraphics.
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
    def CGEventCreateScrollWheelEvent(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent(long,int,int,int)"""
        return int.__wrap(__CoreGraphics.CGEventCreateScrollWheelEvent(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def CGEventCreateSourceFromEvent(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateSourceFromEvent(long)"""
        return int.__wrap(__CoreGraphics.CGEventCreateSourceFromEvent(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventGetLocation(arg0: int, arg1: 'CGPoint') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CoreGraphics.CGEventGetLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        return CGPoint.__wrap(__CoreGraphics.CGEventGetLocation(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def CGEventKeyboardSetUnicodeString(arg0: int, arg1: 'short'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardSetUnicodeString(long,short[])"""
        __CoreGraphics.CGEventKeyboardSetUnicodeString(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def CGEventCreateFromData(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateFromData(long,long)"""
        return int.__wrap(__CoreGraphics.CGEventCreateFromData(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventSetLocation(arg0: int, arg1: 'CGPoint'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        __CoreGraphics.CGEventSetLocation(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def CGEventSetType(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetType(long,int)"""
        __CoreGraphics.CGEventSetType(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def CGEventGetDoubleValueField(arg0: int, arg1: int) -> float:
        """public static double org.lwjgl.system.macosx.CoreGraphics.CGEventGetDoubleValueField(long,int)"""
        return float.__wrap(__CoreGraphics.CGEventGetDoubleValueField(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventGetIntegerValueField(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetIntegerValueField(long,int)"""
        return int.__wrap(__CoreGraphics.CGEventGetIntegerValueField(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventSetFlags(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetFlags(long,long)"""
        __CoreGraphics.CGEventSetFlags(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventGetLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetLocation(long,long)"""
        __CoreGraphics.nCGEventGetLocation(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventKeyboardSetUnicodeString(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventKeyboardSetUnicodeString(long,long,long)"""
        __CoreGraphics.nCGEventKeyboardSetUnicodeString(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventPostToPid(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventPostToPid(long,long)"""
        __CoreGraphics.CGEventPostToPid(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventTapCreate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventTapCreate(int,int,int,long,long,long)"""
        return int.__wrap(__CoreGraphics.nCGEventTapCreate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nCGEventGetUnflippedLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetUnflippedLocation(long,long,long)"""
        __CoreGraphics.nCGEventGetUnflippedLocation(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventGetTypeID() -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetTypeID()"""
        return int.__wrap(__CoreGraphics.CGEventGetTypeID())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nCGEventTapCreateForPid(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventTapCreateForPid(long,int,int,long,long,long)"""
        return int.__wrap(__CoreGraphics.nCGEventTapCreateForPid(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4), __long.valueOf(arg5)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def CGEventTapIsEnabled(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.CoreGraphics.CGEventTapIsEnabled(long)"""
        return bool.__wrap(__CoreGraphics.CGEventTapIsEnabled(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventCreateScrollWheelEvent2(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent2(long,int,int,int,int,int)"""
        return int.__wrap(__CoreGraphics.CGEventCreateScrollWheelEvent2(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.system.macosx.CoreGraphics.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__CoreGraphics.getLibrary())

    @staticmethod
    @overload
    def CGEventGetUnflippedLocation(arg0: int, arg1: 'CGPoint') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CoreGraphics.CGEventGetUnflippedLocation(long,org.lwjgl.system.macosx.CGPoint)"""
        return CGPoint.__wrap(__CoreGraphics.CGEventGetUnflippedLocation(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def CGEventTapCreateForPid(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'CGEventTapCallBackI', arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventTapCreateForPid(long,int,int,long,org.lwjgl.system.macosx.CGEventTapCallBackI,long)"""
        return int.__wrap(__CoreGraphics.CGEventTapCreateForPid(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @staticmethod
    @overload
    def CGEventCreateData(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateData(long,long)"""
        return int.__wrap(__CoreGraphics.CGEventCreateData(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def CGEventTapCreate(arg0: int, arg1: int, arg2: int, arg3: int, arg4: 'CGEventTapCallBackI', arg5: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventTapCreate(int,int,int,long,org.lwjgl.system.macosx.CGEventTapCallBackI,long)"""
        return int.__wrap(__CoreGraphics.CGEventTapCreate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __long.valueOf(arg3), arg4, __long.valueOf(arg5)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def CGEventKeyboardSetUnicodeString(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardSetUnicodeString(long,java.nio.ShortBuffer)"""
        __CoreGraphics.CGEventKeyboardSetUnicodeString(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nCGEventKeyboardGetUnicodeString(arg0: int, arg1: int, arg2: int, arg3: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventKeyboardGetUnicodeString(long,long,long,long)"""
        __CoreGraphics.nCGEventKeyboardGetUnicodeString(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventSetIntegerValueField(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetIntegerValueField(long,int,long)"""
        __CoreGraphics.CGEventSetIntegerValueField(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventCreate(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreate(long)"""
        return int.__wrap(__CoreGraphics.CGEventCreate(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventCreateScrollWheelEvent(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateScrollWheelEvent(long,int,int)"""
        return int.__wrap(__CoreGraphics.CGEventCreateScrollWheelEvent(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def CGEventSetTimestamp(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetTimestamp(long,long)"""
        __CoreGraphics.CGEventSetTimestamp(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def CGGetEventTapList(arg0: 'Buffer', arg1: 'IntBuffer') -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGGetEventTapList(org.lwjgl.system.macosx.CGEventTapInformation$Buffer,java.nio.IntBuffer)"""
        return int.__wrap(__CoreGraphics.CGGetEventTapList(arg0, arg1))

    @staticmethod
    @overload
    def nCGEventGetUnflippedLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetUnflippedLocation(long,long)"""
        __CoreGraphics.nCGEventGetUnflippedLocation(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventKeyboardGetUnicodeString(arg0: int, arg1: 'CLongBuffer', arg2: 'ShortBuffer'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardGetUnicodeString(long,org.lwjgl.CLongBuffer,java.nio.ShortBuffer)"""
        __CoreGraphics.CGEventKeyboardGetUnicodeString(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def CGEventTapPostEvent(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventTapPostEvent(long,long)"""
        __CoreGraphics.CGEventTapPostEvent(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nCGEventCreateMouseEvent(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static native long org.lwjgl.system.macosx.CoreGraphics.nCGEventCreateMouseEvent(long,int,long,int,long)"""
        return int.__wrap(__CoreGraphics.nCGEventCreateMouseEvent(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nCGEventSetLocation(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.nCGEventSetLocation(long,long)"""
        __CoreGraphics.nCGEventSetLocation(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventCreateMouseEvent(arg0: int, arg1: int, arg2: 'CGPoint', arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateMouseEvent(long,int,org.lwjgl.system.macosx.CGPoint,int)"""
        return int.__wrap(__CoreGraphics.CGEventCreateMouseEvent(__long.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def CGEventSetSource(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetSource(long,long)"""
        __CoreGraphics.CGEventSetSource(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventKeyboardGetUnicodeString(arg0: int, arg1: 'CLongBuffer', arg2: 'short'):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventKeyboardGetUnicodeString(long,org.lwjgl.CLongBuffer,short[])"""
        __CoreGraphics.CGEventKeyboardGetUnicodeString(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def CGEventGetTimestamp(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetTimestamp(long)"""
        return int.__wrap(__CoreGraphics.CGEventGetTimestamp(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventGetFlags(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventGetFlags(long)"""
        return int.__wrap(__CoreGraphics.CGEventGetFlags(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def CGEventCreateKeyboardEvent(arg0: int, arg1: int, arg2: bool) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateKeyboardEvent(long,short,boolean)"""
        return int.__wrap(__CoreGraphics.CGEventCreateKeyboardEvent(__long.valueOf(arg0), __short.valueOf(arg1), __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def nCGGetEventTapList(arg0: int, arg1: int, arg2: int) -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.nCGGetEventTapList(int,long,long)"""
        return int.__wrap(__CoreGraphics.nCGGetEventTapList(__int.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2)))

    @staticmethod
    @overload
    def nCGEventGetLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventGetLocation(long,long,long)"""
        __CoreGraphics.nCGEventGetLocation(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventCreateCopy(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.CGEventCreateCopy(long)"""
        return int.__wrap(__CoreGraphics.CGEventCreateCopy(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nCGEventCreateMouseEvent(arg0: int, arg1: int, arg2: int, arg3: int) -> int:
        """public static long org.lwjgl.system.macosx.CoreGraphics.nCGEventCreateMouseEvent(long,int,long,int)"""
        return int.__wrap(__CoreGraphics.nCGEventCreateMouseEvent(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __int.valueOf(arg3)))

    @staticmethod
    @overload
    def nCGEventSetLocation(arg0: int, arg1: int, arg2: int):
        """public static native void org.lwjgl.system.macosx.CoreGraphics.nCGEventSetLocation(long,long,long)"""
        __CoreGraphics.nCGEventSetLocation(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def CGGetEventTapList(arg0: 'Buffer', arg1: 'int') -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGGetEventTapList(org.lwjgl.system.macosx.CGEventTapInformation$Buffer,int[])"""
        return int.__wrap(__CoreGraphics.CGGetEventTapList(arg0, arg1))

    @staticmethod
    @overload
    def CGEventGetType(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CoreGraphics.CGEventGetType(long)"""
        return int.__wrap(__CoreGraphics.CGEventGetType(__long.valueOf(arg0)))

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
    def CGEventTapEnable(arg0: int, arg1: bool):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventTapEnable(long,boolean)"""
        __CoreGraphics.CGEventTapEnable(__long.valueOf(arg0), __boolean.valueOf(arg1))

    @staticmethod
    @overload
    def CGEventSetDoubleValueField(arg0: int, arg1: int, arg2: float):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventSetDoubleValueField(long,int,double)"""
        __CoreGraphics.CGEventSetDoubleValueField(__long.valueOf(arg0), __int.valueOf(arg1), __double.valueOf(arg2))

    @staticmethod
    @overload
    def CGEventPost(arg0: int, arg1: int):
        """public static void org.lwjgl.system.macosx.CoreGraphics.CGEventPost(int,long)"""
        __CoreGraphics.CGEventPost(__int.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCMethodDescription
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.macosx.ObjCMethodDescription as __ObjCMethodDescription_Buffer
__Buffer = __ObjCMethodDescription_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.macosx.ObjCMethodDescription as __ObjCMethodDescription
__ObjCMethodDescription = __ObjCMethodDescription
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
 
class ObjCMethodDescription(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.ObjCMethodDescription"""
 
    @staticmethod
    def __wrap(java_value: __ObjCMethodDescription) -> 'ObjCMethodDescription':
        return ObjCMethodDescription(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjCMethodDescription):
        """
        Dynamic initializer for ObjCMethodDescription.
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
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCMethodDescription(java.nio.ByteBuffer)"""
        val = __ObjCMethodDescription(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.callocStack(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.calloc()"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.calloc())

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
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(int)"""
        return Buffer.__wrap(__ObjCMethodDescription.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack()"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.mallocStack())

    @staticmethod
    @overload
    def ntypes(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription.ntypes(long)"""
        return ByteBuffer.__wrap(__ObjCMethodDescription.ntypes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.malloc()"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.malloc())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.calloc(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.calloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCMethodDescription.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCMethodDescription.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCMethodDescription.calloc(__int.valueOf(arg0), arg1))

    @overload
    def name(self) -> int:
        """public long org.lwjgl.system.macosx.ObjCMethodDescription.name()"""
        return int.__wrap(super(ObjCMethodDescription, self).name())

    @staticmethod
    @overload
    def create(arg0: int) -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.create(long)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.create(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.malloc(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.malloc(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.create(long,int)"""
        return Buffer.__wrap(__ObjCMethodDescription.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(int)"""
        return Buffer.__wrap(__ObjCMethodDescription.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntypesString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription.ntypesString(long)"""
        return str.__wrap(__ObjCMethodDescription.ntypesString(__long.valueOf(arg0)))

    @overload
    def types(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription.types()"""
        return 'ByteBuffer'.__wrap(super(ObjCMethodDescription, self).types())

    @staticmethod
    @overload
    def callocStack() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.callocStack()"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.callocStack())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.malloc(int)"""
        return Buffer.__wrap(__ObjCMethodDescription.malloc(__int.valueOf(arg0)))

    @overload
    def typesString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription.typesString()"""
        return str.__wrap(super(ObjCMethodDescription, self).typesString())

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

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.calloc(int)"""
        return Buffer.__wrap(__ObjCMethodDescription.calloc(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.ObjCMethodDescription.sizeof()"""
        return int.__wrap(super(ObjCMethodDescription, self).sizeof())

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
    def mallocStack(arg0: 'MemoryStack') -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.mallocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.mallocStack(arg0))

    @staticmethod
    @overload
    def nname(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.ObjCMethodDescription.nname(long)"""
        return int.__wrap(__ObjCMethodDescription.nname(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.createSafe(long)"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCMethodDescription.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create() -> 'ObjCMethodDescription':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription org.lwjgl.system.macosx.ObjCMethodDescription.create()"""
        return ObjCMethodDescription.__wrap(__ObjCMethodDescription.create())

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
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.createSafe(long,int)"""
        return Buffer.__wrap(__ObjCMethodDescription.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCMethodDescription$Buffer org.lwjgl.system.macosx.ObjCMethodDescription.create(int)"""
        return Buffer.__wrap(__ObjCMethodDescription.create(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer
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
import org.lwjgl.system.macosx.ObjCPropertyAttribute as __ObjCPropertyAttribute_Buffer
__Buffer = __ObjCPropertyAttribute_Buffer.Buffer
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
    """org.lwjgl.system.macosx.ObjCPropertyAttribute.Buffer"""
 
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
    def name(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.name(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).name(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(__pyglsystem.StructBuffer, self).forEach(arg0)

    @overload
    def value(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.value(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).value(arg0))

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
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.name()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).name())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer(java.nio.ByteBuffer)"""
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
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.nameString()"""
        return str.__wrap(super(Buffer, self).nameString())

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
    def valueString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.valueString()"""
        return str.__wrap(super(Buffer, self).valueString())

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
    def value(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer.value()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).value())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'.__wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCMethodDescription$Buffer
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
import org.lwjgl.system.macosx.ObjCMethodDescription as __ObjCMethodDescription_Buffer
__Buffer = __ObjCMethodDescription_Buffer.Buffer
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
    """org.lwjgl.system.macosx.ObjCMethodDescription.Buffer"""
 
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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCMethodDescription$Buffer(java.nio.ByteBuffer)"""
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
    def types(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.types()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).types())

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
    def name(self) -> int:
        """public long org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.name()"""
        return int.__wrap(super(Buffer, self).name())

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

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.system.macosx.ObjCMethodDescription$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'.__wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def typesString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCMethodDescription$Buffer.typesString()"""
        return str.__wrap(super(Buffer, self).typesString())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).slice(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.lwjgl.system.macosx.ObjCPropertyAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.system.macosx.ObjCPropertyAttribute as __ObjCPropertyAttribute
__ObjCPropertyAttribute = __ObjCPropertyAttribute
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.system.macosx.ObjCPropertyAttribute as __ObjCPropertyAttribute_Buffer
__Buffer = __ObjCPropertyAttribute_Buffer.Buffer
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
 
class ObjCPropertyAttribute(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.ObjCPropertyAttribute"""
 
    @staticmethod
    def __wrap(java_value: __ObjCPropertyAttribute) -> 'ObjCPropertyAttribute':
        return ObjCPropertyAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjCPropertyAttribute):
        """
        Dynamic initializer for ObjCPropertyAttribute.
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
    def callocStack(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.callocStack(arg0))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.validate(long)"""
        __ObjCPropertyAttribute.validate(__long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def name(self, arg0: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.name(java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'.__wrap(super(__ObjCPropertyAttribute, self).name(arg0))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'ObjCPropertyAttribute') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.set(org.lwjgl.system.macosx.ObjCPropertyAttribute)"""
        return 'ObjCPropertyAttribute'.__wrap(super(__ObjCPropertyAttribute, self).set(arg0))

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
    def valueString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.valueString()"""
        return str.__wrap(super(ObjCPropertyAttribute, self).valueString())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.createSafe(long)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nname(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.nname(long,java.nio.ByteBuffer)"""
        __ObjCPropertyAttribute.nname(__long.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute(java.nio.ByteBuffer)"""
        val = __ObjCPropertyAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def value(self, arg0: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.value(java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'.__wrap(super(__ObjCPropertyAttribute, self).value(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.create(int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nvalueString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalueString(long)"""
        return str.__wrap(__ObjCPropertyAttribute.nvalueString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.malloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nnameString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nnameString(long)"""
        return str.__wrap(__ObjCPropertyAttribute.nnameString(__long.valueOf(arg0)))

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

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'ByteBuffer') -> 'ObjCPropertyAttribute':
        """public org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.set(java.nio.ByteBuffer,java.nio.ByteBuffer)"""
        return 'ObjCPropertyAttribute'.__wrap(super(__ObjCPropertyAttribute, self).set(arg0, arg1))

    @staticmethod
    @overload
    def create() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.create()"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.create())

    @staticmethod
    @overload
    def nvalue(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalue(long)"""
        return ByteBuffer.__wrap(__ObjCPropertyAttribute.nvalue(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack()"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.calloc(arg0))

    @overload
    def value(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.value()"""
        return 'ByteBuffer'.__wrap(super(ObjCPropertyAttribute, self).value())

    @overload
    def nameString(self) -> str:
        """public java.lang.String org.lwjgl.system.macosx.ObjCPropertyAttribute.nameString()"""
        return str.__wrap(super(ObjCPropertyAttribute, self).nameString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.create(long,int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack()"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.callocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nvalue(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.system.macosx.ObjCPropertyAttribute.nvalue(long,java.nio.ByteBuffer)"""
        __ObjCPropertyAttribute.nvalue(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc()"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.calloc())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.mallocStack(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.createSafe(long,int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def name(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.name()"""
        return 'ByteBuffer'.__wrap(super(ObjCPropertyAttribute, self).name())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.calloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc(org.lwjgl.system.MemoryStack)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.malloc(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(int)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.malloc()"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.malloc())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int) -> 'ObjCPropertyAttribute':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute org.lwjgl.system.macosx.ObjCPropertyAttribute.create(long)"""
        return ObjCPropertyAttribute.__wrap(__ObjCPropertyAttribute.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nname(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.system.macosx.ObjCPropertyAttribute.nname(long)"""
        return ByteBuffer.__wrap(__ObjCPropertyAttribute.nname(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.ObjCPropertyAttribute.sizeof()"""
        return int.__wrap(super(ObjCPropertyAttribute, self).sizeof())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.ObjCPropertyAttribute$Buffer org.lwjgl.system.macosx.ObjCPropertyAttribute.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__ObjCPropertyAttribute.mallocStack(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapInformation
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.macosx.CGEventTapInformation as __CGEventTapInformation
__CGEventTapInformation = __CGEventTapInformation
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.system.macosx.CGEventTapInformation as __CGEventTapInformation_Buffer
__Buffer = __CGEventTapInformation_Buffer.Buffer
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
 
class CGEventTapInformation(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.CGEventTapInformation"""
 
    @staticmethod
    def __wrap(java_value: __CGEventTapInformation) -> 'CGEventTapInformation':
        return CGEventTapInformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CGEventTapInformation):
        """
        Dynamic initializer for CGEventTapInformation.
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
    def nprocessBeingTapped(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.nprocessBeingTapped(long)"""
        return int.__wrap(__CGEventTapInformation.nprocessBeingTapped(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nmaxUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.nmaxUsecLatency(long)"""
        return float.__wrap(__CGEventTapInformation.nmaxUsecLatency(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGEventTapInformation.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.create(long,int)"""
        return Buffer.__wrap(__CGEventTapInformation.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGEventTapInformation.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def maxUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.maxUsecLatency()"""
        return float.__wrap(super(CGEventTapInformation, self).maxUsecLatency())

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGEventTapInformation(java.nio.ByteBuffer)"""
        val = __CGEventTapInformation(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def noptions(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.noptions(long)"""
        return int.__wrap(__CGEventTapInformation.noptions(__long.valueOf(arg0)))

    @overload
    def minUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.minUsecLatency()"""
        return float.__wrap(super(CGEventTapInformation, self).minUsecLatency())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.callocStack(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.callocStack(arg0))

    @overload
    def eventsOfInterest(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.eventsOfInterest()"""
        return int.__wrap(super(CGEventTapInformation, self).eventsOfInterest())

    @overload
    def avgUsecLatency(self) -> float:
        """public float org.lwjgl.system.macosx.CGEventTapInformation.avgUsecLatency()"""
        return float.__wrap(super(CGEventTapInformation, self).avgUsecLatency())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.callocStack(int)"""
        return Buffer.__wrap(__CGEventTapInformation.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.create()"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.create())

    @overload
    def eventTapID(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.eventTapID()"""
        return int.__wrap(super(CGEventTapInformation, self).eventTapID())

    @overload
    def enabled(self) -> bool:
        """public boolean org.lwjgl.system.macosx.CGEventTapInformation.enabled()"""
        return bool.__wrap(super(CGEventTapInformation, self).enabled())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.createSafe(long,int)"""
        return Buffer.__wrap(__CGEventTapInformation.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.callocStack()"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.callocStack())

    @staticmethod
    @overload
    def neventsOfInterest(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.neventsOfInterest(long)"""
        return int.__wrap(__CGEventTapInformation.neventsOfInterest(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ntappingProcess(arg0: int) -> int:
        """public static long org.lwjgl.system.macosx.CGEventTapInformation.ntappingProcess(long)"""
        return int.__wrap(__CGEventTapInformation.ntappingProcess(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGEventTapInformation.malloc(__int.valueOf(arg0), arg1))

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
    def options(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.options()"""
        return int.__wrap(super(CGEventTapInformation, self).options())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.calloc(int)"""
        return Buffer.__wrap(__CGEventTapInformation.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.calloc()"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.calloc())

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.create(long)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.malloc(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.malloc(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def processBeingTapped(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.processBeingTapped()"""
        return int.__wrap(super(CGEventTapInformation, self).processBeingTapped())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGEventTapInformation.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.mallocStack(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.create(int)"""
        return Buffer.__wrap(__CGEventTapInformation.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.createSafe(long)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def navgUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.navgUsecLatency(long)"""
        return float.__wrap(__CGEventTapInformation.navgUsecLatency(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nenabled(arg0: int) -> bool:
        """public static boolean org.lwjgl.system.macosx.CGEventTapInformation.nenabled(long)"""
        return bool.__wrap(__CGEventTapInformation.nenabled(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.mallocStack(int)"""
        return Buffer.__wrap(__CGEventTapInformation.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ntapPoint(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.ntapPoint(long)"""
        return int.__wrap(__CGEventTapInformation.ntapPoint(__long.valueOf(arg0)))

    @overload
    def tapPoint(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.tapPoint()"""
        return int.__wrap(super(CGEventTapInformation, self).tapPoint())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGEventTapInformation$Buffer org.lwjgl.system.macosx.CGEventTapInformation.malloc(int)"""
        return Buffer.__wrap(__CGEventTapInformation.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.CGEventTapInformation.sizeof()"""
        return int.__wrap(super(CGEventTapInformation, self).sizeof())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nminUsecLatency(arg0: int) -> float:
        """public static float org.lwjgl.system.macosx.CGEventTapInformation.nminUsecLatency(long)"""
        return float.__wrap(__CGEventTapInformation.nminUsecLatency(__long.valueOf(arg0)))

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
    def malloc() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.malloc()"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.malloc())

    @staticmethod
    @overload
    def neventTapID(arg0: int) -> int:
        """public static int org.lwjgl.system.macosx.CGEventTapInformation.neventTapID(long)"""
        return int.__wrap(__CGEventTapInformation.neventTapID(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.mallocStack()"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.mallocStack())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CGEventTapInformation':
        """public static org.lwjgl.system.macosx.CGEventTapInformation org.lwjgl.system.macosx.CGEventTapInformation.calloc(org.lwjgl.system.MemoryStack)"""
        return CGEventTapInformation.__wrap(__CGEventTapInformation.calloc(arg0))

    @overload
    def tappingProcess(self) -> int:
        """public long org.lwjgl.system.macosx.CGEventTapInformation.tappingProcess()"""
        return int.__wrap(super(CGEventTapInformation, self).tappingProcess()) 
 
 
# CLASS: org.lwjgl.system.macosx.CGEventTapCallBackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.macosx.CGEventTapCallBackI as __CGEventTapCallBackI
__CGEventTapCallBackI = __CGEventTapCallBackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class CGEventTapCallBackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.system.macosx.CGEventTapCallBackI"""
 
    @staticmethod
    def __wrap(java_value: __CGEventTapCallBackI) -> 'CGEventTapCallBackI':
        return CGEventTapCallBackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CGEventTapCallBackI):
        """
        Dynamic initializer for CGEventTapCallBackI.
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
        """public default void org.lwjgl.system.macosx.CGEventTapCallBackI.callback(long,long)"""
        super(__CGEventTapCallBackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.system.macosx.CGEventTapCallBackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(CGEventTapCallBackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract long org.lwjgl.system.macosx.CGEventTapCallBackI.invoke(long,int,long,long)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.system.macosx.CoreGraphics$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.system.macosx.CoreGraphics as __CoreGraphics_Functions
__Functions = __CoreGraphics_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.system.macosx.CoreGraphics.Functions"""
 
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
 
 
# CLASS: org.lwjgl.system.macosx.CGPoint
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.system.macosx.CGPoint as __CGPoint
__CGPoint = __CGPoint
from builtins import float
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
import org.lwjgl.system.macosx.CGPoint as __CGPoint_Buffer
__Buffer = __CGPoint_Buffer.Buffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Double as __double
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class CGPoint(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.system.macosx.CGPoint"""
 
    @staticmethod
    def __wrap(java_value: __CGPoint) -> 'CGPoint':
        return CGPoint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CGPoint):
        """
        Dynamic initializer for CGPoint.
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
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.mallocStack(int)"""
        return Buffer.__wrap(__CGPoint.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.callocStack()"""
        return CGPoint.__wrap(__CGPoint.callocStack())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.calloc(int)"""
        return Buffer.__wrap(__CGPoint.calloc(__int.valueOf(arg0)))

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
    def ny(arg0: int) -> float:
        """public static double org.lwjgl.system.macosx.CGPoint.ny(long)"""
        return float.__wrap(__CGPoint.ny(__long.valueOf(arg0)))

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.malloc(int)"""
        return Buffer.__wrap(__CGPoint.malloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.malloc(org.lwjgl.system.MemoryStack)"""
        return CGPoint.__wrap(__CGPoint.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.callocStack(org.lwjgl.system.MemoryStack)"""
        return CGPoint.__wrap(__CGPoint.callocStack(arg0))

    @overload
    def y(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint.y()"""
        return float.__wrap(super(CGPoint, self).y())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGPoint.malloc(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: 'CGPoint') -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.set(org.lwjgl.system.macosx.CGPoint)"""
        return 'CGPoint'.__wrap(super(__CGPoint, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGPoint.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.callocStack(int)"""
        return Buffer.__wrap(__CGPoint.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def ny(arg0: int, arg1: float):
        """public static void org.lwjgl.system.macosx.CGPoint.ny(long,double)"""
        __CGPoint.ny(__long.valueOf(arg0), __double.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.create(long,int)"""
        return Buffer.__wrap(__CGPoint.create(__long.valueOf(arg0), __int.valueOf(arg1)))

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
    def create() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.create()"""
        return CGPoint.__wrap(__CGPoint.create())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.mallocStack(org.lwjgl.system.MemoryStack)"""
        return CGPoint.__wrap(__CGPoint.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.create(int)"""
        return Buffer.__wrap(__CGPoint.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.malloc()"""
        return CGPoint.__wrap(__CGPoint.malloc())

    @staticmethod
    @overload
    def nx(arg0: int, arg1: float):
        """public static void org.lwjgl.system.macosx.CGPoint.nx(long,double)"""
        __CGPoint.nx(__long.valueOf(arg0), __double.valueOf(arg1))

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

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.macosx.CGPoint.sizeof()"""
        return int.__wrap(super(CGPoint, self).sizeof())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.system.macosx.CGPoint(java.nio.ByteBuffer)"""
        val = __CGPoint(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def create(arg0: int) -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.create(long)"""
        return CGPoint.__wrap(__CGPoint.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.calloc()"""
        return CGPoint.__wrap(__CGPoint.calloc())

    @overload
    def set(self, arg0: float, arg1: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.set(double,double)"""
        return 'CGPoint'.__wrap(super(__CGPoint, self).set(__double.valueOf(arg0), __double.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def x(self) -> float:
        """public double org.lwjgl.system.macosx.CGPoint.x()"""
        return float.__wrap(super(CGPoint, self).x())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGPoint.mallocStack(__int.valueOf(arg0), arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.createSafe(long,int)"""
        return Buffer.__wrap(__CGPoint.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.mallocStack()"""
        return CGPoint.__wrap(__CGPoint.mallocStack())

    @overload
    def y(self, arg0: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.y(double)"""
        return 'CGPoint'.__wrap(super(__CGPoint, self).y(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def x(self, arg0: float) -> 'CGPoint':
        """public org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.x(double)"""
        return 'CGPoint'.__wrap(super(__CGPoint, self).x(__double.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.calloc(org.lwjgl.system.MemoryStack)"""
        return CGPoint.__wrap(__CGPoint.calloc(arg0))

    @staticmethod
    @overload
    def nx(arg0: int) -> float:
        """public static double org.lwjgl.system.macosx.CGPoint.nx(long)"""
        return float.__wrap(__CGPoint.nx(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.system.macosx.CGPoint$Buffer org.lwjgl.system.macosx.CGPoint.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__CGPoint.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'CGPoint':
        """public static org.lwjgl.system.macosx.CGPoint org.lwjgl.system.macosx.CGPoint.createSafe(long)"""
        return CGPoint.__wrap(__CGPoint.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.system.macosx.LibC$Functions
import org.lwjgl.system.macosx.LibC as __LibC_Functions
__Functions = __LibC_Functions.Functions
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
from builtins import int
 
class Functions():
    """org.lwjgl.system.macosx.LibC.Functions"""
 
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