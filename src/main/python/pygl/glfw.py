from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWNativeX11 as __GLFWNativeX11
__GLFWNativeX11 = __GLFWNativeX11
import java.lang.Object as __object
from builtins import type
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
 
class GLFWNativeX11():
    """org.lwjgl.glfw.GLFWNativeX11"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeX11) -> 'GLFWNativeX11':
        return GLFWNativeX11(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeX11):
        """
        Dynamic initializer for GLFWNativeX11.
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
    def nglfwGetX11SelectionString() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.nglfwGetX11SelectionString()"""
        return int.__wrap(__GLFWNativeX11.nglfwGetX11SelectionString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetX11SelectionString(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.nio.ByteBuffer)"""
        __GLFWNativeX11.glfwSetX11SelectionString(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nglfwSetX11SelectionString(arg0: int):
        """public static void org.lwjgl.glfw.GLFWNativeX11.nglfwSetX11SelectionString(long)"""
        __GLFWNativeX11.nglfwSetX11SelectionString(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetX11Display() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Display()"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Display())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def glfwGetX11Window(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Window(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Window(__long.valueOf(arg0)))

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
    def glfwSetX11SelectionString(arg0: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.lang.CharSequence)"""
        __GLFWNativeX11.glfwSetX11SelectionString(arg0)

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
    def glfwGetX11Adapter(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Adapter(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Adapter(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetX11Monitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Monitor(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Monitor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetX11SelectionString() -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeX11.glfwGetX11SelectionString()"""
        return str.__wrap(__GLFWNativeX11.glfwGetX11SelectionString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeX11
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWNativeX11 as __GLFWNativeX11
__GLFWNativeX11 = __GLFWNativeX11
import java.lang.Object as __object
from builtins import type
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
 
class GLFWNativeX11():
    """org.lwjgl.glfw.GLFWNativeX11"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeX11) -> 'GLFWNativeX11':
        return GLFWNativeX11(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeX11):
        """
        Dynamic initializer for GLFWNativeX11.
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
    def nglfwGetX11SelectionString() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.nglfwGetX11SelectionString()"""
        return int.__wrap(__GLFWNativeX11.nglfwGetX11SelectionString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetX11SelectionString(arg0: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.nio.ByteBuffer)"""
        __GLFWNativeX11.glfwSetX11SelectionString(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nglfwSetX11SelectionString(arg0: int):
        """public static void org.lwjgl.glfw.GLFWNativeX11.nglfwSetX11SelectionString(long)"""
        __GLFWNativeX11.nglfwSetX11SelectionString(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetX11Display() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Display()"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Display())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def glfwGetX11Window(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Window(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Window(__long.valueOf(arg0)))

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
    def glfwSetX11SelectionString(arg0: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFWNativeX11.glfwSetX11SelectionString(java.lang.CharSequence)"""
        __GLFWNativeX11.glfwSetX11SelectionString(arg0)

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
    def glfwGetX11Adapter(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Adapter(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Adapter(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetX11Monitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeX11.glfwGetX11Monitor(long)"""
        return int.__wrap(__GLFWNativeX11.glfwGetX11Monitor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetX11SelectionString() -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeX11.glfwGetX11SelectionString()"""
        return str.__wrap(__GLFWNativeX11.glfwGetX11SelectionString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeX11 
 
 
# CLASS: org.lwjgl.glfw.GLFWImage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.glfw.GLFWImage as __GLFWImage
__GLFWImage = __GLFWImage
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
import org.lwjgl.glfw.GLFWImage as __GLFWImage_Buffer
__Buffer = __GLFWImage_Buffer.Buffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWImage(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWImage"""
 
    @staticmethod
    def __wrap(java_value: __GLFWImage) -> 'GLFWImage':
        return GLFWImage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWImage):
        """
        Dynamic initializer for GLFWImage.
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
    def createSafe(arg0: int) -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.createSafe(long)"""
        return GLFWImage.__wrap(__GLFWImage.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWImage.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.malloc()"""
        return GLFWImage.__wrap(__GLFWImage.malloc())

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
    def callocStack() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.callocStack()"""
        return GLFWImage.__wrap(__GLFWImage.callocStack())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWImage.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nwidth(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWImage.nwidth(long,int)"""
        __GLFWImage.nwidth(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.create(int)"""
        return Buffer.__wrap(__GLFWImage.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWImage.__wrap(__GLFWImage.callocStack(arg0))

    @overload
    def height(self, arg0: int) -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.height(int)"""
        return 'GLFWImage'.__wrap(super(__GLFWImage, self).height(__int.valueOf(arg0)))

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
    def set(self, arg0: int, arg1: int, arg2: 'ByteBuffer') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.set(int,int,java.nio.ByteBuffer)"""
        return 'GLFWImage'.__wrap(super(__GLFWImage, self).set(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def create() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.create()"""
        return GLFWImage.__wrap(__GLFWImage.create())

    @staticmethod
    @overload
    def calloc() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.calloc()"""
        return GLFWImage.__wrap(__GLFWImage.calloc())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.create(long,int)"""
        return Buffer.__wrap(__GLFWImage.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWImage.__wrap(__GLFWImage.mallocStack(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nheight(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWImage.nheight(long,int)"""
        __GLFWImage.nheight(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__GLFWImage, self).pixels(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.mallocStack(int)"""
        return Buffer.__wrap(__GLFWImage.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWImage.callocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWImage.__wrap(__GLFWImage.malloc(arg0))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.callocStack(int)"""
        return Buffer.__wrap(__GLFWImage.callocStack(__int.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.sizeof()"""
        return int.__wrap(super(GLFWImage, self).sizeof())

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.mallocStack()"""
        return GLFWImage.__wrap(__GLFWImage.mallocStack())

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWImage.__wrap(__GLFWImage.calloc(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWImage(java.nio.ByteBuffer)"""
        val = __GLFWImage(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.pixels(java.nio.ByteBuffer)"""
        return 'GLFWImage'.__wrap(super(__GLFWImage, self).pixels(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.calloc(int)"""
        return Buffer.__wrap(__GLFWImage.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWImage.npixels(long,java.nio.ByteBuffer)"""
        __GLFWImage.npixels(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.createSafe(long,int)"""
        return Buffer.__wrap(__GLFWImage.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWImage.nwidth(long)"""
        return int.__wrap(__GLFWImage.nwidth(__long.valueOf(arg0)))

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
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWImage.validate(long)"""
        __GLFWImage.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWImage.nheight(long)"""
        return int.__wrap(__GLFWImage.nheight(__long.valueOf(arg0)))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.width()"""
        return int.__wrap(super(GLFWImage, self).width())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWImage.mallocStack(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWImage':
        """public static org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.create(long)"""
        return GLFWImage.__wrap(__GLFWImage.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def npixels(arg0: int, arg1: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage.npixels(long,int)"""
        return ByteBuffer.__wrap(__GLFWImage.npixels(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage.height()"""
        return int.__wrap(super(GLFWImage, self).height())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage.malloc(int)"""
        return Buffer.__wrap(__GLFWImage.malloc(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: 'GLFWImage') -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.set(org.lwjgl.glfw.GLFWImage)"""
        return 'GLFWImage'.__wrap(super(__GLFWImage, self).set(arg0))

    @overload
    def width(self, arg0: int) -> 'GLFWImage':
        """public org.lwjgl.glfw.GLFWImage org.lwjgl.glfw.GLFWImage.width(int)"""
        return 'GLFWImage'.__wrap(super(__GLFWImage, self).width(__int.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWMouseButtonCallback
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
import org.lwjgl.glfw.GLFWMouseButtonCallback as __GLFWMouseButtonCallback
__GLFWMouseButtonCallback = __GLFWMouseButtonCallback
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
import org.lwjgl.glfw.GLFWMouseButtonCallbackI as __GLFWMouseButtonCallbackI
__GLFWMouseButtonCallbackI = __GLFWMouseButtonCallbackI
from builtins import int
 
class GLFWMouseButtonCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWMouseButtonCallbackI, GLFWMouseButtonCallbackI):
    """org.lwjgl.glfw.GLFWMouseButtonCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWMouseButtonCallback) -> 'GLFWMouseButtonCallback':
        return GLFWMouseButtonCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWMouseButtonCallback):
        """
        Dynamic initializer for GLFWMouseButtonCallback.
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
    def create(arg0: int) -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.create(long)"""
        return GLFWMouseButtonCallback.__wrap(__GLFWMouseButtonCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void org.lwjgl.glfw.GLFWMouseButtonCallbackI.invoke(long,int,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMouseButtonCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWMouseButtonCallbackI, self).getCallInterface())

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
    def createSafe(arg0: int) -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.createSafe(long)"""
        return GLFWMouseButtonCallback.__wrap(__GLFWMouseButtonCallback.createSafe(__long.valueOf(arg0)))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(long,long)"""
        super(__GLFWMouseButtonCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def set(self, arg0: int) -> 'GLFWMouseButtonCallback':
        """public org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.set(long)"""
        return 'GLFWMouseButtonCallback'.__wrap(super(__GLFWMouseButtonCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'GLFWMouseButtonCallbackI') -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFWMouseButtonCallback.create(org.lwjgl.glfw.GLFWMouseButtonCallbackI)"""
        return GLFWMouseButtonCallback.__wrap(__GLFWMouseButtonCallback.create(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeCocoa
import org.lwjgl.glfw.GLFWNativeCocoa as __GLFWNativeCocoa
__GLFWNativeCocoa = __GLFWNativeCocoa
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
 
class GLFWNativeCocoa():
    """org.lwjgl.glfw.GLFWNativeCocoa"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeCocoa) -> 'GLFWNativeCocoa':
        return GLFWNativeCocoa(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeCocoa):
        """
        Dynamic initializer for GLFWNativeCocoa.
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
    def glfwGetCocoaMonitor(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeCocoa.glfwGetCocoaMonitor(long)"""
        return int.__wrap(__GLFWNativeCocoa.glfwGetCocoaMonitor(__long.valueOf(arg0)))

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
    def glfwGetCocoaWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeCocoa.glfwGetCocoaWindow(long)"""
        return int.__wrap(__GLFWNativeCocoa.glfwGetCocoaWindow(__long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWScrollCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWScrollCallback as __GLFWScrollCallback
__GLFWScrollCallback = __GLFWScrollCallback
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
import org.lwjgl.glfw.GLFWScrollCallbackI as __GLFWScrollCallbackI
__GLFWScrollCallbackI = __GLFWScrollCallbackI
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWScrollCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWScrollCallbackI, GLFWScrollCallbackI):
    """org.lwjgl.glfw.GLFWScrollCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWScrollCallback) -> 'GLFWScrollCallback':
        return GLFWScrollCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWScrollCallback):
        """
        Dynamic initializer for GLFWScrollCallback.
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

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWScrollCallbackI.invoke(long,double,double)"""
        pass

    @overload
    def set(self, arg0: int) -> 'GLFWScrollCallback':
        """public org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.set(long)"""
        return 'GLFWScrollCallback'.__wrap(super(__GLFWScrollCallback, self).set(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.createSafe(long)"""
        return GLFWScrollCallback.__wrap(__GLFWScrollCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.create(long)"""
        return GLFWScrollCallback.__wrap(__GLFWScrollCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWScrollCallbackI.callback(long,long)"""
        super(__GLFWScrollCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def create(arg0: 'GLFWScrollCallbackI') -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFWScrollCallback.create(org.lwjgl.glfw.GLFWScrollCallbackI)"""
        return GLFWScrollCallback.__wrap(__GLFWScrollCallback.create(arg0))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWScrollCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWScrollCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWImage$Buffer
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
import org.lwjgl.glfw.GLFWImage as __GLFWImage_Buffer
__Buffer = __GLFWImage_Buffer.Buffer
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWImage.Buffer"""
 
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
        """public org.lwjgl.glfw.GLFWImage$Buffer(long,int)"""
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
    def height(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.height(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).height(__int.valueOf(arg0)))

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWImage$Buffer(java.nio.ByteBuffer)"""
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

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage$Buffer.height()"""
        return int.__wrap(super(Buffer, self).height())

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.CustomBuffer.address()"""
        return int.__wrap(super(pyglsystem.CustomBuffer, self).address())

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWImage$Buffer.width()"""
        return int.__wrap(super(Buffer, self).width())

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
    def width(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.width(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).width(__int.valueOf(arg0)))

    @overload
    def pixels(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWImage$Buffer org.lwjgl.glfw.GLFWImage$Buffer.pixels(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).pixels(arg0))

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
    def pixels(self, arg0: int) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWImage$Buffer.pixels(int)"""
        return 'ByteBuffer'.__wrap(super(__Buffer, self).pixels(__int.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWin32$Functions
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
import org.lwjgl.glfw.GLFWNativeWin32 as __GLFWNativeWin32_Functions
__Functions = __GLFWNativeWin32_Functions.Functions
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWin32.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowPosCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWWindowPosCallback as __GLFWWindowPosCallback
__GLFWWindowPosCallback = __GLFWWindowPosCallback
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWWindowPosCallbackI as __GLFWWindowPosCallbackI
__GLFWWindowPosCallbackI = __GLFWWindowPosCallbackI
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
 
class GLFWWindowPosCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowPosCallbackI, GLFWWindowPosCallbackI):
    """org.lwjgl.glfw.GLFWWindowPosCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowPosCallback) -> 'GLFWWindowPosCallback':
        return GLFWWindowPosCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowPosCallback):
        """
        Dynamic initializer for GLFWWindowPosCallback.
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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowPosCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowPosCallbackI, self).getCallInterface())

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
    def createSafe(arg0: int) -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.createSafe(long)"""
        return GLFWWindowPosCallback.__wrap(__GLFWWindowPosCallback.createSafe(__long.valueOf(arg0)))

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

    @overload
    def set(self, arg0: int) -> 'GLFWWindowPosCallback':
        """public org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.set(long)"""
        return 'GLFWWindowPosCallback'.__wrap(super(__GLFWWindowPosCallback, self).set(__long.valueOf(arg0)))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowPosCallbackI.callback(long,long)"""
        super(__GLFWWindowPosCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.create(long)"""
        return GLFWWindowPosCallback.__wrap(__GLFWWindowPosCallback.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowPosCallbackI') -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFWWindowPosCallback.create(org.lwjgl.glfw.GLFWWindowPosCallbackI)"""
        return GLFWWindowPosCallback.__wrap(__GLFWWindowPosCallback.create(arg0))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowRefreshCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWWindowRefreshCallbackI as __GLFWWindowRefreshCallbackI
__GLFWWindowRefreshCallbackI = __GLFWWindowRefreshCallbackI
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowRefreshCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowRefreshCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowRefreshCallbackI) -> 'GLFWWindowRefreshCallbackI':
        return GLFWWindowRefreshCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowRefreshCallbackI):
        """
        Dynamic initializer for GLFWWindowRefreshCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.callback(long,long)"""
        super(__GLFWWindowRefreshCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowRefreshCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowRefreshCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowMaximizeCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.glfw.GLFWWindowMaximizeCallback as __GLFWWindowMaximizeCallback
__GLFWWindowMaximizeCallback = __GLFWWindowMaximizeCallback
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWWindowMaximizeCallbackI as __GLFWWindowMaximizeCallbackI
__GLFWWindowMaximizeCallbackI = __GLFWWindowMaximizeCallbackI
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWWindowMaximizeCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowMaximizeCallbackI, GLFWWindowMaximizeCallbackI):
    """org.lwjgl.glfw.GLFWWindowMaximizeCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowMaximizeCallback) -> 'GLFWWindowMaximizeCallback':
        return GLFWWindowMaximizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowMaximizeCallback):
        """
        Dynamic initializer for GLFWWindowMaximizeCallback.
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

    @overload
    def set(self, arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.set(long)"""
        return 'GLFWWindowMaximizeCallback'.__wrap(super(__GLFWWindowMaximizeCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowMaximizeCallbackI') -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.create(org.lwjgl.glfw.GLFWWindowMaximizeCallbackI)"""
        return GLFWWindowMaximizeCallback.__wrap(__GLFWWindowMaximizeCallback.create(arg0))

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

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.create(long)"""
        return GLFWWindowMaximizeCallback.__wrap(__GLFWWindowMaximizeCallback.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFWWindowMaximizeCallback.createSafe(long)"""
        return GLFWWindowMaximizeCallback.__wrap(__GLFWWindowMaximizeCallback.createSafe(__long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowMaximizeCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.callback(long,long)"""
        super(__GLFWWindowMaximizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWayland
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
import org.lwjgl.glfw.GLFWNativeWayland as __GLFWNativeWayland
__GLFWNativeWayland = __GLFWNativeWayland
from builtins import int
 
class GLFWNativeWayland():
    """org.lwjgl.glfw.GLFWNativeWayland"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeWayland) -> 'GLFWNativeWayland':
        return GLFWNativeWayland(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeWayland):
        """
        Dynamic initializer for GLFWNativeWayland.
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
    def glfwGetWaylandDisplay() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandDisplay()"""
        return int.__wrap(__GLFWNativeWayland.glfwGetWaylandDisplay())

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

    @staticmethod
    @overload
    def glfwGetWaylandMonitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandMonitor(long)"""
        return int.__wrap(__GLFWNativeWayland.glfwGetWaylandMonitor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWaylandWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWayland.glfwGetWaylandWindow(long)"""
        return int.__wrap(__GLFWNativeWayland.glfwGetWaylandWindow(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVulkan
 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowCloseCallback
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWWindowCloseCallback as __GLFWWindowCloseCallback
__GLFWWindowCloseCallback = __GLFWWindowCloseCallback
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
import org.lwjgl.glfw.GLFWWindowCloseCallbackI as __GLFWWindowCloseCallbackI
__GLFWWindowCloseCallbackI = __GLFWWindowCloseCallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWWindowCloseCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowCloseCallbackI, GLFWWindowCloseCallbackI):
    """org.lwjgl.glfw.GLFWWindowCloseCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowCloseCallback) -> 'GLFWWindowCloseCallback':
        return GLFWWindowCloseCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowCloseCallback):
        """
        Dynamic initializer for GLFWWindowCloseCallback.
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

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowCloseCallbackI.invoke(long)"""
        pass

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.create(long)"""
        return GLFWWindowCloseCallback.__wrap(__GLFWWindowCloseCallback.create(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWWindowCloseCallback':
        """public org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.set(long)"""
        return 'GLFWWindowCloseCallback'.__wrap(super(__GLFWWindowCloseCallback, self).set(__long.valueOf(arg0)))

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
    def create(arg0: 'GLFWWindowCloseCallbackI') -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.create(org.lwjgl.glfw.GLFWWindowCloseCallbackI)"""
        return GLFWWindowCloseCallback.__wrap(__GLFWWindowCloseCallback.create(arg0))

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
    def createSafe(arg0: int) -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFWWindowCloseCallback.createSafe(long)"""
        return GLFWWindowCloseCallback.__wrap(__GLFWWindowCloseCallback.createSafe(__long.valueOf(arg0)))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowCloseCallbackI.callback(long,long)"""
        super(__GLFWWindowCloseCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowCloseCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowCloseCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWReallocateCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWReallocateCallbackI as __GLFWReallocateCallbackI
__GLFWReallocateCallbackI = __GLFWReallocateCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWReallocateCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWReallocateCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWReallocateCallbackI) -> 'GLFWReallocateCallbackI':
        return GLFWReallocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWReallocateCallbackI):
        """
        Dynamic initializer for GLFWReallocateCallbackI.
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWReallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWReallocateCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract long org.lwjgl.glfw.GLFWReallocateCallbackI.invoke(long,long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWReallocateCallbackI.callback(long,long)"""
        super(__GLFWReallocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWJoystickCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWJoystickCallbackI as __GLFWJoystickCallbackI
__GLFWJoystickCallbackI = __GLFWJoystickCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWJoystickCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWJoystickCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWJoystickCallbackI) -> 'GLFWJoystickCallbackI':
        return GLFWJoystickCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWJoystickCallbackI):
        """
        Dynamic initializer for GLFWJoystickCallbackI.
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
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWJoystickCallbackI.invoke(int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWJoystickCallbackI.callback(long,long)"""
        super(__GLFWJoystickCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWJoystickCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWJoystickCallbackI, self).getCallInterface()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocator$Buffer
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
import org.lwjgl.glfw.GLFWAllocateCallback as __GLFWAllocateCallback
__GLFWAllocateCallback = __GLFWAllocateCallback
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

import org.lwjgl.glfw.GLFWAllocator as __GLFWAllocator_Buffer
__Buffer = __GLFWAllocator_Buffer.Buffer
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
import org.lwjgl.glfw.GLFWDeallocateCallback as __GLFWDeallocateCallback
__GLFWDeallocateCallback = __GLFWDeallocateCallback
import java.util.stream.Stream as Stream
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import int
import org.lwjgl.glfw.GLFWReallocateCallback as __GLFWReallocateCallback
__GLFWReallocateCallback = __GLFWReallocateCallback
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWAllocator.Buffer"""
 
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

    @overload
    def deallocate(self) -> 'GLFWDeallocateCallback':
        """public org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.deallocate()"""
        return 'GLFWDeallocateCallback'.__wrap(super(Buffer, self).deallocate())

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

    @overload
    def deallocate(self, arg0: 'GLFWDeallocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.deallocate(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).deallocate(arg0))

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
    def reallocate(self) -> 'GLFWReallocateCallback':
        """public org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.reallocate()"""
        return 'GLFWReallocateCallback'.__wrap(super(Buffer, self).reallocate())

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
    def user(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.user(long)"""
        return 'Buffer'.__wrap(super(__Buffer, self).user(__long.valueOf(arg0)))

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
    def reallocate(self, arg0: 'GLFWReallocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.reallocate(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).reallocate(arg0))

    @overload
    def user(self) -> int:
        """public long org.lwjgl.glfw.GLFWAllocator$Buffer.user()"""
        return int.__wrap(super(Buffer, self).user())

    @overload
    def allocate(self, arg0: 'GLFWAllocateCallbackI') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator$Buffer.allocate(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return 'Buffer'.__wrap(super(__Buffer, self).allocate(arg0))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWAllocator$Buffer(java.nio.ByteBuffer)"""
        val = __Buffer(arg0)
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
    def allocate(self) -> 'GLFWAllocateCallback':
        """public org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator$Buffer.allocate()"""
        return 'GLFWAllocateCallback'.__wrap(super(Buffer, self).allocate())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWAllocator$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowRefreshCallback
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWWindowRefreshCallbackI as __GLFWWindowRefreshCallbackI
__GLFWWindowRefreshCallbackI = __GLFWWindowRefreshCallbackI
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.glfw.GLFWWindowRefreshCallback as __GLFWWindowRefreshCallback
__GLFWWindowRefreshCallback = __GLFWWindowRefreshCallback
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
 
class GLFWWindowRefreshCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowRefreshCallbackI, GLFWWindowRefreshCallbackI):
    """org.lwjgl.glfw.GLFWWindowRefreshCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowRefreshCallback) -> 'GLFWWindowRefreshCallback':
        return GLFWWindowRefreshCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowRefreshCallback):
        """
        Dynamic initializer for GLFWWindowRefreshCallback.
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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.createSafe(long)"""
        return GLFWWindowRefreshCallback.__wrap(__GLFWWindowRefreshCallback.createSafe(__long.valueOf(arg0)))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowRefreshCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowRefreshCallbackI, self).getCallInterface())

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
    def create(arg0: int) -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.create(long)"""
        return GLFWWindowRefreshCallback.__wrap(__GLFWWindowRefreshCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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
    def create(arg0: 'GLFWWindowRefreshCallbackI') -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.create(org.lwjgl.glfw.GLFWWindowRefreshCallbackI)"""
        return GLFWWindowRefreshCallback.__wrap(__GLFWWindowRefreshCallback.create(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.callback(long,long)"""
        super(__GLFWWindowRefreshCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @overload
    def set(self, arg0: int) -> 'GLFWWindowRefreshCallback':
        """public org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFWWindowRefreshCallback.set(long)"""
        return 'GLFWWindowRefreshCallback'.__wrap(super(__GLFWWindowRefreshCallback, self).set(__long.valueOf(arg0)))

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

    @abstractmethod
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowRefreshCallbackI.invoke(long)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWDropCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWDropCallbackI as __GLFWDropCallbackI
__GLFWDropCallbackI = __GLFWDropCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWDropCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWDropCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWDropCallbackI) -> 'GLFWDropCallbackI':
        return GLFWDropCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWDropCallbackI):
        """
        Dynamic initializer for GLFWDropCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWDropCallbackI.callback(long,long)"""
        super(__GLFWDropCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWDropCallbackI.invoke(long,int,long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDropCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWDropCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocateCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWAllocateCallbackI as __GLFWAllocateCallbackI
__GLFWAllocateCallbackI = __GLFWAllocateCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWAllocateCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWAllocateCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWAllocateCallbackI) -> 'GLFWAllocateCallbackI':
        return GLFWAllocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWAllocateCallbackI):
        """
        Dynamic initializer for GLFWAllocateCallbackI.
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
    def invoke(self, arg0: int, arg1: int):
        """public abstract long org.lwjgl.glfw.GLFWAllocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWAllocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWAllocateCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWAllocateCallbackI.callback(long,long)"""
        super(__GLFWAllocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowIconifyCallback
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.glfw.GLFWWindowIconifyCallback as __GLFWWindowIconifyCallback
__GLFWWindowIconifyCallback = __GLFWWindowIconifyCallback
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.glfw.GLFWWindowIconifyCallbackI as __GLFWWindowIconifyCallbackI
__GLFWWindowIconifyCallbackI = __GLFWWindowIconifyCallbackI
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWWindowIconifyCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowIconifyCallbackI, GLFWWindowIconifyCallbackI):
    """org.lwjgl.glfw.GLFWWindowIconifyCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowIconifyCallback) -> 'GLFWWindowIconifyCallback':
        return GLFWWindowIconifyCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowIconifyCallback):
        """
        Dynamic initializer for GLFWWindowIconifyCallback.
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
    def set(self, arg0: int) -> 'GLFWWindowIconifyCallback':
        """public org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.set(long)"""
        return 'GLFWWindowIconifyCallback'.__wrap(super(__GLFWWindowIconifyCallback, self).set(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowIconifyCallbackI') -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.create(org.lwjgl.glfw.GLFWWindowIconifyCallbackI)"""
        return GLFWWindowIconifyCallback.__wrap(__GLFWWindowIconifyCallback.create(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.callback(long,long)"""
        super(__GLFWWindowIconifyCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.create(long)"""
        return GLFWWindowIconifyCallback.__wrap(__GLFWWindowIconifyCallback.create(__long.valueOf(arg0)))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowIconifyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowIconifyCallbackI, self).getCallInterface())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFWWindowIconifyCallback.createSafe(long)"""
        return GLFWWindowIconifyCallback.__wrap(__GLFWWindowIconifyCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowIconifyCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWWindowIconifyCallbackI as __GLFWWindowIconifyCallbackI
__GLFWWindowIconifyCallbackI = __GLFWWindowIconifyCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowIconifyCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowIconifyCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowIconifyCallbackI) -> 'GLFWWindowIconifyCallbackI':
        return GLFWWindowIconifyCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowIconifyCallbackI):
        """
        Dynamic initializer for GLFWWindowIconifyCallbackI.
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowIconifyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowIconifyCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowIconifyCallbackI.callback(long,long)"""
        super(__GLFWWindowIconifyCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWGL
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.lwjgl.glfw.GLFWNativeWGL as __GLFWNativeWGL
__GLFWNativeWGL = __GLFWNativeWGL
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWNativeWGL():
    """org.lwjgl.glfw.GLFWNativeWGL"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeWGL) -> 'GLFWNativeWGL':
        return GLFWNativeWGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeWGL):
        """
        Dynamic initializer for GLFWNativeWGL.
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
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeWGL.setPath(org.lwjgl.system.FunctionProvider)"""
        __GLFWNativeWGL.setPath(arg0)

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
    def glfwGetWGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWGL.glfwGetWGLContext(long)"""
        return int.__wrap(__GLFWNativeWGL.glfwGetWGLContext(__long.valueOf(arg0)))

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
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeWGL.setPath(java.lang.String)"""
        __GLFWNativeWGL.setPath(arg0)

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
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocateCallback
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
import org.lwjgl.glfw.GLFWAllocateCallback as __GLFWAllocateCallback
__GLFWAllocateCallback = __GLFWAllocateCallback
import org.lwjgl.glfw.GLFWAllocateCallbackI as __GLFWAllocateCallbackI
__GLFWAllocateCallbackI = __GLFWAllocateCallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWAllocateCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWAllocateCallbackI, GLFWAllocateCallbackI):
    """org.lwjgl.glfw.GLFWAllocateCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWAllocateCallback) -> 'GLFWAllocateCallback':
        return GLFWAllocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWAllocateCallback):
        """
        Dynamic initializer for GLFWAllocateCallback.
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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.createSafe(long)"""
        return GLFWAllocateCallback.__wrap(__GLFWAllocateCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWAllocateCallbackI') -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.create(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return GLFWAllocateCallback.__wrap(__GLFWAllocateCallback.create(arg0))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWAllocateCallbackI.callback(long,long)"""
        super(__GLFWAllocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocateCallback.create(long)"""
        return GLFWAllocateCallback.__wrap(__GLFWAllocateCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWAllocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWAllocateCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeEGL$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.glfw.GLFWNativeEGL as __GLFWNativeEGL_Functions
__Functions = __GLFWNativeEGL_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeEGL.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowMaximizeCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWWindowMaximizeCallbackI as __GLFWWindowMaximizeCallbackI
__GLFWWindowMaximizeCallbackI = __GLFWWindowMaximizeCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowMaximizeCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowMaximizeCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowMaximizeCallbackI) -> 'GLFWWindowMaximizeCallbackI':
        return GLFWWindowMaximizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowMaximizeCallbackI):
        """
        Dynamic initializer for GLFWWindowMaximizeCallbackI.
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
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowMaximizeCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowMaximizeCallbackI.callback(long,long)"""
        super(__GLFWWindowMaximizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeEGL
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.glfw.GLFWNativeEGL as __GLFWNativeEGL
__GLFWNativeEGL = __GLFWNativeEGL
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
 
class GLFWNativeEGL():
    """org.lwjgl.glfw.GLFWNativeEGL"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeEGL) -> 'GLFWNativeEGL':
        return GLFWNativeEGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeEGL):
        """
        Dynamic initializer for GLFWNativeEGL.
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
    def setEGLPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setEGLPath(org.lwjgl.system.FunctionProvider)"""
        __GLFWNativeEGL.setEGLPath(arg0)

    @staticmethod
    @overload
    def glfwGetEGLDisplay() -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLDisplay()"""
        return int.__wrap(__GLFWNativeEGL.glfwGetEGLDisplay())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setGLESPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setGLESPath(org.lwjgl.system.FunctionProvider)"""
        __GLFWNativeEGL.setGLESPath(arg0)

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
    def setGLESPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setGLESPath(java.lang.String)"""
        __GLFWNativeEGL.setGLESPath(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def glfwGetEGLSurface(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLSurface(long)"""
        return int.__wrap(__GLFWNativeEGL.glfwGetEGLSurface(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def setEGLPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeEGL.setEGLPath(java.lang.String)"""
        __GLFWNativeEGL.setEGLPath(arg0)

    @staticmethod
    @overload
    def glfwGetEGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLContext(long)"""
        return int.__wrap(__GLFWNativeEGL.glfwGetEGLContext(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetEGLConfig(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeEGL.glfwGetEGLConfig(long)"""
        return int.__wrap(__GLFWNativeEGL.glfwGetEGLConfig(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVidMode
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.glfw.GLFWVidMode as __GLFWVidMode
__GLFWVidMode = __GLFWVidMode
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import org.lwjgl.glfw.GLFWVidMode as __GLFWVidMode_Buffer
__Buffer = __GLFWVidMode_Buffer.Buffer
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
 
class GLFWVidMode(pyglsystem.__Struct, pyglsystem.Struct):
    """org.lwjgl.glfw.GLFWVidMode"""
 
    @staticmethod
    def __wrap(java_value: __GLFWVidMode) -> 'GLFWVidMode':
        return GLFWVidMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWVidMode):
        """
        Dynamic initializer for GLFWVidMode.
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
    def refreshRate(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.refreshRate()"""
        return int.__wrap(super(GLFWVidMode, self).refreshRate())

    @staticmethod
    @overload
    def nwidth(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nwidth(long)"""
        return int.__wrap(__GLFWVidMode.nwidth(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nblueBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nblueBits(long)"""
        return int.__wrap(__GLFWVidMode.nblueBits(__long.valueOf(arg0)))

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
    def createSafe(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFWVidMode.createSafe(long)"""
        return GLFWVidMode.__wrap(__GLFWVidMode.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nrefreshRate(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nrefreshRate(long)"""
        return int.__wrap(__GLFWVidMode.nrefreshRate(__long.valueOf(arg0)))

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @overload
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.height()"""
        return int.__wrap(super(GLFWVidMode, self).height())

    @staticmethod
    @overload
    def nheight(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nheight(long)"""
        return int.__wrap(__GLFWVidMode.nheight(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Pointer$Default.hashCode()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).hashCode())

    @overload
    def greenBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.greenBits()"""
        return int.__wrap(super(GLFWVidMode, self).greenBits())

    @staticmethod
    @overload
    def nredBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.nredBits(long)"""
        return int.__wrap(__GLFWVidMode.nredBits(__long.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFWVidMode.createSafe(long,int)"""
        return Buffer.__wrap(__GLFWVidMode.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.width()"""
        return int.__wrap(super(GLFWVidMode, self).width())

    @overload
    def redBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.redBits()"""
        return int.__wrap(super(GLFWVidMode, self).redBits())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFWVidMode.create(long)"""
        return GLFWVidMode.__wrap(__GLFWVidMode.create(__long.valueOf(arg0)))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.sizeof()"""
        return int.__wrap(super(GLFWVidMode, self).sizeof())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFWVidMode.create(long,int)"""
        return Buffer.__wrap(__GLFWVidMode.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

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

    @overload
    def blueBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode.blueBits()"""
        return int.__wrap(super(GLFWVidMode, self).blueBits())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWVidMode(java.nio.ByteBuffer)"""
        val = __GLFWVidMode(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ngreenBits(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWVidMode.ngreenBits(long)"""
        return int.__wrap(__GLFWVidMode.ngreenBits(__long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWReallocateCallback
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
import org.lwjgl.glfw.GLFWReallocateCallbackI as __GLFWReallocateCallbackI
__GLFWReallocateCallbackI = __GLFWReallocateCallbackI
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
import org.lwjgl.glfw.GLFWReallocateCallback as __GLFWReallocateCallback
__GLFWReallocateCallback = __GLFWReallocateCallback
from builtins import int
 
class GLFWReallocateCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWReallocateCallbackI, GLFWReallocateCallbackI):
    """org.lwjgl.glfw.GLFWReallocateCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWReallocateCallback) -> 'GLFWReallocateCallback':
        return GLFWReallocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWReallocateCallback):
        """
        Dynamic initializer for GLFWReallocateCallback.
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
    def createSafe(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.createSafe(long)"""
        return GLFWReallocateCallback.__wrap(__GLFWReallocateCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: 'GLFWReallocateCallbackI') -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.create(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return GLFWReallocateCallback.__wrap(__GLFWReallocateCallback.create(arg0))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWReallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWReallocateCallbackI, self).getCallInterface())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract long org.lwjgl.glfw.GLFWReallocateCallbackI.invoke(long,long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWReallocateCallbackI.callback(long,long)"""
        super(__GLFWReallocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWReallocateCallback.create(long)"""
        return GLFWReallocateCallback.__wrap(__GLFWReallocateCallback.create(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWCharCallbackI as __GLFWCharCallbackI
__GLFWCharCallbackI = __GLFWCharCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWCharCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWCharCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCharCallbackI) -> 'GLFWCharCallbackI':
        return GLFWCharCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCharCallbackI):
        """
        Dynamic initializer for GLFWCharCallbackI.
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
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWCharCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCharCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharCallbackI.callback(long,long)"""
        super(__GLFWCharCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowFocusCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.glfw.GLFWWindowFocusCallbackI as __GLFWWindowFocusCallbackI
__GLFWWindowFocusCallbackI = __GLFWWindowFocusCallbackI
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowFocusCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowFocusCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowFocusCallbackI) -> 'GLFWWindowFocusCallbackI':
        return GLFWWindowFocusCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowFocusCallbackI):
        """
        Dynamic initializer for GLFWWindowFocusCallbackI.
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowFocusCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowFocusCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowFocusCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowFocusCallbackI.callback(long,long)"""
        super(__GLFWWindowFocusCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowSizeCallback
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

import org.lwjgl.glfw.GLFWWindowSizeCallbackI as __GLFWWindowSizeCallbackI
__GLFWWindowSizeCallbackI = __GLFWWindowSizeCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWWindowSizeCallback as __GLFWWindowSizeCallback
__GLFWWindowSizeCallback = __GLFWWindowSizeCallback
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
 
class GLFWWindowSizeCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowSizeCallbackI, GLFWWindowSizeCallbackI):
    """org.lwjgl.glfw.GLFWWindowSizeCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowSizeCallback) -> 'GLFWWindowSizeCallback':
        return GLFWWindowSizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowSizeCallback):
        """
        Dynamic initializer for GLFWWindowSizeCallback.
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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowSizeCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.create(long)"""
        return GLFWWindowSizeCallback.__wrap(__GLFWWindowSizeCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowSizeCallbackI.callback(long,long)"""
        super(__GLFWWindowSizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def set(self, arg0: int) -> 'GLFWWindowSizeCallback':
        """public org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.set(long)"""
        return 'GLFWWindowSizeCallback'.__wrap(super(__GLFWWindowSizeCallback, self).set(__long.valueOf(arg0)))

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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.createSafe(long)"""
        return GLFWWindowSizeCallback.__wrap(__GLFWWindowSizeCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowSizeCallbackI') -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFWWindowSizeCallback.create(org.lwjgl.glfw.GLFWWindowSizeCallbackI)"""
        return GLFWWindowSizeCallback.__wrap(__GLFWWindowSizeCallback.create(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDeallocateCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWDeallocateCallbackI as __GLFWDeallocateCallbackI
__GLFWDeallocateCallbackI = __GLFWDeallocateCallbackI
from builtins import int
 
class GLFWDeallocateCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWDeallocateCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWDeallocateCallbackI) -> 'GLFWDeallocateCallbackI':
        return GLFWDeallocateCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWDeallocateCallbackI):
        """
        Dynamic initializer for GLFWDeallocateCallbackI.
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
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWDeallocateCallbackI.invoke(long,long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDeallocateCallbackI.callback(long,long)"""
        super(__GLFWDeallocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDeallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWDeallocateCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDeallocateCallback
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
import org.lwjgl.glfw.GLFWDeallocateCallback as __GLFWDeallocateCallback
__GLFWDeallocateCallback = __GLFWDeallocateCallback
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import org.lwjgl.glfw.GLFWDeallocateCallbackI as __GLFWDeallocateCallbackI
__GLFWDeallocateCallbackI = __GLFWDeallocateCallbackI
 
class GLFWDeallocateCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWDeallocateCallbackI, GLFWDeallocateCallbackI):
    """org.lwjgl.glfw.GLFWDeallocateCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWDeallocateCallback) -> 'GLFWDeallocateCallback':
        return GLFWDeallocateCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWDeallocateCallback):
        """
        Dynamic initializer for GLFWDeallocateCallback.
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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWDeallocateCallbackI.invoke(long,long)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDeallocateCallbackI.callback(long,long)"""
        super(__GLFWDeallocateCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDeallocateCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWDeallocateCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.create(long)"""
        return GLFWDeallocateCallback.__wrap(__GLFWDeallocateCallback.create(__long.valueOf(arg0)))

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
    def createSafe(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.createSafe(long)"""
        return GLFWDeallocateCallback.__wrap(__GLFWDeallocateCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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

    @staticmethod
    @overload
    def create(arg0: 'GLFWDeallocateCallbackI') -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWDeallocateCallback.create(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return GLFWDeallocateCallback.__wrap(__GLFWDeallocateCallback.create(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowPosCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWWindowPosCallbackI as __GLFWWindowPosCallbackI
__GLFWWindowPosCallbackI = __GLFWWindowPosCallbackI
from builtins import int
 
class GLFWWindowPosCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowPosCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowPosCallbackI) -> 'GLFWWindowPosCallbackI':
        return GLFWWindowPosCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowPosCallbackI):
        """
        Dynamic initializer for GLFWWindowPosCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWWindowPosCallbackI.callback(long,long)"""
        super(__GLFWWindowPosCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowPosCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowPosCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowSizeCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWWindowSizeCallbackI as __GLFWWindowSizeCallbackI
__GLFWWindowSizeCallbackI = __GLFWWindowSizeCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowSizeCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowSizeCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowSizeCallbackI) -> 'GLFWWindowSizeCallbackI':
        return GLFWWindowSizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowSizeCallbackI):
        """
        Dynamic initializer for GLFWWindowSizeCallbackI.
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
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowSizeCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowSizeCallbackI.callback(long,long)"""
        super(__GLFWWindowSizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWKeyCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.glfw.GLFWKeyCallbackI as __GLFWKeyCallbackI
__GLFWKeyCallbackI = __GLFWKeyCallbackI
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWKeyCallback as __GLFWKeyCallback
__GLFWKeyCallback = __GLFWKeyCallback
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
 
class GLFWKeyCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWKeyCallbackI, GLFWKeyCallbackI):
    """org.lwjgl.glfw.GLFWKeyCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWKeyCallback) -> 'GLFWKeyCallback':
        return GLFWKeyCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWKeyCallback):
        """
        Dynamic initializer for GLFWKeyCallback.
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
    def create(arg0: int) -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.create(long)"""
        return GLFWKeyCallback.__wrap(__GLFWKeyCallback.create(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int) -> 'GLFWKeyCallback':
        """public org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.set(long)"""
        return 'GLFWKeyCallback'.__wrap(super(__GLFWKeyCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.createSafe(long)"""
        return GLFWKeyCallback.__wrap(__GLFWKeyCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWKeyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWKeyCallbackI, self).getCallInterface())

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

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWKeyCallbackI.callback(long,long)"""
        super(__GLFWKeyCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWKeyCallbackI') -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFWKeyCallback.create(org.lwjgl.glfw.GLFWKeyCallbackI)"""
        return GLFWKeyCallback.__wrap(__GLFWKeyCallback.create(arg0))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWMonitorCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWMonitorCallbackI as __GLFWMonitorCallbackI
__GLFWMonitorCallbackI = __GLFWMonitorCallbackI
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
import org.lwjgl.glfw.GLFWMonitorCallback as __GLFWMonitorCallback
__GLFWMonitorCallback = __GLFWMonitorCallback
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
 
class GLFWMonitorCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWMonitorCallbackI, GLFWMonitorCallbackI):
    """org.lwjgl.glfw.GLFWMonitorCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWMonitorCallback) -> 'GLFWMonitorCallback':
        return GLFWMonitorCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWMonitorCallback):
        """
        Dynamic initializer for GLFWMonitorCallback.
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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWMonitorCallbackI.invoke(long,int)"""
        pass

    @overload
    def set(self) -> 'GLFWMonitorCallback':
        """public org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.set()"""
        return 'GLFWMonitorCallback'.__wrap(super(GLFWMonitorCallback, self).set())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMonitorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWMonitorCallbackI, self).getCallInterface())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.createSafe(long)"""
        return GLFWMonitorCallback.__wrap(__GLFWMonitorCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWMonitorCallbackI') -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.create(org.lwjgl.glfw.GLFWMonitorCallbackI)"""
        return GLFWMonitorCallback.__wrap(__GLFWMonitorCallback.create(arg0))

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
    def create(arg0: int) -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFWMonitorCallback.create(long)"""
        return GLFWMonitorCallback.__wrap(__GLFWMonitorCallback.create(__long.valueOf(arg0)))

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
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMonitorCallbackI.callback(long,long)"""
        super(__GLFWMonitorCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWin32
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.glfw.GLFWNativeWin32 as __GLFWNativeWin32
__GLFWNativeWin32 = __GLFWNativeWin32
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWNativeWin32():
    """org.lwjgl.glfw.GLFWNativeWin32"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeWin32) -> 'GLFWNativeWin32':
        return GLFWNativeWin32(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeWin32):
        """
        Dynamic initializer for GLFWNativeWin32.
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
    def nglfwGetWin32Adapter(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.nglfwGetWin32Adapter(long)"""
        return int.__wrap(__GLFWNativeWin32.nglfwGetWin32Adapter(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def glfwGetWin32Adapter(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Adapter(long)"""
        return str.__wrap(__GLFWNativeWin32.glfwGetWin32Adapter(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nglfwGetWin32Monitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.nglfwGetWin32Monitor(long)"""
        return int.__wrap(__GLFWNativeWin32.nglfwGetWin32Monitor(__long.valueOf(arg0)))

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
    def glfwAttachWin32Window(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.glfwAttachWin32Window(long,long)"""
        return int.__wrap(__GLFWNativeWin32.glfwAttachWin32Window(__long.valueOf(arg0), __long.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def glfwGetWin32Window(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Window(long)"""
        return int.__wrap(__GLFWNativeWin32.glfwGetWin32Window(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetWin32Monitor(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWNativeWin32.glfwGetWin32Monitor(long)"""
        return str.__wrap(__GLFWNativeWin32.glfwGetWin32Monitor(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWCharCallback as __GLFWCharCallback
__GLFWCharCallback = __GLFWCharCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWCharCallbackI as __GLFWCharCallbackI
__GLFWCharCallbackI = __GLFWCharCallbackI
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
 
class GLFWCharCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWCharCallbackI, GLFWCharCallbackI):
    """org.lwjgl.glfw.GLFWCharCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCharCallback) -> 'GLFWCharCallback':
        return GLFWCharCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCharCallback):
        """
        Dynamic initializer for GLFWCharCallback.
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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCharCallbackI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.create(long)"""
        return GLFWCharCallback.__wrap(__GLFWCharCallback.create(__long.valueOf(arg0)))

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
    def create(arg0: 'GLFWCharCallbackI') -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.create(org.lwjgl.glfw.GLFWCharCallbackI)"""
        return GLFWCharCallback.__wrap(__GLFWCharCallback.create(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.createSafe(long)"""
        return GLFWCharCallback.__wrap(__GLFWCharCallback.createSafe(__long.valueOf(arg0)))

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
    def getSafe(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.getSafe(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.getSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWCharCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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
        """public default void org.lwjgl.glfw.GLFWCharCallbackI.callback(long,long)"""
        super(__GLFWCharCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @overload
    def set(self, arg0: int) -> 'GLFWCharCallback':
        """public org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFWCharCallback.set(long)"""
        return 'GLFWCharCallback'.__wrap(super(__GLFWCharCallback, self).set(__long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWErrorCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWErrorCallbackI as __GLFWErrorCallbackI
__GLFWErrorCallbackI = __GLFWErrorCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWErrorCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWErrorCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWErrorCallbackI) -> 'GLFWErrorCallbackI':
        return GLFWErrorCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWErrorCallbackI):
        """
        Dynamic initializer for GLFWErrorCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWErrorCallbackI.callback(long,long)"""
        super(__GLFWErrorCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWErrorCallbackI.invoke(int,long)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWErrorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWErrorCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeGLX
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.lwjgl.glfw.GLFWNativeGLX as __GLFWNativeGLX
__GLFWNativeGLX = __GLFWNativeGLX
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWNativeGLX():
    """org.lwjgl.glfw.GLFWNativeGLX"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeGLX) -> 'GLFWNativeGLX':
        return GLFWNativeGLX(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeGLX):
        """
        Dynamic initializer for GLFWNativeGLX.
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
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeGLX.setPath(java.lang.String)"""
        __GLFWNativeGLX.setPath(arg0)

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
    def glfwGetGLXContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXContext(long)"""
        return int.__wrap(__GLFWNativeGLX.glfwGetGLXContext(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeGLX.setPath(org.lwjgl.system.FunctionProvider)"""
        __GLFWNativeGLX.setPath(arg0)

    @staticmethod
    @overload
    def glfwGetGLXFBConfig(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXFBConfig(long)"""
        return int.__wrap(__GLFWNativeGLX.glfwGetGLXFBConfig(__long.valueOf(arg0)))

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
    def glfwGetGLXWindow(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeGLX.glfwGetGLXWindow(long)"""
        return int.__wrap(__GLFWNativeGLX.glfwGetGLXWindow(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGammaRamp
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWGammaRamp as __GLFWGammaRamp_Buffer
__Buffer = __GLFWGammaRamp_Buffer.Buffer
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import java.nio.ShortBuffer as ShortBuffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import org.lwjgl.glfw.GLFWGammaRamp as __GLFWGammaRamp
__GLFWGammaRamp = __GLFWGammaRamp
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class GLFWGammaRamp(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWGammaRamp"""
 
    @staticmethod
    def __wrap(java_value: __GLFWGammaRamp) -> 'GLFWGammaRamp':
        return GLFWGammaRamp(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWGammaRamp):
        """
        Dynamic initializer for GLFWGammaRamp.
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
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.calloc(int)"""
        return Buffer.__wrap(__GLFWGammaRamp.calloc(__int.valueOf(arg0)))

    @overload
    def blue(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.blue()"""
        return 'ShortBuffer'.__wrap(super(GLFWGammaRamp, self).blue())

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
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.malloc(int)"""
        return Buffer.__wrap(__GLFWGammaRamp.malloc(__int.valueOf(arg0)))

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
        """public org.lwjgl.glfw.GLFWGammaRamp(java.nio.ByteBuffer)"""
        val = __GLFWGammaRamp(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def red(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.red(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).red(arg0))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp.sizeof()"""
        return int.__wrap(super(GLFWGammaRamp, self).sizeof())

    @staticmethod
    @overload
    def nblue(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nblue(long,java.nio.ShortBuffer)"""
        __GLFWGammaRamp.nblue(__long.valueOf(arg0), arg1)

    @overload
    def red(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.red()"""
        return 'ShortBuffer'.__wrap(super(GLFWGammaRamp, self).red())

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.validate(long)"""
        __GLFWGammaRamp.validate(__long.valueOf(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.create(long)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.malloc()"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.malloc())

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @staticmethod
    @overload
    def nblue(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.nblue(long)"""
        return ShortBuffer.__wrap(__GLFWGammaRamp.nblue(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGammaRamp.callocStack(__int.valueOf(arg0), arg1))

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
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGammaRamp.calloc(__int.valueOf(arg0), arg1))

    @overload
    def blue(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.blue(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).blue(arg0))

    @overload
    def set(self, arg0: 'GLFWGammaRamp') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.set(org.lwjgl.glfw.GLFWGammaRamp)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).set(arg0))

    @overload
    def green(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.green()"""
        return 'ShortBuffer'.__wrap(super(GLFWGammaRamp, self).green())

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.createSafe(long,int)"""
        return Buffer.__wrap(__GLFWGammaRamp.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ngreen(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.ngreen(long,java.nio.ShortBuffer)"""
        __GLFWGammaRamp.ngreen(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def callocStack() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.callocStack()"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.callocStack())

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
    def nsize(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nsize(long,int)"""
        __GLFWGammaRamp.nsize(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.mallocStack()"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.mallocStack())

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.callocStack(arg0))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.create(long,int)"""
        return Buffer.__wrap(__GLFWGammaRamp.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nsize(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFWGammaRamp.nsize(long)"""
        return int.__wrap(__GLFWGammaRamp.nsize(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGammaRamp.malloc(__int.valueOf(arg0), arg1))

    @overload
    def green(self, arg0: 'ShortBuffer') -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.green(java.nio.ShortBuffer)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).green(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.createSafe(long)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.mallocStack(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def ngreen(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.ngreen(long)"""
        return ShortBuffer.__wrap(__GLFWGammaRamp.ngreen(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.callocStack(int)"""
        return Buffer.__wrap(__GLFWGammaRamp.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGammaRamp.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def size(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp.size()"""
        return int.__wrap(super(GLFWGammaRamp, self).size())

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @overload
    def set(self, arg0: 'ShortBuffer', arg1: 'ShortBuffer', arg2: 'ShortBuffer', arg3: int) -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.set(java.nio.ShortBuffer,java.nio.ShortBuffer,java.nio.ShortBuffer,int)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).set(arg0, arg1, arg2, __int.valueOf(arg3)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.create(int)"""
        return Buffer.__wrap(__GLFWGammaRamp.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.create()"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.create())

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
    def size(self, arg0: int) -> 'GLFWGammaRamp':
        """public org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.size(int)"""
        return 'GLFWGammaRamp'.__wrap(super(__GLFWGammaRamp, self).size(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc() -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.calloc()"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.calloc())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.malloc(arg0))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFWGammaRamp.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGammaRamp.__wrap(__GLFWGammaRamp.calloc(arg0))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def nred(arg0: int) -> 'ShortBuffer':
        """public static java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp.nred(long)"""
        return ShortBuffer.__wrap(__GLFWGammaRamp.nred(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp.mallocStack(int)"""
        return Buffer.__wrap(__GLFWGammaRamp.mallocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nred(arg0: int, arg1: 'ShortBuffer'):
        """public static void org.lwjgl.glfw.GLFWGammaRamp.nred(long,java.nio.ShortBuffer)"""
        __GLFWGammaRamp.nred(__long.valueOf(arg0), arg1) 
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowContentScaleCallback
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
import org.lwjgl.glfw.GLFWWindowContentScaleCallback as __GLFWWindowContentScaleCallback
__GLFWWindowContentScaleCallback = __GLFWWindowContentScaleCallback
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
import org.lwjgl.glfw.GLFWWindowContentScaleCallbackI as __GLFWWindowContentScaleCallbackI
__GLFWWindowContentScaleCallbackI = __GLFWWindowContentScaleCallbackI
from builtins import int
 
class GLFWWindowContentScaleCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowContentScaleCallbackI, GLFWWindowContentScaleCallbackI):
    """org.lwjgl.glfw.GLFWWindowContentScaleCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowContentScaleCallback) -> 'GLFWWindowContentScaleCallback':
        return GLFWWindowContentScaleCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowContentScaleCallback):
        """
        Dynamic initializer for GLFWWindowContentScaleCallback.
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
    def createSafe(arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.createSafe(long)"""
        return GLFWWindowContentScaleCallback.__wrap(__GLFWWindowContentScaleCallback.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: 'GLFWWindowContentScaleCallbackI') -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.create(org.lwjgl.glfw.GLFWWindowContentScaleCallbackI)"""
        return GLFWWindowContentScaleCallback.__wrap(__GLFWWindowContentScaleCallback.create(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowContentScaleCallbackI, self).getCallInterface())

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.invoke(long,float,float)"""
        pass

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
    def create(arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.create(long)"""
        return GLFWWindowContentScaleCallback.__wrap(__GLFWWindowContentScaleCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.callback(long,long)"""
        super(__GLFWWindowContentScaleCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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

    @overload
    def set(self, arg0: int) -> 'GLFWWindowContentScaleCallback':
        """public org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFWWindowContentScaleCallback.set(long)"""
        return 'GLFWWindowContentScaleCallback'.__wrap(super(__GLFWWindowContentScaleCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWDropCallback
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWDropCallback as __GLFWDropCallback
__GLFWDropCallback = __GLFWDropCallback
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
import org.lwjgl.glfw.GLFWDropCallbackI as __GLFWDropCallbackI
__GLFWDropCallbackI = __GLFWDropCallbackI
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWDropCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWDropCallbackI, GLFWDropCallbackI):
    """org.lwjgl.glfw.GLFWDropCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWDropCallback) -> 'GLFWDropCallback':
        return GLFWDropCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWDropCallback):
        """
        Dynamic initializer for GLFWDropCallback.
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

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.create(long)"""
        return GLFWDropCallback.__wrap(__GLFWDropCallback.create(__long.valueOf(arg0)))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWDropCallbackI.invoke(long,int,long)"""
        pass

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
    def getName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWDropCallback.getName(long,int)"""
        return str.__wrap(__GLFWDropCallback.getName(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @overload
    def set(self, arg0: int) -> 'GLFWDropCallback':
        """public org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.set(long)"""
        return 'GLFWDropCallback'.__wrap(super(__GLFWDropCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWDropCallbackI.callback(long,long)"""
        super(__GLFWDropCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def create(arg0: 'GLFWDropCallbackI') -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.create(org.lwjgl.glfw.GLFWDropCallbackI)"""
        return GLFWDropCallback.__wrap(__GLFWDropCallback.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFWDropCallback.createSafe(long)"""
        return GLFWDropCallback.__wrap(__GLFWDropCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWDropCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWDropCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeX11$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.glfw.GLFWNativeX11 as __GLFWNativeX11_Functions
__Functions = __GLFWNativeX11_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeX11.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeNSGL$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import org.lwjgl.glfw.GLFWNativeNSGL as __GLFWNativeNSGL_Functions
__Functions = __GLFWNativeNSGL_Functions.Functions
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeNSGL.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowContentScaleCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWWindowContentScaleCallbackI as __GLFWWindowContentScaleCallbackI
__GLFWWindowContentScaleCallbackI = __GLFWWindowContentScaleCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowContentScaleCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowContentScaleCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowContentScaleCallbackI) -> 'GLFWWindowContentScaleCallbackI':
        return GLFWWindowContentScaleCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowContentScaleCallbackI):
        """
        Dynamic initializer for GLFWWindowContentScaleCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.callback(long,long)"""
        super(__GLFWWindowContentScaleCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowContentScaleCallbackI, self).getCallInterface())

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWWindowContentScaleCallbackI.invoke(long,float,float)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharModsCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import org.lwjgl.glfw.GLFWCharModsCallback as __GLFWCharModsCallback
__GLFWCharModsCallback = __GLFWCharModsCallback
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.glfw.GLFWCharModsCallbackI as __GLFWCharModsCallbackI
__GLFWCharModsCallbackI = __GLFWCharModsCallbackI
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
 
class GLFWCharModsCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWCharModsCallbackI, GLFWCharModsCallbackI):
    """org.lwjgl.glfw.GLFWCharModsCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCharModsCallback) -> 'GLFWCharModsCallback':
        return GLFWCharModsCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCharModsCallback):
        """
        Dynamic initializer for GLFWCharModsCallback.
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
    def create(arg0: int) -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.create(long)"""
        return GLFWCharModsCallback.__wrap(__GLFWCharModsCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @overload
    def set(self, arg0: int) -> 'GLFWCharModsCallback':
        """public org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.set(long)"""
        return 'GLFWCharModsCallback'.__wrap(super(__GLFWCharModsCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharModsCallbackI.callback(long,long)"""
        super(__GLFWCharModsCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharModsCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCharModsCallbackI, self).getCallInterface())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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
    def create(arg0: 'GLFWCharModsCallbackI') -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.create(org.lwjgl.glfw.GLFWCharModsCallbackI)"""
        return GLFWCharModsCallback.__wrap(__GLFWCharModsCallback.create(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFWCharModsCallback.createSafe(long)"""
        return GLFWCharModsCallback.__wrap(__GLFWCharModsCallback.createSafe(__long.valueOf(arg0)))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWCharModsCallbackI.invoke(long,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWErrorCallback
from pyquantum_helper import import_once as __import_once__
from builtins import str
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import org.lwjgl.glfw.GLFWErrorCallbackI as __GLFWErrorCallbackI
__GLFWErrorCallbackI = __GLFWErrorCallbackI
import org.lwjgl.glfw.GLFWErrorCallback as __GLFWErrorCallback
__GLFWErrorCallback = __GLFWErrorCallback
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
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWErrorCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWErrorCallbackI, GLFWErrorCallbackI):
    """org.lwjgl.glfw.GLFWErrorCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWErrorCallback) -> 'GLFWErrorCallback':
        return GLFWErrorCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWErrorCallback):
        """
        Dynamic initializer for GLFWErrorCallback.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createPrint() -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createPrint()"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.createPrint())

    @staticmethod
    @overload
    def get(arg0: int) -> 'pyglsystem.CallbackI':
        """public static <T extends org.lwjgl.system.CallbackI> T org.lwjgl.system.Callback.get(long)"""
        return pyglsystem.CallbackI.__wrap(__Callback.get(__long.valueOf(arg0)))

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
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWErrorCallbackI.callback(long,long)"""
        super(__GLFWErrorCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def createThrow() -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createThrow()"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.createThrow())

    @staticmethod
    @overload
    def getDescription(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFWErrorCallback.getDescription(long)"""
        return str.__wrap(__GLFWErrorCallback.getDescription(__long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWErrorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWErrorCallbackI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def createPrint(arg0: 'PrintStream') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createPrint(java.io.PrintStream)"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.createPrint(arg0))

    @staticmethod
    @overload
    def create(arg0: 'GLFWErrorCallbackI') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.create(org.lwjgl.glfw.GLFWErrorCallbackI)"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.create(arg0))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWErrorCallbackI.invoke(int,long)"""
        pass

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

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
    def set(self) -> 'GLFWErrorCallback':
        """public org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.set()"""
        return 'GLFWErrorCallback'.__wrap(super(GLFWErrorCallback, self).set())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.createSafe(long)"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Callback.free()"""
        super(pyglsystem.Callback, self).free()

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFWErrorCallback.create(long)"""
        return GLFWErrorCallback.__wrap(__GLFWErrorCallback.create(__long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWMouseButtonCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
import org.lwjgl.glfw.GLFWMouseButtonCallbackI as __GLFWMouseButtonCallbackI
__GLFWMouseButtonCallbackI = __GLFWMouseButtonCallbackI
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWMouseButtonCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWMouseButtonCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWMouseButtonCallbackI) -> 'GLFWMouseButtonCallbackI':
        return GLFWMouseButtonCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWMouseButtonCallbackI):
        """
        Dynamic initializer for GLFWMouseButtonCallbackI.
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
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void org.lwjgl.glfw.GLFWMouseButtonCallbackI.invoke(long,int,int,int)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMouseButtonCallbackI.callback(long,long)"""
        super(__GLFWMouseButtonCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMouseButtonCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWMouseButtonCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWayland$Functions
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
import org.lwjgl.glfw.GLFWNativeWayland as __GLFWNativeWayland_Functions
__Functions = __GLFWNativeWayland_Functions.Functions
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWayland.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowFocusCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
import org.lwjgl.glfw.GLFWWindowFocusCallbackI as __GLFWWindowFocusCallbackI
__GLFWWindowFocusCallbackI = __GLFWWindowFocusCallbackI
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
import org.lwjgl.glfw.GLFWWindowFocusCallback as __GLFWWindowFocusCallback
__GLFWWindowFocusCallback = __GLFWWindowFocusCallback
from builtins import bool
from builtins import int
 
class GLFWWindowFocusCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWWindowFocusCallbackI, GLFWWindowFocusCallbackI):
    """org.lwjgl.glfw.GLFWWindowFocusCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowFocusCallback) -> 'GLFWWindowFocusCallback':
        return GLFWWindowFocusCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowFocusCallback):
        """
        Dynamic initializer for GLFWWindowFocusCallback.
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
    def set(self, arg0: int) -> 'GLFWWindowFocusCallback':
        """public org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.set(long)"""
        return 'GLFWWindowFocusCallback'.__wrap(super(__GLFWWindowFocusCallback, self).set(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.createSafe(long)"""
        return GLFWWindowFocusCallback.__wrap(__GLFWWindowFocusCallback.createSafe(__long.valueOf(arg0)))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWWindowFocusCallbackI.invoke(long,boolean)"""
        pass

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
    def create(arg0: 'GLFWWindowFocusCallbackI') -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.create(org.lwjgl.glfw.GLFWWindowFocusCallbackI)"""
        return GLFWWindowFocusCallback.__wrap(__GLFWWindowFocusCallback.create(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFWWindowFocusCallback.create(long)"""
        return GLFWWindowFocusCallback.__wrap(__GLFWWindowFocusCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowFocusCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowFocusCallbackI, self).getCallInterface())

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

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowFocusCallbackI.callback(long,long)"""
        super(__GLFWWindowFocusCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.Callbacks
from builtins import str
import org.lwjgl.glfw.Callbacks as __Callbacks
__Callbacks = __Callbacks
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
 
class Callbacks():
    """org.lwjgl.glfw.Callbacks"""
 
    @staticmethod
    def __wrap(java_value: __Callbacks) -> 'Callbacks':
        return Callbacks(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Callbacks):
        """
        Dynamic initializer for Callbacks.
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
    def glfwFreeCallbacks(arg0: int):
        """public static void org.lwjgl.glfw.Callbacks.glfwFreeCallbacks(long)"""
        __Callbacks.glfwFreeCallbacks(__long.valueOf(arg0))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeCocoa$Functions
from builtins import str
import org.lwjgl.glfw.GLFWNativeCocoa as __GLFWNativeCocoa_Functions
__Functions = __GLFWNativeCocoa_Functions.Functions
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
    """org.lwjgl.glfw.GLFWNativeCocoa.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeGLX$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.glfw.GLFWNativeGLX as __GLFWNativeGLX_Functions
__Functions = __GLFWNativeGLX_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeGLX.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorPosCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWCursorPosCallbackI as __GLFWCursorPosCallbackI
__GLFWCursorPosCallbackI = __GLFWCursorPosCallbackI
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.glfw.GLFWCursorPosCallback as __GLFWCursorPosCallback
__GLFWCursorPosCallback = __GLFWCursorPosCallback
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
 
class GLFWCursorPosCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWCursorPosCallbackI, GLFWCursorPosCallbackI):
    """org.lwjgl.glfw.GLFWCursorPosCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCursorPosCallback) -> 'GLFWCursorPosCallback':
        return GLFWCursorPosCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCursorPosCallback):
        """
        Dynamic initializer for GLFWCursorPosCallback.
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
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCursorPosCallbackI, self).getCallInterface())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.lwjgl.system.Callback.equals(java.lang.Object)"""
        return bool.__wrap(super(__pyglsystem.Callback, self).equals(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.createSafe(long)"""
        return GLFWCursorPosCallback.__wrap(__GLFWCursorPosCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorPosCallbackI.callback(long,long)"""
        super(__GLFWCursorPosCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

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

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWCursorPosCallbackI.invoke(long,double,double)"""
        pass

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
    def create(arg0: int) -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.create(long)"""
        return GLFWCursorPosCallback.__wrap(__GLFWCursorPosCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

    @staticmethod
    @overload
    def create(arg0: 'GLFWCursorPosCallbackI') -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.create(org.lwjgl.glfw.GLFWCursorPosCallbackI)"""
        return GLFWCursorPosCallback.__wrap(__GLFWCursorPosCallback.create(arg0))

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

    @overload
    def set(self, arg0: int) -> 'GLFWCursorPosCallback':
        """public org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFWCursorPosCallback.set(long)"""
        return 'GLFWCursorPosCallback'.__wrap(super(__GLFWCursorPosCallback, self).set(__long.valueOf(arg0)))

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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeNSGL
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
import org.lwjgl.glfw.GLFWNativeNSGL as __GLFWNativeNSGL
__GLFWNativeNSGL = __GLFWNativeNSGL
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWNativeNSGL():
    """org.lwjgl.glfw.GLFWNativeNSGL"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeNSGL) -> 'GLFWNativeNSGL':
        return GLFWNativeNSGL(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeNSGL):
        """
        Dynamic initializer for GLFWNativeNSGL.
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

    @staticmethod
    @overload
    def glfwGetNSGLContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeNSGL.glfwGetNSGLContext(long)"""
        return int.__wrap(__GLFWNativeNSGL.glfwGetNSGLContext(__long.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWFramebufferSizeCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWFramebufferSizeCallbackI as __GLFWFramebufferSizeCallbackI
__GLFWFramebufferSizeCallbackI = __GLFWFramebufferSizeCallbackI
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWFramebufferSizeCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWFramebufferSizeCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWFramebufferSizeCallbackI) -> 'GLFWFramebufferSizeCallbackI':
        return GLFWFramebufferSizeCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWFramebufferSizeCallbackI):
        """
        Dynamic initializer for GLFWFramebufferSizeCallbackI.
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
        """public default void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.callback(long,long)"""
        super(__GLFWFramebufferSizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.invoke(long,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWFramebufferSizeCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGamepadState
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
from builtins import float
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.glfw.GLFWGamepadState as __GLFWGamepadState_Buffer
__Buffer = __GLFWGamepadState_Buffer.Buffer
import java.nio.FloatBuffer as FloatBuffer
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.Byte as __byte
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import bool
import org.lwjgl.glfw.GLFWGamepadState as __GLFWGamepadState
__GLFWGamepadState = __GLFWGamepadState
from builtins import int
 
class GLFWGamepadState(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWGamepadState"""
 
    @staticmethod
    def __wrap(java_value: __GLFWGamepadState) -> 'GLFWGamepadState':
        return GLFWGamepadState(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWGamepadState):
        """
        Dynamic initializer for GLFWGamepadState.
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
    def nbuttons(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,java.nio.ByteBuffer)"""
        __GLFWGamepadState.nbuttons(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGamepadState.calloc(__int.valueOf(arg0), arg1))

    @overload
    def buttons(self, arg0: 'ByteBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.buttons(java.nio.ByteBuffer)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).buttons(arg0))

    @staticmethod
    @overload
    def malloc() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.malloc()"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.malloc())

    @overload
    def set(self, arg0: 'GLFWGamepadState') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.set(org.lwjgl.glfw.GLFWGamepadState)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).set(arg0))

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.createSafe(long)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.createSafe(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nbuttons(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState.nbuttons(long)"""
        return ByteBuffer.__wrap(__GLFWGamepadState.nbuttons(__long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def callocStack() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.callocStack()"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.callocStack())

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.create(int)"""
        return Buffer.__wrap(__GLFWGamepadState.create(__int.valueOf(arg0)))

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
    def malloc(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.malloc(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'ByteBuffer', arg1: 'FloatBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.set(java.nio.ByteBuffer,java.nio.FloatBuffer)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).set(arg0, arg1))

    @overload
    def axes(self, arg0: 'FloatBuffer') -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.axes(java.nio.FloatBuffer)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).axes(arg0))

    @overload
    def axes(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState.axes()"""
        return 'FloatBuffer'.__wrap(super(GLFWGamepadState, self).axes())

    @staticmethod
    @overload
    def nbuttons(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,int,byte)"""
        __GLFWGamepadState.nbuttons(__long.valueOf(arg0), __int.valueOf(arg1), __byte.valueOf(arg2))

    @staticmethod
    @overload
    def naxes(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState.naxes(long)"""
        return FloatBuffer.__wrap(__GLFWGamepadState.naxes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nbuttons(arg0: int, arg1: int) -> int:
        """public static byte org.lwjgl.glfw.GLFWGamepadState.nbuttons(long,int)"""
        return int.__wrap(__GLFWGamepadState.nbuttons(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def callocStack(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.callocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.callocStack(arg0))

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
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.create(long,int)"""
        return Buffer.__wrap(__GLFWGamepadState.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def buttons(self, arg0: int) -> int:
        """public byte org.lwjgl.glfw.GLFWGamepadState.buttons(int)"""
        return int.__wrap(super(__GLFWGamepadState, self).buttons(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def mallocStack() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.mallocStack()"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.mallocStack())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.calloc(int)"""
        return Buffer.__wrap(__GLFWGamepadState.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.create()"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.create())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def callocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.callocStack(int)"""
        return Buffer.__wrap(__GLFWGamepadState.callocStack(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.createSafe(long,int)"""
        return Buffer.__wrap(__GLFWGamepadState.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def calloc() -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.calloc()"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.calloc())

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.malloc(int)"""
        return Buffer.__wrap(__GLFWGamepadState.malloc(__int.valueOf(arg0)))

    @overload
    def buttons(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState.buttons()"""
        return 'ByteBuffer'.__wrap(super(GLFWGamepadState, self).buttons())

    @staticmethod
    @overload
    def mallocStack(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.mallocStack(int)"""
        return Buffer.__wrap(__GLFWGamepadState.mallocStack(__int.valueOf(arg0)))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def mallocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.mallocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGamepadState.mallocStack(__int.valueOf(arg0), arg1))

    @overload
    def axes(self, arg0: int) -> float:
        """public float org.lwjgl.glfw.GLFWGamepadState.axes(int)"""
        return float.__wrap(super(__GLFWGamepadState, self).axes(__int.valueOf(arg0)))

    @overload
    def axes(self, arg0: int, arg1: float) -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.axes(int,float)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).axes(__int.valueOf(arg0), __float.valueOf(arg1)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.create(long)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.create(__long.valueOf(arg0)))

    @overload
    def buttons(self, arg0: int, arg1: int) -> 'GLFWGamepadState':
        """public org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.buttons(int,byte)"""
        return 'GLFWGamepadState'.__wrap(super(__GLFWGamepadState, self).buttons(__int.valueOf(arg0), __byte.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGamepadState.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWGamepadState.sizeof()"""
        return int.__wrap(super(GLFWGamepadState, self).sizeof())

    @staticmethod
    @overload
    def mallocStack(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.mallocStack(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.mallocStack(arg0))

    @override
    @overload
    def free(self):
        """public void org.lwjgl.system.Struct.free()"""
        super(pyglsystem.Struct, self).free()

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: int, arg2: float):
        """public static void org.lwjgl.glfw.GLFWGamepadState.naxes(long,int,float)"""
        __GLFWGamepadState.naxes(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))

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
    def callocStack(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState.callocStack(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWGamepadState.callocStack(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGamepadState(java.nio.ByteBuffer)"""
        val = __GLFWGamepadState(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWGamepadState':
        """public static org.lwjgl.glfw.GLFWGamepadState org.lwjgl.glfw.GLFWGamepadState.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWGamepadState.__wrap(__GLFWGamepadState.calloc(arg0))

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: int) -> float:
        """public static float org.lwjgl.glfw.GLFWGamepadState.naxes(long,int)"""
        return float.__wrap(__GLFWGamepadState.naxes(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def naxes(arg0: int, arg1: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFWGamepadState.naxes(long,java.nio.FloatBuffer)"""
        __GLFWGamepadState.naxes(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorPosCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWCursorPosCallbackI as __GLFWCursorPosCallbackI
__GLFWCursorPosCallbackI = __GLFWCursorPosCallbackI
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWCursorPosCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWCursorPosCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCursorPosCallbackI) -> 'GLFWCursorPosCallbackI':
        return GLFWCursorPosCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCursorPosCallbackI):
        """
        Dynamic initializer for GLFWCursorPosCallbackI.
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorPosCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCursorPosCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorPosCallbackI.callback(long,long)"""
        super(__GLFWCursorPosCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @abstractmethod
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWCursorPosCallbackI.invoke(long,double,double)"""
        pass

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWKeyCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWKeyCallbackI as __GLFWKeyCallbackI
__GLFWKeyCallbackI = __GLFWKeyCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWKeyCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWKeyCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWKeyCallbackI) -> 'GLFWKeyCallbackI':
        return GLFWKeyCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWKeyCallbackI):
        """
        Dynamic initializer for GLFWKeyCallbackI.
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
    def invoke(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public abstract void org.lwjgl.glfw.GLFWKeyCallbackI.invoke(long,int,int,int,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWKeyCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWKeyCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWKeyCallbackI.callback(long,long)"""
        super(__GLFWKeyCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWJoystickCallback
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.glfw.GLFWJoystickCallback as __GLFWJoystickCallback
__GLFWJoystickCallback = __GLFWJoystickCallback
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWJoystickCallbackI as __GLFWJoystickCallbackI
__GLFWJoystickCallbackI = __GLFWJoystickCallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWJoystickCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWJoystickCallbackI, GLFWJoystickCallbackI):
    """org.lwjgl.glfw.GLFWJoystickCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWJoystickCallback) -> 'GLFWJoystickCallback':
        return GLFWJoystickCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWJoystickCallback):
        """
        Dynamic initializer for GLFWJoystickCallback.
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
    def set(self) -> 'GLFWJoystickCallback':
        """public org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.set()"""
        return 'GLFWJoystickCallback'.__wrap(super(GLFWJoystickCallback, self).set())

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
    def create(arg0: 'GLFWJoystickCallbackI') -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.create(org.lwjgl.glfw.GLFWJoystickCallbackI)"""
        return GLFWJoystickCallback.__wrap(__GLFWJoystickCallback.create(arg0))

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.create(long)"""
        return GLFWJoystickCallback.__wrap(__GLFWJoystickCallback.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def free(arg0: int):
        """public static void org.lwjgl.system.Callback.free(long)"""
        __Callback.free(__long.valueOf(arg0))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWJoystickCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWJoystickCallbackI, self).getCallInterface())

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

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFWJoystickCallback.createSafe(long)"""
        return GLFWJoystickCallback.__wrap(__GLFWJoystickCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWJoystickCallbackI.callback(long,long)"""
        super(__GLFWJoystickCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGammaRamp$Buffer
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWGammaRamp as __GLFWGammaRamp_Buffer
__Buffer = __GLFWGammaRamp_Buffer.Buffer
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.nio.ShortBuffer as ShortBuffer
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
import java.nio.ShortBuffer as __ShortBuffer
__ShortBuffer = __ShortBuffer
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
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWGammaRamp.Buffer"""
 
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
    def blue(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.blue(java.nio.ShortBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).blue(arg0))

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
    def green(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.green(java.nio.ShortBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).green(arg0))

    @overload
    def red(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.red()"""
        return 'ShortBuffer'.__wrap(super(Buffer, self).red())

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

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer(java.nio.ByteBuffer)"""
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
    def green(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.green()"""
        return 'ShortBuffer'.__wrap(super(Buffer, self).green())

    @overload
    def blue(self) -> 'ShortBuffer':
        """public java.nio.ShortBuffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.blue()"""
        return 'ShortBuffer'.__wrap(super(Buffer, self).blue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def size(self) -> int:
        """public int org.lwjgl.glfw.GLFWGammaRamp$Buffer.size()"""
        return int.__wrap(super(Buffer, self).size())

    @overload
    def red(self, arg0: 'ShortBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.red(java.nio.ShortBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).red(arg0))

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
    def size(self, arg0: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer org.lwjgl.glfw.GLFWGammaRamp$Buffer.size(int)"""
        return 'Buffer'.__wrap(super(__Buffer, self).size(__int.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWGammaRamp$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
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
 
 
# CLASS: org.lwjgl.glfw.GLFWScrollCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWScrollCallbackI as __GLFWScrollCallbackI
__GLFWScrollCallbackI = __GLFWScrollCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWScrollCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWScrollCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWScrollCallbackI) -> 'GLFWScrollCallbackI':
        return GLFWScrollCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWScrollCallbackI):
        """
        Dynamic initializer for GLFWScrollCallbackI.
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
    def invoke(self, arg0: int, arg1: float, arg2: float):
        """public abstract void org.lwjgl.glfw.GLFWScrollCallbackI.invoke(long,double,double)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWScrollCallbackI.callback(long,long)"""
        super(__GLFWScrollCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWScrollCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWScrollCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFW
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWCharModsCallback as __GLFWCharModsCallback
__GLFWCharModsCallback = __GLFWCharModsCallback
import org.lwjgl.glfw.GLFWWindowMaximizeCallback as __GLFWWindowMaximizeCallback
__GLFWWindowMaximizeCallback = __GLFWWindowMaximizeCallback
import java.nio.IntBuffer as IntBuffer
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import org.lwjgl.glfw.GLFWWindowCloseCallback as __GLFWWindowCloseCallback
__GLFWWindowCloseCallback = __GLFWWindowCloseCallback
import org.lwjgl.glfw.GLFWWindowIconifyCallback as __GLFWWindowIconifyCallback
__GLFWWindowIconifyCallback = __GLFWWindowIconifyCallback
import org.lwjgl.glfw.GLFWFramebufferSizeCallback as __GLFWFramebufferSizeCallback
__GLFWFramebufferSizeCallback = __GLFWFramebufferSizeCallback
import java.lang.Class as __Class
__Class = __Class
import java.lang.Double as __double
from builtins import bool
import java.lang.CharSequence as CharSequence
import java.nio.DoubleBuffer as DoubleBuffer
import org.lwjgl.glfw.GLFWCursorEnterCallback as __GLFWCursorEnterCallback
__GLFWCursorEnterCallback = __GLFWCursorEnterCallback
import org.lwjgl.glfw.GLFWCharCallback as __GLFWCharCallback
__GLFWCharCallback = __GLFWCharCallback
from builtins import float
import org.lwjgl.glfw.GLFWErrorCallback as __GLFWErrorCallback
__GLFWErrorCallback = __GLFWErrorCallback
import org.lwjgl.glfw.GLFWDropCallback as __GLFWDropCallback
__GLFWDropCallback = __GLFWDropCallback
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

import org.lwjgl.glfw.GLFWWindowContentScaleCallback as __GLFWWindowContentScaleCallback
__GLFWWindowContentScaleCallback = __GLFWWindowContentScaleCallback
import org.lwjgl.glfw.GLFWKeyCallback as __GLFWKeyCallback
__GLFWKeyCallback = __GLFWKeyCallback
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import org.lwjgl.glfw.GLFWGammaRamp as __GLFWGammaRamp
__GLFWGammaRamp = __GLFWGammaRamp
import java.lang.Object as __Object
__Object = __Object
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
from builtins import int
import org.lwjgl.glfw.GLFWWindowPosCallback as __GLFWWindowPosCallback
__GLFWWindowPosCallback = __GLFWWindowPosCallback
import java.lang.Boolean as __boolean
import org.lwjgl.glfw.GLFWVidMode as __GLFWVidMode
__GLFWVidMode = __GLFWVidMode
from builtins import type
import java.nio.FloatBuffer as FloatBuffer
import org.lwjgl.glfw.GLFWWindowSizeCallback as __GLFWWindowSizeCallback
__GLFWWindowSizeCallback = __GLFWWindowSizeCallback
import org.lwjgl.glfw.GLFWWindowRefreshCallback as __GLFWWindowRefreshCallback
__GLFWWindowRefreshCallback = __GLFWWindowRefreshCallback
import org.lwjgl.glfw.GLFWVidMode as __GLFWVidMode_Buffer
__Buffer = __GLFWVidMode_Buffer.Buffer
import org.lwjgl.glfw.GLFWMonitorCallback as __GLFWMonitorCallback
__GLFWMonitorCallback = __GLFWMonitorCallback
import org.lwjgl.glfw.GLFWMouseButtonCallback as __GLFWMouseButtonCallback
__GLFWMouseButtonCallback = __GLFWMouseButtonCallback
import org.lwjgl.glfw.GLFWWindowFocusCallback as __GLFWWindowFocusCallback
__GLFWWindowFocusCallback = __GLFWWindowFocusCallback
import org.lwjgl.PointerBuffer as __PointerBuffer
__PointerBuffer = __PointerBuffer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

import org.lwjgl.glfw.GLFWScrollCallback as __GLFWScrollCallback
__GLFWScrollCallback = __GLFWScrollCallback
import org.lwjgl.glfw.GLFW as __GLFW
__GLFW = __GLFW
import org.lwjgl.glfw.GLFWCursorPosCallback as __GLFWCursorPosCallback
__GLFWCursorPosCallback = __GLFWCursorPosCallback
import org.lwjgl.system.SharedLibrary as __SharedLibrary
__SharedLibrary = __SharedLibrary
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWJoystickCallback as __GLFWJoystickCallback
__GLFWJoystickCallback = __GLFWJoystickCallback
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
 
class GLFW():
    """org.lwjgl.glfw.GLFW"""
 
    @staticmethod
    def __wrap(java_value: __GLFW) -> 'GLFW':
        return GLFW(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFW):
        """
        Dynamic initializer for GLFW.
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
    def glfwInit() -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwInit()"""
        return bool.__wrap(__GLFW.glfwInit())

    @staticmethod
    @overload
    def glfwGetProcAddress(arg0: 'ByteBuffer') -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetProcAddress(java.nio.ByteBuffer)"""
        return int.__wrap(__GLFW.glfwGetProcAddress(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nglfwUpdateGamepadMappings(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwUpdateGamepadMappings(long)"""
        return int.__wrap(__GLFW.nglfwUpdateGamepadMappings(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowCloseCallback(arg0: int, arg1: 'GLFWWindowCloseCallbackI') -> 'GLFWWindowCloseCallback':
        """public static org.lwjgl.glfw.GLFWWindowCloseCallback org.lwjgl.glfw.GLFW.glfwSetWindowCloseCallback(long,org.lwjgl.glfw.GLFWWindowCloseCallbackI)"""
        return GLFWWindowCloseCallback.__wrap(__GLFW.glfwSetWindowCloseCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwFocusWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwFocusWindow(long)"""
        __GLFW.glfwFocusWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwSetWindowSizeCallback(arg0: int, arg1: 'GLFWWindowSizeCallbackI') -> 'GLFWWindowSizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowSizeCallback org.lwjgl.glfw.GLFW.glfwSetWindowSizeCallback(long,org.lwjgl.glfw.GLFWWindowSizeCallbackI)"""
        return GLFWWindowSizeCallback.__wrap(__GLFW.glfwSetWindowSizeCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetCursorPosCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCursorPosCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetCursorPosCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetJoystickHats(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickHats(int,long)"""
        return int.__wrap(__GLFW.nglfwGetJoystickHats(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetScrollCallback(arg0: int, arg1: 'GLFWScrollCallbackI') -> 'GLFWScrollCallback':
        """public static org.lwjgl.glfw.GLFWScrollCallback org.lwjgl.glfw.GLFW.glfwSetScrollCallback(long,org.lwjgl.glfw.GLFWScrollCallbackI)"""
        return GLFWScrollCallback.__wrap(__GLFW.glfwSetScrollCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwExtensionSupported(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwExtensionSupported(long)"""
        return int.__wrap(__GLFW.nglfwExtensionSupported(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetJoystickGUID(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetJoystickGUID(int)"""
        return str.__wrap(__GLFW.glfwGetJoystickGUID(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwRequestWindowAttention(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwRequestWindowAttention(long)"""
        __GLFW.glfwRequestWindowAttention(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetFramebufferSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetFramebufferSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetFramebufferSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwExtensionSupported(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwExtensionSupported(java.nio.ByteBuffer)"""
        return bool.__wrap(__GLFW.glfwExtensionSupported(arg0))

    @staticmethod
    @overload
    def glfwGetWindowMonitor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetWindowMonitor(long)"""
        return int.__wrap(__GLFW.glfwGetWindowMonitor(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetTimerValue() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetTimerValue()"""
        return int.__wrap(__GLFW.glfwGetTimerValue())

    @staticmethod
    @overload
    def nglfwGetWindowContentScale(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowContentScale(long,long,long)"""
        __GLFW.nglfwGetWindowContentScale(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwSetWindowRefreshCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowRefreshCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowRefreshCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetWindowUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetWindowUserPointer(long)"""
        return int.__wrap(__GLFW.glfwGetWindowUserPointer(__long.valueOf(arg0)))

        @staticmethod
        @overload
        def glfwPollEvents():
            """public static void org.lwjgl.glfw.GLFW.glfwPollEvents()"""
            __GLFW.glfwPollEvents()

    @staticmethod
    @overload
    def glfwCreateWindow(arg0: int, arg1: int, arg2: 'CharSequence', arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateWindow(int,int,java.lang.CharSequence,long,long)"""
        return int.__wrap(__GLFW.glfwCreateWindow(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def nglfwGetJoystickButtons(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickButtons(int,long)"""
        return int.__wrap(__GLFW.nglfwGetJoystickButtons(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetCursorPos(arg0: int, arg1: 'DoubleBuffer', arg2: 'DoubleBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetCursorPos(long,java.nio.DoubleBuffer,java.nio.DoubleBuffer)"""
        __GLFW.glfwGetCursorPos(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetPrimaryMonitor() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetPrimaryMonitor()"""
        return int.__wrap(__GLFW.glfwGetPrimaryMonitor())

    @staticmethod
    @overload
    def nglfwSetWindowSizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowSizeCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowSizeCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetClipboardString(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetClipboardString(long,java.lang.CharSequence)"""
        __GLFW.glfwSetClipboardString(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSetMonitorUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetMonitorUserPointer(long,long)"""
        __GLFW.glfwSetMonitorUserPointer(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetWindowPos(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowPos(long,int[],int[])"""
        __GLFW.glfwGetWindowPos(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def nglfwCreateCursor(arg0: int, arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwCreateCursor(long,int,int)"""
        return int.__wrap(__GLFW.nglfwCreateCursor(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def glfwGetGamepadState(arg0: int, arg1: 'GLFWGamepadState') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwGetGamepadState(int,org.lwjgl.glfw.GLFWGamepadState)"""
        return bool.__wrap(__GLFW.glfwGetGamepadState(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetCursorPos(arg0: int, arg1: 'double', arg2: 'double'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetCursorPos(long,double[],double[])"""
        __GLFW.glfwGetCursorPos(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwHideWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwHideWindow(long)"""
        __GLFW.glfwHideWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwInitAllocator(arg0: 'GLFWAllocator'):
        """public static void org.lwjgl.glfw.GLFW.glfwInitAllocator(org.lwjgl.glfw.GLFWAllocator)"""
        __GLFW.glfwInitAllocator(arg0)

    @staticmethod
    @overload
    def glfwGetMonitorContentScale(arg0: int, arg1: 'float', arg2: 'float'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorContentScale(long,float[],float[])"""
        __GLFW.glfwGetMonitorContentScale(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetWindowPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowPos(long,int,int)"""
        __GLFW.glfwSetWindowPos(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetCharModsCallback(arg0: int, arg1: 'GLFWCharModsCallbackI') -> 'GLFWCharModsCallback':
        """public static org.lwjgl.glfw.GLFWCharModsCallback org.lwjgl.glfw.GLFW.glfwSetCharModsCallback(long,org.lwjgl.glfw.GLFWCharModsCallbackI)"""
        return GLFWCharModsCallback.__wrap(__GLFW.glfwSetCharModsCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetWindowTitle(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetWindowTitle(long,long)"""
        __GLFW.nglfwSetWindowTitle(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetWindowAttrib(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetWindowAttrib(long,int)"""
        return int.__wrap(__GLFW.glfwGetWindowAttrib(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwSetJoystickCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetJoystickCallback(long)"""
        return int.__wrap(__GLFW.nglfwSetJoystickCallback(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwWindowHintString(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHintString(int,java.nio.ByteBuffer)"""
        __GLFW.glfwWindowHintString(__int.valueOf(arg0), arg1)

        @staticmethod
        @overload
        def glfwPostEmptyEvent():
            """public static void org.lwjgl.glfw.GLFW.glfwPostEmptyEvent()"""
            __GLFW.glfwPostEmptyEvent()

    @staticmethod
    @overload
    def glfwSetCursorPos(arg0: int, arg1: float, arg2: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetCursorPos(long,double,double)"""
        __GLFW.glfwSetCursorPos(__long.valueOf(arg0), __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def glfwInitHint(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwInitHint(int,int)"""
        __GLFW.glfwInitHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetWindowFocusCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowFocusCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowFocusCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetInputMode(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetInputMode(long,int)"""
        return int.__wrap(__GLFW.glfwGetInputMode(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwIconifyWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwIconifyWindow(long)"""
        __GLFW.glfwIconifyWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetJoystickHats(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickHats(int)"""
        return ByteBuffer.__wrap(__GLFW.glfwGetJoystickHats(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetJoystickCallback(arg0: 'GLFWJoystickCallbackI') -> 'GLFWJoystickCallback':
        """public static org.lwjgl.glfw.GLFWJoystickCallback org.lwjgl.glfw.GLFW.glfwSetJoystickCallback(org.lwjgl.glfw.GLFWJoystickCallbackI)"""
        return GLFWJoystickCallback.__wrap(__GLFW.glfwSetJoystickCallback(arg0))

    @staticmethod
    @overload
    def glfwGetMonitorContentScale(arg0: int, arg1: 'FloatBuffer', arg2: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorContentScale(long,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        __GLFW.glfwGetMonitorContentScale(__long.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwCreateCursor(arg0: 'GLFWImage', arg1: int, arg2: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateCursor(org.lwjgl.glfw.GLFWImage,int,int)"""
        return int.__wrap(__GLFW.glfwCreateCursor(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @staticmethod
    @overload
    def glfwGetVideoModes(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWVidMode$Buffer org.lwjgl.glfw.GLFW.glfwGetVideoModes(long)"""
        return Buffer.__wrap(__GLFW.glfwGetVideoModes(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def getLibrary() -> 'pyglsystem.SharedLibrary':
        """public static org.lwjgl.system.SharedLibrary org.lwjgl.glfw.GLFW.getLibrary()"""
        return pyglsystem.SharedLibrary.__wrap(__GLFW.getLibrary())

    @staticmethod
    @overload
    def nglfwGetGamepadName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetGamepadName(int)"""
        return int.__wrap(__GLFW.nglfwGetGamepadName(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetInputMode(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetInputMode(long,int,int)"""
        __GLFW.glfwSetInputMode(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

        @staticmethod
        @overload
        def glfwTerminate():
            """public static void org.lwjgl.glfw.GLFW.glfwTerminate()"""
            __GLFW.glfwTerminate()

    @staticmethod
    @overload
    def nglfwGetMonitorPhysicalSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorPhysicalSize(long,long,long)"""
        __GLFW.nglfwGetMonitorPhysicalSize(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwGetJoystickName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickName(int)"""
        return int.__wrap(__GLFW.nglfwGetJoystickName(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwInitAllocator(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwInitAllocator(long)"""
        __GLFW.nglfwInitAllocator(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwJoystickPresent(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwJoystickPresent(int)"""
        return bool.__wrap(__GLFW.glfwJoystickPresent(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetMonitorWorkarea(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorWorkarea(long,int[],int[],int[],int[])"""
        __GLFW.glfwGetMonitorWorkarea(__long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwGetMonitors() -> 'pygl.PointerBuffer':
        """public static org.lwjgl.PointerBuffer org.lwjgl.glfw.GLFW.glfwGetMonitors()"""
        return pygl.PointerBuffer.__wrap(__GLFW.glfwGetMonitors())

    @staticmethod
    @overload
    def glfwGetClipboardString(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetClipboardString(long)"""
        return str.__wrap(__GLFW.glfwGetClipboardString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetCursorEnterCallback(arg0: int, arg1: 'GLFWCursorEnterCallbackI') -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFW.glfwSetCursorEnterCallback(long,org.lwjgl.glfw.GLFWCursorEnterCallbackI)"""
        return GLFWCursorEnterCallback.__wrap(__GLFW.glfwSetCursorEnterCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwJoystickIsGamepad(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwJoystickIsGamepad(int)"""
        return bool.__wrap(__GLFW.glfwJoystickIsGamepad(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWindowFrameSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowFrameSize(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetWindowFrameSize(__long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def nglfwGetError(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwGetError(long)"""
        return int.__wrap(__GLFW.nglfwGetError(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetFramebufferSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetFramebufferSize(long,long,long)"""
        __GLFW.nglfwGetFramebufferSize(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwGetVersionString() -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVersionString()"""
        return int.__wrap(__GLFW.nglfwGetVersionString())

    @staticmethod
    @overload
    def glfwGetWindowContentScale(arg0: int, arg1: 'float', arg2: 'float'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowContentScale(long,float[],float[])"""
        __GLFW.glfwGetWindowContentScale(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetGamepadName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetGamepadName(int)"""
        return str.__wrap(__GLFW.glfwGetGamepadName(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWindowPos(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowPos(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetWindowPos(__long.valueOf(arg0), arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nglfwSetWindowPosCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowPosCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowPosCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetWindowSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowSize(long,long,long)"""
        __GLFW.nglfwGetWindowSize(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetJoystickButtons(arg0: int) -> 'ByteBuffer':
        """public static java.nio.ByteBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickButtons(int)"""
        return ByteBuffer.__wrap(__GLFW.glfwGetJoystickButtons(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwWindowShouldClose(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwWindowShouldClose(long)"""
        return bool.__wrap(__GLFW.glfwWindowShouldClose(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetMonitors(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetMonitors(long)"""
        return int.__wrap(__GLFW.nglfwGetMonitors(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwCreateWindow(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwCreateWindow(int,int,long,long,long)"""
        return int.__wrap(__GLFW.nglfwCreateWindow(__int.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def nglfwSetClipboardString(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetClipboardString(long,long)"""
        __GLFW.nglfwSetClipboardString(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetMonitorWorkarea(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorWorkarea(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetMonitorWorkarea(__long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwGetProcAddress(arg0: 'CharSequence') -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetProcAddress(java.lang.CharSequence)"""
        return int.__wrap(__GLFW.glfwGetProcAddress(arg0))

    @staticmethod
    @overload
    def glfwSetWindowAspectRatio(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowAspectRatio(long,int,int)"""
        __GLFW.glfwSetWindowAspectRatio(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwGetJoystickAxes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickAxes(int,long)"""
        return int.__wrap(__GLFW.nglfwGetJoystickAxes(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetVideoMode(arg0: int) -> 'GLFWVidMode':
        """public static org.lwjgl.glfw.GLFWVidMode org.lwjgl.glfw.GLFW.glfwGetVideoMode(long)"""
        return GLFWVidMode.__wrap(__GLFW.glfwGetVideoMode(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetCharModsCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCharModsCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetCharModsCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwDestroyCursor(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwDestroyCursor(long)"""
        __GLFW.glfwDestroyCursor(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwRawMouseMotionSupported() -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwRawMouseMotionSupported()"""
        return bool.__wrap(__GLFW.glfwRawMouseMotionSupported())

    @staticmethod
    @overload
    def nglfwSetErrorCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetErrorCallback(long)"""
        return int.__wrap(__GLFW.nglfwSetErrorCallback(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowFocusCallback(arg0: int, arg1: 'GLFWWindowFocusCallbackI') -> 'GLFWWindowFocusCallback':
        """public static org.lwjgl.glfw.GLFWWindowFocusCallback org.lwjgl.glfw.GLFW.glfwSetWindowFocusCallback(long,org.lwjgl.glfw.GLFWWindowFocusCallbackI)"""
        return GLFWWindowFocusCallback.__wrap(__GLFW.glfwSetWindowFocusCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetTime() -> float:
        """public static double org.lwjgl.glfw.GLFW.glfwGetTime()"""
        return float.__wrap(__GLFW.glfwGetTime())

    @staticmethod
    @overload
    def nglfwGetWindowFrameSize(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowFrameSize(long,long,long,long,long)"""
        __GLFW.nglfwGetWindowFrameSize(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def nglfwGetVideoMode(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVideoMode(long)"""
        return int.__wrap(__GLFW.nglfwGetVideoMode(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetMouseButtonCallback(arg0: int, arg1: 'GLFWMouseButtonCallbackI') -> 'GLFWMouseButtonCallback':
        """public static org.lwjgl.glfw.GLFWMouseButtonCallback org.lwjgl.glfw.GLFW.glfwSetMouseButtonCallback(long,org.lwjgl.glfw.GLFWMouseButtonCallbackI)"""
        return GLFWMouseButtonCallback.__wrap(__GLFW.glfwSetMouseButtonCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetMonitorPhysicalSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPhysicalSize(long,int[],int[])"""
        __GLFW.glfwGetMonitorPhysicalSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetWindowFrameSize(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowFrameSize(long,int[],int[],int[],int[])"""
        __GLFW.glfwGetWindowFrameSize(__long.valueOf(arg0), arg1, arg2, arg3, arg4)

    @staticmethod
    @overload
    def glfwSetWindowPosCallback(arg0: int, arg1: 'GLFWWindowPosCallbackI') -> 'GLFWWindowPosCallback':
        """public static org.lwjgl.glfw.GLFWWindowPosCallback org.lwjgl.glfw.GLFW.glfwSetWindowPosCallback(long,org.lwjgl.glfw.GLFWWindowPosCallbackI)"""
        return GLFWWindowPosCallback.__wrap(__GLFW.glfwSetWindowPosCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwGetKeyName(arg0: int, arg1: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetKeyName(int,int)"""
        return str.__wrap(__GLFW.glfwGetKeyName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowIcon(arg0: int, arg1: 'Buffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowIcon(long,org.lwjgl.glfw.GLFWImage$Buffer)"""
        __GLFW.glfwSetWindowIcon(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSetWindowUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowUserPointer(long,long)"""
        __GLFW.glfwSetWindowUserPointer(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetWindowShouldClose(arg0: int, arg1: bool):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowShouldClose(long,boolean)"""
        __GLFW.glfwSetWindowShouldClose(__long.valueOf(arg0), __boolean.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwWindowHintString(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwWindowHintString(int,long)"""
        __GLFW.nglfwWindowHintString(__int.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetWindowTitle(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowTitle(long,java.nio.ByteBuffer)"""
        __GLFW.glfwSetWindowTitle(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def nglfwGetVideoModes(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetVideoModes(long,long)"""
        return int.__wrap(__GLFW.nglfwGetVideoModes(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwWindowHintString(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHintString(int,java.lang.CharSequence)"""
        __GLFW.glfwWindowHintString(__int.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwGetMouseButton(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetMouseButton(long,int)"""
        return int.__wrap(__GLFW.glfwGetMouseButton(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowMonitor(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowMonitor(long,long,int,int,int,int,int)"""
        __GLFW.glfwSetWindowMonitor(__long.valueOf(arg0), __long.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @staticmethod
    @overload
    def glfwSetWindowSize(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowSize(long,int,int)"""
        __GLFW.glfwSetWindowSize(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwSetFramebufferSizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetFramebufferSizeCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetFramebufferSizeCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSwapBuffers(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSwapBuffers(long)"""
        __GLFW.glfwSwapBuffers(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwExtensionSupported(arg0: 'CharSequence') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwExtensionSupported(java.lang.CharSequence)"""
        return bool.__wrap(__GLFW.glfwExtensionSupported(arg0))

    @staticmethod
    @overload
    def nglfwGetKeyName(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetKeyName(int,int)"""
        return int.__wrap(__GLFW.nglfwGetKeyName(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwDestroyWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwDestroyWindow(long)"""
        __GLFW.glfwDestroyWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nglfwGetJoystickGUID(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetJoystickGUID(int)"""
        return int.__wrap(__GLFW.nglfwGetJoystickGUID(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwPlatformSupported(arg0: int) -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwPlatformSupported(int)"""
        return bool.__wrap(__GLFW.glfwPlatformSupported(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetMonitorName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetMonitorName(long)"""
        return str.__wrap(__GLFW.glfwGetMonitorName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetMonitorName(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetMonitorName(long)"""
        return int.__wrap(__GLFW.nglfwGetMonitorName(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetVersion(arg0: 'IntBuffer', arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetVersion(java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetVersion(arg0, arg1, arg2)

    @staticmethod
    @overload
    def glfwGetGammaRamp(arg0: int) -> 'GLFWGammaRamp':
        """public static org.lwjgl.glfw.GLFWGammaRamp org.lwjgl.glfw.GLFW.glfwGetGammaRamp(long)"""
        return GLFWGammaRamp.__wrap(__GLFW.glfwGetGammaRamp(__long.valueOf(arg0)))

        @staticmethod
        @overload
        def glfwDefaultWindowHints():
            """public static void org.lwjgl.glfw.GLFW.glfwDefaultWindowHints()"""
            __GLFW.glfwDefaultWindowHints()

    @staticmethod
    @overload
    def glfwSetCursorPosCallback(arg0: int, arg1: 'GLFWCursorPosCallbackI') -> 'GLFWCursorPosCallback':
        """public static org.lwjgl.glfw.GLFWCursorPosCallback org.lwjgl.glfw.GLFW.glfwSetCursorPosCallback(long,org.lwjgl.glfw.GLFWCursorPosCallbackI)"""
        return GLFWCursorPosCallback.__wrap(__GLFW.glfwSetCursorPosCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetMonitorCallback(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetMonitorCallback(long)"""
        return int.__wrap(__GLFW.nglfwSetMonitorCallback(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetWindowSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowSize(long,int[],int[])"""
        __GLFW.glfwGetWindowSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetJoystickUserPointer(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetJoystickUserPointer(int,long)"""
        __GLFW.glfwSetJoystickUserPointer(__int.valueOf(arg0), __long.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def nglfwGetWindowPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetWindowPos(long,long,long)"""
        __GLFW.nglfwGetWindowPos(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetError(arg0: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetError(org.lwjgl.PointerBuffer)"""
        return int.__wrap(__GLFW.glfwGetError(arg0))

    @staticmethod
    @overload
    def glfwMakeContextCurrent(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwMakeContextCurrent(long)"""
        __GLFW.glfwMakeContextCurrent(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetJoystickUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetJoystickUserPointer(int)"""
        return int.__wrap(__GLFW.glfwGetJoystickUserPointer(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetKey(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetKey(long,int)"""
        return int.__wrap(__GLFW.glfwGetKey(__long.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetKeyScancode(arg0: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetKeyScancode(int)"""
        return int.__wrap(__GLFW.glfwGetKeyScancode(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetCursorPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetCursorPos(long,long,long)"""
        __GLFW.nglfwGetCursorPos(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

        @staticmethod
        @overload
        def glfwWaitEvents():
            """public static void org.lwjgl.glfw.GLFW.glfwWaitEvents()"""
            __GLFW.glfwWaitEvents()

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
    def glfwGetMonitorUserPointer(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetMonitorUserPointer(long)"""
        return int.__wrap(__GLFW.glfwGetMonitorUserPointer(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetWindowIconifyCallback(arg0: int, arg1: 'GLFWWindowIconifyCallbackI') -> 'GLFWWindowIconifyCallback':
        """public static org.lwjgl.glfw.GLFWWindowIconifyCallback org.lwjgl.glfw.GLFW.glfwSetWindowIconifyCallback(long,org.lwjgl.glfw.GLFWWindowIconifyCallbackI)"""
        return GLFWWindowIconifyCallback.__wrap(__GLFW.glfwSetWindowIconifyCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetWindowIcon(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetWindowIcon(long,int,long)"""
        __GLFW.nglfwSetWindowIcon(__long.valueOf(arg0), __int.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetCurrentContext() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetCurrentContext()"""
        return int.__wrap(__GLFW.glfwGetCurrentContext())

    @staticmethod
    @overload
    def glfwGetVersion(arg0: 'int', arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetVersion(int[],int[],int[])"""
        __GLFW.glfwGetVersion(arg0, arg1, arg2)

    @staticmethod
    @overload
    def nglfwSetGammaRamp(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwSetGammaRamp(long,long)"""
        __GLFW.nglfwSetGammaRamp(__long.valueOf(arg0), __long.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetWindowContentScaleCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowContentScaleCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowContentScaleCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetCharCallback(arg0: int, arg1: 'GLFWCharCallbackI') -> 'GLFWCharCallback':
        """public static org.lwjgl.glfw.GLFWCharCallback org.lwjgl.glfw.GLFW.glfwSetCharCallback(long,org.lwjgl.glfw.GLFWCharCallbackI)"""
        return GLFWCharCallback.__wrap(__GLFW.glfwSetCharCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwSetDropCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetDropCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetDropCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwSetWindowMaximizeCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowMaximizeCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowMaximizeCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetWindowSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetWindowSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetDropCallback(arg0: int, arg1: 'GLFWDropCallbackI') -> 'GLFWDropCallback':
        """public static org.lwjgl.glfw.GLFWDropCallback org.lwjgl.glfw.GLFW.glfwSetDropCallback(long,org.lwjgl.glfw.GLFWDropCallbackI)"""
        return GLFWDropCallback.__wrap(__GLFW.glfwSetDropCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwGetGamepadState(arg0: int, arg1: int) -> int:
        """public static int org.lwjgl.glfw.GLFW.nglfwGetGamepadState(int,long)"""
        return int.__wrap(__GLFW.nglfwGetGamepadState(__int.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowSizeLimits(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowSizeLimits(long,int,int,int,int)"""
        __GLFW.glfwSetWindowSizeLimits(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @staticmethod
    @overload
    def nglfwSetWindowCloseCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowCloseCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowCloseCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwGetVersionString() -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetVersionString()"""
        return str.__wrap(__GLFW.glfwGetVersionString())

    @staticmethod
    @overload
    def nglfwSetScrollCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetScrollCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetScrollCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetGammaRamp(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetGammaRamp(long)"""
        return int.__wrap(__GLFW.nglfwGetGammaRamp(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetGammaRamp(arg0: int, arg1: 'GLFWGammaRamp'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetGammaRamp(long,org.lwjgl.glfw.GLFWGammaRamp)"""
        __GLFW.glfwSetGammaRamp(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwShowWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwShowWindow(long)"""
        __GLFW.glfwShowWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwSetClipboardString(arg0: int, arg1: 'ByteBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetClipboardString(long,java.nio.ByteBuffer)"""
        __GLFW.glfwSetClipboardString(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSwapInterval(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSwapInterval(int)"""
        __GLFW.glfwSwapInterval(__int.valueOf(arg0))

    @staticmethod
    @overload
    def glfwGetWindowOpacity(arg0: int) -> float:
        """public static float org.lwjgl.glfw.GLFW.glfwGetWindowOpacity(long)"""
        return float.__wrap(__GLFW.glfwGetWindowOpacity(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetWindowIconifyCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetWindowIconifyCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetWindowIconifyCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetWindowAttrib(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowAttrib(long,int,int)"""
        __GLFW.glfwSetWindowAttrib(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @staticmethod
    @overload
    def glfwGetPlatform() -> int:
        """public static int org.lwjgl.glfw.GLFW.glfwGetPlatform()"""
        return int.__wrap(__GLFW.glfwGetPlatform())

    @staticmethod
    @overload
    def nglfwSetCharCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCharCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetCharCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetMonitorWorkarea(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorWorkarea(long,long,long,long,long)"""
        __GLFW.nglfwGetMonitorWorkarea(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4))

    @staticmethod
    @overload
    def nglfwGetMonitorPos(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorPos(long,long,long)"""
        __GLFW.nglfwGetMonitorPos(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwSetWindowContentScaleCallback(arg0: int, arg1: 'GLFWWindowContentScaleCallbackI') -> 'GLFWWindowContentScaleCallback':
        """public static org.lwjgl.glfw.GLFWWindowContentScaleCallback org.lwjgl.glfw.GLFW.glfwSetWindowContentScaleCallback(long,org.lwjgl.glfw.GLFWWindowContentScaleCallbackI)"""
        return GLFWWindowContentScaleCallback.__wrap(__GLFW.glfwSetWindowContentScaleCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nglfwGetVersion(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetVersion(long,long,long)"""
        __GLFW.nglfwGetVersion(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def glfwWindowHint(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwWindowHint(int,int)"""
        __GLFW.glfwWindowHint(__int.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def nglfwSetKeyCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetKeyCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetKeyCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwSetTime(arg0: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetTime(double)"""
        __GLFW.glfwSetTime(__double.valueOf(arg0))

    @staticmethod
    @overload
    def glfwRestoreWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwRestoreWindow(long)"""
        __GLFW.glfwRestoreWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwSetWindowTitle(arg0: int, arg1: 'CharSequence'):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowTitle(long,java.lang.CharSequence)"""
        __GLFW.glfwSetWindowTitle(__long.valueOf(arg0), arg1)

    @staticmethod
    @overload
    def glfwSetErrorCallback(arg0: 'GLFWErrorCallbackI') -> 'GLFWErrorCallback':
        """public static org.lwjgl.glfw.GLFWErrorCallback org.lwjgl.glfw.GLFW.glfwSetErrorCallback(org.lwjgl.glfw.GLFWErrorCallbackI)"""
        return GLFWErrorCallback.__wrap(__GLFW.glfwSetErrorCallback(arg0))

    @staticmethod
    @overload
    def glfwGetMonitorPos(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPos(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetMonitorPos(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetWindowMaximizeCallback(arg0: int, arg1: 'GLFWWindowMaximizeCallbackI') -> 'GLFWWindowMaximizeCallback':
        """public static org.lwjgl.glfw.GLFWWindowMaximizeCallback org.lwjgl.glfw.GLFW.glfwSetWindowMaximizeCallback(long,org.lwjgl.glfw.GLFWWindowMaximizeCallbackI)"""
        return GLFWWindowMaximizeCallback.__wrap(__GLFW.glfwSetWindowMaximizeCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwCreateStandardCursor(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateStandardCursor(int)"""
        return int.__wrap(__GLFW.glfwCreateStandardCursor(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwGetMonitorContentScale(arg0: int, arg1: int, arg2: int):
        """public static void org.lwjgl.glfw.GLFW.nglfwGetMonitorContentScale(long,long,long)"""
        __GLFW.nglfwGetMonitorContentScale(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2))

    @staticmethod
    @overload
    def nglfwSetCursorEnterCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetCursorEnterCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetCursorEnterCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def glfwWaitEventsTimeout(arg0: float):
        """public static void org.lwjgl.glfw.GLFW.glfwWaitEventsTimeout(double)"""
        __GLFW.glfwWaitEventsTimeout(__double.valueOf(arg0))

    @staticmethod
    @overload
    def glfwSetFramebufferSizeCallback(arg0: int, arg1: 'GLFWFramebufferSizeCallbackI') -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFW.glfwSetFramebufferSizeCallback(long,org.lwjgl.glfw.GLFWFramebufferSizeCallbackI)"""
        return GLFWFramebufferSizeCallback.__wrap(__GLFW.glfwSetFramebufferSizeCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetMonitorCallback(arg0: 'GLFWMonitorCallbackI') -> 'GLFWMonitorCallback':
        """public static org.lwjgl.glfw.GLFWMonitorCallback org.lwjgl.glfw.GLFW.glfwSetMonitorCallback(org.lwjgl.glfw.GLFWMonitorCallbackI)"""
        return GLFWMonitorCallback.__wrap(__GLFW.glfwSetMonitorCallback(arg0))

    @staticmethod
    @overload
    def glfwGetWindowContentScale(arg0: int, arg1: 'FloatBuffer', arg2: 'FloatBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetWindowContentScale(long,java.nio.FloatBuffer,java.nio.FloatBuffer)"""
        __GLFW.glfwGetWindowContentScale(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetTimerFrequency() -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwGetTimerFrequency()"""
        return int.__wrap(__GLFW.glfwGetTimerFrequency())

    @staticmethod
    @overload
    def glfwGetFramebufferSize(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetFramebufferSize(long,int[],int[])"""
        __GLFW.glfwGetFramebufferSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwGetMonitorPos(arg0: int, arg1: 'int', arg2: 'int'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPos(long,int[],int[])"""
        __GLFW.glfwGetMonitorPos(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetGamma(arg0: int, arg1: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetGamma(long,float)"""
        __GLFW.glfwSetGamma(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def glfwCreateWindow(arg0: int, arg1: int, arg2: 'ByteBuffer', arg3: int, arg4: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.glfwCreateWindow(int,int,java.nio.ByteBuffer,long,long)"""
        return int.__wrap(__GLFW.glfwCreateWindow(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __long.valueOf(arg3), __long.valueOf(arg4)))

    @staticmethod
    @overload
    def glfwGetJoystickAxes(arg0: int) -> 'FloatBuffer':
        """public static java.nio.FloatBuffer org.lwjgl.glfw.GLFW.glfwGetJoystickAxes(int)"""
        return FloatBuffer.__wrap(__GLFW.glfwGetJoystickAxes(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwGetJoystickName(arg0: int) -> str:
        """public static java.lang.String org.lwjgl.glfw.GLFW.glfwGetJoystickName(int)"""
        return str.__wrap(__GLFW.glfwGetJoystickName(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwMaximizeWindow(arg0: int):
        """public static void org.lwjgl.glfw.GLFW.glfwMaximizeWindow(long)"""
        __GLFW.glfwMaximizeWindow(__long.valueOf(arg0))

    @staticmethod
    @overload
    def glfwUpdateGamepadMappings(arg0: 'ByteBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFW.glfwUpdateGamepadMappings(java.nio.ByteBuffer)"""
        return bool.__wrap(__GLFW.glfwUpdateGamepadMappings(arg0))

    @staticmethod
    @overload
    def glfwGetMonitorPhysicalSize(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer'):
        """public static void org.lwjgl.glfw.GLFW.glfwGetMonitorPhysicalSize(long,java.nio.IntBuffer,java.nio.IntBuffer)"""
        __GLFW.glfwGetMonitorPhysicalSize(__long.valueOf(arg0), arg1, arg2)

    @staticmethod
    @overload
    def glfwSetWindowRefreshCallback(arg0: int, arg1: 'GLFWWindowRefreshCallbackI') -> 'GLFWWindowRefreshCallback':
        """public static org.lwjgl.glfw.GLFWWindowRefreshCallback org.lwjgl.glfw.GLFW.glfwSetWindowRefreshCallback(long,org.lwjgl.glfw.GLFWWindowRefreshCallbackI)"""
        return GLFWWindowRefreshCallback.__wrap(__GLFW.glfwSetWindowRefreshCallback(__long.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def nglfwGetClipboardString(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetClipboardString(long)"""
        return int.__wrap(__GLFW.nglfwGetClipboardString(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def nglfwSetMouseButtonCallback(arg0: int, arg1: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwSetMouseButtonCallback(long,long)"""
        return int.__wrap(__GLFW.nglfwSetMouseButtonCallback(__long.valueOf(arg0), __long.valueOf(arg1)))

    @staticmethod
    @overload
    def nglfwGetProcAddress(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFW.nglfwGetProcAddress(long)"""
        return int.__wrap(__GLFW.nglfwGetProcAddress(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def glfwSetKeyCallback(arg0: int, arg1: 'GLFWKeyCallbackI') -> 'GLFWKeyCallback':
        """public static org.lwjgl.glfw.GLFWKeyCallback org.lwjgl.glfw.GLFW.glfwSetKeyCallback(long,org.lwjgl.glfw.GLFWKeyCallbackI)"""
        return GLFWKeyCallback.__wrap(__GLFW.glfwSetKeyCallback(__long.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def glfwSetWindowOpacity(arg0: int, arg1: float):
        """public static void org.lwjgl.glfw.GLFW.glfwSetWindowOpacity(long,float)"""
        __GLFW.glfwSetWindowOpacity(__long.valueOf(arg0), __float.valueOf(arg1))

    @staticmethod
    @overload
    def glfwSetCursor(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFW.glfwSetCursor(long,long)"""
        __GLFW.glfwSetCursor(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWCharModsCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWCharModsCallbackI as __GLFWCharModsCallbackI
__GLFWCharModsCallbackI = __GLFWCharModsCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWCharModsCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWCharModsCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCharModsCallbackI) -> 'GLFWCharModsCallbackI':
        return GLFWCharModsCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCharModsCallbackI):
        """
        Dynamic initializer for GLFWCharModsCallbackI.
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
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCharModsCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCharModsCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCharModsCallbackI.callback(long,long)"""
        super(__GLFWCharModsCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address())

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWCharModsCallbackI.invoke(long,int,int)"""
        pass 
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorEnterCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.Callback as __Callback
__Callback = __Callback
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import org.lwjgl.glfw.GLFWCursorEnterCallback as __GLFWCursorEnterCallback
__GLFWCursorEnterCallback = __GLFWCursorEnterCallback
from builtins import type
import org.lwjgl.system.NativeResource as __NativeResource
__NativeResource = __NativeResource
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
import org.lwjgl.glfw.GLFWCursorEnterCallbackI as __GLFWCursorEnterCallbackI
__GLFWCursorEnterCallbackI = __GLFWCursorEnterCallbackI
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GLFWCursorEnterCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWCursorEnterCallbackI, GLFWCursorEnterCallbackI):
    """org.lwjgl.glfw.GLFWCursorEnterCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCursorEnterCallback) -> 'GLFWCursorEnterCallback':
        return GLFWCursorEnterCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCursorEnterCallback):
        """
        Dynamic initializer for GLFWCursorEnterCallback.
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
    def create(arg0: int) -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.create(long)"""
        return GLFWCursorEnterCallback.__wrap(__GLFWCursorEnterCallback.create(__long.valueOf(arg0)))

    @overload
    def set(self, arg0: int) -> 'GLFWCursorEnterCallback':
        """public org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.set(long)"""
        return 'GLFWCursorEnterCallback'.__wrap(super(__GLFWCursorEnterCallback, self).set(__long.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.lwjgl.system.Callback.hashCode()"""
        return int.__wrap(super(pyglsystem.Callback, self).hashCode())

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
    def create(arg0: 'GLFWCursorEnterCallbackI') -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.create(org.lwjgl.glfw.GLFWCursorEnterCallbackI)"""
        return GLFWCursorEnterCallback.__wrap(__GLFWCursorEnterCallback.create(arg0))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWCursorEnterCallback':
        """public static org.lwjgl.glfw.GLFWCursorEnterCallback org.lwjgl.glfw.GLFWCursorEnterCallback.createSafe(long)"""
        return GLFWCursorEnterCallback.__wrap(__GLFWCursorEnterCallback.createSafe(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWCursorEnterCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorEnterCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCursorEnterCallbackI, self).getCallInterface())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorEnterCallbackI.callback(long,long)"""
        super(__GLFWCursorEnterCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWMonitorCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWMonitorCallbackI as __GLFWMonitorCallbackI
__GLFWMonitorCallbackI = __GLFWMonitorCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWMonitorCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWMonitorCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWMonitorCallbackI) -> 'GLFWMonitorCallbackI':
        return GLFWMonitorCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWMonitorCallbackI):
        """
        Dynamic initializer for GLFWMonitorCallbackI.
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
    def invoke(self, arg0: int, arg1: int):
        """public abstract void org.lwjgl.glfw.GLFWMonitorCallbackI.invoke(long,int)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWMonitorCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWMonitorCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWMonitorCallbackI.callback(long,long)"""
        super(__GLFWMonitorCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWVidMode$Buffer
from pyquantum_helper import import_once as __import_once__
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import org.lwjgl.system.StructBuffer as __StructBuffer
__StructBuffer = __StructBuffer
import java.util.function.Consumer as Consumer
import org.lwjgl.glfw.GLFWVidMode as __GLFWVidMode_Buffer
__Buffer = __GLFWVidMode_Buffer.Buffer
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
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer):
    """org.lwjgl.glfw.GLFWVidMode.Buffer"""
 
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
    def width(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.width()"""
        return int.__wrap(super(Buffer, self).width())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def redBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.redBits()"""
        return int.__wrap(super(Buffer, self).redBits())

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
    def height(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.height()"""
        return int.__wrap(super(Buffer, self).height())

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
        """public org.lwjgl.glfw.GLFWVidMode$Buffer(java.nio.ByteBuffer)"""
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
    def refreshRate(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.refreshRate()"""
        return int.__wrap(super(Buffer, self).refreshRate())

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
    def greenBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.greenBits()"""
        return int.__wrap(super(Buffer, self).greenBits())

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWVidMode$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def blueBits(self) -> int:
        """public int org.lwjgl.glfw.GLFWVidMode$Buffer.blueBits()"""
        return int.__wrap(super(Buffer, self).blueBits())

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
 
 
# CLASS: org.lwjgl.glfw.GLFWVulkan$Functions
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
import org.lwjgl.glfw.GLFWVulkan as __GLFWVulkan_Functions
__Functions = __GLFWVulkan_Functions.Functions
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWVulkan.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWCursorEnterCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.glfw.GLFWCursorEnterCallbackI as __GLFWCursorEnterCallbackI
__GLFWCursorEnterCallbackI = __GLFWCursorEnterCallbackI
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWCursorEnterCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWCursorEnterCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWCursorEnterCallbackI) -> 'GLFWCursorEnterCallbackI':
        return GLFWCursorEnterCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWCursorEnterCallbackI):
        """
        Dynamic initializer for GLFWCursorEnterCallbackI.
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
    def invoke(self, arg0: int, arg1: bool):
        """public abstract void org.lwjgl.glfw.GLFWCursorEnterCallbackI.invoke(long,boolean)"""
        pass

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWCursorEnterCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWCursorEnterCallbackI, self).getCallInterface())

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWCursorEnterCallbackI.callback(long,long)"""
        super(__GLFWCursorEnterCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeOSMesa$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.glfw.GLFWNativeOSMesa as __GLFWNativeOSMesa_Functions
__Functions = __GLFWNativeOSMesa_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeOSMesa.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWWindowCloseCallbackI
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import java.lang.Long as __long
import org.lwjgl.system.CallbackI as __CallbackI
__CallbackI = __CallbackI
import org.lwjgl.glfw.GLFWWindowCloseCallbackI as __GLFWWindowCloseCallbackI
__GLFWWindowCloseCallbackI = __GLFWWindowCloseCallbackI
from abc import abstractmethod, ABC
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

from builtins import int
 
class GLFWWindowCloseCallbackI(ABC, pyglsystem.__CallbackI, pyglsystem.CallbackI):
    """org.lwjgl.glfw.GLFWWindowCloseCallbackI"""
 
    @staticmethod
    def __wrap(java_value: __GLFWWindowCloseCallbackI) -> 'GLFWWindowCloseCallbackI':
        return GLFWWindowCloseCallbackI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWWindowCloseCallbackI):
        """
        Dynamic initializer for GLFWWindowCloseCallbackI.
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
    def invoke(self, arg0: int):
        """public abstract void org.lwjgl.glfw.GLFWWindowCloseCallbackI.invoke(long)"""
        pass

    @override
    @overload
    def callback(self, arg0: int, arg1: int):
        """public default void org.lwjgl.glfw.GLFWWindowCloseCallbackI.callback(long,long)"""
        super(__GLFWWindowCloseCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWWindowCloseCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWWindowCloseCallbackI, self).getCallInterface())

    @override
    @overload
    def address(self) -> int:
        """public default long org.lwjgl.system.CallbackI.address()"""
        return int.__wrap(super(pyglsystem.CallbackI, self).address()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWFramebufferSizeCallback
from pyquantum_helper import import_once as __import_once__
import org.lwjgl.glfw.GLFWFramebufferSizeCallbackI as __GLFWFramebufferSizeCallbackI
__GLFWFramebufferSizeCallbackI = __GLFWFramebufferSizeCallbackI
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
try:
    from pyglsystem import libffi
except ImportError:
    libffi = __import_once__("pyglsystem.libffi")

import org.lwjgl.system.libffi.FFICIF as __FFICIF
__FFICIF = __FFICIF
import org.lwjgl.glfw.GLFWFramebufferSizeCallback as __GLFWFramebufferSizeCallback
__GLFWFramebufferSizeCallback = __GLFWFramebufferSizeCallback
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
 
class GLFWFramebufferSizeCallback(ABC, pyglsystem.__Callback, pyglsystem.Callback, __GLFWFramebufferSizeCallbackI, GLFWFramebufferSizeCallbackI):
    """org.lwjgl.glfw.GLFWFramebufferSizeCallback"""
 
    @staticmethod
    def __wrap(java_value: __GLFWFramebufferSizeCallback) -> 'GLFWFramebufferSizeCallback':
        return GLFWFramebufferSizeCallback(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWFramebufferSizeCallback):
        """
        Dynamic initializer for GLFWFramebufferSizeCallback.
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

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.createSafe(long)"""
        return GLFWFramebufferSizeCallback.__wrap(__GLFWFramebufferSizeCallback.createSafe(__long.valueOf(arg0)))

    @abstractmethod
    def invoke(self, arg0: int, arg1: int, arg2: int):
        """public abstract void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.invoke(long,int,int)"""
        pass

    @overload
    def set(self, arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.set(long)"""
        return 'GLFWFramebufferSizeCallback'.__wrap(super(__GLFWFramebufferSizeCallback, self).set(__long.valueOf(arg0)))

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

    @override
    @overload
    def getCallInterface(self) -> 'libffi.FFICIF':
        """public default org.lwjgl.system.libffi.FFICIF org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.getCallInterface()"""
        return 'libffi.FFICIF'.__wrap(super(GLFWFramebufferSizeCallbackI, self).getCallInterface())

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
        """public default void org.lwjgl.glfw.GLFWFramebufferSizeCallbackI.callback(long,long)"""
        super(__GLFWFramebufferSizeCallbackI, self).callback(__long.valueOf(arg0), __long.valueOf(arg1))

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Callback.address()"""
        return int.__wrap(super(pyglsystem.Callback, self).address())

    @staticmethod
    @overload
    def create(arg0: 'GLFWFramebufferSizeCallbackI') -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.create(org.lwjgl.glfw.GLFWFramebufferSizeCallbackI)"""
        return GLFWFramebufferSizeCallback.__wrap(__GLFWFramebufferSizeCallback.create(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWFramebufferSizeCallback':
        """public static org.lwjgl.glfw.GLFWFramebufferSizeCallback org.lwjgl.glfw.GLFWFramebufferSizeCallback.create(long)"""
        return GLFWFramebufferSizeCallback.__wrap(__GLFWFramebufferSizeCallback.create(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Callback.toString()"""
        return str.__wrap(super(pyglsystem.Callback, self).toString()) 
 
 
# CLASS: org.lwjgl.glfw.GLFWGamepadState$Buffer
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
import java.nio.FloatBuffer as FloatBuffer
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.Byte as __byte
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

import org.lwjgl.glfw.GLFWGamepadState as __GLFWGamepadState_Buffer
__Buffer = __GLFWGamepadState_Buffer.Buffer
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.Float as __float
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.nio.FloatBuffer as __FloatBuffer
__FloatBuffer = __FloatBuffer
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class Buffer(pyglsystem.__StructBuffer, pyglsystem.StructBuffer, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWGamepadState.Buffer"""
 
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
    def axes(self, arg0: int) -> float:
        """public float org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(int)"""
        return float.__wrap(super(__Buffer, self).axes(__int.valueOf(arg0)))

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
    def buttons(self, arg0: int, arg1: int) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(int,byte)"""
        return 'Buffer'.__wrap(super(__Buffer, self).buttons(__int.valueOf(arg0), __byte.valueOf(arg1)))

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
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer(java.nio.ByteBuffer)"""
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
    def axes(self, arg0: int, arg1: float) -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(int,float)"""
        return 'Buffer'.__wrap(super(__Buffer, self).axes(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def position(self, arg0: int) -> 'pyglsystem.CustomBuffer':
        """public SELF org.lwjgl.system.CustomBuffer.position(int)"""
        return 'pyglsystem.CustomBuffer'.__wrap(super(__pyglsystem.CustomBuffer, self).position(__int.valueOf(arg0)))

    @overload
    def buttons(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons()"""
        return 'ByteBuffer'.__wrap(super(Buffer, self).buttons())

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
    def buttons(self, arg0: 'ByteBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(java.nio.ByteBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).buttons(arg0))

    @overload
    def put(self, arg0: int, arg1: 'Struct') -> 'pyglsystem.StructBuffer':
        """public SELF org.lwjgl.system.StructBuffer.put(int,T)"""
        return 'pyglsystem.StructBuffer'.__wrap(super(__pyglsystem.StructBuffer, self).put(__int.valueOf(arg0), arg1))

    @overload
    def axes(self, arg0: 'FloatBuffer') -> 'Buffer':
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes(java.nio.FloatBuffer)"""
        return 'Buffer'.__wrap(super(__Buffer, self).axes(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public org.lwjgl.glfw.GLFWGamepadState$Buffer(long,int)"""
        val = __Buffer(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def buttons(self, arg0: int) -> int:
        """public byte org.lwjgl.glfw.GLFWGamepadState$Buffer.buttons(int)"""
        return int.__wrap(super(__Buffer, self).buttons(__int.valueOf(arg0)))

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
    def axes(self) -> 'FloatBuffer':
        """public java.nio.FloatBuffer org.lwjgl.glfw.GLFWGamepadState$Buffer.axes()"""
        return 'FloatBuffer'.__wrap(super(Buffer, self).axes())

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
 
 
# CLASS: org.lwjgl.glfw.GLFWAllocator
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

import org.lwjgl.glfw.GLFWAllocator as __GLFWAllocator_Buffer
__Buffer = __GLFWAllocator_Buffer.Buffer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.lwjgl.system.Struct as __Struct
__Struct = __Struct
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.lwjgl.glfw.GLFWAllocator as __GLFWAllocator
__GLFWAllocator = __GLFWAllocator
import org.lwjgl.glfw.GLFWAllocateCallback as __GLFWAllocateCallback
__GLFWAllocateCallback = __GLFWAllocateCallback
import org.lwjgl.glfw.GLFWDeallocateCallback as __GLFWDeallocateCallback
__GLFWDeallocateCallback = __GLFWDeallocateCallback
import org.lwjgl.system.Pointer as __Pointer_Default
__Default = __Pointer_Default.Default
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
import org.lwjgl.glfw.GLFWReallocateCallback as __GLFWReallocateCallback
__GLFWReallocateCallback = __GLFWReallocateCallback
 
class GLFWAllocator(pyglsystem.__Struct, pyglsystem.Struct, pyglsystem.__NativeResource, pyglsystem.NativeResource):
    """org.lwjgl.glfw.GLFWAllocator"""
 
    @staticmethod
    def __wrap(java_value: __GLFWAllocator) -> 'GLFWAllocator':
        return GLFWAllocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWAllocator):
        """
        Dynamic initializer for GLFWAllocator.
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
    def set(self, arg0: 'GLFWAllocateCallbackI', arg1: 'GLFWReallocateCallbackI', arg2: 'GLFWDeallocateCallbackI', arg3: int) -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.set(org.lwjgl.glfw.GLFWAllocateCallbackI,org.lwjgl.glfw.GLFWReallocateCallbackI,org.lwjgl.glfw.GLFWDeallocateCallbackI,long)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).set(arg0, arg1, arg2, __long.valueOf(arg3)))

    @staticmethod
    @overload
    def validate(arg0: int):
        """public static void org.lwjgl.glfw.GLFWAllocator.validate(long)"""
        __GLFWAllocator.validate(__long.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def malloc() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.malloc()"""
        return GLFWAllocator.__wrap(__GLFWAllocator.malloc())

    @overload
    def isNull(self, arg0: int) -> bool:
        """public boolean org.lwjgl.system.Struct.isNull(int)"""
        return bool.__wrap(super(__pyglsystem.Struct, self).isNull(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.create(long,int)"""
        return Buffer.__wrap(__GLFWAllocator.create(__long.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def allocate(self) -> 'GLFWAllocateCallback':
        """public org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator.allocate()"""
        return 'GLFWAllocateCallback'.__wrap(super(GLFWAllocator, self).allocate())

    @staticmethod
    @overload
    def nuser(arg0: int, arg1: int):
        """public static void org.lwjgl.glfw.GLFWAllocator.nuser(long,long)"""
        __GLFWAllocator.nuser(__long.valueOf(arg0), __long.valueOf(arg1))

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
    def user(self) -> int:
        """public long org.lwjgl.glfw.GLFWAllocator.user()"""
        return int.__wrap(super(GLFWAllocator, self).user())

    @staticmethod
    @overload
    def calloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.calloc(int)"""
        return Buffer.__wrap(__GLFWAllocator.calloc(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def calloc(arg0: 'MemoryStack') -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.calloc(org.lwjgl.system.MemoryStack)"""
        return GLFWAllocator.__wrap(__GLFWAllocator.calloc(arg0))

    @staticmethod
    @overload
    def ndeallocate(arg0: int) -> 'GLFWDeallocateCallback':
        """public static org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator.ndeallocate(long)"""
        return GLFWDeallocateCallback.__wrap(__GLFWAllocator.ndeallocate(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def create(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.create(int)"""
        return Buffer.__wrap(__GLFWAllocator.create(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def nuser(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWAllocator.nuser(long)"""
        return int.__wrap(__GLFWAllocator.nuser(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createSafe(arg0: int, arg1: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.createSafe(long,int)"""
        return Buffer.__wrap(__GLFWAllocator.createSafe(__long.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def close(self):
        """public default void org.lwjgl.system.NativeResource.close()"""
        super(pyglsystem.NativeResource, self).close()

    @overload
    def reallocate(self) -> 'GLFWReallocateCallback':
        """public org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator.reallocate()"""
        return 'GLFWReallocateCallback'.__wrap(super(GLFWAllocator, self).reallocate())

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
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.malloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWAllocator.malloc(__int.valueOf(arg0), arg1))

    @override
    @overload
    def sizeof(self) -> int:
        """public int org.lwjgl.glfw.GLFWAllocator.sizeof()"""
        return int.__wrap(super(GLFWAllocator, self).sizeof())

    @overload
    def allocate(self, arg0: 'GLFWAllocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.allocate(org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).allocate(arg0))

    @staticmethod
    @overload
    def nreallocate(arg0: int) -> 'GLFWReallocateCallback':
        """public static org.lwjgl.glfw.GLFWReallocateCallback org.lwjgl.glfw.GLFWAllocator.nreallocate(long)"""
        return GLFWReallocateCallback.__wrap(__GLFWAllocator.nreallocate(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def malloc(arg0: int) -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.malloc(int)"""
        return Buffer.__wrap(__GLFWAllocator.malloc(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def deallocate(self, arg0: 'GLFWDeallocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.deallocate(org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).deallocate(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ByteBuffer'):
        """public org.lwjgl.glfw.GLFWAllocator(java.nio.ByteBuffer)"""
        val = __GLFWAllocator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def reallocate(self, arg0: 'GLFWReallocateCallbackI') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.reallocate(org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).reallocate(arg0))

    @staticmethod
    @overload
    def create() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.create()"""
        return GLFWAllocator.__wrap(__GLFWAllocator.create())

    @staticmethod
    @overload
    def nallocate(arg0: int, arg1: 'GLFWAllocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.nallocate(long,org.lwjgl.glfw.GLFWAllocateCallbackI)"""
        __GLFWAllocator.nallocate(__long.valueOf(arg0), arg1)

    @override
    @overload
    def address(self) -> int:
        """public long org.lwjgl.system.Pointer$Default.address()"""
        return int.__wrap(super(pyglsystem.Pointer$Default, self).address())

    @staticmethod
    @overload
    def createSafe(arg0: int) -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.createSafe(long)"""
        return GLFWAllocator.__wrap(__GLFWAllocator.createSafe(__long.valueOf(arg0)))

    @overload
    def user(self, arg0: int) -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.user(long)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).user(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def ndeallocate(arg0: int, arg1: 'GLFWDeallocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.ndeallocate(long,org.lwjgl.glfw.GLFWDeallocateCallbackI)"""
        __GLFWAllocator.ndeallocate(__long.valueOf(arg0), arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.lwjgl.system.Pointer$Default.toString()"""
        return str.__wrap(super(pyglsystem.Pointer$Default, self).toString())

    @staticmethod
    @overload
    def malloc(arg0: 'MemoryStack') -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.malloc(org.lwjgl.system.MemoryStack)"""
        return GLFWAllocator.__wrap(__GLFWAllocator.malloc(arg0))

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

    @staticmethod
    @overload
    def calloc() -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.calloc()"""
        return GLFWAllocator.__wrap(__GLFWAllocator.calloc())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def calloc(arg0: int, arg1: 'MemoryStack') -> 'Buffer':
        """public static org.lwjgl.glfw.GLFWAllocator$Buffer org.lwjgl.glfw.GLFWAllocator.calloc(int,org.lwjgl.system.MemoryStack)"""
        return Buffer.__wrap(__GLFWAllocator.calloc(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def nreallocate(arg0: int, arg1: 'GLFWReallocateCallbackI'):
        """public static void org.lwjgl.glfw.GLFWAllocator.nreallocate(long,org.lwjgl.glfw.GLFWReallocateCallbackI)"""
        __GLFWAllocator.nreallocate(__long.valueOf(arg0), arg1)

    @overload
    def deallocate(self) -> 'GLFWDeallocateCallback':
        """public org.lwjgl.glfw.GLFWDeallocateCallback org.lwjgl.glfw.GLFWAllocator.deallocate()"""
        return 'GLFWDeallocateCallback'.__wrap(super(GLFWAllocator, self).deallocate())

    @staticmethod
    @overload
    def create(arg0: int) -> 'GLFWAllocator':
        """public static org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.create(long)"""
        return GLFWAllocator.__wrap(__GLFWAllocator.create(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def validate(arg0: int, arg1: int, arg2: int, arg3: 'StructValidation'):
        """public static void org.lwjgl.system.Struct.validate(long,int,int,org.lwjgl.system.Struct$StructValidation)"""
        __Struct.validate(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), arg3)

    @overload
    def set(self, arg0: 'GLFWAllocator') -> 'GLFWAllocator':
        """public org.lwjgl.glfw.GLFWAllocator org.lwjgl.glfw.GLFWAllocator.set(org.lwjgl.glfw.GLFWAllocator)"""
        return 'GLFWAllocator'.__wrap(super(__GLFWAllocator, self).set(arg0))

    @staticmethod
    @overload
    def nallocate(arg0: int) -> 'GLFWAllocateCallback':
        """public static org.lwjgl.glfw.GLFWAllocateCallback org.lwjgl.glfw.GLFWAllocator.nallocate(long)"""
        return GLFWAllocateCallback.__wrap(__GLFWAllocator.nallocate(__long.valueOf(arg0))) 
 
 
# CLASS: org.lwjgl.glfw.GLFW$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import org.lwjgl.glfw.GLFW as __GLFW_Functions
__Functions = __GLFW_Functions.Functions
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFW.Functions"""
 
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
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeOSMesa
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.IntBuffer as IntBuffer
try:
    import pygl
except ImportError:
    pygl = __import_once__("pygl")

from builtins import type
try:
    import pyglsystem
except ImportError:
    pyglsystem = __import_once__("pyglsystem")

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
import org.lwjgl.glfw.GLFWNativeOSMesa as __GLFWNativeOSMesa
__GLFWNativeOSMesa = __GLFWNativeOSMesa
from builtins import int
 
class GLFWNativeOSMesa():
    """org.lwjgl.glfw.GLFWNativeOSMesa"""
 
    @staticmethod
    def __wrap(java_value: __GLFWNativeOSMesa) -> 'GLFWNativeOSMesa':
        return GLFWNativeOSMesa(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GLFWNativeOSMesa):
        """
        Dynamic initializer for GLFWNativeOSMesa.
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
    def glfwGetOSMesaDepthBuffer(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(long,int[],int[],int[],org.lwjgl.PointerBuffer)"""
        return int.__wrap(__GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def glfwGetOSMesaContext(arg0: int) -> int:
        """public static long org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaContext(long)"""
        return int.__wrap(__GLFWNativeOSMesa.glfwGetOSMesaContext(__long.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def glfwGetOSMesaDepthBuffer(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'PointerBuffer') -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return int.__wrap(__GLFWNativeOSMesa.glfwGetOSMesaDepthBuffer(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def setPath(arg0: str):
        """public static void org.lwjgl.glfw.GLFWNativeOSMesa.setPath(java.lang.String)"""
        __GLFWNativeOSMesa.setPath(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def nglfwGetOSMesaDepthBuffer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.nglfwGetOSMesaDepthBuffer(long,long,long,long,long)"""
        return int.__wrap(__GLFWNativeOSMesa.nglfwGetOSMesaDepthBuffer(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

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
    def setPath(arg0: 'FunctionProvider'):
        """public static void org.lwjgl.glfw.GLFWNativeOSMesa.setPath(org.lwjgl.system.FunctionProvider)"""
        __GLFWNativeOSMesa.setPath(arg0)

    @staticmethod
    @overload
    def glfwGetOSMesaColorBuffer(arg0: int, arg1: 'IntBuffer', arg2: 'IntBuffer', arg3: 'IntBuffer', arg4: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(long,java.nio.IntBuffer,java.nio.IntBuffer,java.nio.IntBuffer,org.lwjgl.PointerBuffer)"""
        return bool.__wrap(__GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nglfwGetOSMesaColorBuffer(arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> int:
        """public static int org.lwjgl.glfw.GLFWNativeOSMesa.nglfwGetOSMesaColorBuffer(long,long,long,long,long)"""
        return int.__wrap(__GLFWNativeOSMesa.nglfwGetOSMesaColorBuffer(__long.valueOf(arg0), __long.valueOf(arg1), __long.valueOf(arg2), __long.valueOf(arg3), __long.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def glfwGetOSMesaColorBuffer(arg0: int, arg1: 'int', arg2: 'int', arg3: 'int', arg4: 'PointerBuffer') -> bool:
        """public static boolean org.lwjgl.glfw.GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(long,int[],int[],int[],org.lwjgl.PointerBuffer)"""
        return bool.__wrap(__GLFWNativeOSMesa.glfwGetOSMesaColorBuffer(__long.valueOf(arg0), arg1, arg2, arg3, arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.lwjgl.glfw.GLFWNativeWGL$Functions
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import org.lwjgl.glfw.GLFWNativeWGL as __GLFWNativeWGL_Functions
__Functions = __GLFWNativeWGL_Functions.Functions
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Functions():
    """org.lwjgl.glfw.GLFWNativeWGL.Functions"""
 
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