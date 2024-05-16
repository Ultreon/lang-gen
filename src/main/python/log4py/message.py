from __future__ import annotations
from overload import overload


 
import org.apache.logging.log4j.message.FlowMessageFactory as __FlowMessageFactory
__FlowMessageFactory = __FlowMessageFactory
from builtins import object
from abc import abstractmethod, ABC
 
class FlowMessageFactory(ABC):
    """org.apache.logging.log4j.message.FlowMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __FlowMessageFactory) -> 'FlowMessageFactory':
        return FlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlowMessageFactory):
        """
        Dynamic initializer for FlowMessageFactory.
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
import org.apache.logging.log4j.message.FlowMessageFactory as __FlowMessageFactory
__FlowMessageFactory = __FlowMessageFactory
from builtins import object
from abc import abstractmethod, ABC
 
class FlowMessageFactory(ABC):
    """org.apache.logging.log4j.message.FlowMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __FlowMessageFactory) -> 'FlowMessageFactory':
        return FlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlowMessageFactory):
        """
        Dynamic initializer for FlowMessageFactory.
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
 
 
# CLASS: org.apache.logging.log4j.message.MessageFactory2
import java.lang.CharSequence as CharSequence
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
import org.apache.logging.log4j.message.MessageFactory2 as __MessageFactory2
__MessageFactory2 = __MessageFactory2
from abc import abstractmethod, ABC
from builtins import object
 
class MessageFactory2(ABC, __MessageFactory, MessageFactory):
    """org.apache.logging.log4j.message.MessageFactory2"""
 
    @staticmethod
    def __wrap(java_value: __MessageFactory2) -> 'MessageFactory2':
        return MessageFactory2(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFactory2):
        """
        Dynamic initializer for MessageFactory2.
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
 
 
# CLASS: org.apache.logging.log4j.message.MultiformatMessage
from builtins import str
import org.apache.logging.log4j.message.MultiformatMessage as __MultiformatMessage
__MultiformatMessage = __MultiformatMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class MultiformatMessage(ABC, __Message, Message):
    """org.apache.logging.log4j.message.MultiformatMessage"""
 
    @staticmethod
    def __wrap(java_value: __MultiformatMessage) -> 'MultiformatMessage':
        return MultiformatMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MultiformatMessage):
        """
        Dynamic initializer for MultiformatMessage.
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
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataMessage
from pyquantum_helper import import_once as __import_once__
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.logging.log4j.message.StructuredDataId as __StructuredDataId
__StructuredDataId = __StructuredDataId
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Double as __double
from builtins import bool
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as __IndexedReadOnlyStringMap
__IndexedReadOnlyStringMap = __IndexedReadOnlyStringMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.StructuredDataMessage as __StructuredDataMessage
__StructuredDataMessage = __StructuredDataMessage
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.MapMessage as __MapMessage
__MapMessage = __MapMessage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class StructuredDataMessage(__MapMessage, MapMessage):
    """org.apache.logging.log4j.message.StructuredDataMessage"""
 
    @staticmethod
    def __wrap(java_value: __StructuredDataMessage) -> 'StructuredDataMessage':
        return StructuredDataMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StructuredDataMessage):
        """
        Dynamic initializer for StructuredDataMessage.
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
    def getId(self) -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataMessage.getId()"""
        return 'StructuredDataId'.__wrap(super(StructuredDataMessage, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, data: 'Map'):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>)"""
        val = __StructuredDataMessage(id, msg, type, data)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString()"""
        return str.__wrap(super(StructuredDataMessage, self).asString())

    @overload
    def getType(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getType()"""
        return str.__wrap(super(StructuredDataMessage, self).getType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __boolean.valueOf(value)))

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).remove(key))

    @override
    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'.__wrap(super(MapMessage, self).getData())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormat()"""
        return str.__wrap(super(StructuredDataMessage, self).getFormat())

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormattedMessage(java.lang.String[])"""
        return str.__wrap(super(__StructuredDataMessage, self).getFormattedMessage(formats))

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __double.valueOf(value)))

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String)"""
        val = __StructuredDataMessage(id, msg, type)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def asString(self, format: 'Format', structuredDataId: 'StructuredDataId') -> str:
        """public final java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString(org.apache.logging.log4j.message.StructuredDataMessage$Format,org.apache.logging.log4j.message.StructuredDataId)"""
        return str.__wrap(super(__StructuredDataMessage, self).asString(format, structuredDataId))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __long.valueOf(value)))

    @overload
    def newInstance(self, map: 'Map') -> 'StructuredDataMessage':
        """public org.apache.logging.log4j.message.StructuredDataMessage org.apache.logging.log4j.message.StructuredDataMessage.newInstance(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'StructuredDataMessage'.__wrap(super(__StructuredDataMessage, self).newInstance(map))

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,int)"""
        val = __StructuredDataMessage(id, msg, type, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, id: str, msg: str, type: str, data: 'Map'):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>)"""
        val = __StructuredDataMessage(id, msg, type, data)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, id: str, msg: str, type: str, data: 'Map', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>,int)"""
        val = __StructuredDataMessage(id, msg, type, data, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, id: str, msg: str, type: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String,int)"""
        val = __StructuredDataMessage(id, msg, type, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.StructuredDataMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__StructuredDataMessage, self).equals(o))

    @overload
    def __init__(self, id: str, msg: str, type: str):
        """public org.apache.logging.log4j.message.StructuredDataMessage(java.lang.String,java.lang.String,java.lang.String)"""
        val = __StructuredDataMessage(id, msg, type)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__MapMessage, self).putAll(map)

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __short.valueOf(value)))

    @override
    @overload
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(__MapMessage, self).asXml(sb)

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.getFormattedMessage()"""
        return str.__wrap(super(StructuredDataMessage, self).getFormattedMessage())

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(__MapMessage, self).forEach(action)

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __float.valueOf(value)))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataMessage.formatTo(java.lang.StringBuilder)"""
        super(__StructuredDataMessage, self).formatTo(buffer)

    @override
    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(__MapMessage, self).put(candidateKey, value)

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __char.valueOf(value)))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(MapMessage, self).getThrowable())

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool.__wrap(super(__MapMessage, self).containsKey(key))

    @override
    @overload
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataMessage.getFormats()"""
        return List[str].__wrap(super(StructuredDataMessage, self).getFormats())

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).get(key))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.StructuredDataMessage.hashCode()"""
        return int.__wrap(super(StructuredDataMessage, self).hashCode())

    @overload
    def asString(self, format: 'Format', structuredDataId: 'StructuredDataId', sb: 'StringBuilder'):
        """public final void org.apache.logging.log4j.message.StructuredDataMessage.asString(org.apache.logging.log4j.message.StructuredDataMessage$Format,org.apache.logging.log4j.message.StructuredDataId,java.lang.StringBuilder)"""
        super(__StructuredDataMessage, self).asString(format, structuredDataId, sb)

    @overload
    def __init__(self, id: 'StructuredDataId', msg: str, type: str, data: 'Map', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataMessage(org.apache.logging.log4j.message.StructuredDataId,java.lang.String,java.lang.String,java.util.Map<java.lang.String, java.lang.String>,int)"""
        val = __StructuredDataMessage(id, msg, type, data, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(__StructuredDataMessage, self).formatTo(formats, buffer)

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __int.valueOf(value)))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __byte.valueOf(value)))

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.asString(java.lang.String)"""
        return str.__wrap(super(__StructuredDataMessage, self).asString(format))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataMessage.toString()"""
        return str.__wrap(super(StructuredDataMessage, self).toString())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object].__wrap(super(MapMessage, self).getParameters())

    @override
    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'.__wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(__MapMessage, self).forEach(action, state) 
 
 
# CLASS: org.apache.logging.log4j.message.ThreadDumpMessage$ThreadInfoFactory
import org.apache.logging.log4j.message.ThreadDumpMessage as __ThreadDumpMessage_ThreadInfoFactory
__ThreadInfoFactory = __ThreadDumpMessage_ThreadInfoFactory.ThreadInfoFactory
from abc import abstractmethod, ABC
 
class ThreadInfoFactory(ABC):
    """org.apache.logging.log4j.message.ThreadDumpMessage.ThreadInfoFactory"""
 
    @staticmethod
    def __wrap(java_value: __ThreadInfoFactory) -> 'ThreadInfoFactory':
        return ThreadInfoFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadInfoFactory):
        """
        Dynamic initializer for ThreadInfoFactory.
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
    def createThreadInfo(self, ):
        """public abstract java.util.Map<org.apache.logging.log4j.message.ThreadInformation, java.lang.StackTraceElement[]> org.apache.logging.log4j.message.ThreadDumpMessage$ThreadInfoFactory.createThreadInfo()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import org.apache.logging.log4j.message.ReusableMessageFactory as __ReusableMessageFactory
