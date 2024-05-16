from __future__ import annotations
from overload import overload


 
import com.google.common.eventbus.AsyncEventBus as _AsyncEventBus
_AsyncEventBus = _AsyncEventBus
from builtins import str
from pyquantum_helper import override
import com.google.common.eventbus.EventBus as _EventBus
_EventBus = _EventBus
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AsyncEventBus():
    """com.google.common.eventbus.AsyncEventBus"""
 
    @staticmethod
    def _wrap(java_value: _AsyncEventBus) -> 'AsyncEventBus':
        return AsyncEventBus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncEventBus):
        """
        Dynamic initializer for AsyncEventBus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncEventBus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncEventBus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def post(self, event: object):
        """public void com.google.common.eventbus.EventBus.post(java.lang.Object)"""
        super(_EventBus, self).post(event)

    @override
    @overload
    def identifier(self) -> str:
        """public final java.lang.String com.google.common.eventbus.EventBus.identifier()"""
        return str._wrap(super(EventBus, self).identifier())

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
    def register(self, object: object):
        """public void com.google.common.eventbus.EventBus.register(java.lang.Object)"""
        super(_EventBus, self).register(object)

    @overload
    def __init__(self, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor)"""
        val = _AsyncEventBus(executor)
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.EventBus.toString()"""
        return str._wrap(super(EventBus, self).toString())

    @overload
    def __init__(self, identifier: str, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.lang.String,java.util.concurrent.Executor)"""
        val = _AsyncEventBus(identifier, executor)
        self.__wrapper = val

    @overload
    def __init__(self, executor: 'Executor', subscriberExceptionHandler: 'SubscriberExceptionHandler'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor,com.google.common.eventbus.SubscriberExceptionHandler)"""
        val = _AsyncEventBus(executor, subscriberExceptionHandler)
        self.__wrapper = val

    @override
    @overload
    def unregister(self, object: object):
        """public void com.google.common.eventbus.EventBus.unregister(java.lang.Object)"""
        super(_EventBus, self).unregister(object)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.eventbus.AsyncEventBus
import com.google.common.eventbus.AsyncEventBus as _AsyncEventBus
_AsyncEventBus = _AsyncEventBus
from builtins import str
from pyquantum_helper import override
import com.google.common.eventbus.EventBus as _EventBus
_EventBus = _EventBus
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.concurrent.Executor as Executor
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AsyncEventBus():
    """com.google.common.eventbus.AsyncEventBus"""
 
    @staticmethod
    def _wrap(java_value: _AsyncEventBus) -> 'AsyncEventBus':
        return AsyncEventBus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AsyncEventBus):
        """
        Dynamic initializer for AsyncEventBus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AsyncEventBus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AsyncEventBus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def post(self, event: object):
        """public void com.google.common.eventbus.EventBus.post(java.lang.Object)"""
        super(_EventBus, self).post(event)

    @override
    @overload
    def identifier(self) -> str:
        """public final java.lang.String com.google.common.eventbus.EventBus.identifier()"""
        return str._wrap(super(EventBus, self).identifier())

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
    def register(self, object: object):
        """public void com.google.common.eventbus.EventBus.register(java.lang.Object)"""
        super(_EventBus, self).register(object)

    @overload
    def __init__(self, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor)"""
        val = _AsyncEventBus(executor)
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.EventBus.toString()"""
        return str._wrap(super(EventBus, self).toString())

    @overload
    def __init__(self, identifier: str, executor: 'Executor'):
        """public com.google.common.eventbus.AsyncEventBus(java.lang.String,java.util.concurrent.Executor)"""
        val = _AsyncEventBus(identifier, executor)
        self.__wrapper = val

    @overload
    def __init__(self, executor: 'Executor', subscriberExceptionHandler: 'SubscriberExceptionHandler'):
        """public com.google.common.eventbus.AsyncEventBus(java.util.concurrent.Executor,com.google.common.eventbus.SubscriberExceptionHandler)"""
        val = _AsyncEventBus(executor, subscriberExceptionHandler)
        self.__wrapper = val

    @override
    @overload
    def unregister(self, object: object):
        """public void com.google.common.eventbus.EventBus.unregister(java.lang.Object)"""
        super(_EventBus, self).unregister(object)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.eventbus.AsyncEventBus 
 
 
# CLASS: com.google.common.eventbus.DeadEvent
from builtins import str
import com.google.common.eventbus.DeadEvent as _DeadEvent
_DeadEvent = _DeadEvent
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DeadEvent():
    """com.google.common.eventbus.DeadEvent"""
 
    @staticmethod
    def _wrap(java_value: _DeadEvent) -> 'DeadEvent':
        return DeadEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DeadEvent):
        """
        Dynamic initializer for DeadEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DeadEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DeadEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSource(self) -> object:
        """public java.lang.Object com.google.common.eventbus.DeadEvent.getSource()"""
        return object._wrap(super(DeadEvent, self).getSource())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.DeadEvent.toString()"""
        return str._wrap(super(DeadEvent, self).toString())

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
    def __init__(self, source: object, event: object):
        """public com.google.common.eventbus.DeadEvent(java.lang.Object,java.lang.Object)"""
        val = _DeadEvent(source, event)
        self.__wrapper = val

    @overload
    def getEvent(self) -> object:
        """public java.lang.Object com.google.common.eventbus.DeadEvent.getEvent()"""
        return object._wrap(super(DeadEvent, self).getEvent())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.eventbus.SubscriberExceptionHandler
