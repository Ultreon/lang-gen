from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.PermissionsBrokenError as _PermissionsBrokenError
_PermissionsBrokenError = _PermissionsBrokenError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PermissionsBrokenError():
    """dev.ultreon.quantum.api.commands.error.PermissionsBrokenError"""
 
    @staticmethod
    def _wrap(java_value: _PermissionsBrokenError) -> 'PermissionsBrokenError':
        return PermissionsBrokenError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PermissionsBrokenError):
        """
        Dynamic initializer for PermissionsBrokenError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PermissionsBrokenError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PermissionsBrokenError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.getName()"""
        return str._wrap(super(PermissionsBrokenError, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.setName(java.lang.String)"""
        super(_PermissionsBrokenError, self).setName(arg0)

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = _PermissionsBrokenError()
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = _PermissionsBrokenError()
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

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PermissionsBrokenError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.PermissionsBrokenError as _PermissionsBrokenError
_PermissionsBrokenError = _PermissionsBrokenError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PermissionsBrokenError():
    """dev.ultreon.quantum.api.commands.error.PermissionsBrokenError"""
 
    @staticmethod
    def _wrap(java_value: _PermissionsBrokenError) -> 'PermissionsBrokenError':
        return PermissionsBrokenError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PermissionsBrokenError):
        """
        Dynamic initializer for PermissionsBrokenError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PermissionsBrokenError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PermissionsBrokenError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.getName()"""
        return str._wrap(super(PermissionsBrokenError, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.setName(java.lang.String)"""
        super(_PermissionsBrokenError, self).setName(arg0)

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = _PermissionsBrokenError()
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = _PermissionsBrokenError()
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

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PermissionsBrokenError 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NoPermissionError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.NoPermissionError as _NoPermissionError
_NoPermissionError = _NoPermissionError
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoPermissionError():
    """dev.ultreon.quantum.api.commands.error.NoPermissionError"""
 
    @staticmethod
    def _wrap(java_value: _NoPermissionError) -> 'NoPermissionError':
        return NoPermissionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoPermissionError):
        """
        Dynamic initializer for NoPermissionError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoPermissionError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoPermissionError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NoPermissionError()"""
        val = _NoPermissionError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NoPermissionError.getName()"""
        return str._wrap(super(NoPermissionError, self).getName())

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
        """public dev.ultreon.quantum.api.commands.error.NoPermissionError()"""
        val = _NoPermissionError()
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError as _InvalidCoordinateXError
_InvalidCoordinateXError = _InvalidCoordinateXError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCoordinateXError():
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCoordinateXError) -> 'InvalidCoordinateXError':
        return InvalidCoordinateXError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCoordinateXError):
        """
        Dynamic initializer for InvalidCoordinateXError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCoordinateXError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCoordinateXError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError()"""
        val = _InvalidCoordinateXError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(int)"""
        val = _InvalidCoordinateXError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError()"""
        val = _InvalidCoordinateXError()
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
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(java.lang.String,int)"""
        val = _InvalidCoordinateXError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(java.lang.String)"""
        val = _InvalidCoordinateXError(arg0)
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError.getName()"""
        return str._wrap(super(InvalidCoordinateXError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidShortError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.InvalidShortError as _InvalidShortError
_InvalidShortError = _InvalidShortError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidShortError():
    """dev.ultreon.quantum.api.commands.error.InvalidShortError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidShortError) -> 'InvalidShortError':
        return InvalidShortError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidShortError):
        """
        Dynamic initializer for InvalidShortError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidShortError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidShortError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(int)"""
        val = _InvalidShortError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidShortError.getName()"""
        return str._wrap(super(InvalidShortError, self).getName())

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError()"""
        val = _InvalidShortError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(java.lang.String)"""
        val = _InvalidShortError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError()"""
        val = _InvalidShortError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(java.lang.String,int)"""
        val = _InvalidShortError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NoSelectedError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.NoSelectedError as _NoSelectedError
_NoSelectedError = _NoSelectedError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NoSelectedError():
    """dev.ultreon.quantum.api.commands.error.NoSelectedError"""
 
    @staticmethod
    def _wrap(java_value: _NoSelectedError) -> 'NoSelectedError':
        return NoSelectedError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NoSelectedError):
        """
        Dynamic initializer for NoSelectedError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NoSelectedError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NoSelectedError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NoSelectedError(java.lang.String)"""
        val = _NoSelectedError(arg0)
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NoSelectedError.getName()"""
        return str._wrap(super(NoSelectedError, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NoSelectedError(java.lang.String,int)"""
        val = _NoSelectedError(arg0, _int.valueOf(arg1))
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.OverloadError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.OverloadError as _OverloadError
_OverloadError = _OverloadError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OverloadError():
    """dev.ultreon.quantum.api.commands.error.OverloadError"""
 
    @staticmethod
    def _wrap(java_value: _OverloadError) -> 'OverloadError':
        return OverloadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OverloadError):
        """
        Dynamic initializer for OverloadError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OverloadError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OverloadError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.OverloadError.getName()"""
        return str._wrap(super(OverloadError, self).getName())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.OverloadError()"""
        val = _OverloadError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.OverloadError(int)"""
        val = _OverloadError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.OverloadError()"""
        val = _OverloadError()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidTargetError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.error.InvalidTargetError as _InvalidTargetError
_InvalidTargetError = _InvalidTargetError
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidTargetError():
    """dev.ultreon.quantum.api.commands.error.InvalidTargetError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidTargetError) -> 'InvalidTargetError':
        return InvalidTargetError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidTargetError):
        """
        Dynamic initializer for InvalidTargetError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidTargetError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidTargetError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError()"""
        val = _InvalidTargetError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(int)"""
        val = _InvalidTargetError(_int.valueOf(arg0))
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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError()"""
        val = _InvalidTargetError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(java.lang.String,int)"""
        val = _InvalidTargetError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidTargetError.getName()"""
        return str._wrap(super(InvalidTargetError, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(java.lang.String)"""
        val = _InvalidTargetError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidByteError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.error.InvalidByteError as _InvalidByteError
_InvalidByteError = _InvalidByteError
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidByteError():
    """dev.ultreon.quantum.api.commands.error.InvalidByteError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidByteError) -> 'InvalidByteError':
        return InvalidByteError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidByteError):
        """
        Dynamic initializer for InvalidByteError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidByteError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidByteError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError()"""
        val = _InvalidByteError()
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
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(java.lang.String,int)"""
        val = _InvalidByteError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidByteError.getName()"""
        return str._wrap(super(InvalidByteError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError()"""
        val = _InvalidByteError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(java.lang.String)"""
        val = _InvalidByteError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(int)"""
        val = _InvalidByteError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidFloatError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidFloatError as _InvalidFloatError
_InvalidFloatError = _InvalidFloatError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidFloatError():
    """dev.ultreon.quantum.api.commands.error.InvalidFloatError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidFloatError) -> 'InvalidFloatError':
        return InvalidFloatError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidFloatError):
        """
        Dynamic initializer for InvalidFloatError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidFloatError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidFloatError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError()"""
        val = _InvalidFloatError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(java.lang.String)"""
        val = _InvalidFloatError(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(int)"""
        val = _InvalidFloatError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(java.lang.String,int)"""
        val = _InvalidFloatError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError()"""
        val = _InvalidFloatError()
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidFloatError.getName()"""
        return str._wrap(super(InvalidFloatError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidError as _InvalidError
_InvalidError = _InvalidError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidError():
    """dev.ultreon.quantum.api.commands.error.InvalidError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidError) -> 'InvalidError':
        return InvalidError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidError):
        """
        Dynamic initializer for InvalidError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidError(java.lang.String,int)"""
        val = _InvalidError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidError(java.lang.String)"""
        val = _InvalidError(arg0)
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidError.getName()"""
        return str._wrap(super(InvalidError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidBooleanError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.InvalidBooleanError as _InvalidBooleanError
_InvalidBooleanError = _InvalidBooleanError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidBooleanError():
    """dev.ultreon.quantum.api.commands.error.InvalidBooleanError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidBooleanError) -> 'InvalidBooleanError':
        return InvalidBooleanError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidBooleanError):
        """
        Dynamic initializer for InvalidBooleanError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidBooleanError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidBooleanError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError()"""
        val = _InvalidBooleanError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError()"""
        val = _InvalidBooleanError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(java.lang.String)"""
        val = _InvalidBooleanError(arg0)
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(int)"""
        val = _InvalidBooleanError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidBooleanError.getName()"""
        return str._wrap(super(InvalidBooleanError, self).getName())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(java.lang.String,int)"""
        val = _InvalidBooleanError(arg0, _int.valueOf(arg1))
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError as _InvalidCoordinateZError
_InvalidCoordinateZError = _InvalidCoordinateZError
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCoordinateZError():
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCoordinateZError) -> 'InvalidCoordinateZError':
        return InvalidCoordinateZError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCoordinateZError):
        """
        Dynamic initializer for InvalidCoordinateZError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCoordinateZError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCoordinateZError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError()"""
        val = _InvalidCoordinateZError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(int)"""
        val = _InvalidCoordinateZError(_int.valueOf(arg0))
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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(java.lang.String)"""
        val = _InvalidCoordinateZError(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(java.lang.String,int)"""
        val = _InvalidCoordinateZError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError.getName()"""
        return str._wrap(super(InvalidCoordinateZError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError()"""
        val = _InvalidCoordinateZError()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidLongError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidLongError as _InvalidLongError
_InvalidLongError = _InvalidLongError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidLongError():
    """dev.ultreon.quantum.api.commands.error.InvalidLongError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidLongError) -> 'InvalidLongError':
        return InvalidLongError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidLongError):
        """
        Dynamic initializer for InvalidLongError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidLongError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidLongError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError()"""
        val = _InvalidLongError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidLongError.getName()"""
        return str._wrap(super(InvalidLongError, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError()"""
        val = _InvalidLongError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(java.lang.String)"""
        val = _InvalidLongError(arg0)
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(java.lang.String,int)"""
        val = _InvalidLongError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(int)"""
        val = _InvalidLongError(_int.valueOf(arg0))
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCharError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.error.InvalidCharError as _InvalidCharError
_InvalidCharError = _InvalidCharError
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCharError():
    """dev.ultreon.quantum.api.commands.error.InvalidCharError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCharError) -> 'InvalidCharError':
        return InvalidCharError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCharError):
        """
        Dynamic initializer for InvalidCharError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCharError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCharError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(int)"""
        val = _InvalidCharError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCharError.getName()"""
        return str._wrap(super(InvalidCharError, self).getName())

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
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(java.lang.String)"""
        val = _InvalidCharError(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError()"""
        val = _InvalidCharError()
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError()"""
        val = _InvalidCharError()
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(java.lang.String,int)"""
        val = _InvalidCharError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedLivingEntityError
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.error.NeedLivingEntityError as _NeedLivingEntityError
_NeedLivingEntityError = _NeedLivingEntityError
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NeedLivingEntityError():
    """dev.ultreon.quantum.api.commands.error.NeedLivingEntityError"""
 
    @staticmethod
    def _wrap(java_value: _NeedLivingEntityError) -> 'NeedLivingEntityError':
        return NeedLivingEntityError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NeedLivingEntityError):
        """
        Dynamic initializer for NeedLivingEntityError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NeedLivingEntityError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NeedLivingEntityError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedLivingEntityError.getName()"""
        return str._wrap(super(NeedLivingEntityError, self).getName())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError(int)"""
        val = _NeedLivingEntityError(_int.valueOf(arg0))
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError()"""
        val = _NeedLivingEntityError()
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError()"""
        val = _NeedLivingEntityError()
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NotFoundError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.NotFoundError as _NotFoundError
_NotFoundError = _NotFoundError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotFoundError():
    """dev.ultreon.quantum.api.commands.error.NotFoundError"""
 
    @staticmethod
    def _wrap(java_value: _NotFoundError) -> 'NotFoundError':
        return NotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotFoundError):
        """
        Dynamic initializer for NotFoundError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotFoundError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotFoundError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundError(java.lang.String,int)"""
        val = _NotFoundError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NotFoundError.getName()"""
        return str._wrap(super(NotFoundError, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NotFoundError(java.lang.String)"""
        val = _NotFoundError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidKeyError
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.error.InvalidKeyError as _InvalidKeyError
_InvalidKeyError = _InvalidKeyError
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidKeyError():
    """dev.ultreon.quantum.api.commands.error.InvalidKeyError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidKeyError) -> 'InvalidKeyError':
        return InvalidKeyError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidKeyError):
        """
        Dynamic initializer for InvalidKeyError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidKeyError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidKeyError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(java.lang.String)"""
        val = _InvalidKeyError(arg0)
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError()"""
        val = _InvalidKeyError()
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError()"""
        val = _InvalidKeyError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(java.lang.String,int)"""
        val = _InvalidKeyError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(int)"""
        val = _InvalidKeyError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidKeyError.getName()"""
        return str._wrap(super(InvalidKeyError, self).getName())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidDoubleError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.error.InvalidDoubleError as _InvalidDoubleError
