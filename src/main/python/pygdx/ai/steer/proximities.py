from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.RadiusProximity as __RadiusProximity
__RadiusProximity = __RadiusProximity
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as __ProximityBase
__ProximityBase = __ProximityBase
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class RadiusProximity():
    """com.badlogic.gdx.ai.steer.proximities.RadiusProximity"""
 
    @staticmethod
    def __wrap(java_value: __RadiusProximity) -> 'RadiusProximity':
        return RadiusProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RadiusProximity):
        """
        Dynamic initializer for RadiusProximity.
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
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__ProximityBase, self).setOwner(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(__ProximityBase, self).setAgents(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.RadiusProximity.setRadius(float)"""
        super(__RadiusProximity, self).setRadius(__float.valueOf(arg0))

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
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.RadiusProximity.getRadius()"""
        return float.__wrap(super(RadiusProximity, self).getRadius())

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.RadiusProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int.__wrap(super(__RadiusProximity, self).findNeighbors(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'.__wrap(super(ProximityBase, self).getAgents())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float):
        """public com.badlogic.gdx.ai.steer.proximities.RadiusProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float)"""
        val = __RadiusProximity(arg0, arg1, __float.valueOf(arg2))
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

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(ProximityBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.RadiusProximity
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.RadiusProximity as __RadiusProximity
__RadiusProximity = __RadiusProximity
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as __ProximityBase
__ProximityBase = __ProximityBase
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class RadiusProximity():
    """com.badlogic.gdx.ai.steer.proximities.RadiusProximity"""
 
    @staticmethod
    def __wrap(java_value: __RadiusProximity) -> 'RadiusProximity':
        return RadiusProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RadiusProximity):
        """
        Dynamic initializer for RadiusProximity.
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
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__ProximityBase, self).setOwner(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(__ProximityBase, self).setAgents(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.RadiusProximity.setRadius(float)"""
        super(__RadiusProximity, self).setRadius(__float.valueOf(arg0))

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
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.RadiusProximity.getRadius()"""
        return float.__wrap(super(RadiusProximity, self).getRadius())

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.RadiusProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int.__wrap(super(__RadiusProximity, self).findNeighbors(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'.__wrap(super(ProximityBase, self).getAgents())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float):
        """public com.badlogic.gdx.ai.steer.proximities.RadiusProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float)"""
        val = __RadiusProximity(arg0, arg1, __float.valueOf(arg2))
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

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(ProximityBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.RadiusProximity 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.ProximityBase
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
import com.badlogic.gdx.ai.steer.Proximity as __Proximity
__Proximity = __Proximity
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as __ProximityBase
__ProximityBase = __ProximityBase
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
from builtins import int
 
class ProximityBase(ABC):
    """com.badlogic.gdx.ai.steer.proximities.ProximityBase"""
 
    @staticmethod
    def __wrap(java_value: __ProximityBase) -> 'ProximityBase':
        return ProximityBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ProximityBase):
        """
        Dynamic initializer for ProximityBase.
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
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__ProximityBase, self).setOwner(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(__ProximityBase, self).setAgents(arg0)

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

    @abstractmethod
    def findNeighbors(self, arg0: 'ProximityCallback'):
        """public abstract int com.badlogic.gdx.ai.steer.Proximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'.__wrap(super(ProximityBase, self).getAgents())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable'):
        """public com.badlogic.gdx.ai.steer.proximities.ProximityBase(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        val = __ProximityBase(arg0, arg1)
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

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(ProximityBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.InfiniteProximity
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.InfiniteProximity as __InfiniteProximity
__InfiniteProximity = __InfiniteProximity
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as __ProximityBase
__ProximityBase = __ProximityBase
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class InfiniteProximity():
    """com.badlogic.gdx.ai.steer.proximities.InfiniteProximity"""
 
    @staticmethod
    def __wrap(java_value: __InfiniteProximity) -> 'InfiniteProximity':
        return InfiniteProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InfiniteProximity):
        """
        Dynamic initializer for InfiniteProximity.
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
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable'):
        """public com.badlogic.gdx.ai.steer.proximities.InfiniteProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        val = __InfiniteProximity(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__ProximityBase, self).setOwner(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(__ProximityBase, self).setAgents(arg0)

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

    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'.__wrap(super(ProximityBase, self).getAgents())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.InfiniteProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int.__wrap(super(__InfiniteProximity, self).findNeighbors(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(ProximityBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity as __FieldOfViewProximity
__FieldOfViewProximity = __FieldOfViewProximity
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as __ProximityBase
__ProximityBase = __ProximityBase
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class FieldOfViewProximity():
    """com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity"""
 
    @staticmethod
    def __wrap(java_value: __FieldOfViewProximity) -> 'FieldOfViewProximity':
        return FieldOfViewProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldOfViewProximity):
        """
        Dynamic initializer for FieldOfViewProximity.
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
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__ProximityBase, self).setOwner(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(__ProximityBase, self).setAgents(arg0)

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getAngle()"""
        return float.__wrap(super(FieldOfViewProximity, self).getAngle())

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int.__wrap(super(__FieldOfViewProximity, self).findNeighbors(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getRadius()"""
        return float.__wrap(super(FieldOfViewProximity, self).getRadius())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setAngle(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setAngle(float)"""
        super(__FieldOfViewProximity, self).setAngle(__float.valueOf(arg0))

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setRadius(float)"""
        super(__FieldOfViewProximity, self).setRadius(__float.valueOf(arg0))

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
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'.__wrap(super(ProximityBase, self).getAgents())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float,float)"""
        val = __FieldOfViewProximity(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))
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

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(ProximityBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))