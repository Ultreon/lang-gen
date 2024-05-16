from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.util.function.BiPredicate as __BiPredicate
__BiPredicate = __BiPredicate
from typing import List
import dev.ultreon.quantum.client.data.gen.provider.DepthFunc as __DepthFunc
__DepthFunc = __DepthFunc
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.util.function.BiPredicate as BiPredicate
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
 
class DepthFunc(__Enum, Enum):
    """dev.ultreon.quantum.client.data.gen.provider.DepthFunc"""
 
    @staticmethod
    def __wrap(java_value: __DepthFunc) -> 'DepthFunc':
        return DepthFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DepthFunc):
        """
        Dynamic initializer for DepthFunc.
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
 
    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.NOTEQUAL
    NOTEQUAL: 'DepthFunc' = __wrap(__DepthFunc.NOTEQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.ALWAYS
    ALWAYS: 'DepthFunc' = __wrap(__DepthFunc.ALWAYS)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.GREATER
    GREATER: 'DepthFunc' = __wrap(__DepthFunc.GREATER)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.LESS
    LESS: 'DepthFunc' = __wrap(__DepthFunc.LESS)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.NEVER
    NEVER: 'DepthFunc' = __wrap(__DepthFunc.NEVER)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.EQUAL
    EQUAL: 'DepthFunc' = __wrap(__DepthFunc.EQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.LEQUAL
    LEQUAL: 'DepthFunc' = __wrap(__DepthFunc.LEQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.GEQUAL
    GEQUAL: 'DepthFunc' = __wrap(__DepthFunc.GEQUAL)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DepthFunc':
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.valueOf(java.lang.String)"""
        return DepthFunc.__wrap(__DepthFunc.valueOf(arg0))

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

    @overload
    def getPredicate(self) -> 'BiPredicate':
        """public java.util.function.BiPredicate<java.lang.Float, java.lang.Float> dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getPredicate()"""
        return 'BiPredicate'.__wrap(super(DepthFunc, self).getPredicate())

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
    def values() -> List['DepthFunc']:
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc[] dev.ultreon.quantum.client.data.gen.provider.DepthFunc.values()"""
        return List[DepthFunc].__wrap(__DepthFunc.values())

    @overload
    def getGlFunc(self) -> int:
        """public int dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getGlFunc()"""
        return int.__wrap(super(DepthFunc, self).getGlFunc())

 
 
 
# CLASS: dev.ultreon.quantum.client.data.gen.provider.DepthFunc
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import java.util.function.BiPredicate as __BiPredicate
__BiPredicate = __BiPredicate
from typing import List
import dev.ultreon.quantum.client.data.gen.provider.DepthFunc as __DepthFunc
__DepthFunc = __DepthFunc
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.util.function.BiPredicate as BiPredicate
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
 
class DepthFunc(__Enum, Enum):
    """dev.ultreon.quantum.client.data.gen.provider.DepthFunc"""
 
    @staticmethod
    def __wrap(java_value: __DepthFunc) -> 'DepthFunc':
        return DepthFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DepthFunc):
        """
        Dynamic initializer for DepthFunc.
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
 
    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.NOTEQUAL
    NOTEQUAL: 'DepthFunc' = __wrap(__DepthFunc.NOTEQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.ALWAYS
    ALWAYS: 'DepthFunc' = __wrap(__DepthFunc.ALWAYS)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.GREATER
    GREATER: 'DepthFunc' = __wrap(__DepthFunc.GREATER)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.LESS
    LESS: 'DepthFunc' = __wrap(__DepthFunc.LESS)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.NEVER
    NEVER: 'DepthFunc' = __wrap(__DepthFunc.NEVER)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.EQUAL
    EQUAL: 'DepthFunc' = __wrap(__DepthFunc.EQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.LEQUAL
    LEQUAL: 'DepthFunc' = __wrap(__DepthFunc.LEQUAL)

    # public static final dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.GEQUAL
    GEQUAL: 'DepthFunc' = __wrap(__DepthFunc.GEQUAL)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DepthFunc':
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.valueOf(java.lang.String)"""
        return DepthFunc.__wrap(__DepthFunc.valueOf(arg0))

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

    @overload
    def getPredicate(self) -> 'BiPredicate':
        """public java.util.function.BiPredicate<java.lang.Float, java.lang.Float> dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getPredicate()"""
        return 'BiPredicate'.__wrap(super(DepthFunc, self).getPredicate())

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
    def values() -> List['DepthFunc']:
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc[] dev.ultreon.quantum.client.data.gen.provider.DepthFunc.values()"""
        return List[DepthFunc].__wrap(__DepthFunc.values())

    @overload
    def getGlFunc(self) -> int:
        """public int dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getGlFunc()"""
        return int.__wrap(super(DepthFunc, self).getGlFunc())

 
 
 
# CLASS: dev.ultreon.quantum.client.data.gen.provider.DepthFunc