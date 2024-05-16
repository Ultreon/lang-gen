from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
import dev.ultreon.quantum.command.KillCommand as __KillCommand
__KillCommand = __KillCommand
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class KillCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.KillCommand"""
 
    @staticmethod
    def __wrap(java_value: __KillCommand) -> 'KillCommand':
        return KillCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KillCommand):
        """
        Dynamic initializer for KillCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = __KillCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__KillCommand, self).execute(arg0, arg1, arg2))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'.__wrap(super(__KillCommand, self).execute(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = __KillCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.command.KillCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
import dev.ultreon.quantum.command.KillCommand as __KillCommand
__KillCommand = __KillCommand
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class KillCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.KillCommand"""
 
    @staticmethod
    def __wrap(java_value: __KillCommand) -> 'KillCommand':
        return KillCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KillCommand):
        """
        Dynamic initializer for KillCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = __KillCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__KillCommand, self).execute(arg0, arg1, arg2))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'.__wrap(super(__KillCommand, self).execute(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = __KillCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.quantum.command.KillCommand 
 
 
# CLASS: dev.ultreon.quantum.command.ChunkCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import dev.ultreon.quantum.command.ChunkCommand as __ChunkCommand
__ChunkCommand = __ChunkCommand
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class ChunkCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.ChunkCommand"""
 
    @staticmethod
    def __wrap(java_value: __ChunkCommand) -> 'ChunkCommand':
        return ChunkCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChunkCommand):
        """
        Dynamic initializer for ChunkCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.ChunkCommand()"""
        val = __ChunkCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def executeDumpData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.ChunkCommand.executeDumpData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__ChunkCommand, self).executeDumpData(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.ChunkCommand()"""
        val = __ChunkCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.command.GamemodeCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import dev.ultreon.quantum.command.GamemodeCommand as __GamemodeCommand
__GamemodeCommand = __GamemodeCommand
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class GamemodeCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.GamemodeCommand"""
 
    @staticmethod
    def __wrap(java_value: __GamemodeCommand) -> 'GamemodeCommand':
        return GamemodeCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GamemodeCommand):
        """
        Dynamic initializer for GamemodeCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'GameMode') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GamemodeCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.GameMode)"""
        return 'output.CommandResult'.__wrap(super(__GamemodeCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'GameMode') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GamemodeCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.util.GameMode)"""
        return 'output.CommandResult'.__wrap(super(__GamemodeCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.GamemodeCommand()"""
        val = __GamemodeCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.GamemodeCommand()"""
        val = __GamemodeCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.command.GiveCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.command.GiveCommand as __GiveCommand
__GiveCommand = __GiveCommand
import java.lang.Integer as Integer
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class GiveCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.GiveCommand"""
 
    @staticmethod
    def __wrap(java_value: __GiveCommand) -> 'GiveCommand':
        return GiveCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GiveCommand):
        """
        Dynamic initializer for GiveCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.GiveCommand()"""
        val = __GiveCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'Item') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GiveCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item)"""
        return 'output.CommandResult'.__wrap(super(__GiveCommand, self).execute(arg0, arg1, arg2, arg3, arg4))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'Item', arg5: 'Integer') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GiveCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,java.lang.Integer)"""
        return 'output.CommandResult'.__wrap(super(__GiveCommand, self).execute(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.GiveCommand()"""
        val = __GiveCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.SetVarCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

try:
    from pyquantum.api.commands import variables
except ImportError:
    variables = __import_once__("pyquantum.api.commands.variables")

