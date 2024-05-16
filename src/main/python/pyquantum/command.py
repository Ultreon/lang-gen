from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.command.KillCommand as _KillCommand
_KillCommand = _KillCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KillCommand():
    """dev.ultreon.quantum.command.KillCommand"""
 
    @staticmethod
    def _wrap(java_value: _KillCommand) -> 'KillCommand':
        return KillCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KillCommand):
        """
        Dynamic initializer for KillCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KillCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KillCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'._wrap(super(_KillCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_KillCommand, self).execute(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = _KillCommand()
        self.__wrapper = val

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = _KillCommand()
        self.__wrapper = val

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.command.KillCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.command.KillCommand as _KillCommand
_KillCommand = _KillCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KillCommand():
    """dev.ultreon.quantum.command.KillCommand"""
 
    @staticmethod
    def _wrap(java_value: _KillCommand) -> 'KillCommand':
        return KillCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KillCommand):
        """
        Dynamic initializer for KillCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KillCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KillCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'._wrap(super(_KillCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.KillCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_KillCommand, self).execute(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = _KillCommand()
        self.__wrapper = val

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.KillCommand()"""
        val = _KillCommand()
        self.__wrapper = val

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.command.KillCommand 
 
 
# CLASS: dev.ultreon.quantum.command.ChunkCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.command.ChunkCommand as _ChunkCommand
_ChunkCommand = _ChunkCommand
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChunkCommand():
    """dev.ultreon.quantum.command.ChunkCommand"""
 
    @staticmethod
    def _wrap(java_value: _ChunkCommand) -> 'ChunkCommand':
        return ChunkCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChunkCommand):
        """
        Dynamic initializer for ChunkCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChunkCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChunkCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def executeDumpData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.ChunkCommand.executeDumpData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_ChunkCommand, self).executeDumpData(arg0, arg1, arg2))

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.ChunkCommand()"""
        val = _ChunkCommand()
        self.__wrapper = val

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.ChunkCommand()"""
        val = _ChunkCommand()
        self.__wrapper = val

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.GamemodeCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.command.GamemodeCommand as _GamemodeCommand
_GamemodeCommand = _GamemodeCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GamemodeCommand():
    """dev.ultreon.quantum.command.GamemodeCommand"""
 
    @staticmethod
    def _wrap(java_value: _GamemodeCommand) -> 'GamemodeCommand':
        return GamemodeCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GamemodeCommand):
        """
        Dynamic initializer for GamemodeCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GamemodeCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GamemodeCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'GameMode') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GamemodeCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.GameMode)"""
        return 'output.CommandResult'._wrap(super(_GamemodeCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.GamemodeCommand()"""
        val = _GamemodeCommand()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'GameMode') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GamemodeCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.util.GameMode)"""
        return 'output.CommandResult'._wrap(super(_GamemodeCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.GamemodeCommand()"""
        val = _GamemodeCommand()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.GiveCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import dev.ultreon.quantum.command.GiveCommand as _GiveCommand
_GiveCommand = _GiveCommand
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GiveCommand():
    """dev.ultreon.quantum.command.GiveCommand"""
 
    @staticmethod
    def _wrap(java_value: _GiveCommand) -> 'GiveCommand':
        return GiveCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GiveCommand):
        """
        Dynamic initializer for GiveCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GiveCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GiveCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'Item') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GiveCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item)"""
        return 'output.CommandResult'._wrap(super(_GiveCommand, self).execute(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.GiveCommand()"""
        val = _GiveCommand()
        self.__wrapper = val

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: 'Item', arg5: 'Integer') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.GiveCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.item.Item,java.lang.Integer)"""
        return 'output.CommandResult'._wrap(super(_GiveCommand, self).execute(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.GiveCommand()"""
        val = _GiveCommand()
        self.__wrapper = val

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.SetVarCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
try:
    from pyquantum.api.commands import variables
except ImportError:
    variables = _import_once("pyquantum.api.commands.variables")

