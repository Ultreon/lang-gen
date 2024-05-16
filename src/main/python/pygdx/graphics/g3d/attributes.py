from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute as _FloatAttribute
_FloatAttribute = _FloatAttribute
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute"""
 
    @staticmethod
    def _wrap(java_value: _FloatAttribute) -> 'FloatAttribute':
        return FloatAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatAttribute):
        """
        Dynamic initializer for FloatAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatAttribute__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long)"""
        val = _FloatAttribute(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(FloatAttribute, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createAlphaTest(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createAlphaTest(float)"""
        return FloatAttribute._wrap(_FloatAttribute.createAlphaTest(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long,float)"""
        val = _FloatAttribute(_long.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.hashCode()"""
        return int._wrap(super(FloatAttribute, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_FloatAttribute, self).compareTo(arg0))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def createShininess(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createShininess(float)"""
        return FloatAttribute._wrap(_FloatAttribute.createShininess(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute as _FloatAttribute
_FloatAttribute = _FloatAttribute
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute"""
 
    @staticmethod
    def _wrap(java_value: _FloatAttribute) -> 'FloatAttribute':
        return FloatAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatAttribute):
        """
        Dynamic initializer for FloatAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatAttribute__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long)"""
        val = _FloatAttribute(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(FloatAttribute, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createAlphaTest(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createAlphaTest(float)"""
        return FloatAttribute._wrap(_FloatAttribute.createAlphaTest(_float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long,float)"""
        val = _FloatAttribute(_long.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.hashCode()"""
        return int._wrap(super(FloatAttribute, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_FloatAttribute, self).compareTo(arg0))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def createShininess(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createShininess(float)"""
        return FloatAttribute._wrap(_FloatAttribute.createShininess(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute as _ColorAttribute
_ColorAttribute = _ColorAttribute
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute"""
 
    @staticmethod
    def _wrap(java_value: _ColorAttribute) -> 'ColorAttribute':
        return ColorAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorAttribute):
        """
        Dynamic initializer for ColorAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createDiffuse(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createDiffuse(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createDiffuse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.hashCode()"""
        return int._wrap(super(ColorAttribute, self).hashCode())

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.is(long)"""
        return bool._wrap(_ColorAttribute.is(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createAmbientLight(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbientLight(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createAmbientLight(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def createReflection(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createReflection(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createReflection(arg0))

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(ColorAttribute, self).copy())

    @staticmethod
    @overload
    def createAmbient(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbient(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createAmbient(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def createEmissive(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createEmissive(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createEmissive(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long,float,float,float,float)"""
        val = _ColorAttribute(_long.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createSpecular(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createSpecular(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createSpecular(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createFog(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createFog(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createFog(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long)"""
        val = _ColorAttribute(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @staticmethod
    @overload
    def createAmbient(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbient(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createAmbient(arg0))

    @staticmethod
    @overload
    def createReflection(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createReflection(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createReflection(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @staticmethod
    @overload
    def createAmbientLight(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbientLight(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createAmbientLight(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @staticmethod
    @overload
    def createDiffuse(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createDiffuse(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createDiffuse(arg0))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_ColorAttribute, self).compareTo(arg0))

    @staticmethod
    @overload
    def createEmissive(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createEmissive(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createEmissive(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'ColorAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute)"""
        val = _ColorAttribute(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def createFog(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createFog(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute._wrap(_ColorAttribute.createFog(arg0))

    @staticmethod
    @overload
    def createSpecular(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createSpecular(float,float,float,float)"""
        return ColorAttribute._wrap(_ColorAttribute.createSpecular(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long,com.badlogic.gdx.graphics.Color)"""
        val = _ColorAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.IntAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.IntAttribute as _IntAttribute
_IntAttribute = _IntAttribute
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.IntAttribute"""
 
    @staticmethod
    def _wrap(java_value: _IntAttribute) -> 'IntAttribute':
        return IntAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntAttribute):
        """
        Dynamic initializer for IntAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.IntAttribute(long)"""
        val = _IntAttribute(_long.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.hashCode()"""
        return int._wrap(super(IntAttribute, self).hashCode())

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
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(IntAttribute, self).copy())

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

    @staticmethod
    @overload
    def createCullFace(arg0: int) -> 'IntAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.IntAttribute com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.createCullFace(int)"""
        return IntAttribute._wrap(_IntAttribute.createCullFace(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_IntAttribute, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.IntAttribute(long,int)"""
        val = _IntAttribute(_long.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute as _CubemapAttribute
_CubemapAttribute = _CubemapAttribute
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CubemapAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute"""
 
    @staticmethod
    def _wrap(java_value: _CubemapAttribute) -> 'CubemapAttribute':
        return CubemapAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CubemapAttribute):
        """
        Dynamic initializer for CubemapAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CubemapAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CubemapAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(CubemapAttribute, self).copy())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long)"""
        val = _CubemapAttribute(_long.valueOf(arg0))
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
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor'):
        """public <T extends com.badlogic.gdx.graphics.Cubemap> com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        val = _CubemapAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.hashCode()"""
        return int._wrap(super(CubemapAttribute, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

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
    def __init__(self, arg0: int, arg1: 'Cubemap'):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long,com.badlogic.gdx.graphics.Cubemap)"""
        val = _CubemapAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.is(long)"""
        return bool._wrap(_CubemapAttribute.is(_long.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'CubemapAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute)"""
        val = _CubemapAttribute(arg0)
        self.__wrapper = val

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_CubemapAttribute, self).compareTo(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute as _DirectionalLightsAttribute
_DirectionalLightsAttribute = _DirectionalLightsAttribute
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DirectionalLightsAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute"""
 
    @staticmethod
    def _wrap(java_value: _DirectionalLightsAttribute) -> 'DirectionalLightsAttribute':
        return DirectionalLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DirectionalLightsAttribute):
        """
        Dynamic initializer for DirectionalLightsAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DirectionalLightsAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DirectionalLightsAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'DirectionalLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.copy()"""
        return 'DirectionalLightsAttribute'._wrap(super(DirectionalLightsAttribute, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = _DirectionalLightsAttribute()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = _DirectionalLightsAttribute()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.hashCode()"""
        return int._wrap(super(DirectionalLightsAttribute, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'DirectionalLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute)"""
        val = _DirectionalLightsAttribute(arg0)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_DirectionalLightsAttribute, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.is(long)"""
        return bool._wrap(_DirectionalLightsAttribute.is(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute as _SpotLightsAttribute
_SpotLightsAttribute = _SpotLightsAttribute
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpotLightsAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute"""
 
    @staticmethod
    def _wrap(java_value: _SpotLightsAttribute) -> 'SpotLightsAttribute':
        return SpotLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpotLightsAttribute):
        """
        Dynamic initializer for SpotLightsAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpotLightsAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpotLightsAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'SpotLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.copy()"""
        return 'SpotLightsAttribute'._wrap(super(SpotLightsAttribute, self).copy())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute()"""
        val = _SpotLightsAttribute()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute()"""
        val = _SpotLightsAttribute()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'SpotLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute)"""
        val = _SpotLightsAttribute(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.hashCode()"""
        return int._wrap(super(SpotLightsAttribute, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_SpotLightsAttribute, self).compareTo(arg0))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.is(long)"""
        return bool._wrap(_SpotLightsAttribute.is(_long.valueOf(arg0))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute as _DepthTestAttribute
_DepthTestAttribute = _DepthTestAttribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DepthTestAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute"""
 
    @staticmethod
    def _wrap(java_value: _DepthTestAttribute) -> 'DepthTestAttribute':
        return DepthTestAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DepthTestAttribute):
        """
        Dynamic initializer for DepthTestAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DepthTestAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DepthTestAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(DepthTestAttribute, self).copy())

    @overload
    def __init__(self, arg0: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = _DepthTestAttribute(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,float,float)"""
        val = _DepthTestAttribute(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute()"""
        val = _DepthTestAttribute()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(boolean)"""
        val = _DepthTestAttribute(_boolean.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,boolean)"""
        val = _DepthTestAttribute(_int.valueOf(arg0), _boolean.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int)"""
        val = _DepthTestAttribute(_int.valueOf(arg0))
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_DepthTestAttribute, self).compareTo(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.hashCode()"""
        return int._wrap(super(DepthTestAttribute, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute()"""
        val = _DepthTestAttribute()
        self.__wrapper = val

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.is(long)"""
        return bool._wrap(_DepthTestAttribute.is(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,float,float,boolean)"""
        val = _DepthTestAttribute(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(long,int,float,float,boolean)"""
        val = _DepthTestAttribute(_long.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as _BlendingAttribute
_BlendingAttribute = _BlendingAttribute
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlendingAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute"""
 
    @staticmethod
    def _wrap(java_value: _BlendingAttribute) -> 'BlendingAttribute':
        return BlendingAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlendingAttribute):
        """
        Dynamic initializer for BlendingAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlendingAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlendingAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, arg3: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(boolean,int,int,float)"""
        val = _BlendingAttribute(_boolean.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(int,int)"""
        val = _BlendingAttribute(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_BlendingAttribute, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(int,int,float)"""
        val = _BlendingAttribute(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(boolean,float)"""
        val = _BlendingAttribute(_boolean.valueOf(arg0), _float.valueOf(arg1))
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
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def __init__(self, arg0: 'BlendingAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute)"""
        val = _BlendingAttribute(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute()"""
        val = _BlendingAttribute()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

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
    def copy(self) -> 'BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.copy()"""
        return 'BlendingAttribute'._wrap(super(BlendingAttribute, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(float)"""
        val = _BlendingAttribute(_float.valueOf(arg0))
        self.__wrapper = val

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.is(long)"""
        return bool._wrap(_BlendingAttribute.is(_long.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute()"""
        val = _BlendingAttribute()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.hashCode()"""
        return int._wrap(super(BlendingAttribute, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute as _PointLightsAttribute
_PointLightsAttribute = _PointLightsAttribute
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointLightsAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute"""
 
    @staticmethod
    def _wrap(java_value: _PointLightsAttribute) -> 'PointLightsAttribute':
        return PointLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointLightsAttribute):
        """
        Dynamic initializer for PointLightsAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointLightsAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointLightsAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute()"""
        val = _PointLightsAttribute()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute()"""
        val = _PointLightsAttribute()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.is(long)"""
        return bool._wrap(_PointLightsAttribute.is(_long.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_PointLightsAttribute, self).compareTo(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.hashCode()"""
        return int._wrap(super(PointLightsAttribute, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'PointLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.copy()"""
        return 'PointLightsAttribute'._wrap(super(PointLightsAttribute, self).copy())

    @overload
    def __init__(self, arg0: 'PointLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute)"""
        val = _PointLightsAttribute(arg0)
        self.__wrapper = val

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

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Attribute as _Attribute
_Attribute = _Attribute
import com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute as _TextureAttribute
_TextureAttribute = _TextureAttribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextureAttribute():
    """com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute"""
 
    @staticmethod
    def _wrap(java_value: _TextureAttribute) -> 'TextureAttribute':
        return TextureAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureAttribute):
        """
        Dynamic initializer for TextureAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def createReflection(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createReflection(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createReflection(arg0))

    @staticmethod
    @overload
    def createAmbient(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createAmbient(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createAmbient(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long)"""
        val = _TextureAttribute(_long.valueOf(arg0))
        self.__wrapper = val

    @staticmethod
    @overload
    def createBump(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createBump(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createBump(arg0))

    @staticmethod
    @overload
    def createNormal(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createNormal(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createNormal(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor'):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        val = _TextureAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createAmbient(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createAmbient(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createAmbient(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor', arg2: float, arg3: float, arg4: float, arg5: float):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>,float,float,float,float)"""
        val = _TextureAttribute(_long.valueOf(arg0), arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))
        self.__wrapper = val

    @staticmethod
    @overload
    def createBump(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createBump(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createBump(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def createDiffuse(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createDiffuse(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createDiffuse(arg0))

    @staticmethod
    @overload
    def createEmissive(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createEmissive(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createEmissive(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.is(long)"""
        return bool._wrap(_TextureAttribute.is(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def createEmissive(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createEmissive(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createEmissive(arg0))

    @staticmethod
    @overload
    def createSpecular(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createSpecular(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createSpecular(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str._wrap(_Attribute.getAttributeAlias(_long.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int._wrap(super(_TextureAttribute, self).compareTo(arg0))

    @overload
    def set(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.set(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_TextureAttribute, self).set(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.hashCode()"""
        return int._wrap(super(TextureAttribute, self).hashCode())

    @staticmethod
    @overload
    def createSpecular(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createSpecular(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createSpecular(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: int, arg1: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.Texture)"""
        val = _TextureAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _TextureAttribute(_long.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str._wrap(super(g3d.Attribute, self).toString())

    @staticmethod
    @overload
    def createDiffuse(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createDiffuse(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute._wrap(_TextureAttribute.createDiffuse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool._wrap(super(_g3d.Attribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TextureAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute)"""
        val = _TextureAttribute(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor', arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>,float,float,float,float,int)"""
        val = _TextureAttribute(_long.valueOf(arg0), arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _int.valueOf(arg6))
        self.__wrapper = val

    @staticmethod
    @overload
    def createReflection(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createReflection(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createReflection(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createNormal(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createNormal(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute._wrap(_TextureAttribute.createNormal(arg0))

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.copy()"""
        return 'g3d.Attribute'._wrap(super(TextureAttribute, self).copy())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int._wrap(_Attribute.getAttributeType(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()