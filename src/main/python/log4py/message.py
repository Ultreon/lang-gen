from __future__ import annotations
from overload import overload


 
import org.apache.logging.log4j.message.FlowMessageFactory as _FlowMessageFactory
_FlowMessageFactory = _FlowMessageFactory
from builtins import object
from abc import abstractmethod, ABC
 
class FlowMessageFactory():
    """org.apache.logging.log4j.message.FlowMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _FlowMessageFactory) -> 'FlowMessageFactory':
        return FlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlowMessageFactory):
        """
        Dynamic initializer for FlowMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlowMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlowMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newExitMessage(self, message: 'EntryMessage'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def newExitMessage(self, result: object, message: 'EntryMessage'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def newEntryMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.FlowMessageFactory.newEntryMessage(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def newExitMessage(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def newEntryMessage(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.FlowMessageFactory.newEntryMessage(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def newExitMessage(self, format: str, result: object):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def newExitMessage(self, result: object, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.Message)"""
        pass

 
 
 
# CLASS: org.apache.logging.log4j.message.FlowMessageFactory
import org.apache.logging.log4j.message.FlowMessageFactory as _FlowMessageFactory
_FlowMessageFactory = _FlowMessageFactory
from builtins import object
from abc import abstractmethod, ABC
 
class FlowMessageFactory():
    """org.apache.logging.log4j.message.FlowMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _FlowMessageFactory) -> 'FlowMessageFactory':
        return FlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlowMessageFactory):
        """
        Dynamic initializer for FlowMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlowMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlowMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newExitMessage(self, message: 'EntryMessage'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def newExitMessage(self, result: object, message: 'EntryMessage'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.EntryMessage)"""
        pass

    @abstractmethod
    def newEntryMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.FlowMessageFactory.newEntryMessage(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def newExitMessage(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def newEntryMessage(self, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.FlowMessageFactory.newEntryMessage(org.apache.logging.log4j.message.Message)"""
        pass

    @abstractmethod
    def newExitMessage(self, format: str, result: object):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def newExitMessage(self, result: object, message: 'Message'):
        """public abstract org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.FlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.Message)"""
        pass

 
 
 
# CLASS: org.apache.logging.log4j.message.FlowMessageFactory 
 
 
# CLASS: org.apache.logging.log4j.message.FlowMessage
import org.apache.logging.log4j.message.FlowMessage as _FlowMessage
_FlowMessage = _FlowMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from abc import abstractmethod, ABC
 
class FlowMessage():
    """org.apache.logging.log4j.message.FlowMessage"""
 
    @staticmethod
    def _wrap(java_value: _FlowMessage) -> 'FlowMessage':
        return FlowMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlowMessage):
        """
        Dynamic initializer for FlowMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlowMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlowMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getText(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.FlowMessage.getText()"""
        pass

    @abstractmethod
    def getMessage(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FlowMessage.getMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFactory
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
from abc import abstractmethod, ABC
from builtins import object
 
class MessageFactory():
    """org.apache.logging.log4j.message.MessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _MessageFactory) -> 'MessageFactory':
        return MessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFactory):
        """
        Dynamic initializer for MessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def newMessage(self, message: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFormatMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.MessageFormatMessageFactory as _MessageFormatMessageFactory
_MessageFormatMessageFactory = _MessageFormatMessageFactory
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageFormatMessageFactory():
    """org.apache.logging.log4j.message.MessageFormatMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _MessageFormatMessageFactory) -> 'MessageFormatMessageFactory':
        return MessageFormatMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFormatMessageFactory):
        """
        Dynamic initializer for MessageFormatMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFormatMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFormatMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.MessageFormatMessageFactory()"""
        val = _MessageFormatMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.MessageFormatMessageFactory()"""
        val = _MessageFormatMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_MessageFormatMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.ReusableMessageFactory as _ReusableMessageFactory
_ReusableMessageFactory = _ReusableMessageFactory
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReusableMessageFactory():
    """org.apache.logging.log4j.message.ReusableMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _ReusableMessageFactory) -> 'ReusableMessageFactory':
        return ReusableMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReusableMessageFactory):
        """
        Dynamic initializer for ReusableMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReusableMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReusableMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1))

    @staticmethod
    @overload
    def release(message: 'Message'):
        """public static void org.apache.logging.log4j.message.ReusableMessageFactory.release(org.apache.logging.log4j.message.Message)"""
        _ReusableMessageFactory.release(message)

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableMessageFactory()"""
        val = _ReusableMessageFactory()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, charSequence: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(charSequence))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableMessageFactory()"""
        val = _ReusableMessageFactory()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, params))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_ReusableMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StringFormattedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import org.apache.logging.log4j.message.StringFormattedMessage as _StringFormattedMessage
_StringFormattedMessage = _StringFormattedMessage
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringFormattedMessage():
    """org.apache.logging.log4j.message.StringFormattedMessage"""
 
    @staticmethod
    def _wrap(java_value: _StringFormattedMessage) -> 'StringFormattedMessage':
        return StringFormattedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringFormattedMessage):
        """
        Dynamic initializer for StringFormattedMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringFormattedMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringFormattedMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.StringFormattedMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = _StringFormattedMessage(locale, messagePattern, arguments)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.StringFormattedMessage.getThrowable()"""
        return 'Throwable'._wrap(super(StringFormattedMessage, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.StringFormattedMessage(java.lang.String,java.lang.Object...)"""
        val = _StringFormattedMessage(messagePattern, arguments)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.toString()"""
        return str._wrap(super(StringFormattedMessage, self).toString())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.StringFormattedMessage.getParameters()"""
        return List[object]._wrap(super(StringFormattedMessage, self).getParameters())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.StringFormattedMessage.hashCode()"""
        return int._wrap(super(StringFormattedMessage, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.getFormattedMessage()"""
        return str._wrap(super(StringFormattedMessage, self).getFormattedMessage())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.StringFormattedMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_StringFormattedMessage, self).equals(o))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.getFormat()"""
        return str._wrap(super(StringFormattedMessage, self).getFormat()) 
 
 
# CLASS: org.apache.logging.log4j.message.ThreadDumpMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.ThreadDumpMessage as _ThreadDumpMessage
_ThreadDumpMessage = _ThreadDumpMessage
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ThreadDumpMessage():
    """org.apache.logging.log4j.message.ThreadDumpMessage"""
 
    @staticmethod
    def _wrap(java_value: _ThreadDumpMessage) -> 'ThreadDumpMessage':
        return ThreadDumpMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadDumpMessage):
        """
        Dynamic initializer for ThreadDumpMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadDumpMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadDumpMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def formatTo(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ThreadDumpMessage.formatTo(java.lang.StringBuilder)"""
        super(_ThreadDumpMessage, self).formatTo(sb)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.toString()"""
        return str._wrap(super(ThreadDumpMessage, self).toString())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ThreadDumpMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ThreadDumpMessage, self).getThrowable())

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
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.getFormat()"""
        return str._wrap(super(ThreadDumpMessage, self).getFormat())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.getFormattedMessage()"""
        return str._wrap(super(ThreadDumpMessage, self).getFormattedMessage())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ThreadDumpMessage.getParameters()"""
        return List[object]._wrap(super(ThreadDumpMessage, self).getParameters())

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
    def __init__(self, title: str):
        """public org.apache.logging.log4j.message.ThreadDumpMessage(java.lang.String)"""
        val = _ThreadDumpMessage(title)
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
 
 
# CLASS: org.apache.logging.log4j.message.ExitMessage
import org.apache.logging.log4j.message.FlowMessage as _FlowMessage
_FlowMessage = _FlowMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.ExitMessage as _ExitMessage
_ExitMessage = _ExitMessage
from abc import abstractmethod, ABC
 
class ExitMessage():
    """org.apache.logging.log4j.message.ExitMessage"""
 
    @staticmethod
    def _wrap(java_value: _ExitMessage) -> 'ExitMessage':
        return ExitMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ExitMessage):
        """
        Dynamic initializer for ExitMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ExitMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ExitMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getText(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.FlowMessage.getText()"""
        pass

    @abstractmethod
    def getMessage(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FlowMessage.getMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.LocalizedMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.ResourceBundle as ResourceBundle
import java.util.ResourceBundle as _ResourceBundle
_ResourceBundle = _ResourceBundle
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.message.LocalizedMessageFactory as _LocalizedMessageFactory
_LocalizedMessageFactory = _LocalizedMessageFactory
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LocalizedMessageFactory():
    """org.apache.logging.log4j.message.LocalizedMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _LocalizedMessageFactory) -> 'LocalizedMessageFactory':
        return LocalizedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LocalizedMessageFactory):
        """
        Dynamic initializer for LocalizedMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LocalizedMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LocalizedMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, key: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.LocalizedMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_LocalizedMessageFactory, self).newMessage(key))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getResourceBundle(self) -> 'ResourceBundle':
        """public java.util.ResourceBundle org.apache.logging.log4j.message.LocalizedMessageFactory.getResourceBundle()"""
        return 'ResourceBundle'._wrap(super(LocalizedMessageFactory, self).getResourceBundle())

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, key: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.LocalizedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_LocalizedMessageFactory, self).newMessage(key, params))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getBaseName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessageFactory.getBaseName()"""
        return str._wrap(super(LocalizedMessageFactory, self).getBaseName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, baseName: str):
        """public org.apache.logging.log4j.message.LocalizedMessageFactory(java.lang.String)"""
        val = _LocalizedMessageFactory(baseName)
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, resourceBundle: 'ResourceBundle'):
        """public org.apache.logging.log4j.message.LocalizedMessageFactory(java.util.ResourceBundle)"""
        val = _LocalizedMessageFactory(resourceBundle)
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableObjectMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.ReusableObjectMessage as _ReusableObjectMessage
_ReusableObjectMessage = _ReusableObjectMessage
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReusableObjectMessage():
    """org.apache.logging.log4j.message.ReusableObjectMessage"""
 
    @staticmethod
    def _wrap(java_value: _ReusableObjectMessage) -> 'ReusableObjectMessage':
        return ReusableObjectMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReusableObjectMessage):
        """
        Dynamic initializer for ReusableObjectMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReusableObjectMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReusableObjectMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.clear()"""
        super(ReusableObjectMessage, self).clear()

    @overload
    def set(self, object: object):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.set(java.lang.Object)"""
        super(_ReusableObjectMessage, self).set(object)

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableObjectMessage.memento()"""
        return 'Message'._wrap(super(ReusableObjectMessage, self).memento())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableObjectMessage()"""
        val = _ReusableObjectMessage()
        self.__wrapper = val

    @override
    @overload
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableObjectMessage.getParameterCount()"""
        return int._wrap(super(ReusableObjectMessage, self).getParameterCount())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableObjectMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ReusableObjectMessage, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.getFormattedMessage()"""
        return str._wrap(super(ReusableObjectMessage, self).getFormattedMessage())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableObjectMessage.getParameters()"""
        return List[object]._wrap(super(ReusableObjectMessage, self).getParameters())

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
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.toString()"""
        return str._wrap(super(ReusableObjectMessage, self).toString())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.formatTo(java.lang.StringBuilder)"""
        super(_ReusableObjectMessage, self).formatTo(buffer)

    @overload
    def getParameter(self) -> object:
        """public java.lang.Object org.apache.logging.log4j.message.ReusableObjectMessage.getParameter()"""
        return object._wrap(super(ReusableObjectMessage, self).getParameter())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableObjectMessage()"""
        val = _ReusableObjectMessage()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableObjectMessage.swapParameters(java.lang.Object[])"""
        return List[object]._wrap(super(_ReusableObjectMessage, self).swapParameters(emptyReplacement))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableObjectMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(_ReusableObjectMessage, self).forEachParameter(action, state)

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.getFormat()"""
        return str._wrap(super(ReusableObjectMessage, self).getFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableSimpleMessage
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.message.ReusableSimpleMessage as _ReusableSimpleMessage
_ReusableSimpleMessage = _ReusableSimpleMessage
from typing import List
import java.lang.String as _string
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReusableSimpleMessage():
    """org.apache.logging.log4j.message.ReusableSimpleMessage"""
 
    @staticmethod
    def _wrap(java_value: _ReusableSimpleMessage) -> 'ReusableSimpleMessage':
        return ReusableSimpleMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReusableSimpleMessage):
        """
        Dynamic initializer for ReusableSimpleMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReusableSimpleMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReusableSimpleMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableSimpleMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(_ReusableSimpleMessage, self).forEachParameter(action, state)

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
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableSimpleMessage.getParameterCount()"""
        return int._wrap(super(ReusableSimpleMessage, self).getParameterCount())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'._wrap(super(CharSequence, self).codePoints())

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableSimpleMessage.memento()"""
        return 'Message'._wrap(super(ReusableSimpleMessage, self).memento())

    @overload
    def set(self, message: str):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.set(java.lang.String)"""
        super(_ReusableSimpleMessage, self).set(message)

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableSimpleMessage.getFormat()"""
        return str._wrap(super(ReusableSimpleMessage, self).getFormat())

    @overload
    def set(self, charSequence: 'CharSequence'):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.set(java.lang.CharSequence)"""
        super(_ReusableSimpleMessage, self).set(charSequence)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def charAt(self, index: int) -> str:
        """public char org.apache.logging.log4j.message.ReusableSimpleMessage.charAt(int)"""
        return str._wrap(super(_ReusableSimpleMessage, self).charAt(_int.valueOf(index)))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.logging.log4j.message.ReusableSimpleMessage.length()"""
        return int._wrap(super(ReusableSimpleMessage, self).length())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableSimpleMessage.swapParameters(java.lang.Object[])"""
        return List[object]._wrap(super(_ReusableSimpleMessage, self).swapParameters(emptyReplacement))

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'._wrap(super(CharSequence, self).chars())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableSimpleMessage.getFormattedMessage()"""
        return str._wrap(super(ReusableSimpleMessage, self).getFormattedMessage())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableSimpleMessage.getParameters()"""
        return List[object]._wrap(super(ReusableSimpleMessage, self).getParameters())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableSimpleMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ReusableSimpleMessage, self).getThrowable())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableSimpleMessage()"""
        val = _ReusableSimpleMessage()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableSimpleMessage()"""
        val = _ReusableSimpleMessage()
        self.__wrapper = val

    @override
    @overload
    def isEmpty(self) -> bool:
        """public default boolean java.lang.CharSequence.isEmpty()"""
        return bool._wrap(super(CharSequence, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.formatTo(java.lang.StringBuilder)"""
        super(_ReusableSimpleMessage, self).formatTo(buffer)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def subSequence(self, start: int, end: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.message.ReusableSimpleMessage.subSequence(int,int)"""
        return 'CharSequence'._wrap(super(_ReusableSimpleMessage, self).subSequence(_int.valueOf(start), _int.valueOf(end)))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.clear()"""
        super(ReusableSimpleMessage, self).clear()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StringFormatterMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.message.StringFormatterMessageFactory as _StringFormatterMessageFactory
_StringFormatterMessageFactory = _StringFormatterMessageFactory
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringFormatterMessageFactory():
    """org.apache.logging.log4j.message.StringFormatterMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _StringFormatterMessageFactory) -> 'StringFormatterMessageFactory':
        return StringFormatterMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringFormatterMessageFactory):
        """
        Dynamic initializer for StringFormatterMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringFormatterMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringFormatterMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.StringFormatterMessageFactory()"""
        val = _StringFormatterMessageFactory()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, params))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.StringFormatterMessageFactory()"""
        val = _StringFormatterMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.LoggerNameAwareMessage
import org.apache.logging.log4j.message.LoggerNameAwareMessage as _LoggerNameAwareMessage
_LoggerNameAwareMessage = _LoggerNameAwareMessage
from abc import abstractmethod, ABC
 
class LoggerNameAwareMessage():
    """org.apache.logging.log4j.message.LoggerNameAwareMessage"""
 
    @staticmethod
    def _wrap(java_value: _LoggerNameAwareMessage) -> 'LoggerNameAwareMessage':
        return LoggerNameAwareMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoggerNameAwareMessage):
        """
        Dynamic initializer for LoggerNameAwareMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoggerNameAwareMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoggerNameAwareMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getLoggerName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.LoggerNameAwareMessage.getLoggerName()"""
        pass

    @abstractmethod
    def setLoggerName(self, name: str):
        """public abstract void org.apache.logging.log4j.message.LoggerNameAwareMessage.setLoggerName(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterVisitable
import org.apache.logging.log4j.message.ParameterVisitable as _ParameterVisitable
_ParameterVisitable = _ParameterVisitable
from abc import abstractmethod, ABC
 
class ParameterVisitable():
    """org.apache.logging.log4j.message.ParameterVisitable"""
 
    @staticmethod
    def _wrap(java_value: _ParameterVisitable) -> 'ParameterVisitable':
        return ParameterVisitable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterVisitable):
        """
        Dynamic initializer for ParameterVisitable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterVisitable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterVisitable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public abstract <S> void org.apache.logging.log4j.message.ParameterVisitable.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.FormattedMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.FormattedMessageFactory as _FormattedMessageFactory
