from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowContentScaleCallbackI as _GLFWWindowContentScaleCallbackI
_GLFWWindowContentScaleCallbackI = _GLFWWindowContentScaleCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowContentScaleCallbackI():
    """org.lwjgl.glfw.GLFWWindowContentScaleCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowContentScaleCallbackI) -> 'GLFWWindowContentScaleCallbackI':
        return GLFWWindowContentScaleCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowContentScaleCallbackI):
        """
        Dynamic initializer for GLFWWindowContentScaleCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowContentScaleCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowContentScaleCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.callback(long,long)"""
        super(_GLFWWindowContentScaleCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.invoke(long,float,float)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowContentScaleCallbackI, self).getCallInterface())

 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowContentScaleCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowContentScaleCallbackI as _GLFWWindowContentScaleCallbackI
_GLFWWindowContentScaleCallbackI = _GLFWWindowContentScaleCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowContentScaleCallbackI():
    """org.lwjgl.glfw.GLFWWindowContentScaleCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowContentScaleCallbackI) -> 'GLFWWindowContentScaleCallbackI':
        return GLFWWindowContentScaleCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowContentScaleCallbackI):
        """
        Dynamic initializer for GLFWWindowContentScaleCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowContentScaleCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowContentScaleCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.callback(long,long)"""
        super(_GLFWWindowContentScaleCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.invoke(long,float,float)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowContentScaleCallbackI, self).getCallInterface())

 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowContentScaleCallbackI 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowRefreshCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWWindowRefreshCallback as _GLFWWindowRefreshCallback