__ReusableMessageFactory = __ReusableMessageFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReusableMessageFactory(__MessageFactory2, MessageFactory2, __Serializable, Serializable):
    """org.apache.logging.log4j.message.ReusableMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __ReusableMessageFactory) -> 'ReusableMessageFactory':
        return ReusableMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReusableMessageFactory):
        """
        Dynamic initializer for ReusableMessageFactory.
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
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableMessageFactory()"""
        val = __ReusableMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableMessageFactory()"""
        val = __ReusableMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @staticmethod
    @overload
    def release(message: 'Message'):
        """public static void org.apache.logging.log4j.message.ReusableMessageFactory.release(org.apache.logging.log4j.message.Message)"""
        __ReusableMessageFactory.release(message)

    @overload
    def newMessage(self, charSequence: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(charSequence))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ReusableMessageFactory, self).newMessage(message, p0, p1)) 
 
 
# CLASS: org.apache.logging.log4j.message.ThreadInformation
import org.apache.logging.log4j.message.ThreadInformation as __ThreadInformation
__ThreadInformation = __ThreadInformation
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
import java.lang.StackTraceElement as StackTraceElement
 
class ThreadInformation(ABC):
    """org.apache.logging.log4j.message.ThreadInformation"""
 
    @staticmethod
    def __wrap(java_value: __ThreadInformation) -> 'ThreadInformation':
        return ThreadInformation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadInformation):
        """
        Dynamic initializer for ThreadInformation.
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
    def printStack(self, sb: 'StringBuilder', trace: 'StackTraceElement'):
        """public abstract void org.apache.logging.log4j.message.ThreadInformation.printStack(java.lang.StringBuilder,java.lang.StackTraceElement[])"""
        pass

    @abstractmethod
    def printThreadInfo(self, sb: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.message.ThreadInformation.printThreadInfo(java.lang.StringBuilder)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.StringFormattedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import org.apache.logging.log4j.message.StringFormattedMessage as __StringFormattedMessage
__StringFormattedMessage = __StringFormattedMessage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StringFormattedMessage(__Message, Message):
    """org.apache.logging.log4j.message.StringFormattedMessage"""
 
    @staticmethod
    def __wrap(java_value: __StringFormattedMessage) -> 'StringFormattedMessage':
        return StringFormattedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringFormattedMessage):
        """
        Dynamic initializer for StringFormattedMessage.
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
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.StringFormattedMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__StringFormattedMessage, self).equals(o))

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.StringFormattedMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = __StringFormattedMessage(locale, messagePattern, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.getFormat()"""
        return str.__wrap(super(StringFormattedMessage, self).getFormat())

    @overload
    def __init__(self, messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.StringFormattedMessage(java.lang.String,java.lang.Object...)"""
        val = __StringFormattedMessage(messagePattern, arguments)
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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.getFormattedMessage()"""
        return str.__wrap(super(StringFormattedMessage, self).getFormattedMessage())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.StringFormattedMessage.hashCode()"""
        return int.__wrap(super(StringFormattedMessage, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.StringFormattedMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(StringFormattedMessage, self).getThrowable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StringFormattedMessage.toString()"""
        return str.__wrap(super(StringFormattedMessage, self).toString())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.StringFormattedMessage.getParameters()"""
        return List[object].__wrap(super(StringFormattedMessage, self).getParameters()) 
 
 
# CLASS: org.apache.logging.log4j.message.FlowMessage
import org.apache.logging.log4j.message.FlowMessage as __FlowMessage
__FlowMessage = __FlowMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class FlowMessage(ABC, __Message, Message):
    """org.apache.logging.log4j.message.FlowMessage"""
 
    @staticmethod
    def __wrap(java_value: __FlowMessage) -> 'FlowMessage':
        return FlowMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FlowMessage):
        """
        Dynamic initializer for FlowMessage.
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
 
 
# CLASS: org.apache.logging.log4j.message.LoggerNameAwareMessage
import org.apache.logging.log4j.message.LoggerNameAwareMessage as __LoggerNameAwareMessage
__LoggerNameAwareMessage = __LoggerNameAwareMessage
from abc import abstractmethod, ABC
 
class LoggerNameAwareMessage(ABC):
    """org.apache.logging.log4j.message.LoggerNameAwareMessage"""
 
    @staticmethod
    def __wrap(java_value: __LoggerNameAwareMessage) -> 'LoggerNameAwareMessage':
        return LoggerNameAwareMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LoggerNameAwareMessage):
        """
        Dynamic initializer for LoggerNameAwareMessage.
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
    def getLoggerName(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.LoggerNameAwareMessage.getLoggerName()"""
        pass

    @abstractmethod
    def setLoggerName(self, name: str):
        """public abstract void org.apache.logging.log4j.message.LoggerNameAwareMessage.setLoggerName(java.lang.String)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.FormattedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
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
import org.apache.logging.log4j.message.FormattedMessage as __FormattedMessage
__FormattedMessage = __FormattedMessage
from builtins import int
 
class FormattedMessage(__Message, Message):
    """org.apache.logging.log4j.message.FormattedMessage"""
 
    @staticmethod
    def __wrap(java_value: __FormattedMessage) -> 'FormattedMessage':
        return FormattedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormattedMessage):
        """
        Dynamic initializer for FormattedMessage.
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
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.getFormat()"""
        return str.__wrap(super(FormattedMessage, self).getFormat())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object...)"""
        val = __FormattedMessage(messagePattern, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, messagePattern: str, arguments: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __FormattedMessage(messagePattern, arguments, throwable)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __FormattedMessage(locale, messagePattern, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object)"""
        val = __FormattedMessage(messagePattern, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object)"""
        val = __FormattedMessage(locale, messagePattern, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.FormattedMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__FormattedMessage, self).equals(o))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.getFormattedMessage()"""
        return str.__wrap(super(FormattedMessage, self).getFormattedMessage())

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, *arguments: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = __FormattedMessage(locale, messagePattern, arguments)
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
        """public int org.apache.logging.log4j.message.FormattedMessage.hashCode()"""
        return int.__wrap(super(FormattedMessage, self).hashCode())

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, arguments: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.FormattedMessage(java.util.Locale,java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __FormattedMessage(locale, messagePattern, arguments, throwable)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.FormattedMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(FormattedMessage, self).getThrowable())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.FormattedMessage.toString()"""
        return str.__wrap(super(FormattedMessage, self).toString())

    @overload
    def __init__(self, messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.FormattedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __FormattedMessage(messagePattern, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.FormattedMessage.getParameters()"""
        return List[object].__wrap(super(FormattedMessage, self).getParameters()) 
 
 
# CLASS: org.apache.logging.log4j.message.DefaultFlowMessageFactory
import org.apache.logging.log4j.message.EntryMessage as __EntryMessage
__EntryMessage = __EntryMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.DefaultFlowMessageFactory as __DefaultFlowMessageFactory
__DefaultFlowMessageFactory = __DefaultFlowMessageFactory
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.message.ExitMessage as __ExitMessage
__ExitMessage = __ExitMessage
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultFlowMessageFactory(__FlowMessageFactory, FlowMessageFactory, __Serializable, Serializable):
    """org.apache.logging.log4j.message.DefaultFlowMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __DefaultFlowMessageFactory) -> 'DefaultFlowMessageFactory':
        return DefaultFlowMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultFlowMessageFactory):
        """
        Dynamic initializer for DefaultFlowMessageFactory.
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
    def newEntryMessage(self, format: str, *params: object) -> 'EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newEntryMessage(java.lang.String,java.lang.Object...)"""
        return 'EntryMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newEntryMessage(format, params))

    @overload
    def newExitMessage(self, message: 'Message') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.Message)"""
        return 'ExitMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newExitMessage(message))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def newExitMessage(self, message: 'EntryMessage') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(org.apache.logging.log4j.message.EntryMessage)"""
        return 'ExitMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newExitMessage(message))

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
    def __init__(self):
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory()"""
        val = __DefaultFlowMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory()"""
        val = __DefaultFlowMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getExitText(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.DefaultFlowMessageFactory.getExitText()"""
        return str.__wrap(super(DefaultFlowMessageFactory, self).getExitText())

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
    def newEntryMessage(self, message: 'Message') -> 'EntryMessage':
        """public org.apache.logging.log4j.message.EntryMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newEntryMessage(org.apache.logging.log4j.message.Message)"""
        return 'EntryMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newEntryMessage(message))

    @overload
    def newExitMessage(self, format: str, result: object) -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.String,java.lang.Object)"""
        return 'ExitMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newExitMessage(format, result))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newExitMessage(self, result: object, message: 'Message') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.Message)"""
        return 'ExitMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newExitMessage(result, message))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def newExitMessage(self, result: object, message: 'EntryMessage') -> 'ExitMessage':
        """public org.apache.logging.log4j.message.ExitMessage org.apache.logging.log4j.message.DefaultFlowMessageFactory.newExitMessage(java.lang.Object,org.apache.logging.log4j.message.EntryMessage)"""
        return 'ExitMessage'.__wrap(super(__DefaultFlowMessageFactory, self).newExitMessage(result, message))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getEntryText(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.DefaultFlowMessageFactory.getEntryText()"""
        return str.__wrap(super(DefaultFlowMessageFactory, self).getEntryText())

    @overload
    def __init__(self, entryText: str, exitText: str):
        """public org.apache.logging.log4j.message.DefaultFlowMessageFactory(java.lang.String,java.lang.String)"""
        val = __DefaultFlowMessageFactory(entryText, exitText)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.message.SimpleMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.logging.log4j.message.SimpleMessageFactory as __SimpleMessageFactory
__SimpleMessageFactory = __SimpleMessageFactory
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.SimpleMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __SimpleMessageFactory) -> 'SimpleMessageFactory':
        return SimpleMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleMessageFactory):
        """
        Dynamic initializer for SimpleMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, params))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.SimpleMessageFactory()"""
        val = __SimpleMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
        """public org.apache.logging.log4j.message.SimpleMessageFactory()"""
        val = __SimpleMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.SimpleMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__SimpleMessageFactory, self).newMessage(message, p0, p1, p2)) 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableObjectMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.logging.log4j.message.ReusableObjectMessage as __ReusableObjectMessage
__ReusableObjectMessage = __ReusableObjectMessage
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReusableObjectMessage(__ReusableMessage, ReusableMessage, __ParameterVisitable, ParameterVisitable, __Clearable, Clearable):
    """org.apache.logging.log4j.message.ReusableObjectMessage"""
 
    @staticmethod
    def __wrap(java_value: __ReusableObjectMessage) -> 'ReusableObjectMessage':
        return ReusableObjectMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReusableObjectMessage):
        """
        Dynamic initializer for ReusableObjectMessage.
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
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.clear()"""
        super(ReusableObjectMessage, self).clear()

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableObjectMessage()"""
        val = __ReusableObjectMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, object: object):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.set(java.lang.Object)"""
        super(__ReusableObjectMessage, self).set(object)

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableObjectMessage()"""
        val = __ReusableObjectMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.toString()"""
        return str.__wrap(super(ReusableObjectMessage, self).toString())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableObjectMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ReusableObjectMessage, self).getThrowable())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.getFormattedMessage()"""
        return str.__wrap(super(ReusableObjectMessage, self).getFormattedMessage())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableObjectMessage.memento()"""
        return 'Message'.__wrap(super(ReusableObjectMessage, self).memento())

    @overload
    def getParameter(self) -> object:
        """public java.lang.Object org.apache.logging.log4j.message.ReusableObjectMessage.getParameter()"""
        return object.__wrap(super(ReusableObjectMessage, self).getParameter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableObjectMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(__ReusableObjectMessage, self).forEachParameter(action, state)

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableObjectMessage.getFormat()"""
        return str.__wrap(super(ReusableObjectMessage, self).getFormat())

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
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableObjectMessage.formatTo(java.lang.StringBuilder)"""
        super(__ReusableObjectMessage, self).formatTo(buffer)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableObjectMessage.getParameterCount()"""
        return int.__wrap(super(ReusableObjectMessage, self).getParameterCount())

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableObjectMessage.swapParameters(java.lang.Object[])"""
        return List[object].__wrap(super(__ReusableObjectMessage, self).swapParameters(emptyReplacement))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableObjectMessage.getParameters()"""
        return List[object].__wrap(super(ReusableObjectMessage, self).getParameters()) 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterConsumer
import org.apache.logging.log4j.message.ParameterConsumer as __ParameterConsumer
__ParameterConsumer = __ParameterConsumer
from abc import abstractmethod, ABC
 
class ParameterConsumer(ABC):
    """org.apache.logging.log4j.message.ParameterConsumer"""
 
    @staticmethod
    def __wrap(java_value: __ParameterConsumer) -> 'ParameterConsumer':
        return ParameterConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterConsumer):
        """
        Dynamic initializer for ParameterConsumer.
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
    def accept(self, parameter: object, parameterIndex: int, state: object):
        """public abstract void org.apache.logging.log4j.message.ParameterConsumer.accept(java.lang.Object,int,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.ParameterizedMessage as __ParameterizedMessage
__ParameterizedMessage = __ParameterizedMessage
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParameterizedMessage(__Message, Message, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.message.ParameterizedMessage"""
 
    @staticmethod
    def __wrap(java_value: __ParameterizedMessage) -> 'ParameterizedMessage':
        return ParameterizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterizedMessage):
        """
        Dynamic initializer for ParameterizedMessage.
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

    @staticmethod
    @overload
    def identityToString(obj: object) -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.identityToString(java.lang.Object)"""
        return str.__wrap(__ParameterizedMessage.identityToString(obj))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ParameterizedMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__ParameterizedMessage, self).equals(object))

    @staticmethod
    @overload
    def countArgumentPlaceholders(pattern: str) -> int:
        """public static int org.apache.logging.log4j.message.ParameterizedMessage.countArgumentPlaceholders(java.lang.String)"""
        return int.__wrap(__ParameterizedMessage.countArgumentPlaceholders(pattern))

    @staticmethod
    @overload
    def format(pattern: str, args: 'Object') -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.format(java.lang.String,java.lang.Object[])"""
        return str.__wrap(__ParameterizedMessage.format(pattern, args))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ParameterizedMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ParameterizedMessage, self).getThrowable())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.getFormat()"""
        return str.__wrap(super(ParameterizedMessage, self).getFormat())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, pattern: str, args: 'String', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.String[],java.lang.Throwable)"""
        val = __ParameterizedMessage(pattern, args, throwable)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.getFormattedMessage()"""
        return str.__wrap(super(ParameterizedMessage, self).getFormattedMessage())

    @staticmethod
    @overload
    def deepToString(o: object) -> str:
        """public static java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.deepToString(java.lang.Object)"""
        return str.__wrap(__ParameterizedMessage.deepToString(o))

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

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ParameterizedMessage.getParameters()"""
        return List[object].__wrap(super(ParameterizedMessage, self).getParameters())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ParameterizedMessage.formatTo(java.lang.StringBuilder)"""
        super(__ParameterizedMessage, self).formatTo(buffer)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, pattern: str, *args: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object...)"""
        val = __ParameterizedMessage(pattern, args)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ParameterizedMessage.toString()"""
        return str.__wrap(super(ParameterizedMessage, self).toString())

    @overload
    def __init__(self, pattern: str, args: 'Object', throwable: 'Throwable'):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object[],java.lang.Throwable)"""
        val = __ParameterizedMessage(pattern, args, throwable)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, pattern: str, arg0: object, arg1: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __ParameterizedMessage(pattern, arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ParameterizedMessage.hashCode()"""
        return int.__wrap(super(ParameterizedMessage, self).hashCode())

    @overload
    def __init__(self, pattern: str, arg: object):
        """public org.apache.logging.log4j.message.ParameterizedMessage(java.lang.String,java.lang.Object)"""
        val = __ParameterizedMessage(pattern, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.AsynchronouslyFormattable
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.AsynchronouslyFormattable as __AsynchronouslyFormattable
__AsynchronouslyFormattable = __AsynchronouslyFormattable
 
class AsynchronouslyFormattable(ABC, __Annotation, Annotation):
    """org.apache.logging.log4j.message.AsynchronouslyFormattable"""
 
    @staticmethod
    def __wrap(java_value: __AsynchronouslyFormattable) -> 'AsynchronouslyFormattable':
        return AsynchronouslyFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsynchronouslyFormattable):
        """
        Dynamic initializer for AsynchronouslyFormattable.
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
 
 
# CLASS: org.apache.logging.log4j.message.ReusableMessage
import org.apache.logging.log4j.util.StringBuilderFormattable as __StringBuilderFormattable
__StringBuilderFormattable = __StringBuilderFormattable
import org.apache.logging.log4j.message.ReusableMessage as __ReusableMessage
__ReusableMessage = __ReusableMessage
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class ReusableMessage(ABC, __Message, Message, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.message.ReusableMessage"""
 
    @staticmethod
    def __wrap(java_value: __ReusableMessage) -> 'ReusableMessage':
        return ReusableMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReusableMessage):
        """
        Dynamic initializer for ReusableMessage.
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
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.StructuredDataId as __StructuredDataId
__StructuredDataId = __StructuredDataId
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StructuredDataId(__Serializable, Serializable, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.message.StructuredDataId"""
 
    @staticmethod
    def __wrap(java_value: __StructuredDataId) -> 'StructuredDataId':
        return StructuredDataId(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StructuredDataId):
        """
        Dynamic initializer for StructuredDataId.
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
    def __init__(self, name: str, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String[],java.lang.String[])"""
        val = __StructuredDataId(name, required, optional)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.toString()"""
        return str.__wrap(super(StructuredDataId, self).toString())

    @overload
    def makeId(self, defaultId: str, anEnterpriseNumber: str) -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(java.lang.String,java.lang.String)"""
        return 'StructuredDataId'.__wrap(super(__StructuredDataId, self).makeId(defaultId, anEnterpriseNumber))

    @overload
    def isReserved(self) -> bool:
        """public boolean org.apache.logging.log4j.message.StructuredDataId.isReserved()"""
        return bool.__wrap(super(StructuredDataId, self).isReserved())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEnterpriseNumber(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.getEnterpriseNumber()"""
        return str.__wrap(super(StructuredDataId, self).getEnterpriseNumber())

    @overload
    def makeId(self, defaultId: str, anEnterpriseNumber: int) -> 'StructuredDataId':
        """public final org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(java.lang.String,int)"""
        return 'StructuredDataId'.__wrap(super(__StructuredDataId, self).makeId(defaultId, __int.valueOf(anEnterpriseNumber)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, name: str, enterpriseNumber: int, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int,java.lang.String[],java.lang.String[])"""
        val = __StructuredDataId(name, __int.valueOf(enterpriseNumber), required, optional)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, name: str, enterpriseNumber: str, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String,java.lang.String[],java.lang.String[],int)"""
        val = __StructuredDataId(name, enterpriseNumber, required, optional, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, name: str, enterpriseNumber: int, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int,java.lang.String[],java.lang.String[],int)"""
        val = __StructuredDataId(name, __int.valueOf(enterpriseNumber), required, optional, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, name: str, required: 'String', optional: 'String', maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String[],java.lang.String[],int)"""
        val = __StructuredDataId(name, required, optional, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, name: str, maxLength: int):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,int)"""
        val = __StructuredDataId(name, __int.valueOf(maxLength))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getRequired(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataId.getRequired()"""
        return List[str].__wrap(super(StructuredDataId, self).getRequired())

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String)"""
        val = __StructuredDataId(name)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataId.getName()"""
        return str.__wrap(super(StructuredDataId, self).getName())

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
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataId.formatTo(java.lang.StringBuilder)"""
        super(__StructuredDataId, self).formatTo(buffer)

    @overload
    def __init__(self, name: str, enterpriseNumber: str, required: 'String', optional: 'String'):
        """public org.apache.logging.log4j.message.StructuredDataId(java.lang.String,java.lang.String,java.lang.String[],java.lang.String[])"""
        val = __StructuredDataId(name, enterpriseNumber, required, optional)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getOptional(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.StructuredDataId.getOptional()"""
        return List[str].__wrap(super(StructuredDataId, self).getOptional())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def makeId(self, id: 'StructuredDataId') -> 'StructuredDataId':
        """public org.apache.logging.log4j.message.StructuredDataId org.apache.logging.log4j.message.StructuredDataId.makeId(org.apache.logging.log4j.message.StructuredDataId)"""
        return 'StructuredDataId'.__wrap(super(__StructuredDataId, self).makeId(id)) 
 
 
# CLASS: org.apache.logging.log4j.message.StringMapMessage
from pyquantum_helper import import_once as __import_once__
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import org.apache.logging.log4j.message.StringMapMessage as __StringMapMessage
__StringMapMessage = __StringMapMessage
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Double as __double
from builtins import bool
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as __IndexedReadOnlyStringMap
__IndexedReadOnlyStringMap = __IndexedReadOnlyStringMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.MapMessage as __MapMessage
__MapMessage = __MapMessage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class StringMapMessage(__MapMessage, MapMessage):
    """org.apache.logging.log4j.message.StringMapMessage"""
 
    @staticmethod
    def __wrap(java_value: __StringMapMessage) -> 'StringMapMessage':
        return StringMapMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringMapMessage):
        """
        Dynamic initializer for StringMapMessage.
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
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.MapMessage.getFormats()"""
        return List[str].__wrap(super(MapMessage, self).getFormats())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage()"""
        return str.__wrap(super(MapMessage, self).getFormattedMessage())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.StringMapMessage()"""
        val = __StringMapMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.message.StringMapMessage(int)"""
        val = __StringMapMessage(__int.valueOf(initialCapacity))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__MapMessage, self).putAll(map)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __short.valueOf(value)))

    @override
    @overload
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(__MapMessage, self).asXml(sb)

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.message.StringMapMessage(java.util.Map<java.lang.String, java.lang.String>)"""
        val = __StringMapMessage(map)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.StringMapMessage()"""
        val = __StringMapMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(__MapMessage, self).forEach(action)

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __float.valueOf(value)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __boolean.valueOf(value)))

    @override
    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(__MapMessage, self).put(candidateKey, value)

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(__MapMessage, self).formatTo(formats, buffer)

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).remove(key))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __char.valueOf(value)))

    @override
    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'.__wrap(super(MapMessage, self).getData())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(MapMessage, self).getThrowable())

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool.__wrap(super(__MapMessage, self).containsKey(key))

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormat()"""
        return str.__wrap(super(MapMessage, self).getFormat())

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).get(key))

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __double.valueOf(value)))

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage(java.lang.String[])"""
        return str.__wrap(super(__MapMessage, self).getFormattedMessage(formats))

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString()"""
        return str.__wrap(super(MapMessage, self).asString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.MapMessage.hashCode()"""
        return int.__wrap(super(MapMessage, self).hashCode())

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __int.valueOf(value)))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.StringBuilder)"""
        super(__MapMessage, self).formatTo(buffer)

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).asString(format))

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__MapMessage, self).equals(o))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __byte.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.toString()"""
        return str.__wrap(super(MapMessage, self).toString())

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object].__wrap(super(MapMessage, self).getParameters())

    @override
    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'.__wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newInstance(self, map: 'Map') -> 'StringMapMessage':
        """public org.apache.logging.log4j.message.StringMapMessage org.apache.logging.log4j.message.StringMapMessage.newInstance(java.util.Map<java.lang.String, java.lang.String>)"""
        return 'StringMapMessage'.__wrap(super(__StringMapMessage, self).newInstance(map))

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(__MapMessage, self).forEach(action, state) 
 
 
# CLASS: org.apache.logging.log4j.message.FormattedMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.FormattedMessageFactory as __FormattedMessageFactory
__FormattedMessageFactory = __FormattedMessageFactory
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FormattedMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.FormattedMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __FormattedMessageFactory) -> 'FormattedMessageFactory':
        return FormattedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormattedMessageFactory):
        """
        Dynamic initializer for FormattedMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.FormattedMessageFactory()"""
        val = __FormattedMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.FormattedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__FormattedMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.FormattedMessageFactory()"""
        val = __FormattedMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataCollectionMessage
import org.apache.logging.log4j.message.StructuredDataCollectionMessage as __StructuredDataCollectionMessage
__StructuredDataCollectionMessage = __StructuredDataCollectionMessage
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import java.util.Iterator as Iterator
from typing import List
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
import java.lang.Long as __long
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.List as List
 
class StructuredDataCollectionMessage(log4py.__StringBuilderFormattable, util.StringBuilderFormattable, __MessageCollectionMessage, MessageCollectionMessage):
    """org.apache.logging.log4j.message.StructuredDataCollectionMessage"""
 
    @staticmethod
    def __wrap(java_value: __StructuredDataCollectionMessage) -> 'StructuredDataCollectionMessage':
        return StructuredDataCollectionMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StructuredDataCollectionMessage):
        """
        Dynamic initializer for StructuredDataCollectionMessage.
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
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.logging.log4j.message.StructuredDataMessage> org.apache.logging.log4j.message.StructuredDataCollectionMessage.iterator()"""
        return 'Iterator'.__wrap(super(StructuredDataCollectionMessage, self).iterator())

    @overload
    def __init__(self, messages: 'List'):
        """public org.apache.logging.log4j.message.StructuredDataCollectionMessage(java.util.List<org.apache.logging.log4j.message.StructuredDataMessage>)"""
        val = __StructuredDataCollectionMessage(messages)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.StructuredDataCollectionMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(StructuredDataCollectionMessage, self).getThrowable())

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
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataCollectionMessage.getFormat()"""
        return str.__wrap(super(StructuredDataCollectionMessage, self).getFormat())

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.StructuredDataCollectionMessage.getParameters()"""
        return List[object].__wrap(super(StructuredDataCollectionMessage, self).getParameters())

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
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.StructuredDataCollectionMessage.formatTo(java.lang.StringBuilder)"""
        super(__StructuredDataCollectionMessage, self).formatTo(buffer)

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

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.StructuredDataCollectionMessage.getFormattedMessage()"""
        return str.__wrap(super(StructuredDataCollectionMessage, self).getFormattedMessage())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.message.MapMessage$MapFormat
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import org.apache.logging.log4j.message.MapMessage as __MapMessage_MapFormat
__MapFormat = __MapMessage_MapFormat.MapFormat
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
from builtins import int
 
