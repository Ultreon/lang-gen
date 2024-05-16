from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.variables.ObjectSource as __ObjectSource
__ObjectSource = __ObjectSource
import java.lang.Class as __Class
__Class = __Class
from builtins import type
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
 
class ObjectSource(ABC):
    """dev.ultreon.quantum.api.commands.variables.ObjectSource"""
 
    @staticmethod
    def __wrap(java_value: __ObjectSource) -> 'ObjectSource':
        return ObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectSource):
        """
        Dynamic initializer for ObjectSource.
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
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader'):
        """public abstract java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass

    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'.__wrap(super(ObjectSource, self).getType())

    @abstractmethod
    def getObjectType(self, ):
        """public abstract dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getObjectType()"""
        pass

    @abstractmethod
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder'):
        """public abstract dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectSource
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.variables.ObjectSource as __ObjectSource
__ObjectSource = __ObjectSource
import java.lang.Class as __Class
__Class = __Class
from builtins import type
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
 
class ObjectSource(ABC):
    """dev.ultreon.quantum.api.commands.variables.ObjectSource"""
 
    @staticmethod
    def __wrap(java_value: __ObjectSource) -> 'ObjectSource':
        return ObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectSource):
        """
        Dynamic initializer for ObjectSource.
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
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader'):
        """public abstract java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass

    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'.__wrap(super(ObjectSource, self).getType())

    @abstractmethod
    def getObjectType(self, ):
        """public abstract dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getObjectType()"""
        pass

    @abstractmethod
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder'):
        """public abstract dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectSource 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.ObjectField as __ObjectField
__ObjectField = __ObjectField
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.libs.commons.v0.Either as __Either
__Either = __Either
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.variables.ObjectType as __ObjectType
__ObjectType = __ObjectType
from builtins import int
 
