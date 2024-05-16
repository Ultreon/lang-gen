from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.debug.Debugger as __Debugger
__Debugger = __Debugger
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Debugger():
    """dev.ultreon.quantum.debug.Debugger"""
 
    @staticmethod
    def __wrap(java_value: __Debugger) -> 'Debugger':
        return Debugger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Debugger):
        """
        Dynamic initializer for Debugger.
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
    def __init__(self):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = __Debugger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def log(arg0: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String)"""
        __Debugger.log(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log(arg0: str, arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String,java.lang.Throwable)"""
        __Debugger.log(arg0, arg1)

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

    @staticmethod
    @overload
    def log(arg0: 'Type', arg1: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(dev.ultreon.quantum.debug.Debugger$Type,java.lang.String)"""
        __Debugger.log(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = __Debugger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.debug.Debugger as __Debugger
__Debugger = __Debugger
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Debugger():
    """dev.ultreon.quantum.debug.Debugger"""
 
    @staticmethod
    def __wrap(java_value: __Debugger) -> 'Debugger':
        return Debugger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Debugger):
        """
        Dynamic initializer for Debugger.
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
    def __init__(self):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = __Debugger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def log(arg0: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String)"""
        __Debugger.log(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def log(arg0: str, arg1: 'Throwable'):
        """public static void dev.ultreon.quantum.debug.Debugger.log(java.lang.String,java.lang.Throwable)"""
        __Debugger.log(arg0, arg1)

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

    @staticmethod
    @overload
    def log(arg0: 'Type', arg1: str):
        """public static void dev.ultreon.quantum.debug.Debugger.log(dev.ultreon.quantum.debug.Debugger$Type,java.lang.String)"""
        __Debugger.log(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.Debugger()"""
        val = __Debugger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger 
 
 
# CLASS: dev.ultreon.quantum.debug.WorldGenDebugContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.lang.Long as __long
import dev.ultreon.quantum.debug.WorldGenDebugContext as __WorldGenDebugContext
__WorldGenDebugContext = __WorldGenDebugContext
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldGenDebugContext():
    """dev.ultreon.quantum.debug.WorldGenDebugContext"""
 
    @staticmethod
    def __wrap(java_value: __WorldGenDebugContext) -> 'WorldGenDebugContext':
        return WorldGenDebugContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldGenDebugContext):
        """
        Dynamic initializer for WorldGenDebugContext.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.WorldGenDebugContext()"""
        val = __WorldGenDebugContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def isActive() -> bool:
        """public static boolean dev.ultreon.quantum.debug.WorldGenDebugContext.isActive()"""
        return bool.__wrap(__WorldGenDebugContext.isActive())

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
    def __init__(self):
        """public dev.ultreon.quantum.debug.WorldGenDebugContext()"""
        val = __WorldGenDebugContext()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def withinContext(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.debug.WorldGenDebugContext.withinContext(java.lang.Runnable)"""
        __WorldGenDebugContext.withinContext(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.DebugFlag
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.debug.DebugFlag as __DebugFlag
__DebugFlag = __DebugFlag
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DebugFlag():
    """dev.ultreon.quantum.debug.DebugFlag"""
 
    @staticmethod
    def __wrap(java_value: __DebugFlag) -> 'DebugFlag':
        return DebugFlag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugFlag):
        """
        Dynamic initializer for DebugFlag.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.debug.DebugFlag.equals(java.lang.Object)"""
        return bool.__wrap(super(__DebugFlag, self).equals(arg0))

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

    @overload
    def enabled(self) -> bool:
        """public boolean dev.ultreon.quantum.debug.DebugFlag.enabled()"""
        return bool.__wrap(super(DebugFlag, self).enabled())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: bool):
        """public dev.ultreon.quantum.debug.DebugFlag(boolean)"""
        val = __DebugFlag(__boolean.valueOf(arg0))
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.debug.DebugFlag.toString()"""
        return str.__wrap(super(DebugFlag, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.debug.DebugFlag.hashCode()"""
        return int.__wrap(super(DebugFlag, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.debug.DebugFlags
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
import dev.ultreon.quantum.debug.DebugFlags as __DebugFlags
__DebugFlags = __DebugFlags
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DebugFlags():
    """dev.ultreon.quantum.debug.DebugFlags"""
 
    @staticmethod
    def __wrap(java_value: __DebugFlags) -> 'DebugFlags':
        return DebugFlags(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DebugFlags):
        """
        Dynamic initializer for DebugFlags.
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
 
    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.DUMP_TEXTURE_ATLAS
    DUMP_TEXTURE_ATLAS: 'DebugFlag' = __wrap(__DebugFlag.DUMP_TEXTURE_ATLAS)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.LOG_OUT_OF_BOUNDS
    LOG_OUT_OF_BOUNDS: 'DebugFlag' = __wrap(__DebugFlag.LOG_OUT_OF_BOUNDS)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.LOG_POSITION_RESET_ON_CHUNK_LOAD
    LOG_POSITION_RESET_ON_CHUNK_LOAD: 'DebugFlag' = __wrap(__DebugFlag.LOG_POSITION_RESET_ON_CHUNK_LOAD)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.ORE_FEATURE
    ORE_FEATURE: 'DebugFlag' = __wrap(__DebugFlag.ORE_FEATURE)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.WORLD_GEN
    WORLD_GEN: 'DebugFlag' = __wrap(__DebugFlag.WORLD_GEN)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.CHUNK_BLOCK_DATA_DUMP
    CHUNK_BLOCK_DATA_DUMP: 'DebugFlag' = __wrap(__DebugFlag.CHUNK_BLOCK_DATA_DUMP)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.INSPECTION_ENABLED
    INSPECTION_ENABLED: 'DebugFlag' = __wrap(__DebugFlag.INSPECTION_ENABLED)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.WARN_CHUNK_BUILD_OVERLOAD
    WARN_CHUNK_BUILD_OVERLOAD: 'DebugFlag' = __wrap(__DebugFlag.WARN_CHUNK_BUILD_OVERLOAD)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.CHUNK_PACKET_DUMP
    CHUNK_PACKET_DUMP: 'DebugFlag' = __wrap(__DebugFlag.CHUNK_PACKET_DUMP)

    # public static final dev.ultreon.quantum.debug.DebugFlag dev.ultreon.quantum.debug.DebugFlags.PACKET_LOGGING
    PACKET_LOGGING: 'DebugFlag' = __wrap(__DebugFlag.PACKET_LOGGING)


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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.DebugFlags()"""
        val = __DebugFlags()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.DebugFlags()"""
        val = __DebugFlags()
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
 
 
# CLASS: dev.ultreon.quantum.debug.Debugger$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.debug.Debugger as __Debugger_Type
__Type = __Debugger_Type.Type
import java.util.Optional as __Optional
__Optional = __Optional
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
 
class Type(__Enum, Enum):
    """dev.ultreon.quantum.debug.Debugger.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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
 
    # public static final dev.ultreon.quantum.debug.Debugger$Type dev.ultreon.quantum.debug.Debugger$Type.CLEAN_UP
    CLEAN_UP: 'Type' = __wrap(__Type.CLEAN_UP)


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
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.debug.Debugger$Type dev.ultreon.quantum.debug.Debugger$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.debug.Debugger$Type[] dev.ultreon.quantum.debug.Debugger$Type.values()"""
        return List[Type].__wrap(__Type.values()) 
 
 
# CLASS: dev.ultreon.quantum.debug.ValueTracker
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
import dev.ultreon.quantum.debug.ValueTracker as __ValueTracker
__ValueTracker = __ValueTracker
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValueTracker():
    """dev.ultreon.quantum.debug.ValueTracker"""
 
    @staticmethod
    def __wrap(java_value: __ValueTracker) -> 'ValueTracker':
        return ValueTracker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueTracker):
        """
        Dynamic initializer for ValueTracker.
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
    def setPoolPeak(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolPeak(int)"""
        __ValueTracker.setPoolPeak(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

        @staticmethod
        @overload
        def trackFlushRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushRequest()"""
            __ValueTracker.trackFlushRequest()

    @staticmethod
    @overload
    def setPacketsSent(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsSent(int)"""
        __ValueTracker.setPacketsSent(__int.valueOf(arg0))

    @staticmethod
    @overload
    def setVertexCount(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setVertexCount(long)"""
        __ValueTracker.setVertexCount(__long.valueOf(arg0))

        @staticmethod
        @overload
        def resetObtainRequests():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetObtainRequests()"""
            __ValueTracker.resetObtainRequests()

    @staticmethod
    @overload
    def setPoolMax(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolMax(int)"""
        __ValueTracker.setPoolMax(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.debug.ValueTracker()"""
        val = __ValueTracker()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getPacketsReceivedTotal() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsReceivedTotal()"""
        return int.__wrap(__ValueTracker.getPacketsReceivedTotal())

    @staticmethod
    @overload
    def getChunkMeshFrees() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getChunkMeshFrees()"""
        return int.__wrap(__ValueTracker.getChunkMeshFrees())

    @staticmethod
    @overload
    def setChunkMeshFrees(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setChunkMeshFrees(long)"""
        __ValueTracker.setChunkMeshFrees(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getPoolFree() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getPoolFree()"""
        return int.__wrap(__ValueTracker.getPoolFree())

    @staticmethod
    @overload
    def setChunkLoads(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setChunkLoads(int)"""
        __ValueTracker.setChunkLoads(__int.valueOf(arg0))

    @staticmethod
    @overload
    def getVertexCount() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getVertexCount()"""
        return int.__wrap(__ValueTracker.getVertexCount())

        @staticmethod
        @overload
        def trackFreeRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFreeRequest()"""
            __ValueTracker.trackFreeRequest()

    @staticmethod
    @overload
    def getRenderableFlushes() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getRenderableFlushes()"""
        return int.__wrap(__ValueTracker.getRenderableFlushes())

        @staticmethod
        @overload
        def resetFlushed():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetFlushed()"""
            __ValueTracker.resetFlushed()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getFlushRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFlushRequests()"""
        return int.__wrap(__ValueTracker.getFlushRequests())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getPoolPeak() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPoolPeak()"""
        return int.__wrap(__ValueTracker.getPoolPeak())

    @staticmethod
    @overload
    def setObtainedRenderables(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setObtainedRenderables(int)"""
        __ValueTracker.setObtainedRenderables(__int.valueOf(arg0))

    @staticmethod
    @overload
    def setMeshDisposes(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setMeshDisposes(long)"""
        __ValueTracker.setMeshDisposes(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getFlushAttempts() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFlushAttempts()"""
        return int.__wrap(__ValueTracker.getFlushAttempts())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getObtainRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getObtainRequests()"""
        return int.__wrap(__ValueTracker.getObtainRequests())

    @staticmethod
    @overload
    def getChunkLoads() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getChunkLoads()"""
        return int.__wrap(__ValueTracker.getChunkLoads())

    @staticmethod
    @overload
    def trackFlushes(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushes(int)"""
        __ValueTracker.trackFlushes(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getPacketsSent() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsSent()"""
        return int.__wrap(__ValueTracker.getPacketsSent())

    @staticmethod
    @overload
    def setPacketsReceived(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsReceived(int)"""
        __ValueTracker.setPacketsReceived(__int.valueOf(arg0))

    @staticmethod
    @overload
    def setPacketsReceivedTotal(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPacketsReceivedTotal(int)"""
        __ValueTracker.setPacketsReceivedTotal(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.debug.ValueTracker()"""
        val = __ValueTracker()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getObtainedRenderables() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getObtainedRenderables()"""
        return int.__wrap(__ValueTracker.getObtainedRenderables())

        @staticmethod
        @overload
        def trackFlushAttempt():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackFlushAttempt()"""
            __ValueTracker.trackFlushAttempt()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getPacketsReceived() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPacketsReceived()"""
        return int.__wrap(__ValueTracker.getPacketsReceived())

    @staticmethod
    @overload
    def trackFreeRequests(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.trackFreeRequests(int)"""
        __ValueTracker.trackFreeRequests(__int.valueOf(arg0))

    @staticmethod
    @overload
    def getFreeRequests() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getFreeRequests()"""
        return int.__wrap(__ValueTracker.getFreeRequests())

    @staticmethod
    @overload
    def setPoolFree(arg0: int):
        """public static void dev.ultreon.quantum.debug.ValueTracker.setPoolFree(long)"""
        __ValueTracker.setPoolFree(__long.valueOf(arg0))

        @staticmethod
        @overload
        def trackObtainRequest():
            """public static void dev.ultreon.quantum.debug.ValueTracker.trackObtainRequest()"""
            __ValueTracker.trackObtainRequest()

    @staticmethod
    @overload
    def getPoolMax() -> int:
        """public static int dev.ultreon.quantum.debug.ValueTracker.getPoolMax()"""
        return int.__wrap(__ValueTracker.getPoolMax())

        @staticmethod
        @overload
        def resetFlushAttempts():
            """public static void dev.ultreon.quantum.debug.ValueTracker.resetFlushAttempts()"""
            __ValueTracker.resetFlushAttempts()

    @staticmethod
    @overload
    def getMeshDisposes() -> int:
        """public static long dev.ultreon.quantum.debug.ValueTracker.getMeshDisposes()"""
        return int.__wrap(__ValueTracker.getMeshDisposes())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()