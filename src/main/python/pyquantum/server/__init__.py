from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.server.ConsoleCommandSender as __ConsoleCommandSender
__ConsoleCommandSender = __ConsoleCommandSender
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConsoleCommandSender(api.__CommandSender, commands.CommandSender):
    """dev.ultreon.quantum.server.ConsoleCommandSender"""
 
    @staticmethod
    def __wrap(java_value: __ConsoleCommandSender) -> 'ConsoleCommandSender':
        return ConsoleCommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConsoleCommandSender):
        """
        Dynamic initializer for ConsoleCommandSender.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(java.lang.String)"""
        super(__ConsoleCommandSender, self).sendMessage(arg0)

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasPermission(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = __ConsoleCommandSender()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getPublicName()"""
        return str.__wrap(super(ConsoleCommandSender, self).getPublicName())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__ConsoleCommandSender, self).sendMessage(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.server.ConsoleCommandSender.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(ConsoleCommandSender, self).getDisplayName())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = __ConsoleCommandSender()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.isAdmin()"""
        return bool.__wrap(super(ConsoleCommandSender, self).isAdmin())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.server.ConsoleCommandSender.getLocation()"""
        return 'world.Location'.__wrap(super(ConsoleCommandSender, self).getLocation())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getName()"""
        return str.__wrap(super(ConsoleCommandSender, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.ConsoleCommandSender.getUuid()"""
        return 'UUID'.__wrap(super(ConsoleCommandSender, self).getUuid())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.server.ConsoleCommandSender
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import java.util.UUID as UUID
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

import dev.ultreon.quantum.world.Location as __Location
__Location = __Location
import java.lang.Long as __long
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.server.ConsoleCommandSender as __ConsoleCommandSender
__ConsoleCommandSender = __ConsoleCommandSender
import java.lang.String as __String
__String = __String
import java.util.UUID as __UUID
__UUID = __UUID
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ConsoleCommandSender(api.__CommandSender, commands.CommandSender):
    """dev.ultreon.quantum.server.ConsoleCommandSender"""
 
    @staticmethod
    def __wrap(java_value: __ConsoleCommandSender) -> 'ConsoleCommandSender':
        return ConsoleCommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConsoleCommandSender):
        """
        Dynamic initializer for ConsoleCommandSender.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sendMessage(self, arg0: str):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(java.lang.String)"""
        super(__ConsoleCommandSender, self).sendMessage(arg0)

    @overload
    def hasExplicitPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasPermission(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = __ConsoleCommandSender()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasPermission(arg0))

    @override
    @overload
    def getPublicName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getPublicName()"""
        return str.__wrap(super(ConsoleCommandSender, self).getPublicName())

    @override
    @overload
    def sendMessage(self, arg0: 'TextObject'):
        """public void dev.ultreon.quantum.server.ConsoleCommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        super(__ConsoleCommandSender, self).sendMessage(arg0)

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__ConsoleCommandSender, self).hasExplicitPermission(arg0))

    @override
    @overload
    def getDisplayName(self) -> 'text.TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.server.ConsoleCommandSender.getDisplayName()"""
        return 'text.TextObject'.__wrap(super(ConsoleCommandSender, self).getDisplayName())

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.CommandSender, self).execute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.ConsoleCommandSender()"""
        val = __ConsoleCommandSender()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isAdmin(self) -> bool:
        """public boolean dev.ultreon.quantum.server.ConsoleCommandSender.isAdmin()"""
        return bool.__wrap(super(ConsoleCommandSender, self).isAdmin())

    @override
    @overload
    def getLocation(self) -> 'world.Location':
        """public dev.ultreon.quantum.world.Location dev.ultreon.quantum.server.ConsoleCommandSender.getLocation()"""
        return 'world.Location'.__wrap(super(ConsoleCommandSender, self).getLocation())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.ConsoleCommandSender.getName()"""
        return str.__wrap(super(ConsoleCommandSender, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getUuid(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.ConsoleCommandSender.getUuid()"""
        return 'UUID'.__wrap(super(ConsoleCommandSender, self).getUuid())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.server.ConsoleCommandSender 
 
 
# CLASS: dev.ultreon.quantum.server.ServerDisposable
import dev.ultreon.quantum.server.ServerDisposable as __ServerDisposable
__ServerDisposable = __ServerDisposable
from abc import abstractmethod, ABC
 
class ServerDisposable(ABC):
    """dev.ultreon.quantum.server.ServerDisposable"""
 
    @staticmethod
    def __wrap(java_value: __ServerDisposable) -> 'ServerDisposable':
        return ServerDisposable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerDisposable):
        """
        Dynamic initializer for ServerDisposable.
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
    def dispose(self, ):
        """public abstract void dev.ultreon.quantum.server.ServerDisposable.dispose()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.server.PlayerManager
from pyquantum_helper import import_once as __import_once__
import java.net.Socket as Socket
import java.util.UUID as UUID
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import java.net.Socket as __Socket
__Socket = __Socket
import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.lang.Long as __long
import dev.ultreon.quantum.server.PlayerManager as __PlayerManager
__PlayerManager = __PlayerManager
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerManager():
    """dev.ultreon.quantum.server.PlayerManager"""
 
    @staticmethod
    def __wrap(java_value: __PlayerManager) -> 'PlayerManager':
        return PlayerManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerManager):
        """
        Dynamic initializer for PlayerManager.
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
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.server.PlayerManager(dev.ultreon.quantum.server.QuantumServer)"""
        val = __PlayerManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getServer(self) -> 'QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.PlayerManager.getServer()"""
        return 'QuantumServer'.__wrap(super(PlayerManager, self).getServer())

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

    @overload
    def onJoin(self, arg0: 'Socket', arg1: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.PlayerManager.onJoin(java.net.Socket,dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__PlayerManager, self).onJoin(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def byName(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.byName(java.lang.String)"""
        return 'player.ServerPlayer'.__wrap(super(__PlayerManager, self).byName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def byUuid(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.byUuid(java.util.UUID)"""
        return 'player.ServerPlayer'.__wrap(super(__PlayerManager, self).byUuid(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def bySocket(self, arg0: 'Socket') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.PlayerManager.bySocket(java.net.Socket)"""
        return 'player.ServerPlayer'.__wrap(super(__PlayerManager, self).bySocket(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSocket(self, arg0: 'ServerPlayer') -> 'Socket':
        """public java.net.Socket dev.ultreon.quantum.server.PlayerManager.getSocket(dev.ultreon.quantum.server.player.ServerPlayer)"""
        return 'Socket'.__wrap(super(__PlayerManager, self).getSocket(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.server.GameCommands
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.server.GameCommands as __GameCommands
__GameCommands = __GameCommands
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GameCommands():
    """dev.ultreon.quantum.server.GameCommands"""
 
    @staticmethod
    def __wrap(java_value: __GameCommands) -> 'GameCommands':
        return GameCommands(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameCommands):
        """
        Dynamic initializer for GameCommands.
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

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.server.GameCommands.register()"""
            __GameCommands.register()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.GameCommands()"""
        val = __GameCommands()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.GameCommands()"""
        val = __GameCommands()
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
 
 
# CLASS: dev.ultreon.quantum.server.TimeProcessor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.server.TimeProcessor as __TimeProcessor
__TimeProcessor = __TimeProcessor
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TimeProcessor():
    """dev.ultreon.quantum.server.TimeProcessor"""
 
    @staticmethod
    def __wrap(java_value: __TimeProcessor) -> 'TimeProcessor':
        return TimeProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeProcessor):
        """
        Dynamic initializer for TimeProcessor.
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
        """public dev.ultreon.quantum.server.TimeProcessor()"""
        val = __TimeProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.TimeProcessor()"""
        val = __TimeProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def microsToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.microsToTicks(double)"""
        return int.__wrap(__TimeProcessor.microsToTicks(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def now() -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.now()"""
        return float.__wrap(__TimeProcessor.now())

    @staticmethod
    @overload
    def daysToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.daysToTicks(double)"""
        return int.__wrap(__TimeProcessor.daysToTicks(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def hoursToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.hoursToTicks(double)"""
        return int.__wrap(__TimeProcessor.hoursToTicks(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def nanosToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.nanosToTicks(double)"""
        return int.__wrap(__TimeProcessor.nanosToTicks(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def minutesToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.minutesToTicks(double)"""
        return int.__wrap(__TimeProcessor.minutesToTicks(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def secondsToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.secondsToTicks(double)"""
        return int.__wrap(__TimeProcessor.secondsToTicks(__double.valueOf(arg0)))

    @staticmethod
    @overload
    def ticksToSeconds(arg0: int) -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.ticksToSeconds(int)"""
        return float.__wrap(__TimeProcessor.ticksToSeconds(__int.valueOf(arg0)))

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
    def valueToTicks(arg0: int) -> float:
        """public static double dev.ultreon.quantum.server.TimeProcessor.valueToTicks(int)"""
        return float.__wrap(__TimeProcessor.valueToTicks(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def millisToTicks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.TimeProcessor.millisToTicks(double)"""
        return int.__wrap(__TimeProcessor.millisToTicks(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.server.QuantumServer
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

try:
    from pyquantum import recipe
except ImportError:
    recipe = __import_once__("pyquantum.recipe")

import java.util.concurrent.ScheduledFuture as __ScheduledFuture
__ScheduledFuture = __ScheduledFuture
import java.util.stream.Stream as __Stream
__Stream = __Stream
import dev.ultreon.quantum.debug.profiler.Profiler as __Profiler
__Profiler = __Profiler
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import java.util.Collection as Collection
try:
    from pyquantum import crash
except ImportError:
    crash = __import_once__("pyquantum.crash")

import dev.ultreon.quantum.server.player.ServerPlayer as __ServerPlayer
__ServerPlayer = __ServerPlayer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
try:
    from pyquantum.debug import profiler
except ImportError:
    profiler = __import_once__("pyquantum.debug.profiler")

import java.util.concurrent.Callable as Callable
try:
    from pyquantum import gamerule
except ImportError:
    gamerule = __import_once__("pyquantum.gamerule")

from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.resources.ResourceManager as __ResourceManager
__ResourceManager = __ResourceManager
import java.util.concurrent.CompletableFuture as __CompletableFuture
__CompletableFuture = __CompletableFuture
import java.util.List as __List
__List = __List
import java.lang.Float as __float
import dev.ultreon.quantum.server.PlayerManager as __PlayerManager
__PlayerManager = __PlayerManager
import java.lang.String as __String
__String = __String
import java.util.concurrent.TimeUnit as TimeUnit
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.server.ServerDisposable as __ServerDisposable
__ServerDisposable = __ServerDisposable
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.util.concurrent.CompletableFuture as CompletableFuture
try:
    from pyquantum.network import system
except ImportError:
    system = __import_once__("pyquantum.network.system")

from builtins import int
import java.lang.Boolean as __boolean
import dev.ultreon.quantum.server.player.CachedPlayer as __CachedPlayer
__CachedPlayer = __CachedPlayer
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.quantum.util.PollingExecutorService as __PollingExecutorService
__PollingExecutorService = __PollingExecutorService
from abc import abstractmethod, ABC
import java.lang.Exception as Exception
import dev.ultreon.quantum.recipe.RecipeManager as __RecipeManager
__RecipeManager = __RecipeManager
import dev.ultreon.quantum.gamerule.GameRules as __GameRules
__GameRules = __GameRules
import java.lang.String as __string
import dev.ultreon.quantum.server.player.CacheablePlayer as __CacheablePlayer
__CacheablePlayer = __CacheablePlayer
import java.util.concurrent.ScheduledFuture as ScheduledFuture
import dev.ultreon.quantum.server.player.PermissionMap as __PermissionMap
__PermissionMap = __PermissionMap
from builtins import str
import dev.ultreon.quantum.world.WorldStorage as __WorldStorage
__WorldStorage = __WorldStorage
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Runnable as Runnable
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

from builtins import object
import dev.ultreon.quantum.network.Networker as __Networker
__Networker = __Networker
try:
    from pyquantum import log
except ImportError:
    log = __import_once__("pyquantum.log")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
try:
    from pyquantum import network
except ImportError:
    network = __import_once__("pyquantum.network")

import java.util.UUID as __UUID
__UUID = __UUID
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import java.lang.Throwable as Throwable
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
 
class QuantumServer(ABC, pyquantum.__PollingExecutorService, util.PollingExecutorService, __Runnable, Runnable, pyquantum.__Shutdownable, util.Shutdownable):
    """dev.ultreon.quantum.server.QuantumServer"""
 
    @staticmethod
    def __wrap(java_value: __QuantumServer) -> 'QuantumServer':
        return QuantumServer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __QuantumServer):
        """
        Dynamic initializer for QuantumServer.
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
 
    # public static final dev.ultreon.quantum.log.Logger dev.ultreon.quantum.server.QuantumServer.LOGGER
    LOGGER: 'log.Logger' = __wrap(__log.Logger.LOGGER)


    @overload
    def addPlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.addPlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__QuantumServer, self).addPlayer(arg0)

    @override
    @overload
    def execute(self, arg0: 'Runnable'):
        """public void dev.ultreon.quantum.util.PollingExecutorService.execute(java.lang.Runnable)"""
        super(__util.PollingExecutorService, self).execute(arg0)

    @abstractmethod
    def crash(self, arg0: 'CrashLog'):
        """public abstract void dev.ultreon.quantum.server.QuantumServer.crash(dev.ultreon.quantum.crash.CrashLog)"""
        pass

    @overload
    def getEntityRenderDistance(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getEntityRenderDistance()"""
        return int.__wrap(super(QuantumServer, self).getEntityRenderDistance())

    @overload
    def schedule(self, arg0: 'Runnable', arg1: int, arg2: 'TimeUnit') -> 'ScheduledFuture':
        """public java.util.concurrent.ScheduledFuture<?> dev.ultreon.quantum.server.QuantumServer.schedule(java.lang.Runnable,long,java.util.concurrent.TimeUnit)"""
        return 'ScheduledFuture'.__wrap(super(__QuantumServer, self).schedule(arg0, __long.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Callable') -> object:
        """public static <T> T dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.util.concurrent.Callable<T>)"""
        return object.__wrap(__QuantumServer.invokeAndWait(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def handleWorldSaveError(self, arg0: 'Exception'):
        """public void dev.ultreon.quantum.server.QuantumServer.handleWorldSaveError(java.lang.Exception)"""
        super(__QuantumServer, self).handleWorldSaveError(arg0)

    @overload
    def getDefaultPermissions(self) -> 'player.PermissionMap':
        """public dev.ultreon.quantum.server.player.PermissionMap dev.ultreon.quantum.server.QuantumServer.getDefaultPermissions()"""
        return 'player.PermissionMap'.__wrap(super(QuantumServer, self).getDefaultPermissions())

    @overload
    def getWorlds(self) -> 'Collection':
        """public java.util.Collection<? extends dev.ultreon.quantum.world.World> dev.ultreon.quantum.server.QuantumServer.getWorlds()"""
        return 'Collection'.__wrap(super(QuantumServer, self).getWorlds())

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
    def isRunning(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isRunning()"""
        return bool.__wrap(super(QuantumServer, self).isRunning())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.toString()"""
        return str.__wrap(super(QuantumServer, self).toString())

    @overload
    def submit(self, arg0: 'Runnable', arg1: object) -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable,T)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invoke(arg0: 'Callable') -> 'CompletableFuture':
        """public static <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.server.QuantumServer.invoke(java.util.concurrent.Callable<T>)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @overload
    def getPlayer(self, arg0: str) -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.lang.String)"""
        return 'player.ServerPlayer'.__wrap(super(__QuantumServer, self).getPlayer(arg0))

    @overload
    def getCacheablePlayer(self, arg0: 'UUID') -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.util.UUID)"""
        return 'player.CacheablePlayer'.__wrap(super(__QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def poll(self):
        """public void dev.ultreon.quantum.util.PollingExecutorService.poll()"""
        super(util.PollingExecutorService, self).poll()

    @abstractmethod
    def getRenderDistance(self, ):
        """public abstract int dev.ultreon.quantum.server.QuantumServer.getRenderDistance()"""
        pass

    @overload
    def loadPlayer(self, arg0: str, arg1: 'UUID', arg2: 'IConnection') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.loadPlayer(java.lang.String,java.util.UUID,dev.ultreon.quantum.network.system.IConnection)"""
        return 'player.ServerPlayer'.__wrap(super(__QuantumServer, self).loadPlayer(arg0, arg1, arg2))

    @overload
    def getGameRules(self) -> 'gamerule.GameRules':
        """public dev.ultreon.quantum.gamerule.GameRules dev.ultreon.quantum.server.QuantumServer.getGameRules()"""
        return 'gamerule.GameRules'.__wrap(super(QuantumServer, self).getGameRules())

    @override
    @overload
    def close(self):
        """public void dev.ultreon.quantum.server.QuantumServer.close()"""
        super(QuantumServer, self).close()

    @overload
    def hasPlayedBefore(self, arg0: 'CacheablePlayer') -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.hasPlayedBefore(dev.ultreon.quantum.server.player.CacheablePlayer)"""
        return bool.__wrap(super(__QuantumServer, self).hasPlayedBefore(arg0))

    @overload
    def isInitialChunksLoaded(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isInitialChunksLoaded()"""
        return bool.__wrap(super(QuantumServer, self).isInitialChunksLoaded())

    @overload
    def getWorld(self, arg0: 'Identifier') -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld(dev.ultreon.quantum.util.Identifier)"""
        return 'world.ServerWorld'.__wrap(super(__QuantumServer, self).getWorld(arg0))

    @overload
    def getPlayersByName(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersByName()"""
        return 'Map'.__wrap(super(QuantumServer, self).getPlayersByName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def invoke(arg0: 'Runnable') -> 'CompletableFuture':
        """public static java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.server.QuantumServer.invoke(java.lang.Runnable)"""
        return CompletableFuture.__wrap(__QuantumServer.invoke(arg0))

    @overload
    def placePlayer(self, arg0: 'ServerPlayer'):
        """public void dev.ultreon.quantum.server.QuantumServer.placePlayer(dev.ultreon.quantum.server.player.ServerPlayer)"""
        super(__QuantumServer, self).placePlayer(arg0)

    @overload
    def onInitialChunksLoaded(self):
        """public void dev.ultreon.quantum.server.QuantumServer.onInitialChunksLoaded()"""
        super(QuantumServer, self).onInitialChunksLoaded()

    @staticmethod
    @overload
    def isOnServerThread() -> bool:
        """public static boolean dev.ultreon.quantum.server.QuantumServer.isOnServerThread()"""
        return bool.__wrap(__QuantumServer.isOnServerThread())

    @abstractmethod
    def fatalCrash(self, arg0: 'Throwable'):
        """public abstract void dev.ultreon.quantum.server.QuantumServer.fatalCrash(java.lang.Throwable)"""
        pass

    @overload
    def invokeAny(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException,java.util.concurrent.TimeoutException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0, __long.valueOf(arg1), arg2))

    @override
    @overload
    def shutdown(self):
        """public void dev.ultreon.quantum.server.QuantumServer.shutdown()"""
        super(QuantumServer, self).shutdown()

    @overload
    def getEntity(self, arg0: int, *arg1: 'entity.Entity') -> 'entity.Entity':
        """public final <T extends dev.ultreon.quantum.entity.Entity> T dev.ultreon.quantum.server.QuantumServer.getEntity(int,T...)"""
        return 'entity.Entity'.__wrap(super(__QuantumServer, self).getEntity(__int.valueOf(arg0), arg1))

    @overload
    def getRecipeManager(self) -> 'recipe.RecipeManager':
        """public dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.server.QuantumServer.getRecipeManager()"""
        return 'recipe.RecipeManager'.__wrap(super(QuantumServer, self).getRecipeManager())

    @overload
    def save(self, arg0: bool):
        """public void dev.ultreon.quantum.server.QuantumServer.save(boolean) throws java.io.IOException"""
        super(__QuantumServer, self).save(__boolean.valueOf(arg0))

    @overload
    def invokeAny(self, arg0: 'Collection') -> object:
        """public <T> T dev.ultreon.quantum.util.PollingExecutorService.invokeAny(java.util.Collection<? extends java.util.concurrent.Callable<T>>) throws java.lang.InterruptedException,java.util.concurrent.ExecutionException"""
        return object.__wrap(super(__util.PollingExecutorService, self).invokeAny(arg0))

    @overload
    def getPlayers(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayers()"""
        return 'Collection'.__wrap(super(QuantumServer, self).getPlayers())

    @overload
    def getCachedPlayer(self, arg0: 'UUID') -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.util.UUID)"""
        return 'player.CachedPlayer'.__wrap(super(__QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def getStorage(self) -> 'world.WorldStorage':
        """public dev.ultreon.quantum.world.WorldStorage dev.ultreon.quantum.server.QuantumServer.getStorage()"""
        return 'world.WorldStorage'.__wrap(super(QuantumServer, self).getStorage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getNetworker(self) -> 'network.Networker':
        """public dev.ultreon.quantum.network.Networker dev.ultreon.quantum.server.QuantumServer.getNetworker()"""
        return 'network.Networker'.__wrap(super(QuantumServer, self).getNetworker())

    @overload
    def getPlayersInChunk(self, arg0: 'ChunkPos') -> 'Stream':
        """public java.util.stream.Stream<dev.ultreon.quantum.server.player.ServerPlayer> dev.ultreon.quantum.server.QuantumServer.getPlayersInChunk(dev.ultreon.quantum.world.ChunkPos)"""
        return 'Stream'.__wrap(super(__QuantumServer, self).getPlayersInChunk(arg0))

    @overload
    def submit(self, arg0: 'Runnable') -> 'CompletableFuture':
        """public java.util.concurrent.CompletableFuture<java.lang.Void> dev.ultreon.quantum.util.PollingExecutorService.submit(java.lang.Runnable)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def getGameVersion(self) -> str:
        """public java.lang.String dev.ultreon.quantum.server.QuantumServer.getGameVersion()"""
        return str.__wrap(super(QuantumServer, self).getGameVersion())

    @override
    @overload
    def isShutdown(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isShutdown()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isShutdown())

    @overload
    def getPort(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPort()"""
        return int.__wrap(super(QuantumServer, self).getPort())

    @overload
    def getConsoleSender(self) -> 'commands.CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.server.QuantumServer.getConsoleSender()"""
        return 'commands.CommandSender'.__wrap(super(QuantumServer, self).getConsoleSender())

    @overload
    def getCachedPlayers(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.server.QuantumServer.getCachedPlayers()"""
        return 'List'.__wrap(super(QuantumServer, self).getCachedPlayers())

    @overload
    def isIntegrated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isIntegrated()"""
        return bool.__wrap(super(QuantumServer, self).isIntegrated())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getEntity(self, arg0: 'UUID') -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.server.QuantumServer.getEntity(java.util.UUID)"""
        return 'entity.Entity'.__wrap(super(__QuantumServer, self).getEntity(arg0))

    @overload
    def load(self):
        """public void dev.ultreon.quantum.server.QuantumServer.load() throws java.io.IOException"""
        super(QuantumServer, self).load()

    @staticmethod
    @overload
    def invokeAndWait(arg0: 'Runnable'):
        """public static void dev.ultreon.quantum.server.QuantumServer.invokeAndWait(java.lang.Runnable)"""
        __QuantumServer.invokeAndWait(arg0)

    @overload
    def getOnlineTicks(self) -> int:
        """public long dev.ultreon.quantum.server.QuantumServer.getOnlineTicks()"""
        return int.__wrap(super(QuantumServer, self).getOnlineTicks())

    @overload
    def getResourceManager(self) -> 'resources.ResourceManager':
        """public dev.ultreon.quantum.resources.ResourceManager dev.ultreon.quantum.server.QuantumServer.getResourceManager()"""
        return 'resources.ResourceManager'.__wrap(super(QuantumServer, self).getResourceManager())

    @overload
    def submit(self, arg0: 'Callable') -> 'CompletableFuture':
        """public <T> java.util.concurrent.CompletableFuture<T> dev.ultreon.quantum.util.PollingExecutorService.submit(java.util.concurrent.Callable<T>)"""
        return 'CompletableFuture'.__wrap(super(__util.PollingExecutorService, self).submit(arg0))

    @overload
    def invokeAll(self, arg0: 'Collection', arg1: int, arg2: 'TimeUnit') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>,long,java.util.concurrent.TimeUnit)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0, __long.valueOf(arg1), arg2))

    @overload
    def getMaxPlayers(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getMaxPlayers()"""
        return int.__wrap(super(QuantumServer, self).getMaxPlayers())

    @overload
    def getCacheablePlayer(self, arg0: str) -> 'player.CacheablePlayer':
        """public dev.ultreon.quantum.server.player.CacheablePlayer dev.ultreon.quantum.server.QuantumServer.getCacheablePlayer(java.lang.String)"""
        return 'player.CacheablePlayer'.__wrap(super(__QuantumServer, self).getCacheablePlayer(arg0))

    @override
    @overload
    def isTerminated(self) -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.isTerminated()"""
        return bool.__wrap(super(util.PollingExecutorService, self).isTerminated())

    @staticmethod
    @overload
    def seconds2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.seconds2ticks(float)"""
        return int.__wrap(__QuantumServer.seconds2ticks(__float.valueOf(arg0)))

    @overload
    def handleChunkLoadFailure(self, arg0: 'ChunkPos', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.handleChunkLoadFailure(dev.ultreon.quantum.world.ChunkPos,java.lang.String)"""
        super(__QuantumServer, self).handleChunkLoadFailure(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def minutes2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.minutes2ticks(float)"""
        return int.__wrap(__QuantumServer.minutes2ticks(__float.valueOf(arg0)))

    @property
    def profiler(self) -> Profiler:
        return Profiler.__wrap(super(__PollingExecutorService).profiler())

    @override
    @overload
    def run(self):
        """public void dev.ultreon.quantum.server.QuantumServer.run()"""
        super(QuantumServer, self).run()

    @staticmethod
    @overload
    def get() -> 'QuantumServer':
        """public static dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.server.QuantumServer.get()"""
        return QuantumServer.__wrap(__QuantumServer.get())

    @staticmethod
    @overload
    def hours2ticks(arg0: float) -> int:
        """public static int dev.ultreon.quantum.server.QuantumServer.hours2ticks(float)"""
        return int.__wrap(__QuantumServer.hours2ticks(__float.valueOf(arg0)))

    @overload
    def onDisconnected(self, arg0: 'ServerPlayer', arg1: str):
        """public void dev.ultreon.quantum.server.QuantumServer.onDisconnected(dev.ultreon.quantum.server.player.ServerPlayer,java.lang.String)"""
        super(__QuantumServer, self).onDisconnected(arg0, arg1)

    @override
    @overload
    def shutdownNow(self) -> 'List':
        """public java.util.List<java.lang.Runnable> dev.ultreon.quantum.util.PollingExecutorService.shutdownNow()"""
        return 'List'.__wrap(super(util.PollingExecutorService, self).shutdownNow())

    @overload
    def getHost(self) -> 'UUID':
        """public java.util.UUID dev.ultreon.quantum.server.QuantumServer.getHost()"""
        return 'UUID'.__wrap(super(QuantumServer, self).getHost())

    @overload
    def getCachedPlayer(self, arg0: str) -> 'player.CachedPlayer':
        """public dev.ultreon.quantum.server.player.CachedPlayer dev.ultreon.quantum.server.QuantumServer.getCachedPlayer(java.lang.String)"""
        return 'player.CachedPlayer'.__wrap(super(__QuantumServer, self).getCachedPlayer(arg0))

    @overload
    def getCurrentTps(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getCurrentTps()"""
        return int.__wrap(super(QuantumServer, self).getCurrentTps())

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
    def disposeOnClose(self, arg0: 'ServerDisposable') -> 'ServerDisposable':
        """public <T extends dev.ultreon.quantum.server.ServerDisposable> T dev.ultreon.quantum.server.QuantumServer.disposeOnClose(T)"""
        return 'ServerDisposable'.__wrap(super(__QuantumServer, self).disposeOnClose(arg0))

    @overload
    def getPlayerCount(self) -> int:
        """public int dev.ultreon.quantum.server.QuantumServer.getPlayerCount()"""
        return int.__wrap(super(QuantumServer, self).getPlayerCount())

    @overload
    def getPlayerManager(self) -> 'PlayerManager':
        """public dev.ultreon.quantum.server.PlayerManager dev.ultreon.quantum.server.QuantumServer.getPlayerManager()"""
        return 'PlayerManager'.__wrap(super(QuantumServer, self).getPlayerManager())

    @overload
    def invokeAll(self, arg0: 'Collection') -> 'List':
        """public <T> java.util.List<java.util.concurrent.Future<T>> dev.ultreon.quantum.util.PollingExecutorService.invokeAll(java.util.Collection<? extends java.util.concurrent.Callable<T>>)"""
        return 'List'.__wrap(super(__util.PollingExecutorService, self).invokeAll(arg0))

    @overload
    def crash(self, arg0: 'Throwable'):
        """public void dev.ultreon.quantum.server.QuantumServer.crash(java.lang.Throwable)"""
        super(__QuantumServer, self).crash(arg0)

    @overload
    def awaitTermination(self, arg0: int, arg1: 'TimeUnit') -> bool:
        """public boolean dev.ultreon.quantum.util.PollingExecutorService.awaitTermination(long,java.util.concurrent.TimeUnit) throws java.lang.InterruptedException"""
        return bool.__wrap(super(__util.PollingExecutorService, self).awaitTermination(__long.valueOf(arg0), arg1))

    @overload
    def isDedicated(self) -> bool:
        """public boolean dev.ultreon.quantum.server.QuantumServer.isDedicated()"""
        return bool.__wrap(super(QuantumServer, self).isDedicated())

    @overload
    def sendChunk(self, arg0: 'ChunkPos', arg1: 'Chunk'):
        """public void dev.ultreon.quantum.server.QuantumServer.sendChunk(dev.ultreon.quantum.world.ChunkPos,dev.ultreon.quantum.world.Chunk) throws java.io.IOException"""
        super(__QuantumServer, self).sendChunk(arg0, arg1)

    @overload
    def getPlayer(self, arg0: 'UUID') -> 'player.ServerPlayer':
        """public dev.ultreon.quantum.server.player.ServerPlayer dev.ultreon.quantum.server.QuantumServer.getPlayer(java.util.UUID)"""
        return 'player.ServerPlayer'.__wrap(super(__QuantumServer, self).getPlayer(arg0))

    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.server.QuantumServer.getWorld()"""
        return 'world.ServerWorld'.__wrap(super(QuantumServer, self).getWorld())