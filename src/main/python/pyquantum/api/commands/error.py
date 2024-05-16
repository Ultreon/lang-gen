from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.error.PermissionsBrokenError as __PermissionsBrokenError
__PermissionsBrokenError = __PermissionsBrokenError
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PermissionsBrokenError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.PermissionsBrokenError"""
 
    @staticmethod
    def __wrap(java_value: __PermissionsBrokenError) -> 'PermissionsBrokenError':
        return PermissionsBrokenError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PermissionsBrokenError):
        """
        Dynamic initializer for PermissionsBrokenError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = __PermissionsBrokenError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.getName()"""
        return str.__wrap(super(PermissionsBrokenError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.setName(java.lang.String)"""
        super(__PermissionsBrokenError, self).setName(arg0)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = __PermissionsBrokenError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PermissionsBrokenError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.error.PermissionsBrokenError as __PermissionsBrokenError
__PermissionsBrokenError = __PermissionsBrokenError
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PermissionsBrokenError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.PermissionsBrokenError"""
 
    @staticmethod
    def __wrap(java_value: __PermissionsBrokenError) -> 'PermissionsBrokenError':
        return PermissionsBrokenError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PermissionsBrokenError):
        """
        Dynamic initializer for PermissionsBrokenError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = __PermissionsBrokenError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.getName()"""
        return str.__wrap(super(PermissionsBrokenError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def setName(self, arg0: str):
        """public void dev.ultreon.quantum.api.commands.error.PermissionsBrokenError.setName(java.lang.String)"""
        super(__PermissionsBrokenError, self).setName(arg0)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.PermissionsBrokenError()"""
        val = __PermissionsBrokenError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PermissionsBrokenError 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NoPermissionError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.error.NoPermissionError as __NoPermissionError
__NoPermissionError = __NoPermissionError
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NoPermissionError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NoPermissionError"""
 
    @staticmethod
    def __wrap(java_value: __NoPermissionError) -> 'NoPermissionError':
        return NoPermissionError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoPermissionError):
        """
        Dynamic initializer for NoPermissionError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NoPermissionError()"""
        val = __NoPermissionError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NoPermissionError.getName()"""
        return str.__wrap(super(NoPermissionError, self).getName())

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NoPermissionError()"""
        val = __NoPermissionError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError as __InvalidCoordinateXError
__InvalidCoordinateXError = __InvalidCoordinateXError
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCoordinateXError(__InvalidCoordinateError, InvalidCoordinateError):
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCoordinateXError) -> 'InvalidCoordinateXError':
        return InvalidCoordinateXError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCoordinateXError):
        """
        Dynamic initializer for InvalidCoordinateXError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError()"""
        val = __InvalidCoordinateXError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(java.lang.String)"""
        val = __InvalidCoordinateXError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError.getName()"""
        return str.__wrap(super(InvalidCoordinateXError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(java.lang.String,int)"""
        val = __InvalidCoordinateXError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError(int)"""
        val = __InvalidCoordinateXError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateXError()"""
        val = __InvalidCoordinateXError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidShortError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidShortError as __InvalidShortError
__InvalidShortError = __InvalidShortError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidShortError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidShortError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidShortError) -> 'InvalidShortError':
        return InvalidShortError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidShortError):
        """
        Dynamic initializer for InvalidShortError.
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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError()"""
        val = __InvalidShortError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidShortError.getName()"""
        return str.__wrap(super(InvalidShortError, self).getName())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError()"""
        val = __InvalidShortError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(java.lang.String)"""
        val = __InvalidShortError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(int)"""
        val = __InvalidShortError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidShortError(java.lang.String,int)"""
        val = __InvalidShortError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NoSelectedError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.api.commands.error.NoSelectedError as __NoSelectedError
__NoSelectedError = __NoSelectedError
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NoSelectedError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NoSelectedError"""
 
    @staticmethod
    def __wrap(java_value: __NoSelectedError) -> 'NoSelectedError':
        return NoSelectedError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NoSelectedError):
        """
        Dynamic initializer for NoSelectedError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NoSelectedError(java.lang.String)"""
        val = __NoSelectedError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NoSelectedError.getName()"""
        return str.__wrap(super(NoSelectedError, self).getName())

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NoSelectedError(java.lang.String,int)"""
        val = __NoSelectedError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.OverloadError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.OverloadError as __OverloadError
