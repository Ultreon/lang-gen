from __future__ import annotations
from overload import overload


 
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

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.server.chat.Chat as _Chat
_Chat = _Chat
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Chat():
    """dev.ultreon.quantum.server.chat.Chat"""
 
    @staticmethod
    def _wrap(java_value: _Chat) -> 'Chat':
        return Chat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Chat):
        """
        Dynamic initializer for Chat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Chat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Chat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def sendObject(arg0: 'CommandSender', arg1: object):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendObject(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Object)"""
        _Chat.sendObject(arg0, arg1)

    @staticmethod
    @overload
    def sendError(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendError(arg0, arg1)

    @staticmethod
    @overload
    def sendSuccess(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendSuccess(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendSuccess(arg0, arg1)

    @staticmethod
    @overload
    def formatError(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatError(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.chat.Chat()"""
        val = _Chat()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sendInfo(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendInfo(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendInfo(arg0, arg1)

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
    def sendWarning(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendWarning(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendWarning(arg0, arg1)

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: 'MessageCode', arg2: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        _Chat.sendFatal(arg0, arg1, arg2)

    @staticmethod
    @overload
    def formatFatal(arg0: 'CommandSender', arg1: str, arg2: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatFatal(arg0, arg1, arg2))

    @staticmethod
    @overload
    def formatInfo(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatInfo(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatInfo(arg0, arg1))

    @staticmethod
    @overload
    def formatDenied(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatDenied(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatDenied(arg0, arg1))

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendFatal(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def formatWarning(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatWarning(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatWarning(arg0, arg1))

    @staticmethod
    @overload
    def sendServerMessage(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendServerMessage(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendServerMessage(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.chat.Chat()"""
        val = _Chat()
        self.__wrapper = val

    @staticmethod
    @overload
    def formatServerMessage(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatServerMessage(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatServerMessage(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def formatFatal(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatFatal(arg0, arg1))

    @staticmethod
    @overload
    def sendDenied(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendDenied(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendDenied(arg0, arg1)

    @staticmethod
    @overload
    def formatSuccess(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatSuccess(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatSuccess(arg0, arg1))

    @staticmethod
    @overload
    def sendVoidObject(arg0: 'CommandSender'):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendVoidObject(dev.ultreon.quantum.api.commands.CommandSender)"""
        _Chat.sendVoidObject(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def formatDebug(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatDebug(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatDebug(arg0, arg1))

    @staticmethod
    @overload
    def sendError(arg0: 'CommandSender', arg1: str, arg2: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        _Chat.sendError(arg0, arg1, arg2)

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
    def formatError(arg0: 'CommandSender', arg1: str, arg2: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatError(arg0, arg1, arg2))

    @staticmethod
    @overload
    def sendDebug(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendDebug(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendDebug(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.server.chat.Chat
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

try:
    from pyquantum import text
except ImportError:
    text = _import_once("pyquantum.text")

import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.server.chat.Chat as _Chat
_Chat = _Chat
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Chat():
    """dev.ultreon.quantum.server.chat.Chat"""
 
    @staticmethod
    def _wrap(java_value: _Chat) -> 'Chat':
        return Chat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Chat):
        """
        Dynamic initializer for Chat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Chat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Chat__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def sendObject(arg0: 'CommandSender', arg1: object):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendObject(dev.ultreon.quantum.api.commands.CommandSender,java.lang.Object)"""
        _Chat.sendObject(arg0, arg1)

    @staticmethod
    @overload
    def sendError(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendError(arg0, arg1)

    @staticmethod
    @overload
    def sendSuccess(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendSuccess(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendSuccess(arg0, arg1)

    @staticmethod
    @overload
    def formatError(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatError(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.server.chat.Chat()"""
        val = _Chat()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def sendInfo(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendInfo(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendInfo(arg0, arg1)

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
    def sendWarning(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendWarning(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendWarning(arg0, arg1)

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: 'MessageCode', arg2: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,dev.ultreon.quantum.api.commands.MessageCode,java.lang.String)"""
        _Chat.sendFatal(arg0, arg1, arg2)

    @staticmethod
    @overload
    def formatFatal(arg0: 'CommandSender', arg1: str, arg2: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatFatal(arg0, arg1, arg2))

    @staticmethod
    @overload
    def formatInfo(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatInfo(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatInfo(arg0, arg1))

    @staticmethod
    @overload
    def formatDenied(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatDenied(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatDenied(arg0, arg1))

    @staticmethod
    @overload
    def sendFatal(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendFatal(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def formatWarning(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatWarning(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatWarning(arg0, arg1))

    @staticmethod
    @overload
    def sendServerMessage(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendServerMessage(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendServerMessage(arg0, arg1)

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.server.chat.Chat()"""
        val = _Chat()
        self.__wrapper = val

    @staticmethod
    @overload
    def formatServerMessage(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatServerMessage(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatServerMessage(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def formatFatal(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatFatal(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatFatal(arg0, arg1))

    @staticmethod
    @overload
    def sendDenied(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendDenied(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendDenied(arg0, arg1)

    @staticmethod
    @overload
    def formatSuccess(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatSuccess(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatSuccess(arg0, arg1))

    @staticmethod
    @overload
    def sendVoidObject(arg0: 'CommandSender'):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendVoidObject(dev.ultreon.quantum.api.commands.CommandSender)"""
        _Chat.sendVoidObject(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def formatDebug(arg0: 'CommandSender', arg1: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatDebug(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatDebug(arg0, arg1))

    @staticmethod
    @overload
    def sendError(arg0: 'CommandSender', arg1: str, arg2: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        _Chat.sendError(arg0, arg1, arg2)

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
    def formatError(arg0: 'CommandSender', arg1: str, arg2: str) -> 'text.MutableText':
        """public static dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.server.chat.Chat.formatError(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String,java.lang.String)"""
        return text.MutableText._wrap(_Chat.formatError(arg0, arg1, arg2))

    @staticmethod
    @overload
    def sendDebug(arg0: 'CommandSender', arg1: str):
        """public static void dev.ultreon.quantum.server.chat.Chat.sendDebug(dev.ultreon.quantum.api.commands.CommandSender,java.lang.String)"""
        _Chat.sendDebug(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.server.chat.Chat