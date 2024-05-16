from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter
__CommandParameter = __CommandParameter
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class CommandParameter(ABC):
    """dev.ultreon.quantum.api.commands.CommandParameter"""
 
    @staticmethod
    def __wrap(java_value: __CommandParameter) -> 'CommandParameter':
        return CommandParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandParameter):
        """
        Dynamic initializer for CommandParameter.
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
    def getTag(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getTag()"""
        pass

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifArgType(arg0))

    @staticmethod
    @overload
    def ofText(arg0: bool, *arg1: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofText(boolean,java.lang.String...)"""
        return CommandParameter.__wrap(__CommandParameter.ofText(__boolean.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ofArgType(arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofArgType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        return CommandParameter.__wrap(__CommandParameter.ofArgType(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), arg5))

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifText(arg0))

    @abstractmethod
    def getComment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getComment()"""
        pass

    @abstractmethod
    def isOptional(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandParameter.isOptional()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter
from builtins import str
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter
__CommandParameter = __CommandParameter
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class CommandParameter(ABC):
    """dev.ultreon.quantum.api.commands.CommandParameter"""
 
    @staticmethod
    def __wrap(java_value: __CommandParameter) -> 'CommandParameter':
        return CommandParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandParameter):
        """
        Dynamic initializer for CommandParameter.
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
    def getTag(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getTag()"""
        pass

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifArgType(arg0))

    @staticmethod
    @overload
    def ofText(arg0: bool, *arg1: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofText(boolean,java.lang.String...)"""
        return CommandParameter.__wrap(__CommandParameter.ofText(__boolean.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def ofArgType(arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofArgType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        return CommandParameter.__wrap(__CommandParameter.ofArgType(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), arg5))

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifText(arg0))

    @abstractmethod
    def getComment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getComment()"""
        pass

    @abstractmethod
    def isOptional(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandParameter.isOptional()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter 
 
 
# CLASS: dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.PositionCommand as __PositionCommand_PositionSelection
__PositionSelection = __PositionCommand_PositionSelection.PositionSelection
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
 
class PositionSelection():
    """dev.ultreon.quantum.api.commands.PositionCommand.PositionSelection"""
 
    @staticmethod
    def __wrap(java_value: __PositionSelection) -> 'PositionSelection':
        return PositionSelection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PositionSelection):
        """
        Dynamic initializer for PositionSelection.
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection()"""
        val = __PositionSelection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def reset(self, arg0: 'World'):
        """public void dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection.reset(dev.ultreon.quantum.world.World)"""
        super(__PositionSelection, self).reset(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection()"""
        val = __PositionSelection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection.getSize()"""
        return int.__wrap(super(PositionSelection, self).getSize())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$EndOfCommand
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_EndOfCommand
__EndOfCommand = __CommandParseException_EndOfCommand.EndOfCommand
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EndOfCommand(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.EndOfCommand"""
 
    @staticmethod
    def __wrap(java_value: __EndOfCommand) -> 'EndOfCommand':
        return EndOfCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EndOfCommand):
        """
        Dynamic initializer for EndOfCommand.
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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$EndOfCommand(int)"""
        val = __EndOfCommand(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParserImpl
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.api.commands.CommandParserImpl as __CommandParserImpl
__CommandParserImpl = __CommandParserImpl
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.util.Set as Set
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class CommandParserImpl():
    """dev.ultreon.quantum.api.commands.CommandParserImpl"""
 
    @staticmethod
    def __wrap(java_value: __CommandParserImpl) -> 'CommandParserImpl':
        return CommandParserImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandParserImpl):
        """
        Dynamic initializer for CommandParserImpl.
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
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandParserImpl.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__CommandParserImpl, self).tabComplete(arg0, arg1, arg2, arg3))

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

    @property
    def data(self) -> CommandData:
        return CommandData.__wrap(super(__CommandParserImpl).data())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Class', arg1: 'CommandData', arg2: 'Set'):
        """public dev.ultreon.quantum.api.commands.CommandParserImpl(java.lang.Class<? extends dev.ultreon.quantum.api.commands.Command>,dev.ultreon.quantum.api.commands.CommandData,java.util.Set<dev.ultreon.quantum.api.commands.CommandSpec>)"""
        val = __CommandParserImpl(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def execute(self, arg0: 'Command', arg1: 'CommandSender', arg2: 'CommandContext', arg3: str, arg4: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandParserImpl.execute(dev.ultreon.quantum.api.commands.Command,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'output.CommandResult'.__wrap(super(__CommandParserImpl, self).execute(arg0, arg1, arg2, arg3, arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.IndexedCommandSpecValues
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import type
import java.util.Collection as Collection
import dev.ultreon.quantum.api.commands.IndexedCommandSpecValues as __IndexedCommandSpecValues
__IndexedCommandSpecValues = __IndexedCommandSpecValues
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import dev.ultreon.quantum.api.commands.CommandSpecValues as __CommandSpecValues
__CommandSpecValues = __CommandSpecValues
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class IndexedCommandSpecValues(__Iterable, Iterable):
    """dev.ultreon.quantum.api.commands.IndexedCommandSpecValues"""
 
    @staticmethod
    def __wrap(java_value: __IndexedCommandSpecValues) -> 'IndexedCommandSpecValues':
        return IndexedCommandSpecValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndexedCommandSpecValues):
        """
        Dynamic initializer for IndexedCommandSpecValues.
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
    def get(self, arg0: int) -> 'CommandSpecValues':
        """public dev.ultreon.quantum.api.commands.CommandSpecValues dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.get(int)"""
        return 'CommandSpecValues'.__wrap(super(__IndexedCommandSpecValues, self).get(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues()"""
        val = __IndexedCommandSpecValues()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues()"""
        val = __IndexedCommandSpecValues()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def has(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.has(int)"""
        return bool.__wrap(super(__IndexedCommandSpecValues, self).has(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isBlank(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.isBlank()"""
        return bool.__wrap(super(IndexedCommandSpecValues, self).isBlank())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.toString()"""
        return str.__wrap(super(IndexedCommandSpecValues, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.hashCode()"""
        return int.__wrap(super(IndexedCommandSpecValues, self).hashCode())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry> dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.iterator()"""
        return 'Iterator'.__wrap(super(IndexedCommandSpecValues, self).iterator())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.api.commands.CommandSpecValues> dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.values()"""
        return 'Collection'.__wrap(super(IndexedCommandSpecValues, self).values())

    @overload
    def set(self, arg0: int, arg1: 'CommandSpecValues'):
        """public void dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.set(int,dev.ultreon.quantum.api.commands.CommandSpecValues)"""
        super(__IndexedCommandSpecValues, self).set(__int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.equals(java.lang.Object)"""
        return bool.__wrap(super(__IndexedCommandSpecValues, self).equals(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCategory
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
import dev.ultreon.quantum.api.commands.CommandCategory as __CommandCategory
__CommandCategory = __CommandCategory
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class CommandCategory(__Enum, Enum):
    """dev.ultreon.quantum.api.commands.CommandCategory"""
 
    @staticmethod
    def __wrap(java_value: __CommandCategory) -> 'CommandCategory':
        return CommandCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandCategory):
        """
        Dynamic initializer for CommandCategory.
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
 
    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.ADMIN
    ADMIN: 'CommandCategory' = __wrap(__CommandCategory.ADMIN)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.TELEPORT
    TELEPORT: 'CommandCategory' = __wrap(__CommandCategory.TELEPORT)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.MINI_GAME
    MINI_GAME: 'CommandCategory' = __wrap(__CommandCategory.MINI_GAME)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.CHEATS
    CHEATS: 'CommandCategory' = __wrap(__CommandCategory.CHEATS)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.EDIT
    EDIT: 'CommandCategory' = __wrap(__CommandCategory.EDIT)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.SPAWN
    SPAWN: 'CommandCategory' = __wrap(__CommandCategory.SPAWN)

    # public static final dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.FUN
    FUN: 'CommandCategory' = __wrap(__CommandCategory.FUN)


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
    def valueOf(arg0: str) -> 'CommandCategory':
        """public static dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.valueOf(java.lang.String)"""
        return CommandCategory.__wrap(__CommandCategory.valueOf(arg0))

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
    def values() -> List['CommandCategory']:
        """public static dev.ultreon.quantum.api.commands.CommandCategory[] dev.ultreon.quantum.api.commands.CommandCategory.values()"""
        return List[CommandCategory].__wrap(__CommandCategory.values()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Command
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

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
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class Command(ABC):
    """dev.ultreon.quantum.api.commands.Command"""
 
    @staticmethod
    def __wrap(java_value: __Command) -> 'Command':
        return Command(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Command):
        """
        Dynamic initializer for Command.
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
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(Command, self).incomplete()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Command()"""
        val = __Command()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(Command, self).wip())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def data(self) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'CommandData'.__wrap(super(Command, self).data())

    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

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
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__Command, self).warningMessage(arg0, arg1))

    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(Command, self).deprecated())

    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(Command, self).getRequiresOperator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(Command, self).outdated())

    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(Command, self).getRequiredPermission())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Command()"""
        val = __Command()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__Command, self).setNeedPlayer(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(Command, self).requireLivingEntity() 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandStatus
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandStatus as __CommandStatus
__CommandStatus = __CommandStatus
from builtins import int
 
class CommandStatus(__Enum, Enum):
    """dev.ultreon.quantum.api.commands.CommandStatus"""
 
    @staticmethod
    def __wrap(java_value: __CommandStatus) -> 'CommandStatus':
        return CommandStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandStatus):
        """
        Dynamic initializer for CommandStatus.
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
 
    # public static final dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.WIP
    WIP: 'CommandStatus' = __wrap(__CommandStatus.WIP)

    # public static final dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.OUTDATED
    OUTDATED: 'CommandStatus' = __wrap(__CommandStatus.OUTDATED)

    # public static final dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.DEBUG
    DEBUG: 'CommandStatus' = __wrap(__CommandStatus.DEBUG)

    # public static final dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.DONE
    DONE: 'CommandStatus' = __wrap(__CommandStatus.DONE)

    # public static final dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.DEPRECATED
    DEPRECATED: 'CommandStatus' = __wrap(__CommandStatus.DEPRECATED)


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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CommandStatus':
        """public static dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.valueOf(java.lang.String)"""
        return CommandStatus.__wrap(__CommandStatus.valueOf(arg0))

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

    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandStatus.getDescription()"""
        return str.__wrap(super(CommandStatus, self).getDescription())

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
    def values() -> List['CommandStatus']:
        """public static dev.ultreon.quantum.api.commands.CommandStatus[] dev.ultreon.quantum.api.commands.CommandStatus.values()"""
        return List[CommandStatus].__wrap(__CommandStatus.values()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_NotAtStartOfArg
__NotAtStartOfArg = __CommandParseException_NotAtStartOfArg.NotAtStartOfArg
from builtins import int
 
class NotAtStartOfArg(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.NotAtStartOfArg"""
 
    @staticmethod
    def __wrap(java_value: __NotAtStartOfArg) -> 'NotAtStartOfArg':
        return NotAtStartOfArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotAtStartOfArg):
        """
        Dynamic initializer for NotAtStartOfArg.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg(int)"""
        val = __NotAtStartOfArg(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CmdParam
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.api.commands.CmdParam as __CmdParam
__CmdParam = __CmdParam
from abc import abstractmethod, ABC
 
class CmdParam(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.api.commands.CmdParam"""
 
    @staticmethod
    def __wrap(java_value: __CmdParam) -> 'CmdParam':
        return CmdParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CmdParam):
        """
        Dynamic initializer for CmdParam.
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
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotADigit
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_NotADigit
__NotADigit = __CommandParseException_NotADigit.NotADigit
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotADigit(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.NotADigit"""
 
    @staticmethod
    def __wrap(java_value: __NotADigit) -> 'NotADigit':
        return NotADigit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotADigit):
        """
        Dynamic initializer for NotADigit.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotADigit(char)"""
        val = __NotADigit(__char.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotADigit(char,int)"""
        val = __NotADigit(__char.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotANumber
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_NotANumber
__NotANumber = __CommandParseException_NotANumber.NotANumber
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotANumber(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.NotANumber"""
 
    @staticmethod
    def __wrap(java_value: __NotANumber) -> 'NotANumber':
        return NotANumber(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotANumber):
        """
        Dynamic initializer for NotANumber.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotANumber(java.lang.String)"""
        val = __NotANumber(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotANumber(java.lang.String,int)"""
        val = __NotANumber(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.IllegalCommandException
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.IllegalCommandException as __IllegalCommandException
__IllegalCommandException = __IllegalCommandException
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IllegalCommandException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.api.commands.IllegalCommandException"""
 
    @staticmethod
    def __wrap(java_value: __IllegalCommandException) -> 'IllegalCommandException':
        return IllegalCommandException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IllegalCommandException):
        """
        Dynamic initializer for IllegalCommandException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: 'Throwable', arg3: bool, arg4: bool):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,java.lang.Throwable,boolean,boolean)"""
        val = __IllegalCommandException(arg0, arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getCode(self) -> 'MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.IllegalCommandException.getCode()"""
        return 'MessageCode'.__wrap(super(IllegalCommandException, self).getCode())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.Throwable)"""
        val = __IllegalCommandException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'MessageCode'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode)"""
        val = __IllegalCommandException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,java.lang.Throwable)"""
        val = __IllegalCommandException(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        val = __IllegalCommandException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSpecValues
import java.util.function.Predicate as Predicate
from builtins import type
import java.util.stream.Stream as __Stream
__Stream = __Stream
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as __Collection
__Collection = __Collection
import dev.ultreon.quantum.api.commands.CommandSpecValues as __CommandSpecValues
__CommandSpecValues = __CommandSpecValues
import java.lang.Class as __Class
__Class = __Class
import java.util.AbstractCollection as __AbstractCollection
__AbstractCollection = __AbstractCollection
import java.lang.String as __string
from builtins import bool
import java.util.AbstractSet as __AbstractSet
__AbstractSet = __AbstractSet
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.util.HashSet as HashSet
import java.util.function.IntFunction as IntFunction
import java.util.HashSet as __HashSet
__HashSet = __HashSet
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.util.Set as Set
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.util.stream.Stream as Stream
import java.lang.Integer as __int
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class CommandSpecValues(__HashSet, HashSet):
    """dev.ultreon.quantum.api.commands.CommandSpecValues"""
 
    @staticmethod
    def __wrap(java_value: __CommandSpecValues) -> 'CommandSpecValues':
        return CommandSpecValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandSpecValues):
        """
        Dynamic initializer for CommandSpecValues.
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
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str.__wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'.__wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.HashSet.size()"""
        return int.__wrap(super(HashSet, self).size())

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.HashSet.contains(java.lang.Object)"""
        return bool.__wrap(super(__HashSet, self).contains(arg0))

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).retainAll(arg0))

    @overload
    def __init__(self, arg0: 'Set'):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues(java.util.Set<java.lang.String>)"""
        val = __CommandSpecValues(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.HashSet.clone()"""
        return object.__wrap(super(HashSet, self).clone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool.__wrap(super(__AbstractCollection, self).addAll(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractCollection, self).containsAll(arg0))

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.HashSet.remove(java.lang.Object)"""
        return bool.__wrap(super(__HashSet, self).remove(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool.__wrap(super(__AbstractSet, self).removeAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.HashSet.isEmpty()"""
        return bool.__wrap(super(HashSet, self).isEmpty())

    @staticmethod
    @overload
    def newHashSet(arg0: int) -> 'HashSet':
        """public static <T> java.util.HashSet<T> java.util.HashSet.newHashSet(int)"""
        return HashSet.__wrap(__HashSet.newHashSet(__int.valueOf(arg0)))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'.__wrap(super(Collection, self).stream())

    @overload
    def add(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandSpecValues.add(java.lang.String)"""
        return bool.__wrap(super(__CommandSpecValues, self).add(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.HashSet.iterator()"""
        return 'Iterator'.__wrap(super(HashSet, self).iterator())

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues()"""
        val = __CommandSpecValues()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.HashSet.toArray()"""
        return List[object].__wrap(super(HashSet, self).toArray())

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object].__wrap(super(__Collection, self).toArray(arg0))

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.HashSet.toArray(T[])"""
        return List[object].__wrap(super(__HashSet, self).toArray(arg0))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.HashSet.spliterator()"""
        return 'Spliterator'.__wrap(super(HashSet, self).spliterator())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool.__wrap(super(__Collection, self).removeIf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool.__wrap(super(__AbstractSet, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues()"""
        val = __CommandSpecValues()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void java.util.HashSet.clear()"""
        super(HashSet, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int.__wrap(super(AbstractSet, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandArgumentMismatch
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.util.ArrayList as ArrayList
import java.io.OutputStream as OutputStream
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.IllegalArgumentException as IllegalArgumentException
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import dev.ultreon.quantum.api.commands.CommandArgumentMismatch as __CommandArgumentMismatch
__CommandArgumentMismatch = __CommandArgumentMismatch
from builtins import bool
from builtins import int
 
class CommandArgumentMismatch(__IllegalArgumentException, IllegalArgumentException):
    """dev.ultreon.quantum.api.commands.CommandArgumentMismatch"""
 
    @staticmethod
    def __wrap(java_value: __CommandArgumentMismatch) -> 'CommandArgumentMismatch':
        return CommandArgumentMismatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandArgumentMismatch):
        """
        Dynamic initializer for CommandArgumentMismatch.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ArrayList', arg2: 'IllegalArgumentException'):
        """public dev.ultreon.quantum.api.commands.CommandArgumentMismatch(java.lang.Class<?>[],java.util.ArrayList<java.lang.Object>,java.lang.IllegalArgumentException)"""
        val = __CommandArgumentMismatch(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def dumps(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dumps()"""
        return str.__wrap(super(CommandArgumentMismatch, self).dumps())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def dump(self, arg0: 'File'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.File)"""
        super(__CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def dump(self, arg0: 'Writer'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.Writer)"""
        super(__CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def dump(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.OutputStream)"""
        super(__CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandParser as __CommandParser
__CommandParser = __CommandParser
import dev.ultreon.quantum.api.commands.CommandTabCompleter as __CommandTabCompleter
__CommandTabCompleter = __CommandTabCompleter
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter
__CommandParameter = __CommandParameter
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter_ArgumentType
__ArgumentType = __CommandParameter_ArgumentType.ArgumentType
from builtins import int
 
class ArgumentType(__CommandParameter, CommandParameter):
    """dev.ultreon.quantum.api.commands.CommandParameter.ArgumentType"""
 
    @staticmethod
    def __wrap(java_value: __ArgumentType) -> 'ArgumentType':
        return ArgumentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArgumentType):
        """
        Dynamic initializer for ArgumentType.
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
    def getCompleter(self) -> 'CommandTabCompleter':
        """public dev.ultreon.quantum.api.commands.CommandTabCompleter dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getCompleter()"""
        return 'CommandTabCompleter'.__wrap(super(ArgumentType, self).getCompleter())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getType()"""
        return 'type.Class'.__wrap(super(ArgumentType, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getComment()"""
        return str.__wrap(super(ArgumentType, self).getComment())

    @overload
    def __init__(self, arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str):
        """public dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        val = __ArgumentType(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.toString()"""
        return str.__wrap(super(ArgumentType, self).toString())

    @overload
    def getParser(self) -> 'CommandParser':
        """public dev.ultreon.quantum.api.commands.CommandParser<?> dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getParser()"""
        return 'CommandParser'.__wrap(super(ArgumentType, self).getParser())

    @override
    @overload
    def getTag(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getTag()"""
        return str.__wrap(super(ArgumentType, self).getTag())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifArgType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifText(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isOptional(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.isOptional()"""
        return bool.__wrap(super(ArgumentType, self).isOptional())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandTabCompleter
from builtins import str
from abc import abstractmethod, ABC
import dev.ultreon.quantum.api.commands.CommandTabCompleter as __CommandTabCompleter
__CommandTabCompleter = __CommandTabCompleter
 
class CommandTabCompleter(ABC):
    """dev.ultreon.quantum.api.commands.CommandTabCompleter"""
 
    @staticmethod
    def __wrap(java_value: __CommandTabCompleter) -> 'CommandTabCompleter':
        return CommandTabCompleter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandTabCompleter):
        """
        Dynamic initializer for CommandTabCompleter.
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
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'CommandReader', arg3: 'String'):
        """public abstract java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandTabCompleter.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,dev.ultreon.quantum.api.commands.CommandReader,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandData
from pyquantum_helper import import_once as __import_once__
import java.util.function.Predicate as Predicate
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
import dev.ultreon.quantum.api.commands.CommandStatus as __CommandStatus
__CommandStatus = __CommandStatus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.api.commands.CommandParser as __CommandParser
__CommandParser = __CommandParser
import java.util.Set as __Set
__Set = __Set
try:
    from pyquantum import registry
except ImportError:
    registry = __import_once__("pyquantum.registry")

from builtins import object
import dev.ultreon.quantum.api.commands.CommandTabCompleter as __CommandTabCompleter
__CommandTabCompleter = __CommandTabCompleter
from typing import List
import java.lang.Enum as Enum
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandData as __CommandData
__CommandData = __CommandData
import java.util.function.Function as Function
import java.lang.Integer as __int
import java.util.Map as Map
import java.util.List as List
import java.lang.reflect.Method as Method
from builtins import int
 
class CommandData():
    """dev.ultreon.quantum.api.commands.CommandData"""
 
    @staticmethod
    def __wrap(java_value: __CommandData) -> 'CommandData':
        return CommandData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandData):
        """
        Dynamic initializer for CommandData.
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
    def getOverloadDetails(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.api.commands.CommandData.getOverloadDetails()"""
        return 'Collection'.__wrap(super(CommandData, self).getOverloadDetails())

    @overload
    def description(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.description(java.lang.String)"""
        super(__CommandData, self).description(arg0)

    @overload
    def setFlag(self, arg0: 'CommandFlag', arg1: bool):
        """public void dev.ultreon.quantum.api.commands.CommandData.setFlag(dev.ultreon.quantum.api.commands.CommandFlag,boolean)"""
        super(__CommandData, self).setFlag(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getOverloadSpecs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.api.commands.CommandSpec> dev.ultreon.quantum.api.commands.CommandData.getOverloadSpecs()"""
        return 'Set'.__wrap(super(CommandData, self).getOverloadSpecs())

    @overload
    def getCommandSpecs(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.api.commands.CommandSpec> dev.ultreon.quantum.api.commands.CommandData.getCommandSpecs()"""
        return 'Collection'.__wrap(super(CommandData, self).getCommandSpecs())

    @staticmethod
    @overload
    def getType(arg0: str) -> 'type.Class':
        """public static java.lang.Class<?> dev.ultreon.quantum.api.commands.CommandData.getType(java.lang.String)"""
        return type.Class.__wrap(__CommandData.getType(arg0))

    @staticmethod
    @overload
    def validateArgId(arg0: str) -> bool:
        """public static boolean dev.ultreon.quantum.api.commands.CommandData.validateArgId(java.lang.String)"""
        return bool.__wrap(__CommandData.validateArgId(arg0))

    @overload
    def mapToPerm(self, arg0: 'CommandSpec') -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandData.mapToPerm(dev.ultreon.quantum.api.commands.CommandSpec)"""
        return str.__wrap(super(__CommandData, self).mapToPerm(arg0))

    @staticmethod
    @overload
    def readFromEnum(arg0: 'CommandReader', arg1: str, arg2: 'Class') -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T dev.ultreon.quantum.api.commands.CommandData.readFromEnum(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,java.lang.Class<T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return Enum.__wrap(__CommandData.readFromEnum(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def readFromRegistry(arg0: 'CommandReader', arg1: str, arg2: 'Registry') -> object:
        """public static <T> T dev.ultreon.quantum.api.commands.CommandData.readFromRegistry(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,dev.ultreon.quantum.registry.Registry<T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(__CommandData.readFromRegistry(arg0, arg1, arg2))

    @staticmethod
    @overload
    def registerArgument(arg0: str, arg1: 'CommandParser', arg2: 'CommandTabCompleter', *arg3: object):
        """public static <T> void dev.ultreon.quantum.api.commands.CommandData.registerArgument(java.lang.String,dev.ultreon.quantum.api.commands.CommandParser<T>,dev.ultreon.quantum.api.commands.CommandTabCompleter,T...)"""
        __CommandData.registerArgument(arg0, arg1, arg2, arg3)

    @overload
    def sendHelp(self, arg0: str, arg1: 'CommandSender', arg2: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendHelp(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        super(__CommandData, self).sendHelp(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'Command'):
        """public dev.ultreon.quantum.api.commands.CommandData(dev.ultreon.quantum.api.commands.Command)"""
        val = __CommandData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getAliases(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandData.getAliases()"""
        return List[str].__wrap(super(CommandData, self).getAliases())

    @staticmethod
    @overload
    def readFromFunc(arg0: 'CommandReader', arg1: str, arg2: 'Function') -> object:
        """public static <T> T dev.ultreon.quantum.api.commands.CommandData.readFromFunc(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,java.util.function.Function<dev.ultreon.quantum.util.Identifier, T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(__CommandData.readFromFunc(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def completeObject(arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'CommandReader', arg3: 'String') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandData.completeObject(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,dev.ultreon.quantum.api.commands.CommandReader,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return List.__wrap(__CommandData.completeObject(arg0, arg1, arg2, arg3))

    @overload
    def onRegister(self, arg0: 'CommandContext'):
        """public void dev.ultreon.quantum.api.commands.CommandData.onRegister(dev.ultreon.quantum.api.commands.CommandContext)"""
        super(__CommandData, self).onRegister(arg0)

    @overload
    def setCommandStatus(self, arg0: 'CommandStatus'):
        """public void dev.ultreon.quantum.api.commands.CommandData.setCommandStatus(dev.ultreon.quantum.api.commands.CommandStatus)"""
        super(__CommandData, self).setCommandStatus(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getOverloads(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.api.commands.CommandSpec, java.lang.String> dev.ultreon.quantum.api.commands.CommandData.getOverloads()"""
        return 'Map'.__wrap(super(CommandData, self).getOverloads())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def sendUsage(self, arg0: str, arg1: 'CommandSender', arg2: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendUsage(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        super(__CommandData, self).sendUsage(arg0, arg1, arg2)

    @overload
    def mapToMethod(self, arg0: 'CommandSpec') -> 'Method':
        """public java.lang.reflect.Method dev.ultreon.quantum.api.commands.CommandData.mapToMethod(dev.ultreon.quantum.api.commands.CommandSpec)"""
        return 'Method'.__wrap(super(__CommandData, self).mapToMethod(arg0))

    @overload
    def aliases(self, *arg0: str) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.CommandData.aliases(java.lang.String...)"""
        return 'CommandData'.__wrap(super(__CommandData, self).aliases(arg0))

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

    @staticmethod
    @overload
    def readObject(arg0: 'CommandReader') -> object:
        """public static java.lang.Object dev.ultreon.quantum.api.commands.CommandData.readObject(dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object.__wrap(__CommandData.readObject(arg0))

    @overload
    def alias(self, arg0: str) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.CommandData.alias(java.lang.String)"""
        return 'CommandData'.__wrap(super(__CommandData, self).alias(arg0))

    @overload
    def sendUsage(self, arg0: str, arg1: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendUsage(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandData, self).sendUsage(arg0, arg1)

    @staticmethod
    @overload
    def getParser(arg0: str) -> 'CommandParser':
        """public static dev.ultreon.quantum.api.commands.CommandParser<?> dev.ultreon.quantum.api.commands.CommandData.getParser(java.lang.String)"""
        return CommandParser.__wrap(__CommandData.getParser(arg0))

    @overload
    def getStatus(self) -> 'CommandStatus':
        """public dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandData.getStatus()"""
        return 'CommandStatus'.__wrap(super(CommandData, self).getStatus())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def dropLastWhile(arg0: 'List', arg1: 'Predicate') -> 'List':
        """public static <T> java.util.List<T> dev.ultreon.quantum.api.commands.CommandData.dropLastWhile(java.util.List<T>,java.util.function.Predicate<T>)"""
        return List.__wrap(__CommandData.dropLastWhile(arg0, arg1))

    @staticmethod
    @overload
    def getTabCompleter(arg0: str) -> 'CommandTabCompleter':
        """public static dev.ultreon.quantum.api.commands.CommandTabCompleter dev.ultreon.quantum.api.commands.CommandData.getTabCompleter(java.lang.String)"""
        return CommandTabCompleter.__wrap(__CommandData.getTabCompleter(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.DefineCommand
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import dev.ultreon.quantum.api.commands.DefineCommand as __DefineCommand
__DefineCommand = __DefineCommand
from abc import abstractmethod, ABC
 
class DefineCommand(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.api.commands.DefineCommand"""
 
    @staticmethod
    def __wrap(java_value: __DefineCommand) -> 'DefineCommand':
        return DefineCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefineCommand):
        """
        Dynamic initializer for DefineCommand.
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
    def comment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.DefineCommand.comment()"""
        pass

    @abstractmethod
    def value(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.DefineCommand.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Argument
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import dev.ultreon.quantum.api.commands.Argument as __Argument
__Argument = __Argument
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
 
class Argument(ABC):
    """dev.ultreon.quantum.api.commands.Argument"""
 
    @staticmethod
    def __wrap(java_value: __Argument) -> 'Argument':
        return Argument(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Argument):
        """
        Dynamic initializer for Argument.
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
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.api.commands.Argument(T)"""
        val = __Argument(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def get(self) -> object:
        """public T dev.ultreon.quantum.api.commands.Argument.get()"""
        return object.__wrap(super(Argument, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSender
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = __import_once__("pyquantum.api.commands.perms")

import java.lang.String as __string
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import dev.ultreon.quantum.api.commands.output.CommandResult as __CommandResult
__CommandResult = __CommandResult
from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = __import_once__("pyquantum.text")

from builtins import bool
 
class CommandSender(ABC):
    """dev.ultreon.quantum.api.commands.CommandSender"""
 
    @staticmethod
    def __wrap(java_value: __CommandSender) -> 'CommandSender':
        return CommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandSender):
        """
        Dynamic initializer for CommandSender.
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
    def hasExplicitPermission(self, arg0: 'Permission'):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        pass

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'.__wrap(super(__CommandSender, self).execute(arg0, __boolean.valueOf(arg1)))

    @abstractmethod
    def getUuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.api.commands.CommandSender.getUuid()"""
        pass

    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool.__wrap(super(__CommandSender, self).hasPermission(arg0))

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool.__wrap(super(__CommandSender, self).hasExplicitPermission(arg0))

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandSender.getName()"""
        pass

    @abstractmethod
    def isAdmin(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandSender.isAdmin()"""
        pass

    @abstractmethod
    def getPublicName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandSender.getPublicName()"""
        pass

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__CommandSender, self).execute(arg0))

    @abstractmethod
    def sendMessage(self, arg0: 'TextObject'):
        """public abstract void dev.ultreon.quantum.api.commands.CommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        pass

    @abstractmethod
    def getDisplayName(self, ):
        """public abstract dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.commands.CommandSender.getDisplayName()"""
        pass

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool.__wrap(super(__CommandSender, self).hasPermission(arg0))

    @abstractmethod
    def getLocation(self, ):
        """public abstract dev.ultreon.quantum.world.Location dev.ultreon.quantum.api.commands.CommandSender.getLocation()"""
        pass

    @abstractmethod
    def sendMessage(self, arg0: str):
        """public abstract void dev.ultreon.quantum.api.commands.CommandSender.sendMessage(java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandExecuteException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
import dev.ultreon.quantum.api.commands.CommandExecuteException as __CommandExecuteException
__CommandExecuteException = __CommandExecuteException
from builtins import bool
from builtins import int
 
class CommandExecuteException(__Exception, Exception):
    """dev.ultreon.quantum.api.commands.CommandExecuteException"""
 
    @staticmethod
    def __wrap(java_value: __CommandExecuteException) -> 'CommandExecuteException':
        return CommandExecuteException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandExecuteException):
        """
        Dynamic initializer for CommandExecuteException.
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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandExecuteException(java.lang.String)"""
        val = __CommandExecuteException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_EndOfArgument
__EndOfArgument = __CommandParseException_EndOfArgument.EndOfArgument
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EndOfArgument(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.EndOfArgument"""
 
    @staticmethod
    def __wrap(java_value: __EndOfArgument) -> 'EndOfArgument':
        return EndOfArgument(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EndOfArgument):
        """
        Dynamic initializer for EndOfArgument.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument(int)"""
        val = __EndOfArgument(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.ArgumentType$Result
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import dev.ultreon.quantum.api.commands.ArgumentType as __ArgumentType_Result
__Result = __ArgumentType_Result.Result
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Result():
    """dev.ultreon.quantum.api.commands.ArgumentType.Result"""
 
    @staticmethod
    def __wrap(java_value: __Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Result):
        """
        Dynamic initializer for Result.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.ArgumentType$Result.hasError()"""
        return bool.__wrap(super(Result, self).hasError())

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
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = __Result(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(T)"""
        val = __Result(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = __Result(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.api.commands.ArgumentType$Result.get()"""
        return object.__wrap(super(Result, self).get())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.InvalidCommandMethodError
from builtins import str
import dev.ultreon.quantum.api.commands.InvalidCommandMethodError as __InvalidCommandMethodError
__InvalidCommandMethodError = __InvalidCommandMethodError
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.reflect.Method as Method
 
class InvalidCommandMethodError(__Error, Error):
    """dev.ultreon.quantum.api.commands.InvalidCommandMethodError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCommandMethodError) -> 'InvalidCommandMethodError':
        return InvalidCommandMethodError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCommandMethodError):
        """
        Dynamic initializer for InvalidCommandMethodError.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: 'Method', arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.reflect.Method,java.lang.Throwable)"""
        val = __InvalidCommandMethodError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.String)"""
        val = __InvalidCommandMethodError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Method'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.reflect.Method)"""
        val = __InvalidCommandMethodError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.String,java.lang.Throwable)"""
        val = __InvalidCommandMethodError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.Throwable)"""
        val = __InvalidCommandMethodError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Range
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pycorelibs.collections.v0 import iterator
except ImportError:
    iterator = __import_once__("pycorelibs.collections.v0.iterator")

import dev.ultreon.libs.collections.v0.iterator.IntIterator as __IntIterator
__IntIterator = __IntIterator
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = __import_once__("pycorelibs.functions.v0.consumer")

import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import dev.ultreon.libs.collections.v0.iterator.IntIterable as __IntIterable
__IntIterable = __IntIterable
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Range as __Range
__Range = __Range
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class Range(v0.__IntIterable, iterator.IntIterable):
    """dev.ultreon.quantum.api.commands.Range"""
 
    @staticmethod
    def __wrap(java_value: __Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Range):
        """
        Dynamic initializer for Range.
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
    def forEach(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterable.forEach(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(__iterator.IntIterable, self).forEach(arg0)

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.api.commands.Range(int,int,int)"""
        val = __Range(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.Range(int)"""
        val = __Range(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.api.commands.Range(int,int)"""
        val = __Range(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def iterator(self) -> 'iterator.IntIterator':
        """public dev.ultreon.libs.collections.v0.iterator.IntIterator dev.ultreon.quantum.api.commands.Range.iterator()"""
        return 'iterator.IntIterator'.__wrap(super(Range, self).iterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSpec
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.List as __List
__List = __List
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
import dev.ultreon.quantum.api.commands.CommandSpec as __CommandSpec
__CommandSpec = __CommandSpec
from builtins import int
import java.util.List as List
 
class CommandSpec():
    """dev.ultreon.quantum.api.commands.CommandSpec"""
 
    @staticmethod
    def __wrap(java_value: __CommandSpec) -> 'CommandSpec':
        return CommandSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandSpec):
        """
        Dynamic initializer for CommandSpec.
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

    @overload
    def __init__(self, arg0: str, arg1: 'List'):
        """public dev.ultreon.quantum.api.commands.CommandSpec(java.lang.String,java.util.List<dev.ultreon.quantum.api.commands.CommandParameter>)"""
        val = __CommandSpec(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def arguments(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.CommandParameter> dev.ultreon.quantum.api.commands.CommandSpec.arguments()"""
        return 'List'.__wrap(super(CommandSpec, self).arguments())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandSpec.equals(java.lang.Object)"""
        return bool.__wrap(super(__CommandSpec, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandSpec.hashCode()"""
        return int.__wrap(super(CommandSpec, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandSpec.toString()"""
        return str.__wrap(super(CommandSpec, self).toString())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def commandName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandSpec.commandName()"""
        return str.__wrap(super(CommandSpec, self).commandName()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.TabCompleting
from pyquantum_helper import import_once as __import_once__
import java.util.UUID as UUID
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Collection as Collection
try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = __import_once__("pyquantum.api.commands.selector")

import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as __object
import dev.ultreon.quantum.api.commands.TabCompleting as __TabCompleting
__TabCompleting = __TabCompleting
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
try:
    from pyquantum.server import player
except ImportError:
    player = __import_once__("pyquantum.server.player")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.List as List
from builtins import int
 
class TabCompleting():
    """dev.ultreon.quantum.api.commands.TabCompleting"""
 
    @staticmethod
    def __wrap(java_value: __TabCompleting) -> 'TabCompleting':
        return TabCompleting(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TabCompleting):
        """
        Dynamic initializer for TabCompleting.
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
 
    @staticmethod
    @overload
    def forceToString(*arg0: str) -> List[str]:
        """public static java.lang.String[] dev.ultreon.quantum.api.commands.TabCompleting.forceToString(char...)"""
        return List[str].__wrap(__TabCompleting.forceToString(arg0))

    @staticmethod
    @overload
    def doubles(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.doubles(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.doubles(arg0, arg1))

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: str, arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.lang.String,java.lang.String)"""
        __TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: object, arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.lang.Object,java.lang.String)"""
        __TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def players(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.players(java.lang.String)"""
        return List.__wrap(__TabCompleting.players(arg0))

    @staticmethod
    @overload
    def offlinePlayers(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.offlinePlayers(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.offlinePlayers(arg0, arg1))

    @staticmethod
    @overload
    def numbers(arg0: 'List', arg1: str, *arg2: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.util.List<java.lang.String>,java.lang.String,java.lang.Number...)"""
        return List.__wrap(__TabCompleting.numbers(arg0, arg1, arg2))

    @staticmethod
    @overload
    def strings(arg0: 'List', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.util.List<java.lang.String>,java.lang.String,char...)"""
        return List.__wrap(__TabCompleting.strings(arg0, arg1, arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def players(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.players(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.players(arg0, arg1))

    @staticmethod
    @overload
    def biomes(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.biomes(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.biomes(arg0, arg1))

    @staticmethod
    @overload
    def onlinePlayers(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.onlinePlayers(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.onlinePlayers(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def strings(arg0: 'List', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.util.List<java.lang.String>,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.strings(arg0, arg1, arg2))

    @staticmethod
    @overload
    def entityIds(arg0: 'List', arg1: 'ServerWorld', arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityIds(java.util.List<java.lang.String>,dev.ultreon.quantum.world.ServerWorld,java.lang.String)"""
        return List.__wrap(__TabCompleting.entityIds(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def worldIds(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.worldIds(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.worldIds(arg0, arg1))

    @staticmethod
    @overload
    def entityUuids(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityUuids(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.entityUuids(arg0, arg1))

    @staticmethod
    @overload
    def entityTypes(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityTypes(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.entityTypes(arg0, arg1))

    @staticmethod
    @overload
    def difficulties(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.difficulties(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.difficulties(arg0, arg1))

    @staticmethod
    @overload
    def strings(arg0: str, *arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.lang.String,char...)"""
        return List.__wrap(__TabCompleting.strings(arg0, arg1))

    @staticmethod
    @overload
    def worlds(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.worlds(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.worlds(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.TabCompleting()"""
        val = __TabCompleting()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def subCommand(arg0: 'List', arg1: 'CommandSender', arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.subCommand(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.subCommand(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def variables(arg0: 'ArrayList', arg1: str, arg2: 'ServerPlayer', arg3: 'Class') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.variables(java.util.ArrayList<java.lang.Object>,java.lang.String,dev.ultreon.quantum.server.player.ServerPlayer,java.lang.Class<?>)"""
        return List.__wrap(__TabCompleting.variables(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def entityTypes(arg0: 'List', arg1: str, arg2: bool) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityTypes(java.util.List<java.lang.String>,java.lang.String,boolean)"""
        return List.__wrap(__TabCompleting.entityTypes(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def selectors(arg0: 'SelectorKey', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.selectors(arg0, arg1, arg2))

    @staticmethod
    @overload
    def booleans(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.booleans(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.booleans(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def offlinePlayerUuids(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.offlinePlayerUuids(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.offlinePlayerUuids(arg0, arg1))

    @staticmethod
    @overload
    def blocks(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.blocks(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.blocks(arg0, arg1))

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: 'Identifier', arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,dev.ultreon.quantum.util.Identifier,java.lang.String)"""
        __TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def items(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.items(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.items(arg0, arg1))

    @staticmethod
    @overload
    def prefixed(arg0: str, arg1: str, arg2: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List.__wrap(__TabCompleting.prefixed(arg0, arg1, arg2))

    @staticmethod
    @overload
    def entityUuids(arg0: 'List', arg1: str, arg2: 'Class') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityUuids(java.util.List<java.lang.String>,java.lang.String,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return List.__wrap(__TabCompleting.entityUuids(arg0, arg1, arg2))

    @staticmethod
    @overload
    def prefixed(arg0: 'List', arg1: str, arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.util.List<java.lang.String>,java.lang.String,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.prefixed(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def commands(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.commands(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.commands(arg0, arg1))

    @staticmethod
    @overload
    def hex(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.hex(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.hex(arg0, arg1))

    @staticmethod
    @overload
    def mods(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.mods(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.mods(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: 'UUID', arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.util.UUID,java.lang.String)"""
        __TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def numbers(arg0: str, *arg1: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.lang.String,java.lang.Number...)"""
        return List.__wrap(__TabCompleting.numbers(arg0, arg1))

    @staticmethod
    @overload
    def strings(arg0: str, *arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.strings(arg0, arg1))

    @staticmethod
    @overload
    def ints(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.ints(java.util.List<java.lang.String>,java.lang.String)"""
        return List.__wrap(__TabCompleting.ints(arg0, arg1))

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

    @staticmethod
    @overload
    def ruleNames(arg0: 'List', arg1: 'List', arg2: str) -> 'List':
        """public static <T extends dev.ultreon.quantum.gamerule.Rule<?>> java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.ruleNames(java.util.List<java.lang.String>,java.util.List<T>,java.lang.String)"""
        return List.__wrap(__TabCompleting.ruleNames(arg0, arg1, arg2))

    @staticmethod
    @overload
    def selectors(arg0: 'SelectorKey', arg1: str, arg2: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List.__wrap(__TabCompleting.selectors(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.TabCompleting()"""
        val = __TabCompleting()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def keys(arg0: str, arg1: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.keys(java.lang.String,java.util.Collection<dev.ultreon.quantum.util.Identifier>)"""
        return List.__wrap(__TabCompleting.keys(arg0, arg1))

    @staticmethod
    @overload
    def selectors(arg0: 'List', arg1: 'SelectorKey', arg2: str, arg3: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List.__wrap(__TabCompleting.selectors(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def prefixed(arg0: str, arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.lang.String,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.prefixed(arg0, arg1, arg2))

    @staticmethod
    @overload
    def selectors(arg0: 'List', arg1: 'SelectorKey', arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.lang.String...)"""
        return List.__wrap(__TabCompleting.selectors(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def prefixed(arg0: 'List', arg1: str, arg2: str, arg3: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.util.List<java.lang.String>,java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List.__wrap(__TabCompleting.prefixed(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def numbers(arg0: 'List', arg1: str, arg2: int, *arg3: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.util.List<java.lang.String>,java.lang.String,int,java.lang.Number...)"""
        return List.__wrap(__TabCompleting.numbers(arg0, arg1, __int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def onlinePlayers(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.onlinePlayers(java.lang.String)"""
        return List.__wrap(__TabCompleting.onlinePlayers(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.StringIO
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.StringIO as __StringIO
__StringIO = __StringIO
import java.lang.Object as __object
from builtins import type
from typing import List
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
 
class StringIO():
    """dev.ultreon.quantum.api.commands.StringIO"""
 
    @staticmethod
    def __wrap(java_value: __StringIO) -> 'StringIO':
        return StringIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringIO):
        """
        Dynamic initializer for StringIO.
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

    @overload
    def getOffset(self) -> int:
        """public int dev.ultreon.quantum.api.commands.StringIO.getOffset()"""
        return int.__wrap(super(StringIO, self).getOffset())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.StringIO(java.lang.String)"""
        val = __StringIO(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isEOF(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.StringIO.isEOF()"""
        return bool.__wrap(super(StringIO, self).isEOF())

    @overload
    def isNextEOF(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.StringIO.isNextEOF()"""
        return bool.__wrap(super(StringIO, self).isNextEOF())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def readString(self, arg0: int) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.StringIO.readString(int) throws java.io.EOFException"""
        return str.__wrap(super(__StringIO, self).readString(__int.valueOf(arg0)))

    @overload
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.StringIO.readChar() throws java.io.EOFException"""
        return str.__wrap(super(StringIO, self).readChar())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def readChars(self, arg0: int) -> List[str]:
        """public char[] dev.ultreon.quantum.api.commands.StringIO.readChars(int) throws java.io.EOFException"""
        return List[str].__wrap(super(__StringIO, self).readChars(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.OverloadContent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.function.Function as Function
from builtins import bool
import dev.ultreon.quantum.api.commands.OverloadContent as __OverloadContent
__OverloadContent = __OverloadContent
from builtins import int
 
class OverloadContent():
    """dev.ultreon.quantum.api.commands.OverloadContent"""
 
    @staticmethod
    def __wrap(java_value: __OverloadContent) -> 'OverloadContent':
        return OverloadContent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OverloadContent):
        """
        Dynamic initializer for OverloadContent.
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
    def mapSize(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapSize(java.util.function.Function<java.lang.Integer, java.lang.Integer>)"""
        return 'OverloadContent'.__wrap(super(__OverloadContent, self).mapSize(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.OverloadContent.hashCode()"""
        return int.__wrap(super(OverloadContent, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.OverloadContent.toString()"""
        return str.__wrap(super(OverloadContent, self).toString())

    @overload
    def mapIndexedValues(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapIndexedValues(java.util.function.Function<dev.ultreon.quantum.api.commands.IndexedCommandSpecValues, dev.ultreon.quantum.api.commands.IndexedCommandSpecValues>)"""
        return 'OverloadContent'.__wrap(super(__OverloadContent, self).mapIndexedValues(arg0))

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
    def mapName(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapName(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'OverloadContent'.__wrap(super(__OverloadContent, self).mapName(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: 'IndexedCommandSpecValues') -> 'OverloadContent':
        """public static dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.of(java.lang.String,int,dev.ultreon.quantum.api.commands.IndexedCommandSpecValues)"""
        return OverloadContent.__wrap(__OverloadContent.of(arg0, __int.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.OverloadContent.equals(java.lang.Object)"""
        return bool.__wrap(super(__OverloadContent, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: 'IndexedCommandSpecValues'):
        """public dev.ultreon.quantum.api.commands.OverloadContent(java.lang.String,int,dev.ultreon.quantum.api.commands.IndexedCommandSpecValues)"""
        val = __OverloadContent(arg0, __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommandParseException(__Exception, Exception):
    """dev.ultreon.quantum.api.commands.CommandParseException"""
 
    @staticmethod
    def __wrap(java_value: __CommandParseException) -> 'CommandParseException':
        return CommandParseException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandParseException):
        """
        Dynamic initializer for CommandParseException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, arg0: 'CommandError', arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException(dev.ultreon.quantum.api.commands.error.CommandError,int)"""
        val = __CommandParseException(arg0, __int.valueOf(arg1))
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException(java.lang.String)"""
        val = __CommandParseException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException(java.lang.String,int)"""
        val = __CommandParseException(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotFound
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_NotFound
__NotFound = __CommandParseException_NotFound.NotFound
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotFound(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.NotFound"""
 
    @staticmethod
    def __wrap(java_value: __NotFound) -> 'NotFound':
        return NotFound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotFound):
        """
        Dynamic initializer for NotFound.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotFound(java.lang.String,int)"""
        val = __NotFound(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str, arg1: object, arg2: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotFound(java.lang.String,java.lang.Object,int)"""
        val = __NotFound(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.OverloadConflictException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import dev.ultreon.quantum.api.commands.OverloadConflictException as __OverloadConflictException
__OverloadConflictException = __OverloadConflictException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OverloadConflictException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.api.commands.OverloadConflictException"""
 
    @staticmethod
    def __wrap(java_value: __OverloadConflictException) -> 'OverloadConflictException':
        return OverloadConflictException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OverloadConflictException):
        """
        Dynamic initializer for OverloadConflictException.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAliases(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.OverloadConflictException.getAliases()"""
        return List[str].__wrap(super(OverloadConflictException, self).getAliases())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @overload
    def __init__(self, *arg0: str):
        """public dev.ultreon.quantum.api.commands.OverloadConflictException(java.lang.String...)"""
        val = __OverloadConflictException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCrashReport$Details
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandCrashReport as __CommandCrashReport_Details
__Details = __CommandCrashReport_Details.Details
import java.lang.Object as __object
from builtins import type
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
 
class Details():
    """dev.ultreon.quantum.api.commands.CommandCrashReport.Details"""
 
    @staticmethod
    def __wrap(java_value: __Details) -> 'Details':
        return Details(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Details):
        """
        Dynamic initializer for Details.
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
    def report(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.report()"""
        return str.__wrap(super(Details, self).report())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandCrashReport$Details.equals(java.lang.Object)"""
        return bool.__wrap(super(__Details, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.toString()"""
        return str.__wrap(super(Details, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandCrashReport$Details.hashCode()"""
        return int.__wrap(super(Details, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.CommandCrashReport$Details(java.lang.String,java.lang.String)"""
        val = __Details(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.id()"""
        return str.__wrap(super(Details, self).id()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.PositionCommand
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
import dev.ultreon.quantum.api.commands.PositionCommand as __PositionCommand
__PositionCommand = __PositionCommand
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.Command as __Command
__Command = __Command
import java.util.List as List
from builtins import int
 
class PositionCommand(__Command, Command):
    """dev.ultreon.quantum.api.commands.PositionCommand"""
 
    @staticmethod
    def __wrap(java_value: __PositionCommand) -> 'PositionCommand':
        return PositionCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PositionCommand):
        """
        Dynamic initializer for PositionCommand.
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
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(Command, self).requireLivingEntity()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'.__wrap(super(Command, self).outdated())

    @override
    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(Command, self).incomplete()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str.__wrap(super(Command, self).getRequiredPermission())

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'.__wrap(super(__Command, self).onCommand(arg0, arg1, arg2, arg3))

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
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'.__wrap(super(__Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__Command, self).warningMessage(arg0, arg1))

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(__Command, self).setNeedPlayer(__boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def data(self) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'CommandData'.__wrap(super(Command, self).data())

    @overload
    def executeFirst(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.PositionCommand.executeFirst(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__PositionCommand, self).executeFirst(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(__Command, self).setNeedEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'.__wrap(super(Command, self).wip())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(__Command, self).setNeedLivingEntity(__boolean.valueOf(arg0))

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool.__wrap(super(Command, self).getRequiresOperator())

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.PositionCommand()"""
        val = __PositionCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int.__wrap(__Command.getTotalCount())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def executeSecond(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.PositionCommand.executeSecond(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'.__wrap(super(__PositionCommand, self).executeSecond(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.PositionCommand()"""
        val = __PositionCommand()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'.__wrap(super(Command, self).deprecated()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandContext
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandContext as __CommandContext
__CommandContext = __CommandContext
import java.lang.Object as __object
from builtins import type
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
 
class CommandContext():
    """dev.ultreon.quantum.api.commands.CommandContext"""
 
    @staticmethod
    def __wrap(java_value: __CommandContext) -> 'CommandContext':
        return CommandContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandContext):
        """
        Dynamic initializer for CommandContext.
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
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandContext.toString()"""
        return str.__wrap(super(CommandContext, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandContext(java.lang.String)"""
        val = __CommandContext(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandContext.hashCode()"""
        return int.__wrap(super(CommandContext, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandContext.equals(java.lang.Object)"""
        return bool.__wrap(super(__CommandContext, self).equals(arg0))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandContext.name()"""
        return str.__wrap(super(CommandContext, self).name()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Perm
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import dev.ultreon.quantum.api.commands.Perm as __Perm
__Perm = __Perm
 
class Perm(ABC, __Annotation, Annotation):
    """dev.ultreon.quantum.api.commands.Perm"""
 
    @staticmethod
    def __wrap(java_value: __Perm) -> 'Perm':
        return Perm(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Perm):
        """
        Dynamic initializer for Perm.
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
    def value(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.Perm.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandReader
from pyquantum_helper import import_once as __import_once__
import java.lang.Character as __char
from pyquantum_helper import transform as __transform
import java.lang.Boolean as __boolean
from builtins import type
try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = __import_once__("pyquantum.api.commands.selector")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.math.BigInteger as BigInteger
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.api.commands.CommandSender as __CommandSender
__CommandSender = __CommandSender
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.api.commands.selector.Selector as __Selector
__Selector = __Selector
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandReader as __CommandReader
__CommandReader = __CommandReader
import java.math.BigDecimal as BigDecimal
import java.lang.Integer as __int
from builtins import int
 
class CommandReader():
    """dev.ultreon.quantum.api.commands.CommandReader"""
 
    @staticmethod
    def __wrap(java_value: __CommandReader) -> 'CommandReader':
        return CommandReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandReader):
        """
        Dynamic initializer for CommandReader.
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
    def isAtStartOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtStartOfArg()"""
        return bool.__wrap(super(CommandReader, self).isAtStartOfArg())

    @overload
    def getLastChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.getLastChar()"""
        return str.__wrap(super(CommandReader, self).getLastChar())

    @overload
    def readBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.quantum.api.commands.CommandReader.readBigDecimal() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return __transform(super(CommandReader, self).readBigDecimal()).'BigDecimal'Value()

    @overload
    def readByte(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readByte() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readByte())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCommand(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommand()"""
        return str.__wrap(super(CommandReader, self).getCommand())

    @overload
    def getCurChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.getCurChar()"""
        return str.__wrap(super(CommandReader, self).getCurChar())

    @overload
    def isAtLastCmd(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtLastCmd()"""
        return bool.__wrap(super(CommandReader, self).isAtLastCmd())

    @overload
    def readLong(self) -> int:
        """public long dev.ultreon.quantum.api.commands.CommandReader.readLong() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readLong())

    @overload
    def readUntil(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readUntil(char) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return str.__wrap(super(__CommandReader, self).readUntil(__char.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def readString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readString() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str.__wrap(super(CommandReader, self).readString())

    @overload
    def isAtLastCharInArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtLastCharInArg()"""
        return bool.__wrap(super(CommandReader, self).isAtLastCharInArg())

    @overload
    def getArguments(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandReader.getArguments()"""
        return List[str].__wrap(super(CommandReader, self).getArguments())

    @overload
    def readIntHex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.readIntHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readIntHex())

    @overload
    def readMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readMessage() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str.__wrap(super(CommandReader, self).readMessage())

    @overload
    def readShort(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readShort() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readShort())

    @overload
    def readRemaining(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readRemaining() throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return str.__wrap(super(CommandReader, self).readRemaining())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def readByteHex(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readByteHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readByteHex())

    @overload
    def readShortHex(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readShortHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readShortHex())

    @overload
    def back(self):
        """public void dev.ultreon.quantum.api.commands.CommandReader.back() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        super(CommandReader, self).back()

    @overload
    def getOffset(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.getOffset()"""
        return int.__wrap(super(CommandReader, self).getOffset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.api.commands.CommandReader.readId() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'util.Identifier'.__wrap(super(CommandReader, self).readId())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isAtEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtEndOfArg()"""
        return bool.__wrap(super(CommandReader, self).isAtEndOfArg())

    @overload
    def readSelector(self) -> 'selector.Selector':
        """public dev.ultreon.quantum.api.commands.selector.Selector dev.ultreon.quantum.api.commands.CommandReader.readSelector() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'selector.Selector'.__wrap(super(CommandReader, self).readSelector())

    @overload
    def tryNextArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.tryNextArg() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return bool.__wrap(super(CommandReader, self).tryNextArg())

    @overload
    def readBigIntegerHex(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.quantum.api.commands.CommandReader.readBigIntegerHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return __transform(super(CommandReader, self).readBigIntegerHex()).'BigInteger'Value()

    @overload
    def readLongHex(self) -> int:
        """public long dev.ultreon.quantum.api.commands.CommandReader.readLongHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readLongHex())

    @overload
    def readBoolean(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.readBoolean() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return bool.__wrap(super(CommandReader, self).readBoolean())

    @overload
    def getSender(self) -> 'CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.api.commands.CommandReader.getSender()"""
        return 'CommandSender'.__wrap(super(CommandReader, self).getSender())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isAtEndOfCmd(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtEndOfCmd()"""
        return bool.__wrap(super(CommandReader, self).isAtEndOfCmd())

    @overload
    def readBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.quantum.api.commands.CommandReader.readBigInteger() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return __transform(super(CommandReader, self).readBigInteger()).'BigInteger'Value()

    @overload
    def isAtStartEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtStartEndOfArg()"""
        return bool.__wrap(super(CommandReader, self).isAtStartEndOfArg())

    @overload
    def readDouble(self) -> float:
        """public double dev.ultreon.quantum.api.commands.CommandReader.readDouble() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return float.__wrap(super(CommandReader, self).readDouble())

    @overload
    def getCommandline(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommandline()"""
        return str.__wrap(super(CommandReader, self).getCommandline())

    @staticmethod
    @overload
    def get() -> 'CommandReader':
        """public static dev.ultreon.quantum.api.commands.CommandReader dev.ultreon.quantum.api.commands.CommandReader.get()"""
        return CommandReader.__wrap(__CommandReader.get())

    @overload
    def readInt(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.readInt() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int.__wrap(super(CommandReader, self).readInt())

    @overload
    def readMessageUntil(self, arg0: str, arg1: bool) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readMessageUntil(char,boolean) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str.__wrap(super(__CommandReader, self).readMessageUntil(__char.valueOf(arg0), __boolean.valueOf(arg1)))

    @overload
    def getArgument(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getArgument()"""
        return str.__wrap(super(CommandReader, self).getArgument())

    @overload
    def isAtHardEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtHardEndOfArg()"""
        return bool.__wrap(super(CommandReader, self).isAtHardEndOfArg())

    @overload
    def nextSplit(self, arg0: str) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandReader.nextSplit(java.lang.String) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return List[str].__wrap(super(__CommandReader, self).nextSplit(arg0))

    @overload
    def readFloat(self) -> float:
        """public float dev.ultreon.quantum.api.commands.CommandReader.readFloat() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return float.__wrap(super(CommandReader, self).readFloat())

    @overload
    def getCommandlineArgs(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommandlineArgs()"""
        return str.__wrap(super(CommandReader, self).getCommandlineArgs())

    @overload
    def getCurrent(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.getCurrent()"""
        return int.__wrap(super(CommandReader, self).getCurrent())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str, arg2: 'String'):
        """public dev.ultreon.quantum.api.commands.CommandReader(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String[])"""
        val = __CommandReader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.readChar() throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return str.__wrap(super(CommandReader, self).readChar()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.MessageCode
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
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
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
 
class MessageCode(__Enum, Enum):
    """dev.ultreon.quantum.api.commands.MessageCode"""
 
    @staticmethod
    def __wrap(java_value: __MessageCode) -> 'MessageCode':
        return MessageCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageCode):
        """
        Dynamic initializer for MessageCode.
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
 
    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.COMMAND_OUTPUT_DETECTED
    COMMAND_OUTPUT_DETECTED: 'MessageCode' = __wrap(__MessageCode.COMMAND_OUTPUT_DETECTED)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NO_SELECTION
    NO_SELECTION: 'MessageCode' = __wrap(__MessageCode.NO_SELECTION)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.DEPRECATED
    DEPRECATED: 'MessageCode' = __wrap(__MessageCode.DEPRECATED)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.DANGEROUS
    DANGEROUS: 'MessageCode' = __wrap(__MessageCode.DANGEROUS)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.EXPERIMENTAL
    EXPERIMENTAL: 'MessageCode' = __wrap(__MessageCode.EXPERIMENTAL)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.TOO_MANY_ARGS
    TOO_MANY_ARGS: 'MessageCode' = __wrap(__MessageCode.TOO_MANY_ARGS)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NOT_FOUND_IN_WORLD
    NOT_FOUND_IN_WORLD: 'MessageCode' = __wrap(__MessageCode.NOT_FOUND_IN_WORLD)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NOT_FOUND
    NOT_FOUND: 'MessageCode' = __wrap(__MessageCode.NOT_FOUND)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NEED_PLAYER
    NEED_PLAYER: 'MessageCode' = __wrap(__MessageCode.NEED_PLAYER)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.REJECTED
    REJECTED: 'MessageCode' = __wrap(__MessageCode.REJECTED)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NO_TARGET
    NO_TARGET: 'MessageCode' = __wrap(__MessageCode.NO_TARGET)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.OVERFLOW
    OVERFLOW: 'MessageCode' = __wrap(__MessageCode.OVERFLOW)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.WIP
    WIP: 'MessageCode' = __wrap(__MessageCode.WIP)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.INVALID_VALUE
    INVALID_VALUE: 'MessageCode' = __wrap(__MessageCode.INVALID_VALUE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NOT_OP
    NOT_OP: 'MessageCode' = __wrap(__MessageCode.NOT_OP)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NEED_CONSOLE
    NEED_CONSOLE: 'MessageCode' = __wrap(__MessageCode.NEED_CONSOLE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.ACCESS_DENIED
    ACCESS_DENIED: 'MessageCode' = __wrap(__MessageCode.ACCESS_DENIED)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.GENERIC
    GENERIC: 'MessageCode' = __wrap(__MessageCode.GENERIC)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.HACKER
    HACKER: 'MessageCode' = __wrap(__MessageCode.HACKER)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.COOLDOWN
    COOLDOWN: 'MessageCode' = __wrap(__MessageCode.COOLDOWN)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.EDIT_MODE
    EDIT_MODE: 'MessageCode' = __wrap(__MessageCode.EDIT_MODE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.CANNOT_BE_SELF
    CANNOT_BE_SELF: 'MessageCode' = __wrap(__MessageCode.CANNOT_BE_SELF)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.TOO_FEW_ARGS
    TOO_FEW_ARGS: 'MessageCode' = __wrap(__MessageCode.TOO_FEW_ARGS)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.SERVER_ERROR
    SERVER_ERROR: 'MessageCode' = __wrap(__MessageCode.SERVER_ERROR)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.OVERLOAD
    OVERLOAD: 'MessageCode' = __wrap(__MessageCode.OVERLOAD)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.CONFLICT
    CONFLICT: 'MessageCode' = __wrap(__MessageCode.CONFLICT)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.EMPTY
    EMPTY: 'MessageCode' = __wrap(__MessageCode.EMPTY)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NEED_ENTITY
    NEED_ENTITY: 'MessageCode' = __wrap(__MessageCode.NEED_ENTITY)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.SELECTOR_TOO_SMALL
    SELECTOR_TOO_SMALL: 'MessageCode' = __wrap(__MessageCode.SELECTOR_TOO_SMALL)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.DOES_NOT_MAKE_SENSE
    DOES_NOT_MAKE_SENSE: 'MessageCode' = __wrap(__MessageCode.DOES_NOT_MAKE_SENSE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.OUT_OF_RANGE
    OUT_OF_RANGE: 'MessageCode' = __wrap(__MessageCode.OUT_OF_RANGE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.NO_PERMISSION
    NO_PERMISSION: 'MessageCode' = __wrap(__MessageCode.NO_PERMISSION)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.IMPOSSIBLE
    IMPOSSIBLE: 'MessageCode' = __wrap(__MessageCode.IMPOSSIBLE)

    # public static final dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.OUTDATED
    OUTDATED: 'MessageCode' = __wrap(__MessageCode.OUTDATED)


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
    def getCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.MessageCode.getCode()"""
        return int.__wrap(super(MessageCode, self).getCode())

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
    def valueOf(arg0: str) -> 'MessageCode':
        """public static dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.valueOf(java.lang.String)"""
        return MessageCode.__wrap(__MessageCode.valueOf(arg0))

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

    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.MessageCode.getId()"""
        return str.__wrap(super(MessageCode, self).getId())

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
    def values() -> List['MessageCode']:
        """public static dev.ultreon.quantum.api.commands.MessageCode[] dev.ultreon.quantum.api.commands.MessageCode.values()"""
        return List[MessageCode].__wrap(__MessageCode.values()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParser
import dev.ultreon.quantum.api.commands.CommandParser as __CommandParser
__CommandParser = __CommandParser
from abc import abstractmethod, ABC
 
class CommandParser(ABC):
    """dev.ultreon.quantum.api.commands.CommandParser"""
 
    @staticmethod
    def __wrap(java_value: __CommandParser) -> 'CommandParser':
        return CommandParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandParser):
        """
        Dynamic initializer for CommandParser.
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
    def parse(self, arg0: 'CommandReader'):
        """public abstract T dev.ultreon.quantum.api.commands.CommandParser.parse(dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandFlag
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.api.commands.output.BasicCommandResult as __BasicCommandResult_MessageType
__MessageType = __BasicCommandResult_MessageType.MessageType
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api.commands import output
except ImportError:
    output = __import_once__("pyquantum.api.commands.output")

import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import dev.ultreon.quantum.api.commands.CommandFlag as __CommandFlag
__CommandFlag = __CommandFlag
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
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
 
class CommandFlag(__Enum, Enum):
    """dev.ultreon.quantum.api.commands.CommandFlag"""
 
    @staticmethod
    def __wrap(java_value: __CommandFlag) -> 'CommandFlag':
        return CommandFlag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandFlag):
        """
        Dynamic initializer for CommandFlag.
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
 
    # public static final dev.ultreon.quantum.api.commands.CommandFlag dev.ultreon.quantum.api.commands.CommandFlag.EDIT_MODE
    EDIT_MODE: 'CommandFlag' = __wrap(__CommandFlag.EDIT_MODE)

    # public static final dev.ultreon.quantum.api.commands.CommandFlag dev.ultreon.quantum.api.commands.CommandFlag.DANGEROUS
    DANGEROUS: 'CommandFlag' = __wrap(__CommandFlag.DANGEROUS)


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

    @overload
    def getMessageType(self) -> 'output.BasicCommandResult$MessageType':
        """public dev.ultreon.quantum.api.commands.output.BasicCommandResult$MessageType dev.ultreon.quantum.api.commands.CommandFlag.getMessageType()"""
        return 'output.BasicCommandResult$MessageType'.__wrap(super(CommandFlag, self).getMessageType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandFlag.getDescription()"""
        return str.__wrap(super(CommandFlag, self).getDescription())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CommandFlag':
        """public static dev.ultreon.quantum.api.commands.CommandFlag dev.ultreon.quantum.api.commands.CommandFlag.valueOf(java.lang.String)"""
        return CommandFlag.__wrap(__CommandFlag.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['CommandFlag']:
        """public static dev.ultreon.quantum.api.commands.CommandFlag[] dev.ultreon.quantum.api.commands.CommandFlag.values()"""
        return List[CommandFlag].__wrap(__CommandFlag.values())

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

    @overload
    def getMessageCode(self) -> 'MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.CommandFlag.getMessageCode()"""
        return 'MessageCode'.__wrap(super(CommandFlag, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_NotAtEndOfArg
__NotAtEndOfArg = __CommandParseException_NotAtEndOfArg.NotAtEndOfArg
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotAtEndOfArg(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.NotAtEndOfArg"""
 
    @staticmethod
    def __wrap(java_value: __NotAtEndOfArg) -> 'NotAtEndOfArg':
        return NotAtEndOfArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotAtEndOfArg):
        """
        Dynamic initializer for NotAtEndOfArg.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg(int)"""
        val = __NotAtEndOfArg(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry
import it.unimi.dsi.fastutil.ints.Int2ReferenceMap.Entry as Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.IndexedCommandSpecValues as __IndexedCommandSpecValues_Entry
__Entry = __IndexedCommandSpecValues_Entry.Entry
import dev.ultreon.quantum.api.commands.CommandSpecValues as __CommandSpecValues
__CommandSpecValues = __CommandSpecValues
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entry():
    """dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.Entry"""
 
    @staticmethod
    def __wrap(java_value: __Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entry):
        """
        Dynamic initializer for Entry.
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

    @overload
    def __init__(self, arg0: 'Entry'):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry(it.unimi.dsi.fastutil.ints.Int2ReferenceMap$Entry<dev.ultreon.quantum.api.commands.CommandSpecValues>)"""
        val = __Entry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def set(self, arg0: 'CommandSpecValues'):
        """public void dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.set(dev.ultreon.quantum.api.commands.CommandSpecValues)"""
        super(__Entry, self).set(arg0)

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
    def index(self) -> int:
        """public int dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.index()"""
        return int.__wrap(super(Entry, self).index())

    @overload
    def values(self) -> 'CommandSpecValues':
        """public dev.ultreon.quantum.api.commands.CommandSpecValues dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.values()"""
        return 'CommandSpecValues'.__wrap(super(Entry, self).values())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Selections
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

import dev.ultreon.quantum.api.commands.Selections as __Selections
__Selections = __Selections
from builtins import str
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import dev.ultreon.quantum.entity.Entity as __Entity
__Entity = __Entity
from pyquantum_helper import override
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

import java.lang.Object as __object
import dev.ultreon.quantum.entity.player.Player as __Player
__Player = __Player
from builtins import type
import dev.ultreon.quantum.world.ServerChunk as __ServerChunk
__ServerChunk = __ServerChunk
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.world.ServerWorld as __ServerWorld
__ServerWorld = __ServerWorld
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Selections():
    """dev.ultreon.quantum.api.commands.Selections"""
 
    @staticmethod
    def __wrap(java_value: __Selections) -> 'Selections':
        return Selections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Selections):
        """
        Dynamic initializer for Selections.
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
    def getPlayer(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.api.commands.Selections.getPlayer()"""
        return 'player.Player'.__wrap(super(Selections, self).getPlayer())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Selections()"""
        val = __Selections()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Selections()"""
        val = __Selections()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getChunk(self) -> 'world.ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.api.commands.Selections.getChunk()"""
        return 'world.ServerChunk'.__wrap(super(Selections, self).getChunk())

    @overload
    def setChunk(self, arg0: 'ServerChunk'):
        """public void dev.ultreon.quantum.api.commands.Selections.setChunk(dev.ultreon.quantum.world.ServerChunk)"""
        super(__Selections, self).setChunk(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.api.commands.Selections.getWorld()"""
        return 'world.ServerWorld'.__wrap(super(Selections, self).getWorld())

    @overload
    def setWorld(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.api.commands.Selections.setWorld(dev.ultreon.quantum.world.ServerWorld)"""
        super(__Selections, self).setWorld(arg0)

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
    def setPlayer(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.api.commands.Selections.setPlayer(dev.ultreon.quantum.entity.player.Player)"""
        super(__Selections, self).setPlayer(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get(arg0: 'CommandSender') -> 'Selections':
        """public static dev.ultreon.quantum.api.commands.Selections dev.ultreon.quantum.api.commands.Selections.get(dev.ultreon.quantum.api.commands.CommandSender)"""
        return Selections.__wrap(__Selections.get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.api.commands.Selections.getEntity()"""
        return 'entity.Entity'.__wrap(super(Selections, self).getEntity())

    @overload
    def setEntity(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.api.commands.Selections.setEntity(dev.ultreon.quantum.entity.Entity)"""
        super(__Selections, self).setEntity(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Overload
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.Overload as __Overload
__Overload = __Overload
import java.util.ArrayList as ArrayList
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
import java.util.List as List
import dev.ultreon.quantum.api.commands.CommandSpec as __CommandSpec
__CommandSpec = __CommandSpec
 
class Overload():
    """dev.ultreon.quantum.api.commands.Overload"""
 
    @staticmethod
    def __wrap(java_value: __Overload) -> 'Overload':
        return Overload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Overload):
        """
        Dynamic initializer for Overload.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.equals(java.lang.Object)"""
        return bool.__wrap(super(__Overload, self).equals(arg0))

    @overload
    def hasPermission(self, arg0: 'CommandSender') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.hasPermission(dev.ultreon.quantum.api.commands.CommandSender)"""
        return bool.__wrap(super(__Overload, self).hasPermission(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def spec(self) -> 'CommandSpec':
        """public dev.ultreon.quantum.api.commands.CommandSpec dev.ultreon.quantum.api.commands.Overload.spec()"""
        return 'CommandSpec'.__wrap(super(Overload, self).spec())

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
    def matches(self, arg0: 'ArrayList') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.matches(java.util.ArrayList<dev.ultreon.quantum.api.commands.CommandParameter>)"""
        return bool.__wrap(super(__Overload, self).matches(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def validFor(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.validFor(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return bool.__wrap(super(__Overload, self).validFor(arg0, arg1, arg2))

    @overload
    def args(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.CommandParameter> dev.ultreon.quantum.api.commands.Overload.args()"""
        return 'List'.__wrap(super(Overload, self).args())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String', arg3: 'List') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Overload.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[],java.util.List<java.lang.String>)"""
        return 'List'.__wrap(super(__Overload, self).tabComplete(arg0, arg1, arg2, arg3))

    @overload
    def getObjectCache(self) -> 'List':
        """public java.util.List<java.lang.Object> dev.ultreon.quantum.api.commands.Overload.getObjectCache()"""
        return 'List'.__wrap(super(Overload, self).getObjectCache())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Overload.toString()"""
        return str.__wrap(super(Overload, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.Overload.hashCode()"""
        return int.__wrap(super(Overload, self).hashCode())

    @overload
    def __init__(self, arg0: 'List', arg1: 'CommandSpec', arg2: str):
        """public dev.ultreon.quantum.api.commands.Overload(java.util.List<dev.ultreon.quantum.api.commands.CommandParameter>,dev.ultreon.quantum.api.commands.CommandSpec,java.lang.String)"""
        val = __Overload(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.SpecSyntaxException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.SpecSyntaxException as __SpecSyntaxException
__SpecSyntaxException = __SpecSyntaxException
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SpecSyntaxException(__RuntimeException, RuntimeException):
    """dev.ultreon.quantum.api.commands.SpecSyntaxException"""
 
    @staticmethod
    def __wrap(java_value: __SpecSyntaxException) -> 'SpecSyntaxException':
        return SpecSyntaxException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpecSyntaxException):
        """
        Dynamic initializer for SpecSyntaxException.
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
    def __init__(self, arg0: int, arg1: int, arg2: str):
        """public dev.ultreon.quantum.api.commands.SpecSyntaxException(int,int,java.lang.String)"""
        val = __SpecSyntaxException(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.SpecSyntaxException.getMessage()"""
        return str.__wrap(super(SpecSyntaxException, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

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

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void dev.ultreon.quantum.api.commands.SpecSyntaxException.printStackTrace()"""
        super(SpecSyntaxException, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandRunnable
import dev.ultreon.quantum.api.commands.CommandRunnable as __CommandRunnable
__CommandRunnable = __CommandRunnable
from builtins import object
from abc import abstractmethod, ABC
 
class CommandRunnable(ABC):
    """dev.ultreon.quantum.api.commands.CommandRunnable"""
 
    @staticmethod
    def __wrap(java_value: __CommandRunnable) -> 'CommandRunnable':
        return CommandRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandRunnable):
        """
        Dynamic initializer for CommandRunnable.
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
    def invoke(self, *arg0: object):
        """public abstract dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandRunnable.invoke(java.lang.Object...)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCrashReport
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandCrashReport as __CommandCrashReport_Details
__Details = __CommandCrashReport_Details.Details
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandCrashReport as __CommandCrashReport
__CommandCrashReport = __CommandCrashReport
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommandCrashReport():
    """dev.ultreon.quantum.api.commands.CommandCrashReport"""
 
    @staticmethod
    def __wrap(java_value: __CommandCrashReport) -> 'CommandCrashReport':
        return CommandCrashReport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandCrashReport):
        """
        Dynamic initializer for CommandCrashReport.
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
    def save(self, arg0: 'CommandSender') -> 'Details':
        """public dev.ultreon.quantum.api.commands.CommandCrashReport$Details dev.ultreon.quantum.api.commands.CommandCrashReport.save(dev.ultreon.quantum.api.commands.CommandSender)"""
        return 'Details'.__wrap(super(__CommandCrashReport, self).save(arg0))

    @overload
    def __init__(self, arg0: 'Throwable', arg1: str, arg2: 'String'):
        """public dev.ultreon.quantum.api.commands.CommandCrashReport(java.lang.Throwable,java.lang.String,java.lang.String[])"""
        val = __CommandCrashReport(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Role
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.api.commands.Role as __Role
__Role = __Role
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Role():
    """dev.ultreon.quantum.api.commands.Role"""
 
    @staticmethod
    def __wrap(java_value: __Role) -> 'Role':
        return Role(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Role):
        """
        Dynamic initializer for Role.
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Role()"""
        val = __Role()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Role()"""
        val = __Role()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$Invalid
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException_Invalid
__Invalid = __CommandParseException_Invalid.Invalid
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParseException as __CommandParseException
__CommandParseException = __CommandParseException
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Invalid(__CommandParseException, CommandParseException):
    """dev.ultreon.quantum.api.commands.CommandParseException.Invalid"""
 
    @staticmethod
    def __wrap(java_value: __Invalid) -> 'Invalid':
        return Invalid(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Invalid):
        """
        Dynamic initializer for Invalid.
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
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: object, arg2: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$Invalid(java.lang.String,java.lang.Object,int)"""
        val = __Invalid(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$Invalid(java.lang.String,int)"""
        val = __Invalid(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandParseException, self).send(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

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

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter$Text
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter
__CommandParameter = __CommandParameter
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.CommandParameter as __CommandParameter_Text
__Text = __CommandParameter_Text.Text
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Text(__CommandParameter, CommandParameter):
    """dev.ultreon.quantum.api.commands.CommandParameter.Text"""
 
    @staticmethod
    def __wrap(java_value: __Text) -> 'Text':
        return Text(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Text):
        """
        Dynamic initializer for Text.
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
    def getTag(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.getTag()"""
        return str.__wrap(super(Text, self).getTag())

    @overload
    def __init__(self, arg0: 'String', arg1: bool):
        """public dev.ultreon.quantum.api.commands.CommandParameter$Text(java.lang.String[],boolean)"""
        val = __Text(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getText(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandParameter$Text.getText()"""
        return List[str].__wrap(super(Text, self).getText())

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.getComment()"""
        return str.__wrap(super(Text, self).getComment())

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
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifArgType(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.toString()"""
        return str.__wrap(super(Text, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'.__wrap(super(__CommandParameter, self).ifText(arg0))

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
    def isOptional(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandParameter$Text.isOptional()"""
        return bool.__wrap(super(Text, self).isOptional()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.ArgumentType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.api.commands.ArgumentType as __ArgumentType
__ArgumentType = __ArgumentType
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ArgumentType(ABC):
    """dev.ultreon.quantum.api.commands.ArgumentType"""
 
    @staticmethod
    def __wrap(java_value: __ArgumentType) -> 'ArgumentType':
        return ArgumentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArgumentType):
        """
        Dynamic initializer for ArgumentType.
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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.ArgumentType.hashCode()"""
        return int.__wrap(super(ArgumentType, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.ArgumentType.toString()"""
        return str.__wrap(super(ArgumentType, self).toString())

    @overload
    def getArgTypeClasses(self) -> List['type.Class']:
        """public java.lang.Class<?>[] dev.ultreon.quantum.api.commands.ArgumentType.getArgTypeClasses()"""
        return List['type.Class'].__wrap(super(ArgumentType, self).getArgTypeClasses())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getArgsNeeded(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String') -> int:
        """public int dev.ultreon.quantum.api.commands.ArgumentType.getArgsNeeded(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[])"""
        return int.__wrap(super(__ArgumentType, self).getArgsNeeded(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def getArgClass(self, ):
        """public abstract java.lang.Class<? extends dev.ultreon.quantum.api.commands.Argument<?>> dev.ultreon.quantum.api.commands.ArgumentType.getArgClass()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.ArgumentType()"""
        val = __ArgumentType()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.ArgumentType()"""
        val = __ArgumentType()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.ArgumentType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ArgumentType, self).equals(arg0))

    @abstractmethod
    def parse(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String'):
        """public abstract dev.ultreon.quantum.api.commands.ArgumentType$Result<? extends dev.ultreon.quantum.api.commands.Argument<? extends T>> dev.ultreon.quantum.api.commands.ArgumentType.parse(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        pass