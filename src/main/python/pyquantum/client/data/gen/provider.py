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
import dev.ultreon.quantum.client.data.gen.provider.DepthFunc as _DepthFunc
_DepthFunc = _DepthFunc
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.function.BiPredicate as BiPredicate
import java.util.function.BiPredicate as _BiPredicate
_BiPredicate = _BiPredicate
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DepthFunc():
    """dev.ultreon.quantum.client.data.gen.provider.DepthFunc"""
 
    @staticmethod
    def _wrap(java_value: _DepthFunc) -> 'DepthFunc':
        return DepthFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DepthFunc):
        """
        Dynamic initializer for DepthFunc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DepthFunc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DepthFunc__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getGlFunc(self) -> int:
        """public int dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getGlFunc()"""
        return int._wrap(super(DepthFunc, self).getGlFunc())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DepthFunc':
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.valueOf(java.lang.String)"""
        return DepthFunc._wrap(_DepthFunc.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getPredicate(self) -> 'BiPredicate':
        """public java.util.function.BiPredicate<java.lang.Float, java.lang.Float> dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getPredicate()"""
        return 'BiPredicate'._wrap(super(DepthFunc, self).getPredicate())

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

    @staticmethod
    @overload
    def values() -> List['DepthFunc']:
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc[] dev.ultreon.quantum.client.data.gen.provider.DepthFunc.values()"""
        return List[DepthFunc]._wrap(_DepthFunc.values())

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


DepthFunc.NEVER = DepthFunc._wrap(_NEVER.NEVER)

DepthFunc.LESS = DepthFunc._wrap(_LESS.LESS)

DepthFunc.GEQUAL = DepthFunc._wrap(_GEQUAL.GEQUAL)

DepthFunc.EQUAL = DepthFunc._wrap(_EQUAL.EQUAL)

DepthFunc.NOTEQUAL = DepthFunc._wrap(_NOTEQUAL.NOTEQUAL)

DepthFunc.GREATER = DepthFunc._wrap(_GREATER.GREATER)

DepthFunc.LEQUAL = DepthFunc._wrap(_LEQUAL.LEQUAL)

DepthFunc.ALWAYS = DepthFunc._wrap(_ALWAYS.ALWAYS)

 
 
 
# CLASS: dev.ultreon.quantum.client.data.gen.provider.DepthFunc
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.data.gen.provider.DepthFunc as _DepthFunc
_DepthFunc = _DepthFunc
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.function.BiPredicate as BiPredicate
import java.util.function.BiPredicate as _BiPredicate
_BiPredicate = _BiPredicate
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DepthFunc():
    """dev.ultreon.quantum.client.data.gen.provider.DepthFunc"""
 
    @staticmethod
    def _wrap(java_value: _DepthFunc) -> 'DepthFunc':
        return DepthFunc(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DepthFunc):
        """
        Dynamic initializer for DepthFunc.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DepthFunc__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DepthFunc__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getGlFunc(self) -> int:
        """public int dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getGlFunc()"""
        return int._wrap(super(DepthFunc, self).getGlFunc())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'DepthFunc':
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc dev.ultreon.quantum.client.data.gen.provider.DepthFunc.valueOf(java.lang.String)"""
        return DepthFunc._wrap(_DepthFunc.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getPredicate(self) -> 'BiPredicate':
        """public java.util.function.BiPredicate<java.lang.Float, java.lang.Float> dev.ultreon.quantum.client.data.gen.provider.DepthFunc.getPredicate()"""
        return 'BiPredicate'._wrap(super(DepthFunc, self).getPredicate())

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

    @staticmethod
    @overload
    def values() -> List['DepthFunc']:
        """public static dev.ultreon.quantum.client.data.gen.provider.DepthFunc[] dev.ultreon.quantum.client.data.gen.provider.DepthFunc.values()"""
        return List[DepthFunc]._wrap(_DepthFunc.values())

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


DepthFunc.NEVER = DepthFunc._wrap(_NEVER.NEVER)

DepthFunc.LESS = DepthFunc._wrap(_LESS.LESS)

DepthFunc.GEQUAL = DepthFunc._wrap(_GEQUAL.GEQUAL)

DepthFunc.EQUAL = DepthFunc._wrap(_EQUAL.EQUAL)

DepthFunc.NOTEQUAL = DepthFunc._wrap(_NOTEQUAL.NOTEQUAL)

DepthFunc.GREATER = DepthFunc._wrap(_GREATER.GREATER)

DepthFunc.LEQUAL = DepthFunc._wrap(_LEQUAL.LEQUAL)

DepthFunc.ALWAYS = DepthFunc._wrap(_ALWAYS.ALWAYS)

 
 
 
# CLASS: dev.ultreon.quantum.client.data.gen.provider.DepthFunc