__OverloadError = __OverloadError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OverloadError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.OverloadError"""
 
    @staticmethod
    def __wrap(java_value: __OverloadError) -> 'OverloadError':
        return OverloadError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OverloadError):
        """
        Dynamic initializer for OverloadError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.OverloadError()"""
        val = __OverloadError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.OverloadError(int)"""
        val = __OverloadError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.OverloadError.getName()"""
        return str.__wrap(super(OverloadError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.OverloadError()"""
        val = __OverloadError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidTargetError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidTargetError as __InvalidTargetError
__InvalidTargetError = __InvalidTargetError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidTargetError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidTargetError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidTargetError) -> 'InvalidTargetError':
        return InvalidTargetError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidTargetError):
        """
        Dynamic initializer for InvalidTargetError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(int)"""
        val = __InvalidTargetError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError()"""
        val = __InvalidTargetError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(java.lang.String)"""
        val = __InvalidTargetError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError(java.lang.String,int)"""
        val = __InvalidTargetError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidTargetError()"""
        val = __InvalidTargetError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidTargetError.getName()"""
        return str.__wrap(super(InvalidTargetError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidByteError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidByteError as __InvalidByteError
__InvalidByteError = __InvalidByteError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidByteError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidByteError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidByteError) -> 'InvalidByteError':
        return InvalidByteError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidByteError):
        """
        Dynamic initializer for InvalidByteError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidByteError.getName()"""
        return str.__wrap(super(InvalidByteError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError()"""
        val = __InvalidByteError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(java.lang.String)"""
        val = __InvalidByteError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(java.lang.String,int)"""
        val = __InvalidByteError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError(int)"""
        val = __InvalidByteError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidByteError()"""
        val = __InvalidByteError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidFloatError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import dev.ultreon.quantum.api.commands.error.InvalidFloatError as __InvalidFloatError
