from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.LongConsumer as LongConsumer
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import dev.ultreon.quantum.desktop.imgui.ImGuiEx as __ImGuiEx
__ImGuiEx = __ImGuiEx
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
from builtins import bool
import java.util.function.LongSupplier as LongSupplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.function.DoubleConsumer as DoubleConsumer
import java.lang.Runnable as Runnable
import java.util.function.DoubleSupplier as DoubleSupplier
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = __import_once__("pycorelibs.functions.v0.supplier")

import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
from builtins import int
 
class ImGuiEx():
    """dev.ultreon.quantum.desktop.imgui.ImGuiEx"""
 
    @staticmethod
    def __wrap(java_value: __ImGuiEx) -> 'ImGuiEx':
        return ImGuiEx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImGuiEx):
        """
        Dynamic initializer for ImGuiEx.
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
    def editString(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editString(java.lang.String,java.lang.String,java.util.function.Supplier<java.lang.String>,java.util.function.Consumer<java.lang.String>)"""
        __ImGuiEx.editString(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def editShort(arg0: str, arg1: str, arg2: int, arg3: 'ShortConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editShort(java.lang.String,java.lang.String,short,dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        __ImGuiEx.editShort(arg0, arg1, __short.valueOf(arg2), arg3)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = __ImGuiEx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def editFloat(arg0: str, arg1: str, arg2: 'FloatSupplier', arg3: 'FloatConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editFloat(java.lang.String,java.lang.String,dev.ultreon.libs.functions.v0.supplier.FloatSupplier,dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        __ImGuiEx.editFloat(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def editColor3(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor3(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        __ImGuiEx.editColor3(arg0, arg1, arg2, arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def button(arg0: str, arg1: str, arg2: 'Runnable'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.button(java.lang.String,java.lang.String,java.lang.Runnable)"""
        __ImGuiEx.button(arg0, arg1, arg2)

    @staticmethod
    @overload
    def editBool(arg0: str, arg1: str, arg2: 'BooleanSupplier', arg3: 'BooleanConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editBool(java.lang.String,java.lang.String,java.util.function.BooleanSupplier,dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        __ImGuiEx.editBool(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def editVec3i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        __ImGuiEx.editVec3i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec3d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        __ImGuiEx.editVec3d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def editDouble(arg0: str, arg1: str, arg2: 'DoubleSupplier', arg3: 'DoubleConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editDouble(java.lang.String,java.lang.String,java.util.function.DoubleSupplier,java.util.function.DoubleConsumer)"""
        __ImGuiEx.editDouble(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4i>)"""
        __ImGuiEx.editVec4i(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = __ImGuiEx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec4f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4f>)"""
        __ImGuiEx.editVec4f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editLong(arg0: str, arg1: str, arg2: 'LongSupplier', arg3: 'LongConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editLong(java.lang.String,java.lang.String,java.util.function.LongSupplier,java.util.function.LongConsumer)"""
        __ImGuiEx.editLong(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def slider(arg0: str, arg1: str, arg2: int, arg3: int, arg4: int, arg5: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.slider(java.lang.String,java.lang.String,int,int,int,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        __ImGuiEx.slider(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def editVec4d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4d>)"""
        __ImGuiEx.editVec4d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def editEnum(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static <T extends java.lang.Enum<T>> void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editEnum(java.lang.String,java.lang.String,java.util.function.Supplier<T>,java.util.function.Consumer<T>)"""
        __ImGuiEx.editEnum(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2i>)"""
        __ImGuiEx.editVec2i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editByte(arg0: str, arg1: str, arg2: int, arg3: 'ByteConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editByte(java.lang.String,java.lang.String,byte,dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        __ImGuiEx.editByte(arg0, arg1, __byte.valueOf(arg2), arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def editVec2f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2f>)"""
        __ImGuiEx.editVec2f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editColor4(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor4(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        __ImGuiEx.editColor4(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2d>)"""
        __ImGuiEx.editVec2d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def text(arg0: str, arg1: 'Supplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.text(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        __ImGuiEx.text(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def editVec3f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3f>)"""
        __ImGuiEx.editVec3f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editInt(arg0: str, arg1: str, arg2: 'IntSupplier', arg3: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editInt(java.lang.String,java.lang.String,java.util.function.IntSupplier,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        __ImGuiEx.editInt(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def bool(arg0: str, arg1: 'BooleanSupplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.bool(java.lang.String,java.util.function.BooleanSupplier)"""
        __ImGuiEx.bool(arg0, arg1)

 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiEx
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
import java.util.function.LongConsumer as LongConsumer
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import dev.ultreon.quantum.desktop.imgui.ImGuiEx as __ImGuiEx
__ImGuiEx = __ImGuiEx
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
from builtins import bool
import java.util.function.LongSupplier as LongSupplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.function.DoubleConsumer as DoubleConsumer
import java.lang.Runnable as Runnable
import java.util.function.DoubleSupplier as DoubleSupplier
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = __import_once__("pycorelibs.functions.v0.supplier")

import java.util.function.IntSupplier as IntSupplier
import java.lang.Integer as __int
from builtins import int
 
class ImGuiEx():
    """dev.ultreon.quantum.desktop.imgui.ImGuiEx"""
 
    @staticmethod
    def __wrap(java_value: __ImGuiEx) -> 'ImGuiEx':
        return ImGuiEx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImGuiEx):
        """
        Dynamic initializer for ImGuiEx.
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
    def editString(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editString(java.lang.String,java.lang.String,java.util.function.Supplier<java.lang.String>,java.util.function.Consumer<java.lang.String>)"""
        __ImGuiEx.editString(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def editShort(arg0: str, arg1: str, arg2: int, arg3: 'ShortConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editShort(java.lang.String,java.lang.String,short,dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        __ImGuiEx.editShort(arg0, arg1, __short.valueOf(arg2), arg3)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = __ImGuiEx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def editFloat(arg0: str, arg1: str, arg2: 'FloatSupplier', arg3: 'FloatConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editFloat(java.lang.String,java.lang.String,dev.ultreon.libs.functions.v0.supplier.FloatSupplier,dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        __ImGuiEx.editFloat(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def editColor3(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor3(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        __ImGuiEx.editColor3(arg0, arg1, arg2, arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def button(arg0: str, arg1: str, arg2: 'Runnable'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.button(java.lang.String,java.lang.String,java.lang.Runnable)"""
        __ImGuiEx.button(arg0, arg1, arg2)

    @staticmethod
    @overload
    def editBool(arg0: str, arg1: str, arg2: 'BooleanSupplier', arg3: 'BooleanConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editBool(java.lang.String,java.lang.String,java.util.function.BooleanSupplier,dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        __ImGuiEx.editBool(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def editVec3i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        __ImGuiEx.editVec3i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec3d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        __ImGuiEx.editVec3d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def editDouble(arg0: str, arg1: str, arg2: 'DoubleSupplier', arg3: 'DoubleConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editDouble(java.lang.String,java.lang.String,java.util.function.DoubleSupplier,java.util.function.DoubleConsumer)"""
        __ImGuiEx.editDouble(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4i>)"""
        __ImGuiEx.editVec4i(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = __ImGuiEx()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec4f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4f>)"""
        __ImGuiEx.editVec4f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editLong(arg0: str, arg1: str, arg2: 'LongSupplier', arg3: 'LongConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editLong(java.lang.String,java.lang.String,java.util.function.LongSupplier,java.util.function.LongConsumer)"""
        __ImGuiEx.editLong(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def slider(arg0: str, arg1: str, arg2: int, arg3: int, arg4: int, arg5: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.slider(java.lang.String,java.lang.String,int,int,int,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        __ImGuiEx.slider(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def editVec4d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4d>)"""
        __ImGuiEx.editVec4d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def editEnum(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static <T extends java.lang.Enum<T>> void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editEnum(java.lang.String,java.lang.String,java.util.function.Supplier<T>,java.util.function.Consumer<T>)"""
        __ImGuiEx.editEnum(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2i>)"""
        __ImGuiEx.editVec2i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editByte(arg0: str, arg1: str, arg2: int, arg3: 'ByteConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editByte(java.lang.String,java.lang.String,byte,dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        __ImGuiEx.editByte(arg0, arg1, __byte.valueOf(arg2), arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def editVec2f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2f>)"""
        __ImGuiEx.editVec2f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editColor4(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor4(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        __ImGuiEx.editColor4(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2d>)"""
        __ImGuiEx.editVec2d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def text(arg0: str, arg1: 'Supplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.text(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        __ImGuiEx.text(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def editVec3f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3f>)"""
        __ImGuiEx.editVec3f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editInt(arg0: str, arg1: str, arg2: 'IntSupplier', arg3: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editInt(java.lang.String,java.lang.String,java.util.function.IntSupplier,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        __ImGuiEx.editInt(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def bool(arg0: str, arg1: 'BooleanSupplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.bool(java.lang.String,java.util.function.BooleanSupplier)"""
        __ImGuiEx.bool(arg0, arg1)

 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiEx 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.GuiEditor
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.desktop.imgui.GuiEditor as __GuiEditor
__GuiEditor = __GuiEditor
from builtins import int
 
class GuiEditor():
    """dev.ultreon.quantum.desktop.imgui.GuiEditor"""
 
    @staticmethod
    def __wrap(java_value: __GuiEditor) -> 'GuiEditor':
        return GuiEditor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuiEditor):
        """
        Dynamic initializer for GuiEditor.
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
    def render(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.desktop.imgui.GuiEditor.render(dev.ultreon.quantum.client.QuantumClient)"""
        super(__GuiEditor, self).render(arg0)

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.GuiEditor()"""
        val = __GuiEditor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.GuiEditor()"""
        val = __GuiEditor()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiOverlay
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.desktop.imgui.ImGuiOverlay as __ImGuiOverlay
__ImGuiOverlay = __ImGuiOverlay
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = __import_once__("pyquantum.client")

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
 
class ImGuiOverlay():
    """dev.ultreon.quantum.desktop.imgui.ImGuiOverlay"""
 
    @staticmethod
    def __wrap(java_value: __ImGuiOverlay) -> 'ImGuiOverlay':
        return ImGuiOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImGuiOverlay):
        """
        Dynamic initializer for ImGuiOverlay.
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
        def preInitImGui():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.preInitImGui()"""
            __ImGuiOverlay.preInitImGui()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiOverlay()"""
        val = __ImGuiOverlay()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiOverlay()"""
        val = __ImGuiOverlay()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def isProfilerShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isProfilerShown()"""
        return bool.__wrap(__ImGuiOverlay.isProfilerShown())

    @staticmethod
    @overload
    def renderImGui(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.renderImGui(dev.ultreon.quantum.client.QuantumClient)"""
        __ImGuiOverlay.renderImGui(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def isChunkSectionBordersShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isChunkSectionBordersShown()"""
        return bool.__wrap(__ImGuiOverlay.isChunkSectionBordersShown())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

        @staticmethod
        @overload
        def dispose():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.dispose()"""
            __ImGuiOverlay.dispose()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def setupImGui():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.setupImGui()"""
            __ImGuiOverlay.setupImGui()

    @staticmethod
    @overload
    def setShowingImGui(arg0: bool):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.setShowingImGui(boolean)"""
        __ImGuiOverlay.setShowingImGui(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def isShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isShown()"""
        return bool.__wrap(__ImGuiOverlay.isShown())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))