import dev.ultreon.quantum.command.SetVarCommand as __SetVarCommand
__SetVarCommand = __SetVarCommand
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class SetVarCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.SetVarCommand"""
 
    @staticmethod
    def __wrap(java_value: __SetVarCommand) -> 'SetVarCommand':
        return SetVarCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SetVarCommand):
        """
        Dynamic initializer for SetVarCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SetVarCommand()"""
        val = __SetVarCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SetVarCommand()"""
        val = __SetVarCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def executeSet(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'PlayerVariable', arg4: object) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SetVarCommand.executeSet(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.api.commands.variables.PlayerVariable,java.lang.Object)"""
        return 'output.CommandResult'.__wrap(super(__SetVarCommand, self).executeSet(arg0, arg1, arg2, arg3, arg4))

    @overload
    def executeRun(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'PlayerVariable', arg4: 'CommandResult') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SetVarCommand.executeRun(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.api.commands.variables.PlayerVariable,dev.ultreon.quantum.api.commands.output.CommandResult)"""
        return 'output.CommandResult'.__wrap(super(__SetVarCommand, self).executeRun(arg0, arg1, arg2, arg3, arg4)) 
 
 
# CLASS: dev.ultreon.quantum.command.FlyCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.command.FlyCommand as __FlyCommand
__FlyCommand = __FlyCommand
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class FlyCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.FlyCommand"""
 
    @staticmethod
    def __wrap(java_value: __FlyCommand) -> 'FlyCommand':
        return FlyCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlyCommand):
        """
        Dynamic initializer for FlyCommand.
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
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__FlyCommand, self).execute(arg0, arg1, arg2))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: bool) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,boolean)"""
        return 'output.CommandResult'.__wrap(super(__FlyCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4)))

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'.__wrap(super(__FlyCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.FlyCommand()"""
        val = __FlyCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.FlyCommand()"""
        val = __FlyCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.command.InvincibleCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.command.InvincibleCommand as __InvincibleCommand
__InvincibleCommand = __InvincibleCommand
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class InvincibleCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.InvincibleCommand"""
 
    @staticmethod
    def __wrap(java_value: __InvincibleCommand) -> 'InvincibleCommand':
        return InvincibleCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvincibleCommand):
        """
        Dynamic initializer for InvincibleCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.InvincibleCommand()"""
        val = __InvincibleCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: bool) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,boolean)"""
        return 'output.CommandResult'.__wrap(super(__InvincibleCommand, self).executeCoords(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__InvincibleCommand, self).executeCoords(arg0, arg1, arg2))

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.InvincibleCommand()"""
        val = __InvincibleCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'.__wrap(super(__InvincibleCommand, self).executeCoords(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.SummonCommand
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.command.SummonCommand as __SummonCommand
__SummonCommand = __SummonCommand
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class SummonCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.SummonCommand"""
 
    @staticmethod
    def __wrap(java_value: __SummonCommand) -> 'SummonCommand':
        return SummonCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SummonCommand):
        """
        Dynamic initializer for SummonCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SummonCommand()"""
        val = __SummonCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SummonCommand()"""
        val = __SummonCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @overload
    def executeUsingSpawnData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World', arg6: 'DataType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.executeUsingSpawnData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.DataType<?>)"""
        return 'output.CommandResult'.__wrap(super(__SummonCommand, self).executeUsingSpawnData(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World)"""
        return 'output.CommandResult'.__wrap(super(__SummonCommand, self).execute(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'output.CommandResult'.__wrap(super(__SummonCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def executeWithData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World', arg6: 'DataType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.executeWithData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.DataType<?>)"""
        return 'output.CommandResult'.__wrap(super(__SummonCommand, self).executeWithData(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.TimeCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import dev.ultreon.quantum.command.TimeCommand as __TimeCommand
__TimeCommand = __TimeCommand
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class TimeCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.TimeCommand"""
 
    @staticmethod
    def __wrap(java_value: __TimeCommand) -> 'TimeCommand':
        return TimeCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimeCommand):
        """
        Dynamic initializer for TimeCommand.
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
    def executeAdd(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeAdd(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'.__wrap(super(__TimeCommand, self).executeAdd(arg0, arg1, arg2, __int.valueOf(arg3)))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.TimeCommand()"""
        val = __TimeCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def executeSubtract(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeSubtract(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'.__wrap(super(__TimeCommand, self).executeSubtract(arg0, arg1, arg2, __int.valueOf(arg3)))

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def executeSet(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeSet(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'.__wrap(super(__TimeCommand, self).executeSet(arg0, arg1, arg2, __int.valueOf(arg3)))

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.TimeCommand()"""
        val = __TimeCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.command.TeleportCommand
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = __import_once__("pycorelibs.commons.v0.vector")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.command.TeleportCommand as __TeleportCommand
__TeleportCommand = __TeleportCommand
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class TeleportCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.TeleportCommand"""
 
    @staticmethod
    def __wrap(java_value: __TeleportCommand) -> 'TeleportCommand':
        return TeleportCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TeleportCommand):
        """
        Dynamic initializer for TeleportCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.TeleportCommand()"""
        val = __TeleportCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.TeleportCommand()"""
        val = __TeleportCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def executeRelativeInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d', arg4: 'ServerWorld') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeRelativeInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executeRelativeInWorld(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def executeEntity(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity', arg4: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeEntity(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executeEntity(arg0, arg1, arg2, arg3, arg4))

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executeCoords(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @overload
    def executeCoordsInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d', arg4: 'ServerWorld') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeCoordsInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executeCoordsInWorld(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def executeRelative(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeRelative(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executeRelative(arg0, arg1, arg2, arg3))

    @overload
    def executePlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executePlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'.__wrap(super(__TeleportCommand, self).executePlayer(arg0, arg1, arg2, arg3))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.WhereAmICommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.command.WhereAmICommand as __WhereAmICommand
__WhereAmICommand = __WhereAmICommand
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class WhereAmICommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.WhereAmICommand"""
 
    @staticmethod
    def __wrap(java_value: __WhereAmICommand) -> 'WhereAmICommand':
        return WhereAmICommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WhereAmICommand):
        """
        Dynamic initializer for WhereAmICommand.
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
 
    @overload
    def executeCoordsInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.WhereAmICommand.executeCoordsInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__WhereAmICommand, self).executeCoordsInWorld(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.WhereAmICommand()"""
        val = __WhereAmICommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.WhereAmICommand()"""
        val = __WhereAmICommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.PlayerCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.command.PlayerCommand as __PlayerCommand
__PlayerCommand = __PlayerCommand
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class PlayerCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.PlayerCommand"""
 
    @staticmethod
    def __wrap(java_value: __PlayerCommand) -> 'PlayerCommand':
        return PlayerCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerCommand):
        """
        Dynamic initializer for PlayerCommand.
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
        """public dev.ultreon.quantum.command.PlayerCommand()"""
        val = __PlayerCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @overload
    def executeDumpData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.PlayerCommand.executeDumpData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'.__wrap(super(__PlayerCommand, self).executeDumpData(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.PlayerCommand()"""
        val = __PlayerCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.command.SummonItemCommand
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import dev.ultreon.quantum.command.SummonItemCommand as __SummonItemCommand
__SummonItemCommand = __SummonItemCommand
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class SummonItemCommand(api.__Command, commands.Command):
    """dev.ultreon.quantum.command.SummonItemCommand"""
 
    @staticmethod
    def __wrap(java_value: __SummonItemCommand) -> 'SummonItemCommand':
        return SummonItemCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SummonItemCommand):
        """
        Dynamic initializer for SummonItemCommand.
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
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'.__wrap(super(commands.Command, self).data())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__commands.Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__commands.Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__commands.Command, self).setNeedPlayer(__boolean.valueOf(arg0))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            __Command.runCommandLoaders()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).deprecated())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SummonItemCommand()"""
        val = __SummonItemCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).wip())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(commands.Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Item') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonItemCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.item.Item)"""
        return 'output.CommandResult'.__wrap(super(__SummonItemCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(commands.Command, self).outdated())

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

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int.__wrap(__Command.getIncompleteCount())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SummonItemCommand()"""
        val = __SummonItemCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()