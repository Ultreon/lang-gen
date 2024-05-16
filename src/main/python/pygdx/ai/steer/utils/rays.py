from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration as _ParallelSideRayConfiguration
_ParallelSideRayConfiguration = _ParallelSideRayConfiguration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as _RayConfigurationBase
_RayConfigurationBase = _RayConfigurationBase
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParallelSideRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _ParallelSideRayConfiguration) -> 'ParallelSideRayConfiguration':
        return ParallelSideRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParallelSideRayConfiguration):
        """
        Dynamic initializer for ParallelSideRayConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParallelSideRayConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParallelSideRayConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSideOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getSideOffset()"""
        return float._wrap(super(ParallelSideRayConfiguration, self).getSideOffset())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float,float)"""
        val = _ParallelSideRayConfiguration(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getLength()"""
        return float._wrap(super(ParallelSideRayConfiguration, self).getLength())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_RayConfigurationBase, self).setOwner(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(_RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray']._wrap(super(RayConfigurationBase, self).getRays())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setSideOffset(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setSideOffset(float)"""
        super(_ParallelSideRayConfiguration, self).setSideOffset(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setLength(float)"""
        super(_ParallelSideRayConfiguration, self).setLength(_float.valueOf(arg0))

    @override
    @overload
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.updateRays()"""
        return List['utils.Ray']._wrap(super(ParallelSideRayConfiguration, self).updateRays())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(RayConfigurationBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration as _ParallelSideRayConfiguration
_ParallelSideRayConfiguration = _ParallelSideRayConfiguration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as _RayConfigurationBase
_RayConfigurationBase = _RayConfigurationBase
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParallelSideRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _ParallelSideRayConfiguration) -> 'ParallelSideRayConfiguration':
        return ParallelSideRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParallelSideRayConfiguration):
        """
        Dynamic initializer for ParallelSideRayConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParallelSideRayConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParallelSideRayConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSideOffset(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getSideOffset()"""
        return float._wrap(super(ParallelSideRayConfiguration, self).getSideOffset())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float, arg2: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float,float)"""
        val = _ParallelSideRayConfiguration(arg0, _float.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.getLength()"""
        return float._wrap(super(ParallelSideRayConfiguration, self).getLength())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_RayConfigurationBase, self).setOwner(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(_RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray']._wrap(super(RayConfigurationBase, self).getRays())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setSideOffset(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setSideOffset(float)"""
        super(_ParallelSideRayConfiguration, self).setSideOffset(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.setLength(float)"""
        super(_ParallelSideRayConfiguration, self).setLength(_float.valueOf(arg0))

    @override
    @overload
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration.updateRays()"""
        return List['utils.Ray']._wrap(super(ParallelSideRayConfiguration, self).updateRays())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(RayConfigurationBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.ParallelSideRayConfiguration 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as _RayConfigurationBase
_RayConfigurationBase = _RayConfigurationBase
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from typing import List
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.utils.RayConfiguration as _RayConfiguration
_RayConfiguration = _RayConfiguration
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RayConfigurationBase():
    """com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase"""
 
    @staticmethod
    def _wrap(java_value: _RayConfigurationBase) -> 'RayConfigurationBase':
        return RayConfigurationBase(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RayConfigurationBase):
        """
        Dynamic initializer for RayConfigurationBase.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RayConfigurationBase__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RayConfigurationBase__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray']._wrap(super(RayConfigurationBase, self).getRays())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Steerable', arg1: int):
        """public com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase(com.badlogic.gdx.ai.steer.Steerable<T>,int)"""
        val = _RayConfigurationBase(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(_RayConfigurationBase, self).setRays(arg0)

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

    @abstractmethod
    def updateRays(self, ):
        """public abstract com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.RayConfiguration.updateRays()"""
        pass

    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(RayConfigurationBase, self).getOwner())

    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_RayConfigurationBase, self).setOwner(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as _RayConfigurationBase
_RayConfigurationBase = _RayConfigurationBase
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
import com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration as _SingleRayConfiguration
_SingleRayConfiguration = _SingleRayConfiguration
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SingleRayConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _SingleRayConfiguration) -> 'SingleRayConfiguration':
        return SingleRayConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SingleRayConfiguration):
        """
        Dynamic initializer for SingleRayConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SingleRayConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SingleRayConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float)"""
        val = _SingleRayConfiguration(arg0, _float.valueOf(arg1))
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

    @overload
    def setLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.setLength(float)"""
        super(_SingleRayConfiguration, self).setLength(_float.valueOf(arg0))

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_RayConfigurationBase, self).setOwner(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(_RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray']._wrap(super(RayConfigurationBase, self).getRays())

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
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.updateRays()"""
        return List['utils.Ray']._wrap(super(SingleRayConfiguration, self).updateRays())

    @overload
    def getLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.SingleRayConfiguration.getLength()"""
        return float._wrap(super(SingleRayConfiguration, self).getLength())

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(RayConfigurationBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration as _CentralRayWithWhiskersConfiguration
_CentralRayWithWhiskersConfiguration = _CentralRayWithWhiskersConfiguration
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase as _RayConfigurationBase
_RayConfigurationBase = _RayConfigurationBase
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.ai.steer.Steerable as _Steerable
_Steerable = _Steerable
try:
    from pygdx.ai import steer
except ImportError:
    steer = _import_once("pygdx.ai.steer")

import com.badlogic.gdx.ai.utils.Ray as _Ray
_Ray = _Ray
from builtins import bool
try:
    from pygdx.ai import utils
except ImportError:
    utils = _import_once("pygdx.ai.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CentralRayWithWhiskersConfiguration():
    """com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _CentralRayWithWhiskersConfiguration) -> 'CentralRayWithWhiskersConfiguration':
        return CentralRayWithWhiskersConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CentralRayWithWhiskersConfiguration):
        """
        Dynamic initializer for CentralRayWithWhiskersConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CentralRayWithWhiskersConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CentralRayWithWhiskersConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getWhiskerAngle(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getWhiskerAngle()"""
        return float._wrap(super(CentralRayWithWhiskersConfiguration, self).getWhiskerAngle())

    @overload
    def setRayLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setRayLength(float)"""
        super(_CentralRayWithWhiskersConfiguration, self).setRayLength(_float.valueOf(arg0))

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

    @overload
    def getWhiskerLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getWhiskerLength()"""
        return float._wrap(super(CentralRayWithWhiskersConfiguration, self).getWhiskerLength())

    @override
    @overload
    def setOwner(self, arg0: 'Steerable'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setOwner(com.badlogic.gdx.ai.steer.Steerable<T>)"""
        super(_RayConfigurationBase, self).setOwner(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def updateRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.updateRays()"""
        return List['utils.Ray']._wrap(super(CentralRayWithWhiskersConfiguration, self).updateRays())

    @overload
    def setWhiskerAngle(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setWhiskerAngle(float)"""
        super(_CentralRayWithWhiskersConfiguration, self).setWhiskerAngle(_float.valueOf(arg0))

    @override
    @overload
    def setRays(self, arg0: 'Ray'):
        """public void com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.setRays(com.badlogic.gdx.ai.utils.Ray<T>[])"""
        super(_RayConfigurationBase, self).setRays(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getRays(self) -> List['utils.Ray']:
        """public com.badlogic.gdx.ai.utils.Ray<T>[] com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getRays()"""
        return List['utils.Ray']._wrap(super(RayConfigurationBase, self).getRays())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getRayLength(self) -> float:
        """public float com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.getRayLength()"""
        return float._wrap(super(CentralRayWithWhiskersConfiguration, self).getRayLength())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setWhiskerLength(self, arg0: float):
        """public void com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration.setWhiskerLength(float)"""
        super(_CentralRayWithWhiskersConfiguration, self).setWhiskerLength(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Steerable', arg1: float, arg2: float, arg3: float):
        """public com.badlogic.gdx.ai.steer.utils.rays.CentralRayWithWhiskersConfiguration(com.badlogic.gdx.ai.steer.Steerable<T>,float,float,float)"""
        val = _CentralRayWithWhiskersConfiguration(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def getOwner(self) -> 'steer.Steerable':
        """public com.badlogic.gdx.ai.steer.Steerable<T> com.badlogic.gdx.ai.steer.utils.rays.RayConfigurationBase.getOwner()"""
        return 'steer.Steerable'._wrap(super(RayConfigurationBase, self).getOwner())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())