__InvalidFloatError = __InvalidFloatError
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidFloatError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidFloatError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidFloatError) -> 'InvalidFloatError':
        return InvalidFloatError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidFloatError):
        """
        Dynamic initializer for InvalidFloatError.
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
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError()"""
        val = __InvalidFloatError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(java.lang.String)"""
        val = __InvalidFloatError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(java.lang.String,int)"""
        val = __InvalidFloatError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError()"""
        val = __InvalidFloatError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidFloatError.getName()"""
        return str.__wrap(super(InvalidFloatError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidFloatError(int)"""
        val = __InvalidFloatError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidError as __InvalidError
__InvalidError = __InvalidError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.InvalidError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidError) -> 'InvalidError':
        return InvalidError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidError):
        """
        Dynamic initializer for InvalidError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidError(java.lang.String,int)"""
        val = __InvalidError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidError(java.lang.String)"""
        val = __InvalidError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidError.getName()"""
        return str.__wrap(super(InvalidError, self).getName())

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidBooleanError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.error.InvalidBooleanError as __InvalidBooleanError
__InvalidBooleanError = __InvalidBooleanError
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidBooleanError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidBooleanError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidBooleanError) -> 'InvalidBooleanError':
        return InvalidBooleanError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidBooleanError):
        """
        Dynamic initializer for InvalidBooleanError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(java.lang.String,int)"""
        val = __InvalidBooleanError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError()"""
        val = __InvalidBooleanError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(java.lang.String)"""
        val = __InvalidBooleanError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError(int)"""
        val = __InvalidBooleanError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidBooleanError()"""
        val = __InvalidBooleanError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidBooleanError.getName()"""
        return str.__wrap(super(InvalidBooleanError, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError as __InvalidCoordinateZError
__InvalidCoordinateZError = __InvalidCoordinateZError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCoordinateZError(__InvalidCoordinateError, InvalidCoordinateError):
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCoordinateZError) -> 'InvalidCoordinateZError':
        return InvalidCoordinateZError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCoordinateZError):
        """
        Dynamic initializer for InvalidCoordinateZError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(java.lang.String,int)"""
        val = __InvalidCoordinateZError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError.getName()"""
        return str.__wrap(super(InvalidCoordinateZError, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError()"""
        val = __InvalidCoordinateZError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError()"""
        val = __InvalidCoordinateZError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(java.lang.String)"""
        val = __InvalidCoordinateZError(arg0)
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateZError(int)"""
        val = __InvalidCoordinateZError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidLongError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidLongError as __InvalidLongError
__InvalidLongError = __InvalidLongError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidLongError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidLongError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidLongError) -> 'InvalidLongError':
        return InvalidLongError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidLongError):
        """
        Dynamic initializer for InvalidLongError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError()"""
        val = __InvalidLongError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError()"""
        val = __InvalidLongError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(java.lang.String)"""
        val = __InvalidLongError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(int)"""
        val = __InvalidLongError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidLongError.getName()"""
        return str.__wrap(super(InvalidLongError, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLongError(java.lang.String,int)"""
        val = __InvalidLongError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCharError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidCharError as __InvalidCharError
__InvalidCharError = __InvalidCharError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCharError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidCharError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCharError) -> 'InvalidCharError':
        return InvalidCharError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCharError):
        """
        Dynamic initializer for InvalidCharError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(java.lang.String,int)"""
        val = __InvalidCharError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(int)"""
        val = __InvalidCharError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCharError.getName()"""
        return str.__wrap(super(InvalidCharError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError()"""
        val = __InvalidCharError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError()"""
        val = __InvalidCharError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCharError(java.lang.String)"""
        val = __InvalidCharError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedLivingEntityError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.error.NeedLivingEntityError as __NeedLivingEntityError
__NeedLivingEntityError = __NeedLivingEntityError
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NeedLivingEntityError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NeedLivingEntityError"""
 
    @staticmethod
    def __wrap(java_value: __NeedLivingEntityError) -> 'NeedLivingEntityError':
        return NeedLivingEntityError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NeedLivingEntityError):
        """
        Dynamic initializer for NeedLivingEntityError.
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
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedLivingEntityError.getName()"""
        return str.__wrap(super(NeedLivingEntityError, self).getName())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError(int)"""
        val = __NeedLivingEntityError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError()"""
        val = __NeedLivingEntityError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedLivingEntityError()"""
        val = __NeedLivingEntityError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NotFoundError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.NotFoundError as __NotFoundError
__NotFoundError = __NotFoundError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotFoundError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NotFoundError"""
 
    @staticmethod
    def __wrap(java_value: __NotFoundError) -> 'NotFoundError':
        return NotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotFoundError):
        """
        Dynamic initializer for NotFoundError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NotFoundError.getName()"""
        return str.__wrap(super(NotFoundError, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundError(java.lang.String,int)"""
        val = __NotFoundError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NotFoundError(java.lang.String)"""
        val = __NotFoundError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidKeyError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
import dev.ultreon.quantum.api.commands.error.InvalidKeyError as __InvalidKeyError
__InvalidKeyError = __InvalidKeyError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidKeyError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidKeyError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidKeyError) -> 'InvalidKeyError':
        return InvalidKeyError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidKeyError):
        """
        Dynamic initializer for InvalidKeyError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError()"""
        val = __InvalidKeyError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(java.lang.String,int)"""
        val = __InvalidKeyError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidKeyError.getName()"""
        return str.__wrap(super(InvalidKeyError, self).getName())

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(java.lang.String)"""
        val = __InvalidKeyError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError()"""
        val = __InvalidKeyError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidKeyError(int)"""
        val = __InvalidKeyError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidDoubleError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidDoubleError as __InvalidDoubleError
__InvalidDoubleError = __InvalidDoubleError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidDoubleError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidDoubleError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidDoubleError) -> 'InvalidDoubleError':
        return InvalidDoubleError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidDoubleError):
        """
        Dynamic initializer for InvalidDoubleError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(int)"""
        val = __InvalidDoubleError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError()"""
        val = __InvalidDoubleError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(java.lang.String)"""
        val = __InvalidDoubleError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidDoubleError.getName()"""
        return str.__wrap(super(InvalidDoubleError, self).getName())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError()"""
        val = __InvalidDoubleError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidDoubleError(java.lang.String,int)"""
        val = __InvalidDoubleError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetNotFoundError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.error.TargetNotFoundError as __TargetNotFoundError
