from __future__ import annotations
from overload import overload


 
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
import dev.ultreon.libs.commons.v0.tuple.Quadruple as __Quadruple
__Quadruple = __Quadruple
from builtins import bool
from builtins import int
 
class Quadruple():
    """dev.ultreon.libs.commons.v0.tuple.Quadruple"""
 
    @staticmethod
    def __wrap(java_value: __Quadruple) -> 'Quadruple':
        return Quadruple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Quadruple):
        """
        Dynamic initializer for Quadruple.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Quadruple.toString()"""
        return str.__wrap(super(Quadruple, self).toString())

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFirst()"""
        return object.__wrap(super(Quadruple, self).getFirst())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Quadruple.getThird()"""
        return object.__wrap(super(Quadruple, self).getThird())

    @overload
    def getFourth(self) -> object:
        """public T4 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFourth()"""
        return object.__wrap(super(Quadruple, self).getFourth())

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setThird(T3)"""
        super(__Quadruple, self).setThird(arg0)

    @overload
    def setFourth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFourth(T4)"""
        super(__Quadruple, self).setFourth(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Quadruple.getSecond()"""
        return object.__wrap(super(Quadruple, self).getSecond())

    @overload
    def clone(self) -> 'Quadruple':
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple<T1, T2, T3, T4> dev.ultreon.libs.commons.v0.tuple.Quadruple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Quadruple'.__wrap(super(Quadruple, self).clone())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Quadruple.hashCode()"""
        return int.__wrap(super(Quadruple, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFirst(T1)"""
        super(__Quadruple, self).setFirst(arg0)

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
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple(T1,T2,T3,T4)"""
        val = __Quadruple(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Quadruple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Quadruple, self).equals(arg0))

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setSecond(T2)"""
        super(__Quadruple, self).setSecond(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Quadruple
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
import dev.ultreon.libs.commons.v0.tuple.Quadruple as __Quadruple
__Quadruple = __Quadruple
from builtins import bool
from builtins import int
 
class Quadruple():
    """dev.ultreon.libs.commons.v0.tuple.Quadruple"""
 
    @staticmethod
    def __wrap(java_value: __Quadruple) -> 'Quadruple':
        return Quadruple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Quadruple):
        """
        Dynamic initializer for Quadruple.
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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Quadruple.toString()"""
        return str.__wrap(super(Quadruple, self).toString())

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFirst()"""
        return object.__wrap(super(Quadruple, self).getFirst())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Quadruple.getThird()"""
        return object.__wrap(super(Quadruple, self).getThird())

    @overload
    def getFourth(self) -> object:
        """public T4 dev.ultreon.libs.commons.v0.tuple.Quadruple.getFourth()"""
        return object.__wrap(super(Quadruple, self).getFourth())

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setThird(T3)"""
        super(__Quadruple, self).setThird(arg0)

    @overload
    def setFourth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFourth(T4)"""
        super(__Quadruple, self).setFourth(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Quadruple.getSecond()"""
        return object.__wrap(super(Quadruple, self).getSecond())

    @overload
    def clone(self) -> 'Quadruple':
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple<T1, T2, T3, T4> dev.ultreon.libs.commons.v0.tuple.Quadruple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Quadruple'.__wrap(super(Quadruple, self).clone())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Quadruple.hashCode()"""
        return int.__wrap(super(Quadruple, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setFirst(T1)"""
        super(__Quadruple, self).setFirst(arg0)

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
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object):
        """public dev.ultreon.libs.commons.v0.tuple.Quadruple(T1,T2,T3,T4)"""
        val = __Quadruple(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Quadruple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Quadruple, self).equals(arg0))

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quadruple.setSecond(T2)"""
        super(__Quadruple, self).setSecond(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Quadruple 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Triple
import dev.ultreon.libs.commons.v0.tuple.Triple as __Triple
__Triple = __Triple
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
 
class Triple():
    """dev.ultreon.libs.commons.v0.tuple.Triple"""
 
    @staticmethod
    def __wrap(java_value: __Triple) -> 'Triple':
        return Triple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Triple):
        """
        Dynamic initializer for Triple.
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
    def clone(self) -> 'Triple':
        """public dev.ultreon.libs.commons.v0.tuple.Triple<T1, T2, T3> dev.ultreon.libs.commons.v0.tuple.Triple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Triple'.__wrap(super(Triple, self).clone())

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Triple.getThird()"""
        return object.__wrap(super(Triple, self).getThird())

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setFirst(T1)"""
        super(__Triple, self).setFirst(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Triple.toString()"""
        return str.__wrap(super(Triple, self).toString())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setSecond(T2)"""
        super(__Triple, self).setSecond(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Triple.getSecond()"""
        return object.__wrap(super(Triple, self).getSecond())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Triple.hashCode()"""
        return int.__wrap(super(Triple, self).hashCode())

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
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Triple.getFirst()"""
        return object.__wrap(super(Triple, self).getFirst())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Triple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Triple, self).equals(arg0))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object):
        """public dev.ultreon.libs.commons.v0.tuple.Triple(T1,T2,T3)"""
        val = __Triple(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Triple.setThird(T3)"""
        super(__Triple, self).setThird(arg0) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Quintuple
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.commons.v0.tuple.Quintuple as __Quintuple
__Quintuple = __Quintuple
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
 
class Quintuple():
    """dev.ultreon.libs.commons.v0.tuple.Quintuple"""
 
    @staticmethod
    def __wrap(java_value: __Quintuple) -> 'Quintuple':
        return Quintuple(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Quintuple):
        """
        Dynamic initializer for Quintuple.
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
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Quintuple.getSecond()"""
        return object.__wrap(super(Quintuple, self).getSecond())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setThird(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setThird(T3)"""
        super(__Quintuple, self).setThird(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Quintuple.equals(java.lang.Object)"""
        return bool.__wrap(super(__Quintuple, self).equals(arg0))

    @overload
    def getFourth(self) -> object:
        """public T4 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFourth()"""
        return object.__wrap(super(Quintuple, self).getFourth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFourth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFourth(T4)"""
        super(__Quintuple, self).setFourth(arg0)

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFirst(T1)"""
        super(__Quintuple, self).setFirst(arg0)

    @overload
    def clone(self) -> 'Quintuple':
        """public dev.ultreon.libs.commons.v0.tuple.Quintuple<T1, T2, T3, T4, T5> dev.ultreon.libs.commons.v0.tuple.Quintuple.clone() throws java.lang.CloneNotSupportedException"""
        return 'Quintuple'.__wrap(super(Quintuple, self).clone())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setSecond(T2)"""
        super(__Quintuple, self).setSecond(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getThird(self) -> object:
        """public T3 dev.ultreon.libs.commons.v0.tuple.Quintuple.getThird()"""
        return object.__wrap(super(Quintuple, self).getThird())

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
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFirst()"""
        return object.__wrap(super(Quintuple, self).getFirst())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Quintuple.hashCode()"""
        return int.__wrap(super(Quintuple, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Quintuple.toString()"""
        return str.__wrap(super(Quintuple, self).toString())

    @overload
    def setFifth(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Quintuple.setFifth(T5)"""
        super(__Quintuple, self).setFifth(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object):
        """public dev.ultreon.libs.commons.v0.tuple.Quintuple(T1,T2,T3,T4,T5)"""
        val = __Quintuple(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFifth(self) -> object:
        """public T5 dev.ultreon.libs.commons.v0.tuple.Quintuple.getFifth()"""
        return object.__wrap(super(Quintuple, self).getFifth()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Pair
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Pair as __Pair
__Pair = __Pair
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
 
class Pair():
    """dev.ultreon.libs.commons.v0.tuple.Pair"""
 
    @staticmethod
    def __wrap(java_value: __Pair) -> 'Pair':
        return Pair(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Pair):
        """
        Dynamic initializer for Pair.
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
    def getSecond(self) -> object:
        """public T2 dev.ultreon.libs.commons.v0.tuple.Pair.getSecond()"""
        return object.__wrap(super(Pair, self).getSecond())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: object):
        """public dev.ultreon.libs.commons.v0.tuple.Pair(T1,T2)"""
        val = __Pair(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setFirst(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Pair.setFirst(T1)"""
        super(__Pair, self).setFirst(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Pair.equals(java.lang.Object)"""
        return bool.__wrap(super(__Pair, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setSecond(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Pair.setSecond(T2)"""
        super(__Pair, self).setSecond(arg0)

    @overload
    def clone(self) -> 'Pair':
        """public dev.ultreon.libs.commons.v0.tuple.Pair<T1, T2> dev.ultreon.libs.commons.v0.tuple.Pair.clone() throws java.lang.CloneNotSupportedException"""
        return 'Pair'.__wrap(super(Pair, self).clone())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Pair.toString()"""
        return str.__wrap(super(Pair, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Pair.hashCode()"""
        return int.__wrap(super(Pair, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFirst(self) -> object:
        """public T1 dev.ultreon.libs.commons.v0.tuple.Pair.getFirst()"""
        return object.__wrap(super(Pair, self).getFirst()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.tuple.Singleton
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import dev.ultreon.libs.commons.v0.tuple.Singleton as __Singleton
__Singleton = __Singleton
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
 
class Singleton():
    """dev.ultreon.libs.commons.v0.tuple.Singleton"""
 
    @staticmethod
    def __wrap(java_value: __Singleton) -> 'Singleton':
        return Singleton(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Singleton):
        """
        Dynamic initializer for Singleton.
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
    def set(self, arg0: object):
        """public void dev.ultreon.libs.commons.v0.tuple.Singleton.set(T)"""
        super(__Singleton, self).set(arg0)

    @overload
    def get(self) -> object:
        """public T dev.ultreon.libs.commons.v0.tuple.Singleton.get()"""
        return object.__wrap(super(Singleton, self).get())

    @overload
    def __init__(self, arg0: object):
        """public dev.ultreon.libs.commons.v0.tuple.Singleton(T)"""
        val = __Singleton(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.tuple.Singleton.equals(java.lang.Object)"""
        return bool.__wrap(super(__Singleton, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def clone(self) -> 'Singleton':
        """public dev.ultreon.libs.commons.v0.tuple.Singleton<T> dev.ultreon.libs.commons.v0.tuple.Singleton.clone() throws java.lang.CloneNotSupportedException"""
        return 'Singleton'.__wrap(super(Singleton, self).clone())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.tuple.Singleton.toString()"""
        return str.__wrap(super(Singleton, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.tuple.Singleton.hashCode()"""
        return int.__wrap(super(Singleton, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()