class MapFormat(__Enum, Enum):
    """org.apache.logging.log4j.message.MapMessage.MapFormat"""
 
    @staticmethod
    def __wrap(java_value: __MapFormat) -> 'MapFormat':
        return MapFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapFormat):
        """
        Dynamic initializer for MapFormat.
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
    def values() -> List['MapFormat']:
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat[] org.apache.logging.log4j.message.MapMessage$MapFormat.values()"""
        return List[MapFormat].__wrap(__MapFormat.values())

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
    def valueOf(name: str) -> 'MapFormat':
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat org.apache.logging.log4j.message.MapMessage$MapFormat.valueOf(java.lang.String)"""
        return MapFormat.__wrap(__MapFormat.valueOf(name))

    @staticmethod
    @overload
    def lookupIgnoreCase(format: str) -> 'MapFormat':
        """public static org.apache.logging.log4j.message.MapMessage$MapFormat org.apache.logging.log4j.message.MapMessage$MapFormat.lookupIgnoreCase(java.lang.String)"""
        return MapFormat.__wrap(__MapFormat.lookupIgnoreCase(format))

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
    def names() -> List[str]:
        """public static java.lang.String[] org.apache.logging.log4j.message.MapMessage$MapFormat.names()"""
        return List[str].__wrap(__MapFormat.names()) 
 
 
# CLASS: org.apache.logging.log4j.message.ExitMessage
import org.apache.logging.log4j.message.ExitMessage as __ExitMessage
__ExitMessage = __ExitMessage
import org.apache.logging.log4j.message.FlowMessage as __FlowMessage
__FlowMessage = __FlowMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class ExitMessage(ABC, __FlowMessage, FlowMessage):
    """org.apache.logging.log4j.message.ExitMessage"""
 
    @staticmethod
    def __wrap(java_value: __ExitMessage) -> 'ExitMessage':
        return ExitMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ExitMessage):
        """
        Dynamic initializer for ExitMessage.
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
 
 
# CLASS: org.apache.logging.log4j.message.ThreadDumpMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.logging.log4j.message.ThreadDumpMessage as __ThreadDumpMessage
__ThreadDumpMessage = __ThreadDumpMessage
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ThreadDumpMessage(__Message, Message, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.message.ThreadDumpMessage"""
 
    @staticmethod
    def __wrap(java_value: __ThreadDumpMessage) -> 'ThreadDumpMessage':
        return ThreadDumpMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThreadDumpMessage):
        """
        Dynamic initializer for ThreadDumpMessage.
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
    def formatTo(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ThreadDumpMessage.formatTo(java.lang.StringBuilder)"""
        super(__ThreadDumpMessage, self).formatTo(sb)

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.getFormattedMessage()"""
        return str.__wrap(super(ThreadDumpMessage, self).getFormattedMessage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.toString()"""
        return str.__wrap(super(ThreadDumpMessage, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ThreadDumpMessage.getParameters()"""
        return List[object].__wrap(super(ThreadDumpMessage, self).getParameters())

    @overload
    def __init__(self, title: str):
        """public org.apache.logging.log4j.message.ThreadDumpMessage(java.lang.String)"""
        val = __ThreadDumpMessage(title)
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

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ThreadDumpMessage.getFormat()"""
        return str.__wrap(super(ThreadDumpMessage, self).getFormat())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ThreadDumpMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ThreadDumpMessage, self).getThrowable())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.message.MessageCollectionMessage
import java.util.Spliterator as Spliterator
import org.apache.logging.log4j.message.MessageCollectionMessage as __MessageCollectionMessage
__MessageCollectionMessage = __MessageCollectionMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
 
class MessageCollectionMessage(ABC, __Message, Message, __Iterable, Iterable):
    """org.apache.logging.log4j.message.MessageCollectionMessage"""
 
    @staticmethod
    def __wrap(java_value: __MessageCollectionMessage) -> 'MessageCollectionMessage':
        return MessageCollectionMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageCollectionMessage):
        """
        Dynamic initializer for MessageCollectionMessage.
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

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.MapMessage
from pyquantum_helper import import_once as __import_once__
import java.lang.Character as __char
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.Byte as __byte
import java.lang.Short as __short
try:
    from log4py import util
except ImportError:
    util = __import_once__("log4py.util")

import java.lang.Double as __double
from builtins import bool
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as __IndexedReadOnlyStringMap
__IndexedReadOnlyStringMap = __IndexedReadOnlyStringMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.MapMessage as __MapMessage
__MapMessage = __MapMessage
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class MapMessage(log4py.__MultiFormatStringBuilderFormattable, util.MultiFormatStringBuilderFormattable):
    """org.apache.logging.log4j.message.MapMessage"""
 
    @staticmethod
    def __wrap(java_value: __MapMessage) -> 'MapMessage':
        return MapMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MapMessage):
        """
        Dynamic initializer for MapMessage.
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
    def getFormats(self) -> List[str]:
        """public java.lang.String[] org.apache.logging.log4j.message.MapMessage.getFormats()"""
        return List[str].__wrap(super(MapMessage, self).getFormats())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage()"""
        return str.__wrap(super(MapMessage, self).getFormattedMessage())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,short)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __short.valueOf(value)))

    @overload
    def getIndexedReadOnlyStringMap(self) -> 'util.IndexedReadOnlyStringMap':
        """public org.apache.logging.log4j.util.IndexedReadOnlyStringMap org.apache.logging.log4j.message.MapMessage.getIndexedReadOnlyStringMap()"""
        return 'util.IndexedReadOnlyStringMap'.__wrap(super(MapMessage, self).getIndexedReadOnlyStringMap())

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,float)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __float.valueOf(value)))

    @overload
    def asString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString()"""
        return str.__wrap(super(MapMessage, self).asString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.MapMessage.clear()"""
        super(MapMessage, self).clear()

    @overload
    def with(self, candidateKey: str, value: bool) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,boolean)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __boolean.valueOf(value)))

    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <CV,S> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super CV, S>,S)"""
        super(__MapMessage, self).forEach(action, state)

    @overload
    def put(self, candidateKey: str, value: str):
        """public void org.apache.logging.log4j.message.MapMessage.put(java.lang.String,java.lang.String)"""
        super(__MapMessage, self).put(candidateKey, value)

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.MapMessage()"""
        val = __MapMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        super(__MapMessage, self).formatTo(formats, buffer)

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.MapMessage()"""
        val = __MapMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def remove(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.remove(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).remove(key))

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.message.MapMessage(java.util.Map<java.lang.String, V>)"""
        val = __MapMessage(map)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,char)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __char.valueOf(value)))

    @overload
    def asXml(self, sb: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.asXml(java.lang.StringBuilder)"""
        super(__MapMessage, self).asXml(sb)

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MapMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(MapMessage, self).getThrowable())

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.containsKey(java.lang.String)"""
        return bool.__wrap(super(__MapMessage, self).containsKey(key))

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormat()"""
        return str.__wrap(super(MapMessage, self).getFormat())

    @overload
    def get(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.get(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).get(key))

    @overload
    def with(self, candidateKey: str, value: float) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,double)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __double.valueOf(value)))

    @overload
    def getFormattedMessage(self, formats: 'String') -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.getFormattedMessage(java.lang.String[])"""
        return str.__wrap(super(__MapMessage, self).getFormattedMessage(formats))

    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <CV> void org.apache.logging.log4j.message.MapMessage.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super CV>)"""
        super(__MapMessage, self).forEach(action)

    @overload
    def newInstance(self, map: 'Map') -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.newInstance(java.util.Map<java.lang.String, V>)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).newInstance(map))

    @overload
    def with(self, candidateKey: str, value: object) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.Object)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,long)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __long.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def with(self, candidateKey: str, value: str) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,java.lang.String)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.MapMessage.hashCode()"""
        return int.__wrap(super(MapMessage, self).hashCode())

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,int)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __int.valueOf(value)))

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.MapMessage.formatTo(java.lang.StringBuilder)"""
        super(__MapMessage, self).formatTo(buffer)

    @overload
    def asString(self, format: str) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.asString(java.lang.String)"""
        return str.__wrap(super(__MapMessage, self).asString(format))

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MapMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__MapMessage, self).equals(o))

    @overload
    def with(self, candidateKey: str, value: int) -> 'MapMessage':
        """public M org.apache.logging.log4j.message.MapMessage.with(java.lang.String,byte)"""
        return 'MapMessage'.__wrap(super(__MapMessage, self).with(candidateKey, __byte.valueOf(value)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MapMessage.toString()"""
        return str.__wrap(super(MapMessage, self).toString())

    @overload
    def putAll(self, map: 'Map'):
        """public void org.apache.logging.log4j.message.MapMessage.putAll(java.util.Map<java.lang.String, java.lang.String>)"""
        super(__MapMessage, self).putAll(map)

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MapMessage.getParameters()"""
        return List[object].__wrap(super(MapMessage, self).getParameters())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getData(self) -> 'Map':
        """public java.util.Map<java.lang.String, V> org.apache.logging.log4j.message.MapMessage.getData()"""
        return 'Map'.__wrap(super(MapMessage, self).getData())

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.message.MapMessage(int)"""
        val = __MapMessage(__int.valueOf(initialCapacity))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFormatMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.MessageFormatMessage as __MessageFormatMessage
__MessageFormatMessage = __MessageFormatMessage
from typing import List
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
 
class MessageFormatMessage(__Message, Message):
    """org.apache.logging.log4j.message.MessageFormatMessage"""
 
    @staticmethod
    def __wrap(java_value: __MessageFormatMessage) -> 'MessageFormatMessage':
        return MessageFormatMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFormatMessage):
        """
        Dynamic initializer for MessageFormatMessage.
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
    def __init__(self, messagePattern: str, *parameters: object):
        """public org.apache.logging.log4j.message.MessageFormatMessage(java.lang.String,java.lang.Object...)"""
        val = __MessageFormatMessage(messagePattern, parameters)
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
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.MessageFormatMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__MessageFormatMessage, self).equals(o))

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.MessageFormatMessage.getParameters()"""
        return List[object].__wrap(super(MessageFormatMessage, self).getParameters())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.getFormattedMessage()"""
        return str.__wrap(super(MessageFormatMessage, self).getFormattedMessage())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, locale: 'Locale', messagePattern: str, *parameters: object):
        """public org.apache.logging.log4j.message.MessageFormatMessage(java.util.Locale,java.lang.String,java.lang.Object...)"""
        val = __MessageFormatMessage(locale, messagePattern, parameters)
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
        """public int org.apache.logging.log4j.message.MessageFormatMessage.hashCode()"""
        return int.__wrap(super(MessageFormatMessage, self).hashCode())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.getFormat()"""
        return str.__wrap(super(MessageFormatMessage, self).getFormat())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.MessageFormatMessage.toString()"""
        return str.__wrap(super(MessageFormatMessage, self).toString())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.MessageFormatMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(MessageFormatMessage, self).getThrowable()) 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFactory
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
from abc import abstractmethod, ABC
from builtins import object
 