__TargetNotFoundError = __TargetNotFoundError
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TargetNotFoundError(__NotFoundError, NotFoundError):
    """dev.ultreon.quantum.api.commands.error.TargetNotFoundError"""
 
    @staticmethod
    def __wrap(java_value: __TargetNotFoundError) -> 'TargetNotFoundError':
        return TargetNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TargetNotFoundError):
        """
        Dynamic initializer for TargetNotFoundError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetNotFoundError.getName()"""
        return str.__wrap(super(TargetNotFoundError, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.TargetNotFoundError(java.lang.String,int)"""
        val = __TargetNotFoundError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.TargetNotFoundError(java.lang.String)"""
        val = __TargetNotFoundError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedEntityError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.api.commands.error.NeedEntityError as __NeedEntityError
__NeedEntityError = __NeedEntityError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NeedEntityError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NeedEntityError"""
 
    @staticmethod
    def __wrap(java_value: __NeedEntityError) -> 'NeedEntityError':
        return NeedEntityError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NeedEntityError):
        """
        Dynamic initializer for NeedEntityError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError()"""
        val = __NeedEntityError()
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError()"""
        val = __NeedEntityError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedEntityError(int)"""
        val = __NeedEntityError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedEntityError.getName()"""
        return str.__wrap(super(NeedEntityError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NeedPlayerError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.api.commands.error.NeedPlayerError as __NeedPlayerError
__NeedPlayerError = __NeedPlayerError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NeedPlayerError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NeedPlayerError"""
 
    @staticmethod
    def __wrap(java_value: __NeedPlayerError) -> 'NeedPlayerError':
        return NeedPlayerError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NeedPlayerError):
        """
        Dynamic initializer for NeedPlayerError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError()"""
        val = __NeedPlayerError()
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError()"""
        val = __NeedPlayerError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NeedPlayerError.getName()"""
        return str.__wrap(super(NeedPlayerError, self).getName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.NeedPlayerError(int)"""
        val = __NeedPlayerError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateError as __InvalidCoordinateError
__InvalidCoordinateError = __InvalidCoordinateError
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCoordinateError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCoordinateError) -> 'InvalidCoordinateError':
        return InvalidCoordinateError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCoordinateError):
        """
        Dynamic initializer for InvalidCoordinateError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateError.getName()"""
        return str.__wrap(super(InvalidCoordinateError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String)"""
        val = __InvalidCoordinateError(arg0)
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,int)"""
        val = __InvalidCoordinateError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,java.lang.String)"""
        val = __InvalidCoordinateError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateError(java.lang.String,java.lang.String,int)"""
        val = __InvalidCoordinateError(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidValueError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidValueError as __InvalidValueError
__InvalidValueError = __InvalidValueError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidValueError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.InvalidValueError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidValueError) -> 'InvalidValueError':
        return InvalidValueError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidValueError):
        """
        Dynamic initializer for InvalidValueError.
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
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,int)"""
        val = __InvalidValueError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,java.lang.String)"""
        val = __InvalidValueError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidValueError.getName()"""
        return str.__wrap(super(InvalidValueError, self).getName())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String,java.lang.String,int)"""
        val = __InvalidValueError(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidValueError(java.lang.String)"""
        val = __InvalidValueError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidVariableError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.error.InvalidVariableError as __InvalidVariableError
