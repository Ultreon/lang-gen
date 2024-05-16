from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.input.key.KeyBind as __KeyBind
__KeyBind = __KeyBind
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KeyBind():
    """dev.ultreon.quantum.client.input.key.KeyBind"""
 
    @staticmethod
    def __wrap(java_value: __KeyBind) -> 'KeyBind':
        return KeyBind(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyBind):
        """
        Dynamic initializer for KeyBind.
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
    def getKeyCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getKeyCode()"""
        return int.__wrap(super(KeyBind, self).getKeyCode())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,int)"""
        val = __KeyBind(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isReleased()"""
        return bool.__wrap(super(KeyBind, self).isReleased())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setKeyCode(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setKeyCode(int)"""
        super(__KeyBind, self).setKeyCode(__int.valueOf(arg0))

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

    @overload
    def getModifiers(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getModifiers()"""
        return int.__wrap(super(KeyBind, self).getModifiers())

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isPressed()"""
        return bool.__wrap(super(KeyBind, self).isPressed())

    @overload
    def setModifiers(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setModifiers(int)"""
        super(__KeyBind, self).setModifiers(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'Type'):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,dev.ultreon.quantum.client.input.key.KeyBind$Type)"""
        val = __KeyBind(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.key.KeyBind.getName()"""
        return str.__wrap(super(KeyBind, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isJustPressed()"""
        return bool.__wrap(super(KeyBind, self).isJustPressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.input.key.KeyBind as __KeyBind
__KeyBind = __KeyBind
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KeyBind():
    """dev.ultreon.quantum.client.input.key.KeyBind"""
 
    @staticmethod
    def __wrap(java_value: __KeyBind) -> 'KeyBind':
        return KeyBind(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyBind):
        """
        Dynamic initializer for KeyBind.
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
    def getKeyCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getKeyCode()"""
        return int.__wrap(super(KeyBind, self).getKeyCode())

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,int)"""
        val = __KeyBind(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isReleased()"""
        return bool.__wrap(super(KeyBind, self).isReleased())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setKeyCode(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setKeyCode(int)"""
        super(__KeyBind, self).setKeyCode(__int.valueOf(arg0))

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

    @overload
    def getModifiers(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getModifiers()"""
        return int.__wrap(super(KeyBind, self).getModifiers())

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isPressed()"""
        return bool.__wrap(super(KeyBind, self).isPressed())

    @overload
    def setModifiers(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setModifiers(int)"""
        super(__KeyBind, self).setModifiers(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'Type'):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,dev.ultreon.quantum.client.input.key.KeyBind$Type)"""
        val = __KeyBind(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.key.KeyBind.getName()"""
        return str.__wrap(super(KeyBind, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isJustPressed()"""
        return bool.__wrap(super(KeyBind, self).isJustPressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBindRegistry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.input.key.KeyBindRegistry as __KeyBindRegistry
__KeyBindRegistry = __KeyBindRegistry
import dev.ultreon.quantum.client.input.key.KeyBind as __KeyBind
__KeyBind = __KeyBind
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
 
class KeyBindRegistry():
    """dev.ultreon.quantum.client.input.key.KeyBindRegistry"""
 
    @staticmethod
    def __wrap(java_value: __KeyBindRegistry) -> 'KeyBindRegistry':
        return KeyBindRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyBindRegistry):
        """
        Dynamic initializer for KeyBindRegistry.
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
    def register(arg0: 'KeyBind') -> 'KeyBind':
        """public static dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBindRegistry.register(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return KeyBind.__wrap(__KeyBindRegistry.register(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.input.key.KeyBind as __KeyBind_Type
__Type = __KeyBind_Type.Type
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
 
class Type(__Enum, Enum):
    """dev.ultreon.quantum.client.input.key.KeyBind.Type"""
 
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
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind$Type dev.ultreon.quantum.client.input.key.KeyBind$Type.KEY
    KEY: 'Type' = __wrap(__Type.KEY)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind$Type dev.ultreon.quantum.client.input.key.KeyBind$Type.MOUSE
    MOUSE: 'Type' = __wrap(__Type.MOUSE)


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
        """public static dev.ultreon.quantum.client.input.key.KeyBind$Type dev.ultreon.quantum.client.input.key.KeyBind$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @overload
    def isPressed(self, arg0: 'KeyBind') -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind$Type.isPressed(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return bool.__wrap(super(__Type, self).isPressed(arg0))

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

    @overload
    def isJustPressed(self, arg0: 'KeyBind') -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind$Type.isJustPressed(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return bool.__wrap(super(__Type, self).isJustPressed(arg0))

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
        """public static dev.ultreon.quantum.client.input.key.KeyBind$Type[] dev.ultreon.quantum.client.input.key.KeyBind$Type.values()"""
        return List[Type].__wrap(__Type.values()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBinds
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import dev.ultreon.quantum.client.input.key.KeyBinds as __KeyBinds
__KeyBinds = __KeyBinds
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KeyBinds():
    """dev.ultreon.quantum.client.input.key.KeyBinds"""
 
    @staticmethod
    def __wrap(java_value: __KeyBinds) -> 'KeyBinds':
        return KeyBinds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KeyBinds):
        """
        Dynamic initializer for KeyBinds.
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
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.imGuiFocusKey
    imGuiFocusKey: 'KeyBind' = __wrap(__KeyBind.imGuiFocusKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.hideHudKey
    hideHudKey: 'KeyBind' = __wrap(__KeyBind.hideHudKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.runningKey
    runningKey: 'KeyBind' = __wrap(__KeyBind.runningKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.screenshotKey
    screenshotKey: 'KeyBind' = __wrap(__KeyBind.screenshotKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.inventoryKey
    inventoryKey: 'KeyBind' = __wrap(__KeyBind.inventoryKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.thirdPersonKey
    thirdPersonKey: 'KeyBind' = __wrap(__KeyBind.thirdPersonKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkForwardsKey
    walkForwardsKey: 'KeyBind' = __wrap(__KeyBind.walkForwardsKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.jumpKey
    jumpKey: 'KeyBind' = __wrap(__KeyBind.jumpKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.inspectKey
    inspectKey: 'KeyBind' = __wrap(__KeyBind.inspectKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkBackwardsKey
    walkBackwardsKey: 'KeyBind' = __wrap(__KeyBind.walkBackwardsKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkRightKey
    walkRightKey: 'KeyBind' = __wrap(__KeyBind.walkRightKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.crouchKey
    crouchKey: 'KeyBind' = __wrap(__KeyBind.crouchKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.commandKey
    commandKey: 'KeyBind' = __wrap(__KeyBind.commandKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.pauseKey
    pauseKey: 'KeyBind' = __wrap(__KeyBind.pauseKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.debugKey
    debugKey: 'KeyBind' = __wrap(__KeyBind.debugKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.dropItemKey
    dropItemKey: 'KeyBind' = __wrap(__KeyBind.dropItemKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.imGuiKey
    imGuiKey: 'KeyBind' = __wrap(__KeyBind.imGuiKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.quickMove
    quickMove: 'KeyBind' = __wrap(__KeyBind.quickMove)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkLeftKey
    walkLeftKey: 'KeyBind' = __wrap(__KeyBind.walkLeftKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.fullScreenKey
    fullScreenKey: 'KeyBind' = __wrap(__KeyBind.fullScreenKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.chatKey
    chatKey: 'KeyBind' = __wrap(__KeyBind.chatKey)


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