_FormattedMessageFactory = _FormattedMessageFactory
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormattedMessageFactory():
    """org.apache.logging.log4j.message.FormattedMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _FormattedMessageFactory) -> 'FormattedMessageFactory':
        return FormattedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattedMessageFactory):
        """
        Dynamic initializer for FormattedMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattedMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattedMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.FormattedMessageFactory()"""
        val = _FormattedMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.FormattedMessageFactory()"""
        val = _FormattedMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, params))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_FormattedMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StringMapMessage
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.message.MapMessage as _MapMessage
_MapMessage = _MapMessage
import org.apache.logging.log4j.message.StringMapMessage as _StringMapMessage
_StringMapMessage = _StringMapMessage
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as _IndexedReadOnlyStringMap
_IndexedReadOnlyStringMap = _IndexedReadOnlyStringMap
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringMapMessage():
    """org.apache.logging.log4j.message.StringMapMessage"""
 
    @staticmethod
    def _wrap(java_value: _StringMapMessage) -> 'StringMapMessage':
        return StringMapMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringMapMessage):
        """
        Dynamic initializer for StringMapMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringMapMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringMapMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.toString()"""
        return str._wrap(super(MapMessage, self).toString())

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _float.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _int.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _boolean.valueOf(value)))

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).remove(key))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.MapMessage.hashCode()"""
        return int._wrap(super(MapMessage, self).hashCode())

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _double.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(_MapMessage, self).formatTo(formats, buffer)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormat()"""
        return str._wrap(super(MapMessage, self).getFormat())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object]._wrap(super(MapMessage, self).getParameters())

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(_MapMessage, self).forEach(action, state)

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
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(_MapMessage, self).asXml(sb)

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage()"""
        return str._wrap(super(MapMessage, self).getFormattedMessage())

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _char.valueOf(value)))

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.message.StringMapMessage(int)"""
        val = _StringMapMessage(_int.valueOf(initialCapacity))
        self.__wrapper = val

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_MapMessage, self).putAll(map)

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(_MapMessage, self).forEach(action)

    @override
    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'._wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @override
    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(_MapMessage, self).put(candidateKey, value)

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'._wrap(super(MapMessage, self).getThrowable())

    @override
    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString()"""
        return str._wrap(super(MapMessage, self).asString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.message.StringMapMessage(java.util.Map<java.lang.String, java.lang.String>)"""
        val = _StringMapMessage(map)
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _byte.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _long.valueOf(value)))

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool._wrap(super(_MapMessage, self).containsKey(key))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.StringBuilder)"""
        super(_MapMessage, self).formatTo(buffer)

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage(java.lang.String[])"""
        return str._wrap(super(_MapMessage, self).getFormattedMessage(formats))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.StringMapMessage()"""
        val = _StringMapMessage()
        self.__wrapper = val

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).asString(format))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_MapMessage, self).equals(o))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _short.valueOf(value)))

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).get(key))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.StringMapMessage()"""
        val = _StringMapMessage()
        self.__wrapper = val

    @overload
    def newInstance(self, map: 'Map') -> 'StringMapMessage':
        """public org.apache.logging.log4j.message.StringMapMessage org.apache.logging.log4j.message.StringMapMessage.newInstance(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'StringMapMessage'._wrap(super(_StringMapMessage, self).newInstance(map))

    @override
    @overload
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.MapMessage.getFormats()"""
        return List[str]._wrap(super(MapMessage, self).getFormats())

    @override
    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'._wrap(super(MapMessage, self).getData()) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableParameterizedMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Integer as _int