__InvalidVariableError = __InvalidVariableError
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidError as __InvalidError
__InvalidError = __InvalidError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidVariableError(__InvalidError, InvalidError):
    """dev.ultreon.quantum.api.commands.error.InvalidVariableError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidVariableError) -> 'InvalidVariableError':
        return InvalidVariableError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidVariableError):
        """
        Dynamic initializer for InvalidVariableError.
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
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError(java.lang.String)"""
        val = __InvalidVariableError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError()"""
        val = __InvalidVariableError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
        """public dev.ultreon.quantum.api.commands.error.InvalidVariableError()"""
        val = __InvalidVariableError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidError.getName()"""
        return str.__wrap(super(InvalidError, self).getName())

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.CommandError
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

from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CommandError(ABC, commands.__CommandResult, output.CommandResult):
    """dev.ultreon.quantum.api.commands.error.CommandError"""
 
    @staticmethod
    def __wrap(java_value: __CommandError) -> 'CommandError':
        return CommandError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CommandError):
        """
        Dynamic initializer for CommandError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.CommandError(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String,int)"""
        val = __CommandError(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.CommandError(java.lang.String,int)"""
        val = __CommandError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.CommandError(java.lang.String)"""
        val = __CommandError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

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
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getName()"""
        pass

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

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
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'MessageCode', arg1: str):
        """public dev.ultreon.quantum.api.commands.error.CommandError(dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        val = __CommandError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.NotFoundInWorldError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.NotFoundInWorldError as __NotFoundInWorldError
__NotFoundInWorldError = __NotFoundInWorldError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NotFoundInWorldError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.NotFoundInWorldError"""
 
    @staticmethod
    def __wrap(java_value: __NotFoundInWorldError) -> 'NotFoundInWorldError':
        return NotFoundInWorldError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NotFoundInWorldError):
        """
        Dynamic initializer for NotFoundInWorldError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,int)"""
        val = __NotFoundInWorldError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str, arg1: 'World', arg2: int):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,dev.ultreon.quantum.world.World,int)"""
        val = __NotFoundInWorldError(arg0, arg1, __int.valueOf(arg2))
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String)"""
        val = __NotFoundInWorldError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.NotFoundInWorldError.getName()"""
        return str.__wrap(super(NotFoundInWorldError, self).getName())

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: str, arg1: 'World'):
        """public dev.ultreon.quantum.api.commands.error.NotFoundInWorldError(java.lang.String,dev.ultreon.quantum.world.World)"""
        val = __NotFoundInWorldError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidSelectorError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidSelectorError as __InvalidSelectorError
__InvalidSelectorError = __InvalidSelectorError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidSelectorError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidSelectorError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidSelectorError) -> 'InvalidSelectorError':
        return InvalidSelectorError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidSelectorError):
        """
        Dynamic initializer for InvalidSelectorError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidSelectorError.getName()"""
        return str.__wrap(super(InvalidSelectorError, self).getName())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidSelectorError(java.lang.String)"""
        val = __InvalidSelectorError(arg0)
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidSelectorError(java.lang.String,int)"""
        val = __InvalidSelectorError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidLocationError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import dev.ultreon.quantum.api.commands.error.InvalidLocationError as __InvalidLocationError
__InvalidLocationError = __InvalidLocationError
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidLocationError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidLocationError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidLocationError) -> 'InvalidLocationError':
        return InvalidLocationError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidLocationError):
        """
        Dynamic initializer for InvalidLocationError.
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
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(int)"""
        val = __InvalidLocationError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError()"""
        val = __InvalidLocationError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidLocationError.getName()"""
        return str.__wrap(super(InvalidLocationError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(java.lang.String,int)"""
        val = __InvalidLocationError(arg0, __int.valueOf(arg1))
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError(java.lang.String)"""
        val = __InvalidLocationError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidLocationError()"""
        val = __InvalidLocationError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError as __InvalidCoordinateYError
