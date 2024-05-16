from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.debug.Debugger as _Debugger
_Debugger = _Debugger
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Debugger():
    """dev.ultreon.quantum.debug.Debugger"""
 
    @staticmethod
    def _wrap(java_value: _Debugger) -> 'Debugger':
        return Debugger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Debugger):
        """
        Dynamic initializer for Debugger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Debugger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Debugger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = _Debugger()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = _Debugger()
        self.__wrapper = val

    @staticmethod
    @overload
    def log(arg0: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String)"""
        _Debugger.log(arg0)

    @staticmethod
    @overload
    def log(arg0: str, arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String,java.lang.Throwable)"""
        _Debugger.log(arg0, arg1)

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
    def log(arg0: 'Type', arg1: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(dev.ultreon.quantum.debug.Debugger$Type,java.lang.String)"""
        _Debugger.log(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.debug.Debugger as _Debugger
_Debugger = _Debugger
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Debugger():
    """dev.ultreon.quantum.debug.Debugger"""
 
    @staticmethod
    def _wrap(java_value: _Debugger) -> 'Debugger':
        return Debugger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Debugger):
        """
        Dynamic initializer for Debugger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Debugger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Debugger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = _Debugger()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = _Debugger()
        self.__wrapper = val

    @staticmethod
    @overload
    def log(arg0: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String)"""
        _Debugger.log(arg0)

    @staticmethod
    @overload
    def log(arg0: str, arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String,java.lang.Throwable)"""
        _Debugger.log(arg0, arg1)

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
    def log(arg0: 'Type', arg1: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(dev.ultreon.quantum.debug.Debugger$Type,java.lang.String)"""
        _Debugger.log(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger 
 
 
# CLASS: dev.ultreon.quantum.debug.WorldGenDebugContext
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.debug.WorldGenDebugContext as _WorldGenDebugContext
_WorldGenDebugContext = _WorldGenDebugContext
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldGenDebugContext():
    """dev.ultreon.quantum.debug.WorldGenDebugContext"""
 
    @staticmethod
    def _wrap(java_value: _WorldGenDebugContext) -> 'WorldGenDebugContext':
        return WorldGenDebugContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldGenDebugContext):
        """
        Dynamic initializer for WorldGenDebugContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldGenDebugContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldGenDebugContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.WorldGenDebugContext()"""
        val = _WorldGenDebugContext()
        self.__wrapper = val

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.WorldGenDebugContext()"""
        val = _WorldGenDebugContext()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def withinContext(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.debug.WorldGenDebugContext.withinContext(java.lang.Runnable)"""
        _WorldGenDebugContext.withinContext(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isActive() -> bool:
        """public static boolean dev.ultreon.quantum.debug.WorldGenDebugContext.isActive()"""
        return bool._wrap(_WorldGenDebugContext.isActive())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.DebugFlag
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.debug.DebugFlag as _DebugFlag
_DebugFlag = _DebugFlag
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DebugFlag():
    """dev.ultreon.quantum.debug.DebugFlag"""
 
    @staticmethod
    def _wrap(java_value: _DebugFlag) -> 'DebugFlag':
        return DebugFlag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugFlag):
        """
        Dynamic initializer for DebugFlag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugFlag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugFlag__wrapper":
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

    @overload
    def __init__(self, arg0: bool):
        """public dev.ultreon.quantum.debug.DebugFlag(boolean)"""
        val = _DebugFlag(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.DebugFlag.toString()"""
        return str._wrap(super(DebugFlag, self).toString())

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

    @overload
    def enabled(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.DebugFlag.enabled()"""
        return bool._wrap(super(DebugFlag, self).enabled())

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
        """public boolean dev.ultreon.quantum.debug.DebugFlag.equals(java.lang.Object)"""
        return bool._wrap(super(_DebugFlag, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.debug.DebugFlag.hashCode()"""
        return int._wrap(super(DebugFlag, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.debug.DebugFlags
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.debug.DebugFlags as _DebugFlags
_DebugFlags = _DebugFlags
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DebugFlags():
    """dev.ultreon.quantum.debug.DebugFlags"""
 
    @staticmethod
    def _wrap(java_value: _DebugFlags) -> 'DebugFlags':
        return DebugFlags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DebugFlags):
        """
        Dynamic initializer for DebugFlags.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DebugFlags__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DebugFlags__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.CHUNK_BLOCK_DATA_DUMP
    CHUNK_BLOCK_DATA_DUMP: 'DebugFlag' = _wrap(_DebugFlag.CHUNK_BLOCK_DATA_DUMP)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.DUMP_TEXTURE_ATLAS
    DUMP_TEXTURE_ATLAS: 'DebugFlag' = _wrap(_DebugFlag.DUMP_TEXTURE_ATLAS)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.LOG_OUT_OF_BOUNDS
    LOG_OUT_OF_BOUNDS: 'DebugFlag' = _wrap(_DebugFlag.LOG_OUT_OF_BOUNDS)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.WORLD_GEN
    WORLD_GEN: 'DebugFlag' = _wrap(_DebugFlag.WORLD_GEN)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.INSPECTION_ENABLED
    INSPECTION_ENABLED: 'DebugFlag' = _wrap(_DebugFlag.INSPECTION_ENABLED)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.ORE_FEATURE
    ORE_FEATURE: 'DebugFlag' = _wrap(_DebugFlag.ORE_FEATURE)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.LOG_POSITION_RESET_ON_CHUNK_LOAD
    LOG_POSITION_RESET_ON_CHUNK_LOAD: 'DebugFlag' = _wrap(_DebugFlag.LOG_POSITION_RESET_ON_CHUNK_LOAD)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.PACKET_LOGGING
    PACKET_LOGGING: 'DebugFlag' = _wrap(_DebugFlag.PACKET_LOGGING)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.CHUNK_PACKET_DUMP
    CHUNK_PACKET_DUMP: 'DebugFlag' = _wrap(_DebugFlag.CHUNK_PACKET_DUMP)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.WARN_CHUNK_BUILD_OVERLOAD
    WARN_CHUNK_BUILD_OVERLOAD: 'DebugFlag' = _wrap(_DebugFlag.WARN_CHUNK_BUILD_OVERLOAD)


    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.DebugFlags()"""
        val = _DebugFlags()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.DebugFlags()"""
        val = _DebugFlags()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.debug.Debugger as _Debugger_Type
_Type = _Debugger_Type.Type
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """dev.ultreon.quantum.debug.Debugger.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.debug.Debugger$Type[] dev.ultreon.quantum.debug.Debugger$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.debug.Debugger$Type dev.ultreon.quantum.debug.Debugger$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Type.CLEAN_UP = Type._wrap(_CLEAN_UP.CLEAN_UP) 
 
 
# CLASS: dev.ultreon.quantum.debug.ValueTracker
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.debug.ValueTracker as _ValueTracker
_ValueTracker = _ValueTracker
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueTracker():
    """dev.ultreon.quantum.debug.ValueTracker"""
 
    @staticmethod
    def _wrap(java_value: _ValueTracker) -> 'ValueTracker':
        return ValueTracker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueTracker):
        """
        Dynamic initializer for ValueTracker.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueTracker__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueTracker__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getChunkLoads() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getChunkLoads()"""
        return int._wrap(_ValueTracker.getChunkLoads())

    @staticmethod
    @overload
    def getPacketsReceived() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsReceived()"""
        return int._wrap(_ValueTracker.getPacketsReceived())

    @staticmethod
    @overload
    def getPacketsSent() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsSent()"""
        return int._wrap(_ValueTracker.getPacketsSent())

    @staticmethod
    @overload
    def getPoolMax() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPoolMax()"""
        return int._wrap(_ValueTracker.getPoolMax())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def setPacketsSent(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsSent(int)"""
        _ValueTracker.setPacketsSent(_int.valueOf(arg0))

    @staticmethod
    @overload
    def setChunkLoads(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setChunkLoads(int)"""
        _ValueTracker.setChunkLoads(_int.valueOf(arg0))

    @staticmethod
    @overload
    def setVertexCount(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setVertexCount(long)"""
        _ValueTracker.setVertexCount(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getRenderableFlushes() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getRenderableFlushes()"""
        return int._wrap(_ValueTracker.getRenderableFlushes())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def setPacketsReceivedTotal(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsReceivedTotal(int)"""
        _ValueTracker.setPacketsReceivedTotal(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getChunkMeshFrees() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getChunkMeshFrees()"""
        return int._wrap(_ValueTracker.getChunkMeshFrees())

    @staticmethod
    @overload
    def setChunkMeshFrees(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setChunkMeshFrees(long)"""
        _ValueTracker.setChunkMeshFrees(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.ValueTracker()"""
        val = _ValueTracker()
        self.__wrapper = val

        @staticmethod
        @overload
        def trackFreeRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFreeRequest()"""
            _ValueTracker.trackFreeRequest()

    @staticmethod
    @overload
    def getVertexCount() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getVertexCount()"""
        return int._wrap(_ValueTracker.getVertexCount())

    @staticmethod
    @overload
    def setPoolFree(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolFree(long)"""
        _ValueTracker.setPoolFree(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getPoolFree() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getPoolFree()"""
        return int._wrap(_ValueTracker.getPoolFree())

    @staticmethod
    @overload
    def getFlushAttempts() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFlushAttempts()"""
        return int._wrap(_ValueTracker.getFlushAttempts())

        @staticmethod
        @overload
        def trackFlushAttempt():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushAttempt()"""
            _ValueTracker.trackFlushAttempt()

    @staticmethod
    @overload
    def setPoolMax(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolMax(int)"""
        _ValueTracker.setPoolMax(_int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def trackFreeRequests(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.trackFreeRequests(int)"""
        _ValueTracker.trackFreeRequests(_int.valueOf(arg0))

    @staticmethod
    @overload
    def getObtainedRenderables() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getObtainedRenderables()"""
        return int._wrap(_ValueTracker.getObtainedRenderables())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.ValueTracker()"""
        val = _ValueTracker()
        self.__wrapper = val

    @staticmethod
    @overload
    def setPacketsReceived(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsReceived(int)"""
        _ValueTracker.setPacketsReceived(_int.valueOf(arg0))

        @staticmethod
        @overload
        def resetFlushAttempts():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetFlushAttempts()"""
            _ValueTracker.resetFlushAttempts()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

        @staticmethod
        @overload
        def resetObtainRequests():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetObtainRequests()"""
            _ValueTracker.resetObtainRequests()

        @staticmethod
        @overload
        def trackFlushRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushRequest()"""
            _ValueTracker.trackFlushRequest()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def setPoolPeak(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolPeak(int)"""
        _ValueTracker.setPoolPeak(_int.valueOf(arg0))

    @staticmethod
    @overload
    def setObtainedRenderables(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setObtainedRenderables(int)"""
        _ValueTracker.setObtainedRenderables(_int.valueOf(arg0))

        @staticmethod
        @overload
        def trackObtainRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackObtainRequest()"""
            _ValueTracker.trackObtainRequest()

    @staticmethod
    @overload
    def getObtainRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getObtainRequests()"""
        return int._wrap(_ValueTracker.getObtainRequests())

    @staticmethod
    @overload
    def getFlushRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFlushRequests()"""
        return int._wrap(_ValueTracker.getFlushRequests())

    @staticmethod
    @overload
    def getMeshDisposes() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getMeshDisposes()"""
        return int._wrap(_ValueTracker.getMeshDisposes())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setMeshDisposes(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setMeshDisposes(long)"""
        _ValueTracker.setMeshDisposes(_long.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getPoolPeak() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPoolPeak()"""
        return int._wrap(_ValueTracker.getPoolPeak())

    @staticmethod
    @overload
    def trackFlushes(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushes(int)"""
        _ValueTracker.trackFlushes(_int.valueOf(arg0))

    @staticmethod
    @overload
    def getFreeRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFreeRequests()"""
        return int._wrap(_ValueTracker.getFreeRequests())

    @staticmethod
    @overload
    def getPacketsReceivedTotal() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsReceivedTotal()"""
        return int._wrap(_ValueTracker.getPacketsReceivedTotal())

        @staticmethod
        @overload
        def resetFlushed():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetFlushed()"""
            _ValueTracker.resetFlushed()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())