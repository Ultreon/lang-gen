from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.quantum.client.gui.screens.options.BooleanEnum as __BooleanEnum
__BooleanEnum = __BooleanEnum
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import int
 
class BooleanEnum():
    """dev.ultreon.quantum.client.gui.screens.options.BooleanEnum"""
 
    @staticmethod
    def __wrap(java_value: __BooleanEnum) -> 'BooleanEnum':
        return BooleanEnum(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanEnum):
        """
        Dynamic initializer for BooleanEnum.
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
 
    # public static final dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.TRUE
    TRUE: 'BooleanEnum' = __wrap(__BooleanEnum.TRUE)

    # public static final dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.FALSE
    FALSE: 'BooleanEnum' = __wrap(__BooleanEnum.FALSE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BooleanEnum':
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.valueOf(java.lang.String)"""
        return BooleanEnum.__wrap(__BooleanEnum.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: bool) -> 'BooleanEnum':
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.of(boolean)"""
        return BooleanEnum.__wrap(__BooleanEnum.of(__boolean.valueOf(arg0)))

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

    @overload
    def get(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.get()"""
        return bool.__wrap(super(BooleanEnum, self).get())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['BooleanEnum']:
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum[] dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.values()"""
        return List[BooleanEnum].__wrap(__BooleanEnum.values())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.options.BooleanEnum
from builtins import str
import dev.ultreon.quantum.client.gui.screens.options.BooleanEnum as __BooleanEnum
__BooleanEnum = __BooleanEnum
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import int
 
class BooleanEnum():
    """dev.ultreon.quantum.client.gui.screens.options.BooleanEnum"""
 
    @staticmethod
    def __wrap(java_value: __BooleanEnum) -> 'BooleanEnum':
        return BooleanEnum(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanEnum):
        """
        Dynamic initializer for BooleanEnum.
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
 
    # public static final dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.TRUE
    TRUE: 'BooleanEnum' = __wrap(__BooleanEnum.TRUE)

    # public static final dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.FALSE
    FALSE: 'BooleanEnum' = __wrap(__BooleanEnum.FALSE)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'BooleanEnum':
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.valueOf(java.lang.String)"""
        return BooleanEnum.__wrap(__BooleanEnum.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: bool) -> 'BooleanEnum':
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.of(boolean)"""
        return BooleanEnum.__wrap(__BooleanEnum.of(__boolean.valueOf(arg0)))

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

    @overload
    def get(self) -> bool:
        """public boolean dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.get()"""
        return bool.__wrap(super(BooleanEnum, self).get())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['BooleanEnum']:
        """public static dev.ultreon.quantum.client.gui.screens.options.BooleanEnum[] dev.ultreon.quantum.client.gui.screens.options.BooleanEnum.values()"""
        return List[BooleanEnum].__wrap(__BooleanEnum.values())

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

 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.options.BooleanEnum 
 
 
# CLASS: dev.ultreon.quantum.client.gui.screens.options.Scale
from builtins import str
import dev.ultreon.quantum.client.gui.screens.options.Scale as __Scale
__Scale = __Scale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
 
class Scale():
    """dev.ultreon.quantum.client.gui.screens.options.Scale"""
 
    @staticmethod
    def __wrap(java_value: __Scale) -> 'Scale':
        return Scale(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Scale):
        """
        Dynamic initializer for Scale.
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
 
    # public static final dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.MEDIUM
    MEDIUM: 'Scale' = __wrap(__Scale.MEDIUM)

    # public static final dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.AUTO
    AUTO: 'Scale' = __wrap(__Scale.AUTO)

    # public static final dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.SMALL
    SMALL: 'Scale' = __wrap(__Scale.SMALL)

    # public static final dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.LARGE
    LARGE: 'Scale' = __wrap(__Scale.LARGE)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['Scale']:
        """public static dev.ultreon.quantum.client.gui.screens.options.Scale[] dev.ultreon.quantum.client.gui.screens.options.Scale.values()"""
        return List[Scale].__wrap(__Scale.values())

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

    @overload
    def get(self) -> int:
        """public int dev.ultreon.quantum.client.gui.screens.options.Scale.get()"""
        return int.__wrap(super(Scale, self).get())

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
    def of(arg0: int) -> 'Scale':
        """public static dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.of(int)"""
        return Scale.__wrap(__Scale.of(__int.valueOf(arg0)))

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Scale':
        """public static dev.ultreon.quantum.client.gui.screens.options.Scale dev.ultreon.quantum.client.gui.screens.options.Scale.valueOf(java.lang.String)"""
        return Scale.__wrap(__Scale.valueOf(arg0))

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