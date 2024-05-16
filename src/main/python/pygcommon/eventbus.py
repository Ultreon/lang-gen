from __future__ import annotations
from overload import overload


 
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import com.google.common.eventbus.Subscribe as __Subscribe
__Subscribe = __Subscribe
 
class Subscribe(ABC, __Annotation, Annotation):
    """com.google.common.eventbus.Subscribe"""
 
    @staticmethod
    def __wrap(java_value: __Subscribe) -> 'Subscribe':
        return Subscribe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Subscribe):
        """
        Dynamic initializer for Subscribe.
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

 
 
 
# CLASS: com.google.common.eventbus.Subscribe
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import com.google.common.eventbus.Subscribe as __Subscribe
__Subscribe = __Subscribe
 
class Subscribe(ABC, __Annotation, Annotation):
    """com.google.common.eventbus.Subscribe"""
 
    @staticmethod
    def __wrap(java_value: __Subscribe) -> 'Subscribe':
        return Subscribe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Subscribe):
        """
        Dynamic initializer for Subscribe.
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

 
 
 
# CLASS: com.google.common.eventbus.Subscribe 
 
 
# CLASS: com.google.common.eventbus.SubscriberExceptionContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.google.common.eventbus.EventBus as __EventBus
__EventBus = __EventBus
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.Object as __Object
__Object = __Object
import com.google.common.eventbus.SubscriberExceptionContext as __SubscriberExceptionContext
__SubscriberExceptionContext = __SubscriberExceptionContext
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
from builtins import int
 
class SubscriberExceptionContext():
    """com.google.common.eventbus.SubscriberExceptionContext"""
 
    @staticmethod
    def __wrap(java_value: __SubscriberExceptionContext) -> 'SubscriberExceptionContext':
        return SubscriberExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubscriberExceptionContext):
        """
        Dynamic initializer for SubscriberExceptionContext.
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
    def getSubscriberMethod(self) -> 'Method':
        """public java.lang.reflect.Method com.google.common.eventbus.SubscriberExceptionContext.getSubscriberMethod()"""
        return 'Method'.__wrap(super(SubscriberExceptionContext, self).getSubscriberMethod())

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

    @overload
    def getEventBus(self) -> 'EventBus':
        """public com.google.common.eventbus.EventBus com.google.common.eventbus.SubscriberExceptionContext.getEventBus()"""
        return 'EventBus'.__wrap(super(SubscriberExceptionContext, self).getEventBus())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getSubscriber(self) -> object:
        """public java.lang.Object com.google.common.eventbus.SubscriberExceptionContext.getSubscriber()"""
        return object.__wrap(super(SubscriberExceptionContext, self).getSubscriber())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getEvent(self) -> object:
        """public java.lang.Object com.google.common.eventbus.SubscriberExceptionContext.getEvent()"""
        return object.__wrap(super(SubscriberExceptionContext, self).getEvent())

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
 
 
# CLASS: com.google.common.eventbus.EventBus
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.eventbus.EventBus as __EventBus
__EventBus = __EventBus
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
 
class EventBus():
    """com.google.common.eventbus.EventBus"""
 
    @staticmethod
    def __wrap(java_value: __EventBus) -> 'EventBus':
        return EventBus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventBus):
        """
        Dynamic initializer for EventBus.
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
        """public com.google.common.eventbus.EventBus()"""
        val = __EventBus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.google.common.eventbus.EventBus()"""
        val = __EventBus()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def identifier(self) -> str:
        """public final java.lang.String com.google.common.eventbus.EventBus.identifier()"""
        return str.__wrap(super(EventBus, self).identifier())

    @overload
    def post(self, event: object):
        """public void com.google.common.eventbus.EventBus.post(java.lang.Object)"""
        super(__EventBus, self).post(event)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def register(self, object: object):
        """public void com.google.common.eventbus.EventBus.register(java.lang.Object)"""
        super(__EventBus, self).register(object)

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
    def __init__(self, identifier: str):
        """public com.google.common.eventbus.EventBus(java.lang.String)"""
        val = __EventBus(identifier)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, exceptionHandler: 'SubscriberExceptionHandler'):
        """public com.google.common.eventbus.EventBus(com.google.common.eventbus.SubscriberExceptionHandler)"""
        val = __EventBus(exceptionHandler)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.EventBus.toString()"""
        return str.__wrap(super(EventBus, self).toString())

    @overload
    def unregister(self, object: object):
        """public void com.google.common.eventbus.EventBus.unregister(java.lang.Object)"""
        super(__EventBus, self).unregister(object)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.eventbus.AllowConcurrentEvents
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.common.eventbus.AllowConcurrentEvents as __AllowConcurrentEvents
__AllowConcurrentEvents = __AllowConcurrentEvents
from abc import abstractmethod, ABC
 