import com.google.common.eventbus.SubscriberExceptionHandler as _SubscriberExceptionHandler
_SubscriberExceptionHandler = _SubscriberExceptionHandler
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class SubscriberExceptionHandler():
    """com.google.common.eventbus.SubscriberExceptionHandler"""
 
    @staticmethod
    def _wrap(java_value: _SubscriberExceptionHandler) -> 'SubscriberExceptionHandler':
        return SubscriberExceptionHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubscriberExceptionHandler):
        """
        Dynamic initializer for SubscriberExceptionHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubscriberExceptionHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubscriberExceptionHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def handleException(self, exception: 'Throwable', context: 'SubscriberExceptionContext'):
        """public abstract void com.google.common.eventbus.SubscriberExceptionHandler.handleException(java.lang.Throwable,com.google.common.eventbus.SubscriberExceptionContext)"""
        pass 
 
 
# CLASS: com.google.common.eventbus.Subscribe
import com.google.common.eventbus.Subscribe as _Subscribe
_Subscribe = _Subscribe
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class Subscribe():
    """com.google.common.eventbus.Subscribe"""
 
    @staticmethod
    def _wrap(java_value: _Subscribe) -> 'Subscribe':
        return Subscribe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Subscribe):
        """
        Dynamic initializer for Subscribe.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Subscribe__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Subscribe__wrapper":
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
 
 
# CLASS: com.google.common.eventbus.AllowConcurrentEvents
import com.google.common.eventbus.AllowConcurrentEvents as _AllowConcurrentEvents
_AllowConcurrentEvents = _AllowConcurrentEvents
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class AllowConcurrentEvents():
    """com.google.common.eventbus.AllowConcurrentEvents"""
 
    @staticmethod
    def _wrap(java_value: _AllowConcurrentEvents) -> 'AllowConcurrentEvents':
        return AllowConcurrentEvents(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AllowConcurrentEvents):
        """
        Dynamic initializer for AllowConcurrentEvents.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AllowConcurrentEvents__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AllowConcurrentEvents__wrapper":
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
 
 
# CLASS: com.google.common.eventbus.SubscriberExceptionContext
import com.google.common.eventbus.SubscriberExceptionContext as _SubscriberExceptionContext
_SubscriberExceptionContext = _SubscriberExceptionContext
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.google.common.eventbus.EventBus as _EventBus
_EventBus = _EventBus
import java.lang.Object as _object
from builtins import type
import java.lang.reflect.Method as _Method
_Method = _Method
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Method as Method
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SubscriberExceptionContext():
    """com.google.common.eventbus.SubscriberExceptionContext"""
 
    @staticmethod
    def _wrap(java_value: _SubscriberExceptionContext) -> 'SubscriberExceptionContext':
        return SubscriberExceptionContext(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SubscriberExceptionContext):
        """
        Dynamic initializer for SubscriberExceptionContext.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SubscriberExceptionContext__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SubscriberExceptionContext__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getEventBus(self) -> 'EventBus':
        """public com.google.common.eventbus.EventBus com.google.common.eventbus.SubscriberExceptionContext.getEventBus()"""
        return 'EventBus'._wrap(super(SubscriberExceptionContext, self).getEventBus())

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
    def getSubscriber(self) -> object:
        """public java.lang.Object com.google.common.eventbus.SubscriberExceptionContext.getSubscriber()"""
        return object._wrap(super(SubscriberExceptionContext, self).getSubscriber())

    @overload
    def getEvent(self) -> object:
        """public java.lang.Object com.google.common.eventbus.SubscriberExceptionContext.getEvent()"""
        return object._wrap(super(SubscriberExceptionContext, self).getEvent())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSubscriberMethod(self) -> 'Method':
        """public java.lang.reflect.Method com.google.common.eventbus.SubscriberExceptionContext.getSubscriberMethod()"""
        return 'Method'._wrap(super(SubscriberExceptionContext, self).getSubscriberMethod())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.eventbus.EventBus
from builtins import str
from pyquantum_helper import override
import com.google.common.eventbus.EventBus as _EventBus
_EventBus = _EventBus
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventBus():
    """com.google.common.eventbus.EventBus"""
 
    @staticmethod
    def _wrap(java_value: _EventBus) -> 'EventBus':
        return EventBus(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventBus):
        """
        Dynamic initializer for EventBus.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventBus__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventBus__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def register(self, object: object):
        """public void com.google.common.eventbus.EventBus.register(java.lang.Object)"""
        super(_EventBus, self).register(object)

    @overload
    def identifier(self) -> str:
        """public final java.lang.String com.google.common.eventbus.EventBus.identifier()"""
        return str._wrap(super(EventBus, self).identifier())

    @overload
    def __init__(self):
        """public com.google.common.eventbus.EventBus()"""
        val = _EventBus()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.google.common.eventbus.EventBus()"""
        val = _EventBus()
        self.__wrapper = val

    @overload
    def unregister(self, object: object):
        """public void com.google.common.eventbus.EventBus.unregister(java.lang.Object)"""
        super(_EventBus, self).unregister(object)

    @overload
    def __init__(self, identifier: str):
        """public com.google.common.eventbus.EventBus(java.lang.String)"""
        val = _EventBus(identifier)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, exceptionHandler: 'SubscriberExceptionHandler'):
        """public com.google.common.eventbus.EventBus(com.google.common.eventbus.SubscriberExceptionHandler)"""
        val = _EventBus(exceptionHandler)
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
    def post(self, event: object):
        """public void com.google.common.eventbus.EventBus.post(java.lang.Object)"""
        super(_EventBus, self).post(event)

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.eventbus.EventBus.toString()"""
        return str._wrap(super(EventBus, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())