from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import space.earlygrey.shapedrawer.JoinType as __JoinType
__JoinType = __JoinType
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class JoinType(__Enum, Enum):
    """space.earlygrey.shapedrawer.JoinType"""
 
    @staticmethod
    def __wrap(java_value: __JoinType) -> 'JoinType':
        return JoinType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JoinType):
        """
        Dynamic initializer for JoinType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['JoinType']:
        """public static space.earlygrey.shapedrawer.JoinType[] space.earlygrey.shapedrawer.JoinType.values()"""
        return List[JoinType].__wrap(__JoinType.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JoinType':
        """public static space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.JoinType.valueOf(java.lang.String)"""
        return JoinType.__wrap(__JoinType.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

 
 
 
# CLASS: space.earlygrey.shapedrawer.JoinType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import space.earlygrey.shapedrawer.JoinType as __JoinType
__JoinType = __JoinType
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class JoinType(__Enum, Enum):
    """space.earlygrey.shapedrawer.JoinType"""
 
    @staticmethod
    def __wrap(java_value: __JoinType) -> 'JoinType':
        return JoinType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JoinType):
        """
        Dynamic initializer for JoinType.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['JoinType']:
        """public static space.earlygrey.shapedrawer.JoinType[] space.earlygrey.shapedrawer.JoinType.values()"""
        return List[JoinType].__wrap(__JoinType.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JoinType':
        """public static space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.JoinType.valueOf(java.lang.String)"""
        return JoinType.__wrap(__JoinType.valueOf(arg0))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

 
 
 
# CLASS: space.earlygrey.shapedrawer.JoinType 
 
 
# CLASS: space.earlygrey.shapedrawer.Drawing
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import space.earlygrey.shapedrawer.Drawing as __Drawing
__Drawing = __Drawing
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Drawing():
    """space.earlygrey.shapedrawer.Drawing"""
 
    @staticmethod
    def __wrap(java_value: __Drawing) -> 'Drawing':
        return Drawing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Drawing):
        """
        Dynamic initializer for Drawing.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def draw(self):
        """public void space.earlygrey.shapedrawer.Drawing.draw()"""
        super(Drawing, self).draw()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: space.earlygrey.shapedrawer.ShapeUtils
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import space.earlygrey.shapedrawer.ShapeUtils as __ShapeUtils
__ShapeUtils = __ShapeUtils
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ShapeUtils():
    """space.earlygrey.shapedrawer.ShapeUtils"""
 
    @staticmethod
    def __wrap(java_value: __ShapeUtils) -> 'ShapeUtils':
        return ShapeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeUtils):
        """
        Dynamic initializer for ShapeUtils.
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
    def epsilonEquals(arg0: float, arg1: float) -> bool:
        """public static boolean space.earlygrey.shapedrawer.ShapeUtils.epsilonEquals(float,float)"""
        return bool.__wrap(__ShapeUtils.epsilonEquals(__float.valueOf(arg0), __float.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.ShapeUtils()"""
        val = __ShapeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def floor(arg0: float, arg1: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.floor(float,float)"""
        return float.__wrap(__ShapeUtils.floor(__float.valueOf(arg0), __float.valueOf(arg1)))

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

    @staticmethod
    @overload
    def angleRad(arg0: 'Vector2', arg1: 'Vector2') -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.angleRad(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float.__wrap(__ShapeUtils.angleRad(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.ShapeUtils()"""
        val = __ShapeUtils()
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

    @staticmethod
    @overload
    def snap(arg0: float, arg1: float, arg2: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.snap(float,float,float)"""
        return float.__wrap(__ShapeUtils.snap(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @staticmethod
    @overload
    def ceil(arg0: float, arg1: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.ceil(float,float)"""
        return float.__wrap(__ShapeUtils.ceil(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def normaliseAngleToPositive(arg0: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.normaliseAngleToPositive(float)"""
        return float.__wrap(__ShapeUtils.normaliseAngleToPositive(__float.valueOf(arg0))) 
 
 
# CLASS: space.earlygrey.shapedrawer.AbstractShapeDrawer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import space.earlygrey.shapedrawer.Drawing as __Drawing
__Drawing = __Drawing
from builtins import float
import space.earlygrey.shapedrawer.AbstractShapeDrawer as __AbstractShapeDrawer
__AbstractShapeDrawer = __AbstractShapeDrawer
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import space.earlygrey.shapedrawer.SideEstimator as __SideEstimator
__SideEstimator = __SideEstimator
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class AbstractShapeDrawer(ABC):
    """space.earlygrey.shapedrawer.AbstractShapeDrawer"""
 
    @staticmethod
    def __wrap(java_value: __AbstractShapeDrawer) -> 'AbstractShapeDrawer':
        return AbstractShapeDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractShapeDrawer):
        """
        Dynamic initializer for AbstractShapeDrawer.
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
    def getSideEstimator(self) -> 'SideEstimator':
        """public final space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.getSideEstimator()"""
        return 'SideEstimator'.__wrap(super(AbstractShapeDrawer, self).getSideEstimator())

    @overload
    def update(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update()"""
        super(AbstractShapeDrawer, self).update()

    @overload
    def setDefaultSnap(self, arg0: bool) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultSnap(boolean)"""
        return bool.__wrap(super(__AbstractShapeDrawer, self).setDefaultSnap(__boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'g2d.TextureRegion'.__wrap(super(__AbstractShapeDrawer, self).setTextureRegion(arg0))

    @overload
    def getDefaultLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getDefaultLineWidth()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getDefaultLineWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float,float,float,float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch space.earlygrey.shapedrawer.AbstractShapeDrawer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(AbstractShapeDrawer, self).getBatch())

    @overload
    def stopRecording(self) -> 'Drawing':
        """public space.earlygrey.shapedrawer.Drawing space.earlygrey.shapedrawer.AbstractShapeDrawer.stopRecording()"""
        return 'Drawing'.__wrap(super(AbstractShapeDrawer, self).stopRecording())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isDefaultSnap(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.isDefaultSnap()"""
        return bool.__wrap(super(AbstractShapeDrawer, self).isDefaultSnap())

    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPackedColor()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getPackedColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def updatePixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.updatePixelSize()"""
        return float.__wrap(super(AbstractShapeDrawer, self).updatePixelSize())

    @overload
    def getPixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPixelSize()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getPixelSize())

    @overload
    def update(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update(boolean)"""
        super(__AbstractShapeDrawer, self).update(__boolean.valueOf(arg0))

    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.getRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(AbstractShapeDrawer, self).getRegion())

    @overload
    def startRecording(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.startRecording()"""
        super(AbstractShapeDrawer, self).startRecording()

    @overload
    def setDefaultLineWidth(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultLineWidth(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setDefaultLineWidth(__float.valueOf(arg0)))

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
    def setColor(self, arg0: 'Color') -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(com.badlogic.gdx.graphics.Color)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSideEstimator(self, arg0: 'SideEstimator') -> 'SideEstimator':
        """public space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.setSideEstimator(space.earlygrey.shapedrawer.SideEstimator)"""
        return 'SideEstimator'.__wrap(super(__AbstractShapeDrawer, self).setSideEstimator(arg0))

    @overload
    def setPixelSize(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setPixelSize(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setPixelSize(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(__float.valueOf(arg0))) 
 
 
# CLASS: space.earlygrey.shapedrawer.SideEstimator
import space.earlygrey.shapedrawer.SideEstimator as __SideEstimator
__SideEstimator = __SideEstimator
from abc import abstractmethod, ABC
 
class SideEstimator(ABC):
    """space.earlygrey.shapedrawer.SideEstimator"""
 
    @staticmethod
    def __wrap(java_value: __SideEstimator) -> 'SideEstimator':
        return SideEstimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SideEstimator):
        """
        Dynamic initializer for SideEstimator.
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
    def estimateSidesRequired(self, arg0: float, arg1: float, arg2: float):
        """public abstract int space.earlygrey.shapedrawer.SideEstimator.estimateSidesRequired(float,float,float)"""
        pass 
 
 
# CLASS: space.earlygrey.shapedrawer.ShapeDrawer
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import space.earlygrey.shapedrawer.Drawing as __Drawing
__Drawing = __Drawing
from builtins import float
import space.earlygrey.shapedrawer.AbstractShapeDrawer as __AbstractShapeDrawer
__AbstractShapeDrawer = __AbstractShapeDrawer
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
import space.earlygrey.shapedrawer.SideEstimator as __SideEstimator
__SideEstimator = __SideEstimator
import java.lang.Object as __Object
__Object = __Object
import space.earlygrey.shapedrawer.ShapeDrawer as __ShapeDrawer
__ShapeDrawer = __ShapeDrawer
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ShapeDrawer(__AbstractShapeDrawer, AbstractShapeDrawer):
    """space.earlygrey.shapedrawer.ShapeDrawer"""
 
    @staticmethod
    def __wrap(java_value: __ShapeDrawer) -> 'ShapeDrawer':
        return ShapeDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeDrawer):
        """
        Dynamic initializer for ShapeDrawer.
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
    def polygon(self, arg0: 'Polygon', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float)"""
        super(__ShapeDrawer, self).polygon(arg0, __float.valueOf(arg1))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __float.valueOf(arg5))

    @overload
    def setDefaultSnap(self, arg0: bool) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultSnap(boolean)"""
        return bool.__wrap(super(__AbstractShapeDrawer, self).setDefaultSnap(__boolean.valueOf(arg0)))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).triangle(arg0, arg1, arg2, arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float)"""
        super(__ShapeDrawer, self).filledEllipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledPolygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float)"""
        super(__ShapeDrawer, self).sector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.getRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(AbstractShapeDrawer, self).getRegion())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float,float,float,float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(__ShapeDrawer, self).triangle(arg0, arg1, arg2, __float.valueOf(arg3))

    @overload
    def triangles(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangles(float[],short[],float,float)"""
        super(__ShapeDrawer, self).triangles(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float)"""
        super(__ShapeDrawer, self).polygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(__ShapeDrawer, self).line(arg0, arg1, __float.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(arg0, __float.valueOf(arg1), arg2, arg3)

    @overload
    def polygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon)"""
        super(__ShapeDrawer, self).polygon(arg0)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, __float.valueOf(arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5), arg6, arg7)

    @overload
    def path(self, arg0: 'FloatArray', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.FloatArray,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6)

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float)"""
        super(__ShapeDrawer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,float)"""
        super(__ShapeDrawer, self).line(arg0, arg1, arg2, __float.valueOf(arg3))

    @overload
    def polygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[])"""
        super(__ShapeDrawer, self).polygon(arg0)

    @overload
    def setColor(self, arg0: 'Color') -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(com.badlogic.gdx.graphics.Color)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(arg0))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,float)"""
        super(__ShapeDrawer, self).rectangle(arg0, arg1, __float.valueOf(arg2))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[])"""
        super(__ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6)

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledTriangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPixelSize(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setPixelSize(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setPixelSize(__float.valueOf(arg0)))

    @overload
    def path(self, arg0: 'Array', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float)"""
        super(__ShapeDrawer, self).path(arg0, __float.valueOf(arg1))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color', arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6)

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion', arg2: 'SideEstimator'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion,space.earlygrey.shapedrawer.SideEstimator)"""
        val = __ShapeDrawer(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3)

    @overload
    def path(self, arg0: 'float', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6)

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,short[])"""
        super(__ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledPolygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7)

    @overload
    def polygon(self, arg0: 'float', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(arg0, __float.valueOf(arg1), arg2)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6)

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int)"""
        super(__ShapeDrawer, self).sector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5))

    @override
    @overload
    def update(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update(boolean)"""
        super(__AbstractShapeDrawer, self).update(__boolean.valueOf(arg0))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float)"""
        super(__ShapeDrawer, self).filledPolygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(arg0, arg1, arg2)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6, arg7, arg8)

    @override
    @overload
    def getSideEstimator(self) -> 'SideEstimator':
        """public final space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.getSideEstimator()"""
        return 'SideEstimator'.__wrap(super(AbstractShapeDrawer, self).getSideEstimator())

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledTriangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean)"""
        super(__ShapeDrawer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __boolean.valueOf(arg6))

    @overload
    def __init__(self, arg0: 'Batch'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch)"""
        val = __ShapeDrawer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def rectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle)"""
        super(__ShapeDrawer, self).rectangle(arg0)

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __ShapeDrawer(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update()"""
        super(AbstractShapeDrawer, self).update()

    @override
    @overload
    def getDefaultLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getDefaultLineWidth()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getDefaultLineWidth())

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float, arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledCircle(arg0, __float.valueOf(arg1), arg2)

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float)"""
        super(__ShapeDrawer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(arg0, arg1)

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3, arg4, arg5)

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color', arg3: 'Color', arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(arg0, arg1, arg2, arg3, arg4)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(arg0, __float.valueOf(arg1), arg2)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType', arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(__ShapeDrawer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), arg7, __float.valueOf(arg8))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5))

    @overload
    def path(self, arg0: 'Array', arg1: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __boolean.valueOf(arg1))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledEllipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def filledPolygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon)"""
        super(__ShapeDrawer, self).filledPolygon(arg0)

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'g2d.TextureRegion'.__wrap(super(__AbstractShapeDrawer, self).setTextureRegion(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,float)"""
        super(__ShapeDrawer, self).triangle(arg0, arg1, arg2, __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float)"""
        super(__ShapeDrawer, self).filledPolygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPackedColor()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getPackedColor())

    @override
    @overload
    def updatePixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.updatePixelSize()"""
        return float.__wrap(super(AbstractShapeDrawer, self).updatePixelSize())

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch space.earlygrey.shapedrawer.AbstractShapeDrawer.getBatch()"""
        return 'g2d.Batch'.__wrap(super(AbstractShapeDrawer, self).getBatch())

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType', arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4, __boolean.valueOf(arg5))

    @overload
    def filledPolygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[])"""
        super(__ShapeDrawer, self).filledPolygon(arg0)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), arg4)

    @override
    @overload
    def stopRecording(self) -> 'Drawing':
        """public space.earlygrey.shapedrawer.Drawing space.earlygrey.shapedrawer.AbstractShapeDrawer.stopRecording()"""
        return 'Drawing'.__wrap(super(AbstractShapeDrawer, self).stopRecording())

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledRectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[],float,float)"""
        super(__ShapeDrawer, self).filledPolygon(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).filledEllipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __float.valueOf(arg1), __boolean.valueOf(arg2))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float)"""
        super(__ShapeDrawer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,float,float)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __boolean.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @overload
    def setDefaultLineWidth(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultLineWidth(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setDefaultLineWidth(__float.valueOf(arg0)))

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float, arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledCircle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int,float,float)"""
        super(__ShapeDrawer, self).sector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @override
    @overload
    def startRecording(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.startRecording()"""
        super(AbstractShapeDrawer, self).startRecording()

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledTriangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def path(self, arg0: 'Array'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>)"""
        super(__ShapeDrawer, self).path(arg0)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: 'JoinType', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(__ShapeDrawer, self).triangle(arg0, arg1, arg2, __float.valueOf(arg3), arg4, __float.valueOf(arg5))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float)"""
        super(__ShapeDrawer, self).ellipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).sector(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6)

    @override
    @overload
    def getPixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPixelSize()"""
        return float.__wrap(super(AbstractShapeDrawer, self).getPixelSize())

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __boolean.valueOf(arg4))

    @override
    @overload
    def isDefaultSnap(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.isDefaultSnap()"""
        return bool.__wrap(super(AbstractShapeDrawer, self).isDefaultSnap())

    @overload
    def setSideEstimator(self, arg0: 'SideEstimator') -> 'SideEstimator':
        """public space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.setSideEstimator(space.earlygrey.shapedrawer.SideEstimator)"""
        return 'SideEstimator'.__wrap(super(__AbstractShapeDrawer, self).setSideEstimator(arg0))

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).path(arg0, arg1)

    @overload
    def setColor(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float)"""
        return float.__wrap(super(__AbstractShapeDrawer, self).setColor(__float.valueOf(arg0)))

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],com.badlogic.gdx.utils.ShortArray)"""
        super(__ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float)"""
        super(__ShapeDrawer, self).circle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__ShapeDrawer, self).triangle(arg0, arg1, arg2)

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__ShapeDrawer, self).filledTriangle(arg0, arg1, arg2)

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool, arg7: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean,int)"""
        super(__ShapeDrawer, self).arc(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __boolean.valueOf(arg6), __int.valueOf(arg7))

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(__ShapeDrawer, self).path(arg0, __float.valueOf(arg1), arg2, __boolean.valueOf(arg3))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float)"""
        super(__ShapeDrawer, self).triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledRectangle(arg0, __float.valueOf(arg1), arg2, arg3, arg4, arg5)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(arg0, arg1)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), arg4)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(__ShapeDrawer, self).line(arg0, arg1)

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).rectangle(arg0, arg1)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: int, arg2: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],int,int)"""
        super(__ShapeDrawer, self).filledPolygon(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledEllipse(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, arg6)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).line(arg0, arg1, arg2, arg3)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float)"""
        super(__ShapeDrawer, self).filledPolygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float)"""
        super(__ShapeDrawer, self).filledCircle(arg0, __float.valueOf(arg1))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).rectangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5)

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType', arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(__ShapeDrawer, self).path(arg0, arg1, __boolean.valueOf(arg2))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__ShapeDrawer, self).polygon(__float.valueOf(arg0), __float.valueOf(arg1), __int.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), arg7)

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.utils.ShortArray)"""
        super(__ShapeDrawer, self).filledPolygon(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def filledRectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle)"""
        super(__ShapeDrawer, self).filledRectangle(arg0)

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float)"""
        super(__ShapeDrawer, self).filledCircle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(__ShapeDrawer, self).filledTriangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), arg6)

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,float)"""
        super(__ShapeDrawer, self).rectangle(arg0, __float.valueOf(arg1)) 
 
 
# CLASS: space.earlygrey.shapedrawer.GraphDrawer
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
import space.earlygrey.shapedrawer.GraphDrawer as __GraphDrawer
__GraphDrawer = __GraphDrawer
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import space.earlygrey.shapedrawer.ShapeDrawer as __ShapeDrawer
__ShapeDrawer = __ShapeDrawer
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import space.earlygrey.shapedrawer.JoinType as __JoinType
__JoinType = __JoinType
from builtins import bool
from builtins import int
 
class GraphDrawer():
    """space.earlygrey.shapedrawer.GraphDrawer"""
 
    @staticmethod
    def __wrap(java_value: __GraphDrawer) -> 'GraphDrawer':
        return GraphDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphDrawer):
        """
        Dynamic initializer for GraphDrawer.
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
    def draw(self, arg0: 'Interpolation', arg1: 'Rectangle', arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,com.badlogic.gdx.math.Rectangle,space.earlygrey.shapedrawer.JoinType)"""
        super(__GraphDrawer, self).draw(arg0, arg1, arg2)

    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(__GraphDrawer, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5)

    @overload
    def getJoinType(self) -> 'JoinType':
        """public space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.GraphDrawer.getJoinType()"""
        return 'JoinType'.__wrap(super(GraphDrawer, self).getJoinType())

    @overload
    def getShapeDrawer(self) -> 'ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.GraphDrawer.getShapeDrawer()"""
        return 'ShapeDrawer'.__wrap(super(GraphDrawer, self).getShapeDrawer())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDomainBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getDomainBegin()"""
        return float.__wrap(super(GraphDrawer, self).getDomainBegin())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public space.earlygrey.shapedrawer.GraphDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = __GraphDrawer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPlotEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getPlotEnd()"""
        return float.__wrap(super(GraphDrawer, self).getPlotEnd())

    @overload
    def getPlotBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getPlotBegin()"""
        return float.__wrap(super(GraphDrawer, self).getPlotBegin())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setPlotEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setPlotEnd(float)"""
        super(__GraphDrawer, self).setPlotEnd(__float.valueOf(arg0))

    @overload
    def setJoinType(self, arg0: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setJoinType(space.earlygrey.shapedrawer.JoinType)"""
        super(__GraphDrawer, self).setJoinType(arg0)

    @overload
    def setDomainEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setDomainEnd(float)"""
        super(__GraphDrawer, self).setDomainEnd(__float.valueOf(arg0))

    @overload
    def getSamples(self) -> int:
        """public int space.earlygrey.shapedrawer.GraphDrawer.getSamples()"""
        return int.__wrap(super(GraphDrawer, self).getSamples())

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
    def setRescale(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setRescale(boolean)"""
        super(__GraphDrawer, self).setRescale(__boolean.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Interpolation', arg1: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,com.badlogic.gdx.math.Rectangle)"""
        super(__GraphDrawer, self).draw(arg0, arg1)

    @overload
    def isRescale(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.GraphDrawer.isRescale()"""
        return bool.__wrap(super(GraphDrawer, self).isRescale())

    @overload
    def setDomainBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setDomainBegin(float)"""
        super(__GraphDrawer, self).setDomainBegin(__float.valueOf(arg0))

    @overload
    def getDomainEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getDomainEnd()"""
        return float.__wrap(super(GraphDrawer, self).getDomainEnd())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSamples(self, arg0: int):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setSamples(int)"""
        super(__GraphDrawer, self).setSamples(__int.valueOf(arg0))

    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(__GraphDrawer, self).setShapeDrawer(arg0)

    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType', arg6: int, arg7: float, arg8: float, arg9: float, arg10: float, arg11: bool):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float,space.earlygrey.shapedrawer.JoinType,int,float,float,float,float,boolean)"""
        super(__GraphDrawer, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), arg5, __int.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __float.valueOf(arg10), __boolean.valueOf(arg11))

    @overload
    def setPlotBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setPlotBegin(float)"""
        super(__GraphDrawer, self).setPlotBegin(__float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float)"""
        super(__GraphDrawer, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)) 
 
 
# CLASS: space.earlygrey.shapedrawer.DefaultSideEstimator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import space.earlygrey.shapedrawer.DefaultSideEstimator as __DefaultSideEstimator
__DefaultSideEstimator = __DefaultSideEstimator
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultSideEstimator(__SideEstimator, SideEstimator):
    """space.earlygrey.shapedrawer.DefaultSideEstimator"""
 
    @staticmethod
    def __wrap(java_value: __DefaultSideEstimator) -> 'DefaultSideEstimator':
        return DefaultSideEstimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultSideEstimator):
        """
        Dynamic initializer for DefaultSideEstimator.
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
    def setSideMultiplier(self, arg0: float):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setSideMultiplier(float)"""
        super(__DefaultSideEstimator, self).setSideMultiplier(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def estimateSidesRequired(self, arg0: float, arg1: float, arg2: float) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.estimateSidesRequired(float,float,float)"""
        return int.__wrap(super(__DefaultSideEstimator, self).estimateSidesRequired(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator()"""
        val = __DefaultSideEstimator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMaximumSides(self) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.getMaximumSides()"""
        return int.__wrap(super(DefaultSideEstimator, self).getMaximumSides())

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator()"""
        val = __DefaultSideEstimator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getMinimumSides(self) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.getMinimumSides()"""
        return int.__wrap(super(DefaultSideEstimator, self).getMinimumSides())

    @overload
    def getSideMultiplier(self) -> float:
        """public float space.earlygrey.shapedrawer.DefaultSideEstimator.getSideMultiplier()"""
        return float.__wrap(super(DefaultSideEstimator, self).getSideMultiplier())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setMinimumSides(self, arg0: int):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setMinimumSides(int)"""
        super(__DefaultSideEstimator, self).setMinimumSides(__int.valueOf(arg0))

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

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator(int,int,float)"""
        val = __DefaultSideEstimator(__int.valueOf(arg0), __int.valueOf(arg1), __float.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setMaximumSides(self, arg0: int):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setMaximumSides(int)"""
        super(__DefaultSideEstimator, self).setMaximumSides(__int.valueOf(arg0))