class AllowConcurrentEvents(ABC, __Annotation, Annotation):
    """com.google.common.eventbus.AllowConcurrentEvents"""
 
    @staticmethod
    def __wrap(java_value: __AllowConcurrentEvents) -> 'AllowConcurrentEvents':
        return AllowConcurrentEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AllowConcurrentEvents):
        """
        Dynamic initializer for AllowConcurrentEvents.
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
 
 
# CLASS: com.google.common.eventbus.AsyncEventBus
from builtins import str
from pyquantum_helper import override
import com.google.common.eventbus.AsyncEventBus as __AsyncEventBus
__AsyncEventBus = __AsyncEventBus
import java.lang.Object as __object
from builtins import type
import java.util.concurrent.Executor as Executor
import com.google.common.eventbus.EventBus as __EventBus
__EventBus = __EventBus
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
 
class AsyncEventBus(__EventBus, EventBus):
    """com.google.common.eventbus.AsyncEventBus"""
 
    @staticmethod
    def __wrap(java_value: __AsyncEventBus) -> 'AsyncEventBus':
        return AsyncEventBus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AsyncEventBus):
        """
        Dynamic initializer for AsyncEventBus.
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
    def __init__(self, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor)"""
        val = __AsyncEventBus(executor)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def unregister(self, object: object):
        """public void com.google.common.eventbus.EventBus.unregister(java.lang.Object)"""
        super(__EventBus, self).unregister(object)

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
    def post(self, event: object):
        """public void com.google.common.eventbus.EventBus.post(java.lang.Object)"""
        super(__EventBus, self).post(event)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, identifier: str, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.lang.String,java.util.concurrent.Executor)"""
        val = __AsyncEventBus(identifier, executor)
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

    @overload
    def __init__(self, executor: 'Executor', subscriberExceptionHandler: 'SubscriberExceptionHandler'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor,com.google.common.eventbus.SubscriberExceptionHandler)"""
        val = __AsyncEventBus(executor, subscriberExceptionHandler)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.EventBus.toString()"""
        return str.__wrap(super(EventBus, self).toString())

    @override
    @overload
    def register(self, object: object):
        """public void com.google.common.eventbus.EventBus.register(java.lang.Object)"""
        super(__EventBus, self).register(object)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def identifier(self) -> str:
        """public final java.lang.String com.google.common.eventbus.EventBus.identifier()"""
        return str.__wrap(super(EventBus, self).identifier()) 
 
 
# CLASS: com.google.common.eventbus.DeadEvent
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.eventbus.DeadEvent as __DeadEvent
__DeadEvent = __DeadEvent
from builtins import object
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
 
class DeadEvent():
    """com.google.common.eventbus.DeadEvent"""
 
    @staticmethod
    def __wrap(java_value: __DeadEvent) -> 'DeadEvent':
        return DeadEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DeadEvent):
        """
        Dynamic initializer for DeadEvent.
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
    def getSource(self) -> object:
        """public java.lang.Object com.google.common.eventbus.DeadEvent.getSource()"""
        return object.__wrap(super(DeadEvent, self).getSource())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.DeadEvent.toString()"""
        return str.__wrap(super(DeadEvent, self).toString())

    @overload
    def getEvent(self) -> object:
        """public java.lang.Object com.google.common.eventbus.DeadEvent.getEvent()"""
        return object.__wrap(super(DeadEvent, self).getEvent())

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
    def __init__(self, source: object, event: object):
        """public com.google.common.eventbus.DeadEvent(java.lang.Object,java.lang.Object)"""
        val = __DeadEvent(source, event)
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
 
 
# CLASS: com.google.common.eventbus.SubscriberExceptionHandler
import java.lang.Throwable as Throwable
import com.google.common.eventbus.SubscriberExceptionHandler as __SubscriberExceptionHandler
__SubscriberExceptionHandler = __SubscriberExceptionHandler
from abc import abstractmethod, ABC
 
class SubscriberExceptionHandler(ABC):
    """com.google.common.eventbus.SubscriberExceptionHandler"""
 
    @staticmethod
    def __wrap(java_value: __SubscriberExceptionHandler) -> 'SubscriberExceptionHandler':
        return SubscriberExceptionHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SubscriberExceptionHandler):
        """
        Dynamic initializer for SubscriberExceptionHandler.
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
    def handleException(self, exception: 'Throwable', context: 'SubscriberExceptionContext'):
        """public abstract void com.google.common.eventbus.SubscriberExceptionHandler.handleException(java.lang.Throwable,com.google.common.eventbus.SubscriberExceptionContext)"""
        pass