from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Result():
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Result"""
 
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.equals(java.lang.Object)"""
        return bool.__wrap(super(__Result, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = __Result(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hasError()"""
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.toString()"""
        return str.__wrap(super(Result, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.value()"""
        return object.__wrap(super(Result, self).value())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hashCode()"""
        return int.__wrap(super(Result, self).hashCode())

    @overload
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.error()"""
        return 'error.CommandError'.__wrap(super(Result, self).error())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Result
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Result():
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Result"""
 
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.equals(java.lang.Object)"""
        return bool.__wrap(super(__Result, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = __Result(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hasError()"""
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.toString()"""
        return str.__wrap(super(Result, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.value()"""
        return object.__wrap(super(Result, self).value())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hashCode()"""
        return int.__wrap(super(Result, self).hashCode())

    @overload
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.error()"""
        return 'error.CommandError'.__wrap(super(Result, self).error())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Result 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.EntityBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
import java.lang.Boolean as __boolean
from builtins import type
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

from builtins import bool
from builtins import str
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as __SelectorFactory
__SelectorFactory = __SelectorFactory
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.EntityBaseSelector as __EntityBaseSelector
__EntityBaseSelector = __EntityBaseSelector
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
import java.lang.Integer as __int
from builtins import int
 
class EntityBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.EntityBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __EntityBaseSelector) -> 'EntityBaseSelector':
        return EntityBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityBaseSelector):
        """
        Dynamic initializer for EntityBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @staticmethod
    @overload
    def tabComplete(arg0: 'Class', arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.tabComplete(java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__EntityBaseSelector.tabComplete(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def tabComplete(arg0: 'Class', arg1: bool, arg2: 'CommandSender', arg3: 'CommandContext', arg4: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.tabComplete(java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>,boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__EntityBaseSelector.tabComplete(arg0, __boolean.valueOf(arg1), arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Class', arg2: str):
        """public dev.ultreon.quantum.api.commands.selector.EntityBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Class<T>,java.lang.String)"""
        val = __EntityBaseSelector(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<T> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(EntityBaseSelector, self).calculateData())

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
    def __init__(self, arg0: 'CommandSender', arg1: 'Class', arg2: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.EntityBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Class<T>,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __EntityBaseSelector(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'SelectorFactory':
        """public static <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<T>> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.create(java.lang.Class<T>)"""
        return SelectorFactory.__wrap(__EntityBaseSelector.create(arg0))

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class BaseSelector(ABC):
    """dev.ultreon.quantum.api.commands.selector.BaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __BaseSelector) -> 'BaseSelector':
        return BaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BaseSelector):
        """
        Dynamic initializer for BaseSelector.
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
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector(java.lang.String)"""
        val = __BaseSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector(dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __BaseSelector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

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

    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector as __PlayerBaseSelector
__PlayerBaseSelector = __PlayerBaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __PlayerBaseSelector) -> 'PlayerBaseSelector':
        return PlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerBaseSelector):
        """
        Dynamic initializer for PlayerBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__PlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(PlayerBaseSelector, self).calculateData())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __PlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__PlayerBaseSelector.tabComplete(__boolean.valueOf(arg0), arg1, arg2, arg3))

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __PlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector as __CommandSenderBaseSelector
__CommandSenderBaseSelector = __CommandSenderBaseSelector
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommandSenderBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __CommandSenderBaseSelector) -> 'CommandSenderBaseSelector':
        return CommandSenderBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandSenderBaseSelector):
        """
        Dynamic initializer for CommandSenderBaseSelector.
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
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.api.commands.CommandSender> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(CommandSenderBaseSelector, self).calculateData())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__CommandSenderBaseSelector.tabComplete(__boolean.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __CommandSenderBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__CommandSenderBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __CommandSenderBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.Selector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.selector.Selector as __Selector
__Selector = __Selector
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Selector():
    """dev.ultreon.quantum.api.commands.selector.Selector"""
 
    @staticmethod
    def __wrap(java_value: __Selector) -> 'Selector':
        return Selector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Selector):
        """
        Dynamic initializer for Selector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.selector.Selector(java.lang.String)"""
        val = __Selector(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<java.lang.String> dev.ultreon.quantum.api.commands.selector.Selector.calculateData()"""
        return 'Result'.__wrap(super(Selector, self).calculateData())

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
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorFactories
from builtins import str
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as __SelectorFactory
__SelectorFactory = __SelectorFactory
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.SelectorFactories as __SelectorFactories
__SelectorFactories = __SelectorFactories
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
 
class SelectorFactories():
    """dev.ultreon.quantum.api.commands.selector.SelectorFactories"""
 
    @staticmethod
    def __wrap(java_value: __SelectorFactories) -> 'SelectorFactories':
        return SelectorFactories(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectorFactories):
        """
        Dynamic initializer for SelectorFactories.
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
 
    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.ItemBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ITEM
    ITEM: 'SelectorFactory' = __wrap(__SelectorFactory.ITEM)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.OFFLINE_PLAYER
    OFFLINE_PLAYER: 'SelectorFactory' = __wrap(__SelectorFactory.OFFLINE_PLAYER)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<dev.ultreon.quantum.entity.Entity>> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ENTITY
    ENTITY: 'SelectorFactory' = __wrap(__SelectorFactory.ENTITY)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.PLAYER
    PLAYER: 'SelectorFactory' = __wrap(__SelectorFactory.PLAYER)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ANY_PLAYER
    ANY_PLAYER: 'SelectorFactory' = __wrap(__SelectorFactory.ANY_PLAYER)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.WorldBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.WORLD
    WORLD: 'SelectorFactory' = __wrap(__SelectorFactory.WORLD)


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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactories()"""
        val = __SelectorFactories()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def entity(arg0: 'Class') -> 'SelectorFactory':
        """public static <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<T>> dev.ultreon.quantum.api.commands.selector.SelectorFactories.entity(java.lang.Class<T>)"""
        return SelectorFactory.__wrap(__SelectorFactories.entity(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactories()"""
        val = __SelectorFactories()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Parsed():
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Parsed"""
 
    @staticmethod
    def __wrap(java_value: __Parsed) -> 'Parsed':
        return Parsed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Parsed):
        """
        Dynamic initializer for Parsed.
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
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.error()"""
        return 'error.CommandError'.__wrap(super(Parsed, self).error())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.equals(java.lang.Object)"""
        return bool.__wrap(super(__Parsed, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.toString()"""
        return str.__wrap(super(Parsed, self).toString())

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.hasError()"""
        return bool.__wrap(super(Parsed, self).hasError())

    @overload
    def value(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.value()"""
        return str.__wrap(super(Parsed, self).value())

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
    def __init__(self, arg0: 'SelectorKey', arg1: str, arg2: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = __Parsed(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.hashCode()"""
        return int.__wrap(super(Parsed, self).hashCode())

    @overload
    def key(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.key()"""
        return 'SelectorKey'.__wrap(super(Parsed, self).key())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorFactory
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as __SelectorFactory
__SelectorFactory = __SelectorFactory
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

from abc import abstractmethod, ABC
 
class SelectorFactory(ABC):
    """dev.ultreon.quantum.api.commands.selector.SelectorFactory"""
 
    @staticmethod
    def __wrap(java_value: __SelectorFactory) -> 'SelectorFactory':
        return SelectorFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectorFactory):
        """
        Dynamic initializer for SelectorFactory.
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
    def createSelector(self, arg0: 'CommandSender', arg1: str):
        """public abstract T dev.ultreon.quantum.api.commands.selector.SelectorFactory.createSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector as __OfflinePlayerBaseSelector
__OfflinePlayerBaseSelector = __OfflinePlayerBaseSelector
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OfflinePlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __OfflinePlayerBaseSelector) -> 'OfflinePlayerBaseSelector':
        return OfflinePlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OfflinePlayerBaseSelector):
        """
        Dynamic initializer for OfflinePlayerBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __OfflinePlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__OfflinePlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__OfflinePlayerBaseSelector.tabComplete(__boolean.valueOf(arg0), arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(OfflinePlayerBaseSelector, self).calculateData())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __OfflinePlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.WorldBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.WorldBaseSelector as __WorldBaseSelector
__WorldBaseSelector = __WorldBaseSelector
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.WorldBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __WorldBaseSelector) -> 'WorldBaseSelector':
        return WorldBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldBaseSelector):
        """
        Dynamic initializer for WorldBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.WorldBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __WorldBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.WorldBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __WorldBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.world.World> dev.ultreon.quantum.api.commands.selector.WorldBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(WorldBaseSelector, self).calculateData())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'Command', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.WorldBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.Command,java.lang.String)"""
        return ArrayList.__wrap(__WorldBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
from builtins import object
import dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector as __AnyPlayerBaseSelector
__AnyPlayerBaseSelector = __AnyPlayerBaseSelector
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Result
__Result = __BaseSelector_Result.Result
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AnyPlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __AnyPlayerBaseSelector) -> 'AnyPlayerBaseSelector':
        return AnyPlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AnyPlayerBaseSelector):
        """
        Dynamic initializer for AnyPlayerBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __AnyPlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__AnyPlayerBaseSelector.tabComplete(__boolean.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__AnyPlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.server.player.CacheablePlayer> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.calculateData()"""
        return 'Result'.__wrap(super(AnyPlayerBaseSelector, self).calculateData())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __AnyPlayerBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorKey
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class SelectorKey():
    """dev.ultreon.quantum.api.commands.selector.SelectorKey"""
 
    @staticmethod
    def __wrap(java_value: __SelectorKey) -> 'SelectorKey':
        return SelectorKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectorKey):
        """
        Dynamic initializer for SelectorKey.
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
 
    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.UUID
    UUID: 'SelectorKey' = __wrap(__SelectorKey.UUID)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.NAME
    NAME: 'SelectorKey' = __wrap(__SelectorKey.NAME)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.TAG
    TAG: 'SelectorKey' = __wrap(__SelectorKey.TAG)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.DATA
    DATA: 'SelectorKey' = __wrap(__SelectorKey.DATA)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.VARIABLE
    VARIABLE: 'SelectorKey' = __wrap(__SelectorKey.VARIABLE)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.TYPE
    TYPE: 'SelectorKey' = __wrap(__SelectorKey.TYPE)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.ID
    ID: 'SelectorKey' = __wrap(__SelectorKey.ID)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.CUSTOM_NAME
    CUSTOM_NAME: 'SelectorKey' = __wrap(__SelectorKey.CUSTOM_NAME)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.DISPLAY_NAME
    DISPLAY_NAME: 'SelectorKey' = __wrap(__SelectorKey.DISPLAY_NAME)


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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.SelectorKey.toString()"""
        return str.__wrap(super(SelectorKey, self).toString())

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
    def valueOf(arg0: str) -> 'SelectorKey':
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.valueOf(java.lang.String)"""
        return SelectorKey.__wrap(__SelectorKey.valueOf(arg0))

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
    def values() -> List['SelectorKey']:
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey[] dev.ultreon.quantum.api.commands.selector.SelectorKey.values()"""
        return List[SelectorKey].__wrap(__SelectorKey.values())

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
    def symbol(self) -> str:
        """public char dev.ultreon.quantum.api.commands.selector.SelectorKey.symbol()"""
        return str.__wrap(super(SelectorKey, self).symbol())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def fromKey(arg0: str) -> 'SelectorKey':
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.fromKey(char)"""
        return SelectorKey.__wrap(__SelectorKey.fromKey(__char.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.ItemBaseSelector
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorKey as __SelectorKey
__SelectorKey = __SelectorKey
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector_Parsed
__Parsed = __BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.ItemBaseSelector as __ItemBaseSelector
__ItemBaseSelector = __ItemBaseSelector
from builtins import object
import dev.ultreon.quantum.api.commands.selector.BaseSelector as __BaseSelector
__BaseSelector = __BaseSelector
import java.lang.Long as __long
import java.util.ArrayList as ArrayList
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.ArrayList as __ArrayList
__ArrayList = __ArrayList
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.api.commands import error
except ImportError:
    error = __import_once__("pyquantum.api.commands.error")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ItemBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.ItemBaseSelector"""
 
    @staticmethod
    def __wrap(java_value: __ItemBaseSelector) -> 'ItemBaseSelector':
        return ItemBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemBaseSelector):
        """
        Dynamic initializer for ItemBaseSelector.
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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool.__wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str.__wrap(super(BaseSelector, self).toString())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.ItemBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList.__wrap(__ItemBaseSelector.tabComplete(arg0, arg1, arg2))

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed.__wrap(__BaseSelector.parseSelector(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str.__wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'.__wrap(super(BaseSelector, self).getError())

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
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.ItemBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = __ItemBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.ItemBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = __ItemBaseSelector(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object.__wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'.__wrap(super(BaseSelector, self).getKey())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))