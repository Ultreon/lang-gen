from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import java.util.function.LongConsumer as LongConsumer
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.Short as _short
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.lang.Byte as _byte
from builtins import bool
import java.util.function.LongSupplier as LongSupplier
from builtins import str
from pyquantum_helper import override
import java.util.function.DoubleConsumer as DoubleConsumer
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.util.function.DoubleSupplier as DoubleSupplier
import java.lang.Integer as _int
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = _import_once("pycorelibs.functions.v0.supplier")

import java.util.function.IntSupplier as IntSupplier
import dev.ultreon.quantum.desktop.imgui.ImGuiEx as _ImGuiEx
_ImGuiEx = _ImGuiEx
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImGuiEx():
    """dev.ultreon.quantum.desktop.imgui.ImGuiEx"""
 
    @staticmethod
    def _wrap(java_value: _ImGuiEx) -> 'ImGuiEx':
        return ImGuiEx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImGuiEx):
        """
        Dynamic initializer for ImGuiEx.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImGuiEx__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImGuiEx__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def text(arg0: str, arg1: 'Supplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.text(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        _ImGuiEx.text(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = _ImGuiEx()
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec2i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2i>)"""
        _ImGuiEx.editVec2i(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def editLong(arg0: str, arg1: str, arg2: 'LongSupplier', arg3: 'LongConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editLong(java.lang.String,java.lang.String,java.util.function.LongSupplier,java.util.function.LongConsumer)"""
        _ImGuiEx.editLong(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editShort(arg0: str, arg1: str, arg2: int, arg3: 'ShortConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editShort(java.lang.String,java.lang.String,short,dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        _ImGuiEx.editShort(arg0, arg1, _short.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def editDouble(arg0: str, arg1: str, arg2: 'DoubleSupplier', arg3: 'DoubleConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editDouble(java.lang.String,java.lang.String,java.util.function.DoubleSupplier,java.util.function.DoubleConsumer)"""
        _ImGuiEx.editDouble(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def editString(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editString(java.lang.String,java.lang.String,java.util.function.Supplier<java.lang.String>,java.util.function.Consumer<java.lang.String>)"""
        _ImGuiEx.editString(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def editColor4(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor4(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        _ImGuiEx.editColor4(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editByte(arg0: str, arg1: str, arg2: int, arg3: 'ByteConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editByte(java.lang.String,java.lang.String,byte,dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        _ImGuiEx.editByte(arg0, arg1, _byte.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def editVec3d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        _ImGuiEx.editVec3d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def button(arg0: str, arg1: str, arg2: 'Runnable'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.button(java.lang.String,java.lang.String,java.lang.Runnable)"""
        _ImGuiEx.button(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = _ImGuiEx()
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec4f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4f>)"""
        _ImGuiEx.editVec4f(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def editVec2f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2f>)"""
        _ImGuiEx.editVec2f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4d>)"""
        _ImGuiEx.editVec4d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editEnum(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static <T extends java.lang.Enum<T>> void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editEnum(java.lang.String,java.lang.String,java.util.function.Supplier<T>,java.util.function.Consumer<T>)"""
        _ImGuiEx.editEnum(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def editInt(arg0: str, arg1: str, arg2: 'IntSupplier', arg3: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editInt(java.lang.String,java.lang.String,java.util.function.IntSupplier,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        _ImGuiEx.editInt(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec3i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        _ImGuiEx.editVec3i(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def editColor3(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor3(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        _ImGuiEx.editColor3(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4i>)"""
        _ImGuiEx.editVec4i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editFloat(arg0: str, arg1: str, arg2: 'FloatSupplier', arg3: 'FloatConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editFloat(java.lang.String,java.lang.String,dev.ultreon.libs.functions.v0.supplier.FloatSupplier,dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        _ImGuiEx.editFloat(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def slider(arg0: str, arg1: str, arg2: int, arg3: int, arg4: int, arg5: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.slider(java.lang.String,java.lang.String,int,int,int,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        _ImGuiEx.slider(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def editBool(arg0: str, arg1: str, arg2: 'BooleanSupplier', arg3: 'BooleanConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editBool(java.lang.String,java.lang.String,java.util.function.BooleanSupplier,dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        _ImGuiEx.editBool(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2d>)"""
        _ImGuiEx.editVec2d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def bool(arg0: str, arg1: 'BooleanSupplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.bool(java.lang.String,java.util.function.BooleanSupplier)"""
        _ImGuiEx.bool(arg0, arg1)

    @staticmethod
    @overload
    def editVec3f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3f>)"""
        _ImGuiEx.editVec3f(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiEx
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
import java.util.function.LongConsumer as LongConsumer
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.Short as _short
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.lang.Byte as _byte
from builtins import bool
import java.util.function.LongSupplier as LongSupplier
from builtins import str
from pyquantum_helper import override
import java.util.function.DoubleConsumer as DoubleConsumer
import java.lang.Object as _object
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.util.function.DoubleSupplier as DoubleSupplier
import java.lang.Integer as _int
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = _import_once("pycorelibs.functions.v0.supplier")

import java.util.function.IntSupplier as IntSupplier
import dev.ultreon.quantum.desktop.imgui.ImGuiEx as _ImGuiEx
_ImGuiEx = _ImGuiEx
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImGuiEx():
    """dev.ultreon.quantum.desktop.imgui.ImGuiEx"""
 
    @staticmethod
    def _wrap(java_value: _ImGuiEx) -> 'ImGuiEx':
        return ImGuiEx(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImGuiEx):
        """
        Dynamic initializer for ImGuiEx.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImGuiEx__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImGuiEx__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def text(arg0: str, arg1: 'Supplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.text(java.lang.String,java.util.function.Supplier<java.lang.Object>)"""
        _ImGuiEx.text(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = _ImGuiEx()
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec2i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2i>)"""
        _ImGuiEx.editVec2i(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def editLong(arg0: str, arg1: str, arg2: 'LongSupplier', arg3: 'LongConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editLong(java.lang.String,java.lang.String,java.util.function.LongSupplier,java.util.function.LongConsumer)"""
        _ImGuiEx.editLong(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editShort(arg0: str, arg1: str, arg2: int, arg3: 'ShortConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editShort(java.lang.String,java.lang.String,short,dev.ultreon.libs.functions.v0.consumer.ShortConsumer)"""
        _ImGuiEx.editShort(arg0, arg1, _short.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def editDouble(arg0: str, arg1: str, arg2: 'DoubleSupplier', arg3: 'DoubleConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editDouble(java.lang.String,java.lang.String,java.util.function.DoubleSupplier,java.util.function.DoubleConsumer)"""
        _ImGuiEx.editDouble(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def editString(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editString(java.lang.String,java.lang.String,java.util.function.Supplier<java.lang.String>,java.util.function.Consumer<java.lang.String>)"""
        _ImGuiEx.editString(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def editColor4(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor4(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        _ImGuiEx.editColor4(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editByte(arg0: str, arg1: str, arg2: int, arg3: 'ByteConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editByte(java.lang.String,java.lang.String,byte,dev.ultreon.libs.functions.v0.consumer.ByteConsumer)"""
        _ImGuiEx.editByte(arg0, arg1, _byte.valueOf(arg2), arg3)

    @staticmethod
    @overload
    def editVec3d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3d>)"""
        _ImGuiEx.editVec3d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def button(arg0: str, arg1: str, arg2: 'Runnable'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.button(java.lang.String,java.lang.String,java.lang.Runnable)"""
        _ImGuiEx.button(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiEx()"""
        val = _ImGuiEx()
        self.__wrapper = val

    @staticmethod
    @overload
    def editVec4f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4f>)"""
        _ImGuiEx.editVec4f(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def editVec2f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2f>)"""
        _ImGuiEx.editVec2f(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4d>)"""
        _ImGuiEx.editVec4d(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editEnum(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static <T extends java.lang.Enum<T>> void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editEnum(java.lang.String,java.lang.String,java.util.function.Supplier<T>,java.util.function.Consumer<T>)"""
        _ImGuiEx.editEnum(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def editInt(arg0: str, arg1: str, arg2: 'IntSupplier', arg3: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editInt(java.lang.String,java.lang.String,java.util.function.IntSupplier,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        _ImGuiEx.editInt(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec3i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3i>)"""
        _ImGuiEx.editVec3i(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def editColor3(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editColor3(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.quantum.util.RgbColor>,java.util.function.Consumer<dev.ultreon.quantum.util.RgbColor>)"""
        _ImGuiEx.editColor3(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec4i(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec4i(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec4i>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec4i>)"""
        _ImGuiEx.editVec4i(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editFloat(arg0: str, arg1: str, arg2: 'FloatSupplier', arg3: 'FloatConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editFloat(java.lang.String,java.lang.String,dev.ultreon.libs.functions.v0.supplier.FloatSupplier,dev.ultreon.libs.functions.v0.consumer.FloatConsumer)"""
        _ImGuiEx.editFloat(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def slider(arg0: str, arg1: str, arg2: int, arg3: int, arg4: int, arg5: 'IntConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.slider(java.lang.String,java.lang.String,int,int,int,dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        _ImGuiEx.slider(arg0, arg1, _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), arg5)

    @staticmethod
    @overload
    def editBool(arg0: str, arg1: str, arg2: 'BooleanSupplier', arg3: 'BooleanConsumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editBool(java.lang.String,java.lang.String,java.util.function.BooleanSupplier,dev.ultreon.libs.functions.v0.consumer.BooleanConsumer)"""
        _ImGuiEx.editBool(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def editVec2d(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec2d(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec2d>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec2d>)"""
        _ImGuiEx.editVec2d(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def bool(arg0: str, arg1: 'BooleanSupplier'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.bool(java.lang.String,java.util.function.BooleanSupplier)"""
        _ImGuiEx.bool(arg0, arg1)

    @staticmethod
    @overload
    def editVec3f(arg0: str, arg1: str, arg2: 'Supplier', arg3: 'Consumer'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiEx.editVec3f(java.lang.String,java.lang.String,java.util.function.Supplier<dev.ultreon.libs.commons.v0.vector.Vec3f>,java.util.function.Consumer<dev.ultreon.libs.commons.v0.vector.Vec3f>)"""
        _ImGuiEx.editVec3f(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiEx 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.GuiEditor
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import dev.ultreon.quantum.desktop.imgui.GuiEditor as _GuiEditor
_GuiEditor = _GuiEditor
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GuiEditor():
    """dev.ultreon.quantum.desktop.imgui.GuiEditor"""
 
    @staticmethod
    def _wrap(java_value: _GuiEditor) -> 'GuiEditor':
        return GuiEditor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuiEditor):
        """
        Dynamic initializer for GuiEditor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuiEditor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuiEditor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.GuiEditor()"""
        val = _GuiEditor()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.GuiEditor()"""
        val = _GuiEditor()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def render(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.desktop.imgui.GuiEditor.render(dev.ultreon.quantum.client.QuantumClient)"""
        super(_GuiEditor, self).render(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.desktop.imgui.ImGuiOverlay
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import dev.ultreon.quantum.desktop.imgui.ImGuiOverlay as _ImGuiOverlay
_ImGuiOverlay = _ImGuiOverlay
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImGuiOverlay():
    """dev.ultreon.quantum.desktop.imgui.ImGuiOverlay"""
 
    @staticmethod
    def _wrap(java_value: _ImGuiOverlay) -> 'ImGuiOverlay':
        return ImGuiOverlay(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImGuiOverlay):
        """
        Dynamic initializer for ImGuiOverlay.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImGuiOverlay__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImGuiOverlay__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isChunkSectionBordersShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isChunkSectionBordersShown()"""
        return bool._wrap(_ImGuiOverlay.isChunkSectionBordersShown())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def setupImGui():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.setupImGui()"""
            _ImGuiOverlay.setupImGui()

    @staticmethod
    @overload
    def isShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isShown()"""
        return bool._wrap(_ImGuiOverlay.isShown())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

        @staticmethod
        @overload
        def preInitImGui():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.preInitImGui()"""
            _ImGuiOverlay.preInitImGui()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiOverlay()"""
        val = _ImGuiOverlay()
        self.__wrapper = val

        @staticmethod
        @overload
        def dispose():
            """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.dispose()"""
            _ImGuiOverlay.dispose()

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.desktop.imgui.ImGuiOverlay()"""
        val = _ImGuiOverlay()
        self.__wrapper = val

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
    def isProfilerShown() -> bool:
        """public static boolean dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.isProfilerShown()"""
        return bool._wrap(_ImGuiOverlay.isProfilerShown())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def renderImGui(arg0: 'QuantumClient'):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.renderImGui(dev.ultreon.quantum.client.QuantumClient)"""
        _ImGuiOverlay.renderImGui(arg0)

    @staticmethod
    @overload
    def setShowingImGui(arg0: bool):
        """public static void dev.ultreon.quantum.desktop.imgui.ImGuiOverlay.setShowingImGui(boolean)"""
        _ImGuiOverlay.setShowingImGui(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())