from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
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
import dev.ultreon.quantum.events.api.ValueEventResult as __ValueEventResult
__ValueEventResult = __ValueEventResult
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValueEventResult():
    """dev.ultreon.quantum.events.api.ValueEventResult"""
 
    @staticmethod
    def __wrap(java_value: __ValueEventResult) -> 'ValueEventResult':
        return ValueEventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueEventResult):
        """
        Dynamic initializer for ValueEventResult.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isInterrupted()"""
        return bool.__wrap(super(ValueEventResult, self).isInterrupted())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def interrupt(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interrupt(arg0))

    @staticmethod
    @overload
    def interrupt(arg0: bool, arg1: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(boolean,T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interrupt(__boolean.valueOf(arg0), arg1))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.events.api.ValueEventResult.getValue()"""
        return object.__wrap(super(ValueEventResult, self).getValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def interruptCancel(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interruptCancel(T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interruptCancel(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: object):
        """public dev.ultreon.quantum.events.api.ValueEventResult(boolean,boolean,T)"""
        val = __ValueEventResult(__boolean.valueOf(arg0), __boolean.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def pass() -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.pass()"""
        return ValueEventResult.__wrap(__ValueEventResult.pass())

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isCanceled()"""
        return bool.__wrap(super(ValueEventResult, self).isCanceled())

 
 
 
# CLASS: dev.ultreon.quantum.events.api.ValueEventResult
from builtins import str
import java.lang.Boolean as __boolean
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
import dev.ultreon.quantum.events.api.ValueEventResult as __ValueEventResult
__ValueEventResult = __ValueEventResult
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ValueEventResult():
    """dev.ultreon.quantum.events.api.ValueEventResult"""
 
    @staticmethod
    def __wrap(java_value: __ValueEventResult) -> 'ValueEventResult':
        return ValueEventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ValueEventResult):
        """
        Dynamic initializer for ValueEventResult.
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isInterrupted()"""
        return bool.__wrap(super(ValueEventResult, self).isInterrupted())

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def interrupt(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interrupt(arg0))

    @staticmethod
    @overload
    def interrupt(arg0: bool, arg1: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(boolean,T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interrupt(__boolean.valueOf(arg0), arg1))

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.events.api.ValueEventResult.getValue()"""
        return object.__wrap(super(ValueEventResult, self).getValue())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def interruptCancel(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interruptCancel(T)"""
        return ValueEventResult.__wrap(__ValueEventResult.interruptCancel(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: object):
        """public dev.ultreon.quantum.events.api.ValueEventResult(boolean,boolean,T)"""
        val = __ValueEventResult(__boolean.valueOf(arg0), __boolean.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def pass() -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.pass()"""
        return ValueEventResult.__wrap(__ValueEventResult.pass())

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isCanceled()"""
        return bool.__wrap(super(ValueEventResult, self).isCanceled())

 
 
 
# CLASS: dev.ultreon.quantum.events.api.ValueEventResult 
 
 
# CLASS: dev.ultreon.quantum.events.api.Event$Factory
from abc import abstractmethod, ABC
import dev.ultreon.quantum.events.api.Event as __Event_Factory
__Factory = __Event_Factory.Factory
import java.util.List as List
 
class Factory(ABC):
    """dev.ultreon.quantum.events.api.Event.Factory"""
 
    @staticmethod
    def __wrap(java_value: __Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Factory):
        """
        Dynamic initializer for Factory.
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
    def create(self, arg0: 'List'):
        """public abstract T dev.ultreon.quantum.events.api.Event$Factory.create(java.util.List<T>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.api.Main
import dev.ultreon.quantum.events.api.Main as __Main
__Main = __Main
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Main():
    """dev.ultreon.quantum.events.api.Main"""
 
    @staticmethod
    def __wrap(java_value: __Main) -> 'Main':
        return Main(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Main):
        """
        Dynamic initializer for Main.
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
    def __init__(self):
        """public dev.ultreon.quantum.events.api.Main()"""
        val = __Main()
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
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.events.api.Main()"""
        val = __Main()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.events.api.Main.main(java.lang.String[])"""
        __Main.main(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.events.api.EventResult
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.events.api.EventResult as __EventResult
__EventResult = __EventResult
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
 
class EventResult():
    """dev.ultreon.quantum.events.api.EventResult"""
 
    @staticmethod
    def __wrap(java_value: __EventResult) -> 'EventResult':
        return EventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventResult):
        """
        Dynamic initializer for EventResult.
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
    def interrupt() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interrupt()"""
        return EventResult.__wrap(__EventResult.interrupt())

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.EventResult.isCanceled()"""
        return bool.__wrap(super(EventResult, self).isCanceled())

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

    @staticmethod
    @overload
    def interrupt(arg0: bool) -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interrupt(boolean)"""
        return EventResult.__wrap(__EventResult.interrupt(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def pass() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.pass()"""
        return EventResult.__wrap(__EventResult.pass())

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
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.EventResult.isInterrupted()"""
        return bool.__wrap(super(EventResult, self).isInterrupted())

    @staticmethod
    @overload
    def interruptCancel() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interruptCancel()"""
        return EventResult.__wrap(__EventResult.interruptCancel())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: bool, arg1: bool):
        """public dev.ultreon.quantum.events.api.EventResult(boolean,boolean)"""
        val = __EventResult(__boolean.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.events.api.Event
import dev.ultreon.quantum.events.api.Event as __Event
__Event = __Event
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Event():
    """dev.ultreon.quantum.events.api.Event"""
 
    @staticmethod
    def __wrap(java_value: __Event) -> 'Event':
        return Event(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Event):
        """
        Dynamic initializer for Event.
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
    def listen(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.listen(T)"""
        super(__Event, self).listen(arg0)

    @overload
    def __init__(self, arg0: 'Factory'):
        """public dev.ultreon.quantum.events.api.Event(dev.ultreon.quantum.events.api.Event$Factory<T>)"""
        val = __Event(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def cancelable(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.cancelable(java.lang.Class<T>)"""
        return Event.__wrap(__Event.cancelable(arg0))

    @staticmethod
    @overload
    def withValue(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withValue(T...)"""
        return Event.__wrap(__Event.withValue(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def unsubscribe(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.unsubscribe(T)"""
        super(__Event, self).unsubscribe(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def withValue(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withValue(java.lang.Class<T>)"""
        return Event.__wrap(__Event.withValue(arg0))

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

    @staticmethod
    @overload
    def withResult(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withResult(T...)"""
        return Event.__wrap(__Event.withResult(arg0))

    @staticmethod
    @overload
    def create(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.create(T...)"""
        return Event.__wrap(__Event.create(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def withResult(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withResult(java.lang.Class<T>)"""
        return Event.__wrap(__Event.withResult(arg0))

    @overload
    def factory(self) -> object:
        """public T dev.ultreon.quantum.events.api.Event.factory()"""
        return object.__wrap(super(Event, self).factory())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.of(java.lang.Class<T>)"""
        return Event.__wrap(__Event.of(arg0))

    @staticmethod
    @overload
    def cancelable(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.cancelable(T...)"""
        return Event.__wrap(__Event.cancelable(arg0))

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
    def subscribe(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.subscribe(T)"""
        super(__Event, self).subscribe(arg0)