class ObjectType():
    """dev.ultreon.quantum.api.commands.variables.ObjectType"""
 
    @staticmethod
    def __wrap(java_value: __ObjectType) -> 'ObjectType':
        return ObjectType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectType):
        """
        Dynamic initializer for ObjectType.
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
 
    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<java.lang.Number> dev.ultreon.quantum.api.commands.variables.ObjectType.NUMBER
    NUMBER: 'ObjectType' = __wrap(__ObjectType.NUMBER)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<java.lang.Void> dev.ultreon.quantum.api.commands.variables.ObjectType.NONE
    NONE: 'ObjectType' = __wrap(__ObjectType.NONE)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.api.commands.Command> dev.ultreon.quantum.api.commands.variables.ObjectType.COMMAND
    COMMAND: 'ObjectType' = __wrap(__ObjectType.COMMAND)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.api.commands.variables.ObjectType.PLAYER
    PLAYER: 'ObjectType' = __wrap(__ObjectType.PLAYER)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.world.ServerWorld> dev.ultreon.quantum.api.commands.variables.ObjectType.WORLD
    WORLD: 'ObjectType' = __wrap(__ObjectType.WORLD)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.api.commands.variables.ObjectType.ENTITY
    ENTITY: 'ObjectType' = __wrap(__ObjectType.ENTITY)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.item.Item> dev.ultreon.quantum.api.commands.variables.ObjectType.ITEM
    ITEM: 'ObjectType' = __wrap(__ObjectType.ITEM)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<java.lang.String> dev.ultreon.quantum.api.commands.variables.ObjectType.STRING
    STRING: 'ObjectType' = __wrap(__ObjectType.STRING)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.server.QuantumServer> dev.ultreon.quantum.api.commands.variables.ObjectType.SERVER
    SERVER: 'ObjectType' = __wrap(__ObjectType.SERVER)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<java.lang.Boolean> dev.ultreon.quantum.api.commands.variables.ObjectType.BOOLEAN
    BOOLEAN: 'ObjectType' = __wrap(__ObjectType.BOOLEAN)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.api.commands.variables.ObjectType.ITEM_STACK
    ITEM_STACK: 'ObjectType' = __wrap(__ObjectType.ITEM_STACK)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<dev.ultreon.quantum.block.Block> dev.ultreon.quantum.api.commands.variables.ObjectType.BLOCK
    BLOCK: 'ObjectType' = __wrap(__ObjectType.BLOCK)

    # public static final dev.ultreon.quantum.api.commands.variables.ObjectType<java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer>> dev.ultreon.quantum.api.commands.variables.ObjectType.PLAYER_LIST
    PLAYER_LIST: 'ObjectType' = __wrap(__ObjectType.PLAYER_LIST)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def cast(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.api.commands.variables.ObjectType.cast(java.lang.Object)"""
        return object.__wrap(super(__ObjectType, self).cast(arg0))

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectType.getType()"""
        return 'type.Class'.__wrap(super(ObjectType, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectType.getObjectType()"""
        return 'ObjectType'.__wrap(super(ObjectType, self).getObjectType())

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'ObjectType':
        """public static <T> dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectType.get(java.lang.Class<T>)"""
        return ObjectType.__wrap(__ObjectType.get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectType.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'.__wrap(super(__ObjectType, self).tabComplete(arg0, arg1, arg2))

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectType.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(super(__ObjectType, self).get(arg0, arg1))

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

    @overload
    def getField(self, arg0: str) -> 'ObjectField':
        """public dev.ultreon.quantum.api.commands.variables.ObjectField<T, ?> dev.ultreon.quantum.api.commands.variables.ObjectType.getField(java.lang.String)"""
        return 'ObjectField'.__wrap(super(__ObjectType, self).getField(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isInstance(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.variables.ObjectType.isInstance(java.lang.Object)"""
        return bool.__wrap(super(__ObjectType, self).isInstance(arg0))

    @overload
    def registerField(self, arg0: str, arg1: 'ObjectField'):
        """public void dev.ultreon.quantum.api.commands.variables.ObjectType.registerField(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectField<T, ?>)"""
        super(__ObjectType, self).registerField(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.ObjectType.getName()"""
        return str.__wrap(super(ObjectType, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.quantum.api.commands.variables.ObjectType(java.lang.String,T...)"""
        val = __ObjectType(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.RootVariableSource
from pyquantum_helper import import_once as __import_once__
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.libs.commons.v0.Either as __Either
__Either = __Either
from builtins import object
import dev.ultreon.quantum.api.commands.variables.ObjectSource as __ObjectSource
__ObjectSource = __ObjectSource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __String
__String = __String
import java.lang.String as __string
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.util.function.Supplier as __Supplier
__Supplier = __Supplier
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.variables.ObjectType as __ObjectType
__ObjectType = __ObjectType
import dev.ultreon.quantum.api.commands.variables.RootVariableSource as __RootVariableSource
__RootVariableSource = __RootVariableSource
from builtins import int
 
class RootVariableSource():
    """dev.ultreon.quantum.api.commands.variables.RootVariableSource"""
 
    @staticmethod
    def __wrap(java_value: __RootVariableSource) -> 'RootVariableSource':
        return RootVariableSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RootVariableSource):
        """
        Dynamic initializer for RootVariableSource.
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
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.RootVariableSource.getObjectType()"""
        return 'ObjectType'.__wrap(super(RootVariableSource, self).getObjectType())

    @overload
    def __init__(self, arg0: 'ObjectType', arg1: 'Supplier'):
        """public dev.ultreon.quantum.api.commands.variables.RootVariableSource(dev.ultreon.quantum.api.commands.variables.ObjectType<T>,java.util.function.Supplier<T>)"""
        val = __RootVariableSource(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: 'ObjectType', arg2: 'Supplier'):
        """public dev.ultreon.quantum.api.commands.variables.RootVariableSource(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectType<T>,java.util.function.Supplier<T>)"""
        val = __RootVariableSource(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.RootVariableSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'.__wrap(super(__RootVariableSource, self).tabComplete(arg0, arg1, arg2))

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
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'.__wrap(super(ObjectSource, self).getType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getter(self) -> 'Supplier':
        """public java.util.function.Supplier<T> dev.ultreon.quantum.api.commands.variables.RootVariableSource.getter()"""
        return 'Supplier'.__wrap(super(RootVariableSource, self).getter())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.RootVariableSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader)"""
        return object.__wrap(super(__RootVariableSource, self).get(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.PlayerVariables
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.Result as __Result
__Result = __Result
import java.util.stream.Stream as __Stream
__Stream = __Stream
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.variables.PlayerVariables as __PlayerVariables
__PlayerVariables = __PlayerVariables
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerVariables():
    """dev.ultreon.quantum.api.commands.variables.PlayerVariables"""
 
    @staticmethod
    def __wrap(java_value: __PlayerVariables) -> 'PlayerVariables':
        return PlayerVariables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerVariables):
        """
        Dynamic initializer for PlayerVariables.
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
    def get(arg0: 'ServerPlayer') -> 'PlayerVariables':
        """public static dev.ultreon.quantum.api.commands.variables.PlayerVariables dev.ultreon.quantum.api.commands.variables.PlayerVariables.get(dev.ultreon.quantum.server.player.ServerPlayer)"""
        return PlayerVariables.__wrap(__PlayerVariables.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getVariablesByType(self, arg0: 'Class') -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariablesByType(java.lang.Class<?>)"""
        return 'Stream'.__wrap(super(__PlayerVariables, self).getVariablesByType(arg0))

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

    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.api.commands.variables.PlayerVariables.getPlayer()"""
        return 'player.ServerPlayer'.__wrap(super(PlayerVariables, self).getPlayer())

    @overload
    def setVariable(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.api.commands.variables.PlayerVariables.setVariable(java.lang.String,java.lang.Object)"""
        super(__PlayerVariables, self).setVariable(arg0, arg1)

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
    def getVariable(self, arg0: str, arg1: 'Class') -> 'util.Result':
        """public <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariable(java.lang.String,java.lang.Class<T>)"""
        return 'util.Result'.__wrap(super(__PlayerVariables, self).getVariable(arg0, arg1))

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
    def getVariable(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariable(java.lang.String)"""
        return object.__wrap(super(__PlayerVariables, self).getVariable(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectSources
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
import dev.ultreon.quantum.api.commands.variables.ObjectSources as __ObjectSources
__ObjectSources = __ObjectSources
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjectSources():
    """dev.ultreon.quantum.api.commands.variables.ObjectSources"""
 
    @staticmethod
    def __wrap(java_value: __ObjectSources) -> 'ObjectSources':
        return ObjectSources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectSources):
        """
        Dynamic initializer for ObjectSources.
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
 
    # public static final dev.ultreon.quantum.api.commands.variables.SelectorObjectSource<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.api.commands.variables.ObjectSources.PLAYER
    PLAYER: 'SelectorObjectSource' = __wrap(__SelectorObjectSource.PLAYER)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.variables.ObjectSources()"""
        val = __ObjectSources()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.variables.ObjectSources()"""
        val = __ObjectSources()
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.RootVariables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Set as __Set
__Set = __Set
import dev.ultreon.quantum.api.commands.variables.RootVariables as __RootVariables
__RootVariables = __RootVariables
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.variables.RootVariableSource as __RootVariableSource
__RootVariableSource = __RootVariableSource
from builtins import int
 
class RootVariables():
    """dev.ultreon.quantum.api.commands.variables.RootVariables"""
 
    @staticmethod
    def __wrap(java_value: __RootVariables) -> 'RootVariables':
        return RootVariables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RootVariables):
        """
        Dynamic initializer for RootVariables.
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
 
    # public static final dev.ultreon.quantum.api.commands.variables.RootVariableSource<dev.ultreon.quantum.server.QuantumServer> dev.ultreon.quantum.api.commands.variables.RootVariables.SERVER
    SERVER: 'RootVariableSource' = __wrap(__RootVariableSource.SERVER)


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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def names() -> 'Set':
        """public static java.util.Set<java.lang.String> dev.ultreon.quantum.api.commands.variables.RootVariables.names()"""
        return Set.__wrap(__RootVariables.names())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.variables.RootVariables()"""
        val = __RootVariables()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.variables.RootVariables()"""
        val = __RootVariables()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def get(arg0: str) -> 'RootVariableSource':
        """public static dev.ultreon.quantum.api.commands.variables.RootVariableSource<?> dev.ultreon.quantum.api.commands.variables.RootVariables.get(java.lang.String)"""
        return RootVariableSource.__wrap(__RootVariables.get(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.PlayerVariable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.api.commands.variables.PlayerVariable as __PlayerVariable
__PlayerVariable = __PlayerVariable
from builtins import type
from builtins import object
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
 
class PlayerVariable():
    """dev.ultreon.quantum.api.commands.variables.PlayerVariable"""
 
    @staticmethod
    def __wrap(java_value: __PlayerVariable) -> 'PlayerVariable':
        return PlayerVariable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerVariable):
        """
        Dynamic initializer for PlayerVariable.
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

    @overload
    def getValue(self) -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.PlayerVariable.getValue()"""
        return object.__wrap(super(PlayerVariable, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'PlayerVariables', arg1: str):
        """public dev.ultreon.quantum.api.commands.variables.PlayerVariable(dev.ultreon.quantum.api.commands.variables.PlayerVariables,java.lang.String)"""
        val = __PlayerVariable(arg0, arg1)
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

    @overload
    def setValue(self, arg0: object):
        """public void dev.ultreon.quantum.api.commands.variables.PlayerVariable.setValue(java.lang.Object)"""
        super(__PlayerVariable, self).setValue(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectField
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.ObjectField as __ObjectField
__ObjectField = __ObjectField
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.function.Function as __Function
__Function = __Function
import dev.ultreon.libs.commons.v0.Either as __Either
__Either = __Either
from builtins import object
import dev.ultreon.quantum.api.commands.variables.ObjectSource as __ObjectSource
__ObjectSource = __ObjectSource
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __string
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.util.function.Function as Function
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.variables.ObjectType as __ObjectType
__ObjectType = __ObjectType
from builtins import int
 
class ObjectField():
    """dev.ultreon.quantum.api.commands.variables.ObjectField"""
 
    @staticmethod
    def __wrap(java_value: __ObjectField) -> 'ObjectField':
        return ObjectField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectField):
        """
        Dynamic initializer for ObjectField.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectField.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(super(__ObjectField, self).get(arg0, arg1))

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

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectField.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'.__wrap(super(__ObjectField, self).tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'.__wrap(super(ObjectSource, self).getType())

    @overload
    def __init__(self, arg0: str, arg1: 'ObjectType', arg2: 'Function'):
        """public dev.ultreon.quantum.api.commands.variables.ObjectField(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectType<R>,java.util.function.Function<T, R>)"""
        val = __ObjectField(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getter(self) -> 'Function':
        """public java.util.function.Function<T, R> dev.ultreon.quantum.api.commands.variables.ObjectField.getter()"""
        return 'Function'.__wrap(super(ObjectField, self).getter())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.ObjectField.getName()"""
        return str.__wrap(super(ObjectField, self).getName())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<R> dev.ultreon.quantum.api.commands.variables.ObjectField.getObjectType()"""
        return 'ObjectType'.__wrap(super(ObjectField, self).getObjectType())

    @overload
    def getSource(self) -> 'ObjectSource':
        """public dev.ultreon.quantum.api.commands.variables.ObjectSource<?> dev.ultreon.quantum.api.commands.variables.ObjectField.getSource()"""
        return 'ObjectSource'.__wrap(super(ObjectField, self).getSource())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.SelectorObjectSource
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as __SelectorFactory
__SelectorFactory = __SelectorFactory
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.libs.commons.v0.Either as __Either
__Either = __Either
try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = __import_once__("pyquantum.api.commands.selector")

from builtins import object
import dev.ultreon.quantum.api.commands.variables.ObjectSource as __ObjectSource
__ObjectSource = __ObjectSource
import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.variables.SelectorObjectSource as __SelectorObjectSource
__SelectorObjectSource = __SelectorObjectSource
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = __import_once__("pycorelibs.commons.v0")

import java.lang.String as __string
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.variables.ObjectType as __ObjectType
__ObjectType = __ObjectType
from builtins import int
 
class SelectorObjectSource():
    """dev.ultreon.quantum.api.commands.variables.SelectorObjectSource"""
 
    @staticmethod
    def __wrap(java_value: __SelectorObjectSource) -> 'SelectorObjectSource':
        return SelectorObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectorObjectSource):
        """
        Dynamic initializer for SelectorObjectSource.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getName()"""
        return str.__wrap(super(SelectorObjectSource, self).getName())

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'SelectorFactory'):
        """public dev.ultreon.quantum.api.commands.variables.SelectorObjectSource(java.lang.String,java.lang.Class<T>,dev.ultreon.quantum.api.commands.selector.SelectorFactory<? extends dev.ultreon.quantum.api.commands.selector.BaseSelector<T>>)"""
        val = __SelectorObjectSource(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(super(__SelectorObjectSource, self).get(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'.__wrap(super(ObjectSource, self).getType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder)"""
        return 'v0.Either'.__wrap(super(__SelectorObjectSource, self).tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getObjectType()"""
        return 'ObjectType'.__wrap(super(SelectorObjectSource, self).getObjectType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSelectorFactory(self) -> 'selector.SelectorFactory':
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactory<? extends dev.ultreon.quantum.api.commands.selector.BaseSelector<T>> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getSelectorFactory()"""
        return 'selector.SelectorFactory'.__wrap(super(SelectorObjectSource, self).getSelectorFactory())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))