import org.apache.logging.log4j.message.ReusableParameterizedMessage as _ReusableParameterizedMessage
_ReusableParameterizedMessage = _ReusableParameterizedMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReusableParameterizedMessage():
    """org.apache.logging.log4j.message.ReusableParameterizedMessage"""
 
    @staticmethod
    def _wrap(java_value: _ReusableParameterizedMessage) -> 'ReusableParameterizedMessage':
        return ReusableParameterizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReusableParameterizedMessage):
        """
        Dynamic initializer for ReusableParameterizedMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReusableParameterizedMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReusableParameterizedMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.toString()"""
        return str._wrap(super(ReusableParameterizedMessage, self).toString())

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableParameterizedMessage.swapParameters(java.lang.Object[])"""
        return List[object]._wrap(super(_ReusableParameterizedMessage, self).swapParameters(emptyReplacement))

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableParameterizedMessage.getParameters()"""
        return List[object]._wrap(super(ReusableParameterizedMessage, self).getParameters())

    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableParameterizedMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(_ReusableParameterizedMessage, self).forEachParameter(action, state)

    @override
    @overload
    def formatTo(self, builder: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableParameterizedMessage.formatTo(java.lang.StringBuilder)"""
        super(_ReusableParameterizedMessage, self).formatTo(builder)

    @override
    @overload
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableParameterizedMessage.getParameterCount()"""
        return int._wrap(super(ReusableParameterizedMessage, self).getParameterCount())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableParameterizedMessage.memento()"""
        return 'Message'._wrap(super(ReusableParameterizedMessage, self).memento())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableParameterizedMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ReusableParameterizedMessage, self).getThrowable())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.getFormattedMessage()"""
        return str._wrap(super(ReusableParameterizedMessage, self).getFormattedMessage())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableParameterizedMessage.clear()"""
        super(ReusableParameterizedMessage, self).clear()

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
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableParameterizedMessage()"""
        val = _ReusableParameterizedMessage()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableParameterizedMessage()"""
        val = _ReusableParameterizedMessage()
        self.__wrapper = val

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.getFormat()"""
        return str._wrap(super(ReusableParameterizedMessage, self).getFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.ObjectMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import org.apache.logging.log4j.message.ObjectMessage as _ObjectMessage
_ObjectMessage = _ObjectMessage
from typing import List
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectMessage():
    """org.apache.logging.log4j.message.ObjectMessage"""
 
    @staticmethod
    def _wrap(java_value: _ObjectMessage) -> 'ObjectMessage':
        return ObjectMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectMessage):
        """
        Dynamic initializer for ObjectMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ObjectMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_ObjectMessage, self).equals(o))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.toString()"""
        return str._wrap(super(ObjectMessage, self).toString())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.getFormattedMessage()"""
        return str._wrap(super(ObjectMessage, self).getFormattedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ObjectMessage.hashCode()"""
        return int._wrap(super(ObjectMessage, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, obj: object):
        """public org.apache.logging.log4j.message.ObjectMessage(java.lang.Object)"""
        val = _ObjectMessage(obj)
        self.__wrapper = val

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ObjectMessage.formatTo(java.lang.StringBuilder)"""
        super(_ObjectMessage, self).formatTo(buffer)

    @overload
    def getParameter(self) -> object:
        """public java.lang.Object org.apache.logging.log4j.message.ObjectMessage.getParameter()"""
        return object._wrap(super(ObjectMessage, self).getParameter())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ObjectMessage.getParameters()"""
        return List[object]._wrap(super(ObjectMessage, self).getParameters())

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
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.getFormat()"""
        return str._wrap(super(ObjectMessage, self).getFormat())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ObjectMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ObjectMessage, self).getThrowable())

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
 
 
# CLASS: org.apache.logging.log4j.message.MessageFactory2
import java.lang.CharSequence as CharSequence
import org.apache.logging.log4j.message.MessageFactory2 as _MessageFactory2
_MessageFactory2 = _MessageFactory2
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
from abc import abstractmethod, ABC
from builtins import object
 
class MessageFactory2():
    """org.apache.logging.log4j.message.MessageFactory2"""
 
    @staticmethod
    def _wrap(java_value: _MessageFactory2) -> 'MessageFactory2':
        return MessageFactory2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFactory2):
        """
        Dynamic initializer for MessageFactory2.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFactory2__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFactory2__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newMessage(self, charSequence: 'CharSequence'):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.CharSequence)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass

    @abstractmethod
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory2.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.Message
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from abc import abstractmethod, ABC
 
class Message():
    """org.apache.logging.log4j.message.Message"""
 
    @staticmethod
    def _wrap(java_value: _Message) -> 'Message':
        return Message(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Message):
        """
        Dynamic initializer for Message.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Message__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Message__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.LocalizedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.ResourceBundle as ResourceBundle
import org.apache.logging.log4j.message.LocalizedMessage as _LocalizedMessage
_LocalizedMessage = _LocalizedMessage
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LocalizedMessage():
    """org.apache.logging.log4j.message.LocalizedMessage"""
 
    @staticmethod
    def _wrap(java_value: _LocalizedMessage) -> 'LocalizedMessage':
        return LocalizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LocalizedMessage):
        """
        Dynamic initializer for LocalizedMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LocalizedMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LocalizedMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getFormat()"""
        return str._wrap(super(LocalizedMessage, self).getFormat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(messagePattern, arg)
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(locale, key, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.LocalizedMessage.getParameters()"""
        return List[object]._wrap(super(LocalizedMessage, self).getParameters())

    @overload
    def __init__(self, messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(messagePattern, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.LocalizedMessage.getThrowable()"""
        return 'Throwable'._wrap(super(LocalizedMessage, self).getThrowable())

    @overload
    def __init__(self, messagePattern: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(messagePattern, arguments)
        self.__wrapper = val

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getLoggerName()"""
        return str._wrap(super(LocalizedMessage, self).getLoggerName())

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
    def __init__(self, baseName: str, key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(baseName, key, arguments)
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String)"""
        val = _LocalizedMessage(bundle, key)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.toString()"""
        return str._wrap(super(LocalizedMessage, self).toString())

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(bundle, locale, key, arguments)
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(bundle, locale, key, arg)
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(baseName, key, arg)
        self.__wrapper = val

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getFormattedMessage()"""
        return str._wrap(super(LocalizedMessage, self).getFormattedMessage())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(bundle, locale, key, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(locale, key, arg)
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(baseName, locale, key, arguments)
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(bundle, key, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(baseName, locale, key, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, baseName: str, locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(baseName, locale, key, arg)
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _LocalizedMessage(baseName, key, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(locale, key, arguments)
        self.__wrapper = val

    @override
    @overload
    def setLoggerName(self, name: str):
        """public void org.apache.logging.log4j.message.LocalizedMessage.setLoggerName(java.lang.String)"""
        super(_LocalizedMessage, self).setLoggerName(name)

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
    def __init__(self, bundle: 'ResourceBundle', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object)"""
        val = _LocalizedMessage(bundle, key, arg)
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object[])"""
        val = _LocalizedMessage(bundle, key, arguments)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.AsynchronouslyFormattable
import org.apache.logging.log4j.message.AsynchronouslyFormattable as _AsynchronouslyFormattable
_AsynchronouslyFormattable = _AsynchronouslyFormattable
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class AsynchronouslyFormattable():
    """org.apache.logging.log4j.message.AsynchronouslyFormattable"""
 
    @staticmethod
    def _wrap(java_value: _AsynchronouslyFormattable) -> 'AsynchronouslyFormattable':
        return AsynchronouslyFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsynchronouslyFormattable):
        """
        Dynamic initializer for AsynchronouslyFormattable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsynchronouslyFormattable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsynchronouslyFormattable__wrapper":
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
 
 
# CLASS: org.apache.logging.log4j.message.MapMessage$MapFormat
from builtins import str
import org.apache.logging.log4j.message.MapMessage as _MapMessage_MapFormat
_MapFormat = _MapMessage_MapFormat.MapFormat
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
 
class MapFormat():
    """org.apache.logging.log4j.message.MapMessage.MapFormat"""
 
    @staticmethod
    def _wrap(java_value: _MapFormat) -> 'MapFormat':
        return MapFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapFormat):
        """
        Dynamic initializer for MapFormat.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapFormat__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapFormat__wrapper":
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

    @staticmethod
    @overload
    def names() -> List[str]:
        """public static java.lang.String[] org.apache.logging.log4j.message.MapMessage$MapFormat.names()"""
        return List[str]._wrap(_MapFormat.names())

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
    def values() -> List['MapFormat']:
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat[] org.apache.logging.log4j.message.MapMessage$MapFormat.values()"""
        return List[MapFormat]._wrap(_MapFormat.values())

    @staticmethod
    @overload
    def valueOf(name: str) -> 'MapFormat':
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat org.apache.logging.log4j.message.MapMessage$MapFormat.valueOf(java.lang.String)"""
        return MapFormat._wrap(_MapFormat.valueOf(name))

    @staticmethod
    @overload
    def lookupIgnoreCase(format: str) -> 'MapFormat':
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat org.apache.logging.log4j.message.MapMessage$MapFormat.lookupIgnoreCase(java.lang.String)"""
        return MapFormat._wrap(_MapFormat.lookupIgnoreCase(format))

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
 
 
# CLASS: org.apache.logging.log4j.message.MapMessage
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.message.MapMessage as _MapMessage
_MapMessage = _MapMessage
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as _IndexedReadOnlyStringMap
_IndexedReadOnlyStringMap = _IndexedReadOnlyStringMap
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MapMessage():
    """org.apache.logging.log4j.message.MapMessage"""
 
    @staticmethod
    def _wrap(java_value: _MapMessage) -> 'MapMessage':
        return MapMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MapMessage):
        """
        Dynamic initializer for MapMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MapMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MapMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.toString()"""
        return str._wrap(super(MapMessage, self).toString())

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _float.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _int.valueOf(value)))

    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(_MapMessage, self).forEach(action, state)

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.message.MapMessage(int)"""
        val = _MapMessage(_int.valueOf(initialCapacity))
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_MapMessage, self).putAll(map)

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _boolean.valueOf(value)))

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).remove(key))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.MapMessage.hashCode()"""
        return int._wrap(super(MapMessage, self).hashCode())

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _double.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(_MapMessage, self).formatTo(formats, buffer)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.MapMessage()"""
        val = _MapMessage()
        self.__wrapper = val

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormat()"""
        return str._wrap(super(MapMessage, self).getFormat())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object]._wrap(super(MapMessage, self).getParameters())

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
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage()"""
        return str._wrap(super(MapMessage, self).getFormattedMessage())

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.message.MapMessage(java.util.Map<java.lang.String, V>)"""
        val = _MapMessage(map)
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _char.valueOf(value)))

    @overload
    def newInstance(self, map: 'Map') -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.newInstance(java.util.Map<java.lang.String, V>)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).newInstance(map))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'._wrap(super(MapMessage, self).getThrowable())

    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'._wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _byte.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _long.valueOf(value)))

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'._wrap(super(MapMessage, self).getData())

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool._wrap(super(_MapMessage, self).containsKey(key))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.StringBuilder)"""
        super(_MapMessage, self).formatTo(buffer)

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage(java.lang.String[])"""
        return str._wrap(super(_MapMessage, self).getFormattedMessage(formats))

    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(_MapMessage, self).put(candidateKey, value)

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).asString(format))

    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString()"""
        return str._wrap(super(MapMessage, self).asString())

    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(_MapMessage, self).forEach(action)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_MapMessage, self).equals(o))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _short.valueOf(value)))

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).get(key))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(_MapMessage, self).asXml(sb)

    @override
    @overload
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.MapMessage.getFormats()"""
        return List[str]._wrap(super(MapMessage, self).getFormats())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.MapMessage()"""
        val = _MapMessage()
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.EntryMessage
import org.apache.logging.log4j.message.FlowMessage as _FlowMessage
_FlowMessage = _FlowMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.EntryMessage as _EntryMessage
_EntryMessage = _EntryMessage
 
class EntryMessage():
    """org.apache.logging.log4j.message.EntryMessage"""
 
    @staticmethod
    def _wrap(java_value: _EntryMessage) -> 'EntryMessage':
        return EntryMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntryMessage):
        """
        Dynamic initializer for EntryMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntryMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntryMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getText(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.FlowMessage.getText()"""
        pass

    @abstractmethod
    def getMessage(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FlowMessage.getMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ThreadDumpMessage$ThreadInfoFactory
import org.apache.logging.log4j.message.ThreadDumpMessage as _ThreadDumpMessage_ThreadInfoFactory
_ThreadInfoFactory = _ThreadDumpMessage_ThreadInfoFactory.ThreadInfoFactory
from abc import abstractmethod, ABC
 
class ThreadInfoFactory():
    """org.apache.logging.log4j.message.ThreadDumpMessage.ThreadInfoFactory"""
 
    @staticmethod
    def _wrap(java_value: _ThreadInfoFactory) -> 'ThreadInfoFactory':
        return ThreadInfoFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadInfoFactory):
        """
        Dynamic initializer for ThreadInfoFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadInfoFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadInfoFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def createThreadInfo(self, ):
        """public abstract java.util.Map<org.apache.logging.log4j.message.ThreadInformation, java.lang.StackTraceElement[]> org.apache.logging.log4j.message.ThreadDumpMessage$ThreadInfoFactory.createThreadInfo()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.AbstractMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as _MessageFactory
_MessageFactory = _MessageFactory
import java.lang.String as _String
_String = _String
from builtins import object
from abc import abstractmethod, ABC
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractMessageFactory():
    """org.apache.logging.log4j.message.AbstractMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _AbstractMessageFactory) -> 'AbstractMessageFactory':
        return AbstractMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractMessageFactory):
        """
        Dynamic initializer for AbstractMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.AbstractMessageFactory()"""
        val = _AbstractMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.AbstractMessageFactory()"""
        val = _AbstractMessageFactory()
        self.__wrapper = val

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def newMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.MessageCollectionMessage
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.MessageCollectionMessage as _MessageCollectionMessage
_MessageCollectionMessage = _MessageCollectionMessage
import java.util.function.Consumer as Consumer
 
class MessageCollectionMessage():
    """org.apache.logging.log4j.message.MessageCollectionMessage"""
 
    @staticmethod
    def _wrap(java_value: _MessageCollectionMessage) -> 'MessageCollectionMessage':
        return MessageCollectionMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageCollectionMessage):
        """
        Dynamic initializer for MessageCollectionMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageCollectionMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageCollectionMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<T> java.lang.Iterable.iterator()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableMessage
import org.apache.logging.log4j.util.StringBuilderFormattable as _StringBuilderFormattable
_StringBuilderFormattable = _StringBuilderFormattable
import org.apache.logging.log4j.message.ReusableMessage as _ReusableMessage
_ReusableMessage = _ReusableMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
from builtins import object
 
class ReusableMessage():
    """org.apache.logging.log4j.message.ReusableMessage"""
 
    @staticmethod
    def _wrap(java_value: _ReusableMessage) -> 'ReusableMessage':
        return ReusableMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReusableMessage):
        """
        Dynamic initializer for ReusableMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReusableMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReusableMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def memento(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessage.memento()"""
        pass

    @abstractmethod
    def getParameterCount(self, ):
        """public abstract short org.apache.logging.log4j.message.ReusableMessage.getParameterCount()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def formatTo(self, buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.StringBuilderFormattable.formatTo(java.lang.StringBuilder)"""
        pass

    @abstractmethod
    def swapParameters(self, emptyReplacement: 'Object'):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.ReusableMessage.swapParameters(java.lang.Object[])"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataId
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
import org.apache.logging.log4j.message.StructuredDataId as _StructuredDataId
_StructuredDataId = _StructuredDataId
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StructuredDataId():
    """org.apache.logging.log4j.message.StructuredDataId"""
 
    @staticmethod
    def _wrap(java_value: _StructuredDataId) -> 'StructuredDataId':
        return StructuredDataId(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StructuredDataId):
        """
        Dynamic initializer for StructuredDataId.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StructuredDataId__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StructuredDataId__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.toString()"""
        return str._wrap(super(StructuredDataId, self).toString())

    @overload
    def getRequired(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataId.getRequired()"""
        return List[str]._wrap(super(StructuredDataId, self).getRequired())

    @overload
    def __init__(self, name: str, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String[],java.lang.String[])"""
        val = _StructuredDataId(name, required, optional)
        self.__wrapper = val

    @overload
    def __init__(self, name: str, enterpriseNumber: str, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String,java.lang.String[],java.lang.String[],int)"""
        val = _StructuredDataId(name, enterpriseNumber, required, optional, _int.valueOf(maxLength))
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, name: str, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String[],java.lang.String[],int)"""
        val = _StructuredDataId(name, required, optional, _int.valueOf(maxLength))
        self.__wrapper = val

    @overload
    def __init__(self, name: str, enterpriseNumber: int, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int,java.lang.String[],java.lang.String[],int)"""
        val = _StructuredDataId(name, _int.valueOf(enterpriseNumber), required, optional, _int.valueOf(maxLength))
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
    def getOptional(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataId.getOptional()"""
        return List[str]._wrap(super(StructuredDataId, self).getOptional())

    @overload
    def __init__(self, name: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int)"""
        val = _StructuredDataId(name, _int.valueOf(maxLength))
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.getName()"""
        return str._wrap(super(StructuredDataId, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def makeId(self, id: 'StructuredDataId') -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(org.apache.logging.log4j.message.StructuredDataId)"""
        return 'StructuredDataId'._wrap(super(_StructuredDataId, self).makeId(id))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataId.formatTo(java.lang.StringBuilder)"""
        super(_StructuredDataId, self).formatTo(buffer)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getEnterpriseNumber(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.getEnterpriseNumber()"""
        return str._wrap(super(StructuredDataId, self).getEnterpriseNumber())

    @overload
    def makeId(self, defaultId: str, anEnterpriseNumber: int) -> 'StructuredDataId':
        """public final org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(java.lang.String,int)"""
        return 'StructuredDataId'._wrap(super(_StructuredDataId, self).makeId(defaultId, _int.valueOf(anEnterpriseNumber)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, name: str, enterpriseNumber: str, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String,java.lang.String[],java.lang.String[])"""
        val = _StructuredDataId(name, enterpriseNumber, required, optional)
        self.__wrapper = val

    @overload
    def makeId(self, defaultId: str, anEnterpriseNumber: str) -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(java.lang.String,java.lang.String)"""
        return 'StructuredDataId'._wrap(super(_StructuredDataId, self).makeId(defaultId, anEnterpriseNumber))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isReserved(self) -> bool:
        """public boolean org.apache.logging.log4j.message.StructuredDataId.isReserved()"""
        return bool._wrap(super(StructuredDataId, self).isReserved())

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String)"""
        val = _StructuredDataId(name)
        self.__wrapper = val

    @overload
    def __init__(self, name: str, enterpriseNumber: int, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int,java.lang.String[],java.lang.String[])"""
        val = _StructuredDataId(name, _int.valueOf(enterpriseNumber), required, optional)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.FormattedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.FormattedMessage as _FormattedMessage
_FormattedMessage = _FormattedMessage
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FormattedMessage():
    """org.apache.logging.log4j.message.FormattedMessage"""
 
    @staticmethod
    def _wrap(java_value: _FormattedMessage) -> 'FormattedMessage':
        return FormattedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattedMessage):
        """
        Dynamic initializer for FormattedMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattedMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattedMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, messagePattern: str, arguments: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = _FormattedMessage(messagePattern, arguments, throwable)
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _FormattedMessage(locale, messagePattern, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.getFormattedMessage()"""
        return str._wrap(super(FormattedMessage, self).getFormattedMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.getFormat()"""
        return str._wrap(super(FormattedMessage, self).getFormat())

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object)"""
        val = _FormattedMessage(locale, messagePattern, arg)
        self.__wrapper = val

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.FormattedMessage.getThrowable()"""
        return 'Throwable'._wrap(super(FormattedMessage, self).getThrowable())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.FormattedMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_FormattedMessage, self).equals(o))

    @overload
    def __init__(self, messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _FormattedMessage(messagePattern, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object)"""
        val = _FormattedMessage(messagePattern, arg)
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arguments: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = _FormattedMessage(locale, messagePattern, arguments, throwable)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object...)"""
        val = _FormattedMessage(messagePattern, arguments)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.FormattedMessage.hashCode()"""
        return int._wrap(super(FormattedMessage, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.toString()"""
        return str._wrap(super(FormattedMessage, self).toString())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.FormattedMessage.getParameters()"""
        return List[object]._wrap(super(FormattedMessage, self).getParameters())

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
    def __init__(self, locale: 'Locale', messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = _FormattedMessage(locale, messagePattern, arguments)
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.ParameterizedMessage as _ParameterizedMessage
_ParameterizedMessage = _ParameterizedMessage
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParameterizedMessage():
    """org.apache.logging.log4j.message.ParameterizedMessage"""
 
    @staticmethod
    def _wrap(java_value: _ParameterizedMessage) -> 'ParameterizedMessage':
        return ParameterizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterizedMessage):
        """
        Dynamic initializer for ParameterizedMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterizedMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterizedMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def countArgumentPlaceholders(pattern: str) -> int:
        """public static int org.apache.logging.log4j.message.ParameterizedMessage.countArgumentPlaceholders(java.lang.String)"""
        return int._wrap(_ParameterizedMessage.countArgumentPlaceholders(pattern))

    @overload
    def __init__(self, pattern: str, args: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = _ParameterizedMessage(pattern, args, throwable)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, pattern: str, arg: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object)"""
        val = _ParameterizedMessage(pattern, arg)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ParameterizedMessage.hashCode()"""
        return int._wrap(super(ParameterizedMessage, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.toString()"""
        return str._wrap(super(ParameterizedMessage, self).toString())

    @staticmethod
    @overload
    def identityToString(obj: object) -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.identityToString(java.lang.Object)"""
        return str._wrap(_ParameterizedMessage.identityToString(obj))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ParameterizedMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_ParameterizedMessage, self).equals(object))

    @overload
    def __init__(self, pattern: str, *args: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object...)"""
        val = _ParameterizedMessage(pattern, args)
        self.__wrapper = val

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.getFormattedMessage()"""
        return str._wrap(super(ParameterizedMessage, self).getFormattedMessage())

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
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ParameterizedMessage.getParameters()"""
        return List[object]._wrap(super(ParameterizedMessage, self).getParameters())

    @overload
    def __init__(self, pattern: str, args: 'String', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.String[],java.lang.Throwable)"""
        val = _ParameterizedMessage(pattern, args, throwable)
        self.__wrapper = val

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ParameterizedMessage.formatTo(java.lang.StringBuilder)"""
        super(_ParameterizedMessage, self).formatTo(buffer)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.getFormat()"""
        return str._wrap(super(ParameterizedMessage, self).getFormat())

    @staticmethod
    @overload
    def deepToString(o: object) -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.deepToString(java.lang.Object)"""
        return str._wrap(_ParameterizedMessage.deepToString(o))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ParameterizedMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ParameterizedMessage, self).getThrowable())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, pattern: str, arg0: object, arg1: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = _ParameterizedMessage(pattern, arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def format(pattern: str, args: 'Object') -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.format(java.lang.String,java.lang.Object[])"""
        return str._wrap(_ParameterizedMessage.format(pattern, args)) 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterConsumer
import org.apache.logging.log4j.message.ParameterConsumer as _ParameterConsumer
_ParameterConsumer = _ParameterConsumer
from abc import abstractmethod, ABC
 
class ParameterConsumer():
    """org.apache.logging.log4j.message.ParameterConsumer"""
 
    @staticmethod
    def _wrap(java_value: _ParameterConsumer) -> 'ParameterConsumer':
        return ParameterConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterConsumer):
        """
        Dynamic initializer for ParameterConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, parameter: object, parameterIndex: int, state: object):
        """public abstract void org.apache.logging.log4j.message.ParameterConsumer.accept(java.lang.Object,int,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ThreadInformation
import org.apache.logging.log4j.message.ThreadInformation as _ThreadInformation
_ThreadInformation = _ThreadInformation
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
 
class ThreadInformation():
    """org.apache.logging.log4j.message.ThreadInformation"""
 
    @staticmethod
    def _wrap(java_value: _ThreadInformation) -> 'ThreadInformation':
        return ThreadInformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThreadInformation):
        """
        Dynamic initializer for ThreadInformation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThreadInformation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThreadInformation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def printStack(self, sb: 'StringBuilder', trace: 'StackTraceElement'):
        """public abstract void org.apache.logging.log4j.message.ThreadInformation.printStack(java.lang.StringBuilder,java.lang.StackTraceElement[])"""
        pass

    @abstractmethod
    def printThreadInfo(self, sb: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.message.ThreadInformation.printThreadInfo(java.lang.StringBuilder)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ObjectArrayMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import org.apache.logging.log4j.message.ObjectArrayMessage as _ObjectArrayMessage
_ObjectArrayMessage = _ObjectArrayMessage
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectArrayMessage():
    """org.apache.logging.log4j.message.ObjectArrayMessage"""
 
    @staticmethod
    def _wrap(java_value: _ObjectArrayMessage) -> 'ObjectArrayMessage':
        return ObjectArrayMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectArrayMessage):
        """
        Dynamic initializer for ObjectArrayMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectArrayMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectArrayMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.getFormat()"""
        return str._wrap(super(ObjectArrayMessage, self).getFormat())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ObjectArrayMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_ObjectArrayMessage, self).equals(o))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.getFormattedMessage()"""
        return str._wrap(super(ObjectArrayMessage, self).getFormattedMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.toString()"""
        return str._wrap(super(ObjectArrayMessage, self).toString())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ObjectArrayMessage.getThrowable()"""
        return 'Throwable'._wrap(super(ObjectArrayMessage, self).getThrowable())

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
    def __init__(self, *obj: object):
        """public org.apache.logging.log4j.message.ObjectArrayMessage(java.lang.Object...)"""
        val = _ObjectArrayMessage(obj)
        self.__wrapper = val

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ObjectArrayMessage.getParameters()"""
        return List[object]._wrap(super(ObjectArrayMessage, self).getParameters())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ObjectArrayMessage.hashCode()"""
        return int._wrap(super(ObjectArrayMessage, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.SimpleMessage
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.SimpleMessage as _SimpleMessage
_SimpleMessage = _SimpleMessage
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.util.stream.IntStream as _IntStream
_IntStream = _IntStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.util.stream.IntStream as IntStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleMessage():
    """org.apache.logging.log4j.message.SimpleMessage"""
 
    @staticmethod
    def _wrap(java_value: _SimpleMessage) -> 'SimpleMessage':
        return SimpleMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleMessage):
        """
        Dynamic initializer for SimpleMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def length(self) -> int:
        """public int org.apache.logging.log4j.message.SimpleMessage.length()"""
        return int._wrap(super(SimpleMessage, self).length())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.SimpleMessage.hashCode()"""
        return int._wrap(super(SimpleMessage, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'._wrap(super(CharSequence, self).chars())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.SimpleMessage.formatTo(java.lang.StringBuilder)"""
        super(_SimpleMessage, self).formatTo(buffer)

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.SimpleMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_SimpleMessage, self).equals(o))

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.getFormat()"""
        return str._wrap(super(SimpleMessage, self).getFormat())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.SimpleMessage.getParameters()"""
        return List[object]._wrap(super(SimpleMessage, self).getParameters())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.SimpleMessage()"""
        val = _SimpleMessage()
        self.__wrapper = val

    @overload
    def charAt(self, index: int) -> str:
        """public char org.apache.logging.log4j.message.SimpleMessage.charAt(int)"""
        return str._wrap(super(_SimpleMessage, self).charAt(_int.valueOf(index)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, charSequence: 'CharSequence'):
        """public org.apache.logging.log4j.message.SimpleMessage(java.lang.CharSequence)"""
        val = _SimpleMessage(charSequence)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'._wrap(super(CharSequence, self).codePoints())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public default boolean java.lang.CharSequence.isEmpty()"""
        return bool._wrap(super(CharSequence, self).isEmpty())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.SimpleMessage.getThrowable()"""
        return 'Throwable'._wrap(super(SimpleMessage, self).getThrowable())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.getFormattedMessage()"""
        return str._wrap(super(SimpleMessage, self).getFormattedMessage())

    @overload
    def __init__(self, message: str):
        """public org.apache.logging.log4j.message.SimpleMessage(java.lang.String)"""
        val = _SimpleMessage(message)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def subSequence(self, start: int, end: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.message.SimpleMessage.subSequence(int,int)"""
        return 'CharSequence'._wrap(super(_SimpleMessage, self).subSequence(_int.valueOf(start), _int.valueOf(end)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.toString()"""
        return str._wrap(super(SimpleMessage, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.SimpleMessage()"""
        val = _SimpleMessage()
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.message.ParameterizedMessageFactory as _ParameterizedMessageFactory
_ParameterizedMessageFactory = _ParameterizedMessageFactory
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParameterizedMessageFactory():
    """org.apache.logging.log4j.message.ParameterizedMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _ParameterizedMessageFactory) -> 'ParameterizedMessageFactory':
        return ParameterizedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterizedMessageFactory):
        """
        Dynamic initializer for ParameterizedMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterizedMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterizedMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ParameterizedMessageFactory()"""
        val = _ParameterizedMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, params))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ParameterizedMessageFactory()"""
        val = _ParameterizedMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFormatMessage
import org.apache.logging.log4j.message.MessageFormatMessage as _MessageFormatMessage
_MessageFormatMessage = _MessageFormatMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MessageFormatMessage():
    """org.apache.logging.log4j.message.MessageFormatMessage"""
 
    @staticmethod
    def _wrap(java_value: _MessageFormatMessage) -> 'MessageFormatMessage':
        return MessageFormatMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageFormatMessage):
        """
        Dynamic initializer for MessageFormatMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageFormatMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageFormatMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, messagePattern: str, *parameters: object):
        """public org.apache.logging.log4j.message.MessageFormatMessage(java.lang.String,java.lang.Object...)"""
        val = _MessageFormatMessage(messagePattern, parameters)
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
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MessageFormatMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_MessageFormatMessage, self).equals(o))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MessageFormatMessage.getThrowable()"""
        return 'Throwable'._wrap(super(MessageFormatMessage, self).getThrowable())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MessageFormatMessage.getParameters()"""
        return List[object]._wrap(super(MessageFormatMessage, self).getParameters())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, *parameters: object):
        """public org.apache.logging.log4j.message.MessageFormatMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = _MessageFormatMessage(locale, messagePattern, parameters)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.getFormat()"""
        return str._wrap(super(MessageFormatMessage, self).getFormat())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.getFormattedMessage()"""
        return str._wrap(super(MessageFormatMessage, self).getFormattedMessage())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.toString()"""
        return str._wrap(super(MessageFormatMessage, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.MessageFormatMessage.hashCode()"""
        return int._wrap(super(MessageFormatMessage, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataMessage
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.message.MapMessage as _MapMessage
_MapMessage = _MapMessage
import java.lang.Short as _short
import java.lang.String as _string
import org.apache.logging.log4j.message.StructuredDataId as _StructuredDataId
_StructuredDataId = _StructuredDataId
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
try:
    from log4py import util
except ImportError:
    util = _import_once("log4py.util")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as _IndexedReadOnlyStringMap
_IndexedReadOnlyStringMap = _IndexedReadOnlyStringMap
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import org.apache.logging.log4j.message.StructuredDataMessage as _StructuredDataMessage
_StructuredDataMessage = _StructuredDataMessage
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StructuredDataMessage():
    """org.apache.logging.log4j.message.StructuredDataMessage"""
 
    @staticmethod
    def _wrap(java_value: _StructuredDataMessage) -> 'StructuredDataMessage':
        return StructuredDataMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StructuredDataMessage):
        """
        Dynamic initializer for StructuredDataMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StructuredDataMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StructuredDataMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _float.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.StructuredDataMessage.hashCode()"""
        return int._wrap(super(StructuredDataMessage, self).hashCode())

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _boolean.valueOf(value)))

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).remove(key))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormattedMessage()"""
        return str._wrap(super(StructuredDataMessage, self).getFormattedMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, id: str, msg: str, type: str, data: 'Map'):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>)"""
        val = _StructuredDataMessage(id, msg, type, data)
        self.__wrapper = val

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(_MapMessage, self).forEach(action, state)

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String)"""
        val = _StructuredDataMessage(id, msg, type)
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
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(_MapMessage, self).asXml(sb)

    @override
    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'._wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @override
    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(_MapMessage, self).put(candidateKey, value)

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'._wrap(super(MapMessage, self).getThrowable())

    @overload
    def __init__(self, id: str, msg: str, type: str):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String)"""
        val = _StructuredDataMessage(id, msg, type)
        self.__wrapper = val

    @overload
    def __init__(self, id: str, msg: str, type: str, data: 'Map', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>,int)"""
        val = _StructuredDataMessage(id, msg, type, data, _int.valueOf(maxLength))
        self.__wrapper = val

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString(java.lang.String)"""
        return str._wrap(super(_StructuredDataMessage, self).asString(format))

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool._wrap(super(_MapMessage, self).containsKey(key))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @override
    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString()"""
        return str._wrap(super(StructuredDataMessage, self).asString())

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _short.valueOf(value)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, id: str, msg: str, type: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,int)"""
        val = _StructuredDataMessage(id, msg, type, _int.valueOf(maxLength))
        self.__wrapper = val

    @override
    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'._wrap(super(MapMessage, self).getData())

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _int.valueOf(value)))

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, data: 'Map'):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>)"""
        val = _StructuredDataMessage(id, msg, type, data)
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _double.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.toString()"""
        return str._wrap(super(StructuredDataMessage, self).toString())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object]._wrap(super(MapMessage, self).getParameters())

    @overload
    def newInstance(self, map: 'Map') -> 'StructuredDataMessage':
        """public org.apache.logging.log4j.message.StructuredDataMessage org.apache.logging.log4j.message.StructuredDataMessage.newInstance(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'StructuredDataMessage'._wrap(super(_StructuredDataMessage, self).newInstance(map))

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.StructuredDataMessage.equals(java.lang.Object)"""
        return bool._wrap(super(_StructuredDataMessage, self).equals(o))

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormattedMessage(java.lang.String[])"""
        return str._wrap(super(_StructuredDataMessage, self).getFormattedMessage(formats))

    @override
    @overload
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataMessage.getFormats()"""
        return List[str]._wrap(super(StructuredDataMessage, self).getFormats())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormat()"""
        return str._wrap(super(StructuredDataMessage, self).getFormat())

    @overload
    def asString(self, format: 'Format', structuredDataId: 'StructuredDataId') -> str:
        """public final java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString(org.apache.logging.log4j.message.StructuredDataMessage$Format,org.apache.logging.log4j.message.StructuredDataId)"""
        return str._wrap(super(_StructuredDataMessage, self).asString(format, structuredDataId))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _char.valueOf(value)))

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(_MapMessage, self).putAll(map)

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(_MapMessage, self).forEach(action)

    @overload
    def getId(self) -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataMessage.getId()"""
        return 'StructuredDataId'._wrap(super(StructuredDataMessage, self).getId())

    @overload
    def getType(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getType()"""
        return str._wrap(super(StructuredDataMessage, self).getType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _byte.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'._wrap(super(_MapMessage, self).with(candidateKey, _long.valueOf(value)))

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, data: 'Map', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>,int)"""
        val = _StructuredDataMessage(id, msg, type, data, _int.valueOf(maxLength))
        self.__wrapper = val

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(_StructuredDataMessage, self).formatTo(formats, buffer)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str._wrap(super(_MapMessage, self).get(key))

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,int)"""
        val = _StructuredDataMessage(id, msg, type, _int.valueOf(maxLength))
        self.__wrapper = val

    @overload
    def asString(self, format: 'Format', structuredDataId: 'StructuredDataId', sb: 'StringBuilder'):
        """public final void org.apache.logging.log4j.message.StructuredDataMessage.asString(org.apache.logging.log4j.message.StructuredDataMessage$Format,org.apache.logging.log4j.message.StructuredDataId,java.lang.StringBuilder)"""
        super(_StructuredDataMessage, self).asString(format, structuredDataId, sb)

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataMessage.formatTo(java.lang.StringBuilder)"""
        super(_StructuredDataMessage, self).formatTo(buffer) 
 
 
# CLASS: org.apache.logging.log4j.message.TimestampMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.TimestampMessage as _TimestampMessage
_TimestampMessage = _TimestampMessage
 
class TimestampMessage():
    """org.apache.logging.log4j.message.TimestampMessage"""
 
    @staticmethod
    def _wrap(java_value: _TimestampMessage) -> 'TimestampMessage':
        return TimestampMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TimestampMessage):
        """
        Dynamic initializer for TimestampMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TimestampMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TimestampMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getTimestamp(self, ):
        """public abstract long org.apache.logging.log4j.message.TimestampMessage.getTimestamp()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.SimpleMessageFactory
import org.apache.logging.log4j.message.SimpleMessageFactory as _SimpleMessageFactory
_SimpleMessageFactory = _SimpleMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleMessageFactory():
    """org.apache.logging.log4j.message.SimpleMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _SimpleMessageFactory) -> 'SimpleMessageFactory':
        return SimpleMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleMessageFactory):
        """
        Dynamic initializer for SimpleMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.SimpleMessageFactory()"""
        val = _SimpleMessageFactory()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, params))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.SimpleMessageFactory()"""
        val = _SimpleMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_SimpleMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataCollectionMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
import org.apache.logging.log4j.message.StructuredDataCollectionMessage as _StructuredDataCollectionMessage
_StructuredDataCollectionMessage = _StructuredDataCollectionMessage
from typing import List
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class StructuredDataCollectionMessage():
    """org.apache.logging.log4j.message.StructuredDataCollectionMessage"""
 
    @staticmethod
    def _wrap(java_value: _StructuredDataCollectionMessage) -> 'StructuredDataCollectionMessage':
        return StructuredDataCollectionMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StructuredDataCollectionMessage):
        """
        Dynamic initializer for StructuredDataCollectionMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StructuredDataCollectionMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StructuredDataCollectionMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataCollectionMessage.getFormat()"""
        return str._wrap(super(StructuredDataCollectionMessage, self).getFormat())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.StructuredDataCollectionMessage.getParameters()"""
        return List[object]._wrap(super(StructuredDataCollectionMessage, self).getParameters())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.StructuredDataCollectionMessage.getThrowable()"""
        return 'Throwable'._wrap(super(StructuredDataCollectionMessage, self).getThrowable())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataCollectionMessage.formatTo(java.lang.StringBuilder)"""
        super(_StructuredDataCollectionMessage, self).formatTo(buffer)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataCollectionMessage.getFormattedMessage()"""
        return str._wrap(super(StructuredDataCollectionMessage, self).getFormattedMessage())

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, messages: 'List'):
        """public org.apache.logging.log4j.message.StructuredDataCollectionMessage(java.util.List<org.apache.logging.log4j.message.StructuredDataMessage>)"""
        val = _StructuredDataCollectionMessage(messages)
        self.__wrapper = val

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.logging.log4j.message.StructuredDataMessage> org.apache.logging.log4j.message.StructuredDataCollectionMessage.iterator()"""
        return 'Iterator'._wrap(super(StructuredDataCollectionMessage, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.DefaultFlowMessageFactory
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.ExitMessage as _ExitMessage
_ExitMessage = _ExitMessage
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.DefaultFlowMessageFactory as _DefaultFlowMessageFactory
_DefaultFlowMessageFactory = _DefaultFlowMessageFactory
from builtins import bool
import java.lang.Long as _long
import org.apache.logging.log4j.message.EntryMessage as _EntryMessage
_EntryMessage = _EntryMessage
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultFlowMessageFactory():
    """org.apache.logging.log4j.message.DefaultFlowMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _DefaultFlowMessageFactory) -> 'DefaultFlowMessageFactory':
        return DefaultFlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultFlowMessageFactory):
        """
        Dynamic initializer for DefaultFlowMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultFlowMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultFlowMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory()"""
        val = _DefaultFlowMessageFactory()
        self.__wrapper = val

    @overload
    def getExitText(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.DefaultFlowMessageFactory.getExitText()"""
        return str._wrap(super(DefaultFlowMessageFactory, self).getExitText())

    @overload
    def newExitMessage(self, result: object, message: 'EntryMessage') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.EntryMessage)"""
        return 'ExitMessage'._wrap(super(_DefaultFlowMessageFactory, self).newExitMessage(result, message))

    @overload
    def newExitMessage(self, message: 'Message') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.Message)"""
        return 'ExitMessage'._wrap(super(_DefaultFlowMessageFactory, self).newExitMessage(message))

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
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory()"""
        val = _DefaultFlowMessageFactory()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newEntryMessage(self, message: 'Message') -> 'EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newEntryMessage(org.apache.logging.log4j.message.Message)"""
        return 'EntryMessage'._wrap(super(_DefaultFlowMessageFactory, self).newEntryMessage(message))

    @overload
    def getEntryText(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.DefaultFlowMessageFactory.getEntryText()"""
        return str._wrap(super(DefaultFlowMessageFactory, self).getEntryText())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newExitMessage(self, format: str, result: object) -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.String,java.lang.Object)"""
        return 'ExitMessage'._wrap(super(_DefaultFlowMessageFactory, self).newExitMessage(format, result))

    @overload
    def newExitMessage(self, message: 'EntryMessage') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.EntryMessage)"""
        return 'ExitMessage'._wrap(super(_DefaultFlowMessageFactory, self).newExitMessage(message))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, entryText: str, exitText: str):
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory(java.lang.String,java.lang.String)"""
        val = _DefaultFlowMessageFactory(entryText, exitText)
        self.__wrapper = val

    @overload
    def newExitMessage(self, result: object, message: 'Message') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.Message)"""
        return 'ExitMessage'._wrap(super(_DefaultFlowMessageFactory, self).newExitMessage(result, message))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newEntryMessage(self, format: str, *params: object) -> 'EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newEntryMessage(java.lang.String,java.lang.Object...)"""
        return 'EntryMessage'._wrap(super(_DefaultFlowMessageFactory, self).newEntryMessage(format, params))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataMessage$Format
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.StructuredDataMessage as _StructuredDataMessage_Format
_Format = _StructuredDataMessage_Format.Format
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
 