class MessageFactory(ABC):
    """org.apache.logging.log4j.message.MessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __MessageFactory) -> 'MessageFactory':
        return MessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFactory):
        """
        Dynamic initializer for MessageFactory.
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
 
 
# CLASS: org.apache.logging.log4j.message.LocalizedMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.ResourceBundle as ResourceBundle
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.LocalizedMessageFactory as __LocalizedMessageFactory
__LocalizedMessageFactory = __LocalizedMessageFactory
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.util.ResourceBundle as __ResourceBundle
__ResourceBundle = __ResourceBundle
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LocalizedMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.LocalizedMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __LocalizedMessageFactory) -> 'LocalizedMessageFactory':
        return LocalizedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocalizedMessageFactory):
        """
        Dynamic initializer for LocalizedMessageFactory.
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
    def __init__(self, resourceBundle: 'ResourceBundle'):
        """public org.apache.logging.log4j.message.LocalizedMessageFactory(java.util.ResourceBundle)"""
        val = __LocalizedMessageFactory(resourceBundle)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
    def getResourceBundle(self) -> 'ResourceBundle':
        """public java.util.ResourceBundle org.apache.logging.log4j.message.LocalizedMessageFactory.getResourceBundle()"""
        return 'ResourceBundle'.__wrap(super(LocalizedMessageFactory, self).getResourceBundle())

    @overload
    def __init__(self, baseName: str):
        """public org.apache.logging.log4j.message.LocalizedMessageFactory(java.lang.String)"""
        val = __LocalizedMessageFactory(baseName)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
    def getBaseName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessageFactory.getBaseName()"""
        return str.__wrap(super(LocalizedMessageFactory, self).getBaseName())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, key: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.LocalizedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__LocalizedMessageFactory, self).newMessage(key, params))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, key: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.LocalizedMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__LocalizedMessageFactory, self).newMessage(key)) 
 
 
# CLASS: org.apache.logging.log4j.message.AbstractMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.MessageFactory as __MessageFactory
__MessageFactory = __MessageFactory
from builtins import object
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractMessageFactory(ABC, __MessageFactory2, MessageFactory2, __Serializable, Serializable):
    """org.apache.logging.log4j.message.AbstractMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __AbstractMessageFactory) -> 'AbstractMessageFactory':
        return AbstractMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractMessageFactory):
        """
        Dynamic initializer for AbstractMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.AbstractMessageFactory()"""
        val = __AbstractMessageFactory()
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

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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

    @abstractmethod
    def newMessage(self, message: str, *params: object):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        pass

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.AbstractMessageFactory()"""
        val = __AbstractMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableSimpleMessage
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import org.apache.logging.log4j.message.ReusableSimpleMessage as __ReusableSimpleMessage
__ReusableSimpleMessage = __ReusableSimpleMessage
from typing import List
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class ReusableSimpleMessage(__ReusableMessage, ReusableMessage, __CharSequence, CharSequence, __ParameterVisitable, ParameterVisitable, __Clearable, Clearable):
    """org.apache.logging.log4j.message.ReusableSimpleMessage"""
 
    @staticmethod
    def __wrap(java_value: __ReusableSimpleMessage) -> 'ReusableSimpleMessage':
        return ReusableSimpleMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReusableSimpleMessage):
        """
        Dynamic initializer for ReusableSimpleMessage.
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
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableSimpleMessage.getParameterCount()"""
        return int.__wrap(super(ReusableSimpleMessage, self).getParameterCount())

    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableSimpleMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(__ReusableSimpleMessage, self).forEachParameter(action, state)

    @overload
    def set(self, message: str):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.set(java.lang.String)"""
        super(__ReusableSimpleMessage, self).set(message)

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableSimpleMessage.getFormattedMessage()"""
        return str.__wrap(super(ReusableSimpleMessage, self).getFormattedMessage())

    @overload
    def set(self, charSequence: 'CharSequence'):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.set(java.lang.CharSequence)"""
        super(__ReusableSimpleMessage, self).set(charSequence)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableSimpleMessage.memento()"""
        return 'Message'.__wrap(super(ReusableSimpleMessage, self).memento())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableSimpleMessage()"""
        val = __ReusableSimpleMessage()
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def charAt(self, index: int) -> str:
        """public char org.apache.logging.log4j.message.ReusableSimpleMessage.charAt(int)"""
        return str.__wrap(super(__ReusableSimpleMessage, self).charAt(__int.valueOf(index)))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public default boolean java.lang.CharSequence.isEmpty()"""
        return bool.__wrap(super(CharSequence, self).isEmpty())

    @overload
    def subSequence(self, start: int, end: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.message.ReusableSimpleMessage.subSequence(int,int)"""
        return 'CharSequence'.__wrap(super(__ReusableSimpleMessage, self).subSequence(__int.valueOf(start), __int.valueOf(end)))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableSimpleMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ReusableSimpleMessage, self).getThrowable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.logging.log4j.message.ReusableSimpleMessage.length()"""
        return int.__wrap(super(ReusableSimpleMessage, self).length())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.formatTo(java.lang.StringBuilder)"""
        super(__ReusableSimpleMessage, self).formatTo(buffer)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableSimpleMessage.swapParameters(java.lang.Object[])"""
        return List[object].__wrap(super(__ReusableSimpleMessage, self).swapParameters(emptyReplacement))

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'.__wrap(super(CharSequence, self).codePoints())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ReusableSimpleMessage()"""
        val = __ReusableSimpleMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableSimpleMessage.getParameters()"""
        return List[object].__wrap(super(ReusableSimpleMessage, self).getParameters())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableSimpleMessage.getFormat()"""
        return str.__wrap(super(ReusableSimpleMessage, self).getFormat())

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'.__wrap(super(CharSequence, self).chars())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableSimpleMessage.clear()"""
        super(ReusableSimpleMessage, self).clear() 
 
 
# CLASS: org.apache.logging.log4j.message.ObjectArrayMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
from typing import List
import java.lang.Long as __long
import org.apache.logging.log4j.message.ObjectArrayMessage as __ObjectArrayMessage
__ObjectArrayMessage = __ObjectArrayMessage
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjectArrayMessage(__Message, Message):
    """org.apache.logging.log4j.message.ObjectArrayMessage"""
 
    @staticmethod
    def __wrap(java_value: __ObjectArrayMessage) -> 'ObjectArrayMessage':
        return ObjectArrayMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectArrayMessage):
        """
        Dynamic initializer for ObjectArrayMessage.
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
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.getFormattedMessage()"""
        return str.__wrap(super(ObjectArrayMessage, self).getFormattedMessage())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ObjectArrayMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectArrayMessage, self).equals(o))

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ObjectArrayMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ObjectArrayMessage, self).getThrowable())

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
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ObjectArrayMessage.getParameters()"""
        return List[object].__wrap(super(ObjectArrayMessage, self).getParameters())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.getFormat()"""
        return str.__wrap(super(ObjectArrayMessage, self).getFormat())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectArrayMessage.toString()"""
        return str.__wrap(super(ObjectArrayMessage, self).toString())

    @overload
    def __init__(self, *obj: object):
        """public org.apache.logging.log4j.message.ObjectArrayMessage(java.lang.Object...)"""
        val = __ObjectArrayMessage(obj)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ObjectArrayMessage.hashCode()"""
        return int.__wrap(super(ObjectArrayMessage, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedMessageFactory
from builtins import str
import org.apache.logging.log4j.message.ParameterizedMessageFactory as __ParameterizedMessageFactory
__ParameterizedMessageFactory = __ParameterizedMessageFactory
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParameterizedMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.ParameterizedMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __ParameterizedMessageFactory) -> 'ParameterizedMessageFactory':
        return ParameterizedMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterizedMessageFactory):
        """
        Dynamic initializer for ParameterizedMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ParameterizedMessageFactory()"""
        val = __ParameterizedMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, params))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
        """public org.apache.logging.log4j.message.ParameterizedMessageFactory()"""
        val = __ParameterizedMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__ParameterizedMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4)) 
 
 
