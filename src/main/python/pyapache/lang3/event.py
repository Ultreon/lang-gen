from __future__ import annotations
from overload import overload


 
import org.apache.commons.lang3.event.EventListenerSupport as _EventListenerSupport
_EventListenerSupport = _EventListenerSupport
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventListenerSupport():
    """org.apache.commons.lang3.event.EventListenerSupport"""
 
    @staticmethod
    def _wrap(java_value: _EventListenerSupport) -> 'EventListenerSupport':
        return EventListenerSupport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventListenerSupport):
        """
        Dynamic initializer for EventListenerSupport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventListenerSupport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventListenerSupport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addListener(self, arg0: object, arg1: bool):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L,boolean)"""
        super(_EventListenerSupport, self).addListener(arg0, _boolean.valueOf(arg1))

    @overload
    def fire(self) -> object:
        """public L org.apache.commons.lang3.event.EventListenerSupport.fire()"""
        return object._wrap(super(EventListenerSupport, self).fire())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>)"""
        val = _EventListenerSupport(arg0)
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

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'EventListenerSupport':
        """public static <T> org.apache.commons.lang3.event.EventListenerSupport<T> org.apache.commons.lang3.event.EventListenerSupport.create(java.lang.Class<T>)"""
        return EventListenerSupport._wrap(_EventListenerSupport.create(arg0))

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
    def getListeners(self) -> List[object]:
        """public L[] org.apache.commons.lang3.event.EventListenerSupport.getListeners()"""
        return List[object]._wrap(super(EventListenerSupport, self).getListeners())

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ClassLoader'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>,java.lang.ClassLoader)"""
        val = _EventListenerSupport(arg0, arg1)
        self.__wrapper = val

    @overload
    def addListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L)"""
        super(_EventListenerSupport, self).addListener(arg0)

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
    def removeListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.removeListener(L)"""
        super(_EventListenerSupport, self).removeListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport
import org.apache.commons.lang3.event.EventListenerSupport as _EventListenerSupport
_EventListenerSupport = _EventListenerSupport
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventListenerSupport():
    """org.apache.commons.lang3.event.EventListenerSupport"""
 
    @staticmethod
    def _wrap(java_value: _EventListenerSupport) -> 'EventListenerSupport':
        return EventListenerSupport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventListenerSupport):
        """
        Dynamic initializer for EventListenerSupport.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventListenerSupport__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventListenerSupport__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addListener(self, arg0: object, arg1: bool):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L,boolean)"""
        super(_EventListenerSupport, self).addListener(arg0, _boolean.valueOf(arg1))

    @overload
    def fire(self) -> object:
        """public L org.apache.commons.lang3.event.EventListenerSupport.fire()"""
        return object._wrap(super(EventListenerSupport, self).fire())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>)"""
        val = _EventListenerSupport(arg0)
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

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'EventListenerSupport':
        """public static <T> org.apache.commons.lang3.event.EventListenerSupport<T> org.apache.commons.lang3.event.EventListenerSupport.create(java.lang.Class<T>)"""
        return EventListenerSupport._wrap(_EventListenerSupport.create(arg0))

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
    def getListeners(self) -> List[object]:
        """public L[] org.apache.commons.lang3.event.EventListenerSupport.getListeners()"""
        return List[object]._wrap(super(EventListenerSupport, self).getListeners())

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ClassLoader'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>,java.lang.ClassLoader)"""
        val = _EventListenerSupport(arg0, arg1)
        self.__wrapper = val

    @overload
    def addListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L)"""
        super(_EventListenerSupport, self).addListener(arg0)

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
    def removeListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.removeListener(L)"""
        super(_EventListenerSupport, self).removeListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport 
 
 
# CLASS: org.apache.commons.lang3.event.EventUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.commons.lang3.event.EventUtils as _EventUtils
_EventUtils = _EventUtils
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EventUtils():
    """org.apache.commons.lang3.event.EventUtils"""
 
    @staticmethod
    def _wrap(java_value: _EventUtils) -> 'EventUtils':
        return EventUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EventUtils):
        """
        Dynamic initializer for EventUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EventUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EventUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def bindEventsToMethod(arg0: object, arg1: str, arg2: object, arg3: 'Class', *arg4: str):
        """public static <L> void org.apache.commons.lang3.event.EventUtils.bindEventsToMethod(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Class<L>,java.lang.String...)"""
        _EventUtils.bindEventsToMethod(arg0, arg1, arg2, arg3, arg4)

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

    @staticmethod
    @overload
    def addEventListener(arg0: object, arg1: 'Class', arg2: object):
        """public static <L> void org.apache.commons.lang3.event.EventUtils.addEventListener(java.lang.Object,java.lang.Class<L>,L)"""
        _EventUtils.addEventListener(arg0, arg1, arg2)

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
    def __init__(self, ):
        """public org.apache.commons.lang3.event.EventUtils()"""
        val = _EventUtils()
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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.event.EventUtils()"""
        val = _EventUtils()
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport$ProxyInvocationHandler
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.event.EventListenerSupport as _EventListenerSupport_ProxyInvocationHandler
_ProxyInvocationHandler = _EventListenerSupport_ProxyInvocationHandler.ProxyInvocationHandler
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
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
 
class ProxyInvocationHandler():
    """org.apache.commons.lang3.event.EventListenerSupport.ProxyInvocationHandler"""
 
    @staticmethod
    def _wrap(java_value: _ProxyInvocationHandler) -> 'ProxyInvocationHandler':
        return ProxyInvocationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProxyInvocationHandler):
        """
        Dynamic initializer for ProxyInvocationHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProxyInvocationHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProxyInvocationHandler__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def invoke(self, arg0: object, arg1: 'Method', arg2: 'Object') -> object:
        """public java.lang.Object org.apache.commons.lang3.event.EventListenerSupport$ProxyInvocationHandler.invoke(java.lang.Object,java.lang.reflect.Method,java.lang.Object[]) throws java.lang.IllegalAccessException,java.lang.IllegalArgumentException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(super(_ProxyInvocationHandler, self).invoke(arg0, arg1, arg2))

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