from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as _ProximityBase
_ProximityBase = _ProximityBase
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity as _FieldOfViewProximity
_FieldOfViewProximity = _FieldOfViewProximity
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FieldOfViewProximity():
    """com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity"""
 
    @staticmethod
    def _wrap(java_value: _FieldOfViewProximity) -> 'FieldOfViewProximity':
        return FieldOfViewProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldOfViewProximity):
        """
        Dynamic initializer for FieldOfViewProximity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldOfViewProximity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldOfViewProximity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'._wrap(super(ProximityBase, self).getAgents())

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getAngle()"""
        return float._wrap(super(FieldOfViewProximity, self).getAngle())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(_ProximityBase, self).setAgents(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setAngle(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setAngle(float)"""
        super(_FieldOfViewProximity, self).setAngle(_float.valueOf(arg0))

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(ProximityBase, self).getOwner())

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
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setRadius(float)"""
        super(_FieldOfViewProximity, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int._wrap(super(_FieldOfViewProximity, self).findNeighbors(arg0))

    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getRadius()"""
        return float._wrap(super(FieldOfViewProximity, self).getRadius())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_ProximityBase, self).setOwner(arg0)

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
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float,float)"""
        val = _FieldOfViewProximity(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as _ProximityBase
_ProximityBase = _ProximityBase
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity as _FieldOfViewProximity
_FieldOfViewProximity = _FieldOfViewProximity
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FieldOfViewProximity():
    """com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity"""
 
    @staticmethod
    def _wrap(java_value: _FieldOfViewProximity) -> 'FieldOfViewProximity':
        return FieldOfViewProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldOfViewProximity):
        """
        Dynamic initializer for FieldOfViewProximity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldOfViewProximity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldOfViewProximity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'._wrap(super(ProximityBase, self).getAgents())

    @overload
    def getAngle(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getAngle()"""
        return float._wrap(super(FieldOfViewProximity, self).getAngle())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(_ProximityBase, self).setAgents(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setAngle(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setAngle(float)"""
        super(_FieldOfViewProximity, self).setAngle(_float.valueOf(arg0))

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(ProximityBase, self).getOwner())

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
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.setRadius(float)"""
        super(_FieldOfViewProximity, self).setRadius(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int._wrap(super(_FieldOfViewProximity, self).findNeighbors(arg0))

    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity.getRadius()"""
        return float._wrap(super(FieldOfViewProximity, self).getRadius())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_ProximityBase, self).setOwner(arg0)

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
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float,float)"""
        val = _FieldOfViewProximity(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.FieldOfViewProximity 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.ProximityBase
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as _ProximityBase
_ProximityBase = _ProximityBase
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Proximity as _Proximity
_Proximity = _Proximity
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProximityBase():
    """com.badlogic.gdx.ai.steer.proximities.ProximityBase"""
 
    @staticmethod
    def _wrap(java_value: _ProximityBase) -> 'ProximityBase':
        return ProximityBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProximityBase):
        """
        Dynamic initializer for ProximityBase.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProximityBase__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProximityBase__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'._wrap(super(ProximityBase, self).getAgents())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable'):
        """public com.badlogic.gdx.ai.steer.proximities.ProximityBase(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        val = _ProximityBase(arg0, arg1)
        self.__wrapper = val

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

    @abstractmethod
    def findNeighbors(self, arg0: 'ProximityCallback'):
        """public abstract int com.badlogic.gdx.ai.steer.Proximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        pass

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(ProximityBase, self).getOwner())

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
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(_ProximityBase, self).setAgents(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_ProximityBase, self).setOwner(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.InfiniteProximity
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as _ProximityBase
_ProximityBase = _ProximityBase
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.proximities.InfiniteProximity as _InfiniteProximity
_InfiniteProximity = _InfiniteProximity
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InfiniteProximity():
    """com.badlogic.gdx.ai.steer.proximities.InfiniteProximity"""
 
    @staticmethod
    def _wrap(java_value: _InfiniteProximity) -> 'InfiniteProximity':
        return InfiniteProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InfiniteProximity):
        """
        Dynamic initializer for InfiniteProximity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InfiniteProximity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InfiniteProximity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'._wrap(super(ProximityBase, self).getAgents())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(_ProximityBase, self).setAgents(arg0)

    @overload
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable'):
        """public com.badlogic.gdx.ai.steer.proximities.InfiniteProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        val = _InfiniteProximity(arg0, arg1)
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(ProximityBase, self).getOwner())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.InfiniteProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int._wrap(super(_InfiniteProximity, self).findNeighbors(arg0))

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
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_ProximityBase, self).setOwner(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.proximities.RadiusProximity
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.Iterable as Iterable
import com.badlogic.gdx.ai.steer.proximities.RadiusProximity as _RadiusProximity
_RadiusProximity = _RadiusProximity
import com.badlogic.gdx.ai.steer.proximities.ProximityBase as _ProximityBase
_ProximityBase = _ProximityBase
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RadiusProximity():
    """com.badlogic.gdx.ai.steer.proximities.RadiusProximity"""
 
    @staticmethod
    def _wrap(java_value: _RadiusProximity) -> 'RadiusProximity':
        return RadiusProximity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RadiusProximity):
        """
        Dynamic initializer for RadiusProximity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RadiusProximity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RadiusProximity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAgents(self) -> 'Iterable':
        """public java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getAgents()"""
        return 'Iterable'._wrap(super(ProximityBase, self).getAgents())

    @override
    @overload
    def setAgents(self, arg0: 'Iterable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setAgents(java.lang.Iterable<com.badlogic.gdx.ai.steer.Steerable<T>>)"""
        super(_ProximityBase, self).setAgents(arg0)

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

    @overload
    def findNeighbors(self, arg0: 'ProximityCallback') -> int:
        """public int com.badlogic.gdx.ai.steer.proximities.RadiusProximity.findNeighbors(com.badlogic.gdx.ai.steer.Proximity$ProximityCallback<T>)"""
        return int._wrap(super(_RadiusProximity, self).findNeighbors(arg0))

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.proximities.ProximityBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(ProximityBase, self).getOwner())

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
    def __init__(self, arg0: 'Steerable', arg1: 'Iterable', arg2: float):
        """public com.badlogic.gdx.ai.steer.proximities.RadiusProximity(com.badlogic.gdx.ai.steer.Steerable<T>,java.lang.Iterable<? extends com.badlogic.gdx.ai.steer.Steerable<T>>,float)"""
        val = _RadiusProximity(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getRadius(self) -> float:
        """public float com.badlogic.gdx.ai.steer.proximities.RadiusProximity.getRadius()"""
        return float._wrap(super(RadiusProximity, self).getRadius())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.proximities.ProximityBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_ProximityBase, self).setOwner(arg0)

    @overload
    def setRadius(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.proximities.RadiusProximity.setRadius(float)"""
        super(_RadiusProximity, self).setRadius(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())