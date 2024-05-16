from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.events.api.ValueEventResult as _ValueEventResult
_ValueEventResult = _ValueEventResult
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueEventResult():
    """dev.ultreon.quantum.events.api.ValueEventResult"""
 
    @staticmethod
    def _wrap(java_value: _ValueEventResult) -> 'ValueEventResult':
        return ValueEventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueEventResult):
        """
        Dynamic initializer for ValueEventResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueEventResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueEventResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: object):
        """public dev.ultreon.quantum.events.api.ValueEventResult(boolean,boolean,T)"""
        val = _ValueEventResult(_boolean.valueOf(arg0), _boolean.valueOf(arg1), arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def interruptCancel(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interruptCancel(T)"""
        return ValueEventResult._wrap(_ValueEventResult.interruptCancel(arg0))

    @staticmethod
    @overload
    def interrupt(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(T)"""
        return ValueEventResult._wrap(_ValueEventResult.interrupt(arg0))

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isCanceled()"""
        return bool._wrap(super(ValueEventResult, self).isCanceled())

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
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isInterrupted()"""
        return bool._wrap(super(ValueEventResult, self).isInterrupted())

    @staticmethod
    @overload
    def pass() -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.pass()"""
        return ValueEventResult._wrap(_ValueEventResult.pass())

    @staticmethod
    @overload
    def interrupt(arg0: bool, arg1: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(boolean,T)"""
        return ValueEventResult._wrap(_ValueEventResult.interrupt(_boolean.valueOf(arg0), arg1))

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

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.events.api.ValueEventResult.getValue()"""
        return object._wrap(super(ValueEventResult, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.events.api.ValueEventResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.events.api.ValueEventResult as _ValueEventResult
_ValueEventResult = _ValueEventResult
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ValueEventResult():
    """dev.ultreon.quantum.events.api.ValueEventResult"""
 
    @staticmethod
    def _wrap(java_value: _ValueEventResult) -> 'ValueEventResult':
        return ValueEventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ValueEventResult):
        """
        Dynamic initializer for ValueEventResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ValueEventResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ValueEventResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: object):
        """public dev.ultreon.quantum.events.api.ValueEventResult(boolean,boolean,T)"""
        val = _ValueEventResult(_boolean.valueOf(arg0), _boolean.valueOf(arg1), arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def interruptCancel(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interruptCancel(T)"""
        return ValueEventResult._wrap(_ValueEventResult.interruptCancel(arg0))

    @staticmethod
    @overload
    def interrupt(arg0: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(T)"""
        return ValueEventResult._wrap(_ValueEventResult.interrupt(arg0))

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isCanceled()"""
        return bool._wrap(super(ValueEventResult, self).isCanceled())

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
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.ValueEventResult.isInterrupted()"""
        return bool._wrap(super(ValueEventResult, self).isInterrupted())

    @staticmethod
    @overload
    def pass() -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.pass()"""
        return ValueEventResult._wrap(_ValueEventResult.pass())

    @staticmethod
    @overload
    def interrupt(arg0: bool, arg1: object) -> 'ValueEventResult':
        """public static <T> dev.ultreon.quantum.events.api.ValueEventResult<T> dev.ultreon.quantum.events.api.ValueEventResult.interrupt(boolean,T)"""
        return ValueEventResult._wrap(_ValueEventResult.interrupt(_boolean.valueOf(arg0), arg1))

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

    @overload
    def getValue(self) -> object:
        """public T dev.ultreon.quantum.events.api.ValueEventResult.getValue()"""
        return object._wrap(super(ValueEventResult, self).getValue())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.events.api.ValueEventResult 
 
 
# CLASS: dev.ultreon.quantum.events.api.Event$Factory
import dev.ultreon.quantum.events.api.Event as _Event_Factory
_Factory = _Event_Factory.Factory
from abc import abstractmethod, ABC
import java.util.List as List
 
class Factory():
    """dev.ultreon.quantum.events.api.Event.Factory"""
 
    @staticmethod
    def _wrap(java_value: _Factory) -> 'Factory':
        return Factory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Factory):
        """
        Dynamic initializer for Factory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Factory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Factory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def create(self, arg0: 'List'):
        """public abstract T dev.ultreon.quantum.events.api.Event$Factory.create(java.util.List<T>)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.events.api.Main
import dev.ultreon.quantum.events.api.Main as _Main
_Main = _Main
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Main():
    """dev.ultreon.quantum.events.api.Main"""
 
    @staticmethod
    def _wrap(java_value: _Main) -> 'Main':
        return Main(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Main):
        """
        Dynamic initializer for Main.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Main__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Main__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
        """public dev.ultreon.quantum.events.api.Main()"""
        val = _Main()
        self.__wrapper = val

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void dev.ultreon.quantum.events.api.Main.main(java.lang.String[])"""
        _Main.main(arg0)

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.events.api.Main()"""
        val = _Main()
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.events.api.EventResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.events.api.EventResult as _EventResult
_EventResult = _EventResult
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventResult():
    """dev.ultreon.quantum.events.api.EventResult"""
 
    @staticmethod
    def _wrap(java_value: _EventResult) -> 'EventResult':
        return EventResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventResult):
        """
        Dynamic initializer for EventResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def interrupt() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interrupt()"""
        return EventResult._wrap(_EventResult.interrupt())

    @overload
    def isCanceled(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.EventResult.isCanceled()"""
        return bool._wrap(super(EventResult, self).isCanceled())

    @overload
    def isInterrupted(self) -> bool:
        """public boolean dev.ultreon.quantum.events.api.EventResult.isInterrupted()"""
        return bool._wrap(super(EventResult, self).isInterrupted())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def interrupt(arg0: bool) -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interrupt(boolean)"""
        return EventResult._wrap(_EventResult.interrupt(_boolean.valueOf(arg0)))

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

    @staticmethod
    @overload
    def pass() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.pass()"""
        return EventResult._wrap(_EventResult.pass())

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
    def __init__(self, arg0: bool, arg1: bool):
        """public dev.ultreon.quantum.events.api.EventResult(boolean,boolean)"""
        val = _EventResult(_boolean.valueOf(arg0), _boolean.valueOf(arg1))
        self.__wrapper = val

    @staticmethod
    @overload
    def interruptCancel() -> 'EventResult':
        """public static dev.ultreon.quantum.events.api.EventResult dev.ultreon.quantum.events.api.EventResult.interruptCancel()"""
        return EventResult._wrap(_EventResult.interruptCancel())

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
 
 
# CLASS: dev.ultreon.quantum.events.api.Event
import dev.ultreon.quantum.events.api.Event as _Event
_Event = _Event
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Event():
    """dev.ultreon.quantum.events.api.Event"""
 
    @staticmethod
    def _wrap(java_value: _Event) -> 'Event':
        return Event(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Event):
        """
        Dynamic initializer for Event.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Event__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Event__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def subscribe(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.subscribe(T)"""
        super(_Event, self).subscribe(arg0)

    @overload
    def factory(self) -> object:
        """public T dev.ultreon.quantum.events.api.Event.factory()"""
        return object._wrap(super(Event, self).factory())

    @overload
    def unsubscribe(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.unsubscribe(T)"""
        super(_Event, self).unsubscribe(arg0)

    @overload
    def __init__(self, arg0: 'Factory'):
        """public dev.ultreon.quantum.events.api.Event(dev.ultreon.quantum.events.api.Event$Factory<T>)"""
        val = _Event(arg0)
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

    @staticmethod
    @overload
    def cancelable(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.cancelable(java.lang.Class<T>)"""
        return Event._wrap(_Event.cancelable(arg0))

    @staticmethod
    @overload
    def withResult(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withResult(java.lang.Class<T>)"""
        return Event._wrap(_Event.withResult(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def cancelable(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.cancelable(T...)"""
        return Event._wrap(_Event.cancelable(arg0))

    @overload
    def listen(self, arg0: object):
        """public void dev.ultreon.quantum.events.api.Event.listen(T)"""
        super(_Event, self).listen(arg0)

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
    def create(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.create(T...)"""
        return Event._wrap(_Event.create(arg0))

    @staticmethod
    @overload
    def withResult(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withResult(T...)"""
        return Event._wrap(_Event.withResult(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def withValue(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withValue(java.lang.Class<T>)"""
        return Event._wrap(_Event.withValue(arg0))

    @staticmethod
    @overload
    def of(arg0: 'Class') -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.of(java.lang.Class<T>)"""
        return Event._wrap(_Event.of(arg0))

    @staticmethod
    @overload
    def withValue(*arg0: object) -> 'Event':
        """public static <T> dev.ultreon.quantum.events.api.Event<T> dev.ultreon.quantum.events.api.Event.withValue(T...)"""
        return Event._wrap(_Event.withValue(arg0))

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