from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.graphics.g3d.environment.ShadowMap as _ShadowMap
_ShadowMap = _ShadowMap
from abc import abstractmethod, ABC
 
class ShadowMap():
    """com.badlogic.gdx.graphics.g3d.environment.ShadowMap"""
 
    @staticmethod
    def _wrap(java_value: _ShadowMap) -> 'ShadowMap':
        return ShadowMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShadowMap):
        """
        Dynamic initializer for ShadowMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShadowMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShadowMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getProjViewTrans(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getProjViewTrans()"""
        pass

    @abstractmethod
    def getDepthMap(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getDepthMap()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.ShadowMap
import com.badlogic.gdx.graphics.g3d.environment.ShadowMap as _ShadowMap
_ShadowMap = _ShadowMap
from abc import abstractmethod, ABC
 
class ShadowMap():
    """com.badlogic.gdx.graphics.g3d.environment.ShadowMap"""
 
    @staticmethod
    def _wrap(java_value: _ShadowMap) -> 'ShadowMap':
        return ShadowMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShadowMap):
        """
        Dynamic initializer for ShadowMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShadowMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShadowMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getProjViewTrans(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getProjViewTrans()"""
        pass

    @abstractmethod
    def getDepthMap(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.ShadowMap.getDepthMap()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.ShadowMap 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics as _SphericalHarmonics
_SphericalHarmonics = _SphericalHarmonics
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SphericalHarmonics():
    """com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics"""
 
    @staticmethod
    def _wrap(java_value: _SphericalHarmonics) -> 'SphericalHarmonics':
        return SphericalHarmonics(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SphericalHarmonics):
        """
        Dynamic initializer for SphericalHarmonics.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SphericalHarmonics__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SphericalHarmonics__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics(float[])"""
        val = _SphericalHarmonics(arg0)
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

    @overload
    def set(self, arg0: 'Color') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(com.badlogic.gdx.graphics.Color)"""
        return 'SphericalHarmonics'._wrap(super(_SphericalHarmonics, self).set(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'float') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(float[])"""
        return 'SphericalHarmonics'._wrap(super(_SphericalHarmonics, self).set(arg0))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics()"""
        val = _SphericalHarmonics()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'AmbientCubemap') -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        return 'SphericalHarmonics'._wrap(super(_SphericalHarmonics, self).set(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics()"""
        val = _SphericalHarmonics()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'SphericalHarmonics':
        """public com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics com.badlogic.gdx.graphics.g3d.environment.SphericalHarmonics.set(float,float,float)"""
        return 'SphericalHarmonics'._wrap(super(_SphericalHarmonics, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.PointLight
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.environment.PointLight as _PointLight
_PointLight = _PointLight
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.environment.BaseLight as _BaseLight
_BaseLight = _BaseLight
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointLight():
    """com.badlogic.gdx.graphics.g3d.environment.PointLight"""
 
    @staticmethod
    def _wrap(java_value: _PointLight) -> 'PointLight':
        return PointLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointLight):
        """
        Dynamic initializer for PointLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'PointLight') -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return 'PointLight'._wrap(super(_PointLight, self).set(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: 'PointLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.PointLight.equals(com.badlogic.gdx.graphics.g3d.environment.PointLight)"""
        return bool._wrap(super(_PointLight, self).equals(arg0))

    @overload
    def setPosition(self, arg0: 'Vector3') -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setPosition(com.badlogic.gdx.math.Vector3)"""
        return 'PointLight'._wrap(super(_PointLight, self).setPosition(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(float,float,float,float,float,float,float)"""
        return 'PointLight'._wrap(super(_PointLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float, arg4: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.Color,float,float,float,float)"""
        return 'PointLight'._wrap(super(_PointLight, self).set(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setPosition(float,float,float)"""
        return 'PointLight'._wrap(super(_PointLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setIntensity(self, arg0: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.setIntensity(float)"""
        return 'PointLight'._wrap(super(_PointLight, self).setIntensity(_float.valueOf(arg0)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3', arg4: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(float,float,float,com.badlogic.gdx.math.Vector3,float)"""
        return 'PointLight'._wrap(super(_PointLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3, _float.valueOf(arg4)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3', arg2: float) -> 'PointLight':
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight com.badlogic.gdx.graphics.g3d.environment.PointLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,float)"""
        return 'PointLight'._wrap(super(_PointLight, self).set(arg0, arg1, _float.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight()"""
        val = _PointLight()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.PointLight.equals(java.lang.Object)"""
        return bool._wrap(super(_PointLight, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.PointLight()"""
        val = _PointLight()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.DirectionalLight
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight as _DirectionalLight
_DirectionalLight = _DirectionalLight
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.environment.BaseLight as _BaseLight
_BaseLight = _BaseLight
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectionalLight():
    """com.badlogic.gdx.graphics.g3d.environment.DirectionalLight"""
 
    @staticmethod
    def _wrap(java_value: _DirectionalLight) -> 'DirectionalLight':
        return DirectionalLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectionalLight):
        """
        Dynamic initializer for DirectionalLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectionalLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectionalLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0, arg1))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(java.lang.Object)"""
        return bool._wrap(super(_DirectionalLight, self).equals(arg0))

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
    def equals(self, arg0: 'DirectionalLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return bool._wrap(super(_DirectionalLight, self).equals(arg0))

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).setDirection(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'DirectionalLight') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight()"""
        val = _DirectionalLight()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight()"""
        val = _DirectionalLight()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).setDirection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.BaseLight
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.environment.BaseLight as _BaseLight
_BaseLight = _BaseLight
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseLight():
    """com.badlogic.gdx.graphics.g3d.environment.BaseLight"""
 
    @staticmethod
    def _wrap(java_value: _BaseLight) -> 'BaseLight':
        return BaseLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseLight):
        """
        Dynamic initializer for BaseLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.BaseLight()"""
        val = _BaseLight()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.BaseLight()"""
        val = _BaseLight()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.SpotLight
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.environment.SpotLight as _SpotLight
_SpotLight = _SpotLight
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.environment.BaseLight as _BaseLight
_BaseLight = _BaseLight
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpotLight():
    """com.badlogic.gdx.graphics.g3d.environment.SpotLight"""
 
    @staticmethod
    def _wrap(java_value: _SpotLight) -> 'SpotLight':
        return SpotLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpotLight):
        """
        Dynamic initializer for SpotLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpotLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpotLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(float,float,float,float,float,float,float,float,float,float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11)))

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setDirection(float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setDirection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setExponent(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setExponent(float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setExponent(_float.valueOf(arg0)))

    @overload
    def setCutoffAngle(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setCutoffAngle(float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setCutoffAngle(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight()"""
        val = _SpotLight()
        self.__wrapper = val

    @overload
    def set(self, arg0: 'SpotLight') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).set(arg0))

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3', arg3: float, arg4: float, arg5: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).set(arg0, arg1, arg2, _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

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
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.SpotLight.equals(java.lang.Object)"""
        return bool._wrap(super(_SpotLight, self).equals(arg0))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: 'SpotLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.SpotLight.equals(com.badlogic.gdx.graphics.g3d.environment.SpotLight)"""
        return bool._wrap(super(_SpotLight, self).equals(arg0))

    @overload
    def setTarget(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setTarget(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setTarget(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(com.badlogic.gdx.graphics.Color,float,float,float,float,float,float,float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).set(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9)))

    @overload
    def setPosition(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setPosition(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setPosition(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float, arg7: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.set(float,float,float,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3, arg4, _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight()"""
        val = _SpotLight()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setIntensity(self, arg0: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setIntensity(float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setIntensity(_float.valueOf(arg0)))

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float) -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setPosition(float,float,float)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'SpotLight':
        """public com.badlogic.gdx.graphics.g3d.environment.SpotLight com.badlogic.gdx.graphics.g3d.environment.SpotLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'SpotLight'._wrap(super(_SpotLight, self).setDirection(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.glutils.FrameBuffer as _FrameBuffer
_FrameBuffer = _FrameBuffer
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.math.Matrix4 as _Matrix4
_Matrix4 = _Matrix4
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor as _TextureDescriptor
_TextureDescriptor = _TextureDescriptor
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight as _DirectionalShadowLight
_DirectionalShadowLight = _DirectionalShadowLight
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.environment.DirectionalLight as _DirectionalLight
_DirectionalLight = _DirectionalLight
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import com.badlogic.gdx.graphics.g3d.environment.BaseLight as _BaseLight
_BaseLight = _BaseLight
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectionalShadowLight():
    """com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight"""
 
    @staticmethod
    def _wrap(java_value: _DirectionalShadowLight) -> 'DirectionalShadowLight':
        return DirectionalShadowLight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectionalShadowLight):
        """
        Dynamic initializer for DirectionalShadowLight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectionalShadowLight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectionalShadowLight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def begin(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.graphics.Camera)"""
        super(_DirectionalShadowLight, self).begin(arg0)

    @overload
    def set(self, arg0: 'Color', arg1: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0, arg1))

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin()"""
        super(DirectionalShadowLight, self).begin()

    @override
    @overload
    def getProjViewTrans(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getProjViewTrans()"""
        return 'math.Matrix4'._wrap(super(DirectionalShadowLight, self).getProjViewTrans())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getDepthMap(self) -> 'utils.TextureDescriptor':
        """public com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getDepthMap()"""
        return 'utils.TextureDescriptor'._wrap(super(DirectionalShadowLight, self).getDepthMap())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.end()"""
        super(DirectionalShadowLight, self).end()

    @overload
    def setDirection(self, arg0: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).setDirection(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def set(self, arg0: 'DirectionalLight') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: 'Color') -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(com.badlogic.gdx.graphics.Color)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @overload
    def setDirection(self, arg0: float, arg1: float, arg2: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.setDirection(float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).setDirection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'BaseLight':
        """public T com.badlogic.gdx.graphics.g3d.environment.BaseLight.setColor(float,float,float,float)"""
        return 'BaseLight'._wrap(super(_BaseLight, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getCamera()"""
        return 'graphics.Camera'._wrap(super(DirectionalShadowLight, self).getCamera())

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(float,float,float,float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def begin(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.begin(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_DirectionalShadowLight, self).begin(arg0, arg1)

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: float, arg5: float):
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight(int,int,float,float,float,float)"""
        val = _DirectionalShadowLight(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(java.lang.Object)"""
        return bool._wrap(super(_DirectionalLight, self).equals(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.dispose()"""
        super(DirectionalShadowLight, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: 'DirectionalLight') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.equals(com.badlogic.gdx.graphics.g3d.environment.DirectionalLight)"""
        return bool._wrap(super(_DirectionalLight, self).equals(arg0))

    @overload
    def getFrameBuffer(self) -> 'glutils.FrameBuffer':
        """public com.badlogic.gdx.graphics.glutils.FrameBuffer com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.getFrameBuffer()"""
        return 'glutils.FrameBuffer'._wrap(super(DirectionalShadowLight, self).getFrameBuffer())

    @overload
    def update(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_DirectionalShadowLight, self).update(arg0, arg1)

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
    def update(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.environment.DirectionalShadowLight.update(com.badlogic.gdx.graphics.Camera)"""
        super(_DirectionalShadowLight, self).update(arg0)

    @overload
    def set(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'DirectionalLight':
        """public com.badlogic.gdx.graphics.g3d.environment.DirectionalLight com.badlogic.gdx.graphics.g3d.environment.DirectionalLight.set(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'DirectionalLight'._wrap(super(_DirectionalLight, self).set(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap as _AmbientCubemap
_AmbientCubemap = _AmbientCubemap
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AmbientCubemap():
    """com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap"""
 
    @staticmethod
    def _wrap(java_value: _AmbientCubemap) -> 'AmbientCubemap':
        return AmbientCubemap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AmbientCubemap):
        """
        Dynamic initializer for AmbientCubemap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AmbientCubemap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AmbientCubemap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'float') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(float[])"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).set(arg0))

    @overload
    def __init__(self, arg0: 'AmbientCubemap'):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        val = _AmbientCubemap(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: float, arg1: float, arg2: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float,float,float,float)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap()"""
        val = _AmbientCubemap()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(arg0, arg1))

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3', arg3: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(arg0, arg1, arg2, _float.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'float'):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap(float[])"""
        val = _AmbientCubemap(arg0)
        self.__wrapper = val

    @overload
    def getColor(self, arg0: 'Color', arg1: int) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.getColor(com.badlogic.gdx.graphics.Color,int)"""
        return 'graphics.Color'._wrap(super(_AmbientCubemap, self).getColor(arg0, _int.valueOf(arg1)))

    @overload
    def set(self, arg0: 'Color') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(com.badlogic.gdx.graphics.Color)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).set(arg0))

    @overload
    def clear(self) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.clear()"""
        return 'AmbientCubemap'._wrap(super(AmbientCubemap, self).clear())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(float,float,float)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).set(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def set(self, arg0: 'AmbientCubemap') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.set(com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).set(arg0))

    @overload
    def add(self, arg0: float, arg1: float, arg2: float, arg3: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(float,float,float,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.toString()"""
        return str._wrap(super(AmbientCubemap, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap()"""
        val = _AmbientCubemap()
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Color', arg1: float, arg2: float, arg3: float) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,float,float,float)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def add(self, arg0: 'Color', arg1: 'Vector3', arg2: 'Vector3') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'Color') -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.add(com.badlogic.gdx.graphics.Color)"""
        return 'AmbientCubemap'._wrap(super(_AmbientCubemap, self).add(arg0))

    @overload
    def clamp(self) -> 'AmbientCubemap':
        """public com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap com.badlogic.gdx.graphics.g3d.environment.AmbientCubemap.clamp()"""
        return 'AmbientCubemap'._wrap(super(AmbientCubemap, self).clamp())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())