_GLFWWindowRefreshCallback = _GLFWWindowRefreshCallback
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWWindowRefreshCallbackI as _GLFWWindowRefreshCallbackI
_GLFWWindowRefreshCallbackI = _GLFWWindowRefreshCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowRefreshCallback():
    """org.lwjgl.glfw.GLFWWindowRefreshCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowRefreshCallback) -> 'GLFWWindowRefreshCallback':
        return GLFWWindowRefreshCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowRefreshCallback):
        """
        Dynamic initializer for GLFWWindowRefreshCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowRefreshCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowRefreshCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.createSafe(long)"""
        return GLFWWindowRefreshCallback._wrap(_GLFWWindowRefreshCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowRefreshCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowRefreshCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.callback(long,long)"""
        super(_GLFWWindowRefreshCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowRefreshCallbackI') -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.create(org.lwjgl.glfw.GLFWWindowRefreshCallbackI)"""
        return GLFWWindowRefreshCallback._wrap(_GLFWWindowRefreshCallback.create(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowRefreshCallback':
        """public org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.set(long)"""
        return 'GLFWWindowRefreshCallback'._wrap(super(_GLFWWindowRefreshCallback, self).set(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.create(long)"""
        return GLFWWindowRefreshCallback._wrap(_GLFWWindowRefreshCallback.create(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.invoke(long)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeEGL
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import org.lwjgl.glfw.GLFWNativeEGL as _GLFWNativeEGL
_GLFWNativeEGL = _GLFWNativeEGL
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeEGL():
    """org.lwjgl.glfw.GLFWNativeEGL"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeEGL) -> 'GLFWNativeEGL':
        return GLFWNativeEGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeEGL):
        """
        Dynamic initializer for GLFWNativeEGL.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeEGL__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeEGL__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def setGLESPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setGLESPath(java.lang.String)"""
        _GLFWNativeEGL.setGLESPath(arg0)

    @staticmethod
    @overload
    def setEGLPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setEGLPath(java.lang.String)"""
        _GLFWNativeEGL.setEGLPath(arg0)

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

    @staticmethod
    @overload
    def glfwGetEGLSurface(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLSurface(long)"""
        return int._wrap(_GLFWNativeEGL.glfwGetEGLSurface(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def glfwGetEGLConfig(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLConfig(long)"""
        return int._wrap(_GLFWNativeEGL.glfwGetEGLConfig(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def setEGLPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setEGLPath(org.lwjgl.system.FunctionProvider)"""
        _GLFWNativeEGL.setEGLPath(arg0)

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

    @staticmethod
    @overload
    def setGLESPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setGLESPath(org.lwjgl.system.FunctionProvider)"""
        _GLFWNativeEGL.setGLESPath(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetEGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLContext(long)"""
        return int._wrap(_GLFWNativeEGL.glfwGetEGLContext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetEGLDisplay() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLDisplay()"""
        return int._wrap(_GLFWNativeEGL.glfwGetEGLDisplay())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWKeyCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWKeyCallbackI as _GLFWKeyCallbackI
_GLFWKeyCallbackI = _GLFWKeyCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWKeyCallbackI():
    """org.lwjgl.glfw.GLFWKeyCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWKeyCallbackI) -> 'GLFWKeyCallbackI':
        return GLFWKeyCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWKeyCallbackI):
        """
        Dynamic initializer for GLFWKeyCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWKeyCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWKeyCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWKeyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWKeyCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void org.lwjgl.glfw.GLFWKeyCallbackI.invoke(long,int,int,int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWKeyCallbackI.callback(long,long)"""
        super(_GLFWKeyCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWin32
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeWin32 as _GLFWNativeWin32
_GLFWNativeWin32 = _GLFWNativeWin32
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeWin32():
    """org.lwjgl.glfw.GLFWNativeWin32"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeWin32) -> 'GLFWNativeWin32':
        return GLFWNativeWin32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeWin32):
        """
        Dynamic initializer for GLFWNativeWin32.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeWin32__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeWin32__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nglfwGetWin32Adapter(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.nglfwGetWin32Adapter(long)"""
        return int._wrap(_GLFWNativeWin32.nglfwGetWin32Adapter(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def glfwAttachWin32Window(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.glfwAttachWin32Window(long,long)"""
        return int._wrap(_GLFWNativeWin32.glfwAttachWin32Window(_long.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWin32Window(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Window(long)"""
        return int._wrap(_GLFWNativeWin32.glfwGetWin32Window(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nglfwGetWin32Monitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.nglfwGetWin32Monitor(long)"""
        return int._wrap(_GLFWNativeWin32.nglfwGetWin32Monitor(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def glfwGetWin32Monitor(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Monitor(long)"""
        return str._wrap(_GLFWNativeWin32.glfwGetWin32Monitor(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetWin32Adapter(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Adapter(long)"""
        return str._wrap(_GLFWNativeWin32.glfwGetWin32Adapter(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDeallocateCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWDeallocateCallbackI as _GLFWDeallocateCallbackI
_GLFWDeallocateCallbackI = _GLFWDeallocateCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWDeallocateCallbackI():
    """org.lwjgl.glfw.GLFWDeallocateCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWDeallocateCallbackI) -> 'GLFWDeallocateCallbackI':
        return GLFWDeallocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWDeallocateCallbackI):
        """
        Dynamic initializer for GLFWDeallocateCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWDeallocateCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWDeallocateCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWDeallocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDeallocateCallbackI.callback(long,long)"""
        super(_GLFWDeallocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDeallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWDeallocateCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWReallocateCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWReallocateCallback as _GLFWReallocateCallback
_GLFWReallocateCallback = _GLFWReallocateCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWReallocateCallbackI as _GLFWReallocateCallbackI
_GLFWReallocateCallbackI = _GLFWReallocateCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWReallocateCallback():
    """org.lwjgl.glfw.GLFWReallocateCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWReallocateCallback) -> 'GLFWReallocateCallback':
        return GLFWReallocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWReallocateCallback):
        """
        Dynamic initializer for GLFWReallocateCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWReallocateCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWReallocateCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWReallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWReallocateCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'GLFWReallocateCallbackI') -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.create(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return GLFWReallocateCallback._wrap(_GLFWReallocateCallback.create(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWReallocateCallbackI.callback(long,long)"""
        super(_GLFWReallocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.createSafe(long)"""
        return GLFWReallocateCallback._wrap(_GLFWReallocateCallback.createSafe(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.create(long)"""
        return GLFWReallocateCallback._wrap(_GLFWReallocateCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract long org.lwjgl.glfw.GLFWReallocateCallbackI.invoke(long,long,long)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWJoystickCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWJoystickCallbackI as _GLFWJoystickCallbackI
_GLFWJoystickCallbackI = _GLFWJoystickCallbackI
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWJoystickCallback as _GLFWJoystickCallback
_GLFWJoystickCallback = _GLFWJoystickCallback
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWJoystickCallback():
    """org.lwjgl.glfw.GLFWJoystickCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWJoystickCallback) -> 'GLFWJoystickCallback':
        return GLFWJoystickCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWJoystickCallback):
        """
        Dynamic initializer for GLFWJoystickCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWJoystickCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWJoystickCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.createSafe(long)"""
        return GLFWJoystickCallback._wrap(_GLFWJoystickCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.create(long)"""
        return GLFWJoystickCallback._wrap(_GLFWJoystickCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWJoystickCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWJoystickCallbackI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWJoystickCallbackI.invoke(int,int)"""
        pass

    @overload
    def set(self) -> 'GLFWJoystickCallback':
        """public org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.set()"""
        return 'GLFWJoystickCallback'._wrap(super(GLFWJoystickCallback, self).set())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: 'GLFWJoystickCallbackI') -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.create(org.lwjgl.glfw.GLFWJoystickCallbackI)"""
        return GLFWJoystickCallback._wrap(_GLFWJoystickCallback.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWJoystickCallbackI.callback(long,long)"""
        super(_GLFWJoystickCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVidMode$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import org.lwjgl.glfw.GLFWVidMode as _GLFWVidMode_Buffer
_Buffer = _GLFWVidMode_Buffer.Buffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.glfw.GLFWVidMode.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.height()"""
        return int._wrap(super(Buffer, self).height())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.width()"""
        return int._wrap(super(Buffer, self).width())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def redBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.redBits()"""
        return int._wrap(super(Buffer, self).redBits())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def refreshRate(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.refreshRate()"""
        return int._wrap(super(Buffer, self).refreshRate())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWVidMode$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWVidMode$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def blueBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.blueBits()"""
        return int._wrap(super(Buffer, self).blueBits())

    @overload
    def greenBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.greenBits()"""
        return int._wrap(super(Buffer, self).greenBits())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDropCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.glfw.GLFWDropCallback as _GLFWDropCallback
_GLFWDropCallback = _GLFWDropCallback
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.lwjgl.glfw.GLFWDropCallbackI as _GLFWDropCallbackI
_GLFWDropCallbackI = _GLFWDropCallbackI
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWDropCallback():
    """org.lwjgl.glfw.GLFWDropCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWDropCallback) -> 'GLFWDropCallback':
        return GLFWDropCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWDropCallback):
        """
        Dynamic initializer for GLFWDropCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWDropCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWDropCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWDropCallback':
        """public org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.set(long)"""
        return 'GLFWDropCallback'._wrap(super(_GLFWDropCallback, self).set(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWDropCallbackI') -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.create(org.lwjgl.glfw.GLFWDropCallbackI)"""
        return GLFWDropCallback._wrap(_GLFWDropCallback.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.create(long)"""
        return GLFWDropCallback._wrap(_GLFWDropCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWDropCallbackI.invoke(long,int,long)"""
        pass

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDropCallbackI.callback(long,long)"""
        super(_GLFWDropCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.createSafe(long)"""
        return GLFWDropCallback._wrap(_GLFWDropCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWDropCallback.getName(long,int)"""
        return str._wrap(_GLFWDropCallback.getName(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDropCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWDropCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocateCallback
from pyquantum_helper import import_once as _import_once
import org.lwjgl.glfw.GLFWAllocateCallback as _GLFWAllocateCallback
_GLFWAllocateCallback = _GLFWAllocateCallback
from builtins import str
import org.lwjgl.glfw.GLFWAllocateCallbackI as _GLFWAllocateCallbackI
_GLFWAllocateCallbackI = _GLFWAllocateCallbackI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWAllocateCallback():
    """org.lwjgl.glfw.GLFWAllocateCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWAllocateCallback) -> 'GLFWAllocateCallback':
        return GLFWAllocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWAllocateCallback):
        """
        Dynamic initializer for GLFWAllocateCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWAllocateCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWAllocateCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.createSafe(long)"""
        return GLFWAllocateCallback._wrap(_GLFWAllocateCallback.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: 'GLFWAllocateCallbackI') -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.create(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return GLFWAllocateCallback._wrap(_GLFWAllocateCallback.create(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.create(long)"""
        return GLFWAllocateCallback._wrap(_GLFWAllocateCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWAllocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWAllocateCallbackI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.glfw.GLFWAllocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWAllocateCallbackI.callback(long,long)"""
        super(_GLFWAllocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowIconifyCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.glfw.GLFWWindowIconifyCallbackI as _GLFWWindowIconifyCallbackI
_GLFWWindowIconifyCallbackI = _GLFWWindowIconifyCallbackI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowIconifyCallback as _GLFWWindowIconifyCallback
_GLFWWindowIconifyCallback = _GLFWWindowIconifyCallback
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowIconifyCallback():
    """org.lwjgl.glfw.GLFWWindowIconifyCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowIconifyCallback) -> 'GLFWWindowIconifyCallback':
        return GLFWWindowIconifyCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowIconifyCallback):
        """
        Dynamic initializer for GLFWWindowIconifyCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowIconifyCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowIconifyCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.create(long)"""
        return GLFWWindowIconifyCallback._wrap(_GLFWWindowIconifyCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowIconifyCallback':
        """public org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.set(long)"""
        return 'GLFWWindowIconifyCallback'._wrap(super(_GLFWWindowIconifyCallback, self).set(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowIconifyCallbackI') -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.create(org.lwjgl.glfw.GLFWWindowIconifyCallbackI)"""
        return GLFWWindowIconifyCallback._wrap(_GLFWWindowIconifyCallback.create(arg0))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowIconifyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowIconifyCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.callback(long,long)"""
        super(_GLFWWindowIconifyCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.createSafe(long)"""
        return GLFWWindowIconifyCallback._wrap(_GLFWWindowIconifyCallback.createSafe(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGammaRamp$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.ShortBuffer as ShortBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.glfw.GLFWGammaRamp as _GLFWGammaRamp_Buffer
_Buffer = _GLFWGammaRamp_Buffer.Buffer
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.glfw.GLFWGammaRamp.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def red(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.red(java.nio.ShortBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).red(arg0))

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @overload
    def green(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.green(java.nio.ShortBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).green(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def size(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp$Buffer.size()"""
        return int._wrap(super(Buffer, self).size())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def blue(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.blue()"""
        return 'ShortBuffer'._wrap(super(Buffer, self).blue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def blue(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.blue(java.nio.ShortBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).blue(arg0))

    @overload
    def size(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.size(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).size(_int.valueOf(arg0)))

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def red(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.red()"""
        return 'ShortBuffer'._wrap(super(Buffer, self).red())

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @overload
    def green(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.green()"""
        return 'ShortBuffer'._wrap(super(Buffer, self).green())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWScrollCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWScrollCallbackI as _GLFWScrollCallbackI
_GLFWScrollCallbackI = _GLFWScrollCallbackI
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWScrollCallbackI():
    """org.lwjgl.glfw.GLFWScrollCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWScrollCallbackI) -> 'GLFWScrollCallbackI':
        return GLFWScrollCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWScrollCallbackI):
        """
        Dynamic initializer for GLFWScrollCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWScrollCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWScrollCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWScrollCallbackI.invoke(long,double,double)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWScrollCallbackI.callback(long,long)"""
        super(_GLFWScrollCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWScrollCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWScrollCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeX11$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeX11 as _GLFWNativeX11_Functions
_Functions = _GLFWNativeX11_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeX11.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowMaximizeCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWWindowMaximizeCallbackI as _GLFWWindowMaximizeCallbackI
_GLFWWindowMaximizeCallbackI = _GLFWWindowMaximizeCallbackI
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWWindowMaximizeCallback as _GLFWWindowMaximizeCallback
_GLFWWindowMaximizeCallback = _GLFWWindowMaximizeCallback
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowMaximizeCallback():
    """org.lwjgl.glfw.GLFWWindowMaximizeCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowMaximizeCallback) -> 'GLFWWindowMaximizeCallback':
        return GLFWWindowMaximizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowMaximizeCallback):
        """
        Dynamic initializer for GLFWWindowMaximizeCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowMaximizeCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowMaximizeCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.set(long)"""
        return 'GLFWWindowMaximizeCallback'._wrap(super(_GLFWWindowMaximizeCallback, self).set(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.createSafe(long)"""
        return GLFWWindowMaximizeCallback._wrap(_GLFWWindowMaximizeCallback.createSafe(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowMaximizeCallbackI') -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.create(org.lwjgl.glfw.GLFWWindowMaximizeCallbackI)"""
        return GLFWWindowMaximizeCallback._wrap(_GLFWWindowMaximizeCallback.create(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.callback(long,long)"""
        super(_GLFWWindowMaximizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.invoke(long,boolean)"""
        pass

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.create(long)"""
        return GLFWWindowMaximizeCallback._wrap(_GLFWWindowMaximizeCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowMaximizeCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowCloseCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWWindowCloseCallbackI as _GLFWWindowCloseCallbackI
_GLFWWindowCloseCallbackI = _GLFWWindowCloseCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowCloseCallbackI():
    """org.lwjgl.glfw.GLFWWindowCloseCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowCloseCallbackI) -> 'GLFWWindowCloseCallbackI':
        return GLFWWindowCloseCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowCloseCallbackI):
        """
        Dynamic initializer for GLFWWindowCloseCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowCloseCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowCloseCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowCloseCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowCloseCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowCloseCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowCloseCallbackI.callback(long,long)"""
        super(_GLFWWindowCloseCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWGL$Functions
from builtins import str
import org.lwjgl.glfw.GLFWNativeWGL as _GLFWNativeWGL_Functions
_Functions = _GLFWNativeWGL_Functions.Functions
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWGL.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeCocoa$Functions
from builtins import str
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWNativeCocoa as _GLFWNativeCocoa_Functions
_Functions = _GLFWNativeCocoa_Functions.Functions
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeCocoa.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWCharCallbackI as _GLFWCharCallbackI
_GLFWCharCallbackI = _GLFWCharCallbackI
import org.lwjgl.glfw.GLFWCharCallback as _GLFWCharCallback
_GLFWCharCallback = _GLFWCharCallback
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWCharCallback():
    """org.lwjgl.glfw.GLFWCharCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCharCallback) -> 'GLFWCharCallback':
        return GLFWCharCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCharCallback):
        """
        Dynamic initializer for GLFWCharCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCharCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCharCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: int) -> 'GLFWCharCallback':
        """public org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.set(long)"""
        return 'GLFWCharCallback'._wrap(super(_GLFWCharCallback, self).set(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWCharCallbackI') -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.create(org.lwjgl.glfw.GLFWCharCallbackI)"""
        return GLFWCharCallback._wrap(_GLFWCharCallback.create(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharCallbackI.callback(long,long)"""
        super(_GLFWCharCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.create(long)"""
        return GLFWCharCallback._wrap(_GLFWCharCallback.create(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWCharCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCharCallbackI, self).getCallInterface())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.createSafe(long)"""
        return GLFWCharCallback._wrap(_GLFWCharCallback.createSafe(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowFocusCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWWindowFocusCallback as _GLFWWindowFocusCallback
_GLFWWindowFocusCallback = _GLFWWindowFocusCallback
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowFocusCallbackI as _GLFWWindowFocusCallbackI
_GLFWWindowFocusCallbackI = _GLFWWindowFocusCallbackI
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowFocusCallback():
    """org.lwjgl.glfw.GLFWWindowFocusCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowFocusCallback) -> 'GLFWWindowFocusCallback':
        return GLFWWindowFocusCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowFocusCallback):
        """
        Dynamic initializer for GLFWWindowFocusCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowFocusCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowFocusCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowFocusCallbackI') -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.create(org.lwjgl.glfw.GLFWWindowFocusCallbackI)"""
        return GLFWWindowFocusCallback._wrap(_GLFWWindowFocusCallback.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowFocusCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowFocusCallbackI, self).getCallInterface())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowFocusCallbackI.invoke(long,boolean)"""
        pass

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.createSafe(long)"""
        return GLFWWindowFocusCallback._wrap(_GLFWWindowFocusCallback.createSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowFocusCallback':
        """public org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.set(long)"""
        return 'GLFWWindowFocusCallback'._wrap(super(_GLFWWindowFocusCallback, self).set(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.create(long)"""
        return GLFWWindowFocusCallback._wrap(_GLFWWindowFocusCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowFocusCallbackI.callback(long,long)"""
        super(_GLFWWindowFocusCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowSizeCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWWindowSizeCallbackI as _GLFWWindowSizeCallbackI
_GLFWWindowSizeCallbackI = _GLFWWindowSizeCallbackI
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowSizeCallbackI():
    """org.lwjgl.glfw.GLFWWindowSizeCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowSizeCallbackI) -> 'GLFWWindowSizeCallbackI':
        return GLFWWindowSizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowSizeCallbackI):
        """
        Dynamic initializer for GLFWWindowSizeCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowSizeCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowSizeCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowSizeCallbackI.callback(long,long)"""
        super(_GLFWWindowSizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowSizeCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowRefreshCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWWindowRefreshCallbackI as _GLFWWindowRefreshCallbackI
_GLFWWindowRefreshCallbackI = _GLFWWindowRefreshCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowRefreshCallbackI():
    """org.lwjgl.glfw.GLFWWindowRefreshCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowRefreshCallbackI) -> 'GLFWWindowRefreshCallbackI':
        return GLFWWindowRefreshCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowRefreshCallbackI):
        """
        Dynamic initializer for GLFWWindowRefreshCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowRefreshCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowRefreshCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowRefreshCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowRefreshCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.callback(long,long)"""
        super(_GLFWWindowRefreshCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDeallocateCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWDeallocateCallback as _GLFWDeallocateCallback
_GLFWDeallocateCallback = _GLFWDeallocateCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWDeallocateCallbackI as _GLFWDeallocateCallbackI
_GLFWDeallocateCallbackI = _GLFWDeallocateCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWDeallocateCallback():
    """org.lwjgl.glfw.GLFWDeallocateCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWDeallocateCallback) -> 'GLFWDeallocateCallback':
        return GLFWDeallocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWDeallocateCallback):
        """
        Dynamic initializer for GLFWDeallocateCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWDeallocateCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWDeallocateCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWDeallocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDeallocateCallbackI.callback(long,long)"""
        super(_GLFWDeallocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDeallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWDeallocateCallbackI, self).getCallInterface())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.createSafe(long)"""
        return GLFWDeallocateCallback._wrap(_GLFWDeallocateCallback.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.create(long)"""
        return GLFWDeallocateCallback._wrap(_GLFWDeallocateCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWDeallocateCallbackI') -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.create(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return GLFWDeallocateCallback._wrap(_GLFWDeallocateCallback.create(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowIconifyCallbackI
from pyquantum_helper import import_once as _import_once
import org.lwjgl.glfw.GLFWWindowIconifyCallbackI as _GLFWWindowIconifyCallbackI
_GLFWWindowIconifyCallbackI = _GLFWWindowIconifyCallbackI
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowIconifyCallbackI():
    """org.lwjgl.glfw.GLFWWindowIconifyCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowIconifyCallbackI) -> 'GLFWWindowIconifyCallbackI':
        return GLFWWindowIconifyCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowIconifyCallbackI):
        """
        Dynamic initializer for GLFWWindowIconifyCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowIconifyCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowIconifyCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowIconifyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowIconifyCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.callback(long,long)"""
        super(_GLFWWindowIconifyCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowPosCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWWindowPosCallback as _GLFWWindowPosCallback
_GLFWWindowPosCallback = _GLFWWindowPosCallback
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowPosCallbackI as _GLFWWindowPosCallbackI
_GLFWWindowPosCallbackI = _GLFWWindowPosCallbackI
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowPosCallback():
    """org.lwjgl.glfw.GLFWWindowPosCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowPosCallback) -> 'GLFWWindowPosCallback':
        return GLFWWindowPosCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowPosCallback):
        """
        Dynamic initializer for GLFWWindowPosCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowPosCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowPosCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowPosCallbackI, self).getCallInterface())

    @overload
    def set(self, arg0: int) -> 'GLFWWindowPosCallback':
        """public org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.set(long)"""
        return 'GLFWWindowPosCallback'._wrap(super(_GLFWWindowPosCallback, self).set(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowPosCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowPosCallbackI') -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.create(org.lwjgl.glfw.GLFWWindowPosCallbackI)"""
        return GLFWWindowPosCallback._wrap(_GLFWWindowPosCallback.create(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowPosCallbackI.callback(long,long)"""
        super(_GLFWWindowPosCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.create(long)"""
        return GLFWWindowPosCallback._wrap(_GLFWWindowPosCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.createSafe(long)"""
        return GLFWWindowPosCallback._wrap(_GLFWWindowPosCallback.createSafe(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWMouseButtonCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWMouseButtonCallbackI as _GLFWMouseButtonCallbackI
_GLFWMouseButtonCallbackI = _GLFWMouseButtonCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWMouseButtonCallbackI():
    """org.lwjgl.glfw.GLFWMouseButtonCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWMouseButtonCallbackI) -> 'GLFWMouseButtonCallbackI':
        return GLFWMouseButtonCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWMouseButtonCallbackI):
        """
        Dynamic initializer for GLFWMouseButtonCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWMouseButtonCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWMouseButtonCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMouseButtonCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWMouseButtonCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(long,long)"""
        super(_GLFWMouseButtonCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void org.lwjgl.glfw.GLFWMouseButtonCallbackI.invoke(long,int,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowSizeCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWWindowSizeCallback as _GLFWWindowSizeCallback
_GLFWWindowSizeCallback = _GLFWWindowSizeCallback
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import org.lwjgl.glfw.GLFWWindowSizeCallbackI as _GLFWWindowSizeCallbackI
_GLFWWindowSizeCallbackI = _GLFWWindowSizeCallbackI
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowSizeCallback():
    """org.lwjgl.glfw.GLFWWindowSizeCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowSizeCallback) -> 'GLFWWindowSizeCallback':
        return GLFWWindowSizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowSizeCallback):
        """
        Dynamic initializer for GLFWWindowSizeCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowSizeCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowSizeCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowSizeCallbackI.callback(long,long)"""
        super(_GLFWWindowSizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowSizeCallbackI') -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.create(org.lwjgl.glfw.GLFWWindowSizeCallbackI)"""
        return GLFWWindowSizeCallback._wrap(_GLFWWindowSizeCallback.create(arg0))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @overload
    def set(self, arg0: int) -> 'GLFWWindowSizeCallback':
        """public org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.set(long)"""
        return 'GLFWWindowSizeCallback'._wrap(super(_GLFWWindowSizeCallback, self).set(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.create(long)"""
        return GLFWWindowSizeCallback._wrap(_GLFWWindowSizeCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.createSafe(long)"""
        return GLFWWindowSizeCallback._wrap(_GLFWWindowSizeCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowSizeCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGamepadState
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.lang.String as _String
_String = _String
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Float as _float
import org.lwjgl.glfw.GLFWGamepadState as _GLFWGamepadState_Buffer
_Buffer = _GLFWGamepadState_Buffer.Buffer
import java.lang.Integer as _int
import java.lang.Byte as _byte
import org.lwjgl.glfw.GLFWGamepadState as _GLFWGamepadState
_GLFWGamepadState = _GLFWGamepadState
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWGamepadState():
    """org.lwjgl.glfw.GLFWGamepadState"""
 
    @staticmethod
    def _wrap(java_value: _GLFWGamepadState) -> 'GLFWGamepadState':
        return GLFWGamepadState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWGamepadState):
        """
        Dynamic initializer for GLFWGamepadState.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWGamepadState__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWGamepadState__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.mallocStack(int)"""
        return Buffer._wrap(_GLFWGamepadState.mallocStack(_int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'FloatBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.set(java.nio.ByteBuffer,java.nio.FloatBuffer)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).set(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: int) -> float:
        """public static float org.lwjgl.glfw.GLFWGamepadState.naxes(long,int)"""
        return float._wrap(_GLFWGamepadState.naxes(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.mallocStack()"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.mallocStack())

    @overload
    def buttons(self, arg0: int, arg1: int) -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.buttons(int,byte)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).buttons(_int.valueOf(arg0), _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def naxes(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState.naxes(long)"""
        return FloatBuffer._wrap(_GLFWGamepadState.naxes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.callocStack()"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.callocStack())

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def calloc() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.calloc()"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.calloc())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWGamepadState.sizeof()"""
        return int._wrap(super(GLFWGamepadState, self).sizeof())

    @overload
    def buttons(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState.buttons()"""
        return 'ByteBuffer'._wrap(super(GLFWGamepadState, self).buttons())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.createSafe(long,int)"""
        return Buffer._wrap(_GLFWGamepadState.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def axes(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState.axes()"""
        return 'FloatBuffer'._wrap(super(GLFWGamepadState, self).axes())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.callocStack(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGamepadState(java.nio.ByteBuffer)"""
        val = _GLFWGamepadState(arg0)
        self.__wrapper = val

    @overload
    def axes(self, arg0: 'FloatBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.axes(java.nio.FloatBuffer)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).axes(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def set(self, arg0: 'GLFWGamepadState') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.set(org.lwjgl.glfw.GLFWGamepadState)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).set(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.create(int)"""
        return Buffer._wrap(_GLFWGamepadState.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGamepadState.callocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: int, arg2: float):
        """public static void org.lwjgl.glfw.GLFWGamepadState.naxes(long,int,float)"""
        _GLFWGamepadState.naxes(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))

    @staticmethod
    @overload
    def nbuttons(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState.nbuttons(long)"""
        return ByteBuffer._wrap(_GLFWGamepadState.nbuttons(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFWGamepadState.naxes(long,java.nio.FloatBuffer)"""
        _GLFWGamepadState.naxes(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.callocStack(int)"""
        return Buffer._wrap(_GLFWGamepadState.callocStack(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGamepadState.malloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def buttons(self, arg0: 'ByteBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.buttons(java.nio.ByteBuffer)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).buttons(arg0))

    @staticmethod
    @overload
    def nbuttons(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,java.nio.ByteBuffer)"""
        _GLFWGamepadState.nbuttons(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.calloc(int)"""
        return Buffer._wrap(_GLFWGamepadState.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGamepadState.calloc(_int.valueOf(arg0), arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @overload
    def axes(self, arg0: int) -> float:
        """public float org.lwjgl.glfw.GLFWGamepadState.axes(int)"""
        return float._wrap(super(_GLFWGamepadState, self).axes(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.mallocStack(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGamepadState.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nbuttons(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,int)"""
        return int._wrap(_GLFWGamepadState.nbuttons(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.malloc(int)"""
        return Buffer._wrap(_GLFWGamepadState.malloc(_int.valueOf(arg0)))

    @overload
    def buttons(self, arg0: int) -> int:
        """public byte org.lwjgl.glfw.GLFWGamepadState.buttons(int)"""
        return int._wrap(super(_GLFWGamepadState, self).buttons(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.create(long)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.create()"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.create())

    @staticmethod
    @overload
    def nbuttons(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,int,byte)"""
        _GLFWGamepadState.nbuttons(_long.valueOf(arg0), _int.valueOf(arg1), _byte.valueOf(arg2))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def malloc() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.malloc()"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.malloc())

    @overload
    def axes(self, arg0: int, arg1: float) -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.axes(int,float)"""
        return 'GLFWGamepadState'._wrap(super(_GLFWGamepadState, self).axes(_int.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.create(long,int)"""
        return Buffer._wrap(_GLFWGamepadState.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.createSafe(long)"""
        return GLFWGamepadState._wrap(_GLFWGamepadState.createSafe(_long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWErrorCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWErrorCallbackI as _GLFWErrorCallbackI
_GLFWErrorCallbackI = _GLFWErrorCallbackI
import org.lwjgl.glfw.GLFWErrorCallback as _GLFWErrorCallback
_GLFWErrorCallback = _GLFWErrorCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWErrorCallback():
    """org.lwjgl.glfw.GLFWErrorCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWErrorCallback) -> 'GLFWErrorCallback':
        return GLFWErrorCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWErrorCallback):
        """
        Dynamic initializer for GLFWErrorCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWErrorCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWErrorCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createPrint() -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createPrint()"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.createPrint())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: 'GLFWErrorCallbackI') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.create(org.lwjgl.glfw.GLFWErrorCallbackI)"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.create(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createSafe(long)"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWErrorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWErrorCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

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

    @staticmethod
    @overload
    def createThrow() -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createThrow()"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.createThrow())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWErrorCallbackI.callback(long,long)"""
        super(_GLFWErrorCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createPrint(arg0: 'PrintStream') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createPrint(java.io.PrintStream)"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.createPrint(arg0))

    @overload
    def set(self) -> 'GLFWErrorCallback':
        """public org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.set()"""
        return 'GLFWErrorCallback'._wrap(super(GLFWErrorCallback, self).set())

    @staticmethod
    @overload
    def getDescription(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWErrorCallback.getDescription(long)"""
        return str._wrap(_GLFWErrorCallback.getDescription(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWErrorCallbackI.invoke(int,long)"""
        pass

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.create(long)"""
        return GLFWErrorCallback._wrap(_GLFWErrorCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWDropCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWDropCallbackI as _GLFWDropCallbackI
_GLFWDropCallbackI = _GLFWDropCallbackI
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWDropCallbackI():
    """org.lwjgl.glfw.GLFWDropCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWDropCallbackI) -> 'GLFWDropCallbackI':
        return GLFWDropCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWDropCallbackI):
        """
        Dynamic initializer for GLFWDropCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWDropCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWDropCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDropCallbackI.callback(long,long)"""
        super(_GLFWDropCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWDropCallbackI.invoke(long,int,long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDropCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWDropCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeNSGL$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import org.lwjgl.glfw.GLFWNativeNSGL as _GLFWNativeNSGL_Functions
_Functions = _GLFWNativeNSGL_Functions.Functions
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeNSGL.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWJoystickCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWJoystickCallbackI as _GLFWJoystickCallbackI
_GLFWJoystickCallbackI = _GLFWJoystickCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWJoystickCallbackI():
    """org.lwjgl.glfw.GLFWJoystickCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWJoystickCallbackI) -> 'GLFWJoystickCallbackI':
        return GLFWJoystickCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWJoystickCallbackI):
        """
        Dynamic initializer for GLFWJoystickCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWJoystickCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWJoystickCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWJoystickCallbackI.invoke(int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWJoystickCallbackI.callback(long,long)"""
        super(_GLFWJoystickCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWJoystickCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWJoystickCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorEnterCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWCursorEnterCallbackI as _GLFWCursorEnterCallbackI
_GLFWCursorEnterCallbackI = _GLFWCursorEnterCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWCursorEnterCallbackI():
    """org.lwjgl.glfw.GLFWCursorEnterCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCursorEnterCallbackI) -> 'GLFWCursorEnterCallbackI':
        return GLFWCursorEnterCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCursorEnterCallbackI):
        """
        Dynamic initializer for GLFWCursorEnterCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCursorEnterCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCursorEnterCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorEnterCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCursorEnterCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorEnterCallbackI.callback(long,long)"""
        super(_GLFWCursorEnterCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWCursorEnterCallbackI.invoke(long,boolean)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorPosCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWCursorPosCallbackI as _GLFWCursorPosCallbackI
_GLFWCursorPosCallbackI = _GLFWCursorPosCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWCursorPosCallbackI():
    """org.lwjgl.glfw.GLFWCursorPosCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCursorPosCallbackI) -> 'GLFWCursorPosCallbackI':
        return GLFWCursorPosCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCursorPosCallbackI):
        """
        Dynamic initializer for GLFWCursorPosCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCursorPosCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCursorPosCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCursorPosCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorPosCallbackI.callback(long,long)"""
        super(_GLFWCursorPosCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWCursorPosCallbackI.invoke(long,double,double)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWGamepadState$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.glfw.GLFWGamepadState as _GLFWGamepadState_Buffer
_Buffer = _GLFWGamepadState_Buffer.Buffer
import java.lang.Byte as _byte
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
from builtins import float
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Float as _float
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.glfw.GLFWGamepadState.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @overload
    def buttons(self, arg0: int) -> int:
        """public byte org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(int)"""
        return int._wrap(super(_Buffer, self).buttons(_int.valueOf(arg0)))

    @overload
    def axes(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes()"""
        return 'FloatBuffer'._wrap(super(Buffer, self).axes())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @overload
    def axes(self, arg0: 'FloatBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(java.nio.FloatBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).axes(arg0))

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def buttons(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons()"""
        return 'ByteBuffer'._wrap(super(Buffer, self).buttons())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def buttons(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).buttons(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @overload
    def axes(self, arg0: int, arg1: float) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(int,float)"""
        return 'Buffer'._wrap(super(_Buffer, self).axes(_int.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @overload
    def axes(self, arg0: int) -> float:
        """public float org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(int)"""
        return float._wrap(super(_Buffer, self).axes(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def buttons(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(int,byte)"""
        return 'Buffer'._wrap(super(_Buffer, self).buttons(_int.valueOf(arg0), _byte.valueOf(arg1)))

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGammaRamp
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.nio.ShortBuffer as ShortBuffer
import java.lang.String as _String
_String = _String
import org.lwjgl.glfw.GLFWGammaRamp as _GLFWGammaRamp
_GLFWGammaRamp = _GLFWGammaRamp
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWGammaRamp as _GLFWGammaRamp_Buffer
_Buffer = _GLFWGammaRamp_Buffer.Buffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ShortBuffer as _ShortBuffer
_ShortBuffer = _ShortBuffer
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWGammaRamp():
    """org.lwjgl.glfw.GLFWGammaRamp"""
 
    @staticmethod
    def _wrap(java_value: _GLFWGammaRamp) -> 'GLFWGammaRamp':
        return GLFWGammaRamp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWGammaRamp):
        """
        Dynamic initializer for GLFWGammaRamp.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWGammaRamp__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWGammaRamp__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.createSafe(long,int)"""
        return Buffer._wrap(_GLFWGammaRamp.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def blue(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.blue(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).blue(arg0))

    @overload
    def size(self, arg0: int) -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.size(int)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).size(_int.valueOf(arg0)))

    @overload
    def blue(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.blue()"""
        return 'ShortBuffer'._wrap(super(GLFWGammaRamp, self).blue())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGammaRamp.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nblue(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.nblue(long)"""
        return ShortBuffer._wrap(_GLFWGammaRamp.nblue(_long.valueOf(arg0)))

    @overload
    def green(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.green(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).green(arg0))

    @staticmethod
    @overload
    def ngreen(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.ngreen(long)"""
        return ShortBuffer._wrap(_GLFWGammaRamp.ngreen(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGammaRamp.mallocStack(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.malloc(arg0))

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.malloc(int)"""
        return Buffer._wrap(_GLFWGammaRamp.malloc(_int.valueOf(arg0)))

    @overload
    def red(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.red()"""
        return 'ShortBuffer'._wrap(super(GLFWGammaRamp, self).red())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.createSafe(long)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.createSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: 'GLFWGammaRamp') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.set(org.lwjgl.glfw.GLFWGammaRamp)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).set(arg0))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGammaRamp.calloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.create(long,int)"""
        return Buffer._wrap(_GLFWGammaRamp.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def create() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.create()"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.create())

    @overload
    def red(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.red(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).red(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.calloc(arg0))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.validate(long)"""
        _GLFWGammaRamp.validate(_long.valueOf(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp.sizeof()"""
        return int._wrap(super(GLFWGammaRamp, self).sizeof())

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.mallocStack()"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.mallocStack())

    @staticmethod
    @overload
    def nsize(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWGammaRamp.nsize(long)"""
        return int._wrap(_GLFWGammaRamp.nsize(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.malloc()"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.malloc())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.calloc(int)"""
        return Buffer._wrap(_GLFWGammaRamp.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.calloc()"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.calloc())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.mallocStack(int)"""
        return Buffer._wrap(_GLFWGammaRamp.mallocStack(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def callocStack() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.callocStack()"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.callocStack())

    @overload
    def set(self, arg0: 'ShortBuffer', arg1: 'ShortBuffer', arg2: 'ShortBuffer', arg3: int) -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.set(java.nio.ShortBuffer,java.nio.ShortBuffer,java.nio.ShortBuffer,int)"""
        return 'GLFWGammaRamp'._wrap(super(_GLFWGammaRamp, self).set(arg0, arg1, arg2, _int.valueOf(arg3)))

    @staticmethod
    @overload
    def nblue(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nblue(long,java.nio.ShortBuffer)"""
        _GLFWGammaRamp.nblue(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWGammaRamp.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.create(int)"""
        return Buffer._wrap(_GLFWGammaRamp.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.mallocStack(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGammaRamp(java.nio.ByteBuffer)"""
        val = _GLFWGammaRamp(arg0)
        self.__wrapper = val

    @overload
    def size(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp.size()"""
        return int._wrap(super(GLFWGammaRamp, self).size())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.create(long)"""
        return GLFWGammaRamp._wrap(_GLFWGammaRamp.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ngreen(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.ngreen(long,java.nio.ShortBuffer)"""
        _GLFWGammaRamp.ngreen(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nred(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.nred(long)"""
        return ShortBuffer._wrap(_GLFWGammaRamp.nred(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nsize(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nsize(long,int)"""
        _GLFWGammaRamp.nsize(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def nred(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nred(long,java.nio.ShortBuffer)"""
        _GLFWGammaRamp.nred(_long.valueOf(arg0), arg1)

    @overload
    def green(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.green()"""
        return 'ShortBuffer'._wrap(super(GLFWGammaRamp, self).green())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.callocStack(int)"""
        return Buffer._wrap(_GLFWGammaRamp.callocStack(_int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowContentScaleCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowContentScaleCallbackI as _GLFWWindowContentScaleCallbackI
_GLFWWindowContentScaleCallbackI = _GLFWWindowContentScaleCallbackI
import org.lwjgl.glfw.GLFWWindowContentScaleCallback as _GLFWWindowContentScaleCallback
_GLFWWindowContentScaleCallback = _GLFWWindowContentScaleCallback
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowContentScaleCallback():
    """org.lwjgl.glfw.GLFWWindowContentScaleCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowContentScaleCallback) -> 'GLFWWindowContentScaleCallback':
        return GLFWWindowContentScaleCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowContentScaleCallback):
        """
        Dynamic initializer for GLFWWindowContentScaleCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowContentScaleCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowContentScaleCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.create(long)"""
        return GLFWWindowContentScaleCallback._wrap(_GLFWWindowContentScaleCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.invoke(long,float,float)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowContentScaleCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.set(long)"""
        return 'GLFWWindowContentScaleCallback'._wrap(super(_GLFWWindowContentScaleCallback, self).set(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.callback(long,long)"""
        super(_GLFWWindowContentScaleCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.createSafe(long)"""
        return GLFWWindowContentScaleCallback._wrap(_GLFWWindowContentScaleCallback.createSafe(_long.valueOf(arg0)))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowContentScaleCallbackI') -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.create(org.lwjgl.glfw.GLFWWindowContentScaleCallbackI)"""
        return GLFWWindowContentScaleCallback._wrap(_GLFWWindowContentScaleCallback.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWayland$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeWayland as _GLFWNativeWayland_Functions
_Functions = _GLFWNativeWayland_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWayland.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWFramebufferSizeCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWFramebufferSizeCallbackI as _GLFWFramebufferSizeCallbackI
_GLFWFramebufferSizeCallbackI = _GLFWFramebufferSizeCallbackI
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWFramebufferSizeCallbackI():
    """org.lwjgl.glfw.GLFWFramebufferSizeCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWFramebufferSizeCallbackI) -> 'GLFWFramebufferSizeCallbackI':
        return GLFWFramebufferSizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWFramebufferSizeCallbackI):
        """
        Dynamic initializer for GLFWFramebufferSizeCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWFramebufferSizeCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWFramebufferSizeCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.callback(long,long)"""
        super(_GLFWFramebufferSizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWFramebufferSizeCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWImage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWImage as _GLFWImage
_GLFWImage = _GLFWImage
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import org.lwjgl.glfw.GLFWImage as _GLFWImage_Buffer
_Buffer = _GLFWImage_Buffer.Buffer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWImage():
    """org.lwjgl.glfw.GLFWImage"""
 
    @staticmethod
    def _wrap(java_value: _GLFWImage) -> 'GLFWImage':
        return GLFWImage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWImage):
        """
        Dynamic initializer for GLFWImage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWImage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWImage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def calloc() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.calloc()"""
        return GLFWImage._wrap(_GLFWImage.calloc())

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWImage.callocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.calloc(int)"""
        return Buffer._wrap(_GLFWImage.calloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWImage.nheight(long)"""
        return int._wrap(_GLFWImage.nheight(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def create() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.create()"""
        return GLFWImage._wrap(_GLFWImage.create())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.createSafe(long)"""
        return GLFWImage._wrap(_GLFWImage.createSafe(_long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWImage(java.nio.ByteBuffer)"""
        val = _GLFWImage(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWImage._wrap(_GLFWImage.malloc(arg0))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage.npixels(long,int)"""
        return ByteBuffer._wrap(_GLFWImage.npixels(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.mallocStack()"""
        return GLFWImage._wrap(_GLFWImage.mallocStack())

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWImage.nwidth(long)"""
        return int._wrap(_GLFWImage.nwidth(_long.valueOf(arg0)))

    @overload
    def height(self, arg0: int) -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.height(int)"""
        return 'GLFWImage'._wrap(super(_GLFWImage, self).height(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.mallocStack(int)"""
        return Buffer._wrap(_GLFWImage.mallocStack(_int.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def set(self, arg0: 'GLFWImage') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.set(org.lwjgl.glfw.GLFWImage)"""
        return 'GLFWImage'._wrap(super(_GLFWImage, self).set(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.callocStack(int)"""
        return Buffer._wrap(_GLFWImage.callocStack(_int.valueOf(arg0)))

    @overload
    def width(self, arg0: int) -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.width(int)"""
        return 'GLFWImage'._wrap(super(_GLFWImage, self).width(_int.valueOf(arg0)))

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.height()"""
        return int._wrap(super(GLFWImage, self).height())

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWImage.npixels(long,java.nio.ByteBuffer)"""
        _GLFWImage.npixels(_long.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_GLFWImage, self).pixels(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.callocStack()"""
        return GLFWImage._wrap(_GLFWImage.callocStack())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.width()"""
        return int._wrap(super(GLFWImage, self).width())

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.pixels(java.nio.ByteBuffer)"""
        return 'GLFWImage'._wrap(super(_GLFWImage, self).pixels(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWImage.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.malloc()"""
        return GLFWImage._wrap(_GLFWImage.malloc())

    @staticmethod
    @overload
    def nwidth(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWImage.nwidth(long,int)"""
        _GLFWImage.nwidth(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWImage._wrap(_GLFWImage.mallocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.create(int)"""
        return Buffer._wrap(_GLFWImage.create(_int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.sizeof()"""
        return int._wrap(super(GLFWImage, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.createSafe(long,int)"""
        return Buffer._wrap(_GLFWImage.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWImage._wrap(_GLFWImage.callocStack(arg0))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.malloc(int)"""
        return Buffer._wrap(_GLFWImage.malloc(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.create(long,int)"""
        return Buffer._wrap(_GLFWImage.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWImage._wrap(_GLFWImage.calloc(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.create(long)"""
        return GLFWImage._wrap(_GLFWImage.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWImage.validate(long)"""
        _GLFWImage.validate(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: 'ByteBuffer') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.set(int,int,java.nio.ByteBuffer)"""
        return 'GLFWImage'._wrap(super(_GLFWImage, self).set(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWImage.mallocStack(_int.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nheight(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWImage.nheight(long,int)"""
        _GLFWImage.nheight(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWImage.calloc(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWMouseButtonCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import org.lwjgl.glfw.GLFWMouseButtonCallbackI as _GLFWMouseButtonCallbackI
_GLFWMouseButtonCallbackI = _GLFWMouseButtonCallbackI
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import org.lwjgl.glfw.GLFWMouseButtonCallback as _GLFWMouseButtonCallback
_GLFWMouseButtonCallback = _GLFWMouseButtonCallback
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWMouseButtonCallback():
    """org.lwjgl.glfw.GLFWMouseButtonCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWMouseButtonCallback) -> 'GLFWMouseButtonCallback':
        return GLFWMouseButtonCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWMouseButtonCallback):
        """
        Dynamic initializer for GLFWMouseButtonCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWMouseButtonCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWMouseButtonCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.createSafe(long)"""
        return GLFWMouseButtonCallback._wrap(_GLFWMouseButtonCallback.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.create(long)"""
        return GLFWMouseButtonCallback._wrap(_GLFWMouseButtonCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void org.lwjgl.glfw.GLFWMouseButtonCallbackI.invoke(long,int,int,int)"""
        pass

    @overload
    def set(self, arg0: int) -> 'GLFWMouseButtonCallback':
        """public org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.set(long)"""
        return 'GLFWMouseButtonCallback'._wrap(super(_GLFWMouseButtonCallback, self).set(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWMouseButtonCallbackI') -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.create(org.lwjgl.glfw.GLFWMouseButtonCallbackI)"""
        return GLFWMouseButtonCallback._wrap(_GLFWMouseButtonCallback.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMouseButtonCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWMouseButtonCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(long,long)"""
        super(_GLFWMouseButtonCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowPosCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowPosCallbackI as _GLFWWindowPosCallbackI
_GLFWWindowPosCallbackI = _GLFWWindowPosCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowPosCallbackI():
    """org.lwjgl.glfw.GLFWWindowPosCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowPosCallbackI) -> 'GLFWWindowPosCallbackI':
        return GLFWWindowPosCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowPosCallbackI):
        """
        Dynamic initializer for GLFWWindowPosCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowPosCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowPosCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowPosCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowPosCallbackI.callback(long,long)"""
        super(_GLFWWindowPosCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowPosCallbackI.invoke(long,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharModsCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWCharModsCallbackI as _GLFWCharModsCallbackI
_GLFWCharModsCallbackI = _GLFWCharModsCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWCharModsCallbackI():
    """org.lwjgl.glfw.GLFWCharModsCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCharModsCallbackI) -> 'GLFWCharModsCallbackI':
        return GLFWCharModsCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCharModsCallbackI):
        """
        Dynamic initializer for GLFWCharModsCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCharModsCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCharModsCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharModsCallbackI.callback(long,long)"""
        super(_GLFWCharModsCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharModsCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCharModsCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWCharModsCallbackI.invoke(long,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWayland
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeWayland as _GLFWNativeWayland
_GLFWNativeWayland = _GLFWNativeWayland
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeWayland():
    """org.lwjgl.glfw.GLFWNativeWayland"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeWayland) -> 'GLFWNativeWayland':
        return GLFWNativeWayland(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeWayland):
        """
        Dynamic initializer for GLFWNativeWayland.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeWayland__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeWayland__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWaylandMonitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandMonitor(long)"""
        return int._wrap(_GLFWNativeWayland.glfwGetWaylandMonitor(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def glfwGetWaylandDisplay() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandDisplay()"""
        return int._wrap(_GLFWNativeWayland.glfwGetWaylandDisplay())

    @staticmethod
    @overload
    def glfwGetWaylandWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandWindow(long)"""
        return int._wrap(_GLFWNativeWayland.glfwGetWaylandWindow(_long.valueOf(arg0)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeX11
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWNativeX11 as _GLFWNativeX11
_GLFWNativeX11 = _GLFWNativeX11
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeX11():
    """org.lwjgl.glfw.GLFWNativeX11"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeX11) -> 'GLFWNativeX11':
        return GLFWNativeX11(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeX11):
        """
        Dynamic initializer for GLFWNativeX11.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeX11__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeX11__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def glfwSetX11SelectionString(arg0: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.lang.CharSequence)"""
        _GLFWNativeX11.glfwSetX11SelectionString(arg0)

    @staticmethod
    @overload
    def glfwGetX11Window(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Window(long)"""
        return int._wrap(_GLFWNativeX11.glfwGetX11Window(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetX11SelectionString(arg0: int):
        """public static void org.lwjgl.glfw.GLFWNativeX11.nglfwSetX11SelectionString(long)"""
        _GLFWNativeX11.nglfwSetX11SelectionString(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetX11SelectionString() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.nglfwGetX11SelectionString()"""
        return int._wrap(_GLFWNativeX11.nglfwGetX11SelectionString())

    @staticmethod
    @overload
    def glfwGetX11Adapter(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Adapter(long)"""
        return int._wrap(_GLFWNativeX11.glfwGetX11Adapter(_long.valueOf(arg0)))

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
    def glfwGetX11Display() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Display()"""
        return int._wrap(_GLFWNativeX11.glfwGetX11Display())

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

    @staticmethod
    @overload
    def glfwGetX11Monitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Monitor(long)"""
        return int._wrap(_GLFWNativeX11.glfwGetX11Monitor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetX11SelectionString() -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeX11.glfwGetX11SelectionString()"""
        return str._wrap(_GLFWNativeX11.glfwGetX11SelectionString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwSetX11SelectionString(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.nio.ByteBuffer)"""
        _GLFWNativeX11.glfwSetX11SelectionString(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeCocoa
from builtins import str
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWNativeCocoa as _GLFWNativeCocoa
_GLFWNativeCocoa = _GLFWNativeCocoa
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeCocoa():
    """org.lwjgl.glfw.GLFWNativeCocoa"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeCocoa) -> 'GLFWNativeCocoa':
        return GLFWNativeCocoa(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeCocoa):
        """
        Dynamic initializer for GLFWNativeCocoa.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeCocoa__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeCocoa__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetCocoaWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeCocoa.glfwGetCocoaWindow(long)"""
        return int._wrap(_GLFWNativeCocoa.glfwGetCocoaWindow(_long.valueOf(arg0)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetCocoaMonitor(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeCocoa.glfwGetCocoaMonitor(long)"""
        return int._wrap(_GLFWNativeCocoa.glfwGetCocoaMonitor(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowFocusCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWWindowFocusCallbackI as _GLFWWindowFocusCallbackI
_GLFWWindowFocusCallbackI = _GLFWWindowFocusCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowFocusCallbackI():
    """org.lwjgl.glfw.GLFWWindowFocusCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowFocusCallbackI) -> 'GLFWWindowFocusCallbackI':
        return GLFWWindowFocusCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowFocusCallbackI):
        """
        Dynamic initializer for GLFWWindowFocusCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowFocusCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowFocusCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowFocusCallbackI.callback(long,long)"""
        super(_GLFWWindowFocusCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowFocusCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowFocusCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowFocusCallbackI.invoke(long,boolean)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowMaximizeCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWWindowMaximizeCallbackI as _GLFWWindowMaximizeCallbackI
_GLFWWindowMaximizeCallbackI = _GLFWWindowMaximizeCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowMaximizeCallbackI():
    """org.lwjgl.glfw.GLFWWindowMaximizeCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowMaximizeCallbackI) -> 'GLFWWindowMaximizeCallbackI':
        return GLFWWindowMaximizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowMaximizeCallbackI):
        """
        Dynamic initializer for GLFWWindowMaximizeCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowMaximizeCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowMaximizeCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.callback(long,long)"""
        super(_GLFWWindowMaximizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowMaximizeCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVidMode
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.glfw.GLFWVidMode as _GLFWVidMode_Buffer
_Buffer = _GLFWVidMode_Buffer.Buffer
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.glfw.GLFWVidMode as _GLFWVidMode
_GLFWVidMode = _GLFWVidMode
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWVidMode():
    """org.lwjgl.glfw.GLFWVidMode"""
 
    @staticmethod
    def _wrap(java_value: _GLFWVidMode) -> 'GLFWVidMode':
        return GLFWVidMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWVidMode):
        """
        Dynamic initializer for GLFWVidMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWVidMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWVidMode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.height()"""
        return int._wrap(super(GLFWVidMode, self).height())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.sizeof()"""
        return int._wrap(super(GLFWVidMode, self).sizeof())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFWVidMode.createSafe(long,int)"""
        return Buffer._wrap(_GLFWVidMode.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWVidMode(java.nio.ByteBuffer)"""
        val = _GLFWVidMode(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nwidth(long)"""
        return int._wrap(_GLFWVidMode.nwidth(_long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFWVidMode.createSafe(long)"""
        return GLFWVidMode._wrap(_GLFWVidMode.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def blueBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.blueBits()"""
        return int._wrap(super(GLFWVidMode, self).blueBits())

    @overload
    def refreshRate(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.refreshRate()"""
        return int._wrap(super(GLFWVidMode, self).refreshRate())

    @staticmethod
    @overload
    def nblueBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nblueBits(long)"""
        return int._wrap(_GLFWVidMode.nblueBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def ngreenBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.ngreenBits(long)"""
        return int._wrap(_GLFWVidMode.ngreenBits(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nheight(long)"""
        return int._wrap(_GLFWVidMode.nheight(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFWVidMode.create(long)"""
        return GLFWVidMode._wrap(_GLFWVidMode.create(_long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def greenBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.greenBits()"""
        return int._wrap(super(GLFWVidMode, self).greenBits())

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.width()"""
        return int._wrap(super(GLFWVidMode, self).width())

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def redBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.redBits()"""
        return int._wrap(super(GLFWVidMode, self).redBits())

    @staticmethod
    @overload
    def nrefreshRate(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nrefreshRate(long)"""
        return int._wrap(_GLFWVidMode.nrefreshRate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFWVidMode.create(long,int)"""
        return Buffer._wrap(_GLFWVidMode.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nredBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nredBits(long)"""
        return int._wrap(_GLFWVidMode.nredBits(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocator
from pyquantum_helper import import_once as _import_once
import org.lwjgl.glfw.GLFWAllocateCallback as _GLFWAllocateCallback
_GLFWAllocateCallback = _GLFWAllocateCallback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWAllocator as _GLFWAllocator
_GLFWAllocator = _GLFWAllocator
import org.lwjgl.glfw.GLFWReallocateCallback as _GLFWReallocateCallback
_GLFWReallocateCallback = _GLFWReallocateCallback
import org.lwjgl.glfw.GLFWDeallocateCallback as _GLFWDeallocateCallback
_GLFWDeallocateCallback = _GLFWDeallocateCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.glfw.GLFWAllocator as _GLFWAllocator_Buffer
_Buffer = _GLFWAllocator_Buffer.Buffer
import java.lang.Integer as _int
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWAllocator():
    """org.lwjgl.glfw.GLFWAllocator"""
 
    @staticmethod
    def _wrap(java_value: _GLFWAllocator) -> 'GLFWAllocator':
        return GLFWAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWAllocator):
        """
        Dynamic initializer for GLFWAllocator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWAllocator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWAllocator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def allocate(self, arg0: 'GLFWAllocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.allocate(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).allocate(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.create(int)"""
        return Buffer._wrap(_GLFWAllocator.create(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWAllocator._wrap(_GLFWAllocator.calloc(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nuser(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWAllocator.nuser(long)"""
        return int._wrap(_GLFWAllocator.nuser(_long.valueOf(arg0)))

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def user(self, arg0: int) -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.user(long)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).user(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWAllocator._wrap(_GLFWAllocator.malloc(arg0))

    @staticmethod
    @overload
    def nallocate(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator.nallocate(long)"""
        return GLFWAllocateCallback._wrap(_GLFWAllocator.nallocate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nreallocate(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator.nreallocate(long)"""
        return GLFWReallocateCallback._wrap(_GLFWAllocator.nreallocate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.malloc()"""
        return GLFWAllocator._wrap(_GLFWAllocator.malloc())

    @staticmethod
    @overload
    def nreallocate(arg0: int, arg1: 'GLFWReallocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.nreallocate(long,org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        _GLFWAllocator.nreallocate(_long.valueOf(arg0), arg1)

    @overload
    def set(self, arg0: 'GLFWAllocator') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.set(org.lwjgl.glfw.GLFWAllocator)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).set(arg0))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def ndeallocate(arg0: int, arg1: 'GLFWDeallocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.ndeallocate(long,org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        _GLFWAllocator.ndeallocate(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        _Struct.validate(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), arg3)

    @override
    @overload
    def clear(self):
        """public void org.lwjgl.system.Struct.clear()"""
        super(pyglsystem.Struct, self).clear()

    @overload
    def allocate(self) -> 'GLFWAllocateCallback':
        """public org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator.allocate()"""
        return 'GLFWAllocateCallback'._wrap(super(GLFWAllocator, self).allocate())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.createSafe(long)"""
        return GLFWAllocator._wrap(_GLFWAllocator.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.create()"""
        return GLFWAllocator._wrap(_GLFWAllocator.create())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWAllocator.calloc(_int.valueOf(arg0), arg1))

    @overload
    def deallocate(self, arg0: 'GLFWDeallocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.deallocate(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).deallocate(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.create(long)"""
        return GLFWAllocator._wrap(_GLFWAllocator.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nallocate(arg0: int, arg1: 'GLFWAllocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.nallocate(long,org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        _GLFWAllocator.nallocate(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer._wrap(_GLFWAllocator.malloc(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.malloc(int)"""
        return Buffer._wrap(_GLFWAllocator.malloc(_int.valueOf(arg0)))

    @overload
    def user(self) -> int:
        """public long org.lwjgl.glfw.GLFWAllocator.user()"""
        return int._wrap(super(GLFWAllocator, self).user())

    @staticmethod
    @overload
    def calloc() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.calloc()"""
        return GLFWAllocator._wrap(_GLFWAllocator.calloc())

    @overload
    def reallocate(self, arg0: 'GLFWReallocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.reallocate(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).reallocate(arg0))

    @overload
    def deallocate(self) -> 'GLFWDeallocateCallback':
        """public org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator.deallocate()"""
        return 'GLFWDeallocateCallback'._wrap(super(GLFWAllocator, self).deallocate())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.createSafe(long,int)"""
        return Buffer._wrap(_GLFWAllocator.createSafe(_long.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWAllocator(java.nio.ByteBuffer)"""
        val = _GLFWAllocator(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.calloc(int)"""
        return Buffer._wrap(_GLFWAllocator.calloc(_int.valueOf(arg0)))

    @overload
    def reallocate(self) -> 'GLFWReallocateCallback':
        """public org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator.reallocate()"""
        return 'GLFWReallocateCallback'._wrap(super(GLFWAllocator, self).reallocate())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWAllocator.validate(long)"""
        _GLFWAllocator.validate(_long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool._wrap(super(_pyglsystem.Struct, self).isNull(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def ndeallocate(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator.ndeallocate(long)"""
        return GLFWDeallocateCallback._wrap(_GLFWAllocator.ndeallocate(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nuser(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWAllocator.nuser(long,long)"""
        _GLFWAllocator.nuser(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWAllocator.sizeof()"""
        return int._wrap(super(GLFWAllocator, self).sizeof())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.create(long,int)"""
        return Buffer._wrap(_GLFWAllocator.create(_long.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str._wrap(super(pyglsystem.Pointer$Default, self).toString())

    @overload
    def set(self, arg0: 'GLFWAllocateCallbackI', arg1: 'GLFWReallocateCallbackI', arg2: 'GLFWDeallocateCallbackI', arg3: int) -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.set(org.lwjgl.glfw.GLFWAllocateCallbackI,org.lwjgl.glfw.GLFWReallocateCallbackI,org.lwjgl.glfw.GLFWDeallocateCallbackI,long)"""
        return 'GLFWAllocator'._wrap(super(_GLFWAllocator, self).set(arg0, arg1, arg2, _long.valueOf(arg3))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWFramebufferSizeCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import org.lwjgl.glfw.GLFWFramebufferSizeCallback as _GLFWFramebufferSizeCallback
_GLFWFramebufferSizeCallback = _GLFWFramebufferSizeCallback
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWFramebufferSizeCallbackI as _GLFWFramebufferSizeCallbackI
_GLFWFramebufferSizeCallbackI = _GLFWFramebufferSizeCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWFramebufferSizeCallback():
    """org.lwjgl.glfw.GLFWFramebufferSizeCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWFramebufferSizeCallback) -> 'GLFWFramebufferSizeCallback':
        return GLFWFramebufferSizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWFramebufferSizeCallback):
        """
        Dynamic initializer for GLFWFramebufferSizeCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWFramebufferSizeCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWFramebufferSizeCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.create(long)"""
        return GLFWFramebufferSizeCallback._wrap(_GLFWFramebufferSizeCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.createSafe(long)"""
        return GLFWFramebufferSizeCallback._wrap(_GLFWFramebufferSizeCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWFramebufferSizeCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def set(self, arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.set(long)"""
        return 'GLFWFramebufferSizeCallback'._wrap(super(_GLFWFramebufferSizeCallback, self).set(_long.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.callback(long,long)"""
        super(_GLFWFramebufferSizeCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'GLFWFramebufferSizeCallbackI') -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.create(org.lwjgl.glfw.GLFWFramebufferSizeCallbackI)"""
        return GLFWFramebufferSizeCallback._wrap(_GLFWFramebufferSizeCallback.create(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeOSMesa$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeOSMesa as _GLFWNativeOSMesa_Functions
_Functions = _GLFWNativeOSMesa_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeOSMesa.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocator$Buffer
from pyquantum_helper import import_once as _import_once
import org.lwjgl.glfw.GLFWAllocateCallback as _GLFWAllocateCallback
_GLFWAllocateCallback = _GLFWAllocateCallback
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWDeallocateCallback as _GLFWDeallocateCallback
_GLFWDeallocateCallback = _GLFWDeallocateCallback
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import org.lwjgl.glfw.GLFWReallocateCallback as _GLFWReallocateCallback
_GLFWReallocateCallback = _GLFWReallocateCallback
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.lwjgl.glfw.GLFWAllocator as _GLFWAllocator_Buffer
_Buffer = _GLFWAllocator_Buffer.Buffer
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.glfw.GLFWAllocator.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def allocate(self) -> 'GLFWAllocateCallback':
        """public org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.allocate()"""
        return 'GLFWAllocateCallback'._wrap(super(Buffer, self).allocate())

    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def reallocate(self) -> 'GLFWReallocateCallback':
        """public org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.reallocate()"""
        return 'GLFWReallocateCallback'._wrap(super(Buffer, self).reallocate())

    @overload
    def user(self) -> int:
        """public long org.lwjgl.glfw.GLFWAllocator$Buffer.user()"""
        return int._wrap(super(Buffer, self).user())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def user(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.user(long)"""
        return 'Buffer'._wrap(super(_Buffer, self).user(_long.valueOf(arg0)))

    @overload
    def allocate(self, arg0: 'GLFWAllocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.allocate(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).allocate(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWAllocator$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def reallocate(self, arg0: 'GLFWReallocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.reallocate(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).reallocate(arg0))

    @overload
    def deallocate(self, arg0: 'GLFWDeallocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.deallocate(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return 'Buffer'._wrap(super(_Buffer, self).deallocate(arg0))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWAllocator$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def deallocate(self) -> 'GLFWDeallocateCallback':
        """public org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.deallocate()"""
        return 'GLFWDeallocateCallback'._wrap(super(Buffer, self).deallocate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorPosCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWCursorPosCallback as _GLFWCursorPosCallback
_GLFWCursorPosCallback = _GLFWCursorPosCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWCursorPosCallbackI as _GLFWCursorPosCallbackI
_GLFWCursorPosCallbackI = _GLFWCursorPosCallbackI
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWCursorPosCallback():
    """org.lwjgl.glfw.GLFWCursorPosCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCursorPosCallback) -> 'GLFWCursorPosCallback':
        return GLFWCursorPosCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCursorPosCallback):
        """
        Dynamic initializer for GLFWCursorPosCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCursorPosCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCursorPosCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.createSafe(long)"""
        return GLFWCursorPosCallback._wrap(_GLFWCursorPosCallback.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.create(long)"""
        return GLFWCursorPosCallback._wrap(_GLFWCursorPosCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWCursorPosCallbackI') -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.create(org.lwjgl.glfw.GLFWCursorPosCallbackI)"""
        return GLFWCursorPosCallback._wrap(_GLFWCursorPosCallback.create(arg0))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWCursorPosCallbackI.invoke(long,double,double)"""
        pass

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWCursorPosCallback':
        """public org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.set(long)"""
        return 'GLFWCursorPosCallback'._wrap(super(_GLFWCursorPosCallback, self).set(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCursorPosCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorPosCallbackI.callback(long,long)"""
        super(_GLFWCursorPosCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWKeyCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWKeyCallbackI as _GLFWKeyCallbackI
_GLFWKeyCallbackI = _GLFWKeyCallbackI
import org.lwjgl.glfw.GLFWKeyCallback as _GLFWKeyCallback
_GLFWKeyCallback = _GLFWKeyCallback
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWKeyCallback():
    """org.lwjgl.glfw.GLFWKeyCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWKeyCallback) -> 'GLFWKeyCallback':
        return GLFWKeyCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWKeyCallback):
        """
        Dynamic initializer for GLFWKeyCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWKeyCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWKeyCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWKeyCallback':
        """public org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.set(long)"""
        return 'GLFWKeyCallback'._wrap(super(_GLFWKeyCallback, self).set(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWKeyCallbackI') -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.create(org.lwjgl.glfw.GLFWKeyCallbackI)"""
        return GLFWKeyCallback._wrap(_GLFWKeyCallback.create(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWKeyCallbackI.callback(long,long)"""
        super(_GLFWKeyCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.createSafe(long)"""
        return GLFWKeyCallback._wrap(_GLFWKeyCallback.createSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.create(long)"""
        return GLFWKeyCallback._wrap(_GLFWKeyCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWKeyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWKeyCallbackI, self).getCallInterface())

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void org.lwjgl.glfw.GLFWKeyCallbackI.invoke(long,int,int,int,int)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocateCallbackI
from pyquantum_helper import import_once as _import_once
import org.lwjgl.glfw.GLFWAllocateCallbackI as _GLFWAllocateCallbackI
_GLFWAllocateCallbackI = _GLFWAllocateCallbackI
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWAllocateCallbackI():
    """org.lwjgl.glfw.GLFWAllocateCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWAllocateCallbackI) -> 'GLFWAllocateCallbackI':
        return GLFWAllocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWAllocateCallbackI):
        """
        Dynamic initializer for GLFWAllocateCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWAllocateCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWAllocateCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.glfw.GLFWAllocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWAllocateCallbackI.callback(long,long)"""
        super(_GLFWAllocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWAllocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWAllocateCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWScrollCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWScrollCallbackI as _GLFWScrollCallbackI
_GLFWScrollCallbackI = _GLFWScrollCallbackI
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWScrollCallback as _GLFWScrollCallback
_GLFWScrollCallback = _GLFWScrollCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWScrollCallback():
    """org.lwjgl.glfw.GLFWScrollCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWScrollCallback) -> 'GLFWScrollCallback':
        return GLFWScrollCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWScrollCallback):
        """
        Dynamic initializer for GLFWScrollCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWScrollCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWScrollCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWScrollCallbackI.invoke(long,double,double)"""
        pass

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.createSafe(long)"""
        return GLFWScrollCallback._wrap(_GLFWScrollCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWScrollCallbackI.callback(long,long)"""
        super(_GLFWScrollCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWScrollCallback':
        """public org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.set(long)"""
        return 'GLFWScrollCallback'._wrap(super(_GLFWScrollCallback, self).set(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def create(arg0: 'GLFWScrollCallbackI') -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.create(org.lwjgl.glfw.GLFWScrollCallbackI)"""
        return GLFWScrollCallback._wrap(_GLFWScrollCallback.create(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.create(long)"""
        return GLFWScrollCallback._wrap(_GLFWScrollCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWScrollCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWScrollCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFW$Functions
import org.lwjgl.glfw.GLFW as _GLFW_Functions
_Functions = _GLFW_Functions.Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFW.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWImage$Buffer
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.system.CustomBuffer as _CustomBuffer
_CustomBuffer = _CustomBuffer
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWImage as _GLFWImage_Buffer
_Buffer = _GLFWImage_Buffer.Buffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import org.lwjgl.system.StructBuffer as _StructBuffer
_StructBuffer = _StructBuffer
import org.lwjgl.system.Struct as _Struct
_Struct = _Struct
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.lwjgl.system.Pointer as _Pointer_Default
_Default = _Pointer_Default.Default
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import java.lang.Integer as _int
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Buffer():
    """org.lwjgl.glfw.GLFWImage.Buffer"""
 
    @staticmethod
    def _wrap(java_value: _Buffer) -> 'Buffer':
        return Buffer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Buffer):
        """
        Dynamic initializer for Buffer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Buffer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Buffer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def limit(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.limit()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).limit())

    @overload
    def limit(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.limit(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).limit(_int.valueOf(arg0)))

    @override
    @overload
    def address0(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address0()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address0())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).address())

    @override
    @overload
    def rewind(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.rewind()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).rewind())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self, arg0: int) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get(int)"""
        return 'pyglsystem.Struct'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.CustomBuffer.toString()"""
        return str._wrap(super(pyglsystem.CustomBuffer, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int._wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def address(self, arg0: int) -> int:
        """public long org.lwjgl.system.CustomBuffer.address(int)"""
        return int._wrap(super(_pyglsystem.CustomBuffer, self).address(_int.valueOf(arg0)))

    @override
    @overload
    def mark(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.mark()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).mark())

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.pixels(java.nio.ByteBuffer)"""
        return 'Buffer'._wrap(super(_Buffer, self).pixels(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<T> org.lwjgl.system.StructBuffer.spliterator()"""
        return 'Spliterator'._wrap(super(pyglsystem.StructBuffer, self).spliterator())

    @override
    @overload
    def stream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.stream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).stream())

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).position(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWImage$Buffer(long,int)"""
        val = _Buffer(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWImage$Buffer(java.nio.ByteBuffer)"""
        val = _Buffer(arg0)
        self.__wrapper = val

    @overload
    def width(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.width(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).width(_int.valueOf(arg0)))

    @override
    @overload
    def reset(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.reset()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).reset())

    @override
    @overload
    def position(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.position()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).position())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def get(self) -> 'pyglsystem.Struct':
        """public T org.lwjgl.system.StructBuffer.get()"""
        return 'pyglsystem.Struct'._wrap(super(pyglsystem.StructBuffer, self).get())

    @override
    @overload
    def capacity(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.capacity()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).capacity())

    @overload
    def height(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.height(int)"""
        return 'Buffer'._wrap(super(_Buffer, self).height(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def compact(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.compact()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).compact())

    @overload
    def put(self, arg0: 'CustomBuffer') -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.put(SELF)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).put(arg0))

    @overload
    def apply(self, arg0: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Pointer$Default.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Pointer$Default, self).equals(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<T> org.lwjgl.system.StructBuffer.iterator()"""
        return 'Iterator'._wrap(super(pyglsystem.StructBuffer, self).iterator())

    @overload
    def put(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(arg0))

    @override
    @overload
    def slice(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).slice())

    @overload
    def slice(self, arg0: int, arg1: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.slice(int,int)"""
        return 'pyglsystem.CustomBuffer'._wrap(super(_pyglsystem.CustomBuffer, self).slice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage$Buffer.height()"""
        return int._wrap(super(Buffer, self).height())

    @overload
    def get(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(_int.valueOf(arg0), arg1))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).put(_int.valueOf(arg0), arg1))

    @override
    @overload
    def clear(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.clear()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).clear())

    @override
    @overload
    def hasRemaining(self) -> bool:
        """public boolean org.lwjgl.system.CustomBuffer.hasRemaining()"""
        return bool._wrap(super(pyglsystem.CustomBuffer, self).hasRemaining())

    @override
    @overload
    def flip(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.flip()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).flip())

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.system.StructBuffer.sizeof()"""
        return int._wrap(super(pyglsystem.StructBuffer, self).sizeof())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def apply(self, arg0: int, arg1: 'Consumer') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.apply(int,java.util.function.Consumer<T>)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).apply(_int.valueOf(arg0), arg1))

    @override
    @overload
    def remaining(self) -> int:
        """public int org.lwjgl.system.CustomBuffer.remaining()"""
        return int._wrap(super(pyglsystem.CustomBuffer, self).remaining())

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage$Buffer.pixels(int)"""
        return 'ByteBuffer'._wrap(super(_Buffer, self).pixels(_int.valueOf(arg0)))

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public java.util.stream.Stream<T> org.lwjgl.system.StructBuffer.parallelStream()"""
        return 'Stream'._wrap(super(pyglsystem.StructBuffer, self).parallelStream())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public void org.lwjgl.system.StructBuffer.forEach(java.util.function.Consumer<? super T>)"""
        super(_pyglsystem.StructBuffer, self).forEach(arg0)

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.CustomBuffer.free()"""
        super(pyglsystem.CustomBuffer, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage$Buffer.width()"""
        return int._wrap(super(Buffer, self).width())

    @override
    @overload
    def duplicate(self) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.duplicate()"""
        return 'pyglsystem.CustomBuffer'._wrap(super(pyglsystem.CustomBuffer, self).duplicate())

    @overload
    def get(self, arg0: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.get(T)"""
        return 'pyglsystem.StructBuffer'._wrap(super(_pyglsystem.StructBuffer, self).get(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeNSGL
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeNSGL as _GLFWNativeNSGL
_GLFWNativeNSGL = _GLFWNativeNSGL
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeNSGL():
    """org.lwjgl.glfw.GLFWNativeNSGL"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeNSGL) -> 'GLFWNativeNSGL':
        return GLFWNativeNSGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeNSGL):
        """
        Dynamic initializer for GLFWNativeNSGL.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeNSGL__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeNSGL__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def glfwGetNSGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeNSGL.glfwGetNSGLContext(long)"""
        return int._wrap(_GLFWNativeNSGL.glfwGetNSGLContext(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharModsCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWCharModsCallback as _GLFWCharModsCallback
_GLFWCharModsCallback = _GLFWCharModsCallback
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWCharModsCallbackI as _GLFWCharModsCallbackI
_GLFWCharModsCallbackI = _GLFWCharModsCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWCharModsCallback():
    """org.lwjgl.glfw.GLFWCharModsCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCharModsCallback) -> 'GLFWCharModsCallback':
        return GLFWCharModsCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCharModsCallback):
        """
        Dynamic initializer for GLFWCharModsCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCharModsCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCharModsCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.createSafe(long)"""
        return GLFWCharModsCallback._wrap(_GLFWCharModsCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharModsCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCharModsCallbackI, self).getCallInterface())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.create(long)"""
        return GLFWCharModsCallback._wrap(_GLFWCharModsCallback.create(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharModsCallbackI.callback(long,long)"""
        super(_GLFWCharModsCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWCharModsCallbackI') -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.create(org.lwjgl.glfw.GLFWCharModsCallbackI)"""
        return GLFWCharModsCallback._wrap(_GLFWCharModsCallback.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int) -> 'GLFWCharModsCallback':
        """public org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.set(long)"""
        return 'GLFWCharModsCallback'._wrap(super(_GLFWCharModsCallback, self).set(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWCharModsCallbackI.invoke(long,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeGLX$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWNativeGLX as _GLFWNativeGLX_Functions
_Functions = _GLFWNativeGLX_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeGLX.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVulkan$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWVulkan as _GLFWVulkan_Functions
_Functions = _GLFWVulkan_Functions.Functions
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWVulkan.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVulkan
 
 
 
# CLASS: org.lwjgl.glfw.GLFWMonitorCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
import org.lwjgl.glfw.GLFWMonitorCallback as _GLFWMonitorCallback
_GLFWMonitorCallback = _GLFWMonitorCallback
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWMonitorCallbackI as _GLFWMonitorCallbackI
_GLFWMonitorCallbackI = _GLFWMonitorCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWMonitorCallback():
    """org.lwjgl.glfw.GLFWMonitorCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWMonitorCallback) -> 'GLFWMonitorCallback':
        return GLFWMonitorCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWMonitorCallback):
        """
        Dynamic initializer for GLFWMonitorCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWMonitorCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWMonitorCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self) -> 'GLFWMonitorCallback':
        """public org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.set()"""
        return 'GLFWMonitorCallback'._wrap(super(GLFWMonitorCallback, self).set())

    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWMonitorCallbackI') -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.create(org.lwjgl.glfw.GLFWMonitorCallbackI)"""
        return GLFWMonitorCallback._wrap(_GLFWMonitorCallback.create(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.create(long)"""
        return GLFWMonitorCallback._wrap(_GLFWMonitorCallback.create(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWMonitorCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMonitorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWMonitorCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.createSafe(long)"""
        return GLFWMonitorCallback._wrap(_GLFWMonitorCallback.createSafe(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMonitorCallbackI.callback(long,long)"""
        super(_GLFWMonitorCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeEGL$Functions
from builtins import str
import org.lwjgl.glfw.GLFWNativeEGL as _GLFWNativeEGL_Functions
_Functions = _GLFWNativeEGL_Functions.Functions
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeEGL.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWMonitorCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWMonitorCallbackI as _GLFWMonitorCallbackI
_GLFWMonitorCallbackI = _GLFWMonitorCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWMonitorCallbackI():
    """org.lwjgl.glfw.GLFWMonitorCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWMonitorCallbackI) -> 'GLFWMonitorCallbackI':
        return GLFWMonitorCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWMonitorCallbackI):
        """
        Dynamic initializer for GLFWMonitorCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWMonitorCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWMonitorCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWMonitorCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMonitorCallbackI.callback(long,long)"""
        super(_GLFWMonitorCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMonitorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWMonitorCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFW
from pyquantum_helper import import_once as _import_once
import java.nio.IntBuffer as IntBuffer
import org.lwjgl.PointerBuffer as _PointerBuffer
_PointerBuffer = _PointerBuffer
import org.lwjgl.glfw.GLFWCursorPosCallback as _GLFWCursorPosCallback
_GLFWCursorPosCallback = _GLFWCursorPosCallback
import java.lang.Boolean as _boolean
import org.lwjgl.glfw.GLFW as _GLFW
_GLFW = _GLFW
from builtins import bool
import org.lwjgl.glfw.GLFWWindowContentScaleCallback as _GLFWWindowContentScaleCallback
_GLFWWindowContentScaleCallback = _GLFWWindowContentScaleCallback
import java.lang.CharSequence as CharSequence
import java.nio.DoubleBuffer as DoubleBuffer
import org.lwjgl.glfw.GLFWDropCallback as _GLFWDropCallback
_GLFWDropCallback = _GLFWDropCallback
import org.lwjgl.glfw.GLFWCharModsCallback as _GLFWCharModsCallback
_GLFWCharModsCallback = _GLFWCharModsCallback
import java.lang.Object as _object
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import org.lwjgl.glfw.GLFWVidMode as _GLFWVidMode_Buffer
_Buffer = _GLFWVidMode_Buffer.Buffer
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import org.lwjgl.glfw.GLFWWindowMaximizeCallback as _GLFWWindowMaximizeCallback
_GLFWWindowMaximizeCallback = _GLFWWindowMaximizeCallback
import java.lang.Float as _float
import org.lwjgl.glfw.GLFWWindowCloseCallback as _GLFWWindowCloseCallback
_GLFWWindowCloseCallback = _GLFWWindowCloseCallback
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.lwjgl.glfw.GLFWCursorEnterCallback as _GLFWCursorEnterCallback
_GLFWCursorEnterCallback = _GLFWCursorEnterCallback
import org.lwjgl.glfw.GLFWWindowFocusCallback as _GLFWWindowFocusCallback
_GLFWWindowFocusCallback = _GLFWWindowFocusCallback
import org.lwjgl.glfw.GLFWErrorCallback as _GLFWErrorCallback
_GLFWErrorCallback = _GLFWErrorCallback
import org.lwjgl.glfw.GLFWFramebufferSizeCallback as _GLFWFramebufferSizeCallback
_GLFWFramebufferSizeCallback = _GLFWFramebufferSizeCallback
import java.nio.FloatBuffer as _FloatBuffer
_FloatBuffer = _FloatBuffer
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.glfw.GLFWJoystickCallback as _GLFWJoystickCallback
_GLFWJoystickCallback = _GLFWJoystickCallback
import org.lwjgl.glfw.GLFWGammaRamp as _GLFWGammaRamp
_GLFWGammaRamp = _GLFWGammaRamp
import org.lwjgl.glfw.GLFWWindowSizeCallback as _GLFWWindowSizeCallback
_GLFWWindowSizeCallback = _GLFWWindowSizeCallback
import org.lwjgl.glfw.GLFWWindowRefreshCallback as _GLFWWindowRefreshCallback
_GLFWWindowRefreshCallback = _GLFWWindowRefreshCallback
import org.lwjgl.system.SharedLibrary as _SharedLibrary
_SharedLibrary = _SharedLibrary
import org.lwjgl.glfw.GLFWKeyCallback as _GLFWKeyCallback
_GLFWKeyCallback = _GLFWKeyCallback
import org.lwjgl.glfw.GLFWMouseButtonCallback as _GLFWMouseButtonCallback
_GLFWMouseButtonCallback = _GLFWMouseButtonCallback
from builtins import str
import org.lwjgl.glfw.GLFWMonitorCallback as _GLFWMonitorCallback
_GLFWMonitorCallback = _GLFWMonitorCallback
from pyquantum_helper import override
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import org.lwjgl.glfw.GLFWWindowPosCallback as _GLFWWindowPosCallback
_GLFWWindowPosCallback = _GLFWWindowPosCallback
import org.lwjgl.glfw.GLFWScrollCallback as _GLFWScrollCallback
_GLFWScrollCallback = _GLFWScrollCallback
import org.lwjgl.glfw.GLFWVidMode as _GLFWVidMode
_GLFWVidMode = _GLFWVidMode
import java.lang.Integer as _int
import java.nio.ByteBuffer as ByteBuffer
import org.lwjgl.glfw.GLFWCharCallback as _GLFWCharCallback
_GLFWCharCallback = _GLFWCharCallback
import org.lwjgl.glfw.GLFWWindowIconifyCallback as _GLFWWindowIconifyCallback
_GLFWWindowIconifyCallback = _GLFWWindowIconifyCallback
import java.lang.Long as _long
 
class GLFW():
    """org.lwjgl.glfw.GLFW"""
 
    @staticmethod
    def _wrap(java_value: _GLFW) -> 'GLFW':
        return GLFW(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFW):
        """
        Dynamic initializer for GLFW.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFW__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFW__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nglfwSetWindowContentScaleCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowContentScaleCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowContentScaleCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetJoystickButtons(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickButtons(int,long)"""
        return int._wrap(_GLFW.nglfwGetJoystickButtons(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetFramebufferSizeCallback(arg0: int, arg1: 'GLFWFramebufferSizeCallbackI') -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFW.glfwSetFramebufferSizeCallback(long,org.lwjgl.glfw.GLFWFramebufferSizeCallbackI)"""
        return GLFWFramebufferSizeCallback._wrap(_GLFW.glfwSetFramebufferSizeCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwGetGamepadState(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwGetGamepadState(int,long)"""
        return int._wrap(_GLFW.nglfwGetGamepadState(_int.valueOf(arg0), _long.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nglfwSetKeyCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetKeyCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetKeyCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

        @staticmethod
        @overload
        def glfwTerminate():
            """public static void org.lwjgl.glfw.GLFW.glfwTerminate()"""
            _GLFW.glfwTerminate()

    @staticmethod
    @overload
    def glfwWindowHintString(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHintString(int,java.nio.ByteBuffer)"""
        _GLFW.glfwWindowHintString(_int.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSetJoystickUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetJoystickUserPointer(int,long)"""
        _GLFW.glfwSetJoystickUserPointer(_int.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetWindowSizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowSizeCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowSizeCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetJoystickName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickName(int)"""
        return int._wrap(_GLFW.nglfwGetJoystickName(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetPlatform() -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetPlatform()"""
        return int._wrap(_GLFW.glfwGetPlatform())

    @staticmethod
    @overload
    def glfwInitAllocator(arg0: 'GLFWAllocator'):
        """public static void org.lwjgl.glfw.GLFW.glfwInitAllocator(org.lwjgl.glfw.GLFWAllocator)"""
        _GLFW.glfwInitAllocator(arg0)

    @staticmethod
    @overload
    def glfwSetWindowSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowSize(long,int,int)"""
        _GLFW.glfwSetWindowSize(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetWindowMaximizeCallback(arg0: int, arg1: 'GLFWWindowMaximizeCallbackI') -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFW.glfwSetWindowMaximizeCallback(long,org.lwjgl.glfw.GLFWWindowMaximizeCallbackI)"""
        return GLFWWindowMaximizeCallback._wrap(_GLFW.glfwSetWindowMaximizeCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetVersionString() -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetVersionString()"""
        return str._wrap(_GLFW.glfwGetVersionString())

    @staticmethod
    @overload
    def glfwWindowHint(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHint(int,int)"""
        _GLFW.glfwWindowHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetWindowFrameSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowFrameSize(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetWindowFrameSize(_long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwSetCursorPos(arg0: int, arg1: float, arg2: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetCursorPos(long,double,double)"""
        _GLFW.glfwSetCursorPos(_long.valueOf(arg0), _double.valueOf(arg1), _double.valueOf(arg2))

    @staticmethod
    @overload
    def glfwMaximizeWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwMaximizeWindow(long)"""
        _GLFW.glfwMaximizeWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWindowContentScale(arg0: int, arg1: 'float', arg2: 'float'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowContentScale(long,float[],float[])"""
        _GLFW.glfwGetWindowContentScale(_long.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def glfwSetMonitorUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetMonitorUserPointer(long,long)"""
        _GLFW.glfwSetMonitorUserPointer(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwGetVersionString() -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVersionString()"""
        return int._wrap(_GLFW.nglfwGetVersionString())

    @staticmethod
    @overload
    def glfwSetWindowOpacity(arg0: int, arg1: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowOpacity(long,float)"""
        _GLFW.glfwSetWindowOpacity(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetClipboardString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetClipboardString(long)"""
        return str._wrap(_GLFW.glfwGetClipboardString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwCreateCursor(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwCreateCursor(long,int,int)"""
        return int._wrap(_GLFW.nglfwCreateCursor(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def glfwGetJoystickUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetJoystickUserPointer(int)"""
        return int._wrap(_GLFW.glfwGetJoystickUserPointer(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowTitle(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowTitle(long,java.lang.CharSequence)"""
        _GLFW.glfwSetWindowTitle(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSetGammaRamp(arg0: int, arg1: 'GLFWGammaRamp'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetGammaRamp(long,org.lwjgl.glfw.GLFWGammaRamp)"""
        _GLFW.glfwSetGammaRamp(_long.valueOf(arg0), arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nglfwGetWindowSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowSize(long,long,long)"""
        _GLFW.nglfwGetWindowSize(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetWindowFrameSize(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowFrameSize(long,int[],int[],int[],int[])"""
        _GLFW.glfwGetWindowFrameSize(_long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwSetWindowCloseCallback(arg0: int, arg1: 'GLFWWindowCloseCallbackI') -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFW.glfwSetWindowCloseCallback(long,org.lwjgl.glfw.GLFWWindowCloseCallbackI)"""
        return GLFWWindowCloseCallback._wrap(_GLFW.glfwSetWindowCloseCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.glfw.GLFW.getLibrary()"""
        return pyglsystem.SharedLibrary._wrap(_GLFW.getLibrary())

    @staticmethod
    @overload
    def nglfwSetWindowIconifyCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowIconifyCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowIconifyCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwRequestWindowAttention(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwRequestWindowAttention(long)"""
        _GLFW.glfwRequestWindowAttention(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWindowPos(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowPos(long,int[],int[])"""
        _GLFW.glfwGetWindowPos(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetMonitorPhysicalSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPhysicalSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetMonitorPhysicalSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetProcAddress(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetProcAddress(java.nio.ByteBuffer)"""
        return int._wrap(_GLFW.glfwGetProcAddress(arg0))

    @staticmethod
    @overload
    def glfwInitHint(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwInitHint(int,int)"""
        _GLFW.glfwInitHint(_int.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwJoystickIsGamepad(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwJoystickIsGamepad(int)"""
        return bool._wrap(_GLFW.glfwJoystickIsGamepad(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetMonitorWorkarea(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorWorkarea(long,long,long,long,long)"""
        _GLFW.nglfwGetMonitorWorkarea(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def glfwSetCursor(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetCursor(long,long)"""
        _GLFW.glfwSetCursor(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetMouseButton(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetMouseButton(long,int)"""
        return int._wrap(_GLFW.glfwGetMouseButton(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetMonitorName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetMonitorName(long)"""
        return int._wrap(_GLFW.nglfwGetMonitorName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwRawMouseMotionSupported() -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwRawMouseMotionSupported()"""
        return bool._wrap(_GLFW.glfwRawMouseMotionSupported())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetDropCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetDropCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetDropCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowAttrib(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowAttrib(long,int,int)"""
        _GLFW.glfwSetWindowAttrib(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwGetError(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwGetError(long)"""
        return int._wrap(_GLFW.nglfwGetError(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetMonitorPhysicalSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorPhysicalSize(long,long,long)"""
        _GLFW.nglfwGetMonitorPhysicalSize(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwFocusWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwFocusWindow(long)"""
        _GLFW.glfwFocusWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwSetGamma(arg0: int, arg1: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetGamma(long,float)"""
        _GLFW.glfwSetGamma(_long.valueOf(arg0), _float.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetWindowRefreshCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowRefreshCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowRefreshCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetMonitorPos(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPos(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetMonitorPos(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nglfwSetGammaRamp(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetGammaRamp(long,long)"""
        _GLFW.nglfwSetGammaRamp(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwCreateStandardCursor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateStandardCursor(int)"""
        return int._wrap(_GLFW.glfwCreateStandardCursor(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetVersion(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetVersion(long,long,long)"""
        _GLFW.nglfwGetVersion(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

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

    @staticmethod
    @overload
    def glfwGetMonitorName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetMonitorName(long)"""
        return str._wrap(_GLFW.glfwGetMonitorName(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwHideWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwHideWindow(long)"""
        _GLFW.glfwHideWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetProcAddress(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetProcAddress(long)"""
        return int._wrap(_GLFW.nglfwGetProcAddress(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetGamepadState(arg0: int, arg1: 'GLFWGamepadState') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwGetGamepadState(int,org.lwjgl.glfw.GLFWGamepadState)"""
        return bool._wrap(_GLFW.glfwGetGamepadState(_int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwGetGammaRamp(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetGammaRamp(long)"""
        return int._wrap(_GLFW.nglfwGetGammaRamp(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetWindowMaximizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowMaximizeCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowMaximizeCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetCursorPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetCursorPos(long,long,long)"""
        _GLFW.nglfwGetCursorPos(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetErrorCallback(arg0: 'GLFWErrorCallbackI') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFW.glfwSetErrorCallback(org.lwjgl.glfw.GLFWErrorCallbackI)"""
        return GLFWErrorCallback._wrap(_GLFW.glfwSetErrorCallback(arg0))

    @staticmethod
    @overload
    def glfwCreateCursor(arg0: 'GLFWImage', arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateCursor(org.lwjgl.glfw.GLFWImage,int,int)"""
        return int._wrap(_GLFW.glfwCreateCursor(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def glfwSetWindowIconifyCallback(arg0: int, arg1: 'GLFWWindowIconifyCallbackI') -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFW.glfwSetWindowIconifyCallback(long,org.lwjgl.glfw.GLFWWindowIconifyCallbackI)"""
        return GLFWWindowIconifyCallback._wrap(_GLFW.glfwSetWindowIconifyCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwWindowHintString(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwWindowHintString(int,long)"""
        _GLFW.nglfwWindowHintString(_int.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetTime() -> float:
        """public static double org.lwjgl.glfw.GLFW.glfwGetTime()"""
        return float._wrap(_GLFW.glfwGetTime())

    @staticmethod
    @overload
    def glfwPlatformSupported(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwPlatformSupported(int)"""
        return bool._wrap(_GLFW.glfwPlatformSupported(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwWindowHintString(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHintString(int,java.lang.CharSequence)"""
        _GLFW.glfwWindowHintString(_int.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nglfwExtensionSupported(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwExtensionSupported(long)"""
        return int._wrap(_GLFW.nglfwExtensionSupported(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwJoystickPresent(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwJoystickPresent(int)"""
        return bool._wrap(_GLFW.glfwJoystickPresent(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWindowOpacity(arg0: int) -> float:
        """public static float org.lwjgl.glfw.GLFW.glfwGetWindowOpacity(long)"""
        return float._wrap(_GLFW.glfwGetWindowOpacity(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWindowMonitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetWindowMonitor(long)"""
        return int._wrap(_GLFW.glfwGetWindowMonitor(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetInputMode(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetInputMode(long,int,int)"""
        _GLFW.glfwSetInputMode(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSwapInterval(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSwapInterval(int)"""
        _GLFW.glfwSwapInterval(_int.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwSetJoystickCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetJoystickCallback(long)"""
        return int._wrap(_GLFW.nglfwSetJoystickCallback(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetCursorPosCallback(arg0: int, arg1: 'GLFWCursorPosCallbackI') -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFW.glfwSetCursorPosCallback(long,org.lwjgl.glfw.GLFWCursorPosCallbackI)"""
        return GLFWCursorPosCallback._wrap(_GLFW.glfwSetCursorPosCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetDropCallback(arg0: int, arg1: 'GLFWDropCallbackI') -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFW.glfwSetDropCallback(long,org.lwjgl.glfw.GLFWDropCallbackI)"""
        return GLFWDropCallback._wrap(_GLFW.glfwSetDropCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetMonitorCallback(arg0: 'GLFWMonitorCallbackI') -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFW.glfwSetMonitorCallback(org.lwjgl.glfw.GLFWMonitorCallbackI)"""
        return GLFWMonitorCallback._wrap(_GLFW.glfwSetMonitorCallback(arg0))

    @staticmethod
    @overload
    def nglfwSetWindowTitle(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetWindowTitle(long,long)"""
        _GLFW.nglfwSetWindowTitle(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetInputMode(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetInputMode(long,int)"""
        return int._wrap(_GLFW.glfwGetInputMode(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetMonitorPos(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPos(long,int[],int[])"""
        _GLFW.glfwGetMonitorPos(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetWindowContentScaleCallback(arg0: int, arg1: 'GLFWWindowContentScaleCallbackI') -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFW.glfwSetWindowContentScaleCallback(long,org.lwjgl.glfw.GLFWWindowContentScaleCallbackI)"""
        return GLFWWindowContentScaleCallback._wrap(_GLFW.glfwSetWindowContentScaleCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetWindowShouldClose(arg0: int, arg1: bool):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowShouldClose(long,boolean)"""
        _GLFW.glfwSetWindowShouldClose(_long.valueOf(arg0), _boolean.valueOf(arg1))

        @staticmethod
        @overload
        def glfwPollEvents():
            """public static void org.lwjgl.glfw.GLFW.glfwPollEvents()"""
            _GLFW.glfwPollEvents()

    @staticmethod
    @overload
    def nglfwSetCursorEnterCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCursorEnterCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetCursorEnterCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSwapBuffers(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSwapBuffers(long)"""
        _GLFW.glfwSwapBuffers(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetJoystickGUID(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetJoystickGUID(int)"""
        return str._wrap(_GLFW.glfwGetJoystickGUID(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwExtensionSupported(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwExtensionSupported(java.lang.CharSequence)"""
        return bool._wrap(_GLFW.glfwExtensionSupported(arg0))

    @staticmethod
    @overload
    def glfwGetMonitorWorkarea(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorWorkarea(long,int[],int[],int[],int[])"""
        _GLFW.glfwGetMonitorWorkarea(_long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwGetWindowAttrib(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetWindowAttrib(long,int)"""
        return int._wrap(_GLFW.glfwGetWindowAttrib(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowSizeCallback(arg0: int, arg1: 'GLFWWindowSizeCallbackI') -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFW.glfwSetWindowSizeCallback(long,org.lwjgl.glfw.GLFWWindowSizeCallbackI)"""
        return GLFWWindowSizeCallback._wrap(_GLFW.glfwSetWindowSizeCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwCreateWindow(arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateWindow(int,int,java.nio.ByteBuffer,long,long)"""
        return int._wrap(_GLFW.glfwCreateWindow(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4)))

        @staticmethod
        @overload
        def glfwPostEmptyEvent():
            """public static void org.lwjgl.glfw.GLFW.glfwPostEmptyEvent()"""
            _GLFW.glfwPostEmptyEvent()

    @staticmethod
    @overload
    def glfwSetScrollCallback(arg0: int, arg1: 'GLFWScrollCallbackI') -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFW.glfwSetScrollCallback(long,org.lwjgl.glfw.GLFWScrollCallbackI)"""
        return GLFWScrollCallback._wrap(_GLFW.glfwSetScrollCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetClipboardString(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetClipboardString(long,java.lang.CharSequence)"""
        _GLFW.glfwSetClipboardString(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwGetGamepadName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetGamepadName(int)"""
        return str._wrap(_GLFW.glfwGetGamepadName(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetMonitorUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetMonitorUserPointer(long)"""
        return int._wrap(_GLFW.glfwGetMonitorUserPointer(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowIcon(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowIcon(long,org.lwjgl.glfw.GLFWImage$Buffer)"""
        _GLFW.glfwSetWindowIcon(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwGetMonitorContentScale(arg0: int, arg1: 'FloatBuffer', arg2: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorContentScale(long,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        _GLFW.glfwGetMonitorContentScale(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetJoystickHats(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickHats(int)"""
        return ByteBuffer._wrap(_GLFW.glfwGetJoystickHats(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowMonitor(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowMonitor(long,long,int,int,int,int,int)"""
        _GLFW.glfwSetWindowMonitor(_long.valueOf(arg0), _long.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @staticmethod
    @overload
    def glfwGetMonitorWorkarea(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorWorkarea(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetMonitorWorkarea(_long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwGetMonitorPhysicalSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPhysicalSize(long,int[],int[])"""
        _GLFW.glfwGetMonitorPhysicalSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetCursorEnterCallback(arg0: int, arg1: 'GLFWCursorEnterCallbackI') -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFW.glfwSetCursorEnterCallback(long,org.lwjgl.glfw.GLFWCursorEnterCallbackI)"""
        return GLFWCursorEnterCallback._wrap(_GLFW.glfwSetCursorEnterCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetCharModsCallback(arg0: int, arg1: 'GLFWCharModsCallbackI') -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFW.glfwSetCharModsCallback(long,org.lwjgl.glfw.GLFWCharModsCallbackI)"""
        return GLFWCharModsCallback._wrap(_GLFW.glfwSetCharModsCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetWindowFocusCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowFocusCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowFocusCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwDestroyCursor(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwDestroyCursor(long)"""
        _GLFW.glfwDestroyCursor(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwSetMonitorCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetMonitorCallback(long)"""
        return int._wrap(_GLFW.nglfwSetMonitorCallback(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowPos(long,int,int)"""
        _GLFW.glfwSetWindowPos(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwSetFramebufferSizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetFramebufferSizeCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetFramebufferSizeCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetKeyCallback(arg0: int, arg1: 'GLFWKeyCallbackI') -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFW.glfwSetKeyCallback(long,org.lwjgl.glfw.GLFWKeyCallbackI)"""
        return GLFWKeyCallback._wrap(_GLFW.glfwSetKeyCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetMonitors() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.glfw.GLFW.glfwGetMonitors()"""
        return pygl.PointerBuffer._wrap(_GLFW.glfwGetMonitors())

    @staticmethod
    @overload
    def glfwGetWindowSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowSize(long,int[],int[])"""
        _GLFW.glfwGetWindowSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetWindowUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowUserPointer(long,long)"""
        _GLFW.glfwSetWindowUserPointer(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetTime(arg0: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetTime(double)"""
        _GLFW.glfwSetTime(_double.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetGamepadName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetGamepadName(int)"""
        return int._wrap(_GLFW.nglfwGetGamepadName(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowRefreshCallback(arg0: int, arg1: 'GLFWWindowRefreshCallbackI') -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFW.glfwSetWindowRefreshCallback(long,org.lwjgl.glfw.GLFWWindowRefreshCallbackI)"""
        return GLFWWindowRefreshCallback._wrap(_GLFW.glfwSetWindowRefreshCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwGetFramebufferSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetFramebufferSize(long,long,long)"""
        _GLFW.nglfwGetFramebufferSize(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetPrimaryMonitor() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetPrimaryMonitor()"""
        return int._wrap(_GLFW.glfwGetPrimaryMonitor())

    @staticmethod
    @overload
    def glfwSetMouseButtonCallback(arg0: int, arg1: 'GLFWMouseButtonCallbackI') -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFW.glfwSetMouseButtonCallback(long,org.lwjgl.glfw.GLFWMouseButtonCallbackI)"""
        return GLFWMouseButtonCallback._wrap(_GLFW.glfwSetMouseButtonCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetCharModsCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCharModsCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetCharModsCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwShowWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwShowWindow(long)"""
        _GLFW.glfwShowWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetCursorPos(arg0: int, arg1: 'double', arg2: 'double'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetCursorPos(long,double[],double[])"""
        _GLFW.glfwGetCursorPos(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nglfwInitAllocator(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwInitAllocator(long)"""
        _GLFW.nglfwInitAllocator(_long.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def nglfwSetErrorCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetErrorCallback(long)"""
        return int._wrap(_GLFW.nglfwSetErrorCallback(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetKey(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetKey(long,int)"""
        return int._wrap(_GLFW.glfwGetKey(_long.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwRestoreWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwRestoreWindow(long)"""
        _GLFW.glfwRestoreWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWindowUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetWindowUserPointer(long)"""
        return int._wrap(_GLFW.glfwGetWindowUserPointer(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetScrollCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetScrollCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetScrollCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwSetMouseButtonCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetMouseButtonCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetMouseButtonCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwSetWindowIcon(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetWindowIcon(long,int,long)"""
        _GLFW.nglfwSetWindowIcon(_long.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetJoystickAxes(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickAxes(int)"""
        return FloatBuffer._wrap(_GLFW.glfwGetJoystickAxes(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetClipboardString(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetClipboardString(long)"""
        return int._wrap(_GLFW.nglfwGetClipboardString(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowAspectRatio(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowAspectRatio(long,int,int)"""
        _GLFW.glfwSetWindowAspectRatio(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetKeyName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetKeyName(int,int)"""
        return str._wrap(_GLFW.glfwGetKeyName(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetTimerValue() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetTimerValue()"""
        return int._wrap(_GLFW.glfwGetTimerValue())

    @staticmethod
    @overload
    def glfwIconifyWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwIconifyWindow(long)"""
        _GLFW.glfwIconifyWindow(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetFramebufferSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetFramebufferSize(long,int[],int[])"""
        _GLFW.glfwGetFramebufferSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetKeyScancode(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetKeyScancode(int)"""
        return int._wrap(_GLFW.glfwGetKeyScancode(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetVideoModes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVideoModes(long,long)"""
        return int._wrap(_GLFW.nglfwGetVideoModes(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetCursorPos(arg0: int, arg1: 'DoubleBuffer', arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetCursorPos(long,java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        _GLFW.glfwGetCursorPos(_long.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nglfwCreateWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwCreateWindow(int,int,long,long,long)"""
        return int._wrap(_GLFW.nglfwCreateWindow(_int.valueOf(arg0), _int.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nglfwGetWindowFrameSize(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowFrameSize(long,long,long,long,long)"""
        _GLFW.nglfwGetWindowFrameSize(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4))

    @staticmethod
    @overload
    def glfwExtensionSupported(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwExtensionSupported(java.nio.ByteBuffer)"""
        return bool._wrap(_GLFW.glfwExtensionSupported(arg0))

    @staticmethod
    @overload
    def glfwGetVideoModes(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFW.glfwGetVideoModes(long)"""
        return Buffer._wrap(_GLFW.glfwGetVideoModes(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetError(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetError(org.lwjgl.PointerBuffer)"""
        return int._wrap(_GLFW.glfwGetError(arg0))

    @staticmethod
    @overload
    def glfwGetCurrentContext() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetCurrentContext()"""
        return int._wrap(_GLFW.glfwGetCurrentContext())

    @staticmethod
    @overload
    def nglfwGetMonitors(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetMonitors(long)"""
        return int._wrap(_GLFW.nglfwGetMonitors(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetClipboardString(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetClipboardString(long,long)"""
        _GLFW.nglfwSetClipboardString(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwInit() -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwInit()"""
        return bool._wrap(_GLFW.glfwInit())

    @staticmethod
    @overload
    def glfwSetWindowPosCallback(arg0: int, arg1: 'GLFWWindowPosCallbackI') -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFW.glfwSetWindowPosCallback(long,org.lwjgl.glfw.GLFWWindowPosCallbackI)"""
        return GLFWWindowPosCallback._wrap(_GLFW.glfwSetWindowPosCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetGammaRamp(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFW.glfwGetGammaRamp(long)"""
        return GLFWGammaRamp._wrap(_GLFW.glfwGetGammaRamp(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwMakeContextCurrent(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwMakeContextCurrent(long)"""
        _GLFW.glfwMakeContextCurrent(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetVersion(arg0: 'int', arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetVersion(int[],int[],int[])"""
        _GLFW.glfwGetVersion(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nglfwSetWindowCloseCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowCloseCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowCloseCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetJoystickGUID(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickGUID(int)"""
        return int._wrap(_GLFW.nglfwGetJoystickGUID(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetVideoMode(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVideoMode(long)"""
        return int._wrap(_GLFW.nglfwGetVideoMode(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwUpdateGamepadMappings(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwUpdateGamepadMappings(long)"""
        return int._wrap(_GLFW.nglfwUpdateGamepadMappings(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def glfwWindowShouldClose(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwWindowShouldClose(long)"""
        return bool._wrap(_GLFW.glfwWindowShouldClose(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetCharCallback(arg0: int, arg1: 'GLFWCharCallbackI') -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFW.glfwSetCharCallback(long,org.lwjgl.glfw.GLFWCharCallbackI)"""
        return GLFWCharCallback._wrap(_GLFW.glfwSetCharCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetWindowPosCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowPosCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetWindowPosCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwWaitEventsTimeout(arg0: float):
        """public static void org.lwjgl.glfw.GLFW.glfwWaitEventsTimeout(double)"""
        _GLFW.glfwWaitEventsTimeout(_double.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetJoystickHats(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickHats(int,long)"""
        return int._wrap(_GLFW.nglfwGetJoystickHats(_int.valueOf(arg0), _long.valueOf(arg1)))

        @staticmethod
        @overload
        def glfwDefaultWindowHints():
            """public static void org.lwjgl.glfw.GLFW.glfwDefaultWindowHints()"""
            _GLFW.glfwDefaultWindowHints()

    @staticmethod
    @overload
    def glfwCreateWindow(arg0: int, arg1: int, arg2: 'CharSequence', arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateWindow(int,int,java.lang.CharSequence,long,long)"""
        return int._wrap(_GLFW.glfwCreateWindow(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def nglfwGetWindowContentScale(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowContentScale(long,long,long)"""
        _GLFW.nglfwGetWindowContentScale(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetWindowTitle(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowTitle(long,java.nio.ByteBuffer)"""
        _GLFW.glfwSetWindowTitle(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwGetMonitorContentScale(arg0: int, arg1: 'float', arg2: 'float'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorContentScale(long,float[],float[])"""
        _GLFW.glfwGetMonitorContentScale(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetClipboardString(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetClipboardString(long,java.nio.ByteBuffer)"""
        _GLFW.glfwSetClipboardString(_long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwUpdateGamepadMappings(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwUpdateGamepadMappings(java.nio.ByteBuffer)"""
        return bool._wrap(_GLFW.glfwUpdateGamepadMappings(arg0))

    @staticmethod
    @overload
    def glfwGetJoystickName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetJoystickName(int)"""
        return str._wrap(_GLFW.glfwGetJoystickName(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowFocusCallback(arg0: int, arg1: 'GLFWWindowFocusCallbackI') -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFW.glfwSetWindowFocusCallback(long,org.lwjgl.glfw.GLFWWindowFocusCallbackI)"""
        return GLFWWindowFocusCallback._wrap(_GLFW.glfwSetWindowFocusCallback(_long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetVideoMode(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFW.glfwGetVideoMode(long)"""
        return GLFWVidMode._wrap(_GLFW.glfwGetVideoMode(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetWindowPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowPos(long,long,long)"""
        _GLFW.nglfwGetWindowPos(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwGetMonitorContentScale(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorContentScale(long,long,long)"""
        _GLFW.nglfwGetMonitorContentScale(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetWindowSizeLimits(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowSizeLimits(long,int,int,int,int)"""
        _GLFW.glfwSetWindowSizeLimits(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @staticmethod
    @overload
    def glfwGetVersion(arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetVersion(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetVersion(arg0, arg1, arg2)

    @staticmethod
    @overload
    def glfwGetWindowContentScale(arg0: int, arg1: 'FloatBuffer', arg2: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowContentScale(long,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        _GLFW.glfwGetWindowContentScale(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetTimerFrequency() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetTimerFrequency()"""
        return int._wrap(_GLFW.glfwGetTimerFrequency())

    @staticmethod
    @overload
    def nglfwGetMonitorPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorPos(long,long,long)"""
        _GLFW.nglfwGetMonitorPos(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetWindowSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetWindowSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nglfwSetCharCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCharCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetCharCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetProcAddress(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetProcAddress(java.lang.CharSequence)"""
        return int._wrap(_GLFW.glfwGetProcAddress(arg0))

    @staticmethod
    @overload
    def nglfwGetJoystickAxes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickAxes(int,long)"""
        return int._wrap(_GLFW.nglfwGetJoystickAxes(_int.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetKeyName(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetKeyName(int,int)"""
        return int._wrap(_GLFW.nglfwGetKeyName(_int.valueOf(arg0), _int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetFramebufferSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetFramebufferSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetFramebufferSize(_long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetWindowPos(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowPos(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        _GLFW.glfwGetWindowPos(_long.valueOf(arg0), arg1, arg2)

        @staticmethod
        @overload
        def glfwWaitEvents():
            """public static void org.lwjgl.glfw.GLFW.glfwWaitEvents()"""
            _GLFW.glfwWaitEvents()

    @staticmethod
    @overload
    def glfwGetJoystickButtons(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickButtons(int)"""
        return ByteBuffer._wrap(_GLFW.glfwGetJoystickButtons(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetJoystickCallback(arg0: 'GLFWJoystickCallbackI') -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFW.glfwSetJoystickCallback(org.lwjgl.glfw.GLFWJoystickCallbackI)"""
        return GLFWJoystickCallback._wrap(_GLFW.glfwSetJoystickCallback(arg0))

    @staticmethod
    @overload
    def nglfwSetCursorPosCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCursorPosCallback(long,long)"""
        return int._wrap(_GLFW.nglfwSetCursorPosCallback(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwDestroyWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwDestroyWindow(long)"""
        _GLFW.glfwDestroyWindow(_long.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.Callbacks
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import org.lwjgl.glfw.Callbacks as _Callbacks
_Callbacks = _Callbacks
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Callbacks():
    """org.lwjgl.glfw.Callbacks"""
 
    @staticmethod
    def _wrap(java_value: _Callbacks) -> 'Callbacks':
        return Callbacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Callbacks):
        """
        Dynamic initializer for Callbacks.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Callbacks__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Callbacks__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwFreeCallbacks(arg0: int):
        """public static void org.lwjgl.glfw.Callbacks.glfwFreeCallbacks(long)"""
        _Callbacks.glfwFreeCallbacks(_long.valueOf(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeOSMesa
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    import pygl
except ImportError:
    pygl = _import_once("pygl")

import java.nio.IntBuffer as IntBuffer
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWNativeOSMesa as _GLFWNativeOSMesa
_GLFWNativeOSMesa = _GLFWNativeOSMesa
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeOSMesa():
    """org.lwjgl.glfw.GLFWNativeOSMesa"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeOSMesa) -> 'GLFWNativeOSMesa':
        return GLFWNativeOSMesa(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeOSMesa):
        """
        Dynamic initializer for GLFWNativeOSMesa.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeOSMesa__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeOSMesa__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeOSMesa.setPath(org.lwjgl.system.FunctionProvider)"""
        _GLFWNativeOSMesa.setPath(arg0)

    @staticmethod
    @overload
    def nglfwGetOSMesaDepthBuffer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.nglfwGetOSMesaDepthBuffer(long,long,long,long,long)"""
        return int._wrap(_GLFWNativeOSMesa.nglfwGetOSMesaDepthBuffer(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

    @staticmethod
    @overload
    def glfwGetOSMesaContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaContext(long)"""
        return int._wrap(_GLFWNativeOSMesa.glfwGetOSMesaContext(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def glfwGetOSMesaDepthBuffer(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int._wrap(_GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def glfwGetOSMesaDepthBuffer(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(long,int[],int[],int[],org.lwjgl.PointerBuffer)"""
        return int._wrap(_GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeOSMesa.setPath(java.lang.String)"""
        _GLFWNativeOSMesa.setPath(arg0)

    @staticmethod
    @overload
    def glfwGetOSMesaColorBuffer(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return bool._wrap(_GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetOSMesaColorBuffer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.nglfwGetOSMesaColorBuffer(long,long,long,long,long)"""
        return int._wrap(_GLFWNativeOSMesa.nglfwGetOSMesaColorBuffer(_long.valueOf(arg0), _long.valueOf(arg1), _long.valueOf(arg2), _long.valueOf(arg3), _long.valueOf(arg4)))

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

    @staticmethod
    @overload
    def glfwGetOSMesaColorBuffer(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(long,int[],int[],int[],org.lwjgl.PointerBuffer)"""
        return bool._wrap(_GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(_long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeGLX
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import org.lwjgl.glfw.GLFWNativeGLX as _GLFWNativeGLX
_GLFWNativeGLX = _GLFWNativeGLX
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeGLX():
    """org.lwjgl.glfw.GLFWNativeGLX"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeGLX) -> 'GLFWNativeGLX':
        return GLFWNativeGLX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeGLX):
        """
        Dynamic initializer for GLFWNativeGLX.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeGLX__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeGLX__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetGLXContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXContext(long)"""
        return int._wrap(_GLFWNativeGLX.glfwGetGLXContext(_long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def glfwGetGLXWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXWindow(long)"""
        return int._wrap(_GLFWNativeGLX.glfwGetGLXWindow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeGLX.setPath(java.lang.String)"""
        _GLFWNativeGLX.setPath(arg0)

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
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeGLX.setPath(org.lwjgl.system.FunctionProvider)"""
        _GLFWNativeGLX.setPath(arg0)

    @staticmethod
    @overload
    def glfwGetGLXFBConfig(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXFBConfig(long)"""
        return int._wrap(_GLFWNativeGLX.glfwGetGLXFBConfig(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorEnterCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.glfw.GLFWCursorEnterCallback as _GLFWCursorEnterCallback
_GLFWCursorEnterCallback = _GLFWCursorEnterCallback
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWCursorEnterCallbackI as _GLFWCursorEnterCallbackI
_GLFWCursorEnterCallbackI = _GLFWCursorEnterCallbackI
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWCursorEnterCallback():
    """org.lwjgl.glfw.GLFWCursorEnterCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCursorEnterCallback) -> 'GLFWCursorEnterCallback':
        return GLFWCursorEnterCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCursorEnterCallback):
        """
        Dynamic initializer for GLFWCursorEnterCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCursorEnterCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCursorEnterCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorEnterCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCursorEnterCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorEnterCallbackI.callback(long,long)"""
        super(_GLFWCursorEnterCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.create(long)"""
        return GLFWCursorEnterCallback._wrap(_GLFWCursorEnterCallback.create(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.createSafe(long)"""
        return GLFWCursorEnterCallback._wrap(_GLFWCursorEnterCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int) -> 'GLFWCursorEnterCallback':
        """public org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.set(long)"""
        return 'GLFWCursorEnterCallback'._wrap(super(_GLFWCursorEnterCallback, self).set(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: 'GLFWCursorEnterCallbackI') -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.create(org.lwjgl.glfw.GLFWCursorEnterCallbackI)"""
        return GLFWCursorEnterCallback._wrap(_GLFWCursorEnterCallback.create(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWCursorEnterCallbackI.invoke(long,boolean)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowCloseCallback
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.lwjgl.system.NativeResource as _NativeResource
_NativeResource = _NativeResource
import org.lwjgl.glfw.GLFWWindowCloseCallbackI as _GLFWWindowCloseCallbackI
_GLFWWindowCloseCallbackI = _GLFWWindowCloseCallbackI
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

import org.lwjgl.system.Callback as _Callback
_Callback = _Callback
import java.lang.Integer as _int
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWWindowCloseCallback as _GLFWWindowCloseCallback
_GLFWWindowCloseCallback = _GLFWWindowCloseCallback
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWWindowCloseCallback():
    """org.lwjgl.glfw.GLFWWindowCloseCallback"""
 
    @staticmethod
    def _wrap(java_value: _GLFWWindowCloseCallback) -> 'GLFWWindowCloseCallback':
        return GLFWWindowCloseCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWWindowCloseCallback):
        """
        Dynamic initializer for GLFWWindowCloseCallback.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWWindowCloseCallback__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWWindowCloseCallback__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.getSafe(_long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowCloseCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowCloseCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWWindowCloseCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI._wrap(_Callback.get(_long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str._wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int._wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        _Callback.free(_long.valueOf(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowCloseCallback':
        """public org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.set(long)"""
        return 'GLFWWindowCloseCallback'._wrap(super(_GLFWWindowCloseCallback, self).set(_long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool._wrap(super(_pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowCloseCallbackI') -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.create(org.lwjgl.glfw.GLFWWindowCloseCallbackI)"""
        return GLFWWindowCloseCallback._wrap(_GLFWWindowCloseCallback.create(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int._wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.createSafe(long)"""
        return GLFWWindowCloseCallback._wrap(_GLFWWindowCloseCallback.createSafe(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowCloseCallbackI.callback(long,long)"""
        super(_GLFWWindowCloseCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.create(long)"""
        return GLFWWindowCloseCallback._wrap(_GLFWWindowCloseCallback.create(_long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWErrorCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.glfw.GLFWErrorCallbackI as _GLFWErrorCallbackI
_GLFWErrorCallbackI = _GLFWErrorCallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWErrorCallbackI():
    """org.lwjgl.glfw.GLFWErrorCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWErrorCallbackI) -> 'GLFWErrorCallbackI':
        return GLFWErrorCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWErrorCallbackI):
        """
        Dynamic initializer for GLFWErrorCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWErrorCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWErrorCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWErrorCallbackI.invoke(int,long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWErrorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWErrorCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWErrorCallbackI.callback(long,long)"""
        super(_GLFWErrorCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWin32$Functions
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import org.lwjgl.glfw.GLFWNativeWin32 as _GLFWNativeWin32_Functions
_Functions = _GLFWNativeWin32_Functions.Functions
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWin32.Functions"""
 
    @staticmethod
    def _wrap(java_value: _Functions) -> 'Functions':
        return Functions(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Functions):
        """
        Dynamic initializer for Functions.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Functions__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Functions__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
import org.lwjgl.glfw.GLFWCharCallbackI as _GLFWCharCallbackI
_GLFWCharCallbackI = _GLFWCharCallbackI
from abc import abstractmethod, ABC
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWCharCallbackI():
    """org.lwjgl.glfw.GLFWCharCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWCharCallbackI) -> 'GLFWCharCallbackI':
        return GLFWCharCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWCharCallbackI):
        """
        Dynamic initializer for GLFWCharCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWCharCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWCharCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWCharCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWCharCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharCallbackI.callback(long,long)"""
        super(_GLFWCharCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWGL
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = _import_once("pyglsystem")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.lwjgl.glfw.GLFWNativeWGL as _GLFWNativeWGL
_GLFWNativeWGL = _GLFWNativeWGL
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GLFWNativeWGL():
    """org.lwjgl.glfw.GLFWNativeWGL"""
 
    @staticmethod
    def _wrap(java_value: _GLFWNativeWGL) -> 'GLFWNativeWGL':
        return GLFWNativeWGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWNativeWGL):
        """
        Dynamic initializer for GLFWNativeWGL.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWNativeWGL__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWNativeWGL__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def glfwGetWGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWGL.glfwGetWGLContext(long)"""
        return int._wrap(_GLFWNativeWGL.glfwGetWGLContext(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeWGL.setPath(java.lang.String)"""
        _GLFWNativeWGL.setPath(arg0)

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

    @staticmethod
    @overload
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeWGL.setPath(org.lwjgl.system.FunctionProvider)"""
        _GLFWNativeWGL.setPath(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWReallocateCallbackI
from pyquantum_helper import import_once as _import_once
from pyquantum_helper import override
import org.lwjgl.system.CallbackI as _CallbackI
_CallbackI = _CallbackI
import org.lwjgl.system.libffi.FFICIF as _FFICIF
_FFICIF = _FFICIF
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWReallocateCallbackI as _GLFWReallocateCallbackI
_GLFWReallocateCallbackI = _GLFWReallocateCallbackI
import java.lang.Long as _long
try:
    from pyglsystem import libffi
except ImportError:
    libffi = _import_once("pyglsystem.libffi")

from builtins import int
 
class GLFWReallocateCallbackI():
    """org.lwjgl.glfw.GLFWReallocateCallbackI"""
 
    @staticmethod
    def _wrap(java_value: _GLFWReallocateCallbackI) -> 'GLFWReallocateCallbackI':
        return GLFWReallocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GLFWReallocateCallbackI):
        """
        Dynamic initializer for GLFWReallocateCallbackI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GLFWReallocateCallbackI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GLFWReallocateCallbackI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int._wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWReallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'._wrap(super(GLFWReallocateCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract long org.lwjgl.glfw.GLFWReallocateCallbackI.invoke(long,long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWReallocateCallbackI.callback(long,long)"""
        super(_GLFWReallocateCallbackI, self).callback(_long.valueOf(arg0), _long.valueOf(arg1))