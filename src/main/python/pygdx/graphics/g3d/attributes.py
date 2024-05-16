from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute as __DirectionalLightsAttribute
__DirectionalLightsAttribute = __DirectionalLightsAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import int
 
class DirectionalLightsAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute"""
 
    @staticmethod
    def __wrap(java_value: __DirectionalLightsAttribute) -> 'DirectionalLightsAttribute':
        return DirectionalLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectionalLightsAttribute):
        """
        Dynamic initializer for DirectionalLightsAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.hashCode()"""
        return int.__wrap(super(DirectionalLightsAttribute, self).hashCode())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @overload
    def __init__(self, arg0: 'DirectionalLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute)"""
        val = __DirectionalLightsAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = __DirectionalLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__DirectionalLightsAttribute, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = __DirectionalLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def copy(self) -> 'DirectionalLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.copy()"""
        return 'DirectionalLightsAttribute'.__wrap(super(DirectionalLightsAttribute, self).copy())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.is(long)"""
        return bool.__wrap(__DirectionalLightsAttribute.is(__long.valueOf(arg0)))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute as __DirectionalLightsAttribute
__DirectionalLightsAttribute = __DirectionalLightsAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import int
 
class DirectionalLightsAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute"""
 
    @staticmethod
    def __wrap(java_value: __DirectionalLightsAttribute) -> 'DirectionalLightsAttribute':
        return DirectionalLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DirectionalLightsAttribute):
        """
        Dynamic initializer for DirectionalLightsAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.hashCode()"""
        return int.__wrap(super(DirectionalLightsAttribute, self).hashCode())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @overload
    def __init__(self, arg0: 'DirectionalLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute)"""
        val = __DirectionalLightsAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = __DirectionalLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__DirectionalLightsAttribute, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute()"""
        val = __DirectionalLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def copy(self) -> 'DirectionalLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.copy()"""
        return 'DirectionalLightsAttribute'.__wrap(super(DirectionalLightsAttribute, self).copy())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute.is(long)"""
        return bool.__wrap(__DirectionalLightsAttribute.is(__long.valueOf(arg0)))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.DirectionalLightsAttribute 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute as __DepthTestAttribute
__DepthTestAttribute = __DepthTestAttribute
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
from builtins import int
 
class DepthTestAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute"""
 
    @staticmethod
    def __wrap(java_value: __DepthTestAttribute) -> 'DepthTestAttribute':
        return DepthTestAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DepthTestAttribute):
        """
        Dynamic initializer for DepthTestAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.is(long)"""
        return bool.__wrap(__DepthTestAttribute.is(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int)"""
        val = __DepthTestAttribute(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,boolean)"""
        val = __DepthTestAttribute(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,float,float)"""
        val = __DepthTestAttribute(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(DepthTestAttribute, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute()"""
        val = __DepthTestAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float, arg3: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(int,float,float,boolean)"""
        val = __DepthTestAttribute(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute()"""
        val = __DepthTestAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(boolean)"""
        val = __DepthTestAttribute(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = __DepthTestAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float, arg3: float, arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute(long,int,float,float,boolean)"""
        val = __DepthTestAttribute(__long.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.hashCode()"""
        return int.__wrap(super(DepthTestAttribute, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__DepthTestAttribute, self).compareTo(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.IntAttribute
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.attributes.IntAttribute as __IntAttribute
__IntAttribute = __IntAttribute
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
from builtins import int
 
class IntAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.IntAttribute"""
 
    @staticmethod
    def __wrap(java_value: __IntAttribute) -> 'IntAttribute':
        return IntAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntAttribute):
        """
        Dynamic initializer for IntAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createCullFace(arg0: int) -> 'IntAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.IntAttribute com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.createCullFace(int)"""
        return IntAttribute.__wrap(__IntAttribute.createCullFace(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.hashCode()"""
        return int.__wrap(super(IntAttribute, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.IntAttribute(long)"""
        val = __IntAttribute(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.IntAttribute(long,int)"""
        val = __IntAttribute(__long.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(IntAttribute, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.IntAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__IntAttribute, self).compareTo(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute as __SpotLightsAttribute
__SpotLightsAttribute = __SpotLightsAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import int
 
class SpotLightsAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute"""
 
    @staticmethod
    def __wrap(java_value: __SpotLightsAttribute) -> 'SpotLightsAttribute':
        return SpotLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpotLightsAttribute):
        """
        Dynamic initializer for SpotLightsAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute()"""
        val = __SpotLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.is(long)"""
        return bool.__wrap(__SpotLightsAttribute.is(__long.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'SpotLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute)"""
        val = __SpotLightsAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__SpotLightsAttribute, self).compareTo(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.hashCode()"""
        return int.__wrap(super(SpotLightsAttribute, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute()"""
        val = __SpotLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def copy(self) -> 'SpotLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.SpotLightsAttribute.copy()"""
        return 'SpotLightsAttribute'.__wrap(super(SpotLightsAttribute, self).copy())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute as __FloatAttribute
__FloatAttribute = __FloatAttribute
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
from builtins import int
 
class FloatAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute"""
 
    @staticmethod
    def __wrap(java_value: __FloatAttribute) -> 'FloatAttribute':
        return FloatAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatAttribute):
        """
        Dynamic initializer for FloatAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(FloatAttribute, self).copy())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__FloatAttribute, self).compareTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def createAlphaTest(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createAlphaTest(float)"""
        return FloatAttribute.__wrap(__FloatAttribute.createAlphaTest(__float.valueOf(arg0)))

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
    def __init__(self, arg0: int, arg1: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long,float)"""
        val = __FloatAttribute(__long.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.hashCode()"""
        return int.__wrap(super(FloatAttribute, self).hashCode())

    @staticmethod
    @overload
    def createShininess(arg0: float) -> 'FloatAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute.createShininess(float)"""
        return FloatAttribute.__wrap(__FloatAttribute.createShininess(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.FloatAttribute(long)"""
        val = __FloatAttribute(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute as __TextureAttribute
__TextureAttribute = __TextureAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class TextureAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute"""
 
    @staticmethod
    def __wrap(java_value: __TextureAttribute) -> 'TextureAttribute':
        return TextureAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAttribute):
        """
        Dynamic initializer for TextureAttribute.
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
 
    @staticmethod
    @overload
    def createSpecular(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createSpecular(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createSpecular(arg0))

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createReflection(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createReflection(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createReflection(arg0))

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(TextureAttribute, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.hashCode()"""
        return int.__wrap(super(TextureAttribute, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor', arg2: float, arg3: float, arg4: float, arg5: float, arg6: int):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>,float,float,float,float,int)"""
        val = __TextureAttribute(__long.valueOf(arg0), arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createEmissive(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createEmissive(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createEmissive(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor', arg2: float, arg3: float, arg4: float, arg5: float):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>,float,float,float,float)"""
        val = __TextureAttribute(__long.valueOf(arg0), arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long)"""
        val = __TextureAttribute(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createAmbient(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createAmbient(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createAmbient(arg0))

    @staticmethod
    @overload
    def createNormal(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createNormal(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createNormal(arg0))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.is(long)"""
        return bool.__wrap(__TextureAttribute.is(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @staticmethod
    @overload
    def createBump(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createBump(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createBump(arg0))

    @staticmethod
    @overload
    def createReflection(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createReflection(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createReflection(arg0))

    @staticmethod
    @overload
    def createSpecular(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createSpecular(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createSpecular(arg0))

    @overload
    def set(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.set(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureAttribute, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.Texture)"""
        val = __TextureAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createNormal(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createNormal(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createNormal(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createDiffuse(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createDiffuse(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createDiffuse(arg0))

    @staticmethod
    @overload
    def createEmissive(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createEmissive(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createEmissive(arg0))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__TextureAttribute, self).compareTo(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __TextureAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor'):
        """public <T extends com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        val = __TextureAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createDiffuse(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createDiffuse(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createDiffuse(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TextureAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute(com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute)"""
        val = __TextureAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createAmbient(arg0: 'Texture') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createAmbient(com.badlogic.gdx.graphics.Texture)"""
        return TextureAttribute.__wrap(__TextureAttribute.createAmbient(arg0))

    @staticmethod
    @overload
    def createBump(arg0: 'TextureRegion') -> 'TextureAttribute':
        """public static com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute com.badlogic.gdx.graphics.g3d.attributes.TextureAttribute.createBump(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return TextureAttribute.__wrap(__TextureAttribute.createBump(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute as __CubemapAttribute
__CubemapAttribute = __CubemapAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class CubemapAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute"""
 
    @staticmethod
    def __wrap(java_value: __CubemapAttribute) -> 'CubemapAttribute':
        return CubemapAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CubemapAttribute):
        """
        Dynamic initializer for CubemapAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.is(long)"""
        return bool.__wrap(__CubemapAttribute.is(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(CubemapAttribute, self).copy())

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__CubemapAttribute, self).compareTo(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def __init__(self, arg0: int, arg1: 'Cubemap'):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long,com.badlogic.gdx.graphics.Cubemap)"""
        val = __CubemapAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'TextureDescriptor'):
        """public <T extends com.badlogic.gdx.graphics.Cubemap> com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor<T>)"""
        val = __CubemapAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute.hashCode()"""
        return int.__wrap(super(CubemapAttribute, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'CubemapAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute)"""
        val = __CubemapAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.CubemapAttribute(long)"""
        val = __CubemapAttribute(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as __BlendingAttribute
__BlendingAttribute = __BlendingAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import int
 
class BlendingAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute"""
 
    @staticmethod
    def __wrap(java_value: __BlendingAttribute) -> 'BlendingAttribute':
        return BlendingAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BlendingAttribute):
        """
        Dynamic initializer for BlendingAttribute.
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
    def copy(self) -> 'BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.copy()"""
        return 'BlendingAttribute'.__wrap(super(BlendingAttribute, self).copy())

    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.hashCode()"""
        return int.__wrap(super(BlendingAttribute, self).hashCode())

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(float)"""
        val = __BlendingAttribute(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(int,int)"""
        val = __BlendingAttribute(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute()"""
        val = __BlendingAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: bool, arg1: int, arg2: int, arg3: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(boolean,int,int,float)"""
        val = __BlendingAttribute(__boolean.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

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
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(int,int,float)"""
        val = __BlendingAttribute(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute()"""
        val = __BlendingAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'BlendingAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute)"""
        val = __BlendingAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.is(long)"""
        return bool.__wrap(__BlendingAttribute.is(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def __init__(self, arg0: bool, arg1: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute(boolean,float)"""
        val = __BlendingAttribute(__boolean.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__BlendingAttribute, self).compareTo(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute as __ColorAttribute
__ColorAttribute = __ColorAttribute
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ColorAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute"""
 
    @staticmethod
    def __wrap(java_value: __ColorAttribute) -> 'ColorAttribute':
        return ColorAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorAttribute):
        """
        Dynamic initializer for ColorAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def createSpecular(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createSpecular(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createSpecular(arg0))

    @staticmethod
    @overload
    def createSpecular(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createSpecular(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createSpecular(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def createAmbient(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbient(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createAmbient(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long,float,float,float,float)"""
        val = __ColorAttribute(__long.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createDiffuse(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createDiffuse(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createDiffuse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createEmissive(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createEmissive(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createEmissive(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long,com.badlogic.gdx.graphics.Color)"""
        val = __ColorAttribute(__long.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createReflection(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createReflection(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createReflection(arg0))

    @staticmethod
    @overload
    def createReflection(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createReflection(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createReflection(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.hashCode()"""
        return int.__wrap(super(ColorAttribute, self).hashCode())

    @override
    @overload
    def copy(self) -> 'g3d.Attribute':
        """public com.badlogic.gdx.graphics.g3d.Attribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.copy()"""
        return 'g3d.Attribute'.__wrap(super(ColorAttribute, self).copy())

    @staticmethod
    @overload
    def createFog(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createFog(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createFog(arg0))

    @staticmethod
    @overload
    def createAmbientLight(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbientLight(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createAmbientLight(arg0))

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
    def __init__(self, arg0: 'ColorAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute)"""
        val = __ColorAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createDiffuse(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createDiffuse(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createDiffuse(arg0))

    @staticmethod
    @overload
    def createAmbientLight(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbientLight(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createAmbientLight(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def createFog(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createFog(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createFog(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__ColorAttribute, self).compareTo(arg0))

    @staticmethod
    @overload
    def createEmissive(arg0: 'Color') -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createEmissive(com.badlogic.gdx.graphics.Color)"""
        return ColorAttribute.__wrap(__ColorAttribute.createEmissive(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.is(long)"""
        return bool.__wrap(__ColorAttribute.is(__long.valueOf(arg0)))

    @staticmethod
    @overload
    def createAmbient(arg0: float, arg1: float, arg2: float, arg3: float) -> 'ColorAttribute':
        """public static final com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute.createAmbient(float,float,float,float)"""
        return ColorAttribute.__wrap(__ColorAttribute.createAmbient(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.attributes.ColorAttribute(long)"""
        val = __ColorAttribute(__long.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute as __PointLightsAttribute
__PointLightsAttribute = __PointLightsAttribute
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.Attribute as __Attribute
__Attribute = __Attribute
from builtins import int
 
class PointLightsAttribute(graphics.__Attribute, g3d.Attribute):
    """com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute"""
 
    @staticmethod
    def __wrap(java_value: __PointLightsAttribute) -> 'PointLightsAttribute':
        return PointLightsAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointLightsAttribute):
        """
        Dynamic initializer for PointLightsAttribute.
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
 
    @staticmethod
    @overload
    def getAttributeAlias(arg0: int) -> str:
        """public static final java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.getAttributeAlias(long)"""
        return str.__wrap(__Attribute.getAttributeAlias(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAttributeType(arg0: str) -> int:
        """public static final long com.badlogic.gdx.graphics.g3d.Attribute.getAttributeType(java.lang.String)"""
        return int.__wrap(__Attribute.getAttributeType(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'PointLightsAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.copy()"""
        return 'PointLightsAttribute'.__wrap(super(PointLightsAttribute, self).copy())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.Attribute.toString()"""
        return str.__wrap(super(g3d.Attribute, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute()"""
        val = __PointLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute()"""
        val = __PointLightsAttribute()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'PointLightsAttribute'):
        """public com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute(com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute)"""
        val = __PointLightsAttribute(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.hashCode()"""
        return int.__wrap(super(PointLightsAttribute, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def is(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.is(long)"""
        return bool.__wrap(__PointLightsAttribute.is(__long.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.Attribute.equals(java.lang.Object)"""
        return bool.__wrap(super(__g3d.Attribute, self).equals(arg0))

    @overload
    def compareTo(self, arg0: 'Attribute') -> int:
        """public int com.badlogic.gdx.graphics.g3d.attributes.PointLightsAttribute.compareTo(com.badlogic.gdx.graphics.g3d.Attribute)"""
        return int.__wrap(super(__PointLightsAttribute, self).compareTo(arg0))