import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import dev.ultreon.quantum.command.SetVarCommand as _SetVarCommand
_SetVarCommand = _SetVarCommand
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SetVarCommand():
    """dev.ultreon.quantum.command.SetVarCommand"""
 
    @staticmethod
    def _wrap(java_value: _SetVarCommand) -> 'SetVarCommand':
        return SetVarCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SetVarCommand):
        """
        Dynamic initializer for SetVarCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SetVarCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SetVarCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SetVarCommand()"""
        val = _SetVarCommand()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SetVarCommand()"""
        val = _SetVarCommand()
        self.__wrapper = val

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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
    def executeSet(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'PlayerVariable', arg4: object) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SetVarCommand.executeSet(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.api.commands.variables.PlayerVariable,java.lang.Object)"""
        return 'output.CommandResult'._wrap(super(_SetVarCommand, self).executeSet(arg0, arg1, arg2, arg3, arg4))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def executeRun(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'PlayerVariable', arg4: 'CommandResult') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SetVarCommand.executeRun(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.api.commands.variables.PlayerVariable,dev.ultreon.quantum.api.commands.output.CommandResult)"""
        return 'output.CommandResult'._wrap(super(_SetVarCommand, self).executeRun(arg0, arg1, arg2, arg3, arg4))

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.FlyCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.command.FlyCommand as _FlyCommand
_FlyCommand = _FlyCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FlyCommand():
    """dev.ultreon.quantum.command.FlyCommand"""
 
    @staticmethod
    def _wrap(java_value: _FlyCommand) -> 'FlyCommand':
        return FlyCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlyCommand):
        """
        Dynamic initializer for FlyCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlyCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlyCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.FlyCommand()"""
        val = _FlyCommand()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.FlyCommand()"""
        val = _FlyCommand()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_FlyCommand, self).execute(arg0, arg1, arg2))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'._wrap(super(_FlyCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def executeOnPlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: bool) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.FlyCommand.executeOnPlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,boolean)"""
        return 'output.CommandResult'._wrap(super(_FlyCommand, self).executeOnPlayer(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4)))

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.InvincibleCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.command.InvincibleCommand as _InvincibleCommand
_InvincibleCommand = _InvincibleCommand
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvincibleCommand():
    """dev.ultreon.quantum.command.InvincibleCommand"""
 
    @staticmethod
    def _wrap(java_value: _InvincibleCommand) -> 'InvincibleCommand':
        return InvincibleCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvincibleCommand):
        """
        Dynamic initializer for InvincibleCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvincibleCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvincibleCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'._wrap(super(_InvincibleCommand, self).executeCoords(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_InvincibleCommand, self).executeCoords(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.InvincibleCommand()"""
        val = _InvincibleCommand()
        self.__wrapper = val

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.InvincibleCommand()"""
        val = _InvincibleCommand()
        self.__wrapper = val

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player', arg4: bool) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.InvincibleCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player,boolean)"""
        return 'output.CommandResult'._wrap(super(_InvincibleCommand, self).executeCoords(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4)))

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.SummonCommand
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
from builtins import type
import dev.ultreon.quantum.command.SummonCommand as _SummonCommand
_SummonCommand = _SummonCommand
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.Integer as _int
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SummonCommand():
    """dev.ultreon.quantum.command.SummonCommand"""
 
    @staticmethod
    def _wrap(java_value: _SummonCommand) -> 'SummonCommand':
        return SummonCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SummonCommand):
        """
        Dynamic initializer for SummonCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SummonCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SummonCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>)"""
        return 'output.CommandResult'._wrap(super(_SummonCommand, self).execute(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @overload
    def executeWithData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World', arg6: 'DataType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.executeWithData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.DataType<?>)"""
        return 'output.CommandResult'._wrap(super(_SummonCommand, self).executeWithData(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def executeUsingSpawnData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World', arg6: 'DataType') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.executeUsingSpawnData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World,dev.ultreon.ubo.types.DataType<?>)"""
        return 'output.CommandResult'._wrap(super(_SummonCommand, self).executeUsingSpawnData(arg0, arg1, arg2, arg3, arg4, arg5, arg6))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'EntityType', arg4: 'Vec3d', arg5: 'World') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.EntityType<?>,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.World)"""
        return 'output.CommandResult'._wrap(super(_SummonCommand, self).execute(arg0, arg1, arg2, arg3, arg4, arg5))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SummonCommand()"""
        val = _SummonCommand()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SummonCommand()"""
        val = _SummonCommand()
        self.__wrapper = val

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.TimeCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.command.TimeCommand as _TimeCommand
_TimeCommand = _TimeCommand
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TimeCommand():
    """dev.ultreon.quantum.command.TimeCommand"""
 
    @staticmethod
    def _wrap(java_value: _TimeCommand) -> 'TimeCommand':
        return TimeCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimeCommand):
        """
        Dynamic initializer for TimeCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimeCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimeCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def executeSubtract(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeSubtract(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'._wrap(super(_TimeCommand, self).executeSubtract(arg0, arg1, arg2, _int.valueOf(arg3)))

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @overload
    def executeAdd(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeAdd(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'._wrap(super(_TimeCommand, self).executeAdd(arg0, arg1, arg2, _int.valueOf(arg3)))

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.TimeCommand()"""
        val = _TimeCommand()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def executeSet(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: int) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TimeCommand.executeSet(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,int)"""
        return 'output.CommandResult'._wrap(super(_TimeCommand, self).executeSet(arg0, arg1, arg2, _int.valueOf(arg3)))

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.TimeCommand()"""
        val = _TimeCommand()
        self.__wrapper = val

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.TeleportCommand
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
from builtins import type
try:
    from pycorelibs.commons.v0 import vector
except ImportError:
    vector = _import_once("pycorelibs.commons.v0.vector")

import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.command.TeleportCommand as _TeleportCommand
_TeleportCommand = _TeleportCommand
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.Integer as _int
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TeleportCommand():
    """dev.ultreon.quantum.command.TeleportCommand"""
 
    @staticmethod
    def _wrap(java_value: _TeleportCommand) -> 'TeleportCommand':
        return TeleportCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TeleportCommand):
        """
        Dynamic initializer for TeleportCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TeleportCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TeleportCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def executeEntity(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity', arg4: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeEntity(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executeEntity(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @overload
    def executeCoordsInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d', arg4: 'ServerWorld') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeCoordsInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executeCoordsInWorld(arg0, arg1, arg2, arg3, arg4))

    @overload
    def executeRelativeInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d', arg4: 'ServerWorld') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeRelativeInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d,dev.ultreon.quantum.world.ServerWorld)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executeRelativeInWorld(arg0, arg1, arg2, arg3, arg4))

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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
        """public dev.ultreon.quantum.command.TeleportCommand()"""
        val = _TeleportCommand()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.TeleportCommand()"""
        val = _TeleportCommand()
        self.__wrapper = val

    @overload
    def executeCoords(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeCoords(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executeCoords(arg0, arg1, arg2, arg3))

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def executePlayer(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Entity') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executePlayer(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.Entity)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executePlayer(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def executeRelative(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Vec3d') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.TeleportCommand.executeRelative(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.libs.commons.v0.vector.Vec3d)"""
        return 'output.CommandResult'._wrap(super(_TeleportCommand, self).executeRelative(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.WhereAmICommand
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.command.WhereAmICommand as _WhereAmICommand
_WhereAmICommand = _WhereAmICommand
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WhereAmICommand():
    """dev.ultreon.quantum.command.WhereAmICommand"""
 
    @staticmethod
    def _wrap(java_value: _WhereAmICommand) -> 'WhereAmICommand':
        return WhereAmICommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WhereAmICommand):
        """
        Dynamic initializer for WhereAmICommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WhereAmICommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WhereAmICommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.WhereAmICommand()"""
        val = _WhereAmICommand()
        self.__wrapper = val

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.WhereAmICommand()"""
        val = _WhereAmICommand()
        self.__wrapper = val

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def executeCoordsInWorld(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.WhereAmICommand.executeCoordsInWorld(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_WhereAmICommand, self).executeCoordsInWorld(arg0, arg1, arg2))

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.PlayerCommand
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.command.PlayerCommand as _PlayerCommand
_PlayerCommand = _PlayerCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerCommand():
    """dev.ultreon.quantum.command.PlayerCommand"""
 
    @staticmethod
    def _wrap(java_value: _PlayerCommand) -> 'PlayerCommand':
        return PlayerCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerCommand):
        """
        Dynamic initializer for PlayerCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.PlayerCommand()"""
        val = _PlayerCommand()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.PlayerCommand()"""
        val = _PlayerCommand()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @overload
    def executeDumpData(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Player') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.PlayerCommand.executeDumpData(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.entity.player.Player)"""
        return 'output.CommandResult'._wrap(super(_PlayerCommand, self).executeDumpData(arg0, arg1, arg2, arg3))

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.command.SummonItemCommand
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.command.SummonItemCommand as _SummonItemCommand
_SummonItemCommand = _SummonItemCommand
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.Command as _Command
_Command = _Command
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SummonItemCommand():
    """dev.ultreon.quantum.command.SummonItemCommand"""
 
    @staticmethod
    def _wrap(java_value: _SummonItemCommand) -> 'SummonItemCommand':
        return SummonItemCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SummonItemCommand):
        """
        Dynamic initializer for SummonItemCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SummonItemCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SummonItemCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_commands.Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_commands.Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_commands.Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).outdated())

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).wip())

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

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getIncompleteCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getIncompleteCount()"""
        return int._wrap(_Command.getIncompleteCount())

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(commands.Command, self).getRequiredPermission())

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(commands.Command, self).getRequiresOperator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def execute(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'Item') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.command.SummonItemCommand.execute(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,dev.ultreon.quantum.item.Item)"""
        return 'output.CommandResult'._wrap(super(_SummonItemCommand, self).execute(arg0, arg1, arg2, arg3))

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(commands.Command, self).incomplete()

    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(commands.Command, self).requireLivingEntity()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(commands.Command, self).deprecated())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_commands.Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.command.SummonItemCommand()"""
        val = _SummonItemCommand()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.command.SummonItemCommand()"""
        val = _SummonItemCommand()
        self.__wrapper = val

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_commands.Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def data(self) -> 'commands.CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'commands.CommandData'._wrap(super(commands.Command, self).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())