# CLASS: org.apache.logging.log4j.message.Message
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class Message(ABC, __Serializable, Serializable):
    """org.apache.logging.log4j.message.Message"""
 
    @staticmethod
    def __wrap(java_value: __Message) -> 'Message':
        return Message(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Message):
        """
        Dynamic initializer for Message.
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
 
 
# CLASS: org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory as __ParameterizedNoReferenceMessageFactory
__ParameterizedNoReferenceMessageFactory = __ParameterizedNoReferenceMessageFactory
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParameterizedNoReferenceMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __ParameterizedNoReferenceMessageFactory) -> 'ParameterizedNoReferenceMessageFactory':
        return ParameterizedNoReferenceMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterizedNoReferenceMessageFactory):
        """
        Dynamic initializer for ParameterizedNoReferenceMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory()"""
        val = __ParameterizedNoReferenceMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory()"""
        val = __ParameterizedNoReferenceMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ParameterizedNoReferenceMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__ParameterizedNoReferenceMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: org.apache.logging.log4j.message.ReusableParameterizedMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
import org.apache.logging.log4j.message.ReusableParameterizedMessage as __ReusableParameterizedMessage
__ReusableParameterizedMessage = __ReusableParameterizedMessage
from builtins import int
 
class ReusableParameterizedMessage(__ReusableMessage, ReusableMessage, __ParameterVisitable, ParameterVisitable, __Clearable, Clearable):
    """org.apache.logging.log4j.message.ReusableParameterizedMessage"""
 
    @staticmethod
    def __wrap(java_value: __ReusableParameterizedMessage) -> 'ReusableParameterizedMessage':
        return ReusableParameterizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReusableParameterizedMessage):
        """
        Dynamic initializer for ReusableParameterizedMessage.
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
        """public org.apache.logging.log4j.message.ReusableParameterizedMessage()"""
        val = __ReusableParameterizedMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.ReusableParameterizedMessage()"""
        val = __ReusableParameterizedMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def formatTo(self, builder: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ReusableParameterizedMessage.formatTo(java.lang.StringBuilder)"""
        super(__ReusableParameterizedMessage, self).formatTo(builder)

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
    def clear(self):
        """public void org.apache.logging.log4j.message.ReusableParameterizedMessage.clear()"""
        super(ReusableParameterizedMessage, self).clear()

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableParameterizedMessage.getParameters()"""
        return List[object].__wrap(super(ReusableParameterizedMessage, self).getParameters())

    @override
    @overload
    def memento(self) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.ReusableParameterizedMessage.memento()"""
        return 'Message'.__wrap(super(ReusableParameterizedMessage, self).memento())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public <S> void org.apache.logging.log4j.message.ReusableParameterizedMessage.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        super(__ReusableParameterizedMessage, self).forEachParameter(action, state)

    @overload
    def swapParameters(self, emptyReplacement: 'Object') -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ReusableParameterizedMessage.swapParameters(java.lang.Object[])"""
        return List[object].__wrap(super(__ReusableParameterizedMessage, self).swapParameters(emptyReplacement))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ReusableParameterizedMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ReusableParameterizedMessage, self).getThrowable())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.getFormattedMessage()"""
        return str.__wrap(super(ReusableParameterizedMessage, self).getFormattedMessage())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.toString()"""
        return str.__wrap(super(ReusableParameterizedMessage, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getParameterCount(self) -> int:
        """public short org.apache.logging.log4j.message.ReusableParameterizedMessage.getParameterCount()"""
        return int.__wrap(super(ReusableParameterizedMessage, self).getParameterCount())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ReusableParameterizedMessage.getFormat()"""
        return str.__wrap(super(ReusableParameterizedMessage, self).getFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.logging.log4j.message.LocalizedMessage
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.LocalizedMessage as __LocalizedMessage
__LocalizedMessage = __LocalizedMessage
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.util.ResourceBundle as ResourceBundle
from builtins import object
from typing import List
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
 
class LocalizedMessage(__Message, Message, __LoggerNameAwareMessage, LoggerNameAwareMessage):
    """org.apache.logging.log4j.message.LocalizedMessage"""
 
    @staticmethod
    def __wrap(java_value: __LocalizedMessage) -> 'LocalizedMessage':
        return LocalizedMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LocalizedMessage):
        """
        Dynamic initializer for LocalizedMessage.
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
    def __init__(self, baseName: str, locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(baseName, locale, key, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.LocalizedMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(LocalizedMessage, self).getThrowable())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getFormattedMessage()"""
        return str.__wrap(super(LocalizedMessage, self).getFormattedMessage())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getFormat()"""
        return str.__wrap(super(LocalizedMessage, self).getFormat())

    @overload
    def __init__(self, baseName: str, locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(baseName, locale, key, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(baseName, key, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(bundle, key, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(bundle, key, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(bundle, key, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, messagePattern: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(messagePattern, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(locale, key, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.toString()"""
        return str.__wrap(super(LocalizedMessage, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(locale, key, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(bundle, locale, key, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(locale, key, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(bundle, locale, key, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, key: str, arg: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object)"""
        val = __LocalizedMessage(baseName, key, arg)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, bundle: 'ResourceBundle', key: str):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.lang.String)"""
        val = __LocalizedMessage(bundle, key)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, messagePattern: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(messagePattern, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, bundle: 'ResourceBundle', locale: 'Locale', key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.util.ResourceBundle,java.util.Locale,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(bundle, locale, key, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, baseName: str, key: str, arg1: object, arg2: object):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.String,java.lang.Object,java.lang.Object)"""
        val = __LocalizedMessage(baseName, key, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setLoggerName(self, name: str):
        """public void org.apache.logging.log4j.message.LocalizedMessage.setLoggerName(java.lang.String)"""
        super(__LocalizedMessage, self).setLoggerName(name)

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.LocalizedMessage.getParameters()"""
        return List[object].__wrap(super(LocalizedMessage, self).getParameters())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, messagePattern: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(messagePattern, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLoggerName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.LocalizedMessage.getLoggerName()"""
        return str.__wrap(super(LocalizedMessage, self).getLoggerName())

    @overload
    def __init__(self, baseName: str, locale: 'Locale', key: str, arguments: 'Object'):
        """public org.apache.logging.log4j.message.LocalizedMessage(java.lang.String,java.util.Locale,java.lang.String,java.lang.Object[])"""
        val = __LocalizedMessage(baseName, locale, key, arguments)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.ObjectMessage
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import org.apache.logging.log4j.message.ObjectMessage as __ObjectMessage
__ObjectMessage = __ObjectMessage
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ObjectMessage(__Message, Message, log4py.__StringBuilderFormattable, util.StringBuilderFormattable):
    """org.apache.logging.log4j.message.ObjectMessage"""
 
    @staticmethod
    def __wrap(java_value: __ObjectMessage) -> 'ObjectMessage':
        return ObjectMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectMessage):
        """
        Dynamic initializer for ObjectMessage.
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
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.ObjectMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__ObjectMessage, self).equals(o))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.ObjectMessage.hashCode()"""
        return int.__wrap(super(ObjectMessage, self).hashCode())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.getFormattedMessage()"""
        return str.__wrap(super(ObjectMessage, self).getFormattedMessage())

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.ObjectMessage.formatTo(java.lang.StringBuilder)"""
        super(__ObjectMessage, self).formatTo(buffer)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.ObjectMessage.getParameters()"""
        return List[object].__wrap(super(ObjectMessage, self).getParameters())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, obj: object):
        """public org.apache.logging.log4j.message.ObjectMessage(java.lang.Object)"""
        val = __ObjectMessage(obj)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.toString()"""
        return str.__wrap(super(ObjectMessage, self).toString())

    @overload
    def getParameter(self) -> object:
        """public java.lang.Object org.apache.logging.log4j.message.ObjectMessage.getParameter()"""
        return object.__wrap(super(ObjectMessage, self).getParameter())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.ObjectMessage.getFormat()"""
        return str.__wrap(super(ObjectMessage, self).getFormat())

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.ObjectMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(ObjectMessage, self).getThrowable()) 
 
 
# CLASS: org.apache.logging.log4j.message.MessageFormatMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.logging.log4j.message.MessageFormatMessageFactory as __MessageFormatMessageFactory
__MessageFormatMessageFactory = __MessageFormatMessageFactory
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class MessageFormatMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.MessageFormatMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __MessageFormatMessageFactory) -> 'MessageFormatMessageFactory':
        return MessageFormatMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MessageFormatMessageFactory):
        """
        Dynamic initializer for MessageFormatMessageFactory.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, params))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.MessageFormatMessageFactory()"""
        val = __MessageFormatMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.MessageFormatMessageFactory()"""
        val = __MessageFormatMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.MessageFormatMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__MessageFormatMessageFactory, self).newMessage(message, p0, p1, p2, p3)) 
 
 
# CLASS: org.apache.logging.log4j.message.ParameterVisitable
import org.apache.logging.log4j.message.ParameterVisitable as __ParameterVisitable
__ParameterVisitable = __ParameterVisitable
from abc import abstractmethod, ABC
 
class ParameterVisitable(ABC):
    """org.apache.logging.log4j.message.ParameterVisitable"""
 
    @staticmethod
    def __wrap(java_value: __ParameterVisitable) -> 'ParameterVisitable':
        return ParameterVisitable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterVisitable):
        """
        Dynamic initializer for ParameterVisitable.
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
    def forEachParameter(self, action: 'ParameterConsumer', state: object):
        """public abstract <S> void org.apache.logging.log4j.message.ParameterVisitable.forEachParameter(org.apache.logging.log4j.message.ParameterConsumer<S>,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.SimpleMessage
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import org.apache.logging.log4j.message.SimpleMessage as __SimpleMessage
__SimpleMessage = __SimpleMessage
from builtins import object
from typing import List
import java.util.stream.IntStream as __IntStream
__IntStream = __IntStream
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.CharSequence as __CharSequence
__CharSequence = __CharSequence
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.StringBuilder as StringBuilder
import java.lang.Integer as __int
import java.util.stream.IntStream as IntStream
from builtins import bool
from builtins import int
 
class SimpleMessage(__Message, Message, log4py.__StringBuilderFormattable, util.StringBuilderFormattable, __CharSequence, CharSequence):
    """org.apache.logging.log4j.message.SimpleMessage"""
 
    @staticmethod
    def __wrap(java_value: __SimpleMessage) -> 'SimpleMessage':
        return SimpleMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleMessage):
        """
        Dynamic initializer for SimpleMessage.
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
        """public org.apache.logging.log4j.message.SimpleMessage()"""
        val = __SimpleMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, message: str):
        """public org.apache.logging.log4j.message.SimpleMessage(java.lang.String)"""
        val = __SimpleMessage(message)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.toString()"""
        return str.__wrap(super(SimpleMessage, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.message.SimpleMessage.formatTo(java.lang.StringBuilder)"""
        super(__SimpleMessage, self).formatTo(buffer)

    @override
    @overload
    def getThrowable(self) -> 'Throwable':
        """public java.lang.Throwable org.apache.logging.log4j.message.SimpleMessage.getThrowable()"""
        return 'Throwable'.__wrap(super(SimpleMessage, self).getThrowable())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public default boolean java.lang.CharSequence.isEmpty()"""
        return bool.__wrap(super(CharSequence, self).isEmpty())

    @overload
    def subSequence(self, start: int, end: int) -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.message.SimpleMessage.subSequence(int,int)"""
        return 'CharSequence'.__wrap(super(__SimpleMessage, self).subSequence(__int.valueOf(start), __int.valueOf(end)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def length(self) -> int:
        """public int org.apache.logging.log4j.message.SimpleMessage.length()"""
        return int.__wrap(super(SimpleMessage, self).length())

    @override
    @overload
    def getFormattedMessage(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.getFormattedMessage()"""
        return str.__wrap(super(SimpleMessage, self).getFormattedMessage())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.message.SimpleMessage.hashCode()"""
        return int.__wrap(super(SimpleMessage, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def charAt(self, index: int) -> str:
        """public char org.apache.logging.log4j.message.SimpleMessage.charAt(int)"""
        return str.__wrap(super(__SimpleMessage, self).charAt(__int.valueOf(index)))

    @override
    @overload
    def codePoints(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.codePoints()"""
        return 'IntStream'.__wrap(super(CharSequence, self).codePoints())

    @override
    @overload
    def getFormat(self) -> str:
        """public java.lang.String org.apache.logging.log4j.message.SimpleMessage.getFormat()"""
        return str.__wrap(super(SimpleMessage, self).getFormat())

    @override
    @overload
    def chars(self) -> 'IntStream':
        """public default java.util.stream.IntStream java.lang.CharSequence.chars()"""
        return 'IntStream'.__wrap(super(CharSequence, self).chars())

    @overload
    def __init__(self, charSequence: 'CharSequence'):
        """public org.apache.logging.log4j.message.SimpleMessage(java.lang.CharSequence)"""
        val = __SimpleMessage(charSequence)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getParameters(self) -> List[object]:
        """public java.lang.Object[] org.apache.logging.log4j.message.SimpleMessage.getParameters()"""
        return List[object].__wrap(super(SimpleMessage, self).getParameters())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.message.SimpleMessage.equals(java.lang.Object)"""
        return bool.__wrap(super(__SimpleMessage, self).equals(o))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.message.SimpleMessage()"""
        val = __SimpleMessage()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.logging.log4j.message.StringFormatterMessageFactory
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import org.apache.logging.log4j.message.StringFormatterMessageFactory as __StringFormatterMessageFactory
__StringFormatterMessageFactory = __StringFormatterMessageFactory
import org.apache.logging.log4j.message.AbstractMessageFactory as __AbstractMessageFactory
__AbstractMessageFactory = __AbstractMessageFactory
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StringFormatterMessageFactory(__AbstractMessageFactory, AbstractMessageFactory):
    """org.apache.logging.log4j.message.StringFormatterMessageFactory"""
 
    @staticmethod
    def __wrap(java_value: __StringFormatterMessageFactory) -> 'StringFormatterMessageFactory':
        return StringFormatterMessageFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StringFormatterMessageFactory):
        """
        Dynamic initializer for StringFormatterMessageFactory.
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
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3))

    @overload
    def newMessage(self, message: str, p0: object, p1: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newMessage(self, message: str, p0: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0))

    @overload
    def newMessage(self, message: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.Object)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5))

    @overload
    def newMessage(self, message: str, *params: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object...)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, params))

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
    def newMessage(self, message: str) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.String)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7))

    @overload
    def newMessage(self, message: 'CharSequence') -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.AbstractMessageFactory.newMessage(java.lang.CharSequence)"""
        return 'Message'.__wrap(super(__AbstractMessageFactory, self).newMessage(message))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.message.StringFormatterMessageFactory()"""
        val = __StringFormatterMessageFactory()
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
    def __init__(self, ):
        """public org.apache.logging.log4j.message.StringFormatterMessageFactory()"""
        val = __StringFormatterMessageFactory()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6))

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newMessage(self, message: str, p0: object, p1: object, p2: object, p3: object, p4: object, p5: object, p6: object, p7: object, p8: object, p9: object) -> 'Message':
        """public org.apache.logging.log4j.message.Message org.apache.logging.log4j.message.StringFormatterMessageFactory.newMessage(java.lang.String,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object,java.lang.Object)"""
        return 'Message'.__wrap(super(__StringFormatterMessageFactory, self).newMessage(message, p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)) 
 
 
# CLASS: org.apache.logging.log4j.message.TimestampMessage
import org.apache.logging.log4j.message.TimestampMessage as __TimestampMessage
__TimestampMessage = __TimestampMessage
from abc import abstractmethod, ABC
 
class TimestampMessage(ABC):
    """org.apache.logging.log4j.message.TimestampMessage"""
 
    @staticmethod
    def __wrap(java_value: __TimestampMessage) -> 'TimestampMessage':
        return TimestampMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TimestampMessage):
        """
        Dynamic initializer for TimestampMessage.
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
    def getTimestamp(self, ):
        """public abstract long org.apache.logging.log4j.message.TimestampMessage.getTimestamp()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.message.StructuredDataMessage$Format
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
import org.apache.logging.log4j.message.StructuredDataMessage as __StructuredDataMessage_Format
__Format = __StructuredDataMessage_Format.Format
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
 
class Format(__Enum, Enum):
    """org.apache.logging.log4j.message.StructuredDataMessage.Format"""
 
    @staticmethod
    def __wrap(java_value: __Format) -> 'Format':
        return Format(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Format):
        """
        Dynamic initializer for Format.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['Format']:
        """public static org.apache.logging.log4j.message.StructuredDataMessage$Format[] org.apache.logging.log4j.message.StructuredDataMessage$Format.values()"""
        return List[Format].__wrap(__Format.values())

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
    def valueOf(name: str) -> 'Format':
        """public static org.apache.logging.log4j.message.StructuredDataMessage$Format org.apache.logging.log4j.message.StructuredDataMessage$Format.valueOf(java.lang.String)"""
        return Format.__wrap(__Format.valueOf(name)) 
 
 
# CLASS: org.apache.logging.log4j.message.EntryMessage
import org.apache.logging.log4j.message.EntryMessage as __EntryMessage
__EntryMessage = __EntryMessage
import org.apache.logging.log4j.message.FlowMessage as __FlowMessage
__FlowMessage = __FlowMessage
from abc import abstractmethod, ABC
import org.apache.logging.log4j.message.Message as __Message
__Message = __Message
 
class EntryMessage(ABC, __FlowMessage, FlowMessage):
    """org.apache.logging.log4j.message.EntryMessage"""
 
    @staticmethod
    def __wrap(java_value: __EntryMessage) -> 'EntryMessage':
        return EntryMessage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntryMessage):
        """
        Dynamic initializer for EntryMessage.
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