__InvalidCoordinateYError = __InvalidCoordinateYError
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidCoordinateYError(__InvalidCoordinateError, InvalidCoordinateError):
    """dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidCoordinateYError) -> 'InvalidCoordinateYError':
        return InvalidCoordinateYError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidCoordinateYError):
        """
        Dynamic initializer for InvalidCoordinateYError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError()"""
        val = __InvalidCoordinateYError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError.getName()"""
        return str.__wrap(super(InvalidCoordinateYError, self).getName())

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: str, arg1: str, arg2: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(java.lang.String,java.lang.String,int)"""
        val = __InvalidCoordinateYError(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(int)"""
        val = __InvalidCoordinateYError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError()"""
        val = __InvalidCoordinateYError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidCoordinateYError(java.lang.String,java.lang.String)"""
        val = __InvalidCoordinateYError(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InternalError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InternalError as __InternalError
__InternalError = __InternalError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InternalError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.InternalError"""
 
    @staticmethod
    def __wrap(java_value: __InternalError) -> 'InternalError':
        return InternalError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InternalError):
        """
        Dynamic initializer for InternalError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InternalError(java.lang.String)"""
        val = __InternalError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InternalError.getName()"""
        return str.__wrap(super(InternalError, self).getName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError as __TargetEntityNotFoundError
__TargetEntityNotFoundError = __TargetEntityNotFoundError
from builtins import int
 
class TargetEntityNotFoundError(__TargetNotFoundError, TargetNotFoundError):
    """dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError"""
 
    @staticmethod
    def __wrap(java_value: __TargetEntityNotFoundError) -> 'TargetEntityNotFoundError':
        return TargetEntityNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TargetEntityNotFoundError):
        """
        Dynamic initializer for TargetEntityNotFoundError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError(java.lang.String,int)"""
        val = __TargetEntityNotFoundError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError(java.lang.String)"""
        val = __TargetEntityNotFoundError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetEntityNotFoundError.getName()"""
        return str.__wrap(super(TargetEntityNotFoundError, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError as __TargetPlayerNotFoundError
__TargetPlayerNotFoundError = __TargetPlayerNotFoundError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TargetPlayerNotFoundError(__TargetNotFoundError, TargetNotFoundError):
    """dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError"""
 
    @staticmethod
    def __wrap(java_value: __TargetPlayerNotFoundError) -> 'TargetPlayerNotFoundError':
        return TargetPlayerNotFoundError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TargetPlayerNotFoundError):
        """
        Dynamic initializer for TargetPlayerNotFoundError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError()"""
        val = __TargetPlayerNotFoundError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError.getName()"""
        return str.__wrap(super(TargetPlayerNotFoundError, self).getName())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError()"""
        val = __TargetPlayerNotFoundError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.TargetPlayerNotFoundError(int)"""
        val = __TargetPlayerNotFoundError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidUUIDError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import dev.ultreon.quantum.api.commands.error.InvalidUUIDError as __InvalidUUIDError
__InvalidUUIDError = __InvalidUUIDError
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidUUIDError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidUUIDError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidUUIDError) -> 'InvalidUUIDError':
        return InvalidUUIDError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidUUIDError):
        """
        Dynamic initializer for InvalidUUIDError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError()"""
        val = __InvalidUUIDError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidUUIDError.getName()"""
        return str.__wrap(super(InvalidUUIDError, self).getName())

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(int)"""
        val = __InvalidUUIDError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(java.lang.String)"""
        val = __InvalidUUIDError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError()"""
        val = __InvalidUUIDError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidUUIDError(java.lang.String,int)"""
        val = __InvalidUUIDError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.InvalidIntegerError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.api.commands.error.InvalidIntegerError as __InvalidIntegerError
__InvalidIntegerError = __InvalidIntegerError
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InvalidIntegerError(__InvalidValueError, InvalidValueError):
    """dev.ultreon.quantum.api.commands.error.InvalidIntegerError"""
 
    @staticmethod
    def __wrap(java_value: __InvalidIntegerError) -> 'InvalidIntegerError':
        return InvalidIntegerError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InvalidIntegerError):
        """
        Dynamic initializer for InvalidIntegerError.
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
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(int)"""
        val = __InvalidIntegerError(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(java.lang.String,int)"""
        val = __InvalidIntegerError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError()"""
        val = __InvalidIntegerError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError()"""
        val = __InvalidIntegerError()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.InvalidIntegerError.getName()"""
        return str.__wrap(super(InvalidIntegerError, self).getName())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.InvalidIntegerError(java.lang.String)"""
        val = __InvalidIntegerError(arg0)
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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError as __PlayerIsOnlineError
__PlayerIsOnlineError = __PlayerIsOnlineError
from builtins import bool
from builtins import int
 
class PlayerIsOnlineError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError"""
 
    @staticmethod
    def __wrap(java_value: __PlayerIsOnlineError) -> 'PlayerIsOnlineError':
        return PlayerIsOnlineError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayerIsOnlineError):
        """
        Dynamic initializer for PlayerIsOnlineError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError.getName()"""
        return str.__wrap(super(PlayerIsOnlineError, self).getName())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.PlayerIsOnlineError(java.lang.String)"""
        val = __PlayerIsOnlineError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.SelectorTooSmallError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.error.SelectorTooSmallError as __SelectorTooSmallError
__SelectorTooSmallError = __SelectorTooSmallError
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SelectorTooSmallError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.SelectorTooSmallError"""
 
    @staticmethod
    def __wrap(java_value: __SelectorTooSmallError) -> 'SelectorTooSmallError':
        return SelectorTooSmallError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SelectorTooSmallError):
        """
        Dynamic initializer for SelectorTooSmallError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.SelectorTooSmallError.getName()"""
        return str.__wrap(super(SelectorTooSmallError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.SelectorTooSmallError(java.lang.String)"""
        val = __SelectorTooSmallError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: str, arg1: int):
        """public dev.ultreon.quantum.api.commands.error.SelectorTooSmallError(java.lang.String,int)"""
        val = __SelectorTooSmallError(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode()) 
 
 
# CLASS: dev.ultreon.quantum.api.commands.error.ImpossibleError
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.api.commands.error.CommandError as __CommandError
__CommandError = __CommandError
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

import java.lang.Long as __long
import dev.ultreon.quantum.api.commands.error.ImpossibleError as __ImpossibleError
__ImpossibleError = __ImpossibleError
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.api.commands.MessageCode as __MessageCode
__MessageCode = __MessageCode
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ImpossibleError(__CommandError, CommandError):
    """dev.ultreon.quantum.api.commands.error.ImpossibleError"""
 
    @staticmethod
    def __wrap(java_value: __ImpossibleError) -> 'ImpossibleError':
        return ImpossibleError(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImpossibleError):
        """
        Dynamic initializer for ImpossibleError.
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
    def send(self, arg0: 'CommandSender'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender)"""
        super(__CommandError, self).send(arg0)

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.api.commands.error.ImpossibleError(java.lang.String)"""
        val = __ImpossibleError(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.CommandError.getMessage()"""
        return str.__wrap(super(CommandError, self).getMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def send(self, arg0: 'CommandSender', arg1: 'CommandData'):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.send(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.CommandData)"""
        super(__CommandError, self).send(arg0, arg1)

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
    def addIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.addIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).addIndex(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setOnlyOverloads(self, arg0: bool):
        """public void dev.ultreon.quantum.api.commands.error.CommandError.setOnlyOverloads(boolean)"""
        super(__CommandError, self).setOnlyOverloads(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.api.commands.error.ImpossibleError.getName()"""
        return str.__wrap(super(ImpossibleError, self).getName())

    @override
    @overload
    def getIndex(self) -> int:
        """public int dev.ultreon.quantum.api.commands.error.CommandError.getIndex()"""
        return int.__wrap(super(CommandError, self).getIndex())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIndex(self, arg0: int) -> 'CommandError':
        """public dev.ultreon.quantum.api.commands.error.CommandError dev.ultreon.quantum.api.commands.error.CommandError.setIndex(int)"""
        return 'CommandError'.__wrap(super(__CommandError, self).setIndex(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getMessageCode(self) -> 'commands.MessageCode':
        """public dev.ultreon.quantum.api.commands.MessageCode dev.ultreon.quantum.api.commands.error.CommandError.getMessageCode()"""
        return 'commands.MessageCode'.__wrap(super(CommandError, self).getMessageCode())