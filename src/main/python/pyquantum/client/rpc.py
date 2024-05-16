from __future__ import annotations
from overload import overload


 
from builtins import str
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
import dev.ultreon.quantum.client.rpc.GameActivity as __GameActivity
__GameActivity = __GameActivity
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GameActivity():
    """dev.ultreon.quantum.client.rpc.GameActivity"""
 
    @staticmethod
    def __wrap(java_value: __GameActivity) -> 'GameActivity':
        return GameActivity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameActivity):
        """
        Dynamic initializer for GameActivity.
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
 
    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.SINGLEPLAYER
    SINGLEPLAYER: 'GameActivity' = __wrap(__GameActivity.SINGLEPLAYER)

    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.MULTIPLAYER
    MULTIPLAYER: 'GameActivity' = __wrap(__GameActivity.MULTIPLAYER)

    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.MAIN_MENU
    MAIN_MENU: 'GameActivity' = __wrap(__GameActivity.MAIN_MENU)


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

    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.rpc.GameActivity.getDescription() throws java.lang.Exception"""
        return str.__wrap(super(GameActivity, self).getDescription())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GameActivity':
        """public static dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.valueOf(java.lang.String)"""
        return GameActivity.__wrap(__GameActivity.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDisplayName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.rpc.GameActivity.getDisplayName()"""
        return str.__wrap(super(GameActivity, self).getDisplayName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['GameActivity']:
        """public static dev.ultreon.quantum.client.rpc.GameActivity[] dev.ultreon.quantum.client.rpc.GameActivity.values()"""
        return List[GameActivity].__wrap(__GameActivity.values())

 
 
 
# CLASS: dev.ultreon.quantum.client.rpc.GameActivity
from builtins import str
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
import dev.ultreon.quantum.client.rpc.GameActivity as __GameActivity
__GameActivity = __GameActivity
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GameActivity():
    """dev.ultreon.quantum.client.rpc.GameActivity"""
 
    @staticmethod
    def __wrap(java_value: __GameActivity) -> 'GameActivity':
        return GameActivity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameActivity):
        """
        Dynamic initializer for GameActivity.
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
 
    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.SINGLEPLAYER
    SINGLEPLAYER: 'GameActivity' = __wrap(__GameActivity.SINGLEPLAYER)

    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.MULTIPLAYER
    MULTIPLAYER: 'GameActivity' = __wrap(__GameActivity.MULTIPLAYER)

    # public static final dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.MAIN_MENU
    MAIN_MENU: 'GameActivity' = __wrap(__GameActivity.MAIN_MENU)


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

    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.rpc.GameActivity.getDescription() throws java.lang.Exception"""
        return str.__wrap(super(GameActivity, self).getDescription())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GameActivity':
        """public static dev.ultreon.quantum.client.rpc.GameActivity dev.ultreon.quantum.client.rpc.GameActivity.valueOf(java.lang.String)"""
        return GameActivity.__wrap(__GameActivity.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getDisplayName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.rpc.GameActivity.getDisplayName()"""
        return str.__wrap(super(GameActivity, self).getDisplayName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['GameActivity']:
        """public static dev.ultreon.quantum.client.rpc.GameActivity[] dev.ultreon.quantum.client.rpc.GameActivity.values()"""
        return List[GameActivity].__wrap(__GameActivity.values())

 
 
 
# CLASS: dev.ultreon.quantum.client.rpc.GameActivity 
 
 
# CLASS: dev.ultreon.quantum.client.rpc.RpcHandler
import dev.ultreon.quantum.client.rpc.RpcHandler as __RpcHandler
__RpcHandler = __RpcHandler
from abc import abstractmethod, ABC
 
class RpcHandler(ABC):
    """dev.ultreon.quantum.client.rpc.RpcHandler"""
 
    @staticmethod
    def __wrap(java_value: __RpcHandler) -> 'RpcHandler':
        return RpcHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RpcHandler):
        """
        Dynamic initializer for RpcHandler.
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
    def start(self, ):
        """public abstract void dev.ultreon.quantum.client.rpc.RpcHandler.start()"""
        pass

    @staticmethod
    @overload
    def newActivity(arg0: 'GameActivity'):
        """public static void dev.ultreon.quantum.client.rpc.RpcHandler.newActivity(dev.ultreon.quantum.client.rpc.GameActivity)"""
        __RpcHandler.newActivity(arg0)

    @abstractmethod
    def setActivity(self, arg0: 'GameActivity'):
        """public abstract void dev.ultreon.quantum.client.rpc.RpcHandler.setActivity(dev.ultreon.quantum.client.rpc.GameActivity)"""
        pass