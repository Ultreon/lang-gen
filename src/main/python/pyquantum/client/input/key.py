from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.input.key.KeyBind as _KeyBind
_KeyBind = _KeyBind
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyBind():
    """dev.ultreon.quantum.client.input.key.KeyBind"""
 
    @staticmethod
    def _wrap(java_value: _KeyBind) -> 'KeyBind':
        return KeyBind(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyBind):
        """
        Dynamic initializer for KeyBind.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyBind__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyBind__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,int)"""
        val = _KeyBind(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isPressed()"""
        return bool._wrap(super(KeyBind, self).isPressed())

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isJustPressed()"""
        return bool._wrap(super(KeyBind, self).isJustPressed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getKeyCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getKeyCode()"""
        return int._wrap(super(KeyBind, self).getKeyCode())

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

    @overload
    def setModifiers(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setModifiers(int)"""
        super(_KeyBind, self).setModifiers(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setKeyCode(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setKeyCode(int)"""
        super(_KeyBind, self).setKeyCode(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getModifiers(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getModifiers()"""
        return int._wrap(super(KeyBind, self).getModifiers())

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

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'Type'):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,dev.ultreon.quantum.client.input.key.KeyBind$Type)"""
        val = _KeyBind(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.key.KeyBind.getName()"""
        return str._wrap(super(KeyBind, self).getName())

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isReleased()"""
        return bool._wrap(super(KeyBind, self).isReleased())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind
import dev.ultreon.quantum.client.input.key.KeyBind as _KeyBind
_KeyBind = _KeyBind
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyBind():
    """dev.ultreon.quantum.client.input.key.KeyBind"""
 
    @staticmethod
    def _wrap(java_value: _KeyBind) -> 'KeyBind':
        return KeyBind(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyBind):
        """
        Dynamic initializer for KeyBind.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyBind__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyBind__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: int, arg2: int):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,int)"""
        val = _KeyBind(arg0, _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def isPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isPressed()"""
        return bool._wrap(super(KeyBind, self).isPressed())

    @overload
    def isJustPressed(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isJustPressed()"""
        return bool._wrap(super(KeyBind, self).isJustPressed())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getKeyCode(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getKeyCode()"""
        return int._wrap(super(KeyBind, self).getKeyCode())

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

    @overload
    def setModifiers(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setModifiers(int)"""
        super(_KeyBind, self).setModifiers(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setKeyCode(self, arg0: int):
        """public void dev.ultreon.quantum.client.input.key.KeyBind.setKeyCode(int)"""
        super(_KeyBind, self).setKeyCode(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getModifiers(self) -> int:
        """public int dev.ultreon.quantum.client.input.key.KeyBind.getModifiers()"""
        return int._wrap(super(KeyBind, self).getModifiers())

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

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'Type'):
        """public dev.ultreon.quantum.client.input.key.KeyBind(java.lang.String,int,dev.ultreon.quantum.client.input.key.KeyBind$Type)"""
        val = _KeyBind(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.input.key.KeyBind.getName()"""
        return str._wrap(super(KeyBind, self).getName())

    @overload
    def isReleased(self) -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind.isReleased()"""
        return bool._wrap(super(KeyBind, self).isReleased())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBindRegistry
import dev.ultreon.quantum.client.input.key.KeyBind as _KeyBind
_KeyBind = _KeyBind
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.input.key.KeyBindRegistry as _KeyBindRegistry
_KeyBindRegistry = _KeyBindRegistry
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KeyBindRegistry():
    """dev.ultreon.quantum.client.input.key.KeyBindRegistry"""
 
    @staticmethod
    def _wrap(java_value: _KeyBindRegistry) -> 'KeyBindRegistry':
        return KeyBindRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyBindRegistry):
        """
        Dynamic initializer for KeyBindRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyBindRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyBindRegistry__wrapper":
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

    @staticmethod
    @overload
    def register(arg0: 'KeyBind') -> 'KeyBind':
        """public static dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBindRegistry.register(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return KeyBind._wrap(_KeyBindRegistry.register(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBind$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.client.input.key.KeyBind as _KeyBind_Type
_Type = _KeyBind_Type.Type
import java.lang.String as _String
_String = _String
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
    """dev.ultreon.quantum.client.input.key.KeyBind.Type"""
 
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
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static dev.ultreon.quantum.client.input.key.KeyBind$Type dev.ultreon.quantum.client.input.key.KeyBind$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static dev.ultreon.quantum.client.input.key.KeyBind$Type[] dev.ultreon.quantum.client.input.key.KeyBind$Type.values()"""
        return List[Type]._wrap(_Type.values())

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

    @overload
    def isPressed(self, arg0: 'KeyBind') -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind$Type.isPressed(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return bool._wrap(super(_Type, self).isPressed(arg0))

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
    def isJustPressed(self, arg0: 'KeyBind') -> bool:
        """public boolean dev.ultreon.quantum.client.input.key.KeyBind$Type.isJustPressed(dev.ultreon.quantum.client.input.key.KeyBind)"""
        return bool._wrap(super(_Type, self).isJustPressed(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Type.MOUSE = Type._wrap(_MOUSE.MOUSE)

Type.KEY = Type._wrap(_KEY.KEY) 
 
 
# CLASS: dev.ultreon.quantum.client.input.key.KeyBinds
import dev.ultreon.quantum.client.input.key.KeyBinds as _KeyBinds
_KeyBinds = _KeyBinds
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
 
class KeyBinds():
    """dev.ultreon.quantum.client.input.key.KeyBinds"""
 
    @staticmethod
    def _wrap(java_value: _KeyBinds) -> 'KeyBinds':
        return KeyBinds(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KeyBinds):
        """
        Dynamic initializer for KeyBinds.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KeyBinds__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KeyBinds__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.commandKey
    commandKey: 'KeyBind' = _wrap(_KeyBind.commandKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.thirdPersonKey
    thirdPersonKey: 'KeyBind' = _wrap(_KeyBind.thirdPersonKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.imGuiKey
    imGuiKey: 'KeyBind' = _wrap(_KeyBind.imGuiKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkBackwardsKey
    walkBackwardsKey: 'KeyBind' = _wrap(_KeyBind.walkBackwardsKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkRightKey
    walkRightKey: 'KeyBind' = _wrap(_KeyBind.walkRightKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.pauseKey
    pauseKey: 'KeyBind' = _wrap(_KeyBind.pauseKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.fullScreenKey
    fullScreenKey: 'KeyBind' = _wrap(_KeyBind.fullScreenKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.crouchKey
    crouchKey: 'KeyBind' = _wrap(_KeyBind.crouchKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.inspectKey
    inspectKey: 'KeyBind' = _wrap(_KeyBind.inspectKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.inventoryKey
    inventoryKey: 'KeyBind' = _wrap(_KeyBind.inventoryKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.runningKey
    runningKey: 'KeyBind' = _wrap(_KeyBind.runningKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.jumpKey
    jumpKey: 'KeyBind' = _wrap(_KeyBind.jumpKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.hideHudKey
    hideHudKey: 'KeyBind' = _wrap(_KeyBind.hideHudKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkLeftKey
    walkLeftKey: 'KeyBind' = _wrap(_KeyBind.walkLeftKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.debugKey
    debugKey: 'KeyBind' = _wrap(_KeyBind.debugKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.screenshotKey
    screenshotKey: 'KeyBind' = _wrap(_KeyBind.screenshotKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.quickMove
    quickMove: 'KeyBind' = _wrap(_KeyBind.quickMove)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.dropItemKey
    dropItemKey: 'KeyBind' = _wrap(_KeyBind.dropItemKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.imGuiFocusKey
    imGuiFocusKey: 'KeyBind' = _wrap(_KeyBind.imGuiFocusKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.chatKey
    chatKey: 'KeyBind' = _wrap(_KeyBind.chatKey)

    # public static final dev.ultreon.quantum.client.input.key.KeyBind dev.ultreon.quantum.client.input.key.KeyBinds.walkForwardsKey
    walkForwardsKey: 'KeyBind' = _wrap(_KeyBind.walkForwardsKey)


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