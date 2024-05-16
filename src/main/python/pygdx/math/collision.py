from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class BoundingBox():
    """com.badlogic.gdx.math.collision.BoundingBox"""
 
    @staticmethod
    def __wrap(java_value: __BoundingBox) -> 'BoundingBox':
        return BoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundingBox):
        """
        Dynamic initializer for BoundingBox.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.intersects(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).intersects(arg0))

    @overload
    def getCenterX(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterX()"""
        return float.__wrap(super(BoundingBox, self).getCenterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def contains(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def contains(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def ext(self, arg0: 'Vector3', arg1: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3,float)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0, __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getMin(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMin(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getMin(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.BoundingBox.toString()"""
        return str.__wrap(super(BoundingBox, self).toString())

    @overload
    def getCorner100(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner100(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner100(arg0))

    @overload
    def getCorner101(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner101(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner101(arg0))

    @overload
    def getCenterZ(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterZ()"""
        return float.__wrap(super(BoundingBox, self).getCenterZ())

    @overload
    def clr(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.clr()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).clr())

    @overload
    def getCorner001(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner001(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner001(arg0))

    @overload
    def getDimensions(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getDimensions(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getDimensions(arg0))

    @overload
    def getCorner000(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner000(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner000(arg0))

    @overload
    def mul(self, arg0: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).mul(arg0))

    @overload
    def getCenterY(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterY()"""
        return float.__wrap(super(BoundingBox, self).getCenterY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: 'List') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(java.util.List<com.badlogic.gdx.math.Vector3>)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getWidth()"""
        return float.__wrap(super(BoundingBox, self).getWidth())

    @overload
    def ext(self, arg0: 'BoundingBox', arg1: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3[])"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getMax(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMax(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getMax(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ext(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        val = __BoundingBox(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCorner011(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner011(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner011(arg0))

    @overload
    def getCorner010(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner010(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner010(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0, arg1))

    @overload
    def inf(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.inf()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).inf())

    @overload
    def isValid(self) -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.isValid()"""
        return bool.__wrap(super(BoundingBox, self).isValid())

    @overload
    def getDepth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getDepth()"""
        return float.__wrap(super(BoundingBox, self).getDepth())

    @overload
    def getCorner110(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner110(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner110(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getCorner111(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner111(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner111(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __BoundingBox(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self):
        """public void com.badlogic.gdx.math.collision.BoundingBox.update()"""
        super(BoundingBox, self).update()

    @overload
    def ext(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @overload
    def ext(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(float,float,float)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getHeight()"""
        return float.__wrap(super(BoundingBox, self).getHeight())

    @overload
    def getCenter(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCenter(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCenter(arg0))

 
 
 
# CLASS: com.badlogic.gdx.math.collision.BoundingBox
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class BoundingBox():
    """com.badlogic.gdx.math.collision.BoundingBox"""
 
    @staticmethod
    def __wrap(java_value: __BoundingBox) -> 'BoundingBox':
        return BoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BoundingBox):
        """
        Dynamic initializer for BoundingBox.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.intersects(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).intersects(arg0))

    @overload
    def getCenterX(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterX()"""
        return float.__wrap(super(BoundingBox, self).getCenterX())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def contains(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def contains(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @overload
    def ext(self, arg0: 'Vector3', arg1: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3,float)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0, __float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getMin(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMin(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getMin(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.BoundingBox.toString()"""
        return str.__wrap(super(BoundingBox, self).toString())

    @overload
    def getCorner100(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner100(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner100(arg0))

    @overload
    def getCorner101(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner101(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner101(arg0))

    @overload
    def getCenterZ(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterZ()"""
        return float.__wrap(super(BoundingBox, self).getCenterZ())

    @overload
    def clr(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.clr()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).clr())

    @overload
    def getCorner001(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner001(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner001(arg0))

    @overload
    def getDimensions(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getDimensions(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getDimensions(arg0))

    @overload
    def getCorner000(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner000(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner000(arg0))

    @overload
    def mul(self, arg0: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).mul(arg0))

    @overload
    def getCenterY(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getCenterY()"""
        return float.__wrap(super(BoundingBox, self).getCenterY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def set(self, arg0: 'List') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(java.util.List<com.badlogic.gdx.math.Vector3>)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getWidth()"""
        return float.__wrap(super(BoundingBox, self).getWidth())

    @overload
    def ext(self, arg0: 'BoundingBox', arg1: 'Matrix4') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3[])"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def getMax(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getMax(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getMax(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def ext(self, arg0: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        val = __BoundingBox(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCorner011(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner011(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner011(arg0))

    @overload
    def getCorner010(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner010(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner010(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0, arg1))

    @overload
    def inf(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.inf()"""
        return 'BoundingBox'.__wrap(super(BoundingBox, self).inf())

    @overload
    def isValid(self) -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.isValid()"""
        return bool.__wrap(super(BoundingBox, self).isValid())

    @overload
    def getDepth(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getDepth()"""
        return float.__wrap(super(BoundingBox, self).getDepth())

    @overload
    def getCorner110(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner110(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner110(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def set(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.set(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).set(arg0))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.BoundingBox.contains(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__BoundingBox, self).contains(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getCorner111(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCorner111(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCorner111(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.BoundingBox()"""
        val = __BoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.BoundingBox(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __BoundingBox(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self):
        """public void com.badlogic.gdx.math.collision.BoundingBox.update()"""
        super(BoundingBox, self).update()

    @overload
    def ext(self, arg0: 'BoundingBox') -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(com.badlogic.gdx.math.collision.BoundingBox)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(arg0))

    @overload
    def ext(self, arg0: float, arg1: float, arg2: float) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.BoundingBox.ext(float,float,float)"""
        return 'BoundingBox'.__wrap(super(__BoundingBox, self).ext(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.collision.BoundingBox.getHeight()"""
        return float.__wrap(super(BoundingBox, self).getHeight())

    @overload
    def getCenter(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.BoundingBox.getCenter(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__BoundingBox, self).getCenter(arg0))

 
 
 
# CLASS: com.badlogic.gdx.math.collision.BoundingBox 
 
 
# CLASS: com.badlogic.gdx.math.collision.OrientedBoundingBox
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from typing import List
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import com.badlogic.gdx.math.collision.OrientedBoundingBox as __OrientedBoundingBox
__OrientedBoundingBox = __OrientedBoundingBox
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OrientedBoundingBox():
    """com.badlogic.gdx.math.collision.OrientedBoundingBox"""
 
    @staticmethod
    def __wrap(java_value: __OrientedBoundingBox) -> 'OrientedBoundingBox':
        return OrientedBoundingBox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OrientedBoundingBox):
        """
        Dynamic initializer for OrientedBoundingBox.
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
    def getCorner001(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner001(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner001(arg0))

    @overload
    def set(self, arg0: 'BoundingBox', arg1: 'Matrix4') -> 'OrientedBoundingBox':
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox com.badlogic.gdx.math.collision.OrientedBoundingBox.set(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        return 'OrientedBoundingBox'.__wrap(super(__OrientedBoundingBox, self).set(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getCorner010(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner010(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner010(arg0))

    @overload
    def __init__(self, arg0: 'BoundingBox'):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox(com.badlogic.gdx.math.collision.BoundingBox)"""
        val = __OrientedBoundingBox(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCorner100(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner100(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner100(arg0))

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
    def contains(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(super(__OrientedBoundingBox, self).contains(arg0))

    @overload
    def getCorner011(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner011(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner011(arg0))

    @overload
    def __init__(self, arg0: 'BoundingBox', arg1: 'Matrix4'):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox(com.badlogic.gdx.math.collision.BoundingBox,com.badlogic.gdx.math.Matrix4)"""
        val = __OrientedBoundingBox(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def contains(self, arg0: 'Vector3') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__OrientedBoundingBox, self).contains(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def contains(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.contains(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__OrientedBoundingBox, self).contains(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getBounds(self) -> 'BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.math.collision.OrientedBoundingBox.getBounds()"""
        return 'BoundingBox'.__wrap(super(OrientedBoundingBox, self).getBounds())

    @overload
    def intersects(self, arg0: 'OrientedBoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.intersects(com.badlogic.gdx.math.collision.OrientedBoundingBox)"""
        return bool.__wrap(super(__OrientedBoundingBox, self).intersects(arg0))

    @overload
    def getTransform(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.math.collision.OrientedBoundingBox.getTransform()"""
        return 'math.Matrix4'.__wrap(super(OrientedBoundingBox, self).getTransform())

    @overload
    def getCorner110(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner110(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner110(arg0))

    @overload
    def setBounds(self, arg0: 'BoundingBox'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.setBounds(com.badlogic.gdx.math.collision.BoundingBox)"""
        super(__OrientedBoundingBox, self).setBounds(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getCorner101(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner101(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner101(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getCorner111(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner111(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner111(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox()"""
        val = __OrientedBoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.mul(com.badlogic.gdx.math.Matrix4)"""
        super(__OrientedBoundingBox, self).mul(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.OrientedBoundingBox()"""
        val = __OrientedBoundingBox()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getVertices(self) -> List['math.Vector3']:
        """public com.badlogic.gdx.math.Vector3[] com.badlogic.gdx.math.collision.OrientedBoundingBox.getVertices()"""
        return List['math.Vector3'].__wrap(super(OrientedBoundingBox, self).getVertices())

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.math.collision.OrientedBoundingBox.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__OrientedBoundingBox, self).setTransform(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getCorner000(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.OrientedBoundingBox.getCorner000(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__OrientedBoundingBox, self).getCorner000(arg0))

    @overload
    def intersects(self, arg0: 'BoundingBox') -> bool:
        """public boolean com.badlogic.gdx.math.collision.OrientedBoundingBox.intersects(com.badlogic.gdx.math.collision.BoundingBox)"""
        return bool.__wrap(super(__OrientedBoundingBox, self).intersects(arg0)) 
 
 
# CLASS: com.badlogic.gdx.math.collision.Sphere
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.math.collision.Sphere as __Sphere
__Sphere = __Sphere
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class Sphere():
    """com.badlogic.gdx.math.collision.Sphere"""
 
    @staticmethod
    def __wrap(java_value: __Sphere) -> 'Sphere':
        return Sphere(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sphere):
        """
        Dynamic initializer for Sphere.
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
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Sphere.equals(java.lang.Object)"""
        return bool.__wrap(super(__Sphere, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def overlaps(self, arg0: 'Sphere') -> bool:
        """public boolean com.badlogic.gdx.math.collision.Sphere.overlaps(com.badlogic.gdx.math.collision.Sphere)"""
        return bool.__wrap(super(__Sphere, self).overlaps(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Sphere.hashCode()"""
        return int.__wrap(super(Sphere, self).hashCode())

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
    def __init__(self, arg0: 'Vector3', arg1: float):
        """public com.badlogic.gdx.math.collision.Sphere(com.badlogic.gdx.math.Vector3,float)"""
        val = __Sphere(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def volume(self) -> float:
        """public float com.badlogic.gdx.math.collision.Sphere.volume()"""
        return float.__wrap(super(Sphere, self).volume())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def surfaceArea(self) -> float:
        """public float com.badlogic.gdx.math.collision.Sphere.surfaceArea()"""
        return float.__wrap(super(Sphere, self).surfaceArea()) 
 
 
# CLASS: com.badlogic.gdx.math.collision.Segment
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.collision.Segment as __Segment
__Segment = __Segment
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

from builtins import bool
from builtins import int
 
class Segment():
    """com.badlogic.gdx.math.collision.Segment"""
 
    @staticmethod
    def __wrap(java_value: __Segment) -> 'Segment':
        return Segment(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Segment):
        """
        Dynamic initializer for Segment.
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
    def len2(self) -> float:
        """public float com.badlogic.gdx.math.collision.Segment.len2()"""
        return float.__wrap(super(Segment, self).len2())

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

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Segment.hashCode()"""
        return int.__wrap(super(Segment, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Segment.equals(java.lang.Object)"""
        return bool.__wrap(super(__Segment, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.Segment(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __Segment(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public com.badlogic.gdx.math.collision.Segment(float,float,float,float,float,float)"""
        val = __Segment(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def len(self) -> float:
        """public float com.badlogic.gdx.math.collision.Segment.len()"""
        return float.__wrap(super(Segment, self).len()) 
 
 
# CLASS: com.badlogic.gdx.math.collision.Ray
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.Ray as __Ray
__Ray = __Ray
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Ray():
    """com.badlogic.gdx.math.collision.Ray"""
 
    @staticmethod
    def __wrap(java_value: __Ray) -> 'Ray':
        return Ray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Ray):
        """
        Dynamic initializer for Ray.
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
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.collision.Ray.hashCode()"""
        return int.__wrap(super(Ray, self).hashCode())

    @overload
    def set(self, arg0: 'Ray') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.collision.Ray)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.collision.Ray.toString()"""
        return str.__wrap(super(Ray, self).toString())

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        return 'Ray'.__wrap(super(__Ray, self).set(arg0, arg1))

    @overload
    def getEndPoint(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.math.collision.Ray.getEndPoint(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__Ray, self).getEndPoint(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public com.badlogic.gdx.math.collision.Ray(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        val = __Ray(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.collision.Ray.equals(java.lang.Object)"""
        return bool.__wrap(super(__Ray, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def mul(self, arg0: 'Matrix4') -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.mul(com.badlogic.gdx.math.Matrix4)"""
        return 'Ray'.__wrap(super(__Ray, self).mul(arg0))

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
    def __init__(self, ):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = __Ray()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.set(float,float,float,float,float,float)"""
        return 'Ray'.__wrap(super(__Ray, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def cpy(self) -> 'Ray':
        """public com.badlogic.gdx.math.collision.Ray com.badlogic.gdx.math.collision.Ray.cpy()"""
        return 'Ray'.__wrap(super(Ray, self).cpy())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.math.collision.Ray()"""
        val = __Ray()
        self.__dict__ = val.__dict__
        self.__wrapper = val