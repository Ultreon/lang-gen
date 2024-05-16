from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import org.apache.commons.lang3.event.EventListenerSupport as __EventListenerSupport
__EventListenerSupport = __EventListenerSupport
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventListenerSupport():
    """org.apache.commons.lang3.event.EventListenerSupport"""
 
    @staticmethod
    def __wrap(java_value: __EventListenerSupport) -> 'EventListenerSupport':
        return EventListenerSupport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventListenerSupport):
        """
        Dynamic initializer for EventListenerSupport.
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
    def fire(self) -> object:
        """public L org.apache.commons.lang3.event.EventListenerSupport.fire()"""
        return object.__wrap(super(EventListenerSupport, self).fire())

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

    @overload
    def addListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L)"""
        super(__EventListenerSupport, self).addListener(arg0)

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'EventListenerSupport':
        """public static <T> org.apache.commons.lang3.event.EventListenerSupport<T> org.apache.commons.lang3.event.EventListenerSupport.create(java.lang.Class<T>)"""
        return EventListenerSupport.__wrap(__EventListenerSupport.create(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>)"""
        val = __EventListenerSupport(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.removeListener(L)"""
        super(__EventListenerSupport, self).removeListener(arg0)

    @overload
    def getListeners(self) -> List[object]:
        """public L[] org.apache.commons.lang3.event.EventListenerSupport.getListeners()"""
        return List[object].__wrap(super(EventListenerSupport, self).getListeners())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addListener(self, arg0: object, arg1: bool):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L,boolean)"""
        super(__EventListenerSupport, self).addListener(arg0, __boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ClassLoader'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>,java.lang.ClassLoader)"""
        val = __EventListenerSupport(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import org.apache.commons.lang3.event.EventListenerSupport as __EventListenerSupport
__EventListenerSupport = __EventListenerSupport
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.ClassLoader as ClassLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventListenerSupport():
    """org.apache.commons.lang3.event.EventListenerSupport"""
 
    @staticmethod
    def __wrap(java_value: __EventListenerSupport) -> 'EventListenerSupport':
        return EventListenerSupport(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventListenerSupport):
        """
        Dynamic initializer for EventListenerSupport.
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
    def fire(self) -> object:
        """public L org.apache.commons.lang3.event.EventListenerSupport.fire()"""
        return object.__wrap(super(EventListenerSupport, self).fire())

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

    @overload
    def addListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L)"""
        super(__EventListenerSupport, self).addListener(arg0)

    @staticmethod
    @overload
    def create(arg0: 'Class') -> 'EventListenerSupport':
        """public static <T> org.apache.commons.lang3.event.EventListenerSupport<T> org.apache.commons.lang3.event.EventListenerSupport.create(java.lang.Class<T>)"""
        return EventListenerSupport.__wrap(__EventListenerSupport.create(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Class'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>)"""
        val = __EventListenerSupport(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def removeListener(self, arg0: object):
        """public void org.apache.commons.lang3.event.EventListenerSupport.removeListener(L)"""
        super(__EventListenerSupport, self).removeListener(arg0)

    @overload
    def getListeners(self) -> List[object]:
        """public L[] org.apache.commons.lang3.event.EventListenerSupport.getListeners()"""
        return List[object].__wrap(super(EventListenerSupport, self).getListeners())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addListener(self, arg0: object, arg1: bool):
        """public void org.apache.commons.lang3.event.EventListenerSupport.addListener(L,boolean)"""
        super(__EventListenerSupport, self).addListener(arg0, __boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Class', arg1: 'ClassLoader'):
        """public org.apache.commons.lang3.event.EventListenerSupport(java.lang.Class<L>,java.lang.ClassLoader)"""
        val = __EventListenerSupport(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport 
 
 
# CLASS: org.apache.commons.lang3.event.EventListenerSupport$ProxyInvocationHandler
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
import org.apache.commons.lang3.event.EventListenerSupport as __EventListenerSupport_ProxyInvocationHandler
__ProxyInvocationHandler = __EventListenerSupport_ProxyInvocationHandler.ProxyInvocationHandler
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
from builtins import int
 
class ProxyInvocationHandler():
    """org.apache.commons.lang3.event.EventListenerSupport.ProxyInvocationHandler"""
 
    @staticmethod
    def __wrap(java_value: __ProxyInvocationHandler) -> 'ProxyInvocationHandler':
        return ProxyInvocationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProxyInvocationHandler):
        """
        Dynamic initializer for ProxyInvocationHandler.
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

    @overload
    def invoke(self, arg0: object, arg1: 'Method', arg2: 'Object') -> object:
        """public java.lang.Object org.apache.commons.lang3.event.EventListenerSupport$ProxyInvocationHandler.invoke(java.lang.Object,java.lang.reflect.Method,java.lang.Object[]) throws java.lang.IllegalAccessException,java.lang.IllegalArgumentException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(super(__ProxyInvocationHandler, self).invoke(arg0, arg1, arg2))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.event.EventUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.event.EventUtils as __EventUtils
__EventUtils = __EventUtils
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EventUtils():
    """org.apache.commons.lang3.event.EventUtils"""
 
    @staticmethod
    def __wrap(java_value: __EventUtils) -> 'EventUtils':
        return EventUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EventUtils):
        """
        Dynamic initializer for EventUtils.
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
    def addEventListener(arg0: object, arg1: 'Class', arg2: object):
        """public static <L> void org.apache.commons.lang3.event.EventUtils.addEventListener(java.lang.Object,java.lang.Class<L>,L)"""
        __EventUtils.addEventListener(arg0, arg1, arg2)

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.event.EventUtils()"""
        val = __EventUtils()
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

    @staticmethod
    @overload
    def bindEventsToMethod(arg0: object, arg1: str, arg2: object, arg3: 'Class', *arg4: str):
        """public static <L> void org.apache.commons.lang3.event.EventUtils.bindEventsToMethod(java.lang.Object,java.lang.String,java.lang.Object,java.lang.Class<L>,java.lang.String...)"""
        __EventUtils.bindEventsToMethod(arg0, arg1, arg2, arg3, arg4)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.event.EventUtils()"""
        val = __EventUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))