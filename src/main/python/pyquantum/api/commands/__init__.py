from __future__ import annotations
from overload import overload


 
import java.lang.String as _string
from builtins import str
import java.lang.Boolean as _boolean
from builtins import type
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter
_CommandParameter = _CommandParameter
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class CommandParameter():
    """dev.ultreon.quantum.api.commands.CommandParameter"""
 
    @staticmethod
    def _wrap(java_value: _CommandParameter) -> 'CommandParameter':
        return CommandParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandParameter):
        """
        Dynamic initializer for CommandParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandParameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getTag(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getTag()"""
        pass

    @staticmethod
    @overload
    def ofText(arg0: bool, *arg1: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofText(boolean,java.lang.String...)"""
        return CommandParameter._wrap(_CommandParameter.ofText(_boolean.valueOf(arg0), arg1))

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifArgType(arg0))

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifText(arg0))

    @abstractmethod
    def getComment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getComment()"""
        pass

    @staticmethod
    @overload
    def ofArgType(arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofArgType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        return CommandParameter._wrap(_CommandParameter.ofArgType(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), arg5))

    @abstractmethod
    def isOptional(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandParameter.isOptional()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter
import java.lang.String as _string
from builtins import str
import java.lang.Boolean as _boolean
from builtins import type
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter
_CommandParameter = _CommandParameter
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class CommandParameter():
    """dev.ultreon.quantum.api.commands.CommandParameter"""
 
    @staticmethod
    def _wrap(java_value: _CommandParameter) -> 'CommandParameter':
        return CommandParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandParameter):
        """
        Dynamic initializer for CommandParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandParameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getTag(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getTag()"""
        pass

    @staticmethod
    @overload
    def ofText(arg0: bool, *arg1: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofText(boolean,java.lang.String...)"""
        return CommandParameter._wrap(_CommandParameter.ofText(_boolean.valueOf(arg0), arg1))

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifArgType(arg0))

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifText(arg0))

    @abstractmethod
    def getComment(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandParameter.getComment()"""
        pass

    @staticmethod
    @overload
    def ofArgType(arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str) -> 'CommandParameter':
        """public static dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ofArgType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        return CommandParameter._wrap(_CommandParameter.ofArgType(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), arg5))

    @abstractmethod
    def isOptional(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandParameter.isOptional()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter 
 
 
# CLASS: dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.PositionCommand as _PositionCommand_PositionSelection
_PositionSelection = _PositionCommand_PositionSelection.PositionSelection
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PositionSelection():
    """dev.ultreon.quantum.api.commands.PositionCommand.PositionSelection"""
 
    @staticmethod
    def _wrap(java_value: _PositionSelection) -> 'PositionSelection':
        return PositionSelection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PositionSelection):
        """
        Dynamic initializer for PositionSelection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PositionSelection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PositionSelection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reset(self, arg0: 'World'):
        """public void dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection.reset(dev.ultreon.quantum.world.World)"""
        super(_PositionSelection, self).reset(arg0)

    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection.getSize()"""
        return int._wrap(super(PositionSelection, self).getSize())

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection()"""
        val = _PositionSelection()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.PositionCommand$PositionSelection()"""
        val = _PositionSelection()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$EndOfCommand
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_EndOfCommand
_EndOfCommand = _CommandParseException_EndOfCommand.EndOfCommand
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EndOfCommand():
    """dev.ultreon.quantum.api.commands.CommandParseException.EndOfCommand"""
 
    @staticmethod
    def _wrap(java_value: _EndOfCommand) -> 'EndOfCommand':
        return EndOfCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EndOfCommand):
        """
        Dynamic initializer for EndOfCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EndOfCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EndOfCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$EndOfCommand(int)"""
        val = _EndOfCommand(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParserImpl
from pyquantum_helper import import_once as _import_once
from builtins import str
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
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
import java.lang.String as _string
import java.util.Set as Set
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandParserImpl as _CommandParserImpl
_CommandParserImpl = _CommandParserImpl
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandParserImpl():
    """dev.ultreon.quantum.api.commands.CommandParserImpl"""
 
    @staticmethod
    def _wrap(java_value: _CommandParserImpl) -> 'CommandParserImpl':
        return CommandParserImpl(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandParserImpl):
        """
        Dynamic initializer for CommandParserImpl.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandParserImpl__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandParserImpl__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @property
    def data(self) -> CommandData:
        return CommandData._wrap(super(_CommandParserImpl).data())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def execute(self, arg0: 'Command', arg1: 'CommandSender', arg2: 'CommandContext', arg3: str, arg4: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandParserImpl.execute(dev.ultreon.quantum.api.commands.Command,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'output.CommandResult'._wrap(super(_CommandParserImpl, self).execute(arg0, arg1, arg2, arg3, arg4))

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
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandParserImpl.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_CommandParserImpl, self).tabComplete(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'Class', arg1: 'CommandData', arg2: 'Set'):
        """public dev.ultreon.quantum.api.commands.CommandParserImpl(java.lang.Class<? extends dev.ultreon.quantum.api.commands.Command>,dev.ultreon.quantum.api.commands.CommandData,java.util.Set<dev.ultreon.quantum.api.commands.CommandSpec>)"""
        val = _CommandParserImpl(arg0, arg1, arg2)
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.IndexedCommandSpecValues
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import dev.ultreon.quantum.api.commands.IndexedCommandSpecValues as _IndexedCommandSpecValues
_IndexedCommandSpecValues = _IndexedCommandSpecValues
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.api.commands.CommandSpecValues as _CommandSpecValues
_CommandSpecValues = _CommandSpecValues
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IndexedCommandSpecValues():
    """dev.ultreon.quantum.api.commands.IndexedCommandSpecValues"""
 
    @staticmethod
    def _wrap(java_value: _IndexedCommandSpecValues) -> 'IndexedCommandSpecValues':
        return IndexedCommandSpecValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedCommandSpecValues):
        """
        Dynamic initializer for IndexedCommandSpecValues.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedCommandSpecValues__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedCommandSpecValues__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isBlank(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.isBlank()"""
        return bool._wrap(super(IndexedCommandSpecValues, self).isBlank())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry> dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.iterator()"""
        return 'Iterator'._wrap(super(IndexedCommandSpecValues, self).iterator())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.toString()"""
        return str._wrap(super(IndexedCommandSpecValues, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues()"""
        val = _IndexedCommandSpecValues()
        self.__wrapper = val

    @overload
    def has(self, arg0: int) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.has(int)"""
        return bool._wrap(super(_IndexedCommandSpecValues, self).has(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def set(self, arg0: int, arg1: 'CommandSpecValues'):
        """public void dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.set(int,dev.ultreon.quantum.api.commands.CommandSpecValues)"""
        super(_IndexedCommandSpecValues, self).set(_int.valueOf(arg0), arg1)

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def values(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.api.commands.CommandSpecValues> dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.values()"""
        return 'Collection'._wrap(super(IndexedCommandSpecValues, self).values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues()"""
        val = _IndexedCommandSpecValues()
        self.__wrapper = val

    @overload
    def get(self, arg0: int) -> 'CommandSpecValues':
        """public dev.ultreon.quantum.api.commands.CommandSpecValues dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.get(int)"""
        return 'CommandSpecValues'._wrap(super(_IndexedCommandSpecValues, self).get(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.hashCode()"""
        return int._wrap(super(IndexedCommandSpecValues, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.equals(java.lang.Object)"""
        return bool._wrap(super(_IndexedCommandSpecValues, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCategory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandCategory as _CommandCategory
_CommandCategory = _CommandCategory
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
 
class CommandCategory():
    """dev.ultreon.quantum.api.commands.CommandCategory"""
 
    @staticmethod
    def _wrap(java_value: _CommandCategory) -> 'CommandCategory':
        return CommandCategory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandCategory):
        """
        Dynamic initializer for CommandCategory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandCategory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandCategory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CommandCategory':
        """public static dev.ultreon.quantum.api.commands.CommandCategory dev.ultreon.quantum.api.commands.CommandCategory.valueOf(java.lang.String)"""
        return CommandCategory._wrap(_CommandCategory.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['CommandCategory']:
        """public static dev.ultreon.quantum.api.commands.CommandCategory[] dev.ultreon.quantum.api.commands.CommandCategory.values()"""
        return List[CommandCategory]._wrap(_CommandCategory.values())

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
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


CommandCategory.CHEATS = CommandCategory._wrap(_CHEATS.CHEATS)

CommandCategory.FUN = CommandCategory._wrap(_FUN.FUN)

CommandCategory.SPAWN = CommandCategory._wrap(_SPAWN.SPAWN)

CommandCategory.MINI_GAME = CommandCategory._wrap(_MINI_GAME.MINI_GAME)

CommandCategory.EDIT = CommandCategory._wrap(_EDIT.EDIT)

CommandCategory.TELEPORT = CommandCategory._wrap(_TELEPORT.TELEPORT)

CommandCategory.ADMIN = CommandCategory._wrap(_ADMIN.ADMIN) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Command
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
 
class Command():
    """dev.ultreon.quantum.api.commands.Command"""
 
    @staticmethod
    def _wrap(java_value: _Command) -> 'Command':
        return Command(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Command):
        """
        Dynamic initializer for Command.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Command__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Command__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(Command, self).deprecated())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

    @overload
    def incomplete(self):
        """public void dev.ultreon.quantum.api.commands.Command.incomplete()"""
        super(Command, self).incomplete()

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
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(Command, self).getRequiredPermission())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Command()"""
        val = _Command()
        self.__wrapper = val

    @overload
    def data(self) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'CommandData'._wrap(super(Command, self).data())

    @overload
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(Command, self).outdated())

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_Command, self).warningMessage(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(Command, self).getRequiresOperator())

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Command()"""
        val = _Command()
        self.__wrapper = val

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_Command, self).setNeedPlayer(_boolean.valueOf(arg0))

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
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(Command, self).wip())

    @staticmethod
    @overload
    def getTotalCount() -> int:
        """public static int dev.ultreon.quantum.api.commands.Command.getTotalCount()"""
        return int._wrap(_Command.getTotalCount())

    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(Command, self).requireLivingEntity()

    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandStatus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandStatus as _CommandStatus
_CommandStatus = _CommandStatus
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
 
class CommandStatus():
    """dev.ultreon.quantum.api.commands.CommandStatus"""
 
    @staticmethod
    def _wrap(java_value: _CommandStatus) -> 'CommandStatus':
        return CommandStatus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandStatus):
        """
        Dynamic initializer for CommandStatus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandStatus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandStatus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def values() -> List['CommandStatus']:
        """public static dev.ultreon.quantum.api.commands.CommandStatus[] dev.ultreon.quantum.api.commands.CommandStatus.values()"""
        return List[CommandStatus]._wrap(_CommandStatus.values())

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

    @overload
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandStatus.getDescription()"""
        return str._wrap(super(CommandStatus, self).getDescription())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CommandStatus':
        """public static dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandStatus.valueOf(java.lang.String)"""
        return CommandStatus._wrap(_CommandStatus.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


CommandStatus.DEBUG = CommandStatus._wrap(_DEBUG.DEBUG)

CommandStatus.DEPRECATED = CommandStatus._wrap(_DEPRECATED.DEPRECATED)

CommandStatus.OUTDATED = CommandStatus._wrap(_OUTDATED.OUTDATED)

CommandStatus.WIP = CommandStatus._wrap(_WIP.WIP)

CommandStatus.DONE = CommandStatus._wrap(_DONE.DONE) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_NotAtStartOfArg
_NotAtStartOfArg = _CommandParseException_NotAtStartOfArg.NotAtStartOfArg
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotAtStartOfArg():
    """dev.ultreon.quantum.api.commands.CommandParseException.NotAtStartOfArg"""
 
    @staticmethod
    def _wrap(java_value: _NotAtStartOfArg) -> 'NotAtStartOfArg':
        return NotAtStartOfArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotAtStartOfArg):
        """
        Dynamic initializer for NotAtStartOfArg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotAtStartOfArg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotAtStartOfArg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg(int)"""
        val = _NotAtStartOfArg(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CmdParam
import dev.ultreon.quantum.api.commands.CmdParam as _CmdParam
_CmdParam = _CmdParam
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class CmdParam():
    """dev.ultreon.quantum.api.commands.CmdParam"""
 
    @staticmethod
    def _wrap(java_value: _CmdParam) -> 'CmdParam':
        return CmdParam(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CmdParam):
        """
        Dynamic initializer for CmdParam.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CmdParam__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CmdParam__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
import java.lang.Character as _char
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_NotADigit
_NotADigit = _CommandParseException_NotADigit.NotADigit
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotADigit():
    """dev.ultreon.quantum.api.commands.CommandParseException.NotADigit"""
 
    @staticmethod
    def _wrap(java_value: _NotADigit) -> 'NotADigit':
        return NotADigit(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotADigit):
        """
        Dynamic initializer for NotADigit.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotADigit__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotADigit__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotADigit(char,int)"""
        val = _NotADigit(_char.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotADigit(char)"""
        val = _NotADigit(_char.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotANumber
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_NotANumber
_NotANumber = _CommandParseException_NotANumber.NotANumber
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotANumber():
    """dev.ultreon.quantum.api.commands.CommandParseException.NotANumber"""
 
    @staticmethod
    def _wrap(java_value: _NotANumber) -> 'NotANumber':
        return NotANumber(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotANumber):
        """
        Dynamic initializer for NotANumber.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotANumber__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotANumber__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotANumber(java.lang.String,int)"""
        val = _NotANumber(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotANumber(java.lang.String)"""
        val = _NotANumber(arg0)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.IllegalCommandException
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import dev.ultreon.quantum.api.commands.IllegalCommandException as _IllegalCommandException
_IllegalCommandException = _IllegalCommandException
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IllegalCommandException():
    """dev.ultreon.quantum.api.commands.IllegalCommandException"""
 
    @staticmethod
    def _wrap(java_value: _IllegalCommandException) -> 'IllegalCommandException':
        return IllegalCommandException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IllegalCommandException):
        """
        Dynamic initializer for IllegalCommandException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IllegalCommandException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IllegalCommandException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        val = _IllegalCommandException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.Throwable)"""
        val = _IllegalCommandException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self, arg0: 'MessageCode'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode)"""
        val = _IllegalCommandException(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def getCode(self) -> 'MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.IllegalCommandException.getCode()"""
        return 'MessageCode'._wrap(super(IllegalCommandException, self).getCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: 'Throwable', arg3: bool, arg4: bool):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,java.lang.Throwable,boolean,boolean)"""
        val = _IllegalCommandException(arg0, arg1, arg2, _boolean.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.IllegalCommandException(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,java.lang.Throwable)"""
        val = _IllegalCommandException(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSpecValues
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.util.Spliterator as Spliterator
import dev.ultreon.quantum.api.commands.CommandSpecValues as _CommandSpecValues
_CommandSpecValues = _CommandSpecValues
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.HashSet as HashSet
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.AbstractSet as _AbstractSet
_AbstractSet = _AbstractSet
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.AbstractCollection as _AbstractCollection
_AbstractCollection = _AbstractCollection
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.util.HashSet as _HashSet
_HashSet = _HashSet
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandSpecValues():
    """dev.ultreon.quantum.api.commands.CommandSpecValues"""
 
    @staticmethod
    def _wrap(java_value: _CommandSpecValues) -> 'CommandSpecValues':
        return CommandSpecValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandSpecValues):
        """
        Dynamic initializer for CommandSpecValues.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandSpecValues__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandSpecValues__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_AbstractCollection, self).addAll(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int java.util.AbstractSet.hashCode()"""
        return int._wrap(super(AbstractSet, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def toArray(self, arg0: 'Object') -> List[object]:
        """public <T> T[] java.util.HashSet.toArray(T[])"""
        return List[object]._wrap(super(_HashSet, self).toArray(arg0))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> java.util.HashSet.iterator()"""
        return 'Iterator'._wrap(super(HashSet, self).iterator())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public java.util.Spliterator<E> java.util.HashSet.spliterator()"""
        return 'Spliterator'._wrap(super(HashSet, self).spliterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @overload
    def removeAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractSet.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractSet, self).removeAll(arg0))

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.HashSet.contains(java.lang.Object)"""
        return bool._wrap(super(_HashSet, self).contains(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.util.AbstractSet.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractSet, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def retainAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).retainAll(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues()"""
        val = _CommandSpecValues()
        self.__wrapper = val

    @staticmethod
    @overload
    def newHashSet(arg0: int) -> 'HashSet':
        """public static <T> java.util.HashSet<T> java.util.HashSet.newHashSet(int)"""
        return HashSet._wrap(_HashSet.newHashSet(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues()"""
        val = _CommandSpecValues()
        self.__wrapper = val

    @overload
    def add(self, arg0: str) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandSpecValues.add(java.lang.String)"""
        return bool._wrap(super(_CommandSpecValues, self).add(arg0))

    @overload
    def containsAll(self, arg0: 'Collection') -> bool:
        """public boolean java.util.AbstractCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_AbstractCollection, self).containsAll(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.HashSet.isEmpty()"""
        return bool._wrap(super(HashSet, self).isEmpty())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.util.AbstractCollection.toString()"""
        return str._wrap(super(AbstractCollection, self).toString())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.HashSet.size()"""
        return int._wrap(super(HashSet, self).size())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] java.util.HashSet.toArray()"""
        return List[object]._wrap(super(HashSet, self).toArray())

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def __init__(self, arg0: 'Set'):
        """public dev.ultreon.quantum.api.commands.CommandSpecValues(java.util.Set<java.lang.String>)"""
        val = _CommandSpecValues(arg0)
        self.__wrapper = val

    @overload
    def remove(self, arg0: object) -> bool:
        """public boolean java.util.HashSet.remove(java.lang.Object)"""
        return bool._wrap(super(_HashSet, self).remove(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def clone(self) -> object:
        """public java.lang.Object java.util.HashSet.clone()"""
        return object._wrap(super(HashSet, self).clone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def clear(self):
        """public void java.util.HashSet.clear()"""
        super(HashSet, self).clear() 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandArgumentMismatch
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.util.ArrayList as ArrayList
import java.io.OutputStream as OutputStream
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.IllegalArgumentException as IllegalArgumentException
import java.io.Writer as Writer
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandArgumentMismatch as _CommandArgumentMismatch
_CommandArgumentMismatch = _CommandArgumentMismatch
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandArgumentMismatch():
    """dev.ultreon.quantum.api.commands.CommandArgumentMismatch"""
 
    @staticmethod
    def _wrap(java_value: _CommandArgumentMismatch) -> 'CommandArgumentMismatch':
        return CommandArgumentMismatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandArgumentMismatch):
        """
        Dynamic initializer for CommandArgumentMismatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandArgumentMismatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandArgumentMismatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def dumps(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dumps()"""
        return str._wrap(super(CommandArgumentMismatch, self).dumps())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @overload
    def dump(self, arg0: 'Writer'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.Writer)"""
        super(_CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @overload
    def dump(self, arg0: 'File'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.File)"""
        super(_CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def dump(self, arg0: 'OutputStream'):
        """public void dev.ultreon.quantum.api.commands.CommandArgumentMismatch.dump(java.io.OutputStream)"""
        super(_CommandArgumentMismatch, self).dump(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ArrayList', arg2: 'IllegalArgumentException'):
        """public dev.ultreon.quantum.api.commands.CommandArgumentMismatch(java.lang.Class<?>[],java.util.ArrayList<java.lang.Object>,java.lang.IllegalArgumentException)"""
        val = _CommandArgumentMismatch(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandTabCompleter as _CommandTabCompleter
_CommandTabCompleter = _CommandTabCompleter
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter
_CommandParameter = _CommandParameter
import dev.ultreon.quantum.api.commands.CommandParser as _CommandParser
_CommandParser = _CommandParser
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter_ArgumentType
_ArgumentType = _CommandParameter_ArgumentType.ArgumentType
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ArgumentType():
    """dev.ultreon.quantum.api.commands.CommandParameter.ArgumentType"""
 
    @staticmethod
    def _wrap(java_value: _ArgumentType) -> 'ArgumentType':
        return ArgumentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArgumentType):
        """
        Dynamic initializer for ArgumentType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArgumentType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArgumentType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCompleter(self) -> 'CommandTabCompleter':
        """public dev.ultreon.quantum.api.commands.CommandTabCompleter dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getCompleter()"""
        return 'CommandTabCompleter'._wrap(super(ArgumentType, self).getCompleter())

    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifArgType(arg0))

    @override
    @overload
    def getTag(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getTag()"""
        return str._wrap(super(ArgumentType, self).getTag())

    @overload
    def __init__(self, arg0: 'CommandParser', arg1: 'CommandTabCompleter', arg2: 'Class', arg3: str, arg4: bool, arg5: str):
        """public dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType(dev.ultreon.quantum.api.commands.CommandParser<?>,dev.ultreon.quantum.api.commands.CommandTabCompleter,java.lang.Class<?>,java.lang.String,boolean,java.lang.String)"""
        val = _ArgumentType(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), arg5)
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

    @overload
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifText(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.toString()"""
        return str._wrap(super(ArgumentType, self).toString())

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
    def getParser(self) -> 'CommandParser':
        """public dev.ultreon.quantum.api.commands.CommandParser<?> dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getParser()"""
        return 'CommandParser'._wrap(super(ArgumentType, self).getParser())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<?> dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getType()"""
        return 'type.Class'._wrap(super(ArgumentType, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.getComment()"""
        return str._wrap(super(ArgumentType, self).getComment())

    @override
    @overload
    def isOptional(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType.isOptional()"""
        return bool._wrap(super(ArgumentType, self).isOptional())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandTabCompleter
from builtins import str
import dev.ultreon.quantum.api.commands.CommandTabCompleter as _CommandTabCompleter
_CommandTabCompleter = _CommandTabCompleter
from abc import abstractmethod, ABC
 
class CommandTabCompleter():
    """dev.ultreon.quantum.api.commands.CommandTabCompleter"""
 
    @staticmethod
    def _wrap(java_value: _CommandTabCompleter) -> 'CommandTabCompleter':
        return CommandTabCompleter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandTabCompleter):
        """
        Dynamic initializer for CommandTabCompleter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandTabCompleter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandTabCompleter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'CommandReader', arg3: 'String'):
        """public abstract java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandTabCompleter.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,dev.ultreon.quantum.api.commands.CommandReader,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandData
from pyquantum_helper import import_once as _import_once
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.api.commands.CommandStatus as _CommandStatus
_CommandStatus = _CommandStatus
import java.util.Collection as Collection
import dev.ultreon.quantum.api.commands.CommandData as _CommandData
_CommandData = _CommandData
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandTabCompleter as _CommandTabCompleter
_CommandTabCompleter = _CommandTabCompleter
import java.lang.Object as _object
try:
    from pyquantum import registry
except ImportError:
    registry = _import_once("pyquantum.registry")

import java.lang.reflect.Method as _Method
_Method = _Method
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.api.commands.CommandParser as _CommandParser
_CommandParser = _CommandParser
from typing import List
import java.lang.Enum as Enum
import java.util.Set as Set
import java.lang.Enum as _Enum
_Enum = _Enum
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
import java.lang.reflect.Method as Method
from builtins import int
 
class CommandData():
    """dev.ultreon.quantum.api.commands.CommandData"""
 
    @staticmethod
    def _wrap(java_value: _CommandData) -> 'CommandData':
        return CommandData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandData):
        """
        Dynamic initializer for CommandData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sendHelp(self, arg0: str, arg1: 'CommandSender', arg2: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendHelp(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        super(_CommandData, self).sendHelp(arg0, arg1, arg2)

    @overload
    def mapToMethod(self, arg0: 'CommandSpec') -> 'Method':
        """public java.lang.reflect.Method dev.ultreon.quantum.api.commands.CommandData.mapToMethod(dev.ultreon.quantum.api.commands.CommandSpec)"""
        return 'Method'._wrap(super(_CommandData, self).mapToMethod(arg0))

    @overload
    def mapToPerm(self, arg0: 'CommandSpec') -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandData.mapToPerm(dev.ultreon.quantum.api.commands.CommandSpec)"""
        return str._wrap(super(_CommandData, self).mapToPerm(arg0))

    @staticmethod
    @overload
    def registerArgument(arg0: str, arg1: 'CommandParser', arg2: 'CommandTabCompleter', *arg3: object):
        """public static <T> void dev.ultreon.quantum.api.commands.CommandData.registerArgument(java.lang.String,dev.ultreon.quantum.api.commands.CommandParser<T>,dev.ultreon.quantum.api.commands.CommandTabCompleter,T...)"""
        _CommandData.registerArgument(arg0, arg1, arg2, arg3)

    @overload
    def getCommandSpecs(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.api.commands.CommandSpec> dev.ultreon.quantum.api.commands.CommandData.getCommandSpecs()"""
        return 'Collection'._wrap(super(CommandData, self).getCommandSpecs())

    @overload
    def sendUsage(self, arg0: str, arg1: 'CommandSender', arg2: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendUsage(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        super(_CommandData, self).sendUsage(arg0, arg1, arg2)

    @overload
    def setCommandStatus(self, arg0: 'CommandStatus'):
        """public void dev.ultreon.quantum.api.commands.CommandData.setCommandStatus(dev.ultreon.quantum.api.commands.CommandStatus)"""
        super(_CommandData, self).setCommandStatus(arg0)

    @overload
    def description(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.CommandData.description(java.lang.String)"""
        super(_CommandData, self).description(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def onRegister(self, arg0: 'CommandContext'):
        """public void dev.ultreon.quantum.api.commands.CommandData.onRegister(dev.ultreon.quantum.api.commands.CommandContext)"""
        super(_CommandData, self).onRegister(arg0)

    @staticmethod
    @overload
    def dropLastWhile(arg0: 'List', arg1: 'Predicate') -> 'List':
        """public static <T> java.util.List<T> dev.ultreon.quantum.api.commands.CommandData.dropLastWhile(java.util.List<T>,java.util.function.Predicate<T>)"""
        return List._wrap(_CommandData.dropLastWhile(arg0, arg1))

    @staticmethod
    @overload
    def validateArgId(arg0: str) -> bool:
        """public static boolean dev.ultreon.quantum.api.commands.CommandData.validateArgId(java.lang.String)"""
        return bool._wrap(_CommandData.validateArgId(arg0))

    @overload
    def setFlag(self, arg0: 'CommandFlag', arg1: bool):
        """public void dev.ultreon.quantum.api.commands.CommandData.setFlag(dev.ultreon.quantum.api.commands.CommandFlag,boolean)"""
        super(_CommandData, self).setFlag(arg0, _boolean.valueOf(arg1))

    @staticmethod
    @overload
    def readFromFunc(arg0: 'CommandReader', arg1: str, arg2: 'Function') -> object:
        """public static <T> T dev.ultreon.quantum.api.commands.CommandData.readFromFunc(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,java.util.function.Function<dev.ultreon.quantum.util.Identifier, T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(_CommandData.readFromFunc(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getType(arg0: str) -> 'type.Class':
        """public static java.lang.Class<?> dev.ultreon.quantum.api.commands.CommandData.getType(java.lang.String)"""
        return type.Class._wrap(_CommandData.getType(arg0))

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
    def alias(self, arg0: str) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.CommandData.alias(java.lang.String)"""
        return 'CommandData'._wrap(super(_CommandData, self).alias(arg0))

    @overload
    def __init__(self, arg0: 'Command'):
        """public dev.ultreon.quantum.api.commands.CommandData(dev.ultreon.quantum.api.commands.Command)"""
        val = _CommandData(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getParser(arg0: str) -> 'CommandParser':
        """public static dev.ultreon.quantum.api.commands.CommandParser<?> dev.ultreon.quantum.api.commands.CommandData.getParser(java.lang.String)"""
        return CommandParser._wrap(_CommandData.getParser(arg0))

    @staticmethod
    @overload
    def readObject(arg0: 'CommandReader') -> object:
        """public static java.lang.Object dev.ultreon.quantum.api.commands.CommandData.readObject(dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(_CommandData.readObject(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getAliases(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandData.getAliases()"""
        return List[str]._wrap(super(CommandData, self).getAliases())

    @staticmethod
    @overload
    def getTabCompleter(arg0: str) -> 'CommandTabCompleter':
        """public static dev.ultreon.quantum.api.commands.CommandTabCompleter dev.ultreon.quantum.api.commands.CommandData.getTabCompleter(java.lang.String)"""
        return CommandTabCompleter._wrap(_CommandData.getTabCompleter(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOverloadSpecs(self) -> 'Set':
        """public java.util.Set<dev.ultreon.quantum.api.commands.CommandSpec> dev.ultreon.quantum.api.commands.CommandData.getOverloadSpecs()"""
        return 'Set'._wrap(super(CommandData, self).getOverloadSpecs())

    @overload
    def getOverloads(self) -> 'Map':
        """public java.util.Map<dev.ultreon.quantum.api.commands.CommandSpec, java.lang.String> dev.ultreon.quantum.api.commands.CommandData.getOverloads()"""
        return 'Map'._wrap(super(CommandData, self).getOverloads())

    @overload
    def aliases(self, *arg0: str) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.CommandData.aliases(java.lang.String...)"""
        return 'CommandData'._wrap(super(_CommandData, self).aliases(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getOverloadDetails(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> dev.ultreon.quantum.api.commands.CommandData.getOverloadDetails()"""
        return 'Collection'._wrap(super(CommandData, self).getOverloadDetails())

    @staticmethod
    @overload
    def completeObject(arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'CommandReader', arg3: 'String') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.CommandData.completeObject(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,dev.ultreon.quantum.api.commands.CommandReader,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return List._wrap(_CommandData.completeObject(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def readFromEnum(arg0: 'CommandReader', arg1: str, arg2: 'Class') -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T dev.ultreon.quantum.api.commands.CommandData.readFromEnum(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,java.lang.Class<T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return Enum._wrap(_CommandData.readFromEnum(arg0, arg1, arg2))

    @overload
    def getStatus(self) -> 'CommandStatus':
        """public dev.ultreon.quantum.api.commands.CommandStatus dev.ultreon.quantum.api.commands.CommandData.getStatus()"""
        return 'CommandStatus'._wrap(super(CommandData, self).getStatus())

    @overload
    def sendUsage(self, arg0: str, arg1: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandData.sendUsage(java.lang.String,dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandData, self).sendUsage(arg0, arg1)

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

    @staticmethod
    @overload
    def readFromRegistry(arg0: 'CommandReader', arg1: str, arg2: 'Registry') -> object:
        """public static <T> T dev.ultreon.quantum.api.commands.CommandData.readFromRegistry(dev.ultreon.quantum.api.commands.CommandReader,java.lang.String,dev.ultreon.quantum.registry.Registry<T>) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return object._wrap(_CommandData.readFromRegistry(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.DefineCommand
import dev.ultreon.quantum.api.commands.DefineCommand as _DefineCommand
_DefineCommand = _DefineCommand
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class DefineCommand():
    """dev.ultreon.quantum.api.commands.DefineCommand"""
 
    @staticmethod
    def _wrap(java_value: _DefineCommand) -> 'DefineCommand':
        return DefineCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefineCommand):
        """
        Dynamic initializer for DefineCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefineCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefineCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.Argument as _Argument
_Argument = _Argument
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Argument():
    """dev.ultreon.quantum.api.commands.Argument"""
 
    @staticmethod
    def _wrap(java_value: _Argument) -> 'Argument':
        return Argument(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Argument):
        """
        Dynamic initializer for Argument.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Argument__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Argument__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.api.commands.Argument.get()"""
        return object._wrap(super(Argument, self).get())

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

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.api.commands.Argument(T)"""
        val = _Argument(arg0)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSender
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from pyquantum.api.commands import perms
except ImportError:
    perms = _import_once("pyquantum.api.commands.perms")

try:
    from pyquantum.api.commands import output
except ImportError:
    output = _import_once("pyquantum.api.commands.output")

from abc import abstractmethod, ABC
try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

from builtins import bool
import dev.ultreon.quantum.api.commands.output.CommandResult as _CommandResult
_CommandResult = _CommandResult
 
class CommandSender():
    """dev.ultreon.quantum.api.commands.CommandSender"""
 
    @staticmethod
    def _wrap(java_value: _CommandSender) -> 'CommandSender':
        return CommandSender(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandSender):
        """
        Dynamic initializer for CommandSender.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandSender__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandSender__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def hasPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(java.lang.String)"""
        return bool._wrap(super(_CommandSender, self).hasPermission(arg0))

    @abstractmethod
    def hasExplicitPermission(self, arg0: 'Permission'):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        pass

    @abstractmethod
    def getUuid(self, ):
        """public abstract java.util.UUID dev.ultreon.quantum.api.commands.CommandSender.getUuid()"""
        pass

    @overload
    def hasExplicitPermission(self, arg0: str) -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasExplicitPermission(java.lang.String)"""
        return bool._wrap(super(_CommandSender, self).hasExplicitPermission(arg0))

    @overload
    def execute(self, arg0: str, arg1: bool) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String,boolean)"""
        return 'output.CommandResult'._wrap(super(_CommandSender, self).execute(arg0, _boolean.valueOf(arg1)))

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandSender.getName()"""
        pass

    @abstractmethod
    def isAdmin(self, ):
        """public abstract boolean dev.ultreon.quantum.api.commands.CommandSender.isAdmin()"""
        pass

    @overload
    def hasPermission(self, arg0: 'Permission') -> bool:
        """public default boolean dev.ultreon.quantum.api.commands.CommandSender.hasPermission(dev.ultreon.quantum.api.commands.perms.Permission)"""
        return bool._wrap(super(_CommandSender, self).hasPermission(arg0))

    @overload
    def execute(self, arg0: str) -> 'output.CommandResult':
        """public default dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandSender.execute(java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_CommandSender, self).execute(arg0))

    @abstractmethod
    def getPublicName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.CommandSender.getPublicName()"""
        pass

    @abstractmethod
    def sendMessage(self, arg0: 'TextObject'):
        """public abstract void dev.ultreon.quantum.api.commands.CommandSender.sendMessage(dev.ultreon.quantum.text.TextObject)"""
        pass

    @abstractmethod
    def getDisplayName(self, ):
        """public abstract dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.api.commands.CommandSender.getDisplayName()"""
        pass

    @abstractmethod
    def getLocation(self, ):
        """public abstract dev.ultreon.quantum.world.Location dev.ultreon.quantum.api.commands.CommandSender.getLocation()"""
        pass

    @abstractmethod
    def sendMessage(self, arg0: str):
        """public abstract void dev.ultreon.quantum.api.commands.CommandSender.sendMessage(java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandExecuteException
import dev.ultreon.quantum.api.commands.CommandExecuteException as _CommandExecuteException
_CommandExecuteException = _CommandExecuteException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandExecuteException():
    """dev.ultreon.quantum.api.commands.CommandExecuteException"""
 
    @staticmethod
    def _wrap(java_value: _CommandExecuteException) -> 'CommandExecuteException':
        return CommandExecuteException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandExecuteException):
        """
        Dynamic initializer for CommandExecuteException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandExecuteException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandExecuteException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandExecuteException(java.lang.String)"""
        val = _CommandExecuteException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_EndOfArgument
_EndOfArgument = _CommandParseException_EndOfArgument.EndOfArgument
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EndOfArgument():
    """dev.ultreon.quantum.api.commands.CommandParseException.EndOfArgument"""
 
    @staticmethod
    def _wrap(java_value: _EndOfArgument) -> 'EndOfArgument':
        return EndOfArgument(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EndOfArgument):
        """
        Dynamic initializer for EndOfArgument.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EndOfArgument__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EndOfArgument__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument(int)"""
        val = _EndOfArgument(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.ArgumentType$Result
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
import dev.ultreon.quantum.api.commands.ArgumentType as _ArgumentType_Result
_Result = _ArgumentType_Result.Result
import java.lang.Integer as _int
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Result():
    """dev.ultreon.quantum.api.commands.ArgumentType.Result"""
 
    @staticmethod
    def _wrap(java_value: _Result) -> 'Result':
        return Result(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Result):
        """
        Dynamic initializer for Result.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Result__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Result__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = _Result(arg0, arg1)
        self.__wrapper = val

    @overload
    def get(self) -> object:
        """public T dev.ultreon.quantum.api.commands.ArgumentType$Result.get()"""
        return object._wrap(super(Result, self).get())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(T)"""
        val = _Result(arg0)
        self.__wrapper = val

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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.ArgumentType$Result.hasError()"""
        return bool._wrap(super(Result, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.ArgumentType$Result(dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = _Result(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.InvalidCommandMethodError
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.InvalidCommandMethodError as _InvalidCommandMethodError
_InvalidCommandMethodError = _InvalidCommandMethodError
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.lang.reflect.Method as Method
 
class InvalidCommandMethodError():
    """dev.ultreon.quantum.api.commands.InvalidCommandMethodError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCommandMethodError) -> 'InvalidCommandMethodError':
        return InvalidCommandMethodError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCommandMethodError):
        """
        Dynamic initializer for InvalidCommandMethodError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCommandMethodError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCommandMethodError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.String)"""
        val = _InvalidCommandMethodError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Method'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.reflect.Method)"""
        val = _InvalidCommandMethodError(arg0)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

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
    def __init__(self, arg0: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.Throwable)"""
        val = _InvalidCommandMethodError(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

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
    def __init__(self, arg0: 'Method', arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.reflect.Method,java.lang.Throwable)"""
        val = _InvalidCommandMethodError(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public dev.ultreon.quantum.api.commands.InvalidCommandMethodError(java.lang.String,java.lang.Throwable)"""
        val = _InvalidCommandMethodError(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Range
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.Range as _Range
_Range = _Range
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.collections.v0.iterator.IntIterable as _IntIterable
_IntIterable = _IntIterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
try:
    from pycorelibs.collections.v0 import iterator
except ImportError:
    iterator = _import_once("pycorelibs.collections.v0.iterator")

import java.lang.String as _String
_String = _String
import dev.ultreon.libs.collections.v0.iterator.IntIterator as _IntIterator
_IntIterator = _IntIterator
try:
    from pycorelibs.functions.v0 import consumer
except ImportError:
    consumer = _import_once("pycorelibs.functions.v0.consumer")

import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Range():
    """dev.ultreon.quantum.api.commands.Range"""
 
    @staticmethod
    def _wrap(java_value: _Range) -> 'Range':
        return Range(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Range):
        """
        Dynamic initializer for Range.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Range__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Range__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def forEach(self, arg0: 'IntConsumer'):
        """public default void dev.ultreon.libs.collections.v0.iterator.IntIterable.forEach(dev.ultreon.libs.functions.v0.consumer.IntConsumer)"""
        super(_iterator.IntIterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'iterator.IntIterator':
        """public dev.ultreon.libs.collections.v0.iterator.IntIterator dev.ultreon.quantum.api.commands.Range.iterator()"""
        return 'iterator.IntIterator'._wrap(super(Range, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public dev.ultreon.quantum.api.commands.Range(int,int,int)"""
        val = _Range(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.api.commands.Range(int,int)"""
        val = _Range(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.Range(int)"""
        val = _Range(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandSpec
from builtins import str
import dev.ultreon.quantum.api.commands.CommandSpec as _CommandSpec
_CommandSpec = _CommandSpec
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class CommandSpec():
    """dev.ultreon.quantum.api.commands.CommandSpec"""
 
    @staticmethod
    def _wrap(java_value: _CommandSpec) -> 'CommandSpec':
        return CommandSpec(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandSpec):
        """
        Dynamic initializer for CommandSpec.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandSpec__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandSpec__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def commandName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandSpec.commandName()"""
        return str._wrap(super(CommandSpec, self).commandName())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandSpec.toString()"""
        return str._wrap(super(CommandSpec, self).toString())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandSpec.hashCode()"""
        return int._wrap(super(CommandSpec, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def arguments(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.CommandParameter> dev.ultreon.quantum.api.commands.CommandSpec.arguments()"""
        return 'List'._wrap(super(CommandSpec, self).arguments())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: 'List'):
        """public dev.ultreon.quantum.api.commands.CommandSpec(java.lang.String,java.util.List<dev.ultreon.quantum.api.commands.CommandParameter>)"""
        val = _CommandSpec(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandSpec.equals(java.lang.Object)"""
        return bool._wrap(super(_CommandSpec, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.TabCompleting
from pyquantum_helper import import_once as _import_once
import java.util.UUID as UUID
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.api.commands.TabCompleting as _TabCompleting
_TabCompleting = _TabCompleting
import java.util.Collection as Collection
try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = _import_once("pyquantum.api.commands.selector")

import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
from builtins import bool
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import java.lang.Number as Number
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
try:
    from pyquantum.server import player
except ImportError:
    player = _import_once("pyquantum.server.player")

import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TabCompleting():
    """dev.ultreon.quantum.api.commands.TabCompleting"""
 
    @staticmethod
    def _wrap(java_value: _TabCompleting) -> 'TabCompleting':
        return TabCompleting(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TabCompleting):
        """
        Dynamic initializer for TabCompleting.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TabCompleting__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TabCompleting__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def booleans(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.booleans(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.booleans(arg0, arg1))

    @staticmethod
    @overload
    def ruleNames(arg0: 'List', arg1: 'List', arg2: str) -> 'List':
        """public static <T extends dev.ultreon.quantum.gamerule.Rule<?>> java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.ruleNames(java.util.List<java.lang.String>,java.util.List<T>,java.lang.String)"""
        return List._wrap(_TabCompleting.ruleNames(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def hex(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.hex(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.hex(arg0, arg1))

    @staticmethod
    @overload
    def numbers(arg0: str, *arg1: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.lang.String,java.lang.Number...)"""
        return List._wrap(_TabCompleting.numbers(arg0, arg1))

    @staticmethod
    @overload
    def entityTypes(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityTypes(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.entityTypes(arg0, arg1))

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: 'Identifier', arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,dev.ultreon.quantum.util.Identifier,java.lang.String)"""
        _TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def players(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.players(java.lang.String)"""
        return List._wrap(_TabCompleting.players(arg0))

    @staticmethod
    @overload
    def mods(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.mods(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.mods(arg0, arg1))

    @staticmethod
    @overload
    def numbers(arg0: 'List', arg1: str, *arg2: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.util.List<java.lang.String>,java.lang.String,java.lang.Number...)"""
        return List._wrap(_TabCompleting.numbers(arg0, arg1, arg2))

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.TabCompleting()"""
        val = _TabCompleting()
        self.__wrapper = val

    @staticmethod
    @overload
    def offlinePlayerUuids(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.offlinePlayerUuids(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.offlinePlayerUuids(arg0, arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.TabCompleting()"""
        val = _TabCompleting()
        self.__wrapper = val

    @staticmethod
    @overload
    def strings(arg0: str, *arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.strings(arg0, arg1))

    @staticmethod
    @overload
    def prefixed(arg0: str, arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.lang.String,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.prefixed(arg0, arg1, arg2))

    @staticmethod
    @overload
    def prefixed(arg0: str, arg1: str, arg2: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List._wrap(_TabCompleting.prefixed(arg0, arg1, arg2))

    @staticmethod
    @overload
    def difficulties(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.difficulties(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.difficulties(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def prefixed(arg0: 'List', arg1: str, arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.util.List<java.lang.String>,java.lang.String,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.prefixed(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def selectors(arg0: 'SelectorKey', arg1: str, arg2: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List._wrap(_TabCompleting.selectors(arg0, arg1, arg2))

    @staticmethod
    @overload
    def strings(arg0: 'List', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.util.List<java.lang.String>,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.strings(arg0, arg1, arg2))

    @staticmethod
    @overload
    def items(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.items(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.items(arg0, arg1))

    @staticmethod
    @overload
    def ints(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.ints(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.ints(arg0, arg1))

    @staticmethod
    @overload
    def strings(arg0: str, *arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.lang.String,char...)"""
        return List._wrap(_TabCompleting.strings(arg0, arg1))

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: str, arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.lang.String,java.lang.String)"""
        _TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def selectors(arg0: 'SelectorKey', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.selectors(arg0, arg1, arg2))

    @staticmethod
    @overload
    def numbers(arg0: 'List', arg1: str, arg2: int, *arg3: 'Number') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.numbers(java.util.List<java.lang.String>,java.lang.String,int,java.lang.Number...)"""
        return List._wrap(_TabCompleting.numbers(arg0, arg1, _int.valueOf(arg2), arg3))

    @staticmethod
    @overload
    def prefixed(arg0: 'List', arg1: str, arg2: str, arg3: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.prefixed(java.util.List<java.lang.String>,java.lang.String,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List._wrap(_TabCompleting.prefixed(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def entityUuids(arg0: 'List', arg1: str, arg2: 'Class') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityUuids(java.util.List<java.lang.String>,java.lang.String,java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>)"""
        return List._wrap(_TabCompleting.entityUuids(arg0, arg1, arg2))

    @staticmethod
    @overload
    def onlinePlayers(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.onlinePlayers(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.onlinePlayers(arg0, arg1))

    @staticmethod
    @overload
    def blocks(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.blocks(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.blocks(arg0, arg1))

    @staticmethod
    @overload
    def selectors(arg0: 'List', arg1: 'SelectorKey', arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.selectors(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def entityTypes(arg0: 'List', arg1: str, arg2: bool) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityTypes(java.util.List<java.lang.String>,java.lang.String,boolean)"""
        return List._wrap(_TabCompleting.entityTypes(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def entityUuids(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityUuids(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.entityUuids(arg0, arg1))

    @staticmethod
    @overload
    def keys(arg0: str, arg1: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.keys(java.lang.String,java.util.Collection<dev.ultreon.quantum.util.Identifier>)"""
        return List._wrap(_TabCompleting.keys(arg0, arg1))

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: 'UUID', arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.util.UUID,java.lang.String)"""
        _TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @staticmethod
    @overload
    def addIfStartsWith(arg0: 'Collection', arg1: object, arg2: str):
        """public static void dev.ultreon.quantum.api.commands.TabCompleting.addIfStartsWith(java.util.Collection<java.lang.String>,java.lang.Object,java.lang.String)"""
        _TabCompleting.addIfStartsWith(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def players(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.players(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.players(arg0, arg1))

    @staticmethod
    @overload
    def entityIds(arg0: 'List', arg1: 'ServerWorld', arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.entityIds(java.util.List<java.lang.String>,dev.ultreon.quantum.world.ServerWorld,java.lang.String)"""
        return List._wrap(_TabCompleting.entityIds(arg0, arg1, arg2))

    @staticmethod
    @overload
    def forceToString(*arg0: str) -> List[str]:
        """public static java.lang.String[] dev.ultreon.quantum.api.commands.TabCompleting.forceToString(char...)"""
        return List[str]._wrap(_TabCompleting.forceToString(arg0))

    @staticmethod
    @overload
    def doubles(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.doubles(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.doubles(arg0, arg1))

    @staticmethod
    @overload
    def worlds(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.worlds(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.worlds(arg0, arg1))

    @staticmethod
    @overload
    def variables(arg0: 'ArrayList', arg1: str, arg2: 'ServerPlayer', arg3: 'Class') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.variables(java.util.ArrayList<java.lang.Object>,java.lang.String,dev.ultreon.quantum.server.player.ServerPlayer,java.lang.Class<?>)"""
        return List._wrap(_TabCompleting.variables(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def worldIds(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.worldIds(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.worldIds(arg0, arg1))

    @staticmethod
    @overload
    def subCommand(arg0: 'List', arg1: 'CommandSender', arg2: str, *arg3: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.subCommand(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String...)"""
        return List._wrap(_TabCompleting.subCommand(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def offlinePlayers(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.offlinePlayers(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.offlinePlayers(arg0, arg1))

    @staticmethod
    @overload
    def selectors(arg0: 'List', arg1: 'SelectorKey', arg2: str, arg3: 'Collection') -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.selectors(java.util.List<java.lang.String>,dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,java.util.Collection<java.lang.String>)"""
        return List._wrap(_TabCompleting.selectors(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def strings(arg0: 'List', arg1: str, *arg2: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.strings(java.util.List<java.lang.String>,java.lang.String,char...)"""
        return List._wrap(_TabCompleting.strings(arg0, arg1, arg2))

    @staticmethod
    @overload
    def onlinePlayers(arg0: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.onlinePlayers(java.lang.String)"""
        return List._wrap(_TabCompleting.onlinePlayers(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def commands(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.commands(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.commands(arg0, arg1))

    @staticmethod
    @overload
    def biomes(arg0: 'List', arg1: str) -> 'List':
        """public static java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.TabCompleting.biomes(java.util.List<java.lang.String>,java.lang.String)"""
        return List._wrap(_TabCompleting.biomes(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.StringIO
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.StringIO as _StringIO
_StringIO = _StringIO
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringIO():
    """dev.ultreon.quantum.api.commands.StringIO"""
 
    @staticmethod
    def _wrap(java_value: _StringIO) -> 'StringIO':
        return StringIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringIO):
        """
        Dynamic initializer for StringIO.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringIO__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringIO__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def readString(self, arg0: int) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.StringIO.readString(int) throws java.io.EOFException"""
        return str._wrap(super(_StringIO, self).readString(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def readChars(self, arg0: int) -> List[str]:
        """public char[] dev.ultreon.quantum.api.commands.StringIO.readChars(int) throws java.io.EOFException"""
        return List[str]._wrap(super(_StringIO, self).readChars(_int.valueOf(arg0)))

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.StringIO(java.lang.String)"""
        val = _StringIO(arg0)
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

    @overload
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.StringIO.readChar() throws java.io.EOFException"""
        return str._wrap(super(StringIO, self).readChar())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getOffset(self) -> int:
        """public int dev.ultreon.quantum.api.commands.StringIO.getOffset()"""
        return int._wrap(super(StringIO, self).getOffset())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isNextEOF(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.StringIO.isNextEOF()"""
        return bool._wrap(super(StringIO, self).isNextEOF())

    @overload
    def isEOF(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.StringIO.isEOF()"""
        return bool._wrap(super(StringIO, self).isEOF())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.OverloadContent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.api.commands.OverloadContent as _OverloadContent
_OverloadContent = _OverloadContent
import java.lang.Integer as _int
import java.util.function.Function as Function
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OverloadContent():
    """dev.ultreon.quantum.api.commands.OverloadContent"""
 
    @staticmethod
    def _wrap(java_value: _OverloadContent) -> 'OverloadContent':
        return OverloadContent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OverloadContent):
        """
        Dynamic initializer for OverloadContent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OverloadContent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OverloadContent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def of(arg0: str, arg1: int, arg2: 'IndexedCommandSpecValues') -> 'OverloadContent':
        """public static dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.of(java.lang.String,int,dev.ultreon.quantum.api.commands.IndexedCommandSpecValues)"""
        return OverloadContent._wrap(_OverloadContent.of(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.OverloadContent.toString()"""
        return str._wrap(super(OverloadContent, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.OverloadContent.equals(java.lang.Object)"""
        return bool._wrap(super(_OverloadContent, self).equals(arg0))

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
    def __init__(self, arg0: str, arg1: int, arg2: 'IndexedCommandSpecValues'):
        """public dev.ultreon.quantum.api.commands.OverloadContent(java.lang.String,int,dev.ultreon.quantum.api.commands.IndexedCommandSpecValues)"""
        val = _OverloadContent(arg0, _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.OverloadContent.hashCode()"""
        return int._wrap(super(OverloadContent, self).hashCode())

    @overload
    def mapIndexedValues(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapIndexedValues(java.util.function.Function<dev.ultreon.quantum.api.commands.IndexedCommandSpecValues, dev.ultreon.quantum.api.commands.IndexedCommandSpecValues>)"""
        return 'OverloadContent'._wrap(super(_OverloadContent, self).mapIndexedValues(arg0))

    @overload
    def mapSize(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapSize(java.util.function.Function<java.lang.Integer, java.lang.Integer>)"""
        return 'OverloadContent'._wrap(super(_OverloadContent, self).mapSize(arg0))

    @overload
    def mapName(self, arg0: 'Function') -> 'OverloadContent':
        """public dev.ultreon.quantum.api.commands.OverloadContent dev.ultreon.quantum.api.commands.OverloadContent.mapName(java.util.function.Function<java.lang.String, java.lang.String>)"""
        return 'OverloadContent'._wrap(super(_OverloadContent, self).mapName(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandParseException():
    """dev.ultreon.quantum.api.commands.CommandParseException"""
 
    @staticmethod
    def _wrap(java_value: _CommandParseException) -> 'CommandParseException':
        return CommandParseException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandParseException):
        """
        Dynamic initializer for CommandParseException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandParseException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandParseException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException(java.lang.String,int)"""
        val = _CommandParseException(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandParseException(java.lang.String)"""
        val = _CommandParseException(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'CommandError', arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException(dev.ultreon.quantum.api.commands.error.CommandError,int)"""
        val = _CommandParseException(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotFound
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_NotFound
_NotFound = _CommandParseException_NotFound.NotFound
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotFound():
    """dev.ultreon.quantum.api.commands.CommandParseException.NotFound"""
 
    @staticmethod
    def _wrap(java_value: _NotFound) -> 'NotFound':
        return NotFound(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotFound):
        """
        Dynamic initializer for NotFound.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotFound__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotFound__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotFound(java.lang.String,int)"""
        val = _NotFound(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: object, arg2: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotFound(java.lang.String,java.lang.Object,int)"""
        val = _NotFound(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.OverloadConflictException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.OverloadConflictException as _OverloadConflictException
_OverloadConflictException = _OverloadConflictException
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OverloadConflictException():
    """dev.ultreon.quantum.api.commands.OverloadConflictException"""
 
    @staticmethod
    def _wrap(java_value: _OverloadConflictException) -> 'OverloadConflictException':
        return OverloadConflictException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OverloadConflictException):
        """
        Dynamic initializer for OverloadConflictException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OverloadConflictException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OverloadConflictException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, *arg0: str):
        """public dev.ultreon.quantum.api.commands.OverloadConflictException(java.lang.String...)"""
        val = _OverloadConflictException(arg0)
        self.__wrapper = val

    @overload
    def getAliases(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.OverloadConflictException.getAliases()"""
        return List[str]._wrap(super(OverloadConflictException, self).getAliases())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCrashReport$Details
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
import dev.ultreon.quantum.api.commands.CommandCrashReport as _CommandCrashReport_Details
_Details = _CommandCrashReport_Details.Details
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Details():
    """dev.ultreon.quantum.api.commands.CommandCrashReport.Details"""
 
    @staticmethod
    def _wrap(java_value: _Details) -> 'Details':
        return Details(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Details):
        """
        Dynamic initializer for Details.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Details__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Details__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.CommandCrashReport$Details(java.lang.String,java.lang.String)"""
        val = _Details(arg0, arg1)
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

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.id()"""
        return str._wrap(super(Details, self).id())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandCrashReport$Details.hashCode()"""
        return int._wrap(super(Details, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.toString()"""
        return str._wrap(super(Details, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def report(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandCrashReport$Details.report()"""
        return str._wrap(super(Details, self).report())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandCrashReport$Details.equals(java.lang.Object)"""
        return bool._wrap(super(_Details, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.PositionCommand
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
import dev.ultreon.quantum.api.commands.PositionCommand as _PositionCommand
_PositionCommand = _PositionCommand
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PositionCommand():
    """dev.ultreon.quantum.api.commands.PositionCommand"""
 
    @staticmethod
    def _wrap(java_value: _PositionCommand) -> 'PositionCommand':
        return PositionCommand(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PositionCommand):
        """
        Dynamic initializer for PositionCommand.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PositionCommand__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PositionCommand__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def requireLivingEntity(self):
        """public void dev.ultreon.quantum.api.commands.Command.requireLivingEntity()"""
        super(Command, self).requireLivingEntity()

    @override
    @overload
    def wip(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.wip()"""
        return 'output.CommandResult'._wrap(super(Command, self).wip())

    @override
    @overload
    def data(self) -> 'CommandData':
        """public dev.ultreon.quantum.api.commands.CommandData dev.ultreon.quantum.api.commands.Command.data()"""
        return 'CommandData'._wrap(super(Command, self).data())

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
    def outdated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.outdated()"""
        return 'output.CommandResult'._wrap(super(Command, self).outdated())

    @override
    @overload
    def setNeedLivingEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedLivingEntity(boolean)"""
        super(_Command, self).setNeedLivingEntity(_boolean.valueOf(arg0))

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
    def getRequiredPermission(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Command.getRequiredPermission()"""
        return str._wrap(super(Command, self).getRequiredPermission())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.PositionCommand()"""
        val = _PositionCommand()
        self.__wrapper = val

    @override
    @overload
    def deprecated(self) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.deprecated()"""
        return 'output.CommandResult'._wrap(super(Command, self).deprecated())

        @staticmethod
        @overload
        def runCommandLoaders():
            """public static void dev.ultreon.quantum.api.commands.Command.runCommandLoaders()"""
            _Command.runCommandLoaders()

    @overload
    def onTabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Command.onTabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'List'._wrap(super(_Command, self).onTabComplete(arg0, arg1, arg2, arg3))

    @overload
    def warningMessage(self, arg0: 'MessageCode', arg1: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.warningMessage(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_Command, self).warningMessage(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getRequiresOperator(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Command.getRequiresOperator()"""
        return bool._wrap(super(Command, self).getRequiresOperator())

    @overload
    def executeSecond(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.PositionCommand.executeSecond(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_PositionCommand, self).executeSecond(arg0, arg1, arg2))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def onCommand(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String') -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.Command.onCommand(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        return 'output.CommandResult'._wrap(super(_Command, self).onCommand(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.PositionCommand()"""
        val = _PositionCommand()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setNeedPlayer(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedPlayer(boolean)"""
        super(_Command, self).setNeedPlayer(_boolean.valueOf(arg0))

    @override
    @overload
    def setNeedEntity(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.Command.setNeedEntity(boolean)"""
        super(_Command, self).setNeedEntity(_boolean.valueOf(arg0))

    @overload
    def executeFirst(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'output.CommandResult':
        """public dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.PositionCommand.executeFirst(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return 'output.CommandResult'._wrap(super(_PositionCommand, self).executeFirst(arg0, arg1, arg2))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandContext
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
import dev.ultreon.quantum.api.commands.CommandContext as _CommandContext
_CommandContext = _CommandContext
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandContext():
    """dev.ultreon.quantum.api.commands.CommandContext"""
 
    @staticmethod
    def _wrap(java_value: _CommandContext) -> 'CommandContext':
        return CommandContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandContext):
        """
        Dynamic initializer for CommandContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandContext.equals(java.lang.Object)"""
        return bool._wrap(super(_CommandContext, self).equals(arg0))

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.CommandContext(java.lang.String)"""
        val = _CommandContext(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandContext.hashCode()"""
        return int._wrap(super(CommandContext, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandContext.toString()"""
        return str._wrap(super(CommandContext, self).toString())

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

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandContext.name()"""
        return str._wrap(super(CommandContext, self).name()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Perm
import dev.ultreon.quantum.api.commands.Perm as _Perm
_Perm = _Perm
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class Perm():
    """dev.ultreon.quantum.api.commands.Perm"""
 
    @staticmethod
    def _wrap(java_value: _Perm) -> 'Perm':
        return Perm(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Perm):
        """
        Dynamic initializer for Perm.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Perm__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Perm__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
try:
    from pyquantum.api.commands import selector
except ImportError:
    selector = _import_once("pyquantum.api.commands.selector")

import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
import dev.ultreon.quantum.api.commands.CommandReader as _CommandReader
_CommandReader = _CommandReader
import dev.ultreon.quantum.api.commands.CommandSender as _CommandSender
_CommandSender = _CommandSender
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
import dev.ultreon.quantum.api.commands.selector.Selector as _Selector
_Selector = _Selector
import java.math.BigDecimal as BigDecimal
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandReader():
    """dev.ultreon.quantum.api.commands.CommandReader"""
 
    @staticmethod
    def _wrap(java_value: _CommandReader) -> 'CommandReader':
        return CommandReader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandReader):
        """
        Dynamic initializer for CommandReader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandReader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandReader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSender(self) -> 'CommandSender':
        """public dev.ultreon.quantum.api.commands.CommandSender dev.ultreon.quantum.api.commands.CommandReader.getSender()"""
        return 'CommandSender'._wrap(super(CommandReader, self).getSender())

    @overload
    def getArgument(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getArgument()"""
        return str._wrap(super(CommandReader, self).getArgument())

    @overload
    def readString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readString() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str._wrap(super(CommandReader, self).readString())

    @overload
    def readId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.api.commands.CommandReader.readId() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'util.Identifier'._wrap(super(CommandReader, self).readId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def readRemaining(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readRemaining() throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return str._wrap(super(CommandReader, self).readRemaining())

    @overload
    def nextSplit(self, arg0: str) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandReader.nextSplit(java.lang.String) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return List[str]._wrap(super(_CommandReader, self).nextSplit(arg0))

    @overload
    def isAtStartEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtStartEndOfArg()"""
        return bool._wrap(super(CommandReader, self).isAtStartEndOfArg())

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
    def readChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.readChar() throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return str._wrap(super(CommandReader, self).readChar())

    @overload
    def readBoolean(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.readBoolean() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return bool._wrap(super(CommandReader, self).readBoolean())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def tryNextArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.tryNextArg() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return bool._wrap(super(CommandReader, self).tryNextArg())

    @overload
    def getCurrent(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.getCurrent()"""
        return int._wrap(super(CommandReader, self).getCurrent())

    @overload
    def isAtLastCharInArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtLastCharInArg()"""
        return bool._wrap(super(CommandReader, self).isAtLastCharInArg())

    @overload
    def readByteHex(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readByteHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readByteHex())

    @overload
    def readMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readMessage() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str._wrap(super(CommandReader, self).readMessage())

    @overload
    def readBigDecimal(self) -> 'BigDecimal':
        """public java.math.BigDecimal dev.ultreon.quantum.api.commands.CommandReader.readBigDecimal() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return _transform(super(CommandReader, self).readBigDecimal()).'BigDecimal'Value()

    @overload
    def isAtEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtEndOfArg()"""
        return bool._wrap(super(CommandReader, self).isAtEndOfArg())

    @overload
    def isAtEndOfCmd(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtEndOfCmd()"""
        return bool._wrap(super(CommandReader, self).isAtEndOfCmd())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getOffset(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.getOffset()"""
        return int._wrap(super(CommandReader, self).getOffset())

    @overload
    def back(self):
        """public void dev.ultreon.quantum.api.commands.CommandReader.back() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        super(CommandReader, self).back()

    @overload
    def getCommandline(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommandline()"""
        return str._wrap(super(CommandReader, self).getCommandline())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def readDouble(self) -> float:
        """public double dev.ultreon.quantum.api.commands.CommandReader.readDouble() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return float._wrap(super(CommandReader, self).readDouble())

    @overload
    def readByte(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readByte() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readByte())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def readShort(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readShort() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readShort())

    @overload
    def readIntHex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.readIntHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readIntHex())

    @overload
    def readBigIntegerHex(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.quantum.api.commands.CommandReader.readBigIntegerHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return _transform(super(CommandReader, self).readBigIntegerHex()).'BigInteger'Value()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str, arg2: 'String'):
        """public dev.ultreon.quantum.api.commands.CommandReader(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String[])"""
        val = _CommandReader(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def getArguments(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandReader.getArguments()"""
        return List[str]._wrap(super(CommandReader, self).getArguments())

    @staticmethod
    @overload
    def get() -> 'CommandReader':
        """public static dev.ultreon.quantum.api.commands.CommandReader dev.ultreon.quantum.api.commands.CommandReader.get()"""
        return CommandReader._wrap(_CommandReader.get())

    @overload
    def isAtLastCmd(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtLastCmd()"""
        return bool._wrap(super(CommandReader, self).isAtLastCmd())

    @overload
    def isAtStartOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtStartOfArg()"""
        return bool._wrap(super(CommandReader, self).isAtStartOfArg())

    @overload
    def getLastChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.getLastChar()"""
        return str._wrap(super(CommandReader, self).getLastChar())

    @overload
    def readShortHex(self) -> int:
        """public short dev.ultreon.quantum.api.commands.CommandReader.readShortHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readShortHex())

    @overload
    def readUntil(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readUntil(char) throws dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument"""
        return str._wrap(super(_CommandReader, self).readUntil(_char.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isAtHardEndOfArg(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandReader.isAtHardEndOfArg()"""
        return bool._wrap(super(CommandReader, self).isAtHardEndOfArg())

    @overload
    def getCommand(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommand()"""
        return str._wrap(super(CommandReader, self).getCommand())

    @overload
    def getCommandlineArgs(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.getCommandlineArgs()"""
        return str._wrap(super(CommandReader, self).getCommandlineArgs())

    @overload
    def readMessageUntil(self, arg0: str, arg1: bool) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandReader.readMessageUntil(char,boolean) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return str._wrap(super(_CommandReader, self).readMessageUntil(_char.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def readLongHex(self) -> int:
        """public long dev.ultreon.quantum.api.commands.CommandReader.readLongHex() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readLongHex())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getCurChar(self) -> str:
        """public char dev.ultreon.quantum.api.commands.CommandReader.getCurChar()"""
        return str._wrap(super(CommandReader, self).getCurChar())

    @overload
    def readLong(self) -> int:
        """public long dev.ultreon.quantum.api.commands.CommandReader.readLong() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readLong())

    @overload
    def readInt(self) -> int:
        """public int dev.ultreon.quantum.api.commands.CommandReader.readInt() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return int._wrap(super(CommandReader, self).readInt())

    @overload
    def readFloat(self) -> float:
        """public float dev.ultreon.quantum.api.commands.CommandReader.readFloat() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return float._wrap(super(CommandReader, self).readFloat())

    @overload
    def readBigInteger(self) -> 'BigInteger':
        """public java.math.BigInteger dev.ultreon.quantum.api.commands.CommandReader.readBigInteger() throws dev.ultreon.quantum.api.commands.CommandParseException$NotAtStartOfArg,dev.ultreon.quantum.api.commands.CommandParseException$NotADigit,dev.ultreon.quantum.api.commands.CommandParseException$NotANumber,dev.ultreon.quantum.api.commands.CommandParseException$EndOfArgument,dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg"""
        return _transform(super(CommandReader, self).readBigInteger()).'BigInteger'Value()

    @overload
    def readSelector(self) -> 'selector.Selector':
        """public dev.ultreon.quantum.api.commands.selector.Selector dev.ultreon.quantum.api.commands.CommandReader.readSelector() throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return 'selector.Selector'._wrap(super(CommandReader, self).readSelector()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.MessageCode
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
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
 
class MessageCode():
    """dev.ultreon.quantum.api.commands.MessageCode"""
 
    @staticmethod
    def _wrap(java_value: _MessageCode) -> 'MessageCode':
        return MessageCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageCode):
        """
        Dynamic initializer for MessageCode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageCode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageCode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.MessageCode.getCode()"""
        return int._wrap(super(MessageCode, self).getCode())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'MessageCode':
        """public static dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.MessageCode.valueOf(java.lang.String)"""
        return MessageCode._wrap(_MessageCode.valueOf(arg0))

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

    @staticmethod
    @overload
    def values() -> List['MessageCode']:
        """public static dev.ultreon.quantum.api.commands.MessageCode[] dev.ultreon.quantum.api.commands.MessageCode.values()"""
        return List[MessageCode]._wrap(_MessageCode.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getId(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.MessageCode.getId()"""
        return str._wrap(super(MessageCode, self).getId())


MessageCode.NOT_FOUND = MessageCode._wrap(_NOT_FOUND.NOT_FOUND)

MessageCode.SERVER_ERROR = MessageCode._wrap(_SERVER_ERROR.SERVER_ERROR)

MessageCode.NEED_PLAYER = MessageCode._wrap(_NEED_PLAYER.NEED_PLAYER)

MessageCode.CONFLICT = MessageCode._wrap(_CONFLICT.CONFLICT)

MessageCode.TOO_MANY_ARGS = MessageCode._wrap(_TOO_MANY_ARGS.TOO_MANY_ARGS)

MessageCode.NEED_CONSOLE = MessageCode._wrap(_NEED_CONSOLE.NEED_CONSOLE)

MessageCode.DEPRECATED = MessageCode._wrap(_DEPRECATED.DEPRECATED)

MessageCode.REJECTED = MessageCode._wrap(_REJECTED.REJECTED)

MessageCode.OVERFLOW = MessageCode._wrap(_OVERFLOW.OVERFLOW)

MessageCode.OUTDATED = MessageCode._wrap(_OUTDATED.OUTDATED)

MessageCode.INVALID_VALUE = MessageCode._wrap(_INVALID_VALUE.INVALID_VALUE)

MessageCode.WIP = MessageCode._wrap(_WIP.WIP)

MessageCode.COMMAND_OUTPUT_DETECTED = MessageCode._wrap(_COMMAND_OUTPUT_DETECTED.COMMAND_OUTPUT_DETECTED)

MessageCode.NOT_OP = MessageCode._wrap(_NOT_OP.NOT_OP)

MessageCode.IMPOSSIBLE = MessageCode._wrap(_IMPOSSIBLE.IMPOSSIBLE)

MessageCode.DANGEROUS = MessageCode._wrap(_DANGEROUS.DANGEROUS)

MessageCode.NO_SELECTION = MessageCode._wrap(_NO_SELECTION.NO_SELECTION)

MessageCode.HACKER = MessageCode._wrap(_HACKER.HACKER)

MessageCode.NO_PERMISSION = MessageCode._wrap(_NO_PERMISSION.NO_PERMISSION)

MessageCode.CANNOT_BE_SELF = MessageCode._wrap(_CANNOT_BE_SELF.CANNOT_BE_SELF)

MessageCode.DOES_NOT_MAKE_SENSE = MessageCode._wrap(_DOES_NOT_MAKE_SENSE.DOES_NOT_MAKE_SENSE)

MessageCode.OUT_OF_RANGE = MessageCode._wrap(_OUT_OF_RANGE.OUT_OF_RANGE)

MessageCode.OVERLOAD = MessageCode._wrap(_OVERLOAD.OVERLOAD)

MessageCode.GENERIC = MessageCode._wrap(_GENERIC.GENERIC)

MessageCode.TOO_FEW_ARGS = MessageCode._wrap(_TOO_FEW_ARGS.TOO_FEW_ARGS)

MessageCode.EXPERIMENTAL = MessageCode._wrap(_EXPERIMENTAL.EXPERIMENTAL)

MessageCode.EDIT_MODE = MessageCode._wrap(_EDIT_MODE.EDIT_MODE)

MessageCode.EMPTY = MessageCode._wrap(_EMPTY.EMPTY)

MessageCode.NO_TARGET = MessageCode._wrap(_NO_TARGET.NO_TARGET)

MessageCode.NOT_FOUND_IN_WORLD = MessageCode._wrap(_NOT_FOUND_IN_WORLD.NOT_FOUND_IN_WORLD)

MessageCode.COOLDOWN = MessageCode._wrap(_COOLDOWN.COOLDOWN)

MessageCode.SELECTOR_TOO_SMALL = MessageCode._wrap(_SELECTOR_TOO_SMALL.SELECTOR_TOO_SMALL)

MessageCode.NEED_ENTITY = MessageCode._wrap(_NEED_ENTITY.NEED_ENTITY)

MessageCode.ACCESS_DENIED = MessageCode._wrap(_ACCESS_DENIED.ACCESS_DENIED) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParser
from abc import abstractmethod, ABC
import dev.ultreon.quantum.api.commands.CommandParser as _CommandParser
_CommandParser = _CommandParser
 
class CommandParser():
    """dev.ultreon.quantum.api.commands.CommandParser"""
 
    @staticmethod
    def _wrap(java_value: _CommandParser) -> 'CommandParser':
        return CommandParser(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandParser):
        """
        Dynamic initializer for CommandParser.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandParser__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandParser__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def parse(self, arg0: 'CommandReader'):
        """public abstract T dev.ultreon.quantum.api.commands.CommandParser.parse(dev.ultreon.quantum.api.commands.CommandReader) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandFlag
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.output.BasicCommandResult as _BasicCommandResult_MessageType
_MessageType = _BasicCommandResult_MessageType.MessageType
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
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
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandFlag as _CommandFlag
_CommandFlag = _CommandFlag
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandFlag():
    """dev.ultreon.quantum.api.commands.CommandFlag"""
 
    @staticmethod
    def _wrap(java_value: _CommandFlag) -> 'CommandFlag':
        return CommandFlag(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandFlag):
        """
        Dynamic initializer for CommandFlag.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandFlag__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandFlag__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getDescription(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandFlag.getDescription()"""
        return str._wrap(super(CommandFlag, self).getDescription())

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

    @staticmethod
    @overload
    def values() -> List['CommandFlag']:
        """public static dev.ultreon.quantum.api.commands.CommandFlag[] dev.ultreon.quantum.api.commands.CommandFlag.values()"""
        return List[CommandFlag]._wrap(_CommandFlag.values())

    @overload
    def getMessageType(self) -> 'output.BasicCommandResult$MessageType':
        """public dev.ultreon.quantum.api.commands.output.BasicCommandResult$MessageType dev.ultreon.quantum.api.commands.CommandFlag.getMessageType()"""
        return 'output.BasicCommandResult$MessageType'._wrap(super(CommandFlag, self).getMessageType())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'CommandFlag':
        """public static dev.ultreon.quantum.api.commands.CommandFlag dev.ultreon.quantum.api.commands.CommandFlag.valueOf(java.lang.String)"""
        return CommandFlag._wrap(_CommandFlag.valueOf(arg0))

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

    @overload
    def getMessageCode(self) -> 'MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.CommandFlag.getMessageCode()"""
        return 'MessageCode'._wrap(super(CommandFlag, self).getMessageCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


CommandFlag.EDIT_MODE = CommandFlag._wrap(_EDIT_MODE.EDIT_MODE)

CommandFlag.DANGEROUS = CommandFlag._wrap(_DANGEROUS.DANGEROUS) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_NotAtEndOfArg
_NotAtEndOfArg = _CommandParseException_NotAtEndOfArg.NotAtEndOfArg
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotAtEndOfArg():
    """dev.ultreon.quantum.api.commands.CommandParseException.NotAtEndOfArg"""
 
    @staticmethod
    def _wrap(java_value: _NotAtEndOfArg) -> 'NotAtEndOfArg':
        return NotAtEndOfArg(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotAtEndOfArg):
        """
        Dynamic initializer for NotAtEndOfArg.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotAtEndOfArg__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotAtEndOfArg__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$NotAtEndOfArg(int)"""
        val = _NotAtEndOfArg(_int.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry
import it.unimi.dsi.fastutil.ints.Int2ReferenceMap.Entry as Entry
import dev.ultreon.quantum.api.commands.IndexedCommandSpecValues as _IndexedCommandSpecValues_Entry
_Entry = _IndexedCommandSpecValues_Entry.Entry
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandSpecValues as _CommandSpecValues
_CommandSpecValues = _CommandSpecValues
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Entry():
    """dev.ultreon.quantum.api.commands.IndexedCommandSpecValues.Entry"""
 
    @staticmethod
    def _wrap(java_value: _Entry) -> 'Entry':
        return Entry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entry):
        """
        Dynamic initializer for Entry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entry__wrapper":
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

    @overload
    def values(self) -> 'CommandSpecValues':
        """public dev.ultreon.quantum.api.commands.CommandSpecValues dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.values()"""
        return 'CommandSpecValues'._wrap(super(Entry, self).values())

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

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.index()"""
        return int._wrap(super(Entry, self).index())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Entry'):
        """public dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry(it.unimi.dsi.fastutil.ints.Int2ReferenceMap$Entry<dev.ultreon.quantum.api.commands.CommandSpecValues>)"""
        val = _Entry(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: 'CommandSpecValues'):
        """public void dev.ultreon.quantum.api.commands.IndexedCommandSpecValues$Entry.set(dev.ultreon.quantum.api.commands.CommandSpecValues)"""
        super(_Entry, self).set(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Selections
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.world.ServerWorld as _ServerWorld
_ServerWorld = _ServerWorld
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.Selections as _Selections
_Selections = _Selections
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.entity.Entity as _Entity
_Entity = _Entity
import dev.ultreon.quantum.world.ServerChunk as _ServerChunk
_ServerChunk = _ServerChunk
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.entity.player.Player as _Player
_Player = _Player
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Selections():
    """dev.ultreon.quantum.api.commands.Selections"""
 
    @staticmethod
    def _wrap(java_value: _Selections) -> 'Selections':
        return Selections(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Selections):
        """
        Dynamic initializer for Selections.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Selections__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Selections__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def get(arg0: 'CommandSender') -> 'Selections':
        """public static dev.ultreon.quantum.api.commands.Selections dev.ultreon.quantum.api.commands.Selections.get(dev.ultreon.quantum.api.commands.CommandSender)"""
        return Selections._wrap(_Selections.get(arg0))

    @overload
    def getWorld(self) -> 'world.ServerWorld':
        """public dev.ultreon.quantum.world.ServerWorld dev.ultreon.quantum.api.commands.Selections.getWorld()"""
        return 'world.ServerWorld'._wrap(super(Selections, self).getWorld())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Selections()"""
        val = _Selections()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setEntity(self, arg0: 'Entity'):
        """public void dev.ultreon.quantum.api.commands.Selections.setEntity(dev.ultreon.quantum.entity.Entity)"""
        super(_Selections, self).setEntity(arg0)

    @overload
    def setChunk(self, arg0: 'ServerChunk'):
        """public void dev.ultreon.quantum.api.commands.Selections.setChunk(dev.ultreon.quantum.world.ServerChunk)"""
        super(_Selections, self).setChunk(arg0)

    @overload
    def getChunk(self) -> 'world.ServerChunk':
        """public dev.ultreon.quantum.world.ServerChunk dev.ultreon.quantum.api.commands.Selections.getChunk()"""
        return 'world.ServerChunk'._wrap(super(Selections, self).getChunk())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Selections()"""
        val = _Selections()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getPlayer(self) -> 'player.Player':
        """public dev.ultreon.quantum.entity.player.Player dev.ultreon.quantum.api.commands.Selections.getPlayer()"""
        return 'player.Player'._wrap(super(Selections, self).getPlayer())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setWorld(self, arg0: 'ServerWorld'):
        """public void dev.ultreon.quantum.api.commands.Selections.setWorld(dev.ultreon.quantum.world.ServerWorld)"""
        super(_Selections, self).setWorld(arg0)

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
    def getEntity(self) -> 'entity.Entity':
        """public dev.ultreon.quantum.entity.Entity dev.ultreon.quantum.api.commands.Selections.getEntity()"""
        return 'entity.Entity'._wrap(super(Selections, self).getEntity())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPlayer(self, arg0: 'Player'):
        """public void dev.ultreon.quantum.api.commands.Selections.setPlayer(dev.ultreon.quantum.entity.player.Player)"""
        super(_Selections, self).setPlayer(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.Overload
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandSpec as _CommandSpec
_CommandSpec = _CommandSpec
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.Overload as _Overload
_Overload = _Overload
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class Overload():
    """dev.ultreon.quantum.api.commands.Overload"""
 
    @staticmethod
    def _wrap(java_value: _Overload) -> 'Overload':
        return Overload(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Overload):
        """
        Dynamic initializer for Overload.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Overload__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Overload__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def matches(self, arg0: 'ArrayList') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.matches(java.util.ArrayList<dev.ultreon.quantum.api.commands.CommandParameter>)"""
        return bool._wrap(super(_Overload, self).matches(arg0))

    @overload
    def hasPermission(self, arg0: 'CommandSender') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.hasPermission(dev.ultreon.quantum.api.commands.CommandSender)"""
        return bool._wrap(super(_Overload, self).hasPermission(arg0))

    @overload
    def __init__(self, arg0: 'List', arg1: 'CommandSpec', arg2: str):
        """public dev.ultreon.quantum.api.commands.Overload(java.util.List<dev.ultreon.quantum.api.commands.CommandParameter>,dev.ultreon.quantum.api.commands.CommandSpec,java.lang.String)"""
        val = _Overload(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def args(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.api.commands.CommandParameter> dev.ultreon.quantum.api.commands.Overload.args()"""
        return 'List'._wrap(super(Overload, self).args())

    @overload
    def validFor(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String') -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.validFor(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[]) throws dev.ultreon.quantum.api.commands.CommandParseException"""
        return bool._wrap(super(_Overload, self).validFor(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.Overload.toString()"""
        return str._wrap(super(Overload, self).toString())

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
    def getObjectCache(self) -> 'List':
        """public java.util.List<java.lang.Object> dev.ultreon.quantum.api.commands.Overload.getObjectCache()"""
        return 'List'._wrap(super(Overload, self).getObjectCache())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.Overload.hashCode()"""
        return int._wrap(super(Overload, self).hashCode())

    @overload
    def spec(self) -> 'CommandSpec':
        """public dev.ultreon.quantum.api.commands.CommandSpec dev.ultreon.quantum.api.commands.Overload.spec()"""
        return 'CommandSpec'._wrap(super(Overload, self).spec())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def tabComplete(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String', arg3: 'List') -> 'List':
        """public java.util.List<java.lang.String> dev.ultreon.quantum.api.commands.Overload.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[],java.util.List<java.lang.String>)"""
        return 'List'._wrap(super(_Overload, self).tabComplete(arg0, arg1, arg2, arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.Overload.equals(java.lang.Object)"""
        return bool._wrap(super(_Overload, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.SpecSyntaxException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import dev.ultreon.quantum.api.commands.SpecSyntaxException as _SpecSyntaxException
_SpecSyntaxException = _SpecSyntaxException
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpecSyntaxException():
    """dev.ultreon.quantum.api.commands.SpecSyntaxException"""
 
    @staticmethod
    def _wrap(java_value: _SpecSyntaxException) -> 'SpecSyntaxException':
        return SpecSyntaxException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpecSyntaxException):
        """
        Dynamic initializer for SpecSyntaxException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpecSyntaxException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpecSyntaxException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int, arg1: int, arg2: str):
        """public dev.ultreon.quantum.api.commands.SpecSyntaxException(int,int,java.lang.String)"""
        val = _SpecSyntaxException(_int.valueOf(arg0), _int.valueOf(arg1), arg2)
        self.__wrapper = val

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.SpecSyntaxException.getMessage()"""
        return str._wrap(super(SpecSyntaxException, self).getMessage())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def printStackTrace(self):
        """public void dev.ultreon.quantum.api.commands.SpecSyntaxException.printStackTrace()"""
        super(SpecSyntaxException, self).printStackTrace()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandRunnable
import dev.ultreon.quantum.api.commands.CommandRunnable as _CommandRunnable
_CommandRunnable = _CommandRunnable
from builtins import object
from abc import abstractmethod, ABC
 
class CommandRunnable():
    """dev.ultreon.quantum.api.commands.CommandRunnable"""
 
    @staticmethod
    def _wrap(java_value: _CommandRunnable) -> 'CommandRunnable':
        return CommandRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandRunnable):
        """
        Dynamic initializer for CommandRunnable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandRunnable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandRunnable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def invoke(self, *arg0: object):
        """public abstract dev.ultreon.quantum.api.commands.output.CommandResult dev.ultreon.quantum.api.commands.CommandRunnable.invoke(java.lang.Object...)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandCrashReport
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.CommandCrashReport as _CommandCrashReport
_CommandCrashReport = _CommandCrashReport
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.CommandCrashReport as _CommandCrashReport_Details
_Details = _CommandCrashReport_Details.Details
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandCrashReport():
    """dev.ultreon.quantum.api.commands.CommandCrashReport"""
 
    @staticmethod
    def _wrap(java_value: _CommandCrashReport) -> 'CommandCrashReport':
        return CommandCrashReport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandCrashReport):
        """
        Dynamic initializer for CommandCrashReport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandCrashReport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandCrashReport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Throwable', arg1: str, arg2: 'String'):
        """public dev.ultreon.quantum.api.commands.CommandCrashReport(java.lang.Throwable,java.lang.String,java.lang.String[])"""
        val = _CommandCrashReport(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def save(self, arg0: 'CommandSender') -> 'Details':
        """public dev.ultreon.quantum.api.commands.CommandCrashReport$Details dev.ultreon.quantum.api.commands.CommandCrashReport.save(dev.ultreon.quantum.api.commands.CommandSender)"""
        return 'Details'._wrap(super(_CommandCrashReport, self).save(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.Role
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.Role as _Role
_Role = _Role
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Role():
    """dev.ultreon.quantum.api.commands.Role"""
 
    @staticmethod
    def _wrap(java_value: _Role) -> 'Role':
        return Role(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Role):
        """
        Dynamic initializer for Role.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Role__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Role__wrapper":
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.Role()"""
        val = _Role()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.Role()"""
        val = _Role()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParseException$Invalid
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException
_CommandParseException = _CommandParseException
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import dev.ultreon.quantum.api.commands.CommandParseException as _CommandParseException_Invalid
_Invalid = _CommandParseException_Invalid.Invalid
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Invalid():
    """dev.ultreon.quantum.api.commands.CommandParseException.Invalid"""
 
    @staticmethod
    def _wrap(java_value: _Invalid) -> 'Invalid':
        return Invalid(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Invalid):
        """
        Dynamic initializer for Invalid.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Invalid__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Invalid__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: object, arg2: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$Invalid(java.lang.String,java.lang.Object,int)"""
        val = _Invalid(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

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
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.CommandParseException$Invalid(java.lang.String,int)"""
        val = _Invalid(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.CommandParseException.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandParseException, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.CommandParameter$Text
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter_Text
_Text = _CommandParameter_Text.Text
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.CommandParameter as _CommandParameter
_CommandParameter = _CommandParameter
from typing import List
import java.util.function.Consumer as Consumer
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Text():
    """dev.ultreon.quantum.api.commands.CommandParameter.Text"""
 
    @staticmethod
    def _wrap(java_value: _Text) -> 'Text':
        return Text(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Text):
        """
        Dynamic initializer for Text.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Text__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Text__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def ifArgType(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifArgType(java.util.function.Consumer<dev.ultreon.quantum.api.commands.CommandParameter$ArgumentType>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifArgType(arg0))

    @override
    @overload
    def getComment(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.getComment()"""
        return str._wrap(super(Text, self).getComment())

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
    def ifText(self, arg0: 'Consumer') -> 'CommandParameter':
        """public default dev.ultreon.quantum.api.commands.CommandParameter dev.ultreon.quantum.api.commands.CommandParameter.ifText(java.util.function.Consumer<java.lang.String[]>)"""
        return 'CommandParameter'._wrap(super(_CommandParameter, self).ifText(arg0))

    @overload
    def __init__(self, arg0: 'String', arg1: bool):
        """public dev.ultreon.quantum.api.commands.CommandParameter$Text(java.lang.String[],boolean)"""
        val = _Text(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getText(self) -> List[str]:
        """public java.lang.String[] dev.ultreon.quantum.api.commands.CommandParameter$Text.getText()"""
        return List[str]._wrap(super(Text, self).getText())

    @override
    @overload
    def getTag(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.getTag()"""
        return str._wrap(super(Text, self).getTag())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.CommandParameter$Text.toString()"""
        return str._wrap(super(Text, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def isOptional(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.CommandParameter$Text.isOptional()"""
        return bool._wrap(super(Text, self).isOptional())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.ArgumentType
import dev.ultreon.quantum.api.commands.ArgumentType as _ArgumentType
_ArgumentType = _ArgumentType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArgumentType():
    """dev.ultreon.quantum.api.commands.ArgumentType"""
 
    @staticmethod
    def _wrap(java_value: _ArgumentType) -> 'ArgumentType':
        return ArgumentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArgumentType):
        """
        Dynamic initializer for ArgumentType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArgumentType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArgumentType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.ArgumentType.hashCode()"""
        return int._wrap(super(ArgumentType, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.ArgumentType.equals(java.lang.Object)"""
        return bool._wrap(super(_ArgumentType, self).equals(arg0))

    @overload
    def getArgTypeClasses(self) -> List['type.Class']:
        """public java.lang.Class<?>[] dev.ultreon.quantum.api.commands.ArgumentType.getArgTypeClasses()"""
        return List['type.Class']._wrap(super(ArgumentType, self).getArgTypeClasses())

    @abstractmethod
    def getArgClass(self, ):
        """public abstract java.lang.Class<? extends dev.ultreon.quantum.api.commands.Argument<?>> dev.ultreon.quantum.api.commands.ArgumentType.getArgClass()"""
        pass

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.ArgumentType()"""
        val = _ArgumentType()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.ArgumentType()"""
        val = _ArgumentType()
        self.__wrapper = val

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
    def getArgsNeeded(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: 'String') -> int:
        """public int dev.ultreon.quantum.api.commands.ArgumentType.getArgsNeeded(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String[])"""
        return int._wrap(super(_ArgumentType, self).getArgsNeeded(arg0, arg1, arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.ArgumentType.toString()"""
        return str._wrap(super(ArgumentType, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def parse(self, arg0: 'CommandSender', arg1: 'CommandContext', arg2: str, arg3: 'String'):
        """public abstract dev.ultreon.quantum.api.commands.ArgumentType$Result<? extends dev.ultreon.quantum.api.commands.Argument<? extends T>> dev.ultreon.quantum.api.commands.ArgumentType.parse(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String,java.lang.String[])"""
        pass