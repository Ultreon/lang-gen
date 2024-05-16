from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
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
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Result"""
 
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
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hashCode()"""
        return int._wrap(super(Result, self).hashCode())

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.value()"""
        return object._wrap(super(Result, self).value())

    @overload
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.error()"""
        return 'error.CommandError'._wrap(super(Result, self).error())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.equals(java.lang.Object)"""
        return bool._wrap(super(_Result, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = _Result(arg0, arg1)
        self.__wrapper = val

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hasError()"""
        return bool._wrap(super(Result, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.toString()"""
        return str._wrap(super(Result, self).toString())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Result
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
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
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Result"""
 
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
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hashCode()"""
        return int._wrap(super(Result, self).hashCode())

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.value()"""
        return object._wrap(super(Result, self).value())

    @overload
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.error()"""
        return 'error.CommandError'._wrap(super(Result, self).error())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.equals(java.lang.Object)"""
        return bool._wrap(super(_Result, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def __init__(self, arg0: object, arg1: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result(T,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = _Result(arg0, arg1)
        self.__wrapper = val

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.hasError()"""
        return bool._wrap(super(Result, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Result.toString()"""
        return str._wrap(super(Result, self).toString())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Result 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.EntityBaseSelector
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.selector.EntityBaseSelector as _EntityBaseSelector
_EntityBaseSelector = _EntityBaseSelector
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as _SelectorFactory
_SelectorFactory = _SelectorFactory
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntityBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.EntityBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _EntityBaseSelector) -> 'EntityBaseSelector':
        return EntityBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityBaseSelector):
        """
        Dynamic initializer for EntityBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Class', arg2: str):
        """public dev.ultreon.quantum.api.commands.selector.EntityBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Class<T>,java.lang.String)"""
        val = _EntityBaseSelector(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<T> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.calculateData()"""
        return 'Result'._wrap(super(EntityBaseSelector, self).calculateData())

    @staticmethod
    @overload
    def tabComplete(arg0: 'Class', arg1: bool, arg2: 'CommandSender', arg3: 'CommandContext', arg4: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.tabComplete(java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>,boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_EntityBaseSelector.tabComplete(arg0, _boolean.valueOf(arg1), arg2, arg3, arg4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'SelectorFactory':
        """public static <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<T>> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.create(java.lang.Class<T>)"""
        return SelectorFactory._wrap(_EntityBaseSelector.create(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Class', arg2: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.EntityBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Class<T>,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _EntityBaseSelector(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @staticmethod
    @overload
    def tabComplete(arg0: 'Class', arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.EntityBaseSelector.tabComplete(java.lang.Class<? extends dev.ultreon.quantum.entity.Entity>,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_EntityBaseSelector.tabComplete(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseSelector():
    """dev.ultreon.quantum.api.commands.selector.BaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _BaseSelector) -> 'BaseSelector':
        return BaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseSelector):
        """
        Dynamic initializer for BaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector(java.lang.String)"""
        val = _BaseSelector(arg0)
        self.__wrapper = val

    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

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
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @overload
    def __init__(self, arg0: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector(dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _BaseSelector(arg0)
        self.__wrapper = val

    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector as _PlayerBaseSelector
_PlayerBaseSelector = _PlayerBaseSelector
import java.lang.Boolean as _boolean
import java.util.ArrayList as ArrayList
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _PlayerBaseSelector) -> 'PlayerBaseSelector':
        return PlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerBaseSelector):
        """
        Dynamic initializer for PlayerBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.calculateData()"""
        return 'Result'._wrap(super(PlayerBaseSelector, self).calculateData())

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _PlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _PlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_PlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_PlayerBaseSelector.tabComplete(_boolean.valueOf(arg0), arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector as _CommandSenderBaseSelector
_CommandSenderBaseSelector = _CommandSenderBaseSelector
import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandSenderBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _CommandSenderBaseSelector) -> 'CommandSenderBaseSelector':
        return CommandSenderBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandSenderBaseSelector):
        """
        Dynamic initializer for CommandSenderBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandSenderBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandSenderBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _CommandSenderBaseSelector(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _CommandSenderBaseSelector(arg0, arg1)
        self.__wrapper = val

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.api.commands.CommandSender> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.calculateData()"""
        return 'Result'._wrap(super(CommandSenderBaseSelector, self).calculateData())

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_CommandSenderBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.CommandSenderBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_CommandSenderBaseSelector.tabComplete(_boolean.valueOf(arg0), arg1, arg2, arg3))

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.Selector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.selector.Selector as _Selector
_Selector = _Selector
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Selector():
    """dev.ultreon.quantum.api.commands.selector.Selector"""
 
    @staticmethod
    def _wrap(java_value: _Selector) -> 'Selector':
        return Selector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Selector):
        """
        Dynamic initializer for Selector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Selector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Selector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.selector.Selector(java.lang.String)"""
        val = _Selector(arg0)
        self.__wrapper = val

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<java.lang.String> dev.ultreon.quantum.api.commands.selector.Selector.calculateData()"""
        return 'Result'._wrap(super(Selector, self).calculateData())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorFactories
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.selector.SelectorFactories as _SelectorFactories
_SelectorFactories = _SelectorFactories
import dev.ultreon.quantum.api.commands.selector.SelectorFactory as _SelectorFactory
_SelectorFactory = _SelectorFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SelectorFactories():
    """dev.ultreon.quantum.api.commands.selector.SelectorFactories"""
 
    @staticmethod
    def _wrap(java_value: _SelectorFactories) -> 'SelectorFactories':
        return SelectorFactories(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectorFactories):
        """
        Dynamic initializer for SelectorFactories.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectorFactories__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectorFactories__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.WorldBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.WORLD
    WORLD: 'SelectorFactory' = _wrap(_SelectorFactory.WORLD)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.PlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.PLAYER
    PLAYER: 'SelectorFactory' = _wrap(_SelectorFactory.PLAYER)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.ItemBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ITEM
    ITEM: 'SelectorFactory' = _wrap(_SelectorFactory.ITEM)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.OFFLINE_PLAYER
    OFFLINE_PLAYER: 'SelectorFactory' = _wrap(_SelectorFactory.OFFLINE_PLAYER)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<dev.ultreon.quantum.entity.Entity>> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ENTITY
    ENTITY: 'SelectorFactory' = _wrap(_SelectorFactory.ENTITY)

    # public static final dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector> dev.ultreon.quantum.api.commands.selector.SelectorFactories.ANY_PLAYER
    ANY_PLAYER: 'SelectorFactory' = _wrap(_SelectorFactory.ANY_PLAYER)


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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactories()"""
        val = _SelectorFactories()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.selector.SelectorFactories()"""
        val = _SelectorFactories()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def entity(arg0: 'Class') -> 'SelectorFactory':
        """public static <T extends dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.api.commands.selector.SelectorFactory<dev.ultreon.quantum.api.commands.selector.EntityBaseSelector<T>> dev.ultreon.quantum.api.commands.selector.SelectorFactories.entity(java.lang.Class<T>)"""
        return SelectorFactory._wrap(_SelectorFactories.entity(arg0))

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Parsed():
    """dev.ultreon.quantum.api.commands.selector.BaseSelector.Parsed"""
 
    @staticmethod
    def _wrap(java_value: _Parsed) -> 'Parsed':
        return Parsed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parsed):
        """
        Dynamic initializer for Parsed.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parsed__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parsed__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.toString()"""
        return str._wrap(super(Parsed, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.equals(java.lang.Object)"""
        return bool._wrap(super(_Parsed, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.hashCode()"""
        return int._wrap(super(Parsed, self).hashCode())

    @overload
    def key(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.key()"""
        return 'SelectorKey'._wrap(super(Parsed, self).key())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.hasError()"""
        return bool._wrap(super(Parsed, self).hasError())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def value(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.value()"""
        return str._wrap(super(Parsed, self).value())

    @overload
    def error(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed.error()"""
        return 'error.CommandError'._wrap(super(Parsed, self).error())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'SelectorKey', arg1: str, arg2: 'CommandError'):
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed(dev.ultreon.quantum.api.commands.selector.SelectorKey,java.lang.String,dev.ultreon.quantum.api.commands.error.CommandError)"""
        val = _Parsed(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorFactory
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.SelectorFactory as _SelectorFactory
_SelectorFactory = _SelectorFactory
from abc import abstractmethod, ABC
 
class SelectorFactory():
    """dev.ultreon.quantum.api.commands.selector.SelectorFactory"""
 
    @staticmethod
    def _wrap(java_value: _SelectorFactory) -> 'SelectorFactory':
        return SelectorFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectorFactory):
        """
        Dynamic initializer for SelectorFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectorFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectorFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createSelector(self, arg0: 'CommandSender', arg1: str):
        """public abstract T dev.ultreon.quantum.api.commands.selector.SelectorFactory.createSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector as _OfflinePlayerBaseSelector
_OfflinePlayerBaseSelector = _OfflinePlayerBaseSelector
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OfflinePlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _OfflinePlayerBaseSelector) -> 'OfflinePlayerBaseSelector':
        return OfflinePlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OfflinePlayerBaseSelector):
        """
        Dynamic initializer for OfflinePlayerBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OfflinePlayerBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OfflinePlayerBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _OfflinePlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.server.player.CachedPlayer> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.calculateData()"""
        return 'Result'._wrap(super(OfflinePlayerBaseSelector, self).calculateData())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_OfflinePlayerBaseSelector.tabComplete(_boolean.valueOf(arg0), arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _OfflinePlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.OfflinePlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_OfflinePlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.WorldBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import dev.ultreon.quantum.api.commands.selector.WorldBaseSelector as _WorldBaseSelector
_WorldBaseSelector = _WorldBaseSelector
import java.util.ArrayList as ArrayList
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.WorldBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _WorldBaseSelector) -> 'WorldBaseSelector':
        return WorldBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldBaseSelector):
        """
        Dynamic initializer for WorldBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'Command', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.WorldBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.Command,java.lang.String)"""
        return ArrayList._wrap(_WorldBaseSelector.tabComplete(arg0, arg1, arg2))

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.world.World> dev.ultreon.quantum.api.commands.selector.WorldBaseSelector.calculateData()"""
        return 'Result'._wrap(super(WorldBaseSelector, self).calculateData())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.WorldBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _WorldBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.WorldBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _WorldBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Result
_Result = _BaseSelector_Result.Result
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector as _AnyPlayerBaseSelector
_AnyPlayerBaseSelector = _AnyPlayerBaseSelector
import java.util.ArrayList as ArrayList
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AnyPlayerBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _AnyPlayerBaseSelector) -> 'AnyPlayerBaseSelector':
        return AnyPlayerBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AnyPlayerBaseSelector):
        """
        Dynamic initializer for AnyPlayerBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AnyPlayerBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AnyPlayerBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def calculateData(self) -> 'Result':
        """public dev.ultreon.quantum.api.commands.selector.BaseSelector$Result<dev.ultreon.quantum.server.player.CacheablePlayer> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.calculateData()"""
        return 'Result'._wrap(super(AnyPlayerBaseSelector, self).calculateData())

    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _AnyPlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def tabComplete(arg0: bool, arg1: 'CommandSender', arg2: 'CommandContext', arg3: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.tabComplete(boolean,dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_AnyPlayerBaseSelector.tabComplete(_boolean.valueOf(arg0), arg1, arg2, arg3))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_AnyPlayerBaseSelector.tabComplete(arg0, arg1, arg2))

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.AnyPlayerBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _AnyPlayerBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

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
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.SelectorKey
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
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
 
class SelectorKey():
    """dev.ultreon.quantum.api.commands.selector.SelectorKey"""
 
    @staticmethod
    def _wrap(java_value: _SelectorKey) -> 'SelectorKey':
        return SelectorKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectorKey):
        """
        Dynamic initializer for SelectorKey.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectorKey__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectorKey__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SelectorKey':
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.valueOf(java.lang.String)"""
        return SelectorKey._wrap(_SelectorKey.valueOf(arg0))

    @overload
    def symbol(self) -> str:
        """public char dev.ultreon.quantum.api.commands.selector.SelectorKey.symbol()"""
        return str._wrap(super(SelectorKey, self).symbol())

    @staticmethod
    @overload
    def fromKey(arg0: str) -> 'SelectorKey':
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.SelectorKey.fromKey(char)"""
        return SelectorKey._wrap(_SelectorKey.fromKey(_char.valueOf(arg0)))

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
    def values() -> List['SelectorKey']:
        """public static dev.ultreon.quantum.api.commands.selector.SelectorKey[] dev.ultreon.quantum.api.commands.selector.SelectorKey.values()"""
        return List[SelectorKey]._wrap(_SelectorKey.values())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.SelectorKey.toString()"""
        return str._wrap(super(SelectorKey, self).toString())


SelectorKey.VARIABLE = SelectorKey._wrap(_VARIABLE.VARIABLE)

SelectorKey.DISPLAY_NAME = SelectorKey._wrap(_DISPLAY_NAME.DISPLAY_NAME)

SelectorKey.TAG = SelectorKey._wrap(_TAG.TAG)

SelectorKey.NAME = SelectorKey._wrap(_NAME.NAME)

SelectorKey.DATA = SelectorKey._wrap(_DATA.DATA)

SelectorKey.ID = SelectorKey._wrap(_ID.ID)

SelectorKey.TYPE = SelectorKey._wrap(_TYPE.TYPE)

SelectorKey.UUID = SelectorKey._wrap(_UUID.UUID)

SelectorKey.CUSTOM_NAME = SelectorKey._wrap(_CUSTOM_NAME.CUSTOM_NAME) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.selector.ItemBaseSelector
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.api.commands.selector.ItemBaseSelector as _ItemBaseSelector
_ItemBaseSelector = _ItemBaseSelector
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector_Parsed
_Parsed = _BaseSelector_Parsed.Parsed
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.api.commands.selector.SelectorKey as _SelectorKey
_SelectorKey = _SelectorKey
import java.util.ArrayList as _ArrayList
_ArrayList = _ArrayList
import java.lang.String as _string
import java.util.ArrayList as ArrayList
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
try:
    from pyquantum.api.commands import error
except ImportError:
    error = _import_once("pyquantum.api.commands.error")

import dev.ultreon.quantum.api.commands.selector.BaseSelector as _BaseSelector
_BaseSelector = _BaseSelector
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemBaseSelector():
    """dev.ultreon.quantum.api.commands.selector.ItemBaseSelector"""
 
    @staticmethod
    def _wrap(java_value: _ItemBaseSelector) -> 'ItemBaseSelector':
        return ItemBaseSelector(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemBaseSelector):
        """
        Dynamic initializer for ItemBaseSelector.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemBaseSelector__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemBaseSelector__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def parseSelector(arg0: str, arg1: 'Parsed') -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0, arg1))

    @staticmethod
    @overload
    def tabComplete(arg0: 'CommandSender', arg1: 'CommandContext', arg2: str) -> 'ArrayList':
        """public static java.util.ArrayList<java.lang.String> dev.ultreon.quantum.api.commands.selector.ItemBaseSelector.tabComplete(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandContext,java.lang.String)"""
        return ArrayList._wrap(_ItemBaseSelector.tabComplete(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getStringValue(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.getStringValue()"""
        return str._wrap(super(BaseSelector, self).getStringValue())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getError(self) -> 'error.CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.selector.BaseSelector.getError()"""
        return 'error.CommandError'._wrap(super(BaseSelector, self).getError())

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: str):
        """public dev.ultreon.quantum.api.commands.selector.ItemBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        val = _ItemBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.api.commands.selector.BaseSelector.getValue()"""
        return object._wrap(super(BaseSelector, self).getValue())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.selector.BaseSelector.toString()"""
        return str._wrap(super(BaseSelector, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'CommandSender', arg1: 'Parsed'):
        """public dev.ultreon.quantum.api.commands.selector.ItemBaseSelector(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed)"""
        val = _ItemBaseSelector(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def hasError(self) -> bool:
        """public boolean dev.ultreon.quantum.api.commands.selector.BaseSelector.hasError()"""
        return bool._wrap(super(BaseSelector, self).hasError())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getKey(self) -> 'SelectorKey':
        """public dev.ultreon.quantum.api.commands.selector.SelectorKey dev.ultreon.quantum.api.commands.selector.BaseSelector.getKey()"""
        return 'SelectorKey'._wrap(super(BaseSelector, self).getKey())

    @staticmethod
    @overload
    def parseSelector(arg0: str) -> 'Parsed':
        """public static dev.ultreon.quantum.api.commands.selector.BaseSelector$Parsed dev.ultreon.quantum.api.commands.selector.BaseSelector.parseSelector(java.lang.String) throws java.lang.IllegalArgumentException"""
        return Parsed._wrap(_BaseSelector.parseSelector(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())