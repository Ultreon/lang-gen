from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.world.Location as _Location
_Location = _Location
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.server.ConsoleCommandSender as _ConsoleCommandSender
_ConsoleCommandSender = _ConsoleCommandSender
from builtins import bool
import java.lang.Long as _long
import java.util.UUID as _UUID
_UUID = _UUID
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConsoleCommandSender():
    """dev.ultreon.quantum.server.ConsoleCommandSender"""
 
    @staticmethod
    def _wrap(java_value: _ConsoleCommandSender) -> 'ConsoleCommandSender':
        return ConsoleCommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConsoleCommandSender):
        """
        Dynamic initializer for ConsoleCommandSender.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConsoleCommandSender__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConsoleCommandSender__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.ConsoleCommandSender.getUuid()"""
        return 'UUID'._wrap(super(ConsoleCommandSender, self).getUuid())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = _ConsoleCommandSender()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getPublicName()"""
        return str._wrap(super(ConsoleCommandSender, self).getPublicName())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getName()"""
        return str._wrap(super(ConsoleCommandSender, self).getName())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_ConsoleCommandSender, self).sendMessage(arg0)

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
    def hasPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(java.lang.String)"""
        super(_ConsoleCommandSender, self).sendMessage(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.server.ConsoleCommandSender.getDisplayName()"""
        return 'text.TextObject'._wrap(super(ConsoleCommandSender, self).getDisplayName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.server.ConsoleCommandSender.getLocation()"""
        return 'world.Location'._wrap(super(ConsoleCommandSender, self).getLocation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = _ConsoleCommandSender()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.isAdmin()"""
        return bool._wrap(super(ConsoleCommandSender, self).isAdmin())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.server.ConsoleCommandSender
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import dev.ultreon.quantum.world.Location as _Location
_Location = _Location
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.server.ConsoleCommandSender as _ConsoleCommandSender
_ConsoleCommandSender = _ConsoleCommandSender
from builtins import bool
import java.lang.Long as _long
import java.util.UUID as _UUID
_UUID = _UUID
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConsoleCommandSender():
    """dev.ultreon.quantum.server.ConsoleCommandSender"""
 
    @staticmethod
    def _wrap(java_value: _ConsoleCommandSender) -> 'ConsoleCommandSender':
        return ConsoleCommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConsoleCommandSender):
        """
        Dynamic initializer for ConsoleCommandSender.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConsoleCommandSender__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConsoleCommandSender__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.ConsoleCommandSender.getUuid()"""
        return 'UUID'._wrap(super(ConsoleCommandSender, self).getUuid())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = _ConsoleCommandSender()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getPublicName()"""
        return str._wrap(super(ConsoleCommandSender, self).getPublicName())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getName()"""
        return str._wrap(super(ConsoleCommandSender, self).getName())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(_ConsoleCommandSender, self).sendMessage(arg0)

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
    def hasPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(java.lang.String)"""
        super(_ConsoleCommandSender, self).sendMessage(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.server.ConsoleCommandSender.getDisplayName()"""
        return 'text.TextObject'._wrap(super(ConsoleCommandSender, self).getDisplayName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.server.ConsoleCommandSender.getLocation()"""
        return 'world.Location'._wrap(super(ConsoleCommandSender, self).getLocation())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = _ConsoleCommandSender()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.isAdmin()"""
        return bool._wrap(super(ConsoleCommandSender, self).isAdmin())

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_commands.CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.server.ConsoleCommandSender 
 
 
# CLASS: dev.ultreon.quantum.server.ServerDisposable
import dev.ultreon.quantum.server.ServerDisposable as _ServerDisposable
_ServerDisposable = _ServerDisposable
from abc import abstractmethod, ABC
 
class ServerDisposable():
    """dev.ultreon.quantum.server.ServerDisposable"""
 
    @staticmethod
    def _wrap(java_value: _ServerDisposable) -> 'ServerDisposable':
        return ServerDisposable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerDisposable):
        """
        Dynamic initializer for ServerDisposable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerDisposable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerDisposable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def dispose(self, ):
        """public abstract void dev.ultreon.quantum.server.ServerDisposable.dispose()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.PlayerManager