class Format():
    """org.apache.logging.log4j.message.StructuredDataMessage.Format"""
 
    @staticmethod
    def _wrap(java_value: _Format) -> 'Format':
        return Format(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Format):
        """
        Dynamic initializer for Format.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Format__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Format__wrapper":
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
    def valueOf(name: str) -> 'Format':
        """public static org.apache.logging.log4j.message.StructuredDataMessage$Format org.apache.logging.log4j.message.StructuredDataMessage$Format.valueOf(java.lang.String)"""
        return Format._wrap(_Format.valueOf(name))

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
    def values() -> List['Format']:
        """public static org.apache.logging.log4j.message.StructuredDataMessage$Format[] org.apache.logging.log4j.message.StructuredDataMessage$Format.values()"""
        return List[Format]._wrap(_Format.values())

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
 
 
# CLASS: org.apache.logging.log4j.message.MultiformatMessage
from builtins import str
import org.apache.logging.log4j.message.MultiformatMessage as _MultiformatMessage
_MultiformatMessage = _MultiformatMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from abc import abstractmethod, ABC
 
class MultiformatMessage():
    """org.apache.logging.log4j.message.MultiformatMessage"""
 
    @staticmethod
    def _wrap(java_value: _MultiformatMessage) -> 'MultiformatMessage':
        return MultiformatMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiformatMessage):
        """
        Dynamic initializer for MultiformatMessage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiformatMessage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiformatMessage__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormats(self, ):
        """public abstract java.lang.String[] org.apache.logging.log4j.message.MultiformatMessage.getFormats()"""
        pass

    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, formats: 'String'):
        """public abstract java.lang.String org.apache.logging.log4j.message.MultiformatMessage.getFormattedMessage(java.lang.String[])"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory as _ParameterizedNoReferenceMessageFactory
_ParameterizedNoReferenceMessageFactory = _ParameterizedNoReferenceMessageFactory
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import org.apache.logging.log4j.message.AbstractMessageFactory as _AbstractMessageFactory
_AbstractMessageFactory = _AbstractMessageFactory
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParameterizedNoReferenceMessageFactory():
    """org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory"""
 
    @staticmethod
    def _wrap(java_value: _ParameterizedNoReferenceMessageFactory) -> 'ParameterizedNoReferenceMessageFactory':
        return ParameterizedNoReferenceMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterizedNoReferenceMessageFactory):
        """
        Dynamic initializer for ParameterizedNoReferenceMessageFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterizedNoReferenceMessageFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterizedNoReferenceMessageFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory()"""
        val = _ParameterizedNoReferenceMessageFactory()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'._wrap(super(_ParameterizedNoReferenceMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory()"""
        val = _ParameterizedNoReferenceMessageFactory()
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'._wrap(super(_AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())