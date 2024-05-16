from __future__ import annotations
from overload import overload


 
import com.badlogic.ashley.signals.Listener as __Listener
__Listener = __Listener
from abc import abstractmethod, ABC
 
class Listener(ABC):
    """com.badlogic.ashley.signals.Listener"""
 
    @staticmethod
    def __wrap(java_value: __Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Listener):
        """
        Dynamic initializer for Listener.
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
    def receive(self, arg0: 'Signal', arg1: object):
        """public abstract void com.badlogic.ashley.signals.Listener.receive(com.badlogic.ashley.signals.Signal<T>,T)"""
        pass

 
 
 
# CLASS: com.badlogic.ashley.signals.Listener
import com.badlogic.ashley.signals.Listener as __Listener
__Listener = __Listener
from abc import abstractmethod, ABC
 
class Listener(ABC):
    """com.badlogic.ashley.signals.Listener"""
 
    @staticmethod
    def __wrap(java_value: __Listener) -> 'Listener':
        return Listener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Listener):
        """
        Dynamic initializer for Listener.
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
    def receive(self, arg0: 'Signal', arg1: object):
        """public abstract void com.badlogic.ashley.signals.Listener.receive(com.badlogic.ashley.signals.Signal<T>,T)"""
        pass

 
 
 
# CLASS: com.badlogic.ashley.signals.Listener 
 
 
# CLASS: com.badlogic.ashley.signals.Signal
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
import com.badlogic.ashley.signals.Signal as __Signal
__Signal = __Signal
from builtins import int
 
class Signal():
    """com.badlogic.ashley.signals.Signal"""
 
    @staticmethod
    def __wrap(java_value: __Signal) -> 'Signal':
        return Signal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Signal):
        """
        Dynamic initializer for Signal.
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
        """public com.badlogic.ashley.signals.Signal()"""
        val = __Signal()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'Listener'):
        """public void com.badlogic.ashley.signals.Signal.add(com.badlogic.ashley.signals.Listener<T>)"""
        super(__Signal, self).add(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.signals.Signal()"""
        val = __Signal()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeAllListeners(self):
        """public void com.badlogic.ashley.signals.Signal.removeAllListeners()"""
        super(Signal, self).removeAllListeners()

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
    def remove(self, arg0: 'Listener'):
        """public void com.badlogic.ashley.signals.Signal.remove(com.badlogic.ashley.signals.Listener<T>)"""
        super(__Signal, self).remove(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def dispatch(self, arg0: object):
        """public void com.badlogic.ashley.signals.Signal.dispatch(T)"""
        super(__Signal, self).dispatch(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))