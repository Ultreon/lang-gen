from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import dev.ultreon.libs.commons.v0.tuple.Triple as _Triple
_Triple = _Triple
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
 
class Triple():
    """dev.ultreon.libs.commons.v0.tuple.Triple"""
 
    @staticmethod
    def _wrap(java_value: _Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Triple):
        """
        Dynamic initializer for Triple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Triple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Triple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setFirst(T1)"""
        super(_Triple, self).setFirst(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Triple.getFirst()"""
        return object._wrap(super(Triple, self).getFirst())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setThird(T3)"""
        super(_Triple, self).setThird(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Triple.getThird()"""
        return object._wrap(super(Triple, self).getThird())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setSecond(T2)"""
        super(_Triple, self).setSecond(arg0)

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
    def clone(self) -> 'Triple':
        """public dev.ultreon.libs.commons.v0.tuple.Triple<T1, T2, T3> dev.ultreon.libs.commons.v0.tuple.Triple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Triple'._wrap(super(Triple, self).clone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.commons.v0.tuple.Triple(T1,T2,T3)"""
        val = _Triple(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Triple.getSecond()"""
        return object._wrap(super(Triple, self).getSecond())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Triple
from builtins import str
from pyquantum_helper import override
import dev.ultreon.libs.commons.v0.tuple.Triple as _Triple
_Triple = _Triple
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
 
class Triple():
    """dev.ultreon.libs.commons.v0.tuple.Triple"""
 
    @staticmethod
    def _wrap(java_value: _Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Triple):
        """
        Dynamic initializer for Triple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Triple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Triple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setFirst(T1)"""
        super(_Triple, self).setFirst(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Triple.equals(java.lang.Object)"""
        return bool._wrap(super(_Triple, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Triple.hashCode()"""
        return int._wrap(super(Triple, self).hashCode())

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Triple.getFirst()"""
        return object._wrap(super(Triple, self).getFirst())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setThird(T3)"""
        super(_Triple, self).setThird(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Triple.getThird()"""
        return object._wrap(super(Triple, self).getThird())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setSecond(T2)"""
        super(_Triple, self).setSecond(arg0)

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
    def clone(self) -> 'Triple':
        """public dev.ultreon.libs.commons.v0.tuple.Triple<T1, T2, T3> dev.ultreon.libs.commons.v0.tuple.Triple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Triple'._wrap(super(Triple, self).clone())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.commons.v0.tuple.Triple(T1,T2,T3)"""
        val = _Triple(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Triple.toString()"""
        return str._wrap(super(Triple, self).toString())

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Triple.getSecond()"""
        return object._wrap(super(Triple, self).getSecond())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Triple 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Quadruple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Quadruple as _Quadruple
_Quadruple = _Quadruple
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Quadruple():
    """dev.ultreon.libs.commons.v0.tuple.Quadruple"""
 
    @staticmethod
    def _wrap(java_value: _Quadruple) -> 'Quadruple':
        return Quadruple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Quadruple):
        """
        Dynamic initializer for Quadruple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Quadruple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Quadruple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFirst()"""
        return object._wrap(super(Quadruple, self).getFirst())

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFirst(T1)"""
        super(_Quadruple, self).setFirst(arg0)

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setSecond(T2)"""
        super(_Quadruple, self).setSecond(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Quadruple.getSecond()"""
        return object._wrap(super(Quadruple, self).getSecond())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Quadruple.toString()"""
        return str._wrap(super(Quadruple, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple(T1,T2,T3,T4)"""
        val = _Quadruple(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Quadruple.hashCode()"""
        return int._wrap(super(Quadruple, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Quadruple.equals(java.lang.Object)"""
        return bool._wrap(super(_Quadruple, self).equals(arg0))

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
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Quadruple.getThird()"""
        return object._wrap(super(Quadruple, self).getThird())

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setThird(T3)"""
        super(_Quadruple, self).setThird(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFourth(self) -> object:
        """public T4 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFourth()"""
        return object._wrap(super(Quadruple, self).getFourth())

    @overload
    def setFourth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFourth(T4)"""
        super(_Quadruple, self).setFourth(arg0)

    @overload
    def clone(self) -> 'Quadruple':
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple<T1, T2, T3, T4> dev.ultreon.libs.commons.v0.tuple.Quadruple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Quadruple'._wrap(super(Quadruple, self).clone()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Singleton
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.tuple.Singleton as _Singleton
_Singleton = _Singleton
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Singleton():
    """dev.ultreon.libs.commons.v0.tuple.Singleton"""
 
    @staticmethod
    def _wrap(java_value: _Singleton) -> 'Singleton':
        return Singleton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Singleton):
        """
        Dynamic initializer for Singleton.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Singleton__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Singleton__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.libs.commons.v0.tuple.Singleton(T)"""
        val = _Singleton(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Singleton.equals(java.lang.Object)"""
        return bool._wrap(super(_Singleton, self).equals(arg0))

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
    def set(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Singleton.set(T)"""
        super(_Singleton, self).set(arg0)

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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Singleton.hashCode()"""
        return int._wrap(super(Singleton, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def clone(self) -> 'Singleton':
        """public dev.ultreon.libs.commons.v0.tuple.Singleton<T> dev.ultreon.libs.commons.v0.tuple.Singleton.clone() throws java.lang.CloneNotSupportedException"""
        return 'Singleton'._wrap(super(Singleton, self).clone())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Singleton.toString()"""
        return str._wrap(super(Singleton, self).toString())

    @overload
    def get(self) -> object:
        """public T dev.ultreon.libs.commons.v0.tuple.Singleton.get()"""
        return object._wrap(super(Singleton, self).get()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Quintuple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.tuple.Quintuple as _Quintuple
_Quintuple = _Quintuple
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Quintuple():
    """dev.ultreon.libs.commons.v0.tuple.Quintuple"""
 
    @staticmethod
    def _wrap(java_value: _Quintuple) -> 'Quintuple':
        return Quintuple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Quintuple):
        """
        Dynamic initializer for Quintuple.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Quintuple__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Quintuple__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def clone(self) -> 'Quintuple':
        """public dev.ultreon.libs.commons.v0.tuple.Quintuple<T1, T2, T3, T4, T5> dev.ultreon.libs.commons.v0.tuple.Quintuple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Quintuple'._wrap(super(Quintuple, self).clone())

    @overload
    def getFifth(self) -> object:
        """public T5 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFifth()"""
        return object._wrap(super(Quintuple, self).getFifth())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setSecond(T2)"""
        super(_Quintuple, self).setSecond(arg0)

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFirst()"""
        return object._wrap(super(Quintuple, self).getFirst())

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
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setThird(T3)"""
        super(_Quintuple, self).setThird(arg0)

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Quintuple.getSecond()"""
        return object._wrap(super(Quintuple, self).getSecond())

    @overload
    def setFifth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFifth(T5)"""
        super(_Quintuple, self).setFifth(arg0)

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFirst(T1)"""
        super(_Quintuple, self).setFirst(arg0)

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
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object):
        """public dev.ultreon.libs.commons.v0.tuple.Quintuple(T1,T2,T3,T4,T5)"""
        val = _Quintuple(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Quintuple.equals(java.lang.Object)"""
        return bool._wrap(super(_Quintuple, self).equals(arg0))

    @overload
    def getFourth(self) -> object:
        """public T4 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFourth()"""
        return object._wrap(super(Quintuple, self).getFourth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Quintuple.toString()"""
        return str._wrap(super(Quintuple, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Quintuple.hashCode()"""
        return int._wrap(super(Quintuple, self).hashCode())

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Quintuple.getThird()"""
        return object._wrap(super(Quintuple, self).getThird())

    @overload
    def setFourth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFourth(T4)"""
        super(_Quintuple, self).setFourth(arg0) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.libs.commons.v0.tuple.Pair as _Pair
_Pair = _Pair
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Pair():
    """dev.ultreon.libs.commons.v0.tuple.Pair"""
 
    @staticmethod
    def _wrap(java_value: _Pair) -> 'Pair':
        return Pair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Pair):
        """
        Dynamic initializer for Pair.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Pair__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Pair__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: object):
        """public dev.ultreon.libs.commons.v0.tuple.Pair(T1,T2)"""
        val = _Pair(arg0, arg1)
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
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Pair.toString()"""
        return str._wrap(super(Pair, self).toString())

    @overload
    def clone(self) -> 'Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<T1, T2> dev.ultreon.libs.commons.v0.tuple.Pair.clone() throws java.lang.CloneNotSupportedException"""
        return 'Pair'._wrap(super(Pair, self).clone())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Pair.hashCode()"""
        return int._wrap(super(Pair, self).hashCode())

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Pair.getFirst()"""
        return object._wrap(super(Pair, self).getFirst())

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Pair.getSecond()"""
        return object._wrap(super(Pair, self).getSecond())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Pair.setFirst(T1)"""
        super(_Pair, self).setFirst(arg0)

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Pair.setSecond(T2)"""
        super(_Pair, self).setSecond(arg0)

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Pair.equals(java.lang.Object)"""
        return bool._wrap(super(_Pair, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()