from pyquantum_helper import import_once as _import_once
import java.net.Socket as Socket
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.server.PlayerManager as _PlayerManager
_PlayerManager = _PlayerManager
import java.lang.String as _string
import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.net.Socket as _Socket
_Socket = _Socket
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerManager():
    """dev.ultreon.quantum.server.PlayerManager"""
 
    @staticmethod
    def _wrap(java_value: _PlayerManager) -> 'PlayerManager':
        return PlayerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerManager):
        """
        Dynamic initializer for PlayerManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def byName(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.byName(java.lang.String)"""
        return 'player.ServerPlayer'._wrap(super(_PlayerManager, self).byName(arg0))

    @overload
    def byUuid(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.byUuid(java.util.UUID)"""
        return 'player.ServerPlayer'._wrap(super(_PlayerManager, self).byUuid(arg0))

    @overload
    def onJoin(self, arg0: 'Socket', arg1: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.PlayerManager.onJoin(java.net.Socket,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_PlayerManager, self).onJoin(arg0, arg1)

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.server.PlayerManager(dev.ultreon.quantum.server.QuantumServer)"""
        val = _PlayerManager(arg0)
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
    def getServer(self) -> 'QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.PlayerManager.getServer()"""
        return 'QuantumServer'._wrap(super(PlayerManager, self).getServer())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def bySocket(self, arg0: 'Socket') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.bySocket(java.net.Socket)"""
        return 'player.ServerPlayer'._wrap(super(_PlayerManager, self).bySocket(arg0))

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
    def getSocket(self, arg0: 'ServerPlayer') -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.server.PlayerManager.getSocket(dev.ultreon.quantum.server.player.ServerPlayer)"""
        return 'Socket'._wrap(super(_PlayerManager, self).getSocket(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.server.GameCommands
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.server.GameCommands as _GameCommands
_GameCommands = _GameCommands
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameCommands():
    """dev.ultreon.quantum.server.GameCommands"""
 
    @staticmethod
    def _wrap(java_value: _GameCommands) -> 'GameCommands':
        return GameCommands(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameCommands):
        """
        Dynamic initializer for GameCommands.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameCommands__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameCommands__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.server.GameCommands.register()"""
            _GameCommands.register()

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
        """public dev.ultreon.quantum.server.GameCommands()"""
        val = _GameCommands()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.GameCommands()"""
        val = _GameCommands()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.server.TimeProcessor
import dev.ultreon.quantum.server.TimeProcessor as _TimeProcessor
_TimeProcessor = _TimeProcessor
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeProcessor():
    """dev.ultreon.quantum.server.TimeProcessor"""
 
    @staticmethod
    def _wrap(java_value: _TimeProcessor) -> 'TimeProcessor':
        return TimeProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeProcessor):
        """
        Dynamic initializer for TimeProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def nanosToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.nanosToTicks(double)"""
        return int._wrap(_TimeProcessor.nanosToTicks(_double.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.TimeProcessor()"""
        val = _TimeProcessor()
        self.__wrapper = val

    @staticmethod
    @overload
    def microsToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.microsToTicks(double)"""
        return int._wrap(_TimeProcessor.microsToTicks(_double.valueOf(arg0)))

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
    def millisToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.millisToTicks(double)"""
        return int._wrap(_TimeProcessor.millisToTicks(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def hoursToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.hoursToTicks(double)"""
        return int._wrap(_TimeProcessor.hoursToTicks(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def valueToTicks(arg0: int) -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.valueToTicks(int)"""
        return float._wrap(_TimeProcessor.valueToTicks(_int.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def daysToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.daysToTicks(double)"""
        return int._wrap(_TimeProcessor.daysToTicks(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def secondsToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.secondsToTicks(double)"""
        return int._wrap(_TimeProcessor.secondsToTicks(_double.valueOf(arg0)))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.TimeProcessor()"""
        val = _TimeProcessor()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def now() -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.now()"""
        return float._wrap(_TimeProcessor.now())

    @staticmethod
    @overload
    def minutesToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.minutesToTicks(double)"""
        return int._wrap(_TimeProcessor.minutesToTicks(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ticksToSeconds(arg0: int) -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.ticksToSeconds(int)"""
        return float._wrap(_TimeProcessor.ticksToSeconds(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.server.QuantumServer
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = _import_once("pyquantum.recipe")

import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = _import_once("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as _ServerPlayer
_ServerPlayer = _ServerPlayer
import java.lang.Boolean as _boolean
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = _import_once("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
import dev.ultreon.quantum.world.WorldStorage as _WorldStorage
_WorldStorage = _WorldStorage
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = _import_once("pyquantum.gamerule")

import dev.ultreon.quantum.server.player.CacheablePlayer as _CacheablePlayer
_CacheablePlayer = _CacheablePlayer
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
import java.lang.Object as _object
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.util.Collection as _Collection
_Collection = _Collection
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.concurrent.CompletableFuture as _CompletableFuture
_CompletableFuture = _CompletableFuture
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
try:
    from pyquantum.network import system
except ImportError:
    system = _import_once("pyquantum.network.system")

import dev.ultreon.quantum.util.PollingExecutorService as _PollingExecutorService
_PollingExecutorService = _PollingExecutorService
import java.util.UUID as _UUID
_UUID = _UUID
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
from abc import abstractmethod, ABC
import dev.ultreon.quantum.server.PlayerManager as _PlayerManager
_PlayerManager = _PlayerManager
import java.lang.String as _string
import java.lang.Exception as Exception
import dev.ultreon.quantum.network.Networker as _Networker
_Networker = _Networker
import dev.ultreon.quantum.server.player.PermissionMap as _PermissionMap
_PermissionMap = _PermissionMap
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.debug.profiler.Profiler as _Profiler
_Profiler = _Profiler
import dev.ultreon.quantum.recipe.RecipeManager as _RecipeManager
_RecipeManager = _RecipeManager
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.server.ServerDisposable as _ServerDisposable
_ServerDisposable = _ServerDisposable
import java.lang.Runnable as Runnable
import dev.ultreon.quantum.gamerule.GameRules as _GameRules
_GameRules = _GameRules
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.resources.ResourceManager as _ResourceManager
_ResourceManager = _ResourceManager
from builtins import object
import dev.ultreon.quantum.server.player.CachedPlayer as _CachedPlayer
_CachedPlayer = _CachedPlayer
try:
    from pyquantum import log
except ImportError:
    log = _import_once("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

try:
    from pyquantum import network
except ImportError:
    network = _import_once("pyquantum.network")

import java.lang.Integer as _int
import java.util.concurrent.ScheduledFuture as _ScheduledFuture
_ScheduledFuture = _ScheduledFuture
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
import java.util.Map as Map
import java.lang.Long as _long
import java.util.List as List
 
class QuantumServer():
    """dev.ultreon.quantum.server.QuantumServer"""
 
    @staticmethod
    def _wrap(java_value: _QuantumServer) -> 'QuantumServer':
        return QuantumServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _QuantumServer):
        """
        Dynamic initializer for QuantumServer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_QuantumServer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_QuantumServer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = _wrap(_log.Logger.LOGGER)


    @overload
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'ServerDisposable'._wrap(super(_QuantumServer, self).disposeOnClose(arg0))

    @abstractmethod
    def crash(self, arg0: 'CrashLog'):
        """public abstract void dev.ultreon.quantum.server.QuantumServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        pass

    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'._wrap(super(QuantumServer, self).getDefaultPermissions())

    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str._wrap(super(QuantumServer, self).getGameVersion())

    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(_QuantumServer, self).onDisconnected(arg0, arg1)

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'._wrap(super(_QuantumServer, self).getPlayer(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'._wrap(super(_QuantumServer, self).getWorld(arg0))

    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int._wrap(super(QuantumServer, self).getCurrentTps())

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'._wrap(super(_QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'._wrap(super(QuantumServer, self).getResourceManager())

    @overload
    def start(self):
        """public void dev.ultreon.quantum.server.QuantumServer.start()"""
        super(QuantumServer, self).start()

    @override
    @overload
    def pollAll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.pollAll()"""
        super(util.PollingExecutorService, self).pollAll()

    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(_QuantumServer, self).handleChunkLoadFailure(arg0, arg1)

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
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool._wrap(super(util.PollingExecutorService, self).isTerminated())

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @abstractmethod
    def getRenderDistance(self, ):
        """public abstract int dev.ultreon.quantum.server.QuantumServer.getRenderDistance()"""
        pass

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int._wrap(_QuantumServer.minutes2ticks(_float.valueOf(arg0)))

    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.QuantumServer.getHost()"""
        return 'UUID'._wrap(super(QuantumServer, self).getHost())

    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'._wrap(super(QuantumServer, self).getPlayers())

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int._wrap(_QuantumServer.hours2ticks(_float.valueOf(arg0)))

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.server.QuantumServer.close()"""
        super(QuantumServer, self).close()

    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'._wrap(super(QuantumServer, self).getWorld())

    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_QuantumServer, self).placePlayer(arg0)

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool._wrap(super(_QuantumServer, self).hasPlayedBefore(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture._wrap(_QuantumServer.invoke(arg0))

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'._wrap(super(_QuantumServer, self).schedule(arg0, _long.valueOf(arg1), arg2))

    @overload
    def onInitialChunksLoaded(self):
        """public void dev.ultreon.quantum.server.QuantumServer.onInitialChunksLoaded()"""
        super(QuantumServer, self).onInitialChunksLoaded()

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool._wrap(super(_util.PollingExecutorService, self).awaitTermination(_long.valueOf(arg0), arg1))

    @abstractmethod
    def fatalCrash(self, arg0: 'Throwable'):
        """public abstract void dev.ultreon.quantum.server.QuantumServer.fatalCrash(java.lang.Throwable)"""
        pass

    @property
    def profiler(self) -> Profiler:
        return Profiler._wrap(super(_PollingExecutorService).profiler())

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.server.QuantumServer.shutdown()"""
        super(QuantumServer, self).shutdown()

    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int._wrap(super(QuantumServer, self).getPort())

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int._wrap(_QuantumServer.seconds2ticks(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object._wrap(_QuantumServer.invokeAndWait(arg0))

    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.server.QuantumServer.save(boolean) throws java.io.IOException"""
        super(_QuantumServer, self).save(_boolean.valueOf(arg0))

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'._wrap(super(_QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0, _long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def get() -> 'QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return QuantumServer._wrap(_QuantumServer.get())

    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int._wrap(super(QuantumServer, self).getMaxPlayers())

    @overload
    def getPlayerManager(self) -> 'PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'PlayerManager'._wrap(super(QuantumServer, self).getPlayerManager())

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'._wrap(super(util.PollingExecutorService, self).shutdownNow())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'._wrap(super(_QuantumServer, self).getPlayer(arg0))

    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(_QuantumServer, self).sendChunk(arg0, arg1)

    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'._wrap(super(QuantumServer, self).getCachedPlayers())

    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'._wrap(super(QuantumServer, self).getStorage())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'._wrap(super(_util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(_QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(QuantumServer, self).load()

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        _QuantumServer.invokeAndWait(arg0)

    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool._wrap(super(QuantumServer, self).isDedicated())

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'._wrap(super(_QuantumServer, self).getCacheablePlayer(arg0))

    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'._wrap(super(QuantumServer, self).getConsoleSender())

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'._wrap(super(_QuantumServer, self).getPlayersInChunk(arg0))

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'._wrap(super(_QuantumServer, self).getCacheablePlayer(arg0))

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'._wrap(super(_QuantumServer, self).getEntity(arg0))

    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isIntegrated()"""
        return bool._wrap(super(QuantumServer, self).isIntegrated())

    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int._wrap(super(QuantumServer, self).getPlayerCount())

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'._wrap(super(_QuantumServer, self).getEntity(_int.valueOf(arg0), arg1))

    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int._wrap(super(QuantumServer, self).getEntityRenderDistance())

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(_util.PollingExecutorService, self).execute(arg0)

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool._wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int._wrap(super(QuantumServer, self).getOnlineTicks())

    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.server.QuantumServer.handleWorldSaveError(java.lang.Exception)"""
        super(_QuantumServer, self).handleWorldSaveError(arg0)

    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(_QuantumServer, self).crash(arg0)

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(QuantumServer, self).run()

    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'._wrap(super(QuantumServer, self).getRecipeManager())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.toString()"""
        return str._wrap(super(QuantumServer, self).toString())

    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'._wrap(super(QuantumServer, self).getNetworker())

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'._wrap(super(_QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @overload
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool._wrap(super(QuantumServer, self).isRunning())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool._wrap(_QuantumServer.isOnServerThread())

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0, arg1))

    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool._wrap(super(QuantumServer, self).isInitialChunksLoaded())

    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'._wrap(super(QuantumServer, self).getWorlds())

    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'._wrap(super(QuantumServer, self).getPlayersByName())

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object._wrap(super(_util.PollingExecutorService, self).invokeAny(arg0, _long.valueOf(arg1), arg2))

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'._wrap(super(_util.PollingExecutorService, self).submit(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'._wrap(super(QuantumServer, self).getGameRules())