_InvalidDoubleError = _InvalidDoubleError
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidDoubleError():
    """dev.ultreon.quantum.api.commands.error.InvalidDoubleError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidDoubleError) -> 'InvalidDoubleError':
        return InvalidDoubleError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidDoubleError):
        """
        Dynamic initializer for InvalidDoubleError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidDoubleError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidDoubleError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(int)"""
        val = _InvalidDoubleError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError()"""
        val = _InvalidDoubleError()
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

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(java.lang.String)"""
        val = _InvalidDoubleError(arg0)
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError()"""
        val = _InvalidDoubleError()
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(java.lang.String,int)"""
        val = _InvalidDoubleError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidDoubleError.getName()"""
        return str._wrap(super(InvalidDoubleError, self).getName())

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetNotFoundError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.TargetNotFoundError as _TargetNotFoundError
_TargetNotFoundError = _TargetNotFoundError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TargetNotFoundError():
    """dev.ultreon.quantum.api.commands.error.TargetNotFoundError"""
 
    @staticmethod
    def _wrap(java_value: _TargetNotFoundError) -> 'TargetNotFoundError':
        return TargetNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TargetNotFoundError):
        """
        Dynamic initializer for TargetNotFoundError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TargetNotFoundError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TargetNotFoundError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetNotFoundError.getName()"""
        return str._wrap(super(TargetNotFoundError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.TargetNotFoundError(java.lang.String,int)"""
        val = _TargetNotFoundError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.TargetNotFoundError(java.lang.String)"""
        val = _TargetNotFoundError(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedEntityError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.NeedEntityError as _NeedEntityError
_NeedEntityError = _NeedEntityError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NeedEntityError():
    """dev.ultreon.quantum.api.commands.error.NeedEntityError"""
 
    @staticmethod
    def _wrap(java_value: _NeedEntityError) -> 'NeedEntityError':
        return NeedEntityError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NeedEntityError):
        """
        Dynamic initializer for NeedEntityError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NeedEntityError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NeedEntityError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError(int)"""
        val = _NeedEntityError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedEntityError.getName()"""
        return str._wrap(super(NeedEntityError, self).getName())

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError()"""
        val = _NeedEntityError()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError()"""
        val = _NeedEntityError()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedPlayerError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.error.NeedPlayerError as _NeedPlayerError
_NeedPlayerError = _NeedPlayerError
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NeedPlayerError():
    """dev.ultreon.quantum.api.commands.error.NeedPlayerError"""
 
    @staticmethod
    def _wrap(java_value: _NeedPlayerError) -> 'NeedPlayerError':
        return NeedPlayerError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NeedPlayerError):
        """
        Dynamic initializer for NeedPlayerError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NeedPlayerError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NeedPlayerError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError(int)"""
        val = _NeedPlayerError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedPlayerError.getName()"""
        return str._wrap(super(NeedPlayerError, self).getName())

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError()"""
        val = _NeedPlayerError()
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError()"""
        val = _NeedPlayerError()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateError as _InvalidCoordinateError
_InvalidCoordinateError = _InvalidCoordinateError
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCoordinateError():
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCoordinateError) -> 'InvalidCoordinateError':
        return InvalidCoordinateError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCoordinateError):
        """
        Dynamic initializer for InvalidCoordinateError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCoordinateError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCoordinateError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String)"""
        val = _InvalidCoordinateError(arg0)
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,java.lang.String)"""
        val = _InvalidCoordinateError(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateError.getName()"""
        return str._wrap(super(InvalidCoordinateError, self).getName())

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,int)"""
        val = _InvalidCoordinateError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,java.lang.String,int)"""
        val = _InvalidCoordinateError(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidValueError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.api.commands.error.InvalidValueError as _InvalidValueError
_InvalidValueError = _InvalidValueError
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidValueError():
    """dev.ultreon.quantum.api.commands.error.InvalidValueError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidValueError) -> 'InvalidValueError':
        return InvalidValueError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidValueError):
        """
        Dynamic initializer for InvalidValueError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidValueError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidValueError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,java.lang.String)"""
        val = _InvalidValueError(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,java.lang.String,int)"""
        val = _InvalidValueError(arg0, arg1, _int.valueOf(arg2))
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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidValueError.getName()"""
        return str._wrap(super(InvalidValueError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String)"""
        val = _InvalidValueError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,int)"""
        val = _InvalidValueError(arg0, _int.valueOf(arg1))
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidVariableError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.error.InvalidVariableError as _InvalidVariableError
_InvalidVariableError = _InvalidVariableError
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidError as _InvalidError
_InvalidError = _InvalidError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidVariableError():
    """dev.ultreon.quantum.api.commands.error.InvalidVariableError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidVariableError) -> 'InvalidVariableError':
        return InvalidVariableError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidVariableError):
        """
        Dynamic initializer for InvalidVariableError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidVariableError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidVariableError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError(java.lang.String)"""
        val = _InvalidVariableError(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError()"""
        val = _InvalidVariableError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError()"""
        val = _InvalidVariableError()
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidError.getName()"""
        return str._wrap(super(InvalidError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.CommandError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CommandError():
    """dev.ultreon.quantum.api.commands.error.CommandError"""
 
    @staticmethod
    def _wrap(java_value: _CommandError) -> 'CommandError':
        return CommandError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CommandError):
        """
        Dynamic initializer for CommandError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CommandError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CommandError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

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
    def __init__(self, arg0: 'MessageCode', arg1: str):
        """public dev.ultreon.quantum.api.commands.error.CommandError(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        val = _CommandError(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.CommandError(java.lang.String)"""
        val = _CommandError(arg0)
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getName()"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.CommandError(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,int)"""
        val = _CommandError(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.CommandError(java.lang.String,int)"""
        val = _CommandError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NotFoundInWorldError
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.NotFoundInWorldError as _NotFoundInWorldError
_NotFoundInWorldError = _NotFoundInWorldError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NotFoundInWorldError():
    """dev.ultreon.quantum.api.commands.error.NotFoundInWorldError"""
 
    @staticmethod
    def _wrap(java_value: _NotFoundInWorldError) -> 'NotFoundInWorldError':
        return NotFoundInWorldError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NotFoundInWorldError):
        """
        Dynamic initializer for NotFoundInWorldError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NotFoundInWorldError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NotFoundInWorldError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: 'World'):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,dev.ultreon.quantum.world.World)"""
        val = _NotFoundInWorldError(arg0, arg1)
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NotFoundInWorldError.getName()"""
        return str._wrap(super(NotFoundInWorldError, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'World', arg2: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,dev.ultreon.quantum.world.World,int)"""
        val = _NotFoundInWorldError(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String)"""
        val = _NotFoundInWorldError(arg0)
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,int)"""
        val = _NotFoundInWorldError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidSelectorError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.InvalidSelectorError as _InvalidSelectorError
_InvalidSelectorError = _InvalidSelectorError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidSelectorError():
    """dev.ultreon.quantum.api.commands.error.InvalidSelectorError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidSelectorError) -> 'InvalidSelectorError':
        return InvalidSelectorError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidSelectorError):
        """
        Dynamic initializer for InvalidSelectorError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidSelectorError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidSelectorError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidSelectorError(java.lang.String)"""
        val = _InvalidSelectorError(arg0)
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidSelectorError(java.lang.String,int)"""
        val = _InvalidSelectorError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidSelectorError.getName()"""
        return str._wrap(super(InvalidSelectorError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidLocationError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidLocationError as _InvalidLocationError
_InvalidLocationError = _InvalidLocationError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidLocationError():
    """dev.ultreon.quantum.api.commands.error.InvalidLocationError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidLocationError) -> 'InvalidLocationError':
        return InvalidLocationError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidLocationError):
        """
        Dynamic initializer for InvalidLocationError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidLocationError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidLocationError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(java.lang.String,int)"""
        val = _InvalidLocationError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError()"""
        val = _InvalidLocationError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError()"""
        val = _InvalidLocationError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(int)"""
        val = _InvalidLocationError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(java.lang.String)"""
        val = _InvalidLocationError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidLocationError.getName()"""
        return str._wrap(super(InvalidLocationError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError as _InvalidCoordinateYError
_InvalidCoordinateYError = _InvalidCoordinateYError
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidCoordinateYError():
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidCoordinateYError) -> 'InvalidCoordinateYError':
        return InvalidCoordinateYError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidCoordinateYError):
        """
        Dynamic initializer for InvalidCoordinateYError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidCoordinateYError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidCoordinateYError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError.getName()"""
        return str._wrap(super(InvalidCoordinateYError, self).getName())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(int)"""
        val = _InvalidCoordinateYError(_int.valueOf(arg0))
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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError()"""
        val = _InvalidCoordinateYError()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(java.lang.String,java.lang.String)"""
        val = _InvalidCoordinateYError(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(java.lang.String,java.lang.String,int)"""
        val = _InvalidCoordinateYError(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError()"""
        val = _InvalidCoordinateYError()
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InternalError
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.api.commands.error.InternalError as _InternalError
_InternalError = _InternalError
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InternalError():
    """dev.ultreon.quantum.api.commands.error.InternalError"""
 
    @staticmethod
    def _wrap(java_value: _InternalError) -> 'InternalError':
        return InternalError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InternalError):
        """
        Dynamic initializer for InternalError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InternalError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InternalError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InternalError.getName()"""
        return str._wrap(super(InternalError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InternalError(java.lang.String)"""
        val = _InternalError(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError as _TargetEntityNotFoundError
_TargetEntityNotFoundError = _TargetEntityNotFoundError
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TargetEntityNotFoundError():
    """dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError"""
 
    @staticmethod
    def _wrap(java_value: _TargetEntityNotFoundError) -> 'TargetEntityNotFoundError':
        return TargetEntityNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TargetEntityNotFoundError):
        """
        Dynamic initializer for TargetEntityNotFoundError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TargetEntityNotFoundError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TargetEntityNotFoundError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError(java.lang.String,int)"""
        val = _TargetEntityNotFoundError(arg0, _int.valueOf(arg1))
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError.getName()"""
        return str._wrap(super(TargetEntityNotFoundError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError(java.lang.String)"""
        val = _TargetEntityNotFoundError(arg0)
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError as _TargetPlayerNotFoundError
_TargetPlayerNotFoundError = _TargetPlayerNotFoundError
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TargetPlayerNotFoundError():
    """dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError"""
 
    @staticmethod
    def _wrap(java_value: _TargetPlayerNotFoundError) -> 'TargetPlayerNotFoundError':
        return TargetPlayerNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TargetPlayerNotFoundError):
        """
        Dynamic initializer for TargetPlayerNotFoundError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TargetPlayerNotFoundError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TargetPlayerNotFoundError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError(int)"""
        val = _TargetPlayerNotFoundError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError()"""
        val = _TargetPlayerNotFoundError()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError()"""
        val = _TargetPlayerNotFoundError()
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError.getName()"""
        return str._wrap(super(TargetPlayerNotFoundError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidUUIDError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.InvalidUUIDError as _InvalidUUIDError
_InvalidUUIDError = _InvalidUUIDError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidUUIDError():
    """dev.ultreon.quantum.api.commands.error.InvalidUUIDError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidUUIDError) -> 'InvalidUUIDError':
        return InvalidUUIDError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidUUIDError):
        """
        Dynamic initializer for InvalidUUIDError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidUUIDError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidUUIDError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(java.lang.String)"""
        val = _InvalidUUIDError(arg0)
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
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(int)"""
        val = _InvalidUUIDError(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError()"""
        val = _InvalidUUIDError()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(java.lang.String,int)"""
        val = _InvalidUUIDError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidUUIDError.getName()"""
        return str._wrap(super(InvalidUUIDError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError()"""
        val = _InvalidUUIDError()
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidIntegerError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.InvalidIntegerError as _InvalidIntegerError
_InvalidIntegerError = _InvalidIntegerError
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InvalidIntegerError():
    """dev.ultreon.quantum.api.commands.error.InvalidIntegerError"""
 
    @staticmethod
    def _wrap(java_value: _InvalidIntegerError) -> 'InvalidIntegerError':
        return InvalidIntegerError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InvalidIntegerError):
        """
        Dynamic initializer for InvalidIntegerError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InvalidIntegerError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InvalidIntegerError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError()"""
        val = _InvalidIntegerError()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError()"""
        val = _InvalidIntegerError()
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(java.lang.String)"""
        val = _InvalidIntegerError(arg0)
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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(int)"""
        val = _InvalidIntegerError(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(java.lang.String,int)"""
        val = _InvalidIntegerError(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidIntegerError.getName()"""
        return str._wrap(super(InvalidIntegerError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError as _PlayerIsOnlineError
_PlayerIsOnlineError = _PlayerIsOnlineError
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PlayerIsOnlineError():
    """dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError"""
 
    @staticmethod
    def _wrap(java_value: _PlayerIsOnlineError) -> 'PlayerIsOnlineError':
        return PlayerIsOnlineError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PlayerIsOnlineError):
        """
        Dynamic initializer for PlayerIsOnlineError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PlayerIsOnlineError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PlayerIsOnlineError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError.getName()"""
        return str._wrap(super(PlayerIsOnlineError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError(java.lang.String)"""
        val = _PlayerIsOnlineError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.SelectorTooSmallError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
import dev.ultreon.quantum.api.commands.error.SelectorTooSmallError as _SelectorTooSmallError
_SelectorTooSmallError = _SelectorTooSmallError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SelectorTooSmallError():
    """dev.ultreon.quantum.api.commands.error.SelectorTooSmallError"""
 
    @staticmethod
    def _wrap(java_value: _SelectorTooSmallError) -> 'SelectorTooSmallError':
        return SelectorTooSmallError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SelectorTooSmallError):
        """
        Dynamic initializer for SelectorTooSmallError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SelectorTooSmallError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SelectorTooSmallError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

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
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.SelectorTooSmallError.getName()"""
        return str._wrap(super(SelectorTooSmallError, self).getName())

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.SelectorTooSmallError(java.lang.String)"""
        val = _SelectorTooSmallError(arg0)
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.SelectorTooSmallError(java.lang.String,int)"""
        val = _SelectorTooSmallError(arg0, _int.valueOf(arg1))
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
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.ImpossibleError
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.api.commands.MessageCode as _MessageCode
_MessageCode = _MessageCode
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.api.commands.error.ImpossibleError as _ImpossibleError
_ImpossibleError = _ImpossibleError
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.api.commands.error.CommandError as _CommandError
_CommandError = _CommandError
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImpossibleError():
    """dev.ultreon.quantum.api.commands.error.ImpossibleError"""
 
    @staticmethod
    def _wrap(java_value: _ImpossibleError) -> 'ImpossibleError':
        return ImpossibleError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImpossibleError):
        """
        Dynamic initializer for ImpossibleError.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImpossibleError__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImpossibleError__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).addIndex(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.ImpossibleError(java.lang.String)"""
        val = _ImpossibleError(arg0)
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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.ImpossibleError.getName()"""
        return str._wrap(super(ImpossibleError, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(_CommandError, self).send(arg0, arg1)

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'._wrap(super(_CommandError, self).setIndex(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int._wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(_CommandError, self).setOnlyOverloads(_boolean.valueOf(arg0))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(_CommandError, self).send(arg0)

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'._wrap(super(CommandError, self).getMessageCode())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str._wrap(super(CommandError, self).getMessage())

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