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
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as __RayConfigurationBase
__RayConfigurationBase = __RayConfigurationBase
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
import com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration as __SingleRayConfiguration
__SingleRayConfiguration = __SingleRayConfiguration
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class SingleRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __SingleRayConfiguration) -> 'SingleRayConfiguration':
        return SingleRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingleRayConfiguration):
        """
        Dynamic initializer for SingleRayConfiguration.
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
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.setLength(float)"""
        super(__SingleRayConfiguration, self).setLength(__float.valueOf(arg0))

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __SingleRayConfiguration(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__RayConfigurationBase, self).setOwner(arg0)

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(RayConfigurationBase, self).getOwner())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(__RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.getLength()"""
        return float.__wrap(super(SingleRayConfiguration, self).getLength())

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
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.updateRays()"""
        return List['utils.Ray'].__wrap(super(SingleRayConfiguration, self).updateRays())

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray'].__wrap(super(RayConfigurationBase, self).getRays())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as __RayConfigurationBase
__RayConfigurationBase = __RayConfigurationBase
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
import com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration as __SingleRayConfiguration
__SingleRayConfiguration = __SingleRayConfiguration
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class SingleRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __SingleRayConfiguration) -> 'SingleRayConfiguration':
        return SingleRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SingleRayConfiguration):
        """
        Dynamic initializer for SingleRayConfiguration.
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
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.setLength(float)"""
        super(__SingleRayConfiguration, self).setLength(__float.valueOf(arg0))

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = __SingleRayConfiguration(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__RayConfigurationBase, self).setOwner(arg0)

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(RayConfigurationBase, self).getOwner())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(__RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.getLength()"""
        return float.__wrap(super(SingleRayConfiguration, self).getLength())

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
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.updateRays()"""
        return List['utils.Ray'].__wrap(super(SingleRayConfiguration, self).updateRays())

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray'].__wrap(super(RayConfigurationBase, self).getRays())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as __RayConfigurationBase
__RayConfigurationBase = __RayConfigurationBase
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration as __ParallelSideRayConfiguration
__ParallelSideRayConfiguration = __ParallelSideRayConfiguration
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class ParallelSideRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __ParallelSideRayConfiguration) -> 'ParallelSideRayConfiguration':
        return ParallelSideRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParallelSideRayConfiguration):
        """
        Dynamic initializer for ParallelSideRayConfiguration.
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
    def __init__(self, arg0: 'Steerable', arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float,float)"""
        val = __ParallelSideRayConfiguration(arg0, __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setSideOffset(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setSideOffset(float)"""
        super(__ParallelSideRayConfiguration, self).setSideOffset(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setLength(float)"""
        super(__ParallelSideRayConfiguration, self).setLength(__float.valueOf(arg0))

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__RayConfigurationBase, self).setOwner(arg0)

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
    def getSideOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getSideOffset()"""
        return float.__wrap(super(ParallelSideRayConfiguration, self).getSideOffset())

    @override
    @overload
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.updateRays()"""
        return List['utils.Ray'].__wrap(super(ParallelSideRayConfiguration, self).updateRays())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(RayConfigurationBase, self).getOwner())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(__RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getLength()"""
        return float.__wrap(super(ParallelSideRayConfiguration, self).getLength())

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
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray'].__wrap(super(RayConfigurationBase, self).getRays()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as __RayConfiguration
__RayConfiguration = __RayConfiguration
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as __RayConfigurationBase
__RayConfigurationBase = __RayConfigurationBase
from abc import abstractmethod, ABC
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class RayConfigurationBase(ABC):
    """com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase"""
 
    @staticmethod
    def __wrap(java_value: __RayConfigurationBase) -> 'RayConfigurationBase':
        return RayConfigurationBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RayConfigurationBase):
        """
        Dynamic initializer for RayConfigurationBase.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: int):
        """public com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase(com.badlogic.gdx.ai.steer.Steerable<T>,int)"""
        val = __RayConfigurationBase(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__RayConfigurationBase, self).setOwner(arg0)

    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray'].__wrap(super(RayConfigurationBase, self).getRays())

    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(__RayConfigurationBase, self).setRays(arg0)

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(RayConfigurationBase, self).getOwner())

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @abstractmethod
    def updateRays(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.RayConfiguration.updateRays()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.ai.steer.Steerable as __Steerable
__Steerable = __Steerable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as __RayConfigurationBase
__RayConfigurationBase = __RayConfigurationBase
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx.ai import steer
except ImportError:
    steer = __import_once__("pygdx.ai.steer")

import com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration as __CentralRayWithWhiskersConfiguration
__CentralRayWithWhiskersConfiguration = __CentralRayWithWhiskersConfiguration
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = __import_once__("pygdx.ai.utils")

import com.badlogic.gdx.ai.utils.Ray as __Ray
__Ray = __Ray
from builtins import int
 
class CentralRayWithWhiskersConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration"""
 
    @staticmethod
    def __wrap(java_value: __CentralRayWithWhiskersConfiguration) -> 'CentralRayWithWhiskersConfiguration':
        return CentralRayWithWhiskersConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CentralRayWithWhiskersConfiguration):
        """
        Dynamic initializer for CentralRayWithWhiskersConfiguration.
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
    def getWhiskerLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getWhiskerLength()"""
        return float.__wrap(super(CentralRayWithWhiskersConfiguration, self).getWhiskerLength())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setWhiskerLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setWhiskerLength(float)"""
        super(__CentralRayWithWhiskersConfiguration, self).setWhiskerLength(__float.valueOf(arg0))

    @overload
    def getWhiskerAngle(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getWhiskerAngle()"""
        return float.__wrap(super(CentralRayWithWhiskersConfiguration, self).getWhiskerAngle())

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

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float,float,float)"""
        val = __CentralRayWithWhiskersConfiguration(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(__RayConfigurationBase, self).setOwner(arg0)

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
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'.__wrap(super(RayConfigurationBase, self).getOwner())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getRayLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getRayLength()"""
        return float.__wrap(super(CentralRayWithWhiskersConfiguration, self).getRayLength())

    @override
    @overload
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.updateRays()"""
        return List['utils.Ray'].__wrap(super(CentralRayWithWhiskersConfiguration, self).updateRays())

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(__RayConfigurationBase, self).setRays(arg0)

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

    @overload
    def setRayLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setRayLength(float)"""
        super(__CentralRayWithWhiskersConfiguration, self).setRayLength(__float.valueOf(arg0))

    @overload
    def setWhiskerAngle(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setWhiskerAngle(float)"""
        super(__CentralRayWithWhiskersConfiguration, self).setWhiskerAngle(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray'].__wrap(super(RayConfigurationBase, self).getRays())