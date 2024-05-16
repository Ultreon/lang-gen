from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import type
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.variables.ObjectSource as _ObjectSource
_ObjectSource = _ObjectSource
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
import java.lang.Class as _Class
_Class = _Class
 
class ObjectSource():
    """dev.ultreon.quantum.api.commands.variables.ObjectSource"""
 
    @staticmethod
    def _wrap(java_value: _ObjectSource) -> 'ObjectSource':
        return ObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectSource):
        """
        Dynamic initializer for ObjectSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader'):
        """public abstract java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass

    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'._wrap(super(ObjectSource, self).getType())

    @abstractmethod
    def getObjectType(self, ):
        """public abstract dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getObjectType()"""
        pass

    @abstractmethod
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder'):
        """public abstract dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectSource
from pyquantum_helper import import_once as _import_once
from builtins import type
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.variables.ObjectSource as _ObjectSource
_ObjectSource = _ObjectSource
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
import java.lang.Class as _Class
_Class = _Class
 
class ObjectSource():
    """dev.ultreon.quantum.api.commands.variables.ObjectSource"""
 
    @staticmethod
    def _wrap(java_value: _ObjectSource) -> 'ObjectSource':
        return ObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectSource):
        """
        Dynamic initializer for ObjectSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader'):
        """public abstract java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass

    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'._wrap(super(ObjectSource, self).getType())

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
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import dev.ultreon.quantum.api.commands.variables.ObjectType as _ObjectType
_ObjectType = _ObjectType
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.variables.ObjectField as _ObjectField
_ObjectField = _ObjectField
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.StringBuilder as StringBuilder
from builtins import bool
import dev.ultreon.libs.commons.v0.Either as _Either
_Either = _Either
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ObjectType():
    """dev.ultreon.quantum.api.commands.variables.ObjectType"""
 
    @staticmethod
    def _wrap(java_value: _ObjectType) -> 'ObjectType':
        return ObjectType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectType):
        """
        Dynamic initializer for ObjectType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectType.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'._wrap(super(_ObjectType, self).tabComplete(arg0, arg1, arg2))

    @overload
    def registerField(self, arg0: str, arg1: 'ObjectField'):
        """public void dev.ultreon.quantum.api.commands.variables.ObjectType.registerField(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectField<T, ?>)"""
        super(_ObjectType, self).registerField(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectType.getType()"""
        return 'type.Class'._wrap(super(ObjectType, self).getType())

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
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectType.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(super(_ObjectType, self).get(arg0, arg1))

    @overload
    def getField(self, arg0: str) -> 'ObjectField':
        """public dev.ultreon.quantum.api.commands.variables.ObjectField<T, ?> dev.ultreon.quantum.api.commands.variables.ObjectType.getField(java.lang.String)"""
        return 'ObjectField'._wrap(super(_ObjectType, self).getField(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, *arg1: object):
        """public dev.ultreon.quantum.api.commands.variables.ObjectType(java.lang.String,T...)"""
        val = _ObjectType(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def cast(self, arg0: object) -> object:
        """public T dev.ultreon.quantum.api.commands.variables.ObjectType.cast(java.lang.Object)"""
        return object._wrap(super(_ObjectType, self).cast(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'ObjectType':
        """public static <T> dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectType.get(java.lang.Class<T>)"""
        return ObjectType._wrap(_ObjectType.get(arg0))

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.ObjectType.getName()"""
        return str._wrap(super(ObjectType, self).getName())

    @override
    @overload
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.ObjectType.getObjectType()"""
        return 'ObjectType'._wrap(super(ObjectType, self).getObjectType())

    @overload
    def isInstance(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.variables.ObjectType.isInstance(java.lang.Object)"""
        return bool._wrap(super(_ObjectType, self).isInstance(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())


ObjectType.ITEM = ObjectType._wrap(_ITEM.ITEM)

ObjectType.NUMBER = ObjectType._wrap(_NUMBER.NUMBER)

ObjectType.SERVER = ObjectType._wrap(_SERVER.SERVER)

ObjectType.PLAYER_LIST = ObjectType._wrap(_PLAYER_LIST.PLAYER_LIST)

ObjectType.BLOCK = ObjectType._wrap(_BLOCK.BLOCK)

ObjectType.STRING = ObjectType._wrap(_STRING.STRING)

ObjectType.ENTITY = ObjectType._wrap(_ENTITY.ENTITY)

ObjectType.WORLD = ObjectType._wrap(_WORLD.WORLD)

ObjectType.PLAYER = ObjectType._wrap(_PLAYER.PLAYER)

ObjectType.COMMAND = ObjectType._wrap(_COMMAND.COMMAND)

ObjectType.NONE = ObjectType._wrap(_NONE.NONE)

ObjectType.BOOLEAN = ObjectType._wrap(_BOOLEAN.BOOLEAN)

ObjectType.ITEM_STACK = ObjectType._wrap(_ITEM_STACK.ITEM_STACK) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.RootVariableSource
from pyquantum_helper import import_once as _import_once
import java.util.function.Supplier as Supplier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.RootVariableSource as _RootVariableSource
_RootVariableSource = _RootVariableSource
import dev.ultreon.quantum.api.commands.variables.ObjectType as _ObjectType
_ObjectType = _ObjectType
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.api.commands.variables.ObjectSource as _ObjectSource
_ObjectSource = _ObjectSource
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import dev.ultreon.libs.commons.v0.Either as _Either
_Either = _Either
import java.lang.Long as _long
import java.util.function.Supplier as _Supplier
_Supplier = _Supplier
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RootVariableSource():
    """dev.ultreon.quantum.api.commands.variables.RootVariableSource"""
 
    @staticmethod
    def _wrap(java_value: _RootVariableSource) -> 'RootVariableSource':
        return RootVariableSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RootVariableSource):
        """
        Dynamic initializer for RootVariableSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RootVariableSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RootVariableSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.RootVariableSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader)"""
        return object._wrap(super(_RootVariableSource, self).get(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str, arg1: 'ObjectType', arg2: 'Supplier'):
        """public dev.ultreon.quantum.api.commands.variables.RootVariableSource(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectType<T>,java.util.function.Supplier<T>)"""
        val = _RootVariableSource(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'._wrap(super(ObjectSource, self).getType())

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
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.RootVariableSource.getObjectType()"""
        return 'ObjectType'._wrap(super(RootVariableSource, self).getObjectType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getter(self) -> 'Supplier':
        """public java.util.function.Supplier<T> dev.ultreon.quantum.api.commands.variables.RootVariableSource.getter()"""
        return 'Supplier'._wrap(super(RootVariableSource, self).getter())

    @overload
    def __init__(self, arg0: 'ObjectType', arg1: 'Supplier'):
        """public dev.ultreon.quantum.api.commands.variables.RootVariableSource(dev.ultreon.quantum.api.commands.variables.ObjectType<T>,java.util.function.Supplier<T>)"""
        val = _RootVariableSource(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.RootVariableSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'._wrap(super(_RootVariableSource, self).tabComplete(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.PlayerVariables
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.variables.PlayerVariables as _PlayerVariables
_PlayerVariables = _PlayerVariables
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import dev.ultreon.quantum.util.Result as _Result
_Result = _Result
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerVariables():
    """dev.ultreon.quantum.api.commands.variables.PlayerVariables"""
 
    @staticmethod
    def _wrap(java_value: _PlayerVariables) -> 'PlayerVariables':
        return PlayerVariables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerVariables):
        """
        Dynamic initializer for PlayerVariables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerVariables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerVariables__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPlayer(self) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.api.commands.variables.PlayerVariables.getPlayer()"""
        return 'player.ServerPlayer'._wrap(super(PlayerVariables, self).getPlayer())

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
    def setVariable(self, arg0: str, arg1: object):
        """public void dev.ultreon.quantum.api.commands.variables.PlayerVariables.setVariable(java.lang.String,java.lang.Object)"""
        super(_PlayerVariables, self).setVariable(arg0, arg1)

    @staticmethod
    @overload
    def get(arg0: 'ServerPlayer') -> 'PlayerVariables':
        """public static dev.ultreon.quantum.api.commands.variables.PlayerVariables dev.ultreon.quantum.api.commands.variables.PlayerVariables.get(dev.ultreon.quantum.server.player.ServerPlayer)"""
        return PlayerVariables._wrap(_PlayerVariables.get(arg0))

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
    def getVariable(self, arg0: str) -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariable(java.lang.String)"""
        return object._wrap(super(_PlayerVariables, self).getVariable(arg0))

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

    @overload
    def getVariablesByType(self, arg0: 'Class') -> 'Stream':
        """public java.util.stream.Stream<java.lang.String> dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariablesByType(java.lang.Class<?>)"""
        return 'Stream'._wrap(super(_PlayerVariables, self).getVariablesByType(arg0))

    @overload
    def getVariable(self, arg0: str, arg1: 'Class') -> 'util.Result':
        """public <T> dev.ultreon.quantum.util.Result<T> dev.ultreon.quantum.api.commands.variables.PlayerVariables.getVariable(java.lang.String,java.lang.Class<T>)"""
        return 'util.Result'._wrap(super(_PlayerVariables, self).getVariable(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectSources
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.ObjectSources as _ObjectSources
_ObjectSources = _ObjectSources
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectSources():
    """dev.ultreon.quantum.api.commands.variables.ObjectSources"""
 
    @staticmethod
    def _wrap(java_value: _ObjectSources) -> 'ObjectSources':
        return ObjectSources(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectSources):
        """
        Dynamic initializer for ObjectSources.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectSources__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectSources__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.api.commands.variables.SelectorObjectSource<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.api.commands.variables.ObjectSources.PLAYER
    PLAYER: 'SelectorObjectSource' = _wrap(_SelectorObjectSource.PLAYER)


    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.variables.ObjectSources()"""
        val = _ObjectSources()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.variables.ObjectSources()"""
        val = _ObjectSources()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.RootVariables
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.RootVariableSource as _RootVariableSource
_RootVariableSource = _RootVariableSource
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.variables.RootVariables as _RootVariables
_RootVariables = _RootVariables
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RootVariables():
    """dev.ultreon.quantum.api.commands.variables.RootVariables"""
 
    @staticmethod
    def _wrap(java_value: _RootVariables) -> 'RootVariables':
        return RootVariables(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RootVariables):
        """
        Dynamic initializer for RootVariables.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RootVariables__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RootVariables__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.api.commands.variables.RootVariableSource<dev.ultreon.quantum.server.QuantumServer> dev.ultreon.quantum.api.commands.variables.RootVariables.SERVER
    SERVER: 'RootVariableSource' = _wrap(_RootVariableSource.SERVER)


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

    @staticmethod
    @overload
    def names() -> 'Set':
        """public static java.util.Set<java.lang.String> dev.ultreon.quantum.api.commands.variables.RootVariables.names()"""
        return Set._wrap(_RootVariables.names())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.variables.RootVariables()"""
        val = _RootVariables()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.variables.RootVariables()"""
        val = _RootVariables()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def get(arg0: str) -> 'RootVariableSource':
        """public static dev.ultreon.quantum.api.commands.variables.RootVariableSource<?> dev.ultreon.quantum.api.commands.variables.RootVariables.get(java.lang.String)"""
        return RootVariableSource._wrap(_RootVariables.get(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.PlayerVariable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.variables.PlayerVariable as _PlayerVariable
_PlayerVariable = _PlayerVariable
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerVariable():
    """dev.ultreon.quantum.api.commands.variables.PlayerVariable"""
 
    @staticmethod
    def _wrap(java_value: _PlayerVariable) -> 'PlayerVariable':
        return PlayerVariable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerVariable):
        """
        Dynamic initializer for PlayerVariable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerVariable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerVariable__wrapper":
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
    def getValue(self) -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.PlayerVariable.getValue()"""
        return object._wrap(super(PlayerVariable, self).getValue())

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
    def __init__(self, arg0: 'PlayerVariables', arg1: str):
        """public dev.ultreon.quantum.api.commands.variables.PlayerVariable(dev.ultreon.quantum.api.commands.variables.PlayerVariables,java.lang.String)"""
        val = _PlayerVariable(arg0, arg1)
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
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setValue(self, arg0: object):
        """public void dev.ultreon.quantum.api.commands.variables.PlayerVariable.setValue(java.lang.Object)"""
        super(_PlayerVariable, self).setValue(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.ObjectField
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.ObjectType as _ObjectType
_ObjectType = _ObjectType
import dev.ultreon.quantum.api.commands.variables.ObjectField as _ObjectField
_ObjectField = _ObjectField
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.api.commands.variables.ObjectSource as _ObjectSource
_ObjectSource = _ObjectSource
import java.lang.StringBuilder as StringBuilder
import java.util.function.Function as Function
from builtins import bool
import dev.ultreon.libs.commons.v0.Either as _Either
_Either = _Either
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectField():
    """dev.ultreon.quantum.api.commands.variables.ObjectField"""
 
    @staticmethod
    def _wrap(java_value: _ObjectField) -> 'ObjectField':
        return ObjectField(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectField):
        """
        Dynamic initializer for ObjectField.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectField__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectField__wrapper":
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

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'._wrap(super(ObjectSource, self).getType())

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.ObjectField.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(super(_ObjectField, self).get(arg0, arg1))

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.ObjectField.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return 'v0.Either'._wrap(super(_ObjectField, self).tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<R> dev.ultreon.quantum.api.commands.variables.ObjectField.getObjectType()"""
        return 'ObjectType'._wrap(super(ObjectField, self).getObjectType())

    @overload
    def __init__(self, arg0: str, arg1: 'ObjectType', arg2: 'Function'):
        """public dev.ultreon.quantum.api.commands.variables.ObjectField(java.lang.String,dev.ultreon.quantum.api.commands.variables.ObjectType<R>,java.util.function.Function<T, R>)"""
        val = _ObjectField(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def getSource(self) -> 'ObjectSource':
        """public dev.ultreon.quantum.api.commands.variables.ObjectSource<?> dev.ultreon.quantum.api.commands.variables.ObjectField.getSource()"""
        return 'ObjectSource'._wrap(super(ObjectField, self).getSource())

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.ObjectField.getName()"""
        return str._wrap(super(ObjectField, self).getName())

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
    def getter(self) -> 'Function':
        """public java.util.function.Function<T, R> dev.ultreon.quantum.api.commands.variables.ObjectField.getter()"""
        return 'Function'._wrap(super(ObjectField, self).getter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.variables.SelectorObjectSource
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.variables.SelectorObjectSource as _SelectorObjectSource
_SelectorObjectSource = _SelectorObjectSource
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.variables.ObjectType as _ObjectType
_ObjectType = _ObjectType
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = _import_once("pyquantum.api.commands.selector")

import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pycorelibs.commons import v0
except ImportError:
    v0 = _import_once("pycorelibs.commons.v0")

try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import dev.ultreon.quantum.api.commands.selector.SelectorFactory as _SelectorFactory
_SelectorFactory = _SelectorFactory
import dev.ultreon.quantum.api.commands.variables.ObjectSource as _ObjectSource
_ObjectSource = _ObjectSource
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import dev.ultreon.libs.commons.v0.Either as _Either
_Either = _Either
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SelectorObjectSource():
    """dev.ultreon.quantum.api.commands.variables.SelectorObjectSource"""
 
    @staticmethod
    def _wrap(java_value: _SelectorObjectSource) -> 'SelectorObjectSource':
        return SelectorObjectSource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectorObjectSource):
        """
        Dynamic initializer for SelectorObjectSource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectorObjectSource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectorObjectSource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getName()"""
        return str._wrap(super(SelectorObjectSource, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def tabComplete(self, arg0: 'ServerPlayer', arg1: 'CommandReader', arg2: 'StringBuilder') -> 'v0.Either':
        """public dev.ultreon.libs.commons.v0.Either<java.lang.Object, java.util.List<java.lang.String>> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.tabComplete(dev.ultreon.quantum.server.player.ServerPlayer,dev.ultreon.quantum.api.commands.CommandReader,java.lang.StringBuilder)"""
        return 'v0.Either'._wrap(super(_SelectorObjectSource, self).tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self, arg0: 'CommandSender', arg1: 'CommandReader') -> object:
        """public java.lang.Object dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.get(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(super(_SelectorObjectSource, self).get(arg0, arg1))

    @overload
    def getSelectorFactory(self) -> 'selector.SelectorFactory':
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactory<? extends dev.ultreon.quantum.api.commands.selector.BaseSelector<T>> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getSelectorFactory()"""
        return 'selector.SelectorFactory'._wrap(super(SelectorObjectSource, self).getSelectorFactory())

    @override
    @overload
    def getType(self) -> 'type.Class':
        """public default java.lang.Class<T> dev.ultreon.quantum.api.commands.variables.ObjectSource.getType()"""
        return 'type.Class'._wrap(super(ObjectSource, self).getType())

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
    def getObjectType(self) -> 'ObjectType':
        """public dev.ultreon.quantum.api.commands.variables.ObjectType<T> dev.ultreon.quantum.api.commands.variables.SelectorObjectSource.getObjectType()"""
        return 'ObjectType'._wrap(super(SelectorObjectSource, self).getObjectType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: 'Class', arg2: 'SelectorFactory'):
        """public dev.ultreon.quantum.api.commands.variables.SelectorObjectSource(java.lang.String,java.lang.Class<T>,dev.ultreon.quantum.api.commands.selector.SelectorFactory<? extends dev.ultreon.quantum.api.commands.selector.BaseSelector<T>>)"""
        val